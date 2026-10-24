"""Metoprolol body model: the PBPK/PD model of metoprolol and its metabolites."""

from typing import NotRequired, TypedDict

import numpy as np
from pkpdsim.templates import terms_of_use
from sbmlutils.factory import (
    PORT_SUFFIX,
    AssignmentRule,
    Compartment,
    ExternalModelDefinition,
    Model,
    Parameter,
    RateRule,
    Reaction,
    ReplacedElement,
    Species,
    Submodel,
    UnitDefinition,
    create_model,
)
from sbmlutils.metadata import SBO

from pkdb_models.models.metoprolol.models import annotations, templates
from pkdb_models.models.metoprolol.models.fits import FITS


class U(templates.U):
    """UnitsDefinitions."""

    cm = UnitDefinition("cm")
    kg = UnitDefinition("kg")

    l_per_kg = UnitDefinition("l_per_kg", "l/kg")

    mg_per_min = UnitDefinition("mg_per_min", "mg/min")

    ml = UnitDefinition("ml")
    ml_per_l = UnitDefinition("ml_per_l", "ml/l")
    ml_per_min = UnitDefinition("ml_per_min", "ml/min")
    ml_per_s = UnitDefinition("ml_per_s", "ml/s")
    ml_per_s_kg = UnitDefinition("ml_per_s_kg", "ml/s/kg")

    min_per_hr = UnitDefinition("min_per_hr", "min/hr")
    per_hr = UnitDefinition("per_hr", "1/hr")

    s_per_min = UnitDefinition("s_per_min", "s/min")


# ------------------------------------------------------------------------------------
# Whole Body Metabolism
# -------------------------------------------------------------------------------------
_m = Model(
    "metoprolol_body",
    name="Metoprolol body model",
    notes="""
    # Metoprolol whole-body model

    Whole-body model of metoprolol and its metabolites alpha-hydroxymetoprolol
    and metoprolol acid with the blood circulation, the tissue distribution,
    the oral and intravenous dosing, the submodels of the liver (metabolism by
    CYP2D6 and other enzymes) and of the kidneys (renal excretion), and the
    reduction of the exercise heart rate by metoprolol.

    The circulating species are whole blood concentrations: the blood flows
    transport the blood concentrations, the plasma concentration is the blood
    concentration over the blood to plasma ratio `BP_<sid>` (metoprolol 1.2,
    Regardh1974; the metabolites 1). The tissues exchange with the blood by
    the flow `ftissue_<sid>` towards the tissue/blood partition coefficient
    `Kp_<sid>`, which sets the volume of distribution (metoprolol about
    4.5 l/kg of plasma, Regardh1974).
    """
    + terms_of_use,
    units=U,
    model_units=templates.model_units,
    creators=templates.creators,
)


class SubstanceBody(TypedDict):
    """Definition of a substance transported in the whole-body model."""

    name: str
    unit: UnitDefinition
    cinit: float  # initial concentration [mmole/l]
    Mr: float  # molecular weight [g/mole]
    IVDOSE: NotRequired[float]  # intravenous dose [mg]
    PODOSE: NotRequired[float]  # oral dose [mg]
    BP: float  # blood to plasma ratio [-]
    fup: NotRequired[float]  # fraction unbound in plasma [-]
    Kp: NotRequired[float]  # tissue/blood partition coefficient [-], else fitted
    ftissue: NotRequired[float]  # exchange flow at BW_ref [l/min], else fitted


SUBSTANCES_BODY: dict[str, SubstanceBody] = {
    "met": {
        "name": "metoprolol",
        "unit": U.mmole,
        "cinit": 0.0,
        "Mr": 267.36394,
        "IVDOSE": 0,
        "PODOSE": 0,
        # blood to plasma ratio 1.09-1.23, 1.2 at low concentrations
        # (Regardh1974 Table I)
        "BP": 1.2,
        # 12-13 % bound in plasma (Regardh1974)
        "fup": 0.88,
        # Kp and ftissue are fitted (`fits.FITS`): Vss about 4.5 l/kg of
        # plasma (Regardh1974: Vc 2.2 l/kg, Vbeta 5.6 l/kg), a distribution
        # half-life of about 12 min
    },
    "metoh": {
        "name": "alpha-hydroxymetoprolol",
        "unit": U.mmole,
        "cinit": 0.0,
        "Mr": 283.36334,
        "BP": 1.0,
        # Kp is fitted (`fits.FITS`): half-life 5.4-6.1 hr in extensive
        # metabolizers (Jin2008, Bae2014) at a renal clearance of about
        # 14 l/hr (Kirchheiner2004)
        "ftissue": 1.0,
    },
    "mam": {
        "name": "metoprolol acid",
        "unit": U.mmole,
        "cinit": 0.0,
        "Mr": 267.32,
        "BP": 1.0,
        # half-life of the metabolites 5.2 hr at a renal clearance of about
        # 120 ml/min (Regardh1974): a volume of about 50-80 l
        "Kp": 1.0,
        "ftissue": 1.0,
    },
}

# -----------------------------------------------------------------------------
# Submodels
# -----------------------------------------------------------------------------
COMPARTMENTS_BODY = {
    "gu": "gastrointestinal tract",
    "he": "heart",
    "ki": "kidney",
    "li": "liver",
    "lu": "lung",
    "re": "rest",
    "ar": "arterial blood",
    "ve": "venous blood",
    "po": "portal vein",
    "hv": "hepatic vein",
}

#: the compartments of the circulation, without tissue
VESSELS = ["ar", "ve", "po", "hv"]

#: the tissues which exchange with their blood (the liver is the submodel)
TISSUES = ["gu", "he", "ki", "lu", "re"]

SUBMODEL_SID_DICT = {  # tissue to submodel mapping
    "li": "LI",  # liver
    "ki": "KI",  # kidney
}

liver_id = "metoprolol_liver"
kidney_id = "metoprolol_kidney"

_m.external_model_definitions = [
    ExternalModelDefinition(
        sid="liver", source=f"{liver_id}.xml", name="liver", modelRef=liver_id
    ),
    ExternalModelDefinition(
        sid="kidney", source=f"{kidney_id}.xml", name="kidney", modelRef=kidney_id
    ),
]

_m.submodels = [
    Submodel(sid=SUBMODEL_SID_DICT["li"], modelRef="liver", name="liver submodel"),
    Submodel(sid=SUBMODEL_SID_DICT["ki"], modelRef="kidney", name="kidney submodel"),
]


# -------------------------------------------------------------------------------------
# Compartments
# -------------------------------------------------------------------------------------
_m.compartments = [
    Compartment(
        f"V{cid}",
        metaId=f"meta_V{cid}",
        value=1,
        unit=U.liter,
        constant=False,
        name=cname,
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments[cid],
    )
    for cid, cname in COMPARTMENTS_BODY.items()
]
_m.compartments.extend(
    [
        Compartment(
            "Vurine",
            metaId="meta_Vurine",
            value=1,
            unit=U.liter,
            constant=True,
            name="urine",
            sboTerm=SBO.PHYSICAL_COMPARTMENT,
            annotations=annotations.compartments["urine"],
        ),
        Compartment(
            "Vfeces",
            metaId="meta_Vfeces",
            value=1,
            unit=U.liter,
            constant=True,
            name="feces",
            sboTerm=SBO.PHYSICAL_COMPARTMENT,
            annotations=annotations.compartments["feces"],
        ),
    ]
)

# blood and tissue compartments of the organs
for cid, cname in COMPARTMENTS_BODY.items():
    if cid not in VESSELS:
        _m.compartments.extend(
            [
                Compartment(
                    f"V{cid}_tissue",
                    value=1,
                    unit=U.liter,
                    constant=False,
                    name=f"{cname} tissue",
                    metaId=f"meta_V{cid}_tissue",
                    sboTerm=SBO.PHYSICAL_COMPARTMENT,
                    annotations=annotations.compartments["parenchyma"],
                    port=True,
                ),
                Compartment(
                    f"V{cid}_blood",
                    value=1,
                    unit=U.liter,
                    constant=False,
                    name=f"{cname} blood",
                    metaId=f"meta_V{cid}_blood",
                    sboTerm=SBO.PHYSICAL_COMPARTMENT,
                    annotations=annotations.compartments["blood"],
                    port=True,
                ),
            ]
        )


# replace volumes of submodels
_m.replaced_elements.extend(
    [
        # liver
        ReplacedElement(
            sid="Vli_tissue_RE",
            metaId="Vli_tissue_RE",
            elementRef="Vli_tissue",
            submodelRef=SUBMODEL_SID_DICT["li"],
            portRef=f"Vli{PORT_SUFFIX}",
        ),
        ReplacedElement(
            sid="Vli_blood_RE",
            metaId="Vli_blood_RE",
            elementRef="Vli_blood",
            submodelRef=SUBMODEL_SID_DICT["li"],
            portRef=f"Vext{PORT_SUFFIX}",
        ),
        # kidney
        ReplacedElement(
            sid="Vki_tissue_RE",
            metaId="Vki_tissue_RE",
            elementRef="Vki_tissue",
            submodelRef=SUBMODEL_SID_DICT["ki"],
            portRef=f"Vki{PORT_SUFFIX}",
        ),
        ReplacedElement(
            sid="Vki_blood_RE",
            metaId="Vki_blood_RE",
            elementRef="Vki_blood",
            submodelRef=SUBMODEL_SID_DICT["ki"],
            portRef=f"Vext{PORT_SUFFIX}",
        ),
        ReplacedElement(
            sid="Vurine_RE",
            metaId="Vurine_RE",
            elementRef="Vurine",
            submodelRef=SUBMODEL_SID_DICT["ki"],
            portRef=f"Vurine{PORT_SUFFIX}",
        ),
    ]
)

# -------------------------------------------------------------------------------------------------
# Species
# -------------------------------------------------------------------------------------------------
_m.species = []
for sid, sdict in SUBSTANCES_BODY.items():
    # blood species
    for cid, cname in COMPARTMENTS_BODY.items():
        if cid in VESSELS:
            sid_ex = f"C{cid}_{sid}"
            cid_ex = f"V{cid}"
            name = f"{sdict['name']} ({cname})"
        else:
            sid_ex = f"C{cid}_blood_{sid}"
            cid_ex = f"V{cid}_blood"
            name = f"{sdict['name']} ({cname} blood)"
        _m.species.append(
            Species(
                sid_ex,
                metaId=f"meta_{sid_ex}",
                initialConcentration=sdict["cinit"],
                compartment=cid_ex,
                substanceUnit=sdict["unit"],
                name=name,
                hasOnlySubstanceUnits=False,
                sboTerm=SBO.SIMPLE_CHEMICAL,
                annotations=annotations.species[sid],
                port=True,
            )
        )
    # tissue species
    for cid in TISSUES:
        sid_ex = f"C{cid}_{sid}"
        _m.species.append(
            Species(
                sid_ex,
                metaId=f"meta_{sid_ex}",
                initialConcentration=sdict["cinit"],
                compartment=f"V{cid}_tissue",
                substanceUnit=sdict["unit"],
                name=f"{sdict['name']} ({COMPARTMENTS_BODY[cid]} tissue)",
                hasOnlySubstanceUnits=False,
                sboTerm=SBO.SIMPLE_CHEMICAL,
                annotations=annotations.species[sid],
            )
        )
    # urine
    _m.species.append(
        Species(
            f"Aurine_{sid}",
            metaId=f"meta_Aurine_{sid}",
            initialConcentration=0,
            compartment="Vurine",
            substanceUnit=sdict["unit"],
            name=f"{sdict['name']} (urine)",
            hasOnlySubstanceUnits=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species[sid],
        )
    )

# the part of an oral dose which is not absorbed
_m.species.append(
    Species(
        "Afeces_met",
        metaId="meta_Afeces_met",
        initialConcentration=0,
        compartment="Vfeces",
        substanceUnit=U.mmole,
        name="metoprolol (feces)",
        hasOnlySubstanceUnits=True,
        sboTerm=SBO.SIMPLE_CHEMICAL,
        annotations=annotations.species["met"],
    )
)

# blood of the organs and urine of the submodels
for tkey in ["li", "ki"]:
    for skey in SUBSTANCES_BODY:
        _m.replaced_elements.append(
            ReplacedElement(
                sid=f"C{tkey}_blood_{skey}_RE",
                metaId=f"C{tkey}_blood_{skey}_RE",
                elementRef=f"C{tkey}_blood_{skey}",
                submodelRef=SUBMODEL_SID_DICT[tkey],
                portRef=f"{skey}_ext{PORT_SUFFIX}",
            )
        )
for skey in SUBSTANCES_BODY:
    _m.replaced_elements.append(
        ReplacedElement(
            sid=f"Aurine_{skey}_RE",
            metaId=f"Aurine_{skey}_RE",
            elementRef=f"Aurine_{skey}",
            submodelRef=SUBMODEL_SID_DICT["ki"],
            portRef=f"{skey}_urine{PORT_SUFFIX}",
        )
    )

# -------------------------------------------------------------------------------------------------
# Parameters
# -------------------------------------------------------------------------------------------------
_m.parameters = [
    # whole body data
    Parameter(
        "BW",
        75,
        U.kg,
        constant=True,
        name="body weight [kg]",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "BW_ref",
        75,
        U.kg,
        constant=True,
        name="reference body weight [kg]",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes=(
            "Body weight at which the exchange flows of the tissue "
            "distribution (`ftissue_<sid>`) are given; they scale with the "
            "body weight as the volumes, the blood flows and the renal "
            "clearance do."
        ),
    ),
    Parameter(
        "HEIGHT",
        170,
        U.cm,
        constant=True,
        name="height [cm]",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "BSA",
        0,
        U.m2,
        constant=False,
        name="body surface area [m^2]",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "COBW",
        1.548,
        U.ml_per_s_kg,
        constant=True,
        name="cardiac output per bodyweight [ml/s/kg]",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "CO",
        108.33,
        U.ml_per_s,
        constant=False,
        name="cardiac output [ml/s]",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "QC",
        108.33 / 1000 * 60,
        U.l_per_min,
        constant=False,
        name="cardiac output [L/min]",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "Fblood",
        0.02,
        U.dimensionless,
        constant=True,
        name="blood fraction of organ volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    # fractional tissue volumes
    Parameter(
        "FVgu",
        0.0297,
        U.l_per_kg,
        constant=True,
        name="gastrointestinal tract fractional tissue volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        Volume of gastrointestinal tract consisting of
        intestine, pancreas, spleen with volumes of
        0.0171, 0.0026, 0.01
        """,
    ),
    Parameter(
        "FVhe",
        0.0047,
        U.l_per_kg,
        constant=True,
        name="heart fractional tissue volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FVki",
        0.0044,
        U.l_per_kg,
        constant=True,
        name="kidney fractional tissue volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FVli",
        0.0210,
        U.l_per_kg,
        constant=True,
        name="liver fractional tissue volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FVlu",
        0.0076,
        U.l_per_kg,
        constant=True,
        name="lung fractional tissue volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FVre",
        0,
        U.l_per_kg,
        constant=False,
        name="rest of body fractional tissue volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FVve",
        0.0514,
        U.l_per_kg,
        constant=True,
        name="venous fractional tissue volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FVar",
        0.0257,
        U.l_per_kg,
        constant=True,
        name="arterial fractional tissue volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FVpo",
        0.001,
        U.l_per_kg,
        constant=True,
        name="portal fractional tissue volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FVhv",
        0.001,
        U.l_per_kg,
        constant=True,
        name="hepatic venous fractional tissue volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    # fractional tissue blood flows
    Parameter(
        "FQgu",
        0.18,
        U.dimensionless,
        constant=True,
        name="gastrointestinal tract fractional tissue blood flow",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        gastrointestinal tract blood flow consisting of
        intestine, spleen and pancreas
        0.146, 0.017, 0.017
        """,
    ),
    Parameter(
        "FQhe",
        0.04,
        U.dimensionless,
        constant=True,
        name="heart fractional tissue blood flow",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FQki",
        0.190,
        U.dimensionless,
        constant=True,
        name="kidney fractional tissue blood flow",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FQh",
        0.215,
        U.dimensionless,
        constant=True,
        name="hepatic (venous side) fractional tissue blood flow",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FQlu",
        1,
        U.dimensionless,
        constant=True,
        name="lung fractional tissue blood flow",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FQre",
        0,
        U.dimensionless,
        constant=False,
        name="rest of body fractional tissue blood flow",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    # renal function
    Parameter(
        "f_GFR_Qki",
        101 / 1.32354,
        U.ml_per_l,
        constant=True,
        name="relationship GFR and Qki",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        GFR per renal blood flow (76.3 ml/l). Calibrated so that the healthy
        GFR is 101 ml/min at the renal blood flow of 1.32354 l/min of 75 kg,
        the normal GFR of the classes of renal impairment
        (`pkpdsim.impairment`).
        """,
    ),
    Parameter(
        "GFR_base",
        np.nan,
        U.ml_per_min,
        constant=False,
        name="glomerular filtration rate (healthy)",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        The GFR of healthy kidneys, which scales with the renal blood flow and
        so with the body weight; the GFR is `KI__f_renal_function` times this
        rate.
        """,
    ),
]


def _tissue_parameter(
    sid: str, sdict: SubstanceBody, key: str, unit: UnitDefinition
) -> dict:
    """Get the value and unit of `Kp` or `ftissue` of a substance.

    The value of the substance definition, or the fitted value with its
    uncertainty (`fits.FITS`) if the definition has none.
    """
    value = sdict.get(key)
    if value is None:
        return FITS.parameter(f"{key}_{sid}", unit=unit)
    return {"value": value, "unit": unit}


# species specific parameters
for sid, sdict in SUBSTANCES_BODY.items():
    _m.parameters.extend(
        [
            Parameter(
                f"Mr_{sid}",
                sdict["Mr"],
                U.g_per_mole,
                constant=True,
                name=f"molecular weight {sid} [g/mole]",
                sboTerm=SBO.MOLECULAR_MASS,
            ),
            Parameter(
                f"ftissue_{sid}",
                **_tissue_parameter(sid, sdict, "ftissue", U.l_per_min),
                constant=True,
                name=f"tissue distribution {sid}",
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
                notes="Exchange flow at the reference body weight `BW_ref`.",
            ),
            Parameter(
                f"Kp_{sid}",
                **_tissue_parameter(sid, sdict, "Kp", U.dimensionless),
                constant=True,
                name=f"tissue/blood partition coefficient {sid}",
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
                notes="""
                Partition coefficient between the tissue and whole blood, the
                same for every tissue; it sets the volume of distribution.
                """,
            ),
            Parameter(
                f"BP_{sid}",
                sdict["BP"],
                U.dimensionless,
                constant=True,
                name=f"blood to plasma ratio {sid}",
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            ),
        ]
    )
    if "fup" in sdict:
        _m.parameters.append(
            Parameter(
                f"fup_{sid}",
                sdict["fup"],
                U.dimensionless,
                constant=True,
                name=f"fraction unbound in plasma {sid}",
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            )
        )

# the parameters of the kidney model which the body defines
for pid in ["GFR_base", "fup_met", "BP_met"]:
    _m.replaced_elements.append(
        ReplacedElement(
            sid=f"{pid}_ki_RE",
            metaId=f"{pid}_ki_RE",
            elementRef=pid,
            submodelRef=SUBMODEL_SID_DICT["ki"],
            portRef=f"{pid}{PORT_SUFFIX}",
        )
    )

# -------------------------------------------------------------------------------------------------
# Dosing
# -------------------------------------------------------------------------------------------------
_m.parameters.extend(
    [
        # intravenous
        Parameter(
            "IVDOSE_met",
            0,
            U.mg,
            constant=False,
            name="IV bolus dose metoprolol [mg]",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        ),
        Parameter(
            "ti_met",
            10,
            U.second,
            constant=True,
            name="injection time metoprolol [s]",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        ),
        Parameter(
            "Ki_met",
            0.02,
            U.per_min,
            constant=False,
            name="Ki [1/min] injection metoprolol",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        ),
        Parameter(
            "Ri_met",
            0,
            U.mg_per_min,
            constant=False,
            name="Ri [mg/min] rate of infusion metoprolol",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="""
            An infusion sets the rate at its start and 0 at its end (changes of
            the simulation).
            """,
        ),
        # oral
        Parameter(
            "PODOSE_met",
            0,
            U.mg,
            constant=False,
            name="oral dose metoprolol [mg]",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="""
            The undissolved oral dose. A repeated dose adds to it (a change
            with the formula `PODOSE_met + <dose>`), the rest of the previous
            doses of a slow release form is still dissolving.
            """,
        ),
        Parameter(
            "GUTDOSE_met",
            0,
            U.mg,
            constant=False,
            name="dose dissolved in gut metoprolol [mg]",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="An oral solution is dosed here (no dissolution).",
        ),
        Parameter(
            "Ka_dis_met",
            **FITS.parameter("Ka_dis_met", unit=U.per_hr),
            constant=True,
            name="dissolution metoprolol, immediate release [1/hr]",
            sboTerm=SBO.KINETIC_CONSTANT,
            notes="""
            Rate of the dissolution and the gastric emptying of an immediate
            release tablet (dissolved within 10-15 min in vitro, Johnsson1975,
            Sandberg1988; tmax 1-1.5 hr).
            """,
        ),
        Parameter(
            "Ka_dis_sr_met",
            **FITS.parameter("Ka_dis_sr_met", unit=U.per_hr),
            constant=True,
            name="dissolution metoprolol, slow release [1/hr]",
            sboTerm=SBO.KINETIC_CONSTANT,
            notes="""
            Slow release tablet (Lopressor SR, Durules): 96 % dissolved in vitro
            after 10 hr, a first order rate of about 0.26 1/hr (Oosterhuis1988).
            """,
        ),
        Parameter(
            "Ka_dis_cr_met",
            **FITS.parameter("Ka_dis_cr_met", unit=U.per_hr),
            constant=True,
            name="dissolution metoprolol, controlled release [1/hr]",
            sboTerm=SBO.KINETIC_CONSTANT,
            notes="""
            Controlled release tablet (metoprolol succinate, Zok): about zero
            order release over 20 hr in vitro, a first order rate of about
            0.08-0.12 1/hr (Oosterhuis1988, Sandberg1988: mean dissolution time
            8.7 hr).
            """,
        ),
        Parameter(
            "form_sr",
            0,
            U.dimensionless,
            constant=True,
            name="slow release form (0 or 1)",
            sboTerm=SBO.SWITCH_VALUE,
        ),
        Parameter(
            "form_cr",
            0,
            U.dimensionless,
            constant=True,
            name="controlled release form (0 or 1)",
            sboTerm=SBO.SWITCH_VALUE,
        ),
        Parameter(
            "Ka_abs_met",
            **FITS.parameter("Ka_abs_met", unit=U.per_hr),
            constant=True,
            name="absorption metoprolol [1/hr]",
            sboTerm=SBO.KINETIC_CONSTANT,
            notes="""
            Absorption of the dissolved drug: an absorption half-life of 12 min
            and a lag of 0.16-0.18 hr after an oral solution (Regardh1974,
            ka 3.4 1/hr).
            """,
        ),
        Parameter(
            "F_met",
            1.0,
            U.dimensionless,
            constant=True,
            name="fraction absorbed metoprolol",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="""
            Metoprolol is absorbed completely: 95 % of an oral dose of
            3H-metoprolol is recovered in the urine (Regardh1974).
            """,
        ),
        Parameter(
            "F_cr_met",
            **FITS.parameter("F_cr_met", unit=U.dimensionless),
            constant=True,
            name="fraction absorbed metoprolol, controlled release",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="""
            The fraction of the controlled release form which is absorbed,
            relative to `F_met`: the drug released in the colon is absorbed
            less; the bioavailability relative to conventional tablets is 0.65
            (0.42-0.94) (Sandberg1988).
            """,
        ),
    ]
)

# -------------------------------------------------------------------------------------------------
# AssignmentRules
# -------------------------------------------------------------------------------------------------
_m.rules = [
    # Rest body volume
    AssignmentRule(
        "FVre",
        "1.0 l_per_kg - (FVgu + FVhe + FVki + FVli + FVlu + FVve + FVar)",
        U.l_per_kg,
    ),
    # Rest body perfusion
    AssignmentRule("FQre", "1.0 dimensionless - (FQki + FQhe + FQh)", U.dimensionless),
    # Body surface area (Haycock1978)
    AssignmentRule(
        "BSA", "0.024265 m2 * power(BW/1 kg, 0.5378) * power(HEIGHT/1 cm, 0.3964)", U.m2
    ),
    # cardiac output (depending on bodyweight)
    AssignmentRule("CO", "BW*COBW", U.ml_per_s),
    AssignmentRule("QC", "CO/1000 ml_per_l * 60 s_per_min", U.l_per_min),
    # volumes
    AssignmentRule("Vgu", "BW*FVgu", U.liter),
    AssignmentRule("Vhe", "BW*FVhe", U.liter),
    AssignmentRule("Vki", "BW*FVki", U.liter),
    AssignmentRule("Vli", "BW*FVli", U.liter),
    AssignmentRule("Vlu", "BW*FVlu", U.liter),
    AssignmentRule("Vre", "BW*FVre", U.liter),
    # venous and arterial blood volume (corrected for tissue blood volumes)
    AssignmentRule(
        "Vve",
        "BW*FVve - FVve/(FVar+FVve+FVpo+FVhv) * BW * Fblood "
        "* (1 l_per_kg - (FVar+FVve+FVpo+FVhv))",
        U.liter,
    ),
    AssignmentRule(
        "Var",
        "BW*FVar - FVar/(FVar+FVve+FVpo+FVhv) * BW * Fblood "
        "* (1 l_per_kg - (FVar+FVve+FVpo+FVhv))",
        U.liter,
    ),
    AssignmentRule(
        "Vpo",
        "BW*FVpo - FVpo/(FVar+FVve+FVpo+FVhv) * BW * Fblood "
        "* (1 l_per_kg - (FVar+FVve+FVpo+FVhv))",
        U.liter,
    ),
    AssignmentRule(
        "Vhv",
        "BW*FVhv - FVhv/(FVar+FVve+FVpo+FVhv) * BW * Fblood "
        "* (1 l_per_kg - (FVar+FVve+FVpo+FVhv))",
        U.liter,
    ),
    # blood flows
    AssignmentRule("Qgu", "QC*FQgu", U.l_per_min, name="gut blood flow"),
    AssignmentRule("Qhe", "QC*FQhe", U.l_per_min, name="heart blood flow"),
    AssignmentRule("Qki", "QC*FQki", U.l_per_min, name="kidney blood flow"),
    AssignmentRule(
        "Qh", "QC*FQh", U.l_per_min, name="hepatic (venous side) blood flow"
    ),
    AssignmentRule("Qha", "Qh - Qgu", U.l_per_min, name="hepatic artery blood flow"),
    AssignmentRule("Qlu", "QC*FQlu", U.l_per_min, name="lung blood flow"),
    AssignmentRule("Qre", "QC*FQre", U.l_per_min, name="rest of body blood flow"),
    AssignmentRule("Qpo", "Qgu", U.l_per_min, name="portal blood flow"),
    # renal function
    AssignmentRule(
        "GFR_base",
        "f_GFR_Qki * Qki",
        U.ml_per_min,
        name="glomerular filtration rate (healthy)",
    ),
    # dosing
    AssignmentRule(
        "Ki_met",
        "0.693 dimensionless/ti_met * 60 s_per_min",
        U.per_min,
        name="injection rate IV",
        notes="log(2) for the conversion of the injection half-life to the rate.",
    ),
    AssignmentRule(
        "Ka_dis_form_met",
        "(1 dimensionless - form_sr - form_cr) * Ka_dis_met "
        "+ form_sr * Ka_dis_sr_met + form_cr * Ka_dis_cr_met",
        U.per_hr,
        name="dissolution metoprolol of the application form",
    ),
    AssignmentRule(
        "F_form_met",
        "F_met * (1 dimensionless - form_cr * (1 dimensionless - F_cr_met))",
        U.dimensionless,
        name="fraction absorbed metoprolol of the application form",
    ),
    AssignmentRule(
        "dissolution_met",
        "Ka_dis_form_met/60 min_per_hr * PODOSE_met/Mr_met",
        unit=U.mmole_per_min,
        name="dissolution metoprolol",
    ),
]

# Volumes of the organs
for cid, cname in COMPARTMENTS_BODY.items():
    if cid not in VESSELS:
        _m.rules.extend(
            [
                AssignmentRule(
                    f"V{cid}_blood",
                    value=f"V{cid} * Fblood",
                    unit=U.liter,
                    name=f"blood volume of {cname}",
                ),
                AssignmentRule(
                    f"V{cid}_tissue",
                    value=f"V{cid}*(1 dimensionless - Fblood)",
                    unit=U.liter,
                    name=f"tissue volume of {cname}",
                ),
            ]
        )

# --------------------------------------------------------------------------------------------------
# Reactions
# --------------------------------------------------------------------------------------------------
_m.reactions = []

for sid, sdict in SUBSTANCES_BODY.items():
    sname = sdict["name"]

    # tissue distribution
    for cid in TISSUES:
        _m.reactions.append(
            Reaction(
                sid=f"transport_{cid}_{sid}",
                name=f"transport {sname} ({COMPARTMENTS_BODY[cid]})",
                formula=(
                    f"ftissue_{sid} * BW/BW_ref * "
                    f"(C{cid}_blood_{sid}*Kp_{sid} - C{cid}_{sid})",
                    U.mmole_per_min,
                ),
                equation=f"C{cid}_blood_{sid} <-> C{cid}_{sid}",
                compartment=f"V{cid}_tissue",
                sboTerm=SBO.TRANSPORT_REACTION,
            )
        )

    # circulation: ve -> lung -> ar, ar -> organ -> ve, ar -> gut -> po,
    # ar -> liver, po -> liver, liver -> hv -> ve
    flows = [
        ("ve", "lu_blood", "Qlu"),
        ("lu_blood", "ar", "Qlu"),
        ("ar", "ki_blood", "Qki"),
        ("ki_blood", "ve", "Qki"),
        ("ar", "he_blood", "Qhe"),
        ("he_blood", "ve", "Qhe"),
        ("ar", "re_blood", "Qre"),
        ("re_blood", "ve", "Qre"),
        ("ar", "gu_blood", "Qgu"),
        ("gu_blood", "po", "Qgu"),
        ("ar", "li_blood", "Qha"),
        ("po", "li_blood", "Qpo"),
        ("li_blood", "hv", "Qh"),
        ("hv", "ve", "Qh"),
    ]
    for source, target, flow in flows:
        _m.reactions.append(
            Reaction(
                sid=f"Flow_{source.split('_')[0]}_{target.split('_')[0]}_{sid}",
                name=f"blood flow {sname} ({source} to {target})",
                formula=(f"{flow}*C{source}_{sid}", U.mmole_per_min),
                equation=f"C{source}_{sid} -> C{target}_{sid}",
                sboTerm=SBO.TRANSPORT_REACTION,
            )
        )

_m.reactions.extend(
    [
        # iv application
        Reaction(
            sid="iv_met",
            name="iv metoprolol",
            formula=("Ki_met*IVDOSE_met/Mr_met", U.mmole_per_min),
            equation="-> Cve_met",
            compartment="Vve",
            sboTerm=SBO.TRANSPORT_REACTION,
        ),
        # absorption of the dissolved dose from the gut
        Reaction(
            sid="absorption_met",
            name="absorption metoprolol",
            formula=(
                "Ka_abs_met/60 min_per_hr * GUTDOSE_met/Mr_met",
                U.mmole_per_min,
            ),
            equation="-> Cgu_blood_met",
            compartment="Vgu_blood",
            sboTerm=SBO.TRANSPORT_REACTION,
        ),
        # the part of the dissolved dose which is not absorbed
        Reaction(
            sid="excretion_met",
            name="fecal excretion metoprolol",
            formula=(
                "(1 dimensionless - F_form_met) * dissolution_met",
                U.mmole_per_min,
            ),
            equation="-> Afeces_met",
            compartment="Vgu",
            sboTerm=SBO.TRANSPORT_REACTION,
        ),
    ]
)

# --------------------------------------------------------------------------------------------------
# RateRules
# --------------------------------------------------------------------------------------------------
_m.rate_rules = [
    # injection and infusion
    RateRule("IVDOSE_met", "-iv_met*Mr_met + Ri_met", U.mg_per_min),
    # d(PODOSE)/dt = -k_dis
    RateRule("PODOSE_met", "-dissolution_met*Mr_met", U.mg_per_min),
    # d(GUTDOSE)/dt = +F*k_dis - k_abs
    RateRule(
        "GUTDOSE_met",
        "F_form_met * dissolution_met*Mr_met - absorption_met*Mr_met",
        U.mg_per_min,
    ),
]

# --------------------------------------------------------------------------------------------------
# Plasma concentrations
# --------------------------------------------------------------------------------------------------
# The circulating species are blood concentrations, the measured matrix of the
# studies is plasma: the plasma concentration is the blood concentration over
# the blood to plasma ratio.
for sid, sdict in SUBSTANCES_BODY.items():
    _m.species.append(
        Species(
            f"Cveplasma_{sid}",
            metaId=f"meta_Cveplasma_{sid}",
            initialConcentration=0,
            compartment="Vve",
            substanceUnit=U.mmole,
            name=f"{sdict['name']} (venous plasma)",
            hasOnlySubstanceUnits=False,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species[sid],
        )
    )
    _m.rules.append(
        AssignmentRule(
            f"Cveplasma_{sid}",
            f"Cve_{sid} / BP_{sid}",
            unit=U.mM,
            name=f"{sdict['name']} plasma concentration",
            notes="The blood concentration over the blood to plasma ratio (BP).",
        )
    )

# -------------------------------------------------------
# Pharmacodynamics: reduction of the exercise heart rate
# -------------------------------------------------------
# Metoprolol reduces the heart rate of an exercise test by beta1 blockade. The
# reduction is a direct function of the plasma concentration, the effect has
# the half-life of the plasma concentration (no hysteresis, Johnsson1975). The
# heart rate `HR` is the baseline of the effect (the exercise heart rate before
# the dose); it does not change the cardiac output and so not the
# pharmacokinetics (the exercise tests last 4-10 min).
_m.parameters.extend(
    [
        Parameter(
            "HR",
            70,
            U.per_min,
            constant=True,
            name="heart rate without metoprolol [1/min]",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="The baseline of the effect, e.g. the exercise heart rate before the dose.",
        ),
        Parameter(
            "HRred_Emax",
            **FITS.parameter("HRred_Emax", unit=U.dimensionless),
            constant=True,
            name="maximal relative reduction of the heart rate",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="Exercise heart rate: Mmax 52/min of 148/min (Kirchheiner2004).",
        ),
        Parameter(
            "HRred_EC50",
            **FITS.parameter("HRred_EC50", unit=U.mM),
            constant=True,
            name="metoprolol plasma concentration of the half-maximal reduction",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
            notes="CM50 40 µg/l = 0.15 µM (Kirchheiner2004).",
        ),
        Parameter(
            "HRred_n",
            1.0,
            U.dimensionless,
            constant=True,
            name="Hill coefficient of the reduction of the heart rate",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        ),
    ]
)
_m.rules.extend(
    [
        AssignmentRule(
            "HRred",
            "HRred_Emax * power(Cveplasma_met/HRred_EC50, HRred_n)"
            " / (1 dimensionless + power(Cveplasma_met/HRred_EC50, HRred_n))",
            U.dimensionless,
            name="relative reduction of the heart rate",
        ),
        AssignmentRule(
            "HReff",
            "HR * (1 dimensionless - HRred)",
            U.per_min,
            name="heart rate with metoprolol",
        ),
    ]
)

model_body = _m

if __name__ == "__main__":
    from pkdb_models.models.metoprolol import MODEL_BASE_PATH

    results = create_model(
        model=model_body,
        filepath=MODEL_BASE_PATH / f"{model_body.sid}.xml",
    )
