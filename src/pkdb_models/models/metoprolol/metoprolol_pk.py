"""Pharmacokinetic parameters of the metoprolol scans.

The parameters are the non-compartmental analysis of `pkpdutils`, named like
the variables of its `NCAResult` (e.g. `auc_inf_obs`, `cmax`, `thalf`,
`lambda_z`, `cl_f`, `vz_f`), with the unit of every parameter in
`<name>_unit`. Metoprolol is analysed in plasma with its dose (oral, an oral
solution or intravenous), its metabolites alpha-hydroxymetoprolol and
metoprolol acid without a dose, i.e., without clearance and volume. The
concentrations below `LLOQ_FRACTION` of the maximum are below the limit of
quantification, so that the noise of the integrator is not the terminal phase.

A scan has one dimension, the scanned parameter; a run over the draws of the
fitted parameters (`run_simulation pkdb_models.models.metoprolol --uncertainty`)
adds the dimension of the draws. The parameters are calculated for every point
of every dimension, a row per point with its position along each dimension
(the columns `point` and, with draws, `draw`), see `summarize`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
import pandas as pd
from pkpdsim.pk import nca_frame, scan_nca
from pkpdsim.scan import scan_dimensions, start_values
from pkpdutils import Route
from sbmlsim import Q
from sbmlsim.result import ScanResult

if TYPE_CHECKING:
    from pkdb_models.models.metoprolol.experiments.base_experiment import (
        MetoprololSimulationExperiment,
    )

#: the doses of the scans by their route: the oral dose, the dissolved oral
#: dose (a solution) and the intravenous dose
DOSES: dict[str, Route] = {
    "PODOSE_met": Route.ORAL,
    "GUTDOSE_met": Route.ORAL,
    "IVDOSE_met": Route.IV_BOLUS,
}
#: the analytes -> their plasma concentration and whether the dose is theirs
ANALYTES: dict[str, tuple[str, bool]] = {
    "met": ("[Cveplasma_met]", True),
    "metoh": ("[Cveplasma_metoh]", False),
    "mam": ("[Cveplasma_mam]", False),
}
#: the limit of quantification relative to the maximal concentration
LLOQ_FRACTION = 1e-4


def _doses(
    experiment: MetoprololSimulationExperiment, res: ScanResult
) -> tuple[np.ndarray, np.ndarray]:
    """Get the dose of every simulation of a scan and its route.

    The dose is the first of `DOSES` at the start of the simulation, in the
    substance unit of the concentration, which `cl_f` and `vz_f` require.

    Returns:
        The amounts [mmole] and the routes over the dimensions of the scan,
        `NaN` and `None` for a simulation without a dose.
    """
    shape = tuple(res.ds.sizes[dim] for dim in res.dims)
    amounts = np.full(shape, np.nan)
    routes = np.full(shape, None, dtype=object)
    # in reverse, so that the first dose of `DOSES` wins
    for key, route in reversed(DOSES.items()):
        mass = Q(start_values(res, key).values, res.units[key])
        given = mass.magnitude > 0
        amounts = np.where(
            given, (mass / experiment.Mr.met).to("mmole").magnitude, amounts
        )
        routes[given] = route
    return amounts, routes


def pk_parameters(
    experiment: MetoprololSimulationExperiment,
    res: ScanResult,
    substance: str,
) -> pd.DataFrame:
    """Calculate the pharmacokinetic parameters of an analyte in every simulation of a scan.

    The non-compartmental analysis of all simulations with a dose of one route
    at once (`scan_nca`), and of all simulations without a dose (the
    metabolites) at once.

    Args:
        experiment: experiment of the scan, for the molecular weight of the
            dose.
        res: result of the scan.
        substance: the analyte, a key of `ANALYTES`.

    Returns:
        One row per simulation of the scan (in the order of the dimensions of
        the scan), with its position along every dimension (a column named
        after the dimension), `substance`, the parameters and their units
        (`<name>_unit`).
    """
    concentration, with_dose = ANALYTES[substance]
    shape = tuple(res.ds.sizes[dim] for dim in res.dims)
    amounts, routes = (
        _doses(experiment, res)
        if with_dose
        else (np.full(shape, np.nan), np.full(shape, None, dtype=object))
    )
    # an analysis per route (in the order of the first simulation of a route),
    # of which the simulations of the route are taken
    labels = routes.ravel()
    frames = []
    for route in dict.fromkeys(labels):
        result = scan_nca(
            res,
            concentration,
            dose=None if route is None else Q(amounts, "mmole"),
            route=route,
            substance=substance,
            lloq_fraction=LLOQ_FRACTION,
        )
        df = nca_frame(result).drop(columns="nca_flags")
        frames.append(df[labels == route])
    df = pd.concat(frames).sort_index()
    df.insert(len(res.dims), "substance", substance)
    return df


def calculate_metoprolol_pk(
    experiment: MetoprololSimulationExperiment,
    res: ScanResult,
    across: str | None = None,
) -> pd.DataFrame:
    """Calculate the pharmacokinetic parameters of every simulation of a scan.

    Args:
        experiment: experiment of the scan.
        res: result of the scan.
        across: the dimension of the draws of the fitted parameters, `None`
            for a scan without draws.

    Returns:
        One row per simulation of the scan and analyte, with its position
        (`point`, and `draw` with draws).

    Raises:
        ValueError: if the scan has not one dimension besides the draws.
    """
    dims = scan_dimensions(res, across)
    if len(dims) != 1:
        raise ValueError(
            f"A scan of one dimension is required, not of {dims} (draws: {across})."
        )
    names = {dims[0]: "point", **({across: "draw"} if across is not None else {})}
    return pd.concat(
        [
            pk_parameters(experiment, res, substance).rename(columns=names)
            for substance in ANALYTES
        ],
        ignore_index=True,
    )


def summarize(
    df: pd.DataFrame, key: str, quantiles: tuple[float, float]
) -> pd.DataFrame:
    """Get the median and the quantiles of a parameter over the draws of every point.

    Args:
        df: the parameters with the columns `point` and `draw`.
        key: the parameter.
        quantiles: the lower and the upper quantile.

    Returns:
        One row per point (the index), the columns `lower`, `median`, `upper`.
    """
    low, high = quantiles
    grouped = df.groupby("point")[key]
    return pd.DataFrame(
        {
            "lower": grouped.quantile(low),
            "median": grouped.median(),
            "upper": grouped.quantile(high),
        }
    ).astype(np.float64)
