"""Simulation experiment of the study Lennard1982."""

from typing import ClassVar, override

import pandas as pd
from pkpdsim.metadata import (
    ApplicationForm,
    Dosing,
    Fasting,
    Health,
    Phenotype,
    PKPDData,
    PKPDMappingMetaData,
    Route,
    Tissue,
)
from sbmlsim import Q
from sbmlsim.data import DataSet
from sbmlsim.fit import FitData, FitMapping
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.metoprolol import MODEL
from pkdb_models.models.metoprolol.experiments.base_experiment import (
    MetoprololSimulationExperiment,
)
from pkdb_models.models.metoprolol.experiments.figure_templates import (
    EXCRETION_LINESTYLES,
    fig_metoprolol,
)


class Lennard1982(MetoprololSimulationExperiment):
    """Simulation experiment of Lennard1982.

    A single oral dose of 200 mg metoprolol tartrate 1.5 hr after breakfast in
    12 men (8 hypertensive, 4 healthy), 6 extensive and 6 poor hydroxylators of
    debrisoquine (CYP2D6 phenotype). The bars of Fig1 are SD. The urinary
    recovery over 24 hr and the reduction of the exercise heart rate at 12 and
    24 hr (beta blockade relative to the pretreatment values) are given in the
    text as mean +- SD and are not curated in PK-DB.
    """

    metabolizers: ClassVar[list[str]] = ["em", "pm"]
    #: number of subjects per phenotype
    count: ClassVar[int] = 6
    #: the exercise heart rate before the dose [1/min], the baseline of the
    #: reduction: the workload was set for 130/min in subjects over 60 years
    #: and 140/min in younger subjects, the ages are not reported
    hr_baseline: ClassVar[float] = 135.0

    #: the urinary recovery 0-24 hr [% of the dose] (text, mean (SD)), by
    #: phenotype and substance
    urine_recovery: ClassVar[dict[str, dict[str, tuple[float, float]]]] = {
        "em": {"met": (3.2, 3.0), "metoh": (11.1, 4.5)},
        "pm": {"met": (14.7, 7.0), "metoh": (0.7, 0.3)},
    }
    #: the reduction of the exercise heart rate [%] at 12 and 24 hr relative to
    #: the pretreatment values (text, mean (SD))
    hr_reduction: ClassVar[dict[str, list[tuple[float, float, float]]]] = {
        "em": [(12.0, 14.8, 7.9), (24.0, 5.3, 5.6)],
        "pm": [(12.0, 25.0, 3.0), (24.0, 18.9, 3.8)],
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1"]:
            for substance, df in self.load_dataframes_by_substance(fig_id).items():
                dset = DataSet.from_df(df, self.ureg)
                if substance == "metoprolol":
                    dset.unit_conversion("mean", 1 / self.Mr.met)

                # the groups are named after the phenotype, e.g. 'DEB_em'
                for group_name in df.group.unique():
                    group = group_name.split("_")[-1]
                    dsets[f"{fig_id.lower()}_{substance}_{group}"] = dset[
                        dset.group == group_name
                    ]

        # the urinary recovery as amounts: the fraction of the dose (molar)
        dose_mmole = (self.dose_base(200, "tartrate") / self.Mr.met).to("mmole")
        for metabolizer, recoveries in self.urine_recovery.items():
            for sid, (mean, sd) in recoveries.items():
                df = pd.DataFrame(
                    {
                        "time": [24.0],
                        "time_unit": "hr",
                        "mean": [mean],
                        "sd": [sd],
                        "count": [self.count],
                        "unit": "percent",
                    }
                )
                dset = DataSet.from_df(df, self.ureg)
                dset.unit_conversion("mean", dose_mmole)
                dsets[f"text_urine_{sid}_{metabolizer}"] = dset

            df = pd.DataFrame(
                {
                    "time": [t for t, _, _ in self.hr_reduction[metabolizer]],
                    "time_unit": "hr",
                    "mean": [m for _, m, _ in self.hr_reduction[metabolizer]],
                    "sd": [sd for _, _, sd in self.hr_reduction[metabolizer]],
                    "count": self.count,
                    "unit": "percent",
                }
            )
            dsets[f"text_hrred_{metabolizer}"] = DataSet.from_df(df, self.ureg)
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        # 200 mg metoprolol tartrate, the form is not reported and simulated as
        # an immediate release tablet
        dose = self.dose_base(200, "tartrate")
        return {
            f"met_po200_{metabolizer}": Simulation(
                time_unit="hr",
                end=24,
                preinit_changes={
                    **self.default_changes(),
                    **self.application_changes("ir"),
                    **self.metabolizer_changes(metabolizer),
                    "HR": Q(self.hr_baseline, "1/min"),
                    "PODOSE_met": dose,
                },
            )
            for metabolizer in self.metabolizers
        }

    @staticmethod
    def _metadata(
        metabolizer: str, data: PKPDData, tissue: Tissue
    ) -> PKPDMappingMetaData:
        """Get the metadata of a mapping of a phenotype."""
        return PKPDMappingMetaData(
            tissue=tissue,
            route=Route.PO,
            application_form=ApplicationForm.NR,
            dosing=Dosing.SINGLE,
            health=Health.HYPERTENSION,
            phenotype=Phenotype[f"CYP2D6_{metabolizer.upper()}"],
            fasting=Fasting.FED,
            data=data,
        )

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for metabolizer in self.metabolizers:
            task_id = f"task_met_po200_{metabolizer}"
            mappings[f"fm_met_{metabolizer}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"fig1_metoprolol_{metabolizer}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self, task=task_id, xid="time", yid="[Cveplasma_met]"
                ),
                metadata=self._metadata(metabolizer, PKPDData.PK, Tissue.PLASMA),
            )
            for sid in ["met", "metoh"]:
                mappings[f"fm_urine_{sid}_{metabolizer}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"text_urine_{sid}_{metabolizer}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self, task=task_id, xid="time", yid=f"Aurine_{sid}"
                    ),
                    metadata=self._metadata(metabolizer, PKPDData.PK, Tissue.URINE),
                )
            mappings[f"fm_hrred_{metabolizer}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"text_hrred_{metabolizer}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                ),
                observable=FitData(self, task=task_id, xid="time", yid="HRred"),
                metadata=self._metadata(metabolizer, PKPDData.PD, Tissue.NONE),
            )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig, plots = fig_metoprolol(self, fig_id="Fig1")

        # data
        for metabolizer, marker in [("em", "s"), ("pm", "o")]:
            plots[0].add_data(
                dataset=f"fig1_metoprolol_{metabolizer}",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label=f"{metabolizer.upper()}",
                color=self.colors[metabolizer],
                marker=marker,
            )
            plots[5].add_data(
                dataset=f"text_hrred_{metabolizer}",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label=f"{metabolizer.upper()}",
                color=self.colors[metabolizer],
                marker=marker,
            )

        # simulations
        for metabolizer in self.metabolizers:
            task_id = f"task_met_po200_{metabolizer}"
            for k, sid in enumerate(["met", "metoh", "mam"]):
                plots[k].add_data(
                    task=task_id,
                    xid="time",
                    yid=f"[Cveplasma_{sid}]",
                    label=metabolizer.upper(),
                    color=self.colors[metabolizer],
                )
                plots[3].add_data(
                    task=task_id,
                    xid="time",
                    yid=f"KI__{sid.upper()}EX",
                    label=f"{sid} {metabolizer.upper()}",
                    color=self.colors[metabolizer],
                    linestyle=EXCRETION_LINESTYLES[sid],
                )
            for k, yid in [(4, "HReff"), (5, "HRred")]:
                plots[k].add_data(
                    task=task_id,
                    xid="time",
                    yid=yid,
                    label=metabolizer.upper(),
                    color=self.colors[metabolizer],
                )

        return {"fig1": fig, "urine": self._figure_urine()}

    def _figure_urine(self) -> Figure:
        """Get the figure of the urinary recovery over 24 hr (text)."""
        fig = Figure(
            experiment=self,
            sid=self.to_sid("urine"),
            num_rows=1,
            num_cols=2,
            name=f"{self.sid} (urine)",
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, self.unit_time), legend=True
        )
        for k, sid in enumerate(["met", "metoh"]):
            label = self.label_met if sid == "met" else self.label_metoh.strip()
            plots[k].set_yaxis(f"{label}\nurine", self.units[f"Aurine_{sid}"])
            for metabolizer in self.metabolizers:
                plots[k].add_data(
                    task=f"task_met_po200_{metabolizer}",
                    xid="time",
                    yid=f"Aurine_{sid}",
                    label=metabolizer.upper(),
                    color=self.colors[metabolizer],
                )
                plots[k].add_data(
                    dataset=f"text_urine_{sid}_{metabolizer}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"{metabolizer.upper()} (text)",
                    color=self.colors[metabolizer],
                )
        return fig


if __name__ == "__main__":
    MODEL.run_experiments(Lennard1982, output_dir="test")
