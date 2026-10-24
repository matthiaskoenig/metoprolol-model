"""Metoprolol kidney model.

The renal clearances are relative to the glomerular filtration rate (GFR):

- metoprolol: 95 ml/min (109 ml/min corrected for the binding in plasma, i.e.
  about the filtration of the unbound drug, Regardh1974); 6.6-9.6 l/hr
  independent of the CYP2D6 genotype (Kirchheiner2004); 50-80 ml/min
  (Lennard1983), about 70 ml/min (Cerqueira1999). 9.4 % of an intravenous and
  5.2 % of an oral dose are excreted unchanged (Regardh1974); 3.2 % (extensive)
  and 14.7 % (poor metabolizers) of an oral dose (Lennard1982).
- alpha-hydroxymetoprolol: 13.5-14.4 l/hr (225-240 ml/min), about 10 % of an
  oral dose in the urine of extensive metabolizers (Kirchheiner2004,
  Lennard1982).
- metoprolol acid: the metabolites (total radioactivity) 120 ml/min
  (Regardh1974); 60-65 % of a dose in the urine (Sandberg1993, Borg1975).
"""

from pkpdsim.templates import terms_of_use
from sbmlutils.factory import (
    AssignmentRule,
    Compartment,
    Model,
    Parameter,
    Reaction,
    Species,
    UnitDefinition,
    create_model,
)
from sbmlutils.metadata import SBO

from pkdb_models.models.metoprolol.models import annotations, templates
from pkdb_models.models.metoprolol.models.fits import FITS


class U(templates.U):
    """UnitsDefinitions."""

    ml_per_min = UnitDefinition("ml_per_min", "ml/min")
    l_per_ml = UnitDefinition("l_per_ml", "l/ml")


_m = Model(
    "metoprolol_kidney",
    name="Metoprolol kidney model",
    notes="""
    # Metoprolol kidney model

    Metoprolol, alpha-hydroxymetoprolol and metoprolol acid are excreted in the
    urine. The renal clearances are given relative to the glomerular filtration
    rate (GFR) and scale with the renal function (`f_renal_function`): the
    renal clearance of metoprolol is `METEX_f` times the filtration of its
    unbound fraction in plasma (`fup_met * GFR`), the one of a metabolite
    `<X>EX_f` times the GFR. The concentrations of the kidney model are blood
    concentrations, the plasma concentration of metoprolol is the blood
    concentration over the blood to plasma ratio `BP_met`; the metabolites are
    taken to have a blood to plasma ratio of 1.
    """
    + terms_of_use,
    units=U,
    model_units=templates.model_units,
    creators=templates.creators,
)


_m.compartments = [
    Compartment(
        "Vext",
        1.5,
        name="blood",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["blood"],
        unit=U.liter,
        port=True,
    ),
    Compartment(
        "Vki",
        0.3,
        name="kidney",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["ki"],
        unit=U.liter,
        port=True,
    ),
    Compartment(
        "Vurine",
        1.0,
        name="urine",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["urine"],
        unit=U.liter,
        port=True,
    ),
]

_m.species = [
    # [mM] = [mmole/l]
    Species(
        "met_ext",
        initialConcentration=0.0,
        name="metoprolol (blood)",
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["met"],
        port=True,
    ),
    Species(
        "metoh_ext",
        initialConcentration=0.0,
        name="alpha-hydroxymetoprolol (blood)",
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["metoh"],
        port=True,
    ),
    Species(
        "mam_ext",
        initialConcentration=0.0,
        name="metoprolol acid (blood)",
        compartment="Vext",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["mam"],
        port=True,
    ),
    # the urinary species are amounts
    Species(
        "met_urine",
        initialConcentration=0.0,
        name="metoprolol (urine)",
        compartment="Vurine",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["met"],
        port=True,
    ),
    Species(
        "metoh_urine",
        initialConcentration=0.0,
        name="alpha-hydroxymetoprolol (urine)",
        compartment="Vurine",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["metoh"],
        port=True,
    ),
    Species(
        "mam_urine",
        initialConcentration=0.0,
        name="metoprolol acid (urine)",
        compartment="Vurine",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["mam"],
        port=True,
    ),
]

_m.parameters = [
    Parameter(
        "f_renal_function",
        name="renal function",
        value=1.0,
        unit=U.dimensionless,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        The GFR relative to the healthy GFR `GFR_base` (101 ml/min at 75 kg):
        a measured creatinine clearance of X ml/min is the renal function
        X/101. 1.0 is the normal renal function, below 1.0 an impaired one.
        """,
    ),
    Parameter(
        "GFR_base",
        101,
        U.ml_per_min,
        name="glomerular filtration rate (healthy)",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        port=True,
    ),
    Parameter(
        "fup_met",
        0.88,
        U.dimensionless,
        name="fraction unbound in plasma metoprolol",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        port=True,
    ),
    Parameter(
        "BP_met",
        1.2,
        U.dimensionless,
        name="blood to plasma ratio metoprolol",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        port=True,
    ),
    Parameter(
        "METEX_f",
        **FITS.parameter("KI__METEX_f", unit=U.dimensionless),
        name="renal clearance of unbound metoprolol relative to the GFR",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        The renal clearance of metoprolol is METEX_f times the filtration of its
        unbound fraction, fup_met * GFR: 1 is filtration alone. 95-109 ml/min
        of plasma (Regardh1974).
        """,
    ),
    Parameter(
        "METOHEX_f",
        **FITS.parameter("KI__METOHEX_f", unit=U.dimensionless),
        name="renal clearance of alpha-hydroxymetoprolol relative to the GFR",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="13.5-14.4 l/hr, a net tubular secretion (Kirchheiner2004).",
    ),
    Parameter(
        "MAMEX_f",
        **FITS.parameter("KI__MAMEX_f", unit=U.dimensionless),
        name="renal clearance of metoprolol acid relative to the GFR",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        120 ml/min for the metabolites (total radioactivity, Regardh1974),
        about 150 ml/min from the steady state of metoprolol acid of
        Cerqueira2005.
        """,
    ),
]

_m.rules = [
    AssignmentRule(
        "GFR",
        "f_renal_function * GFR_base",
        unit=U.ml_per_min,
        name="glomerular filtration rate",
    ),
]

_m.reactions = [
    Reaction(
        "METEX",
        name="metoprolol renal excretion",
        equation="met_ext -> met_urine",
        sboTerm=SBO.TRANSPORT_REACTION,
        compartment="Vki",
        # [ml/min] * [l/ml] * [-] * [mmole/l]
        formula=(
            "GFR * 0.001 l_per_ml * fup_met * METEX_f * met_ext / BP_met",
            U.mmole_per_min,
        ),
    ),
    Reaction(
        "METOHEX",
        name="alpha-hydroxymetoprolol renal excretion",
        equation="metoh_ext -> metoh_urine",
        sboTerm=SBO.TRANSPORT_REACTION,
        compartment="Vki",
        formula=(
            "GFR * 0.001 l_per_ml * METOHEX_f * metoh_ext",
            U.mmole_per_min,
        ),
    ),
    Reaction(
        "MAMEX",
        name="metoprolol acid renal excretion",
        equation="mam_ext -> mam_urine",
        sboTerm=SBO.TRANSPORT_REACTION,
        compartment="Vki",
        formula=(
            "GFR * 0.001 l_per_ml * MAMEX_f * mam_ext",
            U.mmole_per_min,
        ),
    ),
]

model_kidney = _m


if __name__ == "__main__":
    from pkdb_models.models.metoprolol import MODEL_BASE_PATH

    results = create_model(
        model=model_kidney,
        filepath=MODEL_BASE_PATH / f"{model_kidney.sid}.xml",
    )
