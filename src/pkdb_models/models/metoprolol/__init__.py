"""Metoprolol: PBPK/PD model of metoprolol and its effect on the heart rate.

The paths of the model and its model object `MODEL`, which the commands
`run_simulation`, `run_fit`, `run_report` and `run_identifiability` of pkpdsim
run by its package `pkdb_models.models.metoprolol`.
"""

from pathlib import Path

from pkpdsim.model import FigureSettings, PKPDModel, SimulatorSettings
from pkpdsim.release.settings import Author, ReleaseSettings

from pkdb_models.models.metoprolol.tolerances import ABSOLUTE_TOLERANCE

METOPROLOL_PATH = Path(__file__).parent

MODEL_BASE_PATH = METOPROLOL_PATH / "models" / "output" / "models"
MODEL_PATH = MODEL_BASE_PATH / "metoprolol_body_flat.xml"

DATA_PATH_BASE = METOPROLOL_PATH / "data"
DATA_PATH_METOPROLOL = DATA_PATH_BASE / "metoprolol"
DATA_PATHS = [DATA_PATH_METOPROLOL]

MODEL = PKPDModel(
    name="metoprolol",
    package=__name__,
    title="Metoprolol PBPK/PD model",
    path=METOPROLOL_PATH,
    model_path=MODEL_PATH,
    data_paths=tuple(DATA_PATHS),
    archive_path=MODEL_BASE_PATH.parent / "metoprolol_model.omex",
    factory=".models.factory:create_metoprolol_models",
    experiments=".simulations:EXPERIMENTS",
    fit_definitions=".fitting.fitting:FIT_DEFINITIONS",
    fit_identifiability=True,
    # the adopted fits, whose values the factory takes (`models/fits.py`)
    fits=("PK_20261017_183259__fc82a", "PD_20261017_193512__e995e"),
    simulator=SimulatorSettings(
        absolute_tolerance=ABSOLUTE_TOLERANCE, relative_tolerance=1e-10
    ),
    figures=FigureSettings(formats=("svg",), fig_dpi=150, legend_position="outside"),
    # the release of the model repository
    release=ReleaseSettings(
        title=(
            "Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model"
            " of metoprolol"
        ),
        repository="matthiaskoenig/metoprolol-model",
        doi="10.5281/zenodo.5554358",
        authors=(
            Author(
                "König, Matthias",
                "0000-0003-1725-179X",
                (
                    "Humboldt-Universität zu Berlin, Faculty of Life Sciences, Department of Biology, Institute of Theoretical Biology, Systems Medicine of the Liver; University of Stuttgart, Institute of Structural Mechanics and Dynamics in Aerospace Engineering; University of Southern Denmark, Clinical Pharmacology, Pharmacy and Environmental Medicine, Department of Public Health; University Hospital Schleswig-Holstein, Campus Lübeck, First Department of Medicine, Lübeck, Germany"
                ),
            ),
            Author(
                "Ogata, Paula",
                "0000-0003-0379-6764",
                "Faculty of Engineering, University of Porto, Porto, Portugal",
            ),
        ),
        keywords=(
            "model",
            "metoprolol",
            "beta blocker",
            "CYP2D6",
            "pharmacokinetics",
            "pharmacodynamics",
            "PBPK",
            "physiologically based pharmacokinetic model",
            "SBML",
        ),
        docker_image="matthiaskoenig/metoprolol",
        funding=(
            "Matthias König was supported by the Federal Ministry of Research, Technology and Space (BMFTR, Germany) within ATLAS by grant number 031L0304B and by the German Research Foundation (DFG) within the Research Unit Program FOR 5151 QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection - A Systems Medicine Approach) by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA). This work was supported by the BMBF-funded de.NBI Cloud within the German Network for Bioinformatics Infrastructure (de.NBI) (031A537B, 031A533A, 031A538A, 031A533B, 031A535A, 031A537C, 031A534A, 031A532B)."
        ),
        description=(
            "This repository provides the metoprolol physiologically based"
            " pharmacokinetic/pharmacodynamic (PBPK/PD) model: its oral and"
            " intravenous dosing with the immediate, slow and controlled release"
            " forms, its distribution, its metabolism by CYP2D6 (with the CYP2D6"
            " genotypes) and other enzymes in the liver to alpha-hydroxymetoprolol"
            " and metoprolol acid, the renal excretion of metoprolol and its"
            " metabolites with the renal function and the reduction of the"
            " exercise heart rate."
        ),
        first_year=2020,
    ),
)
"""The metoprolol model: its commands, see `pkpdsim.model`."""
