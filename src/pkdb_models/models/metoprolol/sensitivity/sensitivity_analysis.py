"""Sensitivity analysis of the metoprolol model.

The outputs are the pharmacokinetic parameters of metoprolol and its
metabolites alpha-hydroxymetoprolol and metoprolol acid in plasma after a single
oral dose of 100 mg metoprolol tartrate as an immediate release tablet (the
non-compartmental analysis of `pkpdutils`) and the maximal reduction of the
heart rate. The parameters are the parameters of the model with bounds of
+-15 % around their value. The analyses are run as a script, the local analysis
by default:

    python -m pkdb_models.models.metoprolol.sensitivity.sensitivity_analysis
    python -m pkdb_models.models.metoprolol.sensitivity.sensitivity_analysis local sampling

The analyses run on `pkpdsim.sensitivity.SensitivityRunner`, which writes the
table of the parameters into `results/sensitivity` of the model and the tables
and figures of an analysis into `results/sensitivity/<analysis>`.
An analysis does not vary a parameter which one of its groups sets
(`pkpdsim.sensitivity.free_parameters`): `sampling`, over the groups, leaves out
`KI__f_renal_function` and the CYP2D6 activity of the diplotype. The
environment variable `PKPDSIM_SENSITIVITY_N` replaces the numbers of samples of
the global analyses for a quick run, see `pkpdsim.sensitivity.sample_size`.

The model without metoprolol is stationary, so the simulation of a group starts
with the dose. The dose is followed for `END_HR` hours, long enough for the
terminal phase of metoprolol acid in severe renal impairment and of metoprolol
in poor metabolizers (half-lives of about 25 hr and 12 hr).
"""

from collections.abc import Callable, Mapping

import numpy as np
from pkpdsim.sensitivity import (
    FastAnalysis,
    LocalAnalysis,
    ParameterType,
    SamplingAnalysis,
    SensitivityGroup,
    SensitivityOutput,
    SensitivityParameter,
    SensitivityRunner,
    SobolAnalysis,
    parameters_from_sbml,
    set_bounds,
    set_relative_bounds,
)
from pkpdutils import NCAOptions
from sbmlsim import Q
from sbmlsim.simulation import PK, Custom, Formula, Simulation

from pkdb_models.models.metoprolol import MODEL, MODEL_PATH
from pkdb_models.models.metoprolol.experiments.base_experiment import (
    MetoprololSimulationExperiment,
)
from pkdb_models.models.metoprolol.fitting.parameters import (
    parameters_pd,
    parameters_pk,
)
from pkdb_models.models.metoprolol.models.model_cyp2d6 import ALLELE_ACTIVITIES

#: oral dose of metoprolol of the analysis [mg], 100 mg metoprolol tartrate
DOSE_MET = 100 * float(
    (
        MetoprololSimulationExperiment.Mr.met
        / MetoprololSimulationExperiment.Mr.met_tartrate
    )
    .to("dimensionless")
    .magnitude
)
#: the hours after the dose
END_HR = 168
#: the limit of quantification of the non-compartmental analysis [mM], about
#: 1e-6 of the maximal concentrations of metoprolol (4e-4 mM) and
#: alpha-hydroxymetoprolol (2e-4 mM) after the dose, so that the noise of the
#: integrator is not the terminal phase
LLOQ = 1e-10
#: fraction of the bounds of a parameter relative to its value
BOUNDS_FRACTION = 0.15

#: outputs of the non-compartmental analysis of metoprolol -> unit of the output
PK_OUTPUTS_MET: dict[str, str] = {
    "auc_inf_obs": "mM*min",
    "cmax": "mM",
    "tmax": "min",
    "thalf": "min",
    "vz_f": "l",
    "cl_f": "ml/min",
}
#: outputs of the non-compartmental analysis of the metabolites, without a
#: dose: no clearance or volume -> unit of the output
PK_OUTPUTS_METABOLITE: dict[str, str] = {
    "auc_inf_obs": "mM*min",
    "cmax": "mM",
    "tmax": "min",
    "thalf": "min",
}
#: the outputs whose unit has the amount of the dose: the dose is a mass
#: (`PODOSE_met` in mg), so they are divided by the molecular weight (its value
#: at the start, a value per simulation like the parameter of the analysis)
PK_PER_DOSE_MASS: frozenset[str] = frozenset({"vz_f", "cl_f"})


def max_after_dose(time: np.ndarray, values: dict[str, np.ndarray]) -> float:
    """Get the maximum of a timecourse after the dose (time 0)."""
    (x,) = values.values()
    return float(np.max(x[time >= 0]))


#: the extremes of the pharmacodynamics after the dose: id -> function,
#: selection, unit
EXTREMES: dict[
    str, tuple[Callable[[np.ndarray, dict[str, np.ndarray]], float], str, str]
] = {
    "max_HRred": (max_after_dose, "HRred", "dimensionless"),
}

#: the names of the analytes
NAMES: dict[str, str] = {
    "met": "metoprolol",
    "metoh": "alpha-OH metoprolol",
    "mam": "metoprolol acid",
}

#: the outputs with their ids and names
OUTPUTS: list[SensitivityOutput] = [
    SensitivityOutput("met_auc_inf_obs", "metoprolol AUC∞"),
    SensitivityOutput("met_cmax", "metoprolol Cmax"),
    SensitivityOutput("met_tmax", "metoprolol tmax"),
    SensitivityOutput("met_thalf", "metoprolol Half-life"),
    SensitivityOutput("met_vz_f", "metoprolol Vz/F"),
    SensitivityOutput("met_cl_f", "metoprolol CL/F"),
    *(
        SensitivityOutput(f"{sid}_{key}", f"{NAMES[sid]} {label}")
        for sid in ["metoh", "mam"]
        for key, label in [
            ("auc_inf_obs", "AUC∞"),
            ("cmax", "Cmax"),
            ("tmax", "tmax"),
            ("thalf", "Half-life"),
        ]
    ),
    SensitivityOutput("max_HRred", "max HR reduction"),
]


def _pk_observables(sid: str, outputs: Mapping[str, str]) -> list:
    """Get the non-compartmental analysis of a substance and its outputs."""
    pk_id = f"pk_{sid}"
    return [
        PK(
            pk_id,
            f"[Cveplasma_{sid}]",
            dose="PODOSE_met",
            route="oral",
            options=NCAOptions(lloq=LLOQ),
            parameters=list(outputs),
        ),
        *(
            Formula(
                f"{sid}_{key}",
                f"{pk_id}.{key} / at(Mr_met, 0)"
                if key in PK_PER_DOSE_MASS
                else f"{pk_id}.{key}",
                unit=unit,
            )
            for key, unit in outputs.items()
        ),
    ]


#: the observables of a simulation, the outputs with their units; the ids of
#: the analyses (`pk_met`, ...) are no species of the model
OBSERVABLES = [
    *_pk_observables("met", PK_OUTPUTS_MET),
    *_pk_observables("metoh", PK_OUTPUTS_METABOLITE),
    *_pk_observables("mam", PK_OUTPUTS_METABOLITE),
    *(
        Custom(key, function, unit, symbols=[selection])
        for key, (function, selection, unit) in EXTREMES.items()
    ),
]

#: the output times [hr]: every 0.02 hr in the first day after the dose
#: (absorption and maximum), every 0.5 hr after it
TIMES_HR: tuple[float, ...] = tuple(
    np.unique(
        np.concatenate(
            [
                np.linspace(0, 24, 1201),
                np.linspace(24, END_HR, 2 * (END_HR - 24) + 1),
            ]
        )
    ).tolist()
)


def sensitivity_simulation(changes: Mapping[str, float]) -> Simulation:
    """Get the simulation of a group: a single oral dose of metoprolol at time 0.

    The immediate release tablet is the default application form of the model.
    """
    return Simulation(
        start=0,
        end=END_HR,
        times=TIMES_HR,
        time_unit="hr",
        preinit_changes={**changes, "PODOSE_met": Q(DOSE_MET, "mg")},
    )


def _cyp2d6(activity: float) -> dict[str, float]:
    """Get the changes of a CYP2D6 activity score, both alleles the custom activity."""
    return {
        "LI__cyp2d6_allele1": -1,
        "LI__cyp2d6_allele2": -1,
        "LI__cyp2d6_ac": activity,
    }


#: the groups the analyses are run for: the control (*1/*1, activity score 2),
#: the stages of renal impairment and the poor and ultrarapid metabolizers of
#: the simulation experiments
SENSITIVITY_GROUPS: list[SensitivityGroup] = [
    SensitivityGroup("control", "Control", sensitivity_simulation({}), "dimgrey"),
    *(
        SensitivityGroup(
            uid,
            name,
            sensitivity_simulation(
                {"KI__f_renal_function": MetoprololSimulationExperiment.renal_map[name]}
            ),
            MetoprololSimulationExperiment.renal_colors[name],
        )
        for uid, name in [
            ("mildRI", "Mild renal impairment"),
            ("modRI", "Moderate renal impairment"),
            ("sevRI", "Severe renal impairment"),
        ]
    ),
    *(
        SensitivityGroup(
            uid,
            name,
            sensitivity_simulation(
                _cyp2d6(MetoprololSimulationExperiment.cyp2d6_activity_scores[uid])
            ),
            MetoprololSimulationExperiment.colors[uid],
        )
        for uid, name in [
            ("pm", "CYP2D6 poor metabolizer"),
            ("um", "CYP2D6 ultrarapid metabolizer"),
        ]
    ),
]


def sensitivity_parameters() -> list[SensitivityParameter]:
    """Get the parameters of the analyses with their bounds and references."""
    parameters = parameters_from_sbml(
        MODEL_PATH,
        exclude_ids={
            # molecular weights
            "Mr_met",
            "Mr_metoh",
            "Mr_mam",
            # reference values
            "BW_ref",
            # unchangeable values
            "FQlu",
            "FVhv",
            "FVpo",
            # dosing parameters
            "PODOSE_met",
            "IVDOSE_met",
            "ti_met",
            # unused volumes
            "Vurine",
            "Vfeces",
            # the application forms: switches, the slow and controlled release
            # do not act on the immediate release tablet of the analysis
            "form_sr",
            "form_cr",
            "Ka_dis_sr_met",
            "Ka_dis_cr_met",
            "F_cr_met",
            # the baseline of the heart rate, the reduction does not depend on
            # it
            "HR",
            # the CYP2D6 diplotype: the activities of the alleles and the custom
            # activity, which the alleles *1/*1 of the control do not use
            *(f"LI__cyp2d6_a{k}" for k in range(len(ALLELE_ACTIVITIES))),
            "LI__cyp2d6_ac",
        },
        exclude_na=True,
        exclude_zero=True,
    )

    # the fitted parameters, their bounds are set relative to the value below
    set_bounds(
        parameters,
        [
            (fp.pid, np.nan, np.nan, ParameterType.FIT)
            for fp in [*parameters_pk, *parameters_pd]
            if fp.pid not in {"Ka_dis_sr_met", "Ka_dis_cr_met", "F_cr_met"}
        ],
    )
    # the scaling factors of the organ functions
    set_bounds(
        parameters,
        [
            (uid, 1 - BOUNDS_FRACTION, 1 + BOUNDS_FRACTION, ParameterType.SCALING)
            for uid in ["KI__f_renal_function"]
        ],
    )

    # the references of the values from the literature
    references = {
        "BW": r"\cite{Ogden2004, Jones2013, Thompson2009, Brown1997}",
        "FQgu": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FQh": r"\cite{Jones2013, Wynne1989, Thompson2009, Brown1997}",
        "FQki": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVar": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVgu": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVki": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVli": r"\cite{Jones2013, Wynne1989, Thompson2009, Brown1997}",
        "FVlu": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVve": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "COBW": r"\cite{Cattermole2017, Patel2021, Collis2001}",
        "KI__f_renal_function": r"\cite{Stevens2024}",
    }
    by_uid = {p.uid: p for p in parameters}
    for uid, reference in references.items():
        p = by_uid[uid]
        p.reference = reference
        if p.type == ParameterType.NA:
            p.type = ParameterType.DATA

    # every parameter without bounds varies around its value
    set_relative_bounds(parameters, BOUNDS_FRACTION)
    return parameters


#: the analyses of the script, with their groups and numbers of samples
SENSITIVITY = SensitivityRunner(
    model=MODEL,
    parameters=sensitivity_parameters,
    outputs=OUTPUTS,
    observables=OBSERVABLES,
    analyses={
        "local": LocalAnalysis(groups=SENSITIVITY_GROUPS[:1], delta=0.01),
        "sampling": SamplingAnalysis(groups=SENSITIVITY_GROUPS, n=1000),
        "fast": FastAnalysis(groups=SENSITIVITY_GROUPS[:1], n=1000),
        "sobol": SobolAnalysis(groups=SENSITIVITY_GROUPS[:1], n=4096),
    },
    default=("local",),
)


if __name__ == "__main__":
    SENSITIVITY.main()
