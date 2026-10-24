"""Simulation experiment of the study Cerqueira2003."""

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


class Cerqueira2003(MetoprololSimulationExperiment):
    """Simulation experiment of Cerqueira2003.

    Ten hypertensive patients (74.7 kg), debrisoquine extensive metabolizers
    with normal renal and hepatic function, no CYP2D6 inhibitor; racemic
    metoprolol tartrate (Seloken, conventional tablets) 2 x 100 mg once daily
    for 7 days, the dose of day 7 fasted. Only the four stereoisomers of
    alpha-hydroxymetoprolol were measured: Fig 4 plasma (mean and SEM, n=10),
    Fig 5 urinary excretion rate of patient 7. The total alpha-OH metoprolol
    is the sum of the isomers (curated), its SD the sum of their SDs.
    """

    #: the times of the doses [hr], days 1 to 7; the data are on day 7
    dose_times: ClassVar[list[float]] = [24.0 * k for k in range(7)]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id, yid in [("Fig4", "mean"), ("Fig5", "value")]:
            dframes = self.load_dataframes_by_substance(fig_id)
            for substance, df in dframes.items():
                dset = DataSet.from_df(df, self.ureg)
                dset.unit_conversion(yid, 1 / self.Mr.metoh)
                dsets[self.to_sid(f"{fig_id.lower()}_{substance}")] = dset
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        # 200 mg metoprolol tartrate (156.2 mg metoprolol) daily for 7 days as
        # immediate release tablets; CYP2D6 *1/*1 (extensive metabolizers)
        dose = self.dose_base(200, "tartrate")
        return {
            self.to_sid("met_po200"): Simulation(
                time_unit="hr",
                end=7 * 24,
                preinit_changes={
                    **self.default_changes(),
                    **self.application_changes("ir"),
                    "BW": Q(74.7, "kg"),
                    "PODOSE_met": dose,
                },
                changes=[self.oral_doses(self.dose_times[1:], dose)],
            )
        }

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for key, dataset, yid, yid_sd, count, observable, tissue in [
            # plasma, mean of 10 patients
            (
                "fm_metoh",
                "fig4_alpha_hydroxymetoprolol",
                "mean",
                "mean_sd",
                10,
                "[Cveplasma_metoh]",
                Tissue.PLASMA,
            ),
            # urinary excretion rate of patient 7
            (
                "fm_KI__METOHEX",
                "fig5_alpha_hydroxymetoprolol",
                "value",
                None,
                1,
                "KI__METOHEX",
                Tissue.URINE,
            ),
        ]:
            mappings[key] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=dataset,
                    xid="time",
                    yid=yid,
                    yid_sd=yid_sd,
                    count=count,
                ),
                observable=FitData(
                    self, task="task_met_po200", xid="time", yid=observable
                ),
                metadata=PKPDMappingMetaData(
                    tissue=tissue,
                    route=Route.PO,
                    application_form=ApplicationForm.IMMEDIATE_RELEASE,
                    dosing=Dosing.MULTIPLE,
                    health=Health.HYPERTENSION,
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

        # data
        plots[1].add_data(
            dataset="fig4_alpha_hydroxymetoprolol",
            xid="time",
            yid="mean",
            yid_sd="mean_sd",
            label="plasma (n=10)",
            color="black",
            marker="s",
        )
        plots[3].add_data(
            dataset="fig5_alpha_hydroxymetoprolol",
            xid="time",
            yid="value",
            label="metoh patient 7",
            color="black",
            marker="o",
        )

        # simulation
        task_id = "task_met_po200"
        for k, sid in enumerate(["met", "metoh", "mam"]):
            plots[k].add_data(
                task=task_id,
                xid="time",
                yid=f"[Cveplasma_{sid}]",
                label="200 mg",
                color="black",
            )
            plots[3].add_data(
                task=task_id,
                xid="time",
                yid=f"KI__{sid.upper()}EX",
                label=f"200 mg {sid}",
                color="black",
                linestyle=EXCRETION_LINESTYLES[sid],
            )
        plots[4].add_data(
            task=task_id, xid="time", yid="HReff", label="200 mg", color="black"
        )
        plots[5].add_data(
            task=task_id, xid="time", yid="HRred", label="200 mg", color="black"
        )

        return {"fig1": fig}


if __name__ == "__main__":
    MODEL.run_experiments(Cerqueira2003, output_dir="test")
