"""The simulation experiments of the metoprolol model and their groups.

They are the registry of `MODEL`, the experiments its commands simulate.
"""

from sbmlsim.experiment import SimulationExperiment

from pkdb_models.models.metoprolol import MODEL
from pkdb_models.models.metoprolol.experiments.misc import (
    AbsorptionExperiment,
    DosingExperiment,
    EHRExperiment,
)
from pkdb_models.models.metoprolol.experiments.scans import MetoprololParameterScan
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

EXPERIMENTS: dict[str, list[type[SimulationExperiment]]] = {
    "studies": [
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
    ],
    "iv": [
        Johnsson1975,
        Regardh1974,
    ],
    "po": [
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
    ],
    "cyp2d6": [
        Bae2014,
        Jin2008,
        Kirchheiner2004,
        Lennard1982,
    ],
    "renal_impairment": [
        Cerqueira2005,
    ],
    "heart_rate": [
        Blomqvist1988,
        Johnsson1975,
        Kirchheiner2004,
        Oosterhuis1988,
        Sandberg1988,
    ],
    "misc": [
        AbsorptionExperiment,
        DosingExperiment,
        EHRExperiment,
    ],
    "scans": [
        MetoprololParameterScan,
    ],
}
EXPERIMENTS["all"] = EXPERIMENTS["studies"] + EXPERIMENTS["misc"] + EXPERIMENTS["scans"]


if __name__ == "__main__":
    MODEL.run_simulation_experiments(EXPERIMENTS["all"], MODEL.simulation_dir / "all")
