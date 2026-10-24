"""Parameter scans of metoprolol: the dose, the renal function and CYP2D6."""

from collections.abc import Mapping
from typing import ClassVar, NotRequired, TypedDict, override

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.colors import Colormap
from matplotlib.typing import ColorType
from pkpdsim.scan import point_band, point_timecourse, scan_dimensions, start_values
from sbmlsim import Q
from sbmlsim.plot.serialization_matplotlib import FigureMPL
from sbmlsim.result import ScanResult
from sbmlsim.simulation import Dimension, Scan, Simulation
from sbmlsim.units import Quantity

from pkdb_models.models.metoprolol import MODEL
from pkdb_models.models.metoprolol.experiments.base_experiment import (
    MetoprololSimulationExperiment,
)
from pkdb_models.models.metoprolol.metoprolol_pk import summarize


class ScanSpec(TypedDict):
    """Definition of a parameter scan."""

    parameter: str
    #: the values of the parameter, which contain the reference
    range: np.ndarray
    units: str
    #: the value of the scan in the simulations of the other scans
    reference: float
    label: str
    #: a logarithmic axis of the scanned parameter
    log: bool
    #: the colormap from the lowest to the highest value
    colormap: str
    #: the scanned value per value of the axis, e.g. the dose of metoprolol per
    #: dose of metoprolol tartrate; 1 by default
    factor: NotRequired[float]


_TARTRATE = (
    (
        MetoprololSimulationExperiment.Mr.met
        / MetoprololSimulationExperiment.Mr.met_tartrate
    )
    .to("dimensionless")
    .magnitude
)


class MetoprololParameterScan(MetoprololSimulationExperiment):
    """Scan the effect of parameters on the pharmacokinetics and the heart rate.

    A single oral dose of 100 mg metoprolol tartrate (78.1 mg metoprolol) as
    an immediate release tablet in a CYP2D6 activity score of 2 (*1/*1) at
    rest, followed for 10 days (the half-life is 3 hr, 12 hr in poor
    metabolizers, 57 hr of metoprolol acid at a renal function of 0.1).
    Scanned are the dose (25 to 400 mg tartrate), the renal function (0.1 to
    10, logarithmic) and the CYP2D6 activity score (0, poor, to 3, ultrarapid
    metabolizers); the figures show the first 2 days of the timecourses of
    metoprolol and its metabolites in plasma, their urinary excretion and the
    heart rate, and the pharmacokinetic parameters of the non-compartmental
    analysis (`metoprolol_pk`) and the maximal reduction of the heart rate over
    the scanned parameter.

    In a run over the draws of the fitted parameters (`run_simulation
    pkdb_models.models.metoprolol --uncertainty`) every point of a scan is
    simulated for every draw; the figures draw the median of the draws with the
    band of their quantiles.
    """

    #: the end of the simulations [hr]: the half-life of metoprolol acid is
    #: 57 hr at the lowest renal function of the scan
    tend = 240
    #: the output times [hr]: every 0.05 hr in the first day (absorption and
    #: maximum, tmax about 1.5 hr), every 0.5 hr after it
    times: ClassVar[tuple[float, ...]] = tuple(
        np.unique(
            np.concatenate([np.linspace(0, 24, 481), np.linspace(24, tend, 433)])
        ).tolist()
    )
    #: the end of the time axis of the timecourses [hr]
    tend_plot = 48
    #: the opacity of the bands of the draws
    band_alpha = 0.15
    #: the dose of metoprolol tartrate of the scans [mg]
    dose_tartrate = 100

    selections = (*MetoprololSimulationExperiment.selections, "LI__cyp2d6_ac")

    #: the variables of the timecourses
    timecourses: ClassVar[tuple[str, ...]] = (
        "[Cveplasma_met]",
        "[Cveplasma_metoh]",
        "[Cveplasma_mam]",
        "HReff",
        "Aurine_met",
        "Aurine_metoh",
        "Aurine_mam",
        "HRred",
    )
    #: the pharmacokinetic parameters of the analytes of `metoprolol_pk`
    pk_parameters: ClassVar[dict[str, tuple[str, ...]]] = {
        "met": ("auc_inf_obs", "cmax", "tmax", "thalf", "cl_f"),
        "metoh": ("auc_inf_obs", "cmax", "tmax", "thalf"),
        "mam": ("auc_inf_obs", "cmax", "tmax", "thalf"),
    }
    pk_names: ClassVar[dict[str, str]] = {
        "met": "metoprolol plasma",
        "metoh": "alpha-OH metoprolol plasma",
        "mam": "metoprolol acid plasma",
    }
    pk_labels: ClassVar[Mapping[str, str]] = {
        "auc_inf_obs": "AUC",
        "cmax": "Cmax",
        "tmax": "Tmax",
        "thalf": "Half-life",
        "cl_f": "CL/F",
        "max_hrred": "max HR reduction",
    }
    pk_units: ClassVar[Mapping[str, str]] = {
        "auc_inf_obs": "nmole/l*hr",
        "cmax": "nmole/l",
        "tmax": "hr",
        "thalf": "hr",
        "cl_f": "l/min",
        "max_hrred": "percent",
    }

    scan_map: ClassVar[dict[str, ScanSpec]] = {
        "dose": {
            "parameter": "PODOSE_met",
            "range": _TARTRATE * np.array([25, 50, 100, 150, 200, 300, 400]),
            "units": "mg",
            "reference": _TARTRATE * dose_tartrate,
            "label": "metoprolol tartrate dose [mg]",
            "log": False,
            "colormap": "viridis_r",
            "factor": _TARTRATE,
        },
        "renal": {
            "parameter": "KI__f_renal_function",
            "range": np.logspace(-1, 1, num=11),
            "units": "dimensionless",
            "reference": 1.0,
            "label": "renal function [-]",
            "log": True,
            "colormap": "seismic_r",
        },
        "cyp2d6": {
            "parameter": "LI__cyp2d6_ac",
            "range": np.linspace(0, 3, num=13),
            "units": "dimensionless",
            "reference": 2.0,
            "label": "CYP2D6 activity score [-]",
            "log": False,
            "colormap": "coolwarm",
        },
    }

    font: ClassVar[dict[str, str | int]] = {"weight": "bold", "size": 15}
    tick_font_size = 13

    def _reference_changes(self) -> dict[str, Quantity | float]:
        """Get the changes of the reference: the dose, *1/*1 as activity score 2."""
        return {
            **self.default_changes(),
            **self.application_changes("ir"),
            **self.cyp2d6_changes(self.scan_map["cyp2d6"]["reference"]),
            "PODOSE_met": Q(self.scan_map["dose"]["reference"], "mg"),
        }

    @override
    def simulations(self) -> dict[str, Scan]:
        return {
            f"scan_{key}": Scan(
                simulation=Simulation(
                    time_unit="hr",
                    end=self.tend,
                    times=self.times,
                    preinit_changes=self._reference_changes(),
                ),
                dimensions=[
                    Dimension(
                        "dim_scan",
                        values={spec["parameter"]: Q(spec["range"], spec["units"])},
                    ),
                ],
            )
            for key, spec in self.scan_map.items()
        }

    def _across(self) -> str | None:
        """Get the dimension of the draws of the fitted parameters, `None` without."""
        return None if self.uncertainty is None else self.uncertainty.id

    def _axis_values(self, res: ScanResult, spec: ScanSpec) -> np.ndarray:
        """Get the values of the axis of the scanned parameter at the points."""
        pid = spec["parameter"]
        values = start_values(res, pid)
        across = self._across()
        if across is not None:
            values = values.isel({across: 0})
        scanned = Q(values.values, res.units[pid]).to(spec["units"]).magnitude
        return np.asarray(scanned, dtype=float) / spec.get("factor", 1.0)

    def _color(self, spec: ScanSpec, value: float, cmap: Colormap) -> ColorType:
        """Get the color of a value of a scan, black for the reference."""
        factor = spec.get("factor", 1.0)
        if np.isclose(value * factor, spec["reference"]):
            return "black"
        values = spec["range"] / factor
        vmin, vmax = float(np.min(values)), float(np.max(values))
        if spec["log"]:
            position = (np.log10(value) - np.log10(vmin)) / (
                np.log10(vmax) - np.log10(vmin)
            )
        else:
            position = (value - vmin) / (vmax - vmin)
        return cmap(float(position))

    def _timecourse(
        self, ax: Axes, res: ScanResult, sid: str, index: int, color: ColorType
    ) -> tuple[np.ndarray, np.ndarray, float]:
        """Get the timecourse of a point of a scan, drawing the band of its draws.

        Returns:
            The time and the values in the units of the figure, the median of
            the draws in a run over them, and the maximum of the values or of
            the band.
        """
        (scandim,) = scan_dimensions(res, self._across())
        run = self.uncertainty
        if run is None:
            time, values = point_timecourse(res, sid, **{scandim: index})
        else:
            time, lower, values, upper = point_band(
                res, sid, across=run.id, quantiles=run.quantiles, **{scandim: index}
            )
        unit = self._unit(sid)
        t_vec = Q(time, res.units["time"]).to(self.units["time"]).magnitude
        c_vec = Q(values, res.units[sid]).to(unit).magnitude
        top = float(np.nanmax(c_vec))
        if run is not None:
            upper_vec = Q(upper, res.units[sid]).to(unit).magnitude
            ax.fill_between(
                t_vec,
                Q(lower, res.units[sid]).to(unit).magnitude,
                upper_vec,
                color=color,
                alpha=self.band_alpha,
                linewidth=0,
            )
            top = max(top, float(np.nanmax(upper_vec)))
        return t_vec, c_vec, top

    def _unit(self, sid: str) -> str:
        """Get the unit of a variable in the figures, the reduction in percent."""
        return "percent" if sid == "HRred" else self.units[sid]

    def _max_hrred(self, res: ScanResult) -> pd.DataFrame:
        """Get the maximal reduction of the heart rate of every point of a scan.

        Returns:
            One row per point (and draw), the columns `point`, `draw` (with
            draws), `max_hrred` and `max_hrred_unit`.
        """
        across = self._across()
        (scandim,) = scan_dimensions(res, across)
        draws = range(res.ds.sizes[across]) if across is not None else [None]
        rows = []
        for point in range(res.ds.sizes[scandim]):
            for draw in draws:
                position = {scandim: point}
                if across is not None and draw is not None:
                    position[across] = draw
                _, values = point_timecourse(res, "HRred", **position)
                rows.append(
                    {
                        "point": point,
                        **({"draw": draw} if draw is not None else {}),
                        "max_hrred": float(np.nanmax(values)),
                        "max_hrred_unit": str(res.units["HRred"]),
                    }
                )
        return pd.DataFrame(rows)

    def _summary(
        self, df: pd.DataFrame, key: str, target: str
    ) -> tuple[np.ndarray, np.ndarray | None, np.ndarray | None]:
        """Get a parameter at the points of a scan, the median and the band of the draws.

        Returns:
            The values (the median of the draws in a run over them), and the
            lower and the upper quantile, `None` without draws.
        """
        unit = df[f"{key}_unit"].iloc[0]
        run = self.uncertainty
        if run is None:
            return (
                Q(df[key].to_numpy(dtype=float), unit).to(target).magnitude,
                None,
                None,
            )
        summary = summarize(df, key, run.quantiles)
        median, lower, upper = (
            Q(summary[column].to_numpy(), unit).to(target).magnitude
            for column in ["median", "lower", "upper"]
        )
        return median, lower, upper

    @override
    def figures_mpl(self) -> dict[str, FigureMPL]:
        figures: dict[str, FigureMPL] = {}
        pk_dfs = self.calculate_metoprolol_pk(
            scans=[f"scan_{key}" for key in self.scan_map]
        )
        for key, spec in self.scan_map.items():
            res = self.results[f"task_scan_{key}"]
            figures[f"fig_timecourse_{key}"] = self._figure_timecourses(key, spec, res)
            figures[f"fig_pk_{key}"] = self._figure_pharmacokinetics(
                spec, res, pk_dfs[f"scan_{key}"]
            )
        return figures

    def _figure_timecourses(
        self, key: str, spec: ScanSpec, res: ScanResult
    ) -> FigureMPL:
        """Timecourses of a scan, the reference in black.

        Raises:
            ValueError: if the reference is not a point of the scan.
        """
        cmap = matplotlib.colormaps[spec["colormap"]]
        x_vec = self._axis_values(res, spec)
        factor = spec.get("factor", 1.0)
        references = [
            k for k, x in enumerate(x_vec) if np.isclose(x * factor, spec["reference"])
        ]
        if not references:
            raise ValueError(f"The reference is not a point of the scan '{key}'.")

        ncols = 4
        nrows = (len(self.timecourses) + ncols - 1) // ncols
        f: FigureMPL
        f, axes = plt.subplots(
            nrows=nrows, ncols=ncols, figsize=(5.5 * ncols, 5 * nrows)
        )
        f.subplots_adjust(wspace=0.4, hspace=0.35)
        f.suptitle(
            f"Scan {spec['label']}: reference black", fontsize=20, fontweight="bold"
        )
        for ax, sid in zip(axes.flatten(), self.timecourses, strict=True):
            ymax = 0.0
            # the reference last, on top
            for index in [k for k in range(len(x_vec)) if k not in references] + [
                references[0]
            ]:
                color = self._color(spec, float(x_vec[index]), cmap)
                t_vec, c_vec, top = self._timecourse(ax, res, sid, index, color)
                ymax = max(ymax, top)
                ax.plot(t_vec, c_vec, color=color, linewidth=2.0)
            ax.set_xlim(0, self.tend_plot)
            ax.set_ylim(bottom=0.0, top=1.05 * ymax if ymax > 0 else 1.0)
            ax.tick_params(axis="both", labelsize=self.tick_font_size)
            ax.set_xlabel(
                f"{self.label_time} [{self.units['time']}]", fontdict=self.font
            )
            ax.set_ylabel(f"{self.labels[sid]} [{self._unit(sid)}]", fontdict=self.font)
        return f

    def _figure_pharmacokinetics(
        self, spec: ScanSpec, res: ScanResult, df: pd.DataFrame
    ) -> FigureMPL:
        """Pharmacokinetic parameters of the analytes and the maximal reduction of the heart rate."""
        x_vec = self._axis_values(res, spec)
        ncols = max(len(parameters) for parameters in self.pk_parameters.values())
        nrows = len(self.pk_parameters)
        f: FigureMPL
        f, axes = plt.subplots(
            nrows=nrows, ncols=ncols, figsize=(5 * ncols, 4.5 * nrows)
        )
        f.subplots_adjust(wspace=0.45, hspace=0.45)
        f.suptitle(
            f"Scan {spec['label']}: pharmacokinetics", fontsize=20, fontweight="bold"
        )
        hrred = self._max_hrred(res)
        reference = spec["reference"] / spec.get("factor", 1.0)
        for krow, (substance, parameters) in enumerate(self.pk_parameters.items()):
            df_substance = df[df["substance"] == substance]
            panels: list[tuple[str, pd.DataFrame, str]] = [
                (key, df_substance, self.pk_names[substance]) for key in parameters
            ]
            # the reduction of the heart rate in the free panel of the
            # first metabolite
            if substance == "metoh":
                panels.append(("max_hrred", hrred, "heart rate"))
            for kcol in range(ncols):
                ax: Axes = axes[krow, kcol]
                if kcol >= len(panels):
                    ax.set_axis_off()
                    continue
                key, data, name = panels[kcol]
                target = self.pk_units[key]
                y_vec, y_lower, y_upper = self._summary(data, key, target)
                if y_lower is not None and y_upper is not None:
                    ax.fill_between(
                        x_vec,
                        y_lower,
                        y_upper,
                        color="black",
                        alpha=self.band_alpha,
                        linewidth=0,
                    )
                    top = float(np.nanmax(y_upper))
                else:
                    top = float(np.nanmax(y_vec))
                ax.axvline(x=reference, color="grey", linestyle="--")
                ax.plot(
                    x_vec,
                    y_vec,
                    marker="o",
                    linestyle="-",
                    color="black",
                    markeredgecolor="black",
                )
                if spec["log"]:
                    ax.set_xscale("log")
                # a margin above keeps a constant curve inside the axes
                ax.set_ylim(bottom=0.0, top=1.1 * top if top > 0 else 1.0)
                ax.tick_params(axis="both", labelsize=self.tick_font_size)
                ax.set_title(name, fontsize=13)
                ax.set_xlabel(spec["label"], fontdict=self.font)
                ax.set_ylabel(f"{self.pk_labels[key]} [{target}]", fontdict=self.font)
        return f


if __name__ == "__main__":
    MODEL.run_experiments(MetoprololParameterScan, output_dir="scan_parameters")
