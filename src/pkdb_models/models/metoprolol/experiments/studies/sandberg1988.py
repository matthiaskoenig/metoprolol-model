"""Simulation experiment of the study Sandberg1988."""

from typing import ClassVar, NamedTuple, override

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


class Treatment(NamedTuple):
    """A treatment of the study: the dose of the salt, the form and the interval."""

    #: the dose of the salt [mg]
    dose: float
    #: the salt of the dose
    salt: str
    #: the application form
    application: str
    #: the dosing interval [hr]
    interval: float
    #: the intervention of the data
    intervention: str
    #: the color of the treatment
    color: str


class Sandberg1988(MetoprololSimulationExperiment):
    """Simulation experiment of Sandberg1988.

    Metoprolol CR (95 mg metoprolol succinate, Betaloc ZOK) once daily,
    conventional tablets of 100 mg metoprolol tartrate once daily and of 50 mg
    twice daily for 5 days in 12 healthy men (mean 74 kg), fasted before the
    dose of day 5. Plasma metoprolol over the dosing interval of day 5 (Fig2,
    mean (SEM)) and the reduction of the exercise heart rate relative to
    placebo at the same time (Table 2, mean (SD); the workload was set for an
    exercise heart rate of 145-155/min). The phenotype is not determined.
    """

    #: the treatments by the key of their simulation
    treatments: ClassVar[dict[str, Treatment]] = {
        "100_cr": Treatment(
            dose=95,
            salt="succinate",
            application="cr",
            interval=24,
            intervention="METO_CR_1, METO_CR_2, METO_CR_3, METO_CR_4, METO_CR_5",
            color="tab:blue",
        ),
        "100_ir": Treatment(
            dose=100,
            salt="tartrate",
            application="ir",
            interval=24,
            intervention="METO_100_1, METO_100_2, METO_100_3, METO_100_4, METO_100_5",
            color="black",
        ),
        "50_ir": Treatment(
            dose=50,
            salt="tartrate",
            application="ir",
            interval=12,
            intervention=(
                "METO_50_1,METO_50_2,METO_50_3, METO_50_4, METO_50_5, "
                "METO_50_6,METO_50_7,METO_50_8,METO_50_9,METO_50_10"
            ),
            color="tab:gray",
        ),
    }
    application_forms: ClassVar[dict[str, ApplicationForm]] = {
        "cr": ApplicationForm.CONTROLLED_RELEASE,
        "ir": ApplicationForm.IMMEDIATE_RELEASE,
    }
    #: the exercise heart rate of the workload [1/min], the baseline of the
    #: reduction of the heart rate
    hr_baseline: ClassVar[float] = 150.0

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2", "Tab2"]:
            df = self.load_dataframes_by_substance(fig_id)["metoprolol"]
            dset = DataSet.from_df(df, self.ureg)
            for intervention in df.intervention.unique():
                dsets[self.to_sid(f"{fig_id}_metoprolol_{intervention}")] = dset[
                    dset.intervention == intervention
                ]
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        # 5 days of dosing, the data is of the dosing interval of day 5
        tcsims = {}
        for key, treatment in self.treatments.items():
            dose = self.dose_base(treatment.dose, treatment.salt)
            interval = treatment.interval
            tcsims[f"met_po{key}"] = Simulation(
                time_unit="hr",
                end=5 * 24,
                preinit_changes={
                    **self.default_changes(),
                    **self.application_changes(treatment.application),
                    "BW": Q(74, "kg"),
                    "HR": Q(self.hr_baseline, "1/min"),
                    "PODOSE_met": dose,
                },
                changes=[
                    self.oral_doses(
                        [interval * k for k in range(1, int(5 * 24 / interval))],
                        dose,
                    )
                ],
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        # metoprolol in plasma and the reduction of the exercise heart rate
        for key, fig_id, yid in [
            ("met", "Fig2", "[Cveplasma_met]"),
            ("hr", "Tab2", "HRred"),
        ]:
            for sim_key, treatment in self.treatments.items():
                mappings[f"fm_{key}_{sim_key}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(
                            f"{fig_id}_metoprolol_{treatment.intervention}"
                        ),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count=12,
                    ),
                    observable=FitData(
                        self, task=f"task_met_po{sim_key}", xid="time", yid=yid
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA if key == "met" else Tissue.NONE,
                        route=Route.PO,
                        application_form=self.application_forms[treatment.application],
                        dosing=Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        phenotype=Phenotype.NR,
                        fasting=Fasting.FASTED,
                        data=PKPDData.PK if key == "met" else PKPDData.PD,
                    ),
                )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig, plots = fig_metoprolol(self, fig_id="Fig1")
        # the data is of the last day of the dosing
        for plot in plots:
            if plot.xaxis is not None:
                plot.xaxis.min = 70

        for sim_key, treatment in self.treatments.items():
            dose, application = sim_key.split("_")
            label = f"{dose} mg {application.upper()}"
            # data
            for k, fig_id in [(0, "Fig2"), (5, "Tab2")]:
                plots[k].add_data(
                    dataset=self.to_sid(
                        f"{fig_id}_metoprolol_{treatment.intervention}"
                    ),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count=12,
                    label=label,
                    color=treatment.color,
                )

            # simulations
            task_id = f"task_met_po{sim_key}"
            for k, sid in enumerate(["met", "metoh", "mam"]):
                plots[k].add_data(
                    task=task_id,
                    xid="time",
                    yid=f"[Cveplasma_{sid}]",
                    label=label,
                    color=treatment.color,
                )
                plots[3].add_data(
                    task=task_id,
                    xid="time",
                    yid=f"KI__{sid.upper()}EX",
                    label=f"{sid} {label}",
                    color=treatment.color,
                    linestyle=EXCRETION_LINESTYLES[sid],
                )
            for k, yid in [(4, "HReff"), (5, "HRred")]:
                plots[k].add_data(
                    task=task_id,
                    xid="time",
                    yid=yid,
                    label=label,
                    color=treatment.color,
                )

        return {"fig1": fig}


if __name__ == "__main__":
    MODEL.run_experiments(Sandberg1988, output_dir="test")
