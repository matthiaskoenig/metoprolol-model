"""Simulation experiment of the study Oosterhuis1988."""

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
from sbmlsim.data import DataSet
from sbmlsim.fit import FitData, FitMapping
from sbmlsim.plot import Figure
from sbmlsim.simulation import Simulation
from sbmlsim.units import Quantity

from pkdb_models.models.metoprolol import MODEL
from pkdb_models.models.metoprolol.experiments.base_experiment import (
    MetoprololSimulationExperiment,
)
from pkdb_models.models.metoprolol.experiments.figure_templates import (
    EXCRETION_LINESTYLES,
    fig_metoprolol,
)


class Oosterhuis1988(MetoprololSimulationExperiment):
    """Simulation experiment of Oosterhuis1988.

    Metoprolol CR (95 mg metoprolol succinate, Betaloc ZOK) and metoprolol SR
    (half of a 200 mg tablet of metoprolol tartrate, Lopressor SR) once daily
    in 12 healthy men (68-86 kg, the mean is not reported), the profile of the
    fifth dose (96-120 hr). The reduction of the exercise heart rate is
    relative to placebo at the same time (Table 2, mean (SD)), the plasma
    concentrations are mean (SEM) (Fig2). The phenotype is not determined.
    """

    applications: ClassVar[list[str]] = ["cr", "sr"]

    #: intervention of the data per application form
    interventions: ClassVar[dict[str, str]] = {
        "cr": "METO_CR_1, METO_CR_2, METO_CR_3, METO_CR_4, METO_CR_5",
        "sr": "METO_SR_1, METO_SR_2, METO_SR_3, METO_SR_4, METO_SR_5",
    }
    application_forms: ClassVar[dict[str, ApplicationForm]] = {
        "cr": ApplicationForm.CONTROLLED_RELEASE,
        "sr": ApplicationForm.SLOW_RELEASE,
    }

    def doses(self) -> dict[str, Quantity]:
        """Get the dose of metoprolol (base) per application form."""
        return {
            "cr": self.dose_base(95, "succinate"),
            "sr": self.dose_base(100, "tartrate"),
        }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2", "Tab2A"]:
            for substance, df in self.load_dataframes_by_substance(fig_id).items():
                if substance != "metoprolol":
                    continue
                dset = DataSet.from_df(df, self.ureg)
                for intervention in df.intervention.unique():
                    dsets[self.to_sid(f"{fig_id}_{substance}_{intervention}")] = dset[
                        dset.intervention == intervention
                    ]
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        # metoprolol once daily for 5 days
        tcsims = {}
        for application, dose in self.doses().items():
            tcsims[self.to_sid(f"met_po100_{application}")] = Simulation(
                time_unit="hr",
                end=5 * 24,
                preinit_changes={
                    **self.default_changes(),
                    **self.application_changes(application),
                    "PODOSE_met": dose,
                },
                changes=[self.oral_doses([24, 48, 72, 96], dose)],
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        # metoprolol in plasma and the reduction of the exercise heart rate
        for key, fig_id, yid in [
            ("met", "Fig2", "[Cveplasma_met]"),
            ("hr", "Tab2A", "HRred"),
        ]:
            for application in self.applications:
                intervention = self.interventions[application]
                mappings[self.to_sid(f"fm_{key}_100_{application}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"{fig_id}_metoprolol_{intervention}"),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count=12,
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_met_po100_{application}"),
                        xid="time",
                        yid=yid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA if key == "met" else Tissue.NONE,
                        route=Route.PO,
                        application_form=self.application_forms[application],
                        dosing=Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        phenotype=Phenotype.NR,
                        fasting=Fasting.NR,
                        data=PKPDData.PK if key == "met" else PKPDData.PD,
                    ),
                )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig, plots = fig_metoprolol(self, fig_id="Fig1")
        # the data is of the fifth dose
        for plot in plots:
            if plot.xaxis is not None:
                plot.xaxis.min = 70

        for application in self.applications:
            intervention = self.interventions[application]
            label = application.upper()
            color = self.colors[application]
            # data
            plots[0].add_data(
                dataset=self.to_sid(f"Fig2_metoprolol_{intervention}"),
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count=12,
                label=label,
                color=color,
            )
            plots[5].add_data(
                dataset=self.to_sid(f"Tab2A_metoprolol_{intervention}"),
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count=12,
                label=label,
                color=color,
            )

            # simulations
            task_id = self.to_sid(f"task_met_po100_{application}")
            for k, sid in enumerate(["met", "metoh", "mam"]):
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
                    label=f"{sid} {label}",
                    color=color,
                    linestyle=EXCRETION_LINESTYLES[sid],
                )
            for k, yid in [(4, "HReff"), (5, "HRred")]:
                plots[k].add_data(
                    task=task_id, xid="time", yid=yid, label=label, color=color
                )

        return {"fig1": fig}


if __name__ == "__main__":
    MODEL.run_experiments(Oosterhuis1988, output_dir="test")
