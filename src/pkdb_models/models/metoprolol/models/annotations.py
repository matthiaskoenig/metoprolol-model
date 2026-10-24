"""Annotations of the metoprolol models: the species and the shared compartments."""

from pkpdsim.annotations import compartments
from sbmlutils.metadata import BQB

__all__ = ["compartments", "species"]

species = {
    "met": [
        (BQB.IS, "chebi/CHEBI:6904"),
        (BQB.IS, "ncit/C61845"),
        (BQB.IS, "inchikey/IUBSYMUCCVWXPE-UHFFFAOYSA-N"),
    ],
    "metoh": [
        (BQB.IS, "chebi/CHEBI:165230"),
        (BQB.IS, "inchikey/OFRYBPCSEMMZHR-UHFFFAOYSA-N"),
    ],
    "mam": [
        (BQB.IS, "chebi/CHEBI:83478"),
        (BQB.IS, "inchikey/PUQIRTNPJRFRCZ-UHFFFAOYSA-N"),
    ],
}
