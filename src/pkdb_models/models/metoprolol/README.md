# Metoprolol

Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of the beta blocker metoprolol: its oral dosing as immediate, slow and controlled release tablets or as a solution and its intravenous infusion (doses of the tartrate and succinate salts are converted to metoprolol), its distribution in blood (the plasma is the blood over the blood to plasma ratio) and in the tissues, its hepatic metabolism to alpha-hydroxymetoprolol and metoprolol acid by CYP2D6 (scaled by the activity score of the CYP2D6 diplotype) and to metoprolol acid by other enzymes, the renal excretion of metoprolol and its metabolites relative to the glomerular filtration rate, and the reduction of the exercise heart rate as an Emax model of the plasma concentration. The model describes the effects of the dose, the CYP2D6 genotypes (poor, intermediate, extensive and ultrarapid metabolizers, the *10 allele) and of renal impairment.

The published version of the model is [metoprolol-model](https://github.com/matthiaskoenig/metoprolol-model) ([doi:10.5281/zenodo.5554358](https://doi.org/10.5281/zenodo.5554358)).

## Structure

- `__init__.py`: the paths of the model and its model object `MODEL` with its release metadata and its adopted fits, which the commands below run (pkpdsim).
- `models/`: the tissue models (`model_liver.py` with the CYP2D6 model of the alleles `model_cyp2d6.py`, `model_kidney.py`) and the whole-body model (`model_body.py`). `models/factory.py` creates the SBML models, the flattened whole-body model which is simulated, the ODEs and the COMBINE archive in `models/output/`; the fitted values come from the adopted fits (`models/fits.py`, `models/output/fits/`).
- `experiments/`: the simulation experiments of the clinical studies (`studies/`), the application forms, the intravenous dosing and the exercise heart rate (`misc/`) and the parameter scans of the dose, the renal function and the CYP2D6 activity score (`scans/`). The fit mappings are described with the vocabulary of `pkpdsim.metadata`.
- `fitting/`: the fit problems of the pharmacokinetics (`PK`) and of the reduction of the heart rate on the adopted pharmacokinetics (`PD`), their parameters and the selection of the training, validation and outlier data.
- `sensitivity/`: the sensitivity analysis of the pharmacokinetics and of the reduction of the heart rate.
- `metoprolol_pk.py`: the pharmacokinetic parameters of the scans, the non-compartmental analysis of `pkpdutils`.
- `tolerances.py`: the absolute tolerances of the integrator per state.
- `simulations.py`: the simulation experiments and their groups, `MODEL` runs them.
- `data/`: the data of the studies, a subset of the PK-DB studies (`data/collect_data.py`).
- `TODO.md`: the open issues of the model.

## Commands

```bash
# models, simulations
run_simulation pkdb_models.models.metoprolol --action factory
run_simulation pkdb_models.models.metoprolol --action list_experiments
run_simulation pkdb_models.models.metoprolol --action simulate --experiments all
run_simulation pkdb_models.models.metoprolol --action simulate --experiments all --uncertainty

# fits, adoption of a fit, reports of stored parameters, identifiability
run_fit pkdb_models.models.metoprolol --subset=PK --runs=3 --cores=3 --method=DE
run_fit pkdb_models.models.metoprolol --subset=PD --runs=3 --cores=3 --method=DE
run_fit pkdb_models.models.metoprolol --adopt PK_<fit id>
run_report pkdb_models.models.metoprolol --subset=PK results/fit/PK_<fit id>/parameters.json
run_identifiability pkdb_models.models.metoprolol --subset=PK results/fit/PK_<fit id>/parameters.json

# sensitivity analysis (local by default)
python -m pkdb_models.models.metoprolol.sensitivity.sensitivity_analysis
```

The results are written into `results/` of the model.

## Adopted fits and uncertainty

The values of the fitted parameters come from the adopted fits of the model,
not from numbers in the code: `PK_20261017_183259__fc82a` (the
pharmacokinetics) and `PD_20261017_193512__e995e` (the reduction of the
exercise heart rate). `run_fit pkdb_models.models.metoprolol --adopt <fit id>`
copies the record of a finished fit (its parameters, problem, profile
likelihood and Fisher information) into `models/output/fits/<fit id>/`, which is
tracked; the ids of the adopted fits are listed in `fits` of the model object
(`__init__.py`). The factory takes the fitted values and their uncertainty from
the records (`models/fits.py`) and writes the uncertainty into the SBML
(`distrib:uncertainty`). `run_simulation ... --uncertainty` runs the
experiments over draws of these distributions and draws the simulations as the
median with a band of quantiles into `results/simulation_uncertainty`. A refit
is: fit, adopt, replace the id in `fits`, rebuild the model. See the
documentation of the repository on fitting (`docs/fitting.md`).
