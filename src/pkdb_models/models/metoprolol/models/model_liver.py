"""Metoprolol liver model."""

from pkpdsim.templates import terms_of_use
from sbmlutils.factory import (
    AssignmentRule,
    Compartment,
    Model,
    Parameter,
    Reaction,
    Species,
    create_model,
)
from sbmlutils.metadata import SBO

from pkdb_models.models.metoprolol.models import annotations, templates
from pkdb_models.models.metoprolol.models.fits import FITS


class U(templates.U):
    """UnitsDefinitions."""


_m = Model(
    "metoprolol_liver",
    name="Metoprolol liver model",
    notes="""
    # Metoprolol liver model

    Metoprolol is a lipophilic, highly permeable drug (BCS class I). It
    equilibrates fast between the blood of the liver and the hepatocytes
    (`METIM`), its hepatic clearance is set by the enzymes. The metabolism has
    three routes [Article:2222517][Article:30087611]:

    - alpha-hydroxylation to alpha-hydroxymetoprolol (`METOH`), specific for
      CYP2D6; about 10 % of a dose are excreted as alpha-hydroxymetoprolol in
      the urine of extensive metabolizers, less than 1 % in poor metabolizers
      (Lennard1982, Kirchheiner2004).
    - O-demethylation and the oxidation to metoprolol acid by CYP2D6 (`ODM2D6`),
      the main route (60-65 % of a dose in the urine as metoprolol acid).
    - O-demethylation by other enzymes (CYP3A4, CYP2B6, CYP2C9; `ODM`), the
      clearance of poor metabolizers (Kirchheiner2004: the systemic clearance is
      30.6 l/hr without an active CYP2D6 gene and increases by 20.9 l/hr per
      active gene).

    The N-dealkylation (about 10 %) is part of the O-demethylation, its
    products are counted as metoprolol acid. The CYP2D6 reactions scale with
    the activity of the CYP2D6 diplotype (`f_cyp2d6` = `cyp2d6_activity`/2, 1
    for *1/*1), see the model of the CYP2D6 activity. The concentrations of the
    liver model are blood concentrations, the intrinsic clearances are
    clearances of blood.

    ```
    [Ruedesheim2020] Km(met, → OH-M & ODM) = 10 [8.8-12.4] µM
    [Madani1999] Km(met → OH-M & ODM) = 26 +/- 9 µM (in liver)
    [Yang2019] Km(met, → OH-M & ODM) = 11.31 ± 1.21 µM
    [Kim1991] Km(met, → OH-M & ODM) = 20 [15.6-26.0] µM
    ```
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
        "Vli",
        1.5,
        name="liver",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["li"],
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
    Species(
        "met",
        initialConcentration=0.0,
        name="metoprolol (liver)",
        compartment="Vli",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["met"],
    ),
    Species(
        "metoh",
        initialConcentration=0.0,
        name="alpha-hydroxymetoprolol (liver)",
        compartment="Vli",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["metoh"],
    ),
    Species(
        "mam",
        initialConcentration=0.0,
        name="metoprolol acid (liver)",
        compartment="Vli",
        substanceUnit=U.mmole,
        hasOnlySubstanceUnits=False,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["mam"],
    ),
]

_m.parameters = [
    Parameter(
        "f_cyp2d6",
        1.0,
        unit=U.dimensionless,
        constant=False,
        name="CYP2D6 activity relative to *1/*1",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        The activity score of the CYP2D6 diplotype over the one of *1/*1 (2):
        0 for poor metabolizers, 1.5 for *1x2/*1. The genotype is set by the
        alleles of the CYP2D6 model (`cyp2d6_allele1`, `cyp2d6_allele2`, the
        indexes of the alleles) or by an activity score (`cyp2d6_ac` with both
        allele indexes -1).
        """,
    ),
    Parameter(
        "CYP2D6_Km_met",
        0.015,
        unit=U.mM,
        name="Km of metoprolol for CYP2D6",
        sboTerm=SBO.MICHAELIS_CONSTANT,
        notes="""
        10-26 µM in human liver microsomes (Ruedesheim2020, Madani1999,
        Yang2019, Kim1991); the saturation of the first pass is the dose
        dependent bioavailability (31 % after 20 mg, 46 % after 100 mg
        metoprolol tartrate, Johnsson1975). Not fitted, the data do not
        identify it (a flat profile likelihood between 2 and 100 µM).
        """,
    ),
    Parameter(
        "METOH_Vmax",
        **FITS.parameter("LI__METOH_Vmax", unit=U.mmole_per_min_l),
        name="Vmax of the alpha-hydroxylation (CYP2D6, *1/*1)",
        sboTerm=SBO.MAXIMAL_VELOCITY,
        notes="""
        About 15 % of the hepatic metabolism of extensive metabolizers is
        alpha-hydroxylation (about 10 % of an oral dose in the urine as
        alpha-hydroxymetoprolol, Lennard1982, Kirchheiner2004).
        """,
    ),
    Parameter(
        "ODM2D6_Vmax",
        **FITS.parameter("LI__ODM2D6_Vmax", unit=U.mmole_per_min_l),
        name="Vmax of the O-demethylation by CYP2D6 (*1/*1)",
        sboTerm=SBO.MAXIMAL_VELOCITY,
        notes="""
        Together with the alpha-hydroxylation an intrinsic blood clearance of
        about 1.7 l/min at *1/*1 (CYP2D6 adds 20.9 l/hr of plasma clearance per
        active gene, Kirchheiner2004), a hepatic extraction of about 0.57 and a
        bioavailability of about 0.43.
        """,
    ),
    Parameter(
        "ODM_Vmax",
        **FITS.parameter("LI__ODM_Vmax", unit=U.mmole_per_min_l),
        name="Vmax of the O-demethylation by other enzymes than CYP2D6",
        sboTerm=SBO.MAXIMAL_VELOCITY,
        notes="""
        An intrinsic blood clearance of about 0.25 l/min, the clearance of poor
        metabolizers without the renal clearance (30.6 l/hr of plasma,
        Kirchheiner2004).
        """,
    ),
    Parameter(
        "ODM_Km_met",
        0.015,
        unit=U.mM,
        name="Km of metoprolol for the O-demethylation by other enzymes",
        sboTerm=SBO.MICHAELIS_CONSTANT,
        notes="Not known, taken as the Km of CYP2D6.",
    ),
]

_m.rules = [
    AssignmentRule(
        "f_cyp2d6",
        "cyp2d6_activity / 2 dimensionless",
        U.dimensionless,
        name="CYP2D6 activity relative to *1/*1",
    ),
]

_m.reactions = [
    Reaction(
        "METIM",
        name="metoprolol exchange (blood, hepatocyte)",
        compartment="Vli",
        equation="met_ext <-> met",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "METIM_k",
                100,
                unit=U.per_min,
                name="rate of the metoprolol exchange of the liver",
                sboTerm=SBO.KINETIC_CONSTANT,
            ),
        ],
        formula=("METIM_k * Vli * (met_ext - met)", U.mmole_per_min),
        notes="Passive diffusion of the permeable drug, assumed to be fast.",
    ),
    Reaction(
        "METOH",
        name="alpha-hydroxylation of metoprolol (CYP2D6)",
        compartment="Vli",
        equation="met -> metoh",
        sboTerm=SBO.BIOCHEMICAL_REACTION,
        formula=(
            "f_cyp2d6 * METOH_Vmax * Vli * met/(CYP2D6_Km_met + met)",
            U.mmole_per_min,
        ),
    ),
    Reaction(
        "ODM2D6",
        name="O-demethylation of metoprolol (CYP2D6)",
        compartment="Vli",
        equation="met -> mam",
        sboTerm=SBO.BIOCHEMICAL_REACTION,
        formula=(
            "f_cyp2d6 * ODM2D6_Vmax * Vli * met/(CYP2D6_Km_met + met)",
            U.mmole_per_min,
        ),
    ),
    Reaction(
        "ODM",
        name="O-demethylation of metoprolol (other enzymes)",
        compartment="Vli",
        equation="met -> mam",
        sboTerm=SBO.BIOCHEMICAL_REACTION,
        formula=(
            "ODM_Vmax * Vli * met/(ODM_Km_met + met)",
            U.mmole_per_min,
        ),
        notes="CYP3A4, CYP2B6 and CYP2C9, independent of the CYP2D6 genotype.",
    ),
    Reaction(
        "METOHEX",
        name="alpha-hydroxymetoprolol export",
        compartment="Vli",
        equation="metoh <-> metoh_ext",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "METOHEX_k",
                100,
                unit=U.per_min,
                name="rate of the alpha-hydroxymetoprolol export",
                sboTerm=SBO.KINETIC_CONSTANT,
            ),
        ],
        formula=("METOHEX_k * Vli * (metoh - metoh_ext)", U.mmole_per_min),
        notes="Assumed to be fast.",
    ),
    Reaction(
        "MAMEX",
        name="metoprolol acid export",
        compartment="Vli",
        equation="mam <-> mam_ext",
        sboTerm=SBO.TRANSPORT_REACTION,
        pars=[
            Parameter(
                "MAMEX_k",
                100,
                unit=U.per_min,
                name="rate of the metoprolol acid export",
                sboTerm=SBO.KINETIC_CONSTANT,
            ),
        ],
        formula=("MAMEX_k * Vli * (mam - mam_ext)", U.mmole_per_min),
        notes="Assumed to be fast.",
    ),
]

model_liver = _m

if __name__ == "__main__":
    from pkdb_models.models.metoprolol import MODEL_BASE_PATH
    from pkdb_models.models.metoprolol.models.model_cyp2d6 import model_cyp2d6

    results = create_model(
        model=[model_cyp2d6, model_liver],
        filepath=MODEL_BASE_PATH / f"{model_liver.sid}.xml",
    )
