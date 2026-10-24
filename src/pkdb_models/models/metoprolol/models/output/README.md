[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5554358.svg)](https://doi.org/10.5281/zenodo.5554358)
[![GitHub Action](https://github.com/matthiaskoenig/metoprolol-model/actions/workflows/python.yml/badge.svg)](https://github.com/matthiaskoenig/metoprolol-model/actions/workflows/python.yml)
[![GitHub Action](https://github.com/matthiaskoenig/metoprolol-model/actions/workflows/docker.yml/badge.svg)](https://github.com/matthiaskoenig/metoprolol-model/actions/workflows/docker.yml)

# metoprolol model
This repository provides the metoprolol physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model: the oral (immediate, slow and controlled release tablets, solution) and intravenous dosing of the tartrate and succinate salts, the distribution, the metabolism of metoprolol by CYP2D6 (with the CYP2D6 genotypes and activity scores) and other enzymes in the liver to alpha-hydroxymetoprolol and metoprolol acid, the renal excretion relative to the glomerular filtration rate (renal impairment) and the reduction of the exercise heart rate.

The model is distributed as [SBML](http://sbml.org) format available from [`metoprolol_body_flat.xml`](./models/metoprolol_body_flat.xml) with 
corresponding [SBML4humans model report](https://sbml4humans.de/report?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmatthiaskoenig%2Fmetoprolol-model%2Fmain%2Fmodels%2Fmetoprolol_body_flat.xml) and [model equations](./models/metoprolol_body_flat.md).

The COMBINE archive is available from [`metoprolol_model.omex`](./metoprolol_model.omex).

![model overview](./figures/metoprolol_body.svg)

### Comp submodels
* **liver** submodel [`metoprolol_liver.xml`](./models/metoprolol_liver.xml) with [SBML4humans report](https://sbml4humans.de/report?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmatthiaskoenig%2Fmetoprolol-model%2Fmain%2Fmodels%2Fmetoprolol_liver.xml) and [equations](./models/metoprolol_liver.md).
* **kidney** submodel [`metoprolol_kidney.xml`](./models/metoprolol_kidney.xml) with [SBML4humans report](https://sbml4humans.de/report?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmatthiaskoenig%2Fmetoprolol-model%2Fmain%2Fmodels%2Fmetoprolol_kidney.xml) and [equations](./models/metoprolol_kidney.md).
* **whole-body** submodel [`metoprolol_body.xml`](./models/metoprolol_body.xml) with [SBML4humans report](https://sbml4humans.de/report?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmatthiaskoenig%2Fmetoprolol-model%2Fmain%2Fmodels%2Fmetoprolol_body.xml) and [equations](./models/metoprolol_body.md).

## How to cite
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5554358.svg)](https://doi.org/10.5281/zenodo.5554358)

> König, M. & Ogata, P. (2026).
> *Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of metoprolol.*   
> Zenodo. [https://doi.org/10.5281/zenodo.5554358](https://doi.org/10.5281/zenodo.5554358)

## License

* Source Code: [MIT](https://opensource.org/license/MIT)
* Documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
* Models: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.


## Run simulations
### python
Clone the repository 
```bash
git clone https://github.com/matthiaskoenig/metoprolol-model.git
cd metoprolol-model
```

#### uv
Run the complete analysis with uv (https://docs.astral.sh/uv/getting-started/installation/):
```bash
uv run run_simulation pkdb_models.models.metoprolol -a all -r results
```

#### pip
If you use pip install the package via
```bash
pip install -e .
```
Run the complete analysis in the environment via:
```bash
run_simulation pkdb_models.models.metoprolol -a all -r results
```

### docker
Simulations can also be run within a docker container:

```bash
docker run -v "${PWD}/results:/results" -it matthiaskoenig/metoprolol:latest /bin/bash
```

Run the complete analysis:
```bash
uv run run_simulation pkdb_models.models.metoprolol -a all -r /results
```
The results are written into the mounted `/results` folder on the host.

In case of permission issues with the mounted folder, adjust ownership and access rights with:
```bash
sudo chown $(id -u):$(id -g) -R "${PWD}/results"
sudo chmod 775 "${PWD}/results"
```

## Funding
Matthias König was supported by the Federal Ministry of Research, Technology and Space (BMFTR, Germany) within ATLAS by grant number 031L0304B and by the German Research Foundation (DFG) within the Research Unit Program FOR 5151 QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection - A Systems Medicine Approach) by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA). This work was supported by the BMBF-funded de.NBI Cloud within the German Network for Bioinformatics Infrastructure (de.NBI) (031A537B, 031A533A, 031A538A, 031A533B, 031A535A, 031A537C, 031A534A, 031A532B).

© 2020-2026 Matthias König, [Systems Medicine of the Liver](https://livermetabolism.com)
