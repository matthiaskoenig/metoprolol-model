"""The fit parameters of the metoprolol model.

The pharmacokinetics (`parameters_pk`) are fitted on the plasma
concentrations of metoprolol and its metabolites after intravenous and oral
doses (Johnsson1975, Regardh1974 with the intravenous data which separate the
clearance from the bioavailability) and on the CYP2D6 genotypes, which
separate the CYP2D6 dependent from the independent metabolism. The bounds
contain the literature values. Not fitted: the fraction absorbed (`F_met` 1,
complete absorption, Regardh1974), the binding in plasma (`fup_met` 0.88) and
the blood to plasma ratio (`BP_met` 1.2, Regardh1974), the fast exchanges of
the liver, the distribution of metoprolol acid (`Kp_mam`, `ftissue_<sid>` of
the metabolites), the Km of the other enzymes (`LI__ODM_Km_met`) and the Km
of CYP2D6 (`LI__CYP2D6_Km_met` 15 µM of the microsomes: the profile of the
first fit, PK_20261017_162147__f197c, was flat between 2 and 100 µM).

The pharmacodynamics (`parameters_pd`) are fitted on the relative reduction
of the exercise heart rate (`HRred`) with the adopted pharmacokinetics.
"""

from sbmlsim.fit import FitParameter

#: the pharmacokinetics
parameters_pk: list[FitParameter] = [
    # tissue distribution: Vss about 4.5 l/kg of plasma (Regardh1974),
    # distribution half-life about 12 min
    FitParameter(
        pid="Kp_met",
        start_value=3.0,
        lower_bound=0.5,
        upper_bound=20,
        unit="dimensionless",
    ),
    FitParameter(
        pid="ftissue_met",
        start_value=2.0,
        lower_bound=0.05,
        upper_bound=50,
        unit="l/min",
    ),
    # hepatic metabolism: CYP2D6 alpha-hydroxylation and O-demethylation,
    # the O-demethylation by other enzymes (the clearance of poor metabolizers)
    FitParameter(
        pid="LI__METOH_Vmax",
        start_value=0.0020,
        lower_bound=1e-5,
        upper_bound=0.1,
        unit="mmole/min/l",
    ),
    FitParameter(
        pid="LI__ODM2D6_Vmax",
        start_value=0.0135,
        lower_bound=1e-4,
        upper_bound=0.5,
        unit="mmole/min/l",
    ),
    FitParameter(
        pid="LI__ODM_Vmax",
        start_value=0.0029,
        lower_bound=1e-5,
        upper_bound=0.1,
        unit="mmole/min/l",
    ),
    # renal clearances relative to the GFR: metoprolol 95-109 ml/min
    # (Regardh1974), alpha-hydroxymetoprolol 225-240 ml/min (Kirchheiner2004),
    # the metabolites 120 ml/min (Regardh1974); the upper bound of
    # alpha-hydroxymetoprolol is the renal plasma flow (about 7 GFR)
    FitParameter(
        pid="KI__METEX_f",
        start_value=1.1,
        lower_bound=0.3,
        upper_bound=3.0,
        unit="dimensionless",
    ),
    FitParameter(
        pid="KI__METOHEX_f",
        start_value=2.2,
        lower_bound=0.5,
        upper_bound=7.0,
        unit="dimensionless",
    ),
    FitParameter(
        pid="KI__MAMEX_f",
        start_value=1.5,
        lower_bound=0.3,
        upper_bound=5.0,
        unit="dimensionless",
    ),
    # distribution of alpha-hydroxymetoprolol: half-life 5.4-6.1 hr
    FitParameter(
        pid="Kp_metoh",
        start_value=1.0,
        lower_bound=0.1,
        upper_bound=10,
        unit="dimensionless",
    ),
    # absorption: an oral solution ka 3.4 1/hr with a lag (Regardh1974),
    # immediate release tablets dissolve within 10-15 min, tmax 1-1.5 hr
    FitParameter(
        pid="Ka_abs_met",
        start_value=1.0,
        lower_bound=0.2,
        upper_bound=10,
        unit="1/hr",
    ),
    FitParameter(
        pid="Ka_dis_met",
        start_value=3.0,
        lower_bound=0.3,
        upper_bound=30,
        unit="1/hr",
    ),
    # slow and controlled release: in vitro first order rates of about 0.26
    # and 0.08-0.12 1/hr (Oosterhuis1988, Sandberg1988)
    FitParameter(
        pid="Ka_dis_sr_met",
        start_value=0.25,
        lower_bound=0.05,
        upper_bound=2.0,
        unit="1/hr",
    ),
    FitParameter(
        pid="Ka_dis_cr_met",
        start_value=0.12,
        lower_bound=0.02,
        upper_bound=0.5,
        unit="1/hr",
    ),
    # the controlled release form is absorbed less, relative bioavailability
    # 0.65 (0.42-0.94) (Sandberg1988)
    FitParameter(
        pid="F_cr_met",
        start_value=0.7,
        lower_bound=0.3,
        upper_bound=1.0,
        unit="dimensionless",
    ),
]

#: the pharmacodynamics: the reduction of the exercise heart rate, Mmax 52/min
#: of 148/min and CM50 40 µg/l (0.15 µM, Kirchheiner2004)
parameters_pd: list[FitParameter] = [
    FitParameter(
        pid="HRred_Emax",
        start_value=0.35,
        lower_bound=0.05,
        upper_bound=0.8,
        unit="dimensionless",
    ),
    FitParameter(
        pid="HRred_EC50",
        start_value=1.5e-4,
        lower_bound=5e-6,
        upper_bound=5e-3,
        unit="mM",
    ),
]
