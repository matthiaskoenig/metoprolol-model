"""Model of the CYP2D6 activity of a genotype, merged into the metoprolol liver.

The activity `cyp2d6_activity` of the diplotype is the sum of the activities of
its two alleles. An allele is selected by its index in `ALLELE_ACTIVITIES`
(`cyp2d6_allele1`, `cyp2d6_allele2`), the index -1 selects the custom activity
`cyp2d6_ac` of the diplotype. The default is *1/*1 with the activity 2.

The model is a copy of the CYP2D6 model of dextromethorphan with the same ids,
so that metoprolol does not depend on the dextromethorphan package.
"""

import math

from pkpdsim.templates import terms_of_use
from sbmlutils.factory import AssignmentRule, Model, Parameter
from sbmlutils.metadata import SBO

from pkdb_models.models.metoprolol.models import templates

#: activity scores of the CYP2D6 alleles, the parameters `cyp2d6_a<index>`
ALLELE_ACTIVITIES: dict[str, float] = {
    "*1": 1.0,
    "*10": 0.25,
    "*100": 0.0,
    "*101": 0.0,
    "*10x2": 0.5,
    "*11": 0.0,
    "*114": 0.0,
    "*12": 0.0,
    "*120": 0.0,
    "*124": 0.0,
    "*129": 0.0,
    "*13": 0.0,
    "*14": 0.5,
    "*15": 0.0,
    "*17": 0.5,
    "*17x2": 1.0,
    "*18": 0.0,
    "*19": 0.0,
    "*1x2": 2.0,
    "*1x3": 3.0,
    "*1x4": 4.0,
    "*1x5": 5.0,
    "*1x6": 6.0,
    "*2": 1.0,
    "*20": 0.0,
    "*21": 0.0,
    "*27": 1.0,
    "*29": 0.5,
    "*29x2": 1.0,
    "*2x2": 2.0,
    "*2x3": 3.0,
    "*2x4": 4.0,
    "*2x5": 5.0,
    "*2x6": 6.0,
    "*3": 0.0,
    "*31": 0.0,
    "*33": 1.0,
    "*34": 1.0,
    "*35": 1.0,
    "*35x2": 2.0,
    "*36": 0.0,
    "*36x2": 0.0,
    "*38": 0.0,
    "*39": 1.0,
    "*3x2": 0.0,
    "*4": 0.0,
    "*40": 0.0,
    "*41": 0.5,
    "*41x2": 1.0,
    "*41x3": 1.5,
    "*42": 0.0,
    "*44": 0.0,
    "*45": 1.0,
    "*45x2": 2.0,
    "*46": 1.0,
    "*47": 0.0,
    "*48": 1.0,
    "*49": 0.5,
    "*4x2": 0.0,
    "*4x3": 0.0,
    "*4x4": 0.0,
    "*4x5": 0.0,
    "*5": 0.0,
    "*50": 0.5,
    "*51": 0.0,
    "*53": 1.0,
    "*54": 0.5,
    "*55": 0.5,
    "*56": 0.0,
    "*57": 0.0,
    "*59": 0.5,
    "*6": 0.0,
    "*60": 0.0,
    "*62": 0.0,
    "*68": 0.0,
    "*69": 0.0,
    "*6x2": 0.0,
    "*7": 0.0,
    "*8": 0.0,
    "*81": 0.0,
    "*9": 0.5,
    "*92": 0.0,
    "*96": 0.0,
    "*99": 0.0,
    "*9x2": 1.0,
}


class U(templates.U):
    """UnitsDefinitions."""


_m = Model(
    "cyp2d6",
    name="Model for CYP2D6 activity",
    notes="""
    # Model for CYP2D6 activity

    Allele activity information was used to determine enzymatic activity of CYP2D6.
    """
    + terms_of_use,
    units=U,
    model_units=templates.model_units,
    creators=templates.creators,
)

_m.parameters = [
    Parameter(
        f"cyp2d6_a{ka}",
        allele_activity,
        U.dimensionless,
        name=f"{allele} activity",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    )
    for ka, (allele, allele_activity) in enumerate(ALLELE_ACTIVITIES.items())
]
_m.parameters.extend(
    [
        Parameter(
            "cyp2d6_ac",
            1.0,
            U.dimensionless,
            name="custom allele activity",
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        ),
        # alleles in model (index in ALLELE_ACTIVITIES)
        Parameter(
            "cyp2d6_allele1",
            0,
            unit=U.dimensionless,
            name="allele 1",
            constant=False,
            sboTerm=SBO.SWITCH_VALUE,
        ),
        Parameter(
            "cyp2d6_allele2",
            0,
            unit=U.dimensionless,
            name="allele 2",
            constant=False,
            sboTerm=SBO.SWITCH_VALUE,
        ),
        # activities of alleles in model
        Parameter(
            "cyp2d6_activity1",
            math.nan,
            unit=U.dimensionless,
            name="activity of allele 1",
            constant=False,
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        ),
        Parameter(
            "cyp2d6_activity2",
            math.nan,
            unit=U.dimensionless,
            name="activity of allele 2",
            constant=False,
            sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        ),
    ]
)

_m.rules = []
for allele in [1, 2]:
    # piecewise function which selects the activity of the allele:
    # piecewise(x1, y1, [x2, y2,] [...] [z]): if (y1), x1, otherwise, if (y2), x2,
    # etc. Otherwise, z.
    rule_activity = f"piecewise(cyp2d6_ac/2 dimensionless, cyp2d6_allele{allele} == -1,"
    for ka in range(len(ALLELE_ACTIVITIES)):
        rule_activity += f"cyp2d6_a{ka}, cyp2d6_allele{allele} == {ka},"
    rule_activity += "cyp2d6_ac/2 dimensionless)"

    _m.rules.append(
        AssignmentRule(
            f"cyp2d6_activity{allele}",
            rule_activity,
            unit=U.dimensionless,
            name=f"activity of allele {allele}",
        ),
    )

_m.rules.append(
    AssignmentRule(
        "cyp2d6_activity",
        "(cyp2d6_activity1 + cyp2d6_activity2)",
        unit=U.dimensionless,
        name="activity of CYP2D6 diplotype",
    )
)

model_cyp2d6 = _m
