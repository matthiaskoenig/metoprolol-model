"""Simulation experiment of the study Kirchheiner2004."""

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


class Kirchheiner2004(MetoprololSimulationExperiment):
    """Simulation experiment of Kirchheiner2004.

    A single oral dose of 100 mg metoprolol tartrate (Beloc, immediate release)
    after an overnight fast in 29 healthy volunteers by CYP2D6 genotype: poor
    (PM, no active gene), extensive (EM, two active genes) and ultrarapid
    metabolizers (UM, a gene duplication). The curves of the groups in Fig1 are
    the curves of the population pharmacokinetic model of the study (the bold
    lines), not measured means; measured are the curves of the four PMs. The
    exercise heart rate (Fig3) is the median of a group, its reduction is
    relative to the measurement before the dose.
    """

    metabolizers: ClassVar[list[str]] = ["em", "pm", "um"]
    #: number of subjects per CYP2D6 phenotype
    group_counts: ClassVar[dict[str, int]] = {"em": 13, "pm": 4, "um": 12}
    #: the CYP2D6 activity score of the groups, the mean of the subjects by the
    #: active genes of Fig2: PM 4 x 0, EM 5 x 1.5 and 8 x 2, UM 4 x 2.5 and 8 x 3
    activity_scores: ClassVar[dict[str, float]] = {
        "em": (5 * 1.5 + 8 * 2.0) / 13,
        "pm": 0.0,
        "um": (4 * 2.5 + 8 * 3.0) / 12,
    }
    #: body weight of the groups [kg], medians (TabGroups)
    body_weights: ClassVar[dict[str, float]] = {"em": 77.0, "pm": 90.0, "um": 76.0}
    #: the exercise heart rate before the dose [1/min] (Fig3, medians), the
    #: baseline of the reduction of the heart rate
    hr_baselines: ClassVar[dict[str, float]] = {
        "em": 148.088,
        "pm": 151.682,
        "um": 148.072,
    }
    #: the substances of the urinary amounts of Table III
    urine_substances: ClassVar[dict[str, str]] = {
        "met": "metoprolol",
        "metoh": "alpha-hydroxymetoprolol",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}

        # the curves of the population model of the study (Fig1, bold lines)
        for substance, df in self.load_dataframes_by_substance("Fig1Mean").items():
            dset = DataSet.from_df(df, self.ureg)
            if substance == "metoprolol":
                dset.unit_conversion("mean", 1 / self.Mr.met)
            for group in df.group.unique():
                dsets[f"Fig1Mean_{group}"] = dset[dset.group == group]

        # the mean of the four poor metabolizers (Fig1, thin lines)
        df = self.load_dataframes_by_substance("Fig1")["metoprolol"]
        stats = df.groupby("time")["value"].agg(["mean", "std", "count"])
        df_pm = pd.DataFrame(
            {
                "time": stats.index.to_numpy(),
                "time_unit": "hr",
                "mean": stats["mean"].to_numpy(),
                "sd": stats["std"].to_numpy(),
                "se": (stats["std"] / stats["count"] ** 0.5).to_numpy(),
                "count": stats["count"].to_numpy(),
                "unit": df.unit.iloc[0],
            }
        )
        dset = DataSet.from_df(df_pm, self.ureg)
        dset.unit_conversion("mean", 1 / self.Mr.met)
        dsets["Fig1_PM_mean"] = dset

        # the exercise heart rate (medians) and its reduction relative to the
        # measurement before the dose
        df = self.load_dataframes_by_substance("Fig3")["metoprolol"]
        dset = DataSet.from_df(df, self.ureg)
        for group in df.group.unique():
            dsets[f"Fig3_{group}"] = dset[dset.group == group]
            df_group = df[df.group == group].sort_values("time")
            baseline = float(df_group["median"].iloc[0])
            after = df_group[df_group.time > 0]
            df_red = pd.DataFrame(
                {
                    "time": after.time.to_numpy(),
                    "time_unit": after.time_unit.to_numpy(),
                    "median": 1.0 - after["median"].to_numpy() / baseline,
                    "unit": "dimensionless",
                }
            )
            dsets[f"Fig3_{group}_hrred"] = DataSet.from_df(df_red, self.ureg)

        # the urinary amounts 0-12 hr (Table III, medians)
        frames = self.load_dataframes_by_substance("Tab3")
        for sid, substance in self.urine_substances.items():
            df = frames[substance]
            df = df[df.measurement == "cumulative amount"]
            dset = DataSet.from_df(df, self.ureg)
            dset.unit_conversion("median", 1 / getattr(self.Mr, sid))
            for group in df.group.unique():
                dsets[f"Tab3_{sid}_{group}"] = dset[dset.group == group]

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        dose = self.dose_base(100, "tartrate")
        return {
            f"met_po100_{metabolizer}": Simulation(
                time_unit="hr",
                end=24,
                preinit_changes={
                    **self.default_changes(),
                    **self.application_changes("ir"),
                    **self.cyp2d6_changes(self.activity_scores[metabolizer]),
                    "BW": Q(self.body_weights[metabolizer], "kg"),
                    "HR": Q(self.hr_baselines[metabolizer], "1/min"),
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
            application_form=ApplicationForm.IMMEDIATE_RELEASE,
            dosing=Dosing.SINGLE,
            health=Health.HEALTHY,
            phenotype=Phenotype[f"CYP2D6_{metabolizer.upper()}"],
            fasting=Fasting.FASTED,
            data=data,
        )

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for metabolizer in self.metabolizers:
            group = metabolizer.upper()
            count = self.group_counts[metabolizer]
            task_id = f"task_met_po100_{metabolizer}"

            # the curve of the population model of the study, no measured data
            mappings[f"fm_met_model_{metabolizer}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"Fig1Mean_{group}",
                    xid="time",
                    yid="mean",
                    count=count,
                ),
                observable=FitData(
                    self, task=task_id, xid="time", yid="[Cveplasma_met]"
                ),
                metadata=self._metadata(metabolizer, PKPDData.PK, Tissue.PLASMA),
            )
            # the reduction of the exercise heart rate
            mappings[f"fm_hrred_{metabolizer}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"Fig3_{group}_hrred",
                    xid="time",
                    yid="median",
                    count=count,
                ),
                observable=FitData(self, task=task_id, xid="time", yid="HRred"),
                metadata=self._metadata(metabolizer, PKPDData.PD, Tissue.NONE),
            )
            # the urinary amounts of metoprolol and alpha-hydroxymetoprolol
            for sid in self.urine_substances:
                mappings[f"fm_urine_{sid}_{metabolizer}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"Tab3_{sid}_{group}",
                        xid="time",
                        yid="median",
                        count=count,
                    ),
                    observable=FitData(
                        self, task=task_id, xid="time", yid=f"Aurine_{sid}"
                    ),
                    metadata=self._metadata(metabolizer, PKPDData.PK, Tissue.URINE),
                )

        # the mean of the measured curves of the four poor metabolizers
        mappings["fm_met_pm_mean"] = FitMapping(
            self,
            reference=FitData(
                self,
                dataset="Fig1_PM_mean",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count=self.group_counts["pm"],
            ),
            observable=FitData(
                self, task="task_met_po100_pm", xid="time", yid="[Cveplasma_met]"
            ),
            metadata=self._metadata("pm", PKPDData.PK, Tissue.PLASMA),
        )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig, plots = fig_metoprolol(self, fig_id="Fig1")

        # data
        for metabolizer in self.metabolizers:
            group = metabolizer.upper()
            plots[0].add_data(
                dataset=f"Fig1Mean_{group}",
                xid="time",
                yid="mean",
                label=f"population model {group}",
                color=self.colors[metabolizer],
                marker="x",
            )
            plots[4].add_data(
                dataset=f"Fig3_{group}",
                xid="time",
                yid="median",
                label=f"{group} (median)",
                color=self.colors[metabolizer],
            )
            plots[5].add_data(
                dataset=f"Fig3_{group}_hrred",
                xid="time",
                yid="median",
                label=f"{group} (median)",
                color=self.colors[metabolizer],
            )
        plots[0].add_data(
            dataset="Fig1_PM_mean",
            xid="time",
            yid="mean",
            yid_sd="mean_sd",
            count="count",
            label="PM (mean of 4)",
            color=self.colors["pm"],
        )

        # simulations
        for metabolizer in self.metabolizers:
            task_id = f"task_met_po100_{metabolizer}"
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

        return {"fig1": fig, "tab3": self._figure_urine()}

    def _figure_urine(self) -> Figure:
        """Get the figure of the urinary amounts (Table III)."""
        fig = Figure(
            experiment=self,
            sid=self.to_sid("Tab3"),
            num_rows=1,
            num_cols=2,
            name=f"{self.sid} (urine)",
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, self.unit_time), legend=True
        )
        for k, sid in enumerate(self.urine_substances):
            label = self.label_met if sid == "met" else self.label_metoh.strip()
            plots[k].set_yaxis(f"{label}\nurine", self.units[f"Aurine_{sid}"])
            for metabolizer in self.metabolizers:
                plots[k].add_data(
                    task=f"task_met_po100_{metabolizer}",
                    xid="time",
                    yid=f"Aurine_{sid}",
                    label=metabolizer.upper(),
                    color=self.colors[metabolizer],
                )
                plots[k].add_data(
                    dataset=f"Tab3_{sid}_{metabolizer.upper()}",
                    xid="time",
                    yid="median",
                    label=f"{metabolizer.upper()} (median)",
                    color=self.colors[metabolizer],
                )
        return fig


if __name__ == "__main__":
    MODEL.run_experiments(Kirchheiner2004, output_dir="test")
