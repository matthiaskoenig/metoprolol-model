"""Parameter fit problems for metoprolol.

The data of a fit is selected from the fit mappings of the studies in three
steps, see `sbmlsim.fit.helpers`: the filters on the metadata of the mappings
select the training data of the fit and exclude the rest, the outliers are
named once for all mappings and are the training data which is not usable, and
the validation data is the part of the data a fit is evaluated on but not
fitted to. The metadata of a mapping describes its curve, what a fit does with
the curve is decided here.

The training data are the plasma concentrations of metoprolol and its
metabolites of healthy and hypertensive subjects with a normal renal function
(hypertension does not change the pharmacokinetics) and, for the
pharmacodynamics, the relative reduction of the exercise heart rate. The
validation data has three parts, each a different question: the doses
(`DOSE_VALIDATION`), the populations (`POPULATION_VALIDATION`, the CYP2D6
genotypes with reduced activity alleles and the renal impairment, which the
model describes with the activity scores and the GFR, not fitted) and the
limitations (`LIMITATION_VALIDATION`, data of a process the model does not
describe). The urinary metoprolol after an oral dose of Regardh1974 is an
outlier (`OUTLIER_MAPPINGS`). The summaries of data which is fitted one by
one are excluded (`AGGREGATE_MAPPINGS`).
"""

from pkpdsim.fit import mapping_metadata, observable_filter
from pkpdsim.metadata import Health
from sbmlsim.console import console
from sbmlsim.experiment import SimulationExperiment
from sbmlsim.fit import FitMapping, FitMappingCollection, MappingKind
from sbmlsim.fit.helpers import FitMappings, MappingFilter

from pkdb_models.models.metoprolol import DATA_PATHS, METOPROLOL_PATH
from pkdb_models.models.metoprolol.experiments.studies import (
    Bae2014,
    Blomqvist1988,
    Cerqueira2003,
    Cerqueira2005,
    Jin2008,
    Johnsson1975,
    Kirchheiner2004,
    Lennard1982,
    Oosterhuis1988,
    Regardh1974,
    Sandberg1988,
)

#: the keys of fit mappings by study: the keys of the mappings are SIds of their
#: experiment, which two studies can share, so a named mapping is named with
#: its study
type NamedMappings = dict[str, set[str]]

EXPERIMENT_CLASSES: list[type[SimulationExperiment]] = [
    Bae2014,
    Blomqvist1988,
    Cerqueira2003,
    Cerqueira2005,
    Jin2008,
    Johnsson1975,
    Kirchheiner2004,
    Lennard1982,
    Oosterhuis1988,
    Regardh1974,
    Sandberg1988,
]

#: observables of the pharmacokinetics: metoprolol, alpha-hydroxymetoprolol and
#: metoprolol acid in plasma, their urinary excretion
OBSERVABLES_PK: frozenset[str] = frozenset(
    {
        "Cveplasma_met",
        "Cveplasma_metoh",
        "Cveplasma_mam",
        "Aurine_met",
        "Aurine_metoh",
        "Aurine_mam",
        "KI__METEX",
        "KI__METOHEX",
        "KI__MAMEX",
    }
)
#: observables of the pharmacodynamics: the relative reduction of the exercise
#: heart rate, the absolute heart rate depends on the baseline of a study
OBSERVABLES_PD: frozenset[str] = frozenset({"HRred"})

#: health of the training data, hypertension does not change the
#: pharmacokinetics
TRAINING_HEALTH: frozenset[Health] = frozenset({Health.HEALTHY, Health.HYPERTENSION})

#: mappings which are not fitted, the data is not usable
OUTLIER_MAPPINGS: NamedMappings = {
    # the urinary metoprolol after the oral solution: the method is not
    # selective for metoprolol after an oral dose (Regardh1974)
    "Regardh1974": {"fm_urine_met_oral"},
}

#: the validation of the doses: the low doses of Johnsson1975 (the dose
#: dependent first pass, 31 % bioavailability after 20 mg against 46 % after
#: 100 mg) and the twice daily immediate release tablets of Sandberg1988, which
#: the once daily doses of the training predict
DOSE_VALIDATION: NamedMappings = {
    "Johnsson1975": {"fm_met_oral20", "fm_met_iv5"},
    "Sandberg1988": {"fm_met_50_ir", "fm_hr_50_ir"},
}

#: the validation of the populations: the CYP2D6 genotypes with *10 alleles
#: and the ultrarapid metabolizers (activity scores of the alleles, not
#: fitted), the population model curves of Kirchheiner2004, the debrisoquine
#: phenotypes of a fed, partly hypertensive group and the renal impairment (the
#: GFR of the study, not fitted)
POPULATION_VALIDATION: NamedMappings = {
    "Bae2014": {"fm_met_1010", "fm_metoh_1010"},
    "Jin2008": {"fm_met_110", "fm_met_1010", "fm_metoh_110", "fm_metoh_1010"},
    "Kirchheiner2004": {
        "fm_met_model_em",
        "fm_met_model_pm",
        "fm_met_model_um",
        "fm_urine_met_um",
        "fm_urine_metoh_um",
        "fm_hrred_um",
    },
    "Lennard1982": {
        "fm_met_em",
        "fm_met_pm",
        "fm_urine_met_em",
        "fm_urine_metoh_em",
        "fm_urine_met_pm",
        "fm_urine_metoh_pm",
        "fm_hrred_em",
        "fm_hrred_pm",
    },
    "Cerqueira2005": {"fm_met_crf", "fm_metoh_crf", "fm_mam_crf"},
}

#: the validation of the limitations of the model: valid data of a process the
#: model does not describe, which would distort the fitted parameters of the
#: processes it does describe
LIMITATION_VALIDATION: NamedMappings = {
    # the urinary excretion rate of alpha-hydroxymetoprolol of one patient
    "Cerqueira2003": {"fm_KI__METOHEX"},
}

#: the summaries of data which the fits use one by one, excluded from every
#: fit: a mean of subjects would count the subjects twice
AGGREGATE_MAPPINGS: NamedMappings = {}

#: the validation data
VALIDATION_MAPPINGS: NamedMappings = {
    study: set().union(
        *(
            mappings.get(study, set())
            for mappings in [
                DOSE_VALIDATION,
                POPULATION_VALIDATION,
                LIMITATION_VALIDATION,
            ]
        )
    )
    for study in DOSE_VALIDATION | POPULATION_VALIDATION | LIMITATION_VALIDATION
}


def study(fit_mapping: FitMapping) -> str:
    """Get the study of a fit mapping, the id of its experiment."""
    return fit_mapping.reference.experiment.sid


def named(
    mappings: NamedMappings, fit_mapping_key: str, fit_mapping: FitMapping
) -> bool:
    """Check whether a fit mapping is one of the named mappings of its study."""
    return fit_mapping_key in mappings.get(study(fit_mapping), set())


def check_named(mappings: NamedMappings, fit_mappings: FitMappings) -> None:
    """Check that the named mappings are fit mappings of their studies.

    Raises:
        ValueError: for a study which is no experiment, or a key which is no fit
            mapping of its study.
    """
    for sid, keys in mappings.items():
        experiment = fit_mappings.experiments.get(sid)
        if experiment is None:
            raise ValueError(f"'{sid}' is no experiment of the fits.")
        if unknown := sorted(keys - set(experiment._fit_mappings)):
            raise ValueError(f"'{unknown}' are no fit mappings of '{sid}'.")


def filter_aggregates(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """No summaries of data which is fitted one by one, see `AGGREGATE_MAPPINGS`."""
    return not named(AGGREGATE_MAPPINGS, fit_mapping_key, fit_mapping)


def filter_health(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """Healthy and hypertensive subjects, besides the validation data."""
    if named(VALIDATION_MAPPINGS, fit_mapping_key, fit_mapping):
        return True
    return mapping_metadata(fit_mapping).health in TRAINING_HEALTH


def mapping_collections(
    filters: MappingFilter | list[MappingFilter],
    validation: NamedMappings = VALIDATION_MAPPINGS,
) -> dict[str, list[FitMappingCollection]]:
    """Select the data of a fit from the fit mappings of the studies.

    The filters select the training data, the mappings which fail them are
    excluded, and so are the summaries of data which is fitted one by one
    (`AGGREGATE_MAPPINGS`) and the subjects with another disease than
    hypertension (`filter_health`). The outliers are `OUTLIER_MAPPINGS`, the
    validation data is `VALIDATION_MAPPINGS`. Neither kind enters the cost;
    both are simulated and evaluated with the training data, so a report says
    how the fitted parameters describe data they were not fitted on.

    Args:
        filters: filters of the training data.
        validation: the keys of the validation data by study.

    Returns:
        The fit mapping collections of all kinds by experiment id.

    Raises:
        ValueError: if an outlier is a mapping of no study or of several.
    """
    fit_mappings = FitMappings(
        experiment_classes=EXPERIMENT_CLASSES,
        base_path=METOPROLOL_PATH,
        data_path=DATA_PATHS,
    )
    for mappings in [OUTLIER_MAPPINGS, AGGREGATE_MAPPINGS, validation]:
        check_named(mappings, fit_mappings)
    # sbmlsim selects the outliers by their keys alone, which must name one
    # mapping of all studies
    outliers = {key for keys in OUTLIER_MAPPINGS.values() for key in keys}
    for key in outliers:
        studies = [
            sid
            for sid, experiment in fit_mappings.experiments.items()
            if key in experiment._fit_mappings
        ]
        if len(studies) != 1:
            raise ValueError(f"The outlier '{key}' is a mapping of {studies}.")
    selection = fit_mappings.select(
        filters=[
            *(filters if isinstance(filters, list) else [filters]),
            filter_aggregates,
            filter_health,
        ],
        outliers=outliers,
        validation=lambda key, fit_mapping: named(validation, key, fit_mapping),
        print_info=False,
    )
    # the counts per experiment and kind, not the single mappings
    selection.print(detail=False)
    # the validation mappings by the question they answer
    selected = {
        (sid, key)
        for sid, kinds in selection.kinds.items()
        for key, kind in kinds.items()
        if kind is MappingKind.VALIDATION
    }

    def pairs(mappings: NamedMappings) -> set[tuple[str, str]]:
        return {(sid, key) for sid, keys in mappings.items() for key in keys}

    console.print(
        "validation: "
        + ", ".join(
            f"{len(selected & pairs(mappings))} {question}"
            for question, mappings in [
                ("doses", DOSE_VALIDATION),
                ("populations", POPULATION_VALIDATION),
                ("limitations", LIMITATION_VALIDATION),
            ]
        )
    )
    return selection.collections


def f_collections_pk() -> dict[str, list[FitMappingCollection]]:
    """Pharmacokinetic data: metoprolol and its metabolites in plasma and urine."""
    return mapping_collections([observable_filter(set(OBSERVABLES_PK))])


def f_collections_pd() -> dict[str, list[FitMappingCollection]]:
    """Pharmacodynamic data: the reduction of the exercise heart rate."""
    return mapping_collections([observable_filter(set(OBSERVABLES_PD))])


if __name__ == "__main__":
    for f_collections in [f_collections_pk, f_collections_pd]:
        console.rule(title=f_collections.__name__, align="left", style="white")
        f_collections()
