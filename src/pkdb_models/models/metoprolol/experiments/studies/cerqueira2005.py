"""Simulation experiment of the study Cerqueira2005."""

from typing import ClassVar, override

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
from sbmlsim.plot import Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.metoprolol import MODEL
from pkdb_models.models.metoprolol.experiments.base_experiment import (
    MetoprololSimulationExperiment,
)
from pkdb_models.models.metoprolol.experiments.figure_templates import (
    EXCRETION_LINESTYLES,
    fig_metoprolol,
)


class Cerqueira2005(MetoprololSimulationExperiment):
    """Simulation experiment of Cerqueira2005.

    Hypertensive patients with normal renal function (control, n=7) and with
    chronic renal failure (crf, n=6), debrisoquine extensive metabolizers (the
    two poor metabolizers are excluded), no CYP2D6 inhibitor; racemic
    metoprolol tartrate (Seloken, conventional tablets) 2 x 100 mg once daily
    for 7 days, the dose of day 7 fasted. Fig 2: the enantiomers of metoprolol
    and of metoprolol acid and the four isomers of alpha-hydroxymetoprolol in
    plasma (mean and SEM, log axes); the totals are their sums (curated), the
    SD of a total the sum of their SDs.
    """

    #: hypertensive subjects without (control) and with chronic renal failure (crf)
    groups: ClassVar[list[str]] = ["control", "crf"]
    #: number of subjects per group
    group_counts: ClassVar[dict[str, int]] = {"control": 7, "crf": 6}
    health: ClassVar[dict[str, Health]] = {
        "control": Health.HYPERTENSION,
        "crf": Health.RENAL_IMPAIRMENT,
    }
    #: the renal function, the mean Cockcroft-Gault creatinine clearance of the
    #: extensive metabolizers relative to 101 ml/min (control 82.0, 123.4, 90.0,
    #: 80.0, 87.0, 112.1, 88.0: 94.6 ml/min; crf 48.0, 51.5, 25.8, 51.0, 39.3,
    #: 59.8: 45.9 ml/min)
    renal_functions: ClassVar[dict[str, float]] = {
        "control": 94.6 / 101,
        "crf": 45.9 / 101,
    }
    #: the mean body weight of the extensive metabolizers [kg]
    body_weights: ClassVar[dict[str, float]] = {"control": 88.5, "crf": 87.0}
    group_colors: ClassVar[dict[str, str]] = {"control": "black", "crf": "tab:green"}
    group_markers: ClassVar[dict[str, str]] = {"control": "s", "crf": "o"}
    group_labels: ClassVar[dict[str, str]] = {"control": "control", "crf": "CRF"}
    #: the substances of the model and their totals in the data
    substances: ClassVar[dict[str, str]] = {
        "met": "metoprolol",
        "metoh": "alpha-hydroxymetoprolol",
        "mam": "metoprolol acidic metabolite",
    }
    #: the times of the doses [hr], days 1 to 7; the data are on day 7
    dose_times: ClassVar[list[float]] = [24.0 * k for k in range(7)]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        mrs = {
            "metoprolol": self.Mr.met,
            "alpha-hydroxymetoprolol": self.Mr.metoh,
            "metoprolol acidic metabolite": self.Mr.mam,
        }
        for fig_id in ["Fig2"]:
            dframes = self.load_dataframes_by_substance(fig_id)
            for substance, df in dframes.items():
                dset = DataSet.from_df(df, self.ureg)
                if substance in mrs:
                    dset.unit_conversion("mean", 1 / mrs[substance])

                for group_name in df.group.unique():
                    dsets[self.to_sid(f"{fig_id.lower()}_{substance}_{group_name}")] = (
                        dset[dset.group == group_name]
                    )
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        # 200 mg metoprolol tartrate (156.2 mg metoprolol) daily for 7 days as
        # immediate release tablets; CYP2D6 *1/*1 (extensive metabolizers, the
        # genotypes are mostly *1/*1 or *1/*5 in crf and *1/*3 or *1/*4 in the
        # controls, the pharmacokinetics of metoprolol does not differ)
        dose = self.dose_base(200, "tartrate")
        return {
            self.to_sid(f"met_po200_{group}"): Simulation(
                time_unit="hr",
                end=7 * 24,
                preinit_changes={
                    **self.default_changes(),
                    **self.application_changes("ir"),
                    "BW": Q(self.body_weights[group], "kg"),
                    "KI__f_renal_function": Q(
                        self.renal_functions[group], "dimensionless"
                    ),
                    "PODOSE_met": dose,
                },
                changes=[self.oral_doses(self.dose_times[1:], dose)],
            )
            for group in self.groups
        }

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for sid, substance in self.substances.items():
            for group in self.groups:
                mappings[self.to_sid(f"fm_{sid}_{group}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"fig2_{substance}_{group}"),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count=self.group_counts[group],
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_met_po200_{group}"),
                        xid="time",
                        yid=f"[Cveplasma_{sid}]",
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.IMMEDIATE_RELEASE,
                        dosing=Dosing.MULTIPLE,
                        health=self.health[group],
                        phenotype=Phenotype.CYP2D6_EM,
                        fasting=Fasting.FASTED,
                        data=PKPDData.PK,
                    ),
                )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig, plots = fig_metoprolol(
            self,
            fig_id="Fig1",
            name=f"{self.sid} (200 mg metoprolol tartrate once daily, day 7)",
        )
        # the data are on day 7
        for k, plot in enumerate(plots):
            plot.set_xaxis(
                self.label_time,
                self.unit_time,
                min=143,
                max=169,
                label_visible=k >= 4,
            )

        for group in self.groups:
            label = self.group_labels[group]
            color = self.group_colors[group]
            task_id = self.to_sid(f"task_met_po200_{group}")

            # data
            for k, substance in enumerate(self.substances.values()):
                plots[k].add_data(
                    dataset=self.to_sid(f"fig2_{substance}_{group}"),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    label=label,
                    color=color,
                    marker=self.group_markers[group],
                )

            # simulations
            for k, sid in enumerate(self.substances):
                plots[k].add_data(
                    task=task_id,
                    xid="time",
                    yid=f"[Cveplasma_{sid}]",
                    label=label,
                    color=color,
                )
                plots[3].add_data(
                    task=task_id,
                    xid="time",
                    yid=f"KI__{sid.upper()}EX",
                    label=f"{label} {sid}",
                    color=color,
                    linestyle=EXCRETION_LINESTYLES[sid],
                )
            plots[4].add_data(
                task=task_id, xid="time", yid="HReff", label=label, color=color
            )
            plots[5].add_data(
                task=task_id, xid="time", yid="HRred", label=label, color=color
            )

        return {"fig1": fig}


if __name__ == "__main__":
    MODEL.run_experiments(Cerqueira2005, output_dir="test")
