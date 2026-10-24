"""Templates of the figures of the metoprolol experiments."""

from sbmlsim.plot import Axis, Figure, Plot

from pkdb_models.models.metoprolol.experiments.base_experiment import (
    MetoprololSimulationExperiment,
)

#: line styles of the urinary excretion rates of metoprolol and its metabolites,
#: which tell the substances of a group apart. The panel of the excretion shows
#: the simulations without exercise, unless the exercise is the group: dashed
#: lines are the exercise in the other panels.
EXCRETION_LINESTYLES: dict[str, str] = {"met": "-", "metoh": "-.", "mam": ":"}


def fig_metoprolol(
    experiment: MetoprololSimulationExperiment, fig_id: str, name: str | None = None
) -> tuple[Figure, list[Plot]]:
    """Get the figure of metoprolol, its metabolites, excretion and heart rate.

    The panels are metoprolol, alpha-hydroxymetoprolol and metoprolol acid in
    plasma, the urinary excretion rates, the heart rate and its reduction.
    """
    if not name:
        name = experiment.sid
    fig = Figure(
        experiment=experiment,
        sid=experiment.to_sid(fig_id),
        num_rows=3,
        num_cols=2,
        name=name,
    )
    plots = fig.create_plots(
        xaxis=Axis(experiment.label_time, experiment.unit_time),
        legend=True,
    )
    plots[0].set_yaxis(experiment.label_met, experiment.unit_met)
    plots[1].set_yaxis(experiment.label_metoh, experiment.unit_metoh)
    plots[2].set_yaxis(experiment.label_mam, experiment.unit_mam)
    plots[3].set_yaxis(experiment.label_excretion, experiment.unit_excretion)
    plots[4].set_yaxis(experiment.label_hr, experiment.unit_hr)
    plots[5].set_yaxis(
        experiment.label_hrreduction, experiment.unit_hrreduction, min=35, max=0
    )

    # the time axis is labeled in the bottom row, the concentrations start at 0
    for k in range(4):
        plots[k].set_xaxis(
            experiment.label_time,
            experiment.unit_time,
            label_visible=False,
            min=0 if k < 2 else None,
        )

    return fig, plots


def fig_metoprolol_met_hrreduction(
    experiment: MetoprololSimulationExperiment, fig_id: str, name: str | None = None
) -> tuple[Figure, list[Plot]]:
    """Get the figure of metoprolol in plasma and the reduction of the heart rate."""
    if not name:
        name = experiment.sid
    fig = Figure(
        experiment=experiment,
        sid=experiment.to_sid(fig_id),
        num_rows=1,
        num_cols=2,
        name=name,
    )
    plots = fig.create_plots(
        xaxis=Axis(experiment.label_time, experiment.unit_time),
        legend=True,
    )
    plots[0].set_yaxis(experiment.label_met, experiment.unit_met)
    plots[1].set_yaxis(
        experiment.label_hrreduction, experiment.unit_hrreduction, min=35, max=0
    )

    return fig, plots
