"""Simulation experiment of the absorption of the application forms of metoprolol."""

from typing import override

from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.metoprolol import MODEL
from pkdb_models.models.metoprolol.experiments.base_experiment import (
    MetoprololSimulationExperiment,
)


class AbsorptionExperiment(MetoprololSimulationExperiment):
    """The absorption of the application forms of metoprolol.

    Two oral doses of 100 mg metoprolol tartrate 12 hr apart as immediate
    release (IR), slow release (SR) and controlled release (CR) tablets: the
    undissolved dose (`PODOSE_met`), the dissolved dose in the gut
    (`GUTDOSE_met`) and metoprolol in plasma.
    """

    @override
    def simulations(self) -> dict[str, Simulation]:
        dose = self.dose_base(100, "tartrate")
        return {
            f"met_{application}": Simulation(
                time_unit="hr",
                end=2 * 12,
                preinit_changes={
                    **self.default_changes(),
                    **self.application_changes(application),
                    "PODOSE_met": dose,
                },
                changes=[self.oral_doses([12], dose)],
            )
            for application in self.application_types
        }

    @override
    def figures(self) -> dict[str, Figure]:
        fig1 = Figure(
            experiment=self, sid="Fig1", num_rows=3, num_cols=1, name=self.sid
        )
        plots = fig1.create_plots(xaxis=Axis("time", unit="hr"), legend=True)
        plots[0].set_yaxis("metoprolol plasma", unit="nM")
        plots[1].set_yaxis("undissolved dose", unit="mg")
        plots[2].set_yaxis("dissolved dose (gut)", unit="mg")

        for application in self.application_types:
            task_id = f"task_met_{application}"
            color = self.colors[application]
            for k, yid in enumerate(["[Cveplasma_met]", "PODOSE_met", "GUTDOSE_met"]):
                plots[k].add_data(
                    task=task_id,
                    xid="time",
                    yid=yid,
                    label=application.upper(),
                    color=color,
                )

        return {"fig1": fig1}


if __name__ == "__main__":
    MODEL.run_experiments(AbsorptionExperiment, output_dir="test")
