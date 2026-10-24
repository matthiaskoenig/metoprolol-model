"""Simulation experiment of intravenous doses of metoprolol."""

from typing import override

from sbmlsim import Q
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.metoprolol import MODEL
from pkdb_models.models.metoprolol.experiments.base_experiment import (
    MetoprololSimulationExperiment,
)


class DosingExperiment(MetoprololSimulationExperiment):
    """An intravenous dose of metoprolol as a bolus and as a 10 min infusion.

    10 mg metoprolol tartrate (7.8 mg base), the dose of Johnsson1975 and
    Regardh1974: metoprolol in plasma and blood and its urinary excretion.
    """

    @override
    def simulations(self) -> dict[str, Simulation]:
        dose = self.dose_base(10, "tartrate")
        infusion, changes = self.iv_infusion(dose, duration=Q(10, "min"))
        return {
            "met_bolus": Simulation(
                time_unit="hr",
                end=24,
                preinit_changes={**self.default_changes(), "IVDOSE_met": dose},
            ),
            "met_infusion": Simulation(
                time_unit="hr",
                end=24,
                preinit_changes={**self.default_changes(), **infusion},
                changes=changes,
            ),
        }

    @override
    def figures(self) -> dict[str, Figure]:
        fig1 = Figure(
            experiment=self, sid="Fig1", num_rows=1, num_cols=3, name=self.sid
        )
        plots = fig1.create_plots(xaxis=Axis("time", unit="hr"), legend=True)
        plots[0].set_yaxis("metoprolol plasma", unit="nM")
        plots[1].set_yaxis("metoprolol blood", unit="nM")
        plots[2].set_yaxis("metoprolol urine", unit="µmole")

        for task_id, label, linestyle in [
            ("task_met_bolus", "bolus", ":"),
            ("task_met_infusion", "infusion 10 min", "-"),
        ]:
            for k, yid in enumerate(["[Cveplasma_met]", "[Cve_met]", "Aurine_met"]):
                plots[k].add_data(
                    task=task_id,
                    xid="time",
                    yid=yid,
                    label=label,
                    color="black",
                    linestyle=linestyle,
                )

        return {"fig1": fig1}


if __name__ == "__main__":
    MODEL.run_experiments(DosingExperiment, output_dir="test")
