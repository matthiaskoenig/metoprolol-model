"""Simulation experiment of the effect of exercise on the heart rate."""

from typing import override

from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.metoprolol import MODEL
from pkdb_models.models.metoprolol.experiments.base_experiment import (
    MetoprololSimulationExperiment,
)
from pkdb_models.models.metoprolol.experiments.figure_templates import (
    EXCRETION_LINESTYLES,
)

#: the names of metoprolol and its metabolites in the legends
METABOLITE_NAMES: dict[str, str] = {
    "met": "metoprolol",
    "metoh": "alpha-OH metoprolol",
    "mam": "metoprolol acid",
}


class EHRExperiment(MetoprololSimulationExperiment):
    """Simulate effect of exercise on heart rate.

    EHR: exercise heart rate
    """

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}

        # a day without metoprolol, 200 mg metoprolol tartrate (2 tablets of
        # 100 mg, 156 mg metoprolol) at 24 and 48 hr and two days after the
        # last dose
        dose = self.dose_base(200, "tartrate")
        for exercise in self.exercise_types:
            tcsims[f"met200_{exercise}"] = Simulation(
                time_unit="hr",
                end=4 * 24,
                preinit_changes={
                    **self.default_changes(),
                    **self.application_changes("ir"),
                    **self.metabolizer_changes("em"),
                    **self.exercise_changes(exercise),
                },
                changes=[self.oral_doses([24, 48], dose)],
            )

        return tcsims

    @override
    def figures(self) -> dict[str, Figure]:
        fig1 = Figure(
            experiment=self, sid="Fig1", num_rows=3, num_cols=2, name=self.sid
        )
        plots = fig1.create_plots(
            xaxis=Axis("time", unit="hr", min=0),
            legend=True,
        )
        plots[0].set_yaxis("metoprolol", unit="µM")
        plots[1].set_yaxis("alpha-hydroxymetoprolol\n", unit="µM")
        plots[2].set_yaxis("metoprolol acid", unit="µM")
        plots[3].set_yaxis("urinary excretion rate\n", unit="µmole/min")
        plots[4].set_yaxis("heart rate", unit="1/min")
        plots[5].set_yaxis("HR reduction", unit="percent", min=30, max=0)

        # the time axis is labeled in the bottom row
        for plot in plots[:4]:
            if plot.xaxis is not None:
                plot.xaxis.label_visible = False

        for exercise in self.exercise_types:
            task_id = f"task_met200_{exercise}"

            linestyle = "-" if task_id.endswith("no") else "--"
            for k, sid in enumerate(["met", "metoh", "mam"]):
                # simulations
                plots[k].add_data(
                    task=task_id,
                    xid="time",
                    yid=f"[Cveplasma_{sid}]",
                    label=f"{METABOLITE_NAMES[sid]} ({exercise})",
                    color=self.colors[exercise],
                    linestyle=linestyle,
                )
                plots[3].add_data(
                    task=task_id,
                    xid="time",
                    yid=f"KI__{sid.upper()}EX",
                    label=f"{METABOLITE_NAMES[sid]} ({exercise})",
                    color=self.colors[exercise],
                    linestyle=EXCRETION_LINESTYLES[sid],
                )

            plots[4].add_data(
                task=task_id,
                xid="time",
                yid="HReff",
                label=f"HReff ({exercise})",
                color=self.colors[exercise],
                linestyle=linestyle,
            )

            plots[5].add_data(
                task=task_id,
                xid="time",
                yid="HRred",
                label=f"HR reduction ({exercise})",
                color=self.colors[exercise],
                linestyle=linestyle,
            )
        return {
            "fig1": fig1,
        }


if __name__ == "__main__":
    MODEL.run_experiments(EHRExperiment, output_dir="test")
