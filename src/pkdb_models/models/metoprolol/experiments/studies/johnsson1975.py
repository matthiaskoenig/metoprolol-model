"""Simulation experiment of the study Johnsson1975."""

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
from sbmlsim.plot import Figure, Plot
from sbmlsim.simulation import Simulation

from pkdb_models.models.metoprolol import MODEL
from pkdb_models.models.metoprolol.experiments.base_experiment import (
    MetoprololSimulationExperiment,
)
from pkdb_models.models.metoprolol.experiments.figure_templates import (
    EXCRETION_LINESTYLES,
    fig_metoprolol,
    fig_metoprolol_met_hrreduction,
)


class Johnsson1975(MetoprololSimulationExperiment):
    """Simulation experiment of Johnsson1975.

    Five healthy men (62-70 kg), phenotype not determined, crossover after an
    overnight fast: oral 20, 50 and 100 mg metoprolol tartrate as rapidly
    dissolving tablets and intravenous 5, 10, 15 and 20 mg metoprolol tartrate
    infused over 10 min. Fig 5 (oral) and Fig 6 (intravenous): metoprolol in
    plasma; Fig 2 (oral) and Fig 3 (intravenous): the percentage reduction of
    the exercise heart rate against the pre-dose exercise test (`HRred`), mean
    and SEM; the placebo arm of Fig 2 is shown, the reduction is 0 without drug.
    """

    doses_po: ClassVar[list[int]] = [20, 50, 100]
    doses_iv: ClassVar[list[int]] = [5, 10, 15, 20]
    #: colors of the doses [mg], from light to dark: oral blue, intravenous red
    dose_colors: ClassVar[dict[str, str]] = {
        "po20": "#6baed6",
        "po50": "#3182bd",
        "po100": "#08519c",
        "iv5": "#fcae91",
        "iv10": "#fb6a4a",
        "iv15": "#de2d26",
        "iv20": "#a50f15",
    }
    dose_markers: ClassVar[dict[str, str]] = {
        "po20": "s",
        "po50": "o",
        "po100": "^",
        "iv5": "s",
        "iv10": "o",
        "iv15": "^",
        "iv20": "v",
    }
    #: the body weight [kg], the middle of the range 62-70 kg
    bodyweight: ClassVar[float] = 66.0

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        # the reduction of the exercise heart rate [percent] and metoprolol in
        # plasma
        for fig_id in ["Fig2", "Fig3", "Fig5", "Fig6"]:
            df = self.load_dataframes_by_substance(fig_id)["metoprolol"]
            dset = DataSet.from_df(df, self.ureg)
            if fig_id in {"Fig5", "Fig6"}:
                dset.unit_conversion("mean", 1 / self.Mr.met)
            for intervention in df.intervention.unique():
                dsets[self.to_sid(f"{fig_id.lower()}_{intervention}")] = dset[
                    dset.intervention == intervention
                ]
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        changes = {
            **self.default_changes(),
            **self.application_changes("ir"),
            "BW": Q(self.bodyweight, "kg"),
        }

        # single oral doses of metoprolol tartrate as rapidly dissolving tablets
        # (immediate release)
        for dose in self.doses_po:
            tcsims[self.to_sid(f"met_po{dose}")] = Simulation(
                time_unit="hr",
                end=24,
                preinit_changes={
                    **changes,
                    "PODOSE_met": self.dose_base(dose, "tartrate"),
                },
            )

        # intravenous doses of metoprolol tartrate infused over 10 min
        for dose in self.doses_iv:
            preinit, infusion = self.iv_infusion(
                self.dose_base(dose, "tartrate"), duration=Q(10, "min")
            )
            tcsims[self.to_sid(f"met_iv{dose}")] = Simulation(
                time_unit="hr",
                end=24,
                preinit_changes={**changes, **preinit},
                changes=infusion,
            )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for route, doses, fig_pk, fig_pd in [
            ("oral", self.doses_po, "fig5", "fig2"),
            ("iv", self.doses_iv, "fig6", "fig3"),
        ]:
            prefix = "po" if route == "oral" else "iv"
            for dose in doses:
                task = self.to_sid(f"task_met_{prefix}{dose}")
                for key, fig_id, yid, tissue, data in [
                    ("met", fig_pk, "[Cveplasma_met]", Tissue.PLASMA, PKPDData.PK),
                    ("hrr", fig_pd, "HRred", Tissue.NONE, PKPDData.PD),
                ]:
                    mappings[self.to_sid(f"fm_{key}_{route}{dose}")] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=self.to_sid(f"{fig_id}_metoprolol_{route}{dose}"),
                            xid="time",
                            yid="mean",
                            yid_sd="mean_sd",
                            count="count",
                        ),
                        observable=FitData(self, task=task, xid="time", yid=yid),
                        metadata=PKPDMappingMetaData(
                            tissue=tissue,
                            route=Route.PO if route == "oral" else Route.IV,
                            application_form=(
                                ApplicationForm.IMMEDIATE_RELEASE
                                if route == "oral"
                                else ApplicationForm.SOLUTION
                            ),
                            dosing=Dosing.SINGLE,
                            health=Health.HEALTHY,
                            phenotype=Phenotype.NR,
                            fasting=Fasting.FASTED,
                            data=data,
                        ),
                    )
        return mappings

    @staticmethod
    def dose_label(dosing: str) -> str:
        """Get the label of a dose, e.g. `100 mg oral` of `po100`."""
        route = "oral" if dosing.startswith("po") else "iv"
        return f"{dosing[2:]} mg {route}"

    def add_dose(self, plot_met: Plot, plot_hrred: Plot, dosing: str) -> None:
        """Add the data and the simulation of a dose to metoprolol and HRred.

        Args:
            plot_met: the panel of metoprolol in plasma.
            plot_hrred: the panel of the reduction of the heart rate.
            dosing: the route and the dose, e.g. `po100`, `iv5`.
        """
        route = "oral" if dosing.startswith("po") else "iv"
        dose = dosing[2:]
        fig_pk, fig_pd = ("fig5", "fig2") if route == "oral" else ("fig6", "fig3")
        label = self.dose_label(dosing)
        color = self.dose_colors[dosing]
        task_id = self.to_sid(f"task_met_{dosing}")
        for plot, fig_id, yid in [
            (plot_met, fig_pk, "[Cveplasma_met]"),
            (plot_hrred, fig_pd, "HRred"),
        ]:
            plot.add_data(
                dataset=self.to_sid(f"{fig_id}_metoprolol_{route}{dose}"),
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                label=label,
                color=color,
                marker=self.dose_markers[dosing],
            )
            plot.add_data(task=task_id, xid="time", yid=yid, label=label, color=color)

    @override
    def figures(self) -> dict[str, Figure]:
        dosings = [f"po{dose}" for dose in self.doses_po] + [
            f"iv{dose}" for dose in self.doses_iv
        ]

        # all doses: metoprolol, the metabolites, the excretion and the heart rate
        fig1, plots = fig_metoprolol(
            self, fig_id="Fig1", name=f"{self.sid} (metoprolol tartrate PO and IV)"
        )
        for dosing in dosings:
            self.add_dose(plots[0], plots[5], dosing)
            task_id = self.to_sid(f"task_met_{dosing}")
            color = self.dose_colors[dosing]
            for k, sid in enumerate(["met", "metoh", "mam"]):
                if k > 0:
                    plots[k].add_data(
                        task=task_id,
                        xid="time",
                        yid=f"[Cveplasma_{sid}]",
                        label=self.dose_label(dosing),
                        color=color,
                    )
                # the substances are labeled once, the doses have their colors
                plots[3].add_data(
                    task=task_id,
                    xid="time",
                    yid=f"KI__{sid.upper()}EX",
                    label=f"{self.dose_label(dosing)} {sid}"
                    if dosing == "po100"
                    else None,
                    color=color,
                    linestyle=EXCRETION_LINESTYLES[sid],
                )
            plots[4].add_data(
                task=task_id,
                xid="time",
                yid="HReff",
                label=self.dose_label(dosing),
                color=color,
            )

        # oral and intravenous doses: metoprolol and the reduction of the heart
        # rate
        figs = {"fig1": fig1}
        # the oral data reach 12 hr, the intravenous data 6.5 hr
        for fig_id, route, name, tend in [
            ("Fig2", "po", "oral", 12),
            ("Fig3", "iv", "intravenous, 10 min infusion", 8),
        ]:
            fig, plots_route = fig_metoprolol_met_hrreduction(
                self, fig_id=fig_id, name=f"{self.sid} ({name})"
            )
            for plot in plots_route:
                plot.set_xaxis(self.label_time, self.unit_time, min=0, max=tend)
            for dosing in dosings:
                if dosing.startswith(route):
                    self.add_dose(plots_route[0], plots_route[1], dosing)
            if route == "po":
                plots_route[1].add_data(
                    dataset="fig2_placebo",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    label="placebo",
                    color="tab:gray",
                    marker="x",
                )
            figs[f"fig_{route}"] = fig

        return figs


if __name__ == "__main__":
    MODEL.run_experiments(Johnsson1975, output_dir="test")
