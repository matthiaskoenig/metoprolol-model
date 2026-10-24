# Release notes

## Release notes for metoprolol-model 0.8.0

Made from pkdb_models 3a0b49144b with pkpdsim 0.11.0.

The changes since 0.7.0.

### Core libraries

The versions of the core libraries cannot be compared, there is no lock file in the previous release. The release uses:

- pkpdsim 0.11.0
- sbmlsim 0.13.0
- sbmlutils 0.17.0

### Libraries

The versions cannot be compared, there is no lock file in the previous release.

### Data

- Added: `metoprolol/Bae2014`, `metoprolol/Blomqvist1988`, `metoprolol/Cerqueira2003`, `metoprolol/Cerqueira2005`, `metoprolol/Fux2005`, `metoprolol/Jin2008`, `metoprolol/Johnsson1975`, `metoprolol/Kirchheiner2004`, `metoprolol/Lennard1982`, `metoprolol/Oosterhuis1988`, `metoprolol/Regardh1974`, `metoprolol/Sandberg1988`, `metoprolol/Seeringer2008`

### Analysis

#### Models

- `metoprolol_body.xml`: added 27 species, 9 reactions, 19 parameters; removed 27 species, 18 reactions, 148 parameters; changed values `BP_met` 1 → 1.2, `FQgu` 0.146 → 0.18, `FVgu` 0.0171 → 0.0297, `Ka_abs_met` 1 → 1.00038, `Ka_dis_met` 1 → 2.5259, `Mr_metoh` 283.368 → 283.363, `ftissue_mam` 0 → 1, `ftissue_met` 0 → 45.799, `ftissue_metoh` 0 → 1, `fup_met` 1 → 0.88
- `metoprolol_body_flat.xml`: added 27 species, 11 reactions, 120 parameters; removed 30 species, 20 reactions, 161 parameters; changed values `BP_met` 1 → 1.2, `FQgu` 0.146 → 0.18, `FVgu` 0.0171 → 0.0297, `KI__MAMEX_f` 0.774194 → 1.53418, `KI__METEX_f` 0.0967742 → 0.81523, `KI__METOHEX_f` 0.129032 → 6.76476, `Ka_abs_met` 1 → 1.00038, `Ka_dis_met` 1 → 2.5259, `Mr_metoh` 283.368 → 283.363, `ftissue_mam` 0 → 1, `ftissue_met` 0 → 45.799, `ftissue_metoh` 0 → 1, `fup_met` 1 → 0.88
- `metoprolol_kidney.xml`: added 5 parameters; removed 1 parameter; changed values `MAMEX_f` 0.774194 → 1.53418, `METEX_f` 0.0967742 → 0.81523, `METOHEX_f` 0.129032 → 6.76476
- `metoprolol_liver.xml`: added 2 reactions, 99 parameters; removed 2 reactions, 12 parameters

#### Experiments

- Added: `AbsorptionExperiment`, `Bae2014`, `Blomqvist1988`, `Cerqueira2003`, `Cerqueira2005`, `DosingExperiment`, `EHRExperiment`, `Jin2008`, `Johnsson1975`, `Kirchheiner2004`, `Lennard1982`, `MetoprololParameterScan`, `Oosterhuis1988`, `Regardh1974`, `Sandberg1988`

#### Fits

- `PD`: `PD_20261017_193512__e995e`, no fit record in the previous release
- `PK`: `PK_20261017_183259__fc82a`, no fit record in the previous release

## Release notes for metoprolol-model 0.7.0

We are pleased to release a new version of the metoprolol-model including the 
following changes:

### Features
- sbml4humans report
- model annotations
- zenodo integration

Your metoprolol-model team

