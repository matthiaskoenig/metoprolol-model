"""Templates of the metoprolol models: units, model units and creators."""

from pkpdsim.templates import creators as template_creators
from sbmlutils.factory import Creator, ModelUnits, UnitDefinition, Units


class U(Units):
    """UnitDefinitions."""

    g_per_mole = UnitDefinition("g_per_mole", "g/mole")
    l_per_min = UnitDefinition("litre_per_min", "litre/min")
    m2 = UnitDefinition("m2", "meter^2")
    mg = UnitDefinition("mg")
    min = UnitDefinition("min")
    mM = UnitDefinition("mM", "mmole/liter")
    mmole = UnitDefinition("mmole")
    mmole_per_min = UnitDefinition("mmole_per_min", "mmole/min")
    mmole_per_min_l = UnitDefinition("mmole_per_min_l", "mmole/min/liter")
    per_min = UnitDefinition("per_min", "1/min")


model_units = ModelUnits(
    time=U.min,
    extent=U.mmole,
    substance=U.mmole,
    length=U.meter,
    area=U.m2,
    volume=U.liter,
)


creators = [
    Creator(
        familyName="Ogata",
        givenName="Paula",
        email="ogata.mpaula@gmail.com",
        organization="Faculty of Engineering, University of Porto, Porto, Portugal",
    ),
    *template_creators,
]
