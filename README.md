[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5554358.svg)](https://doi.org/10.5281/zenodo.5554358)
[![Release](https://img.shields.io/github/v/release/matthiaskoenig/metoprolol-model)](https://github.com/matthiaskoenig/metoprolol-model/releases)
[![Documentation](https://github.com/matthiaskoenig/metoprolol-model/actions/workflows/docs.yml/badge.svg)](https://matthiaskoenig.github.io/metoprolol-model/)
[![CI](https://github.com/matthiaskoenig/metoprolol-model/actions/workflows/ci.yml/badge.svg)](https://github.com/matthiaskoenig/metoprolol-model/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/docker/v/matthiaskoenig/metoprolol?sort=semver&label=docker)](https://hub.docker.com/r/matthiaskoenig/metoprolol)
[![Python](https://img.shields.io/badge/python-3.14-blue)](https://www.python.org)
[![Code license: MIT](https://img.shields.io/badge/code%20license-MIT-blue)](https://opensource.org/license/MIT)
[![Model license: CC BY-SA 4.0](https://img.shields.io/badge/model%20license-CC%20BY--SA%204.0-lightgrey)](https://creativecommons.org/licenses/by-sa/4.0/)

# Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of metoprolol

This repository provides the metoprolol physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model: its oral and intravenous dosing with the immediate, slow and controlled release forms, its distribution, its metabolism by CYP2D6 (with the CYP2D6 genotypes) and other enzymes in the liver to alpha-hydroxymetoprolol and metoprolol acid, the renal excretion of metoprolol and its metabolites with the renal function and the reduction of the exercise heart rate.

Documentation: <https://matthiaskoenig.github.io/metoprolol-model/>

## Quick start

```bash
git clone https://github.com/matthiaskoenig/metoprolol-model.git && cd metoprolol-model
uv sync
uv run run_simulation pkdb_models.models.metoprolol --action all -r results
```

## How to cite

> König, M. & Ogata, P. (2026). *Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of metoprolol*. Zenodo. https://doi.org/10.5281/zenodo.5554358

## License

* Source Code: [MIT](https://opensource.org/license/MIT)
* Documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
* Models: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

&copy; 2020-2026 Matthias König and Paula Ogata
