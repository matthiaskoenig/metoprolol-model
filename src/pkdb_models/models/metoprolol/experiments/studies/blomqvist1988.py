"""Simulation experiment of the study Blomqvist1988."""

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


class Blomqvist1988(MetoprololSimulationExperiment):
    """Simulation experiment of Blomqvist1988.

    Ten healthy men (74 kg), phenotype not determined, controlled release
    metoprolol succinate (Betaloc ZOK) "100 mg" (95 mg succinate) and "200 mg"
    (two tablets) once daily for 4 days; day 4 after an overnight fast. Fig 1:
    metoprolol in plasma on day 4 (mean and SEM, nmol/l); Table 2: the
    percentage reduction of the exercise heart rate against placebo (mean and
    SD), the relative reduction `HRred` of the model; Fig 2: the exercise
    heart rate (means), shown with `HReff` and the baseline of the placebo.
    """

    doses: ClassVar[list[int]] = [100, 200]
    #: the dose of metoprolol succinate [mg] per labeled dose
    doses_succinate: ClassVar[dict[int, float]] = {100: 95.0, 200: 190.0}
    dose_colors: ClassVar[dict[int, str]] = {100: "tab:blue", 200: "tab:orange"}
    dose_markers: ClassVar[dict[int, str]] = {100: "s", 200: "o"}
    #: the times of the doses [hr], days 1 to 4; the data are on day 4
    dose_times: ClassVar[list[float]] = [0, 24, 48, 72]
    #: the exercise heart rate of the placebo arm on day 4, mean of Fig 2
    #: (148.2, 148.7, 157.1, 153.1, 150.4, 147.6 /min), the baseline of `HReff`
    hr_placebo: ClassVar[float] = 150.9

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        # metoprolol in plasma [nmol/l], the reduction of the exercise heart rate
        # against placebo [percent]
        for fig_id in ["Fig1", "Tab2"]:
            df = self.load_dataframes_by_substance(fig_id)["metoprolol"]
            dset = DataSet.from_df(df, self.ureg)
            for intervention in df.intervention.unique():
                dsets[self.to_sid(f"{fig_id.lower()}_{intervention.lower()}")] = dset[
                    dset.intervention == intervention
                ]
        # the exercise heart rate (the systolic blood pressure is not used)
        for substance, df in self.load_dataframes_by_substance("Fig2").items():
            if substance not in {"metoprolol", "placebo"}:
                continue
            df_ehr = df[df.measurement == "EHR"]
            dset = DataSet.from_df(df_ehr, self.ureg)
            for intervention in df_ehr.intervention.unique():
                dsets[self.to_sid(f"fig2_{intervention.lower()}_ehr")] = dset[
                    dset.intervention == intervention
                ]
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        # controlled release tablets of metoprolol succinate once daily for 4
        # days, the undissolved rest of the earlier doses is kept
        for dose in self.doses:
            dose_base = self.dose_base(self.doses_succinate[dose], "succinate")
            tcsims[self.to_sid(f"met_po{dose}")] = Simulation(
                time_unit="hr",
                end=96,
                preinit_changes={
                    **self.default_changes(),
                    **self.application_changes("cr"),
                    "BW": Q(74, "kg"),
                    "HR": Q(self.hr_placebo, "1/min"),
                    "PODOSE_met": dose_base,
                },
                changes=[self.oral_doses(self.dose_times[1:], dose_base)],
            )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for dose in self.doses:
            for key, dataset, yid, data, tissue in [
                ("met", "fig1", "[Cveplasma_met]", PKPDData.PK, Tissue.PLASMA),
                ("hrred", "tab2", "HRred", PKPDData.PD, Tissue.NONE),
            ]:
                mappings[self.to_sid(f"fm_{key}_{dose}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"{dataset}_met{dose}"),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count=10,
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_met_po{dose}"),
                        xid="time",
                        yid=yid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=tissue,
                        route=Route.PO,
                        application_form=ApplicationForm.CONTROLLED_RELEASE,
                        dosing=Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        phenotype=Phenotype.NR,
                        fasting=Fasting.FASTED,
                        data=data,
                    ),
                )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig, plots = fig_metoprolol(
            self,
            fig_id="Fig1",
            name=f"{self.sid} (metoprolol succinate CR once daily, day 4)",
        )
        # the data are on day 4
        for k, plot in enumerate(plots):
            plot.set_xaxis(
                self.label_time,
                self.unit_time,
                min=71,
                max=97,
                label_visible=k >= 4,
            )

        plots[4].add_data(
            dataset="fig2_placebo_ehr",
            xid="time",
            yid="mean",
            count=10,
            label="placebo",
            color="tab:gray",
            marker="^",
        )
        for dose in self.doses:
            label = f"{dose} mg"
            color = self.dose_colors[dose]
            marker = self.dose_markers[dose]
            task_id = self.to_sid(f"task_met_po{dose}")

            # data
            plots[0].add_data(
                dataset=self.to_sid(f"fig1_met{dose}"),
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count=10,
                label=label,
                color=color,
                marker=marker,
            )
            plots[4].add_data(
                dataset=self.to_sid(f"fig2_met{dose}_ehr"),
                xid="time",
                yid="mean",
                count=10,
                label=label,
                color=color,
                marker=marker,
            )
            plots[5].add_data(
                dataset=self.to_sid(f"tab2_met{dose}"),
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count=10,
                label=label,
                color=color,
                marker=marker,
            )

            # simulations
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
    MODEL.run_experiments(Blomqvist1988, output_dir="test")
