"""Base class of the metoprolol simulation experiments."""

from collections.abc import Iterable, Mapping, Sequence
from typing import ClassVar, NamedTuple

import pandas as pd
from pkpdsim.experiment import PKPDSimulationExperiment
from pkpdsim.impairment import RENAL_COLORS_END_STAGE, RENAL_FUNCTION_GFR
from sbmlsim import Q
from sbmlsim.simulation import Change
from sbmlsim.units import Quantity

from pkdb_models.models.metoprolol import MODEL
from pkdb_models.models.metoprolol.metoprolol_pk import calculate_metoprolol_pk
from pkdb_models.models.metoprolol.models.model_cyp2d6 import ALLELE_ACTIVITIES


class MolecularWeights(NamedTuple):
    """Molecular weights for the conversion of the data and of the doses."""

    met: Quantity
    metoh: Quantity
    mam: Quantity
    #: metoprolol tartrate per metoprolol: (C15H25NO3)2 x C4H6O6, 684.8 g/mole
    met_tartrate: Quantity
    #: metoprolol succinate per metoprolol: (C15H25NO3)2 x C4H6O4, 652.8 g/mole
    met_succinate: Quantity


class MetoprololSimulationExperiment(PKPDSimulationExperiment):
    """Base class of the metoprolol simulation experiments.

    The model doses metoprolol (base): a dose of a salt is converted with
    `dose_base`. The groups of a study are set by changes of the model: the
    application form (`application_changes`), the CYP2D6 genotype or
    phenotype (`genotype_changes`, `cyp2d6_changes`, `metabolizer_changes`),
    the renal function (`renal_map`, `KI__f_renal_function`), the body weight
    (`BW`) and the baseline of the heart rate (`exercise_changes`, `HR`).
    """

    pkpd_model = MODEL
    selections = (
        "time",
        # dosing
        "IVDOSE_met",
        "PODOSE_met",
        "GUTDOSE_met",
        "Ri_met",
        # plasma
        "[Cveplasma_met]",
        "[Cveplasma_metoh]",
        "[Cveplasma_mam]",
        # blood
        "[Cve_met]",
        # urine and feces
        "Aurine_met",
        "Aurine_metoh",
        "Aurine_mam",
        "Afeces_met",
        "KI__METEX",
        "KI__METOHEX",
        "KI__MAMEX",
        # cases
        "BW",
        "KI__f_renal_function",
        "KI__GFR",
        "LI__f_cyp2d6",
        "form_sr",
        "form_cr",
        # pharmacodynamics
        "HR",
        "HReff",
        "HRred",
    )

    label_time = "time"
    unit_time = "hr"
    label_met = "metoprolol"
    unit_met = "µM"
    label_metoh = r"$\alpha$-OH metoprolol" + "\n"
    unit_metoh = "µM"
    label_mam = "metoprolol acid"
    unit_mam = "µM"
    label_excretion = "urinary excretion rate\n"
    unit_excretion = "µmole/min"
    label_urine = "urine"
    unit_urine = "µmole"
    label_hr = "heart rate"
    unit_hr = "1/min"
    label_hrreduction = "HR reduction\n"
    unit_hrreduction = "percent"

    labels: ClassVar[Mapping[str, str]] = {
        "time": label_time,
        "[Cveplasma_met]": "metoprolol plasma",
        "[Cveplasma_metoh]": "alpha-OH metoprolol plasma",
        "[Cveplasma_mam]": "metoprolol acid plasma",
        "[Cve_met]": "metoprolol blood",
        "Aurine_met": "metoprolol urine",
        "Aurine_metoh": "alpha-OH metoprolol urine",
        "Aurine_mam": "metoprolol acid urine",
        "KI__METEX": "metoprolol urinary excretion rate",
        "KI__METOHEX": "alpha-OH metoprolol urinary excretion rate",
        "KI__MAMEX": "metoprolol acid urinary excretion rate",
        "HReff": label_hr,
        "HRred": "HR reduction",
    }
    units: ClassVar[Mapping[str, str]] = {
        "time": unit_time,
        "[Cveplasma_met]": unit_met,
        "[Cveplasma_metoh]": unit_metoh,
        "[Cveplasma_mam]": unit_mam,
        "[Cve_met]": unit_met,
        "Aurine_met": unit_urine,
        "Aurine_metoh": unit_urine,
        "Aurine_mam": unit_urine,
        "KI__METEX": unit_excretion,
        "KI__METOHEX": unit_excretion,
        "KI__MAMEX": unit_excretion,
        "HReff": unit_hr,
        "HRred": "dimensionless",
    }

    colors: ClassVar[dict[str, str]] = {
        # application
        "ir": "black",
        "sr": "tab:red",
        "cr": "tab:blue",
        "solution": "tab:gray",
        # metabolizer
        "um": "tab:red",
        "em": "tab:orange",
        "im": "black",
        "pm": "tab:blue",
        # exercise
        "no": "black",
        "slow": "tab:blue",
        "medium": "tab:orange",
        "fast": "tab:red",
    }

    # ----------- Renal function --------------
    #: the renal function by the classes of the GFR relative to 101 ml/min; a
    #: measured creatinine clearance of X ml/min is `KI__f_renal_function`
    #: X/101
    renal_map = RENAL_FUNCTION_GFR
    renal_colors = RENAL_COLORS_END_STAGE

    # ----------- CYP2D6 --------------
    #: the CYP2D6 activity score of the phenotypes: ultrarapid (um, a gene
    #: duplication and an active allele), extensive (em, two active alleles),
    #: intermediate (im) and poor (pm, no active allele) metabolizers
    cyp2d6_activity_scores: ClassVar[dict[str, float]] = {
        "um": 3.0,
        "em": 2.0,
        "im": 1.0,
        "pm": 0.0,
    }
    metabolizer_types: ClassVar[list[str]] = list(cyp2d6_activity_scores)

    # ----------- Application forms --------------
    #: the switches of the application forms of the model: immediate release
    #: (ir, the default), slow release (sr, e.g. Lopressor SR, Durules) and
    #: controlled release (cr, metoprolol succinate, Zok) tablets. An oral
    #: solution is dosed as `GUTDOSE_met` (no dissolution) with the switches of
    #: the immediate release.
    application_switches: ClassVar[dict[str, dict[str, float]]] = {
        "ir": {"form_sr": 0.0, "form_cr": 0.0},
        "sr": {"form_sr": 1.0, "form_cr": 0.0},
        "cr": {"form_sr": 0.0, "form_cr": 1.0},
        "solution": {"form_sr": 0.0, "form_cr": 0.0},
    }
    application_types: ClassVar[list[str]] = ["ir", "sr", "cr"]

    # ----------- Exercise --------------
    #: the baseline of the heart rate `HR` [1/min] of an exercise (rest, slow,
    #: medium, fast); it is the baseline of the reduction of the heart rate
    #: and does not change the pharmacokinetics
    exercise_heart_rates: ClassVar[dict[str, float]] = {
        "no": 70.0,
        "slow": 90.0,
        "medium": 110.0,
        "fast": 130.0,
    }
    exercise_types: ClassVar[list[str]] = list(exercise_heart_rates)

    # molecular weights of metoprolol, its metabolites and its salts
    Mr: ClassVar[MolecularWeights] = MolecularWeights(
        met=Q(267.36394, "g/mole"),
        metoh=Q(283.36334, "g/mole"),
        mam=Q(267.32, "g/mole"),
        met_tartrate=Q(684.8 / 2, "g/mole"),
        met_succinate=Q(652.8 / 2, "g/mole"),
    )

    def dose_base(self, dose: float, salt: str) -> Quantity:
        """Get the dose of metoprolol (base) of a dose of a salt.

        Args:
            dose: the dose of the salt [mg], e.g. 100 for 100 mg metoprolol
                tartrate (78.1 mg base) or 95 for 95 mg metoprolol succinate
                (77.8 mg base).
            salt: `tartrate`, `succinate` or `base`.

        Raises:
            ValueError: for an unknown salt.
        """
        if salt == "base":
            return Q(dose, "mg")
        if salt not in ("tartrate", "succinate"):
            raise ValueError(f"salt '{salt}' not in ['tartrate', 'succinate', 'base'].")
        mr_salt: Quantity = getattr(self.Mr, f"met_{salt}")
        return Q(dose, "mg") * (self.Mr.met / mr_salt).to("dimensionless").magnitude

    @staticmethod
    def oral_doses(times: Sequence[float | Quantity], dose: Quantity) -> Change:
        """Get the repeated oral doses of metoprolol, which add to `PODOSE_met`.

        The undissolved rest of the earlier doses (`PODOSE_met`) is kept, which
        matters for the slow and controlled release forms. The first dose is a
        change before the initialization (`PODOSE_met` in `preinit_changes`).

        Args:
            times: the times of the doses after the first one, in the time unit
                of the simulation or quantities.
            dose: the dose of metoprolol (base).
        """
        mg = dose.to("mg").magnitude
        return Change(list(times), {"PODOSE_met": f"PODOSE_met + {mg}"})

    @staticmethod
    def iv_infusion(
        dose: Quantity, duration: Quantity | None = None, start: Quantity | None = None
    ) -> tuple[dict[str, Quantity], list[Change]]:
        """Get an intravenous infusion of metoprolol at a constant rate.

        Args:
            dose: the dose of metoprolol (base).
            duration: the duration of the infusion, 10 min by default
                (Johnsson1975, Regardh1974).
            start: the start of the infusion, 0 by default.

        Returns:
            The changes before the initialization (an infusion which starts at
            0) and the changes of the simulation: the rate `Ri_met` at the start
            and 0 at the end of the infusion.
        """
        duration = Q(10, "min") if duration is None else duration
        start = Q(0, "min") if start is None else start
        rate = (dose / duration).to("mg/min")
        stop = Change([start + duration], {"Ri_met": Q(0, "mg/min")})
        if start.magnitude == 0:
            return {"Ri_met": rate}, [stop]
        return {}, [Change([start], {"Ri_met": rate}), stop]

    def cyp2d6_changes(self, activity: float) -> dict[str, Quantity]:
        """Get the changes of a CYP2D6 activity score (2 for *1/*1).

        Both alleles take the index -1, the custom activity `LI__cyp2d6_ac`.
        """
        return {
            "LI__cyp2d6_allele1": Q(-1, "dimensionless"),
            "LI__cyp2d6_allele2": Q(-1, "dimensionless"),
            "LI__cyp2d6_ac": Q(activity, "dimensionless"),
        }

    def genotype_changes(self, allele1: str, allele2: str) -> dict[str, Quantity]:
        """Get the changes of a CYP2D6 diplotype, e.g. `*1`, `*10`.

        The activity of an allele is its activity score in `ALLELE_ACTIVITIES`
        of the CYP2D6 model (*10 0.25, *41 0.5, *4 0, *1x2 2).

        Raises:
            ValueError: for an unknown allele.
        """
        alleles = list(ALLELE_ACTIVITIES)
        for allele in (allele1, allele2):
            if allele not in alleles:
                raise ValueError(f"CYP2D6 allele '{allele}' is not in the model.")
        return {
            "LI__cyp2d6_allele1": Q(alleles.index(allele1), "dimensionless"),
            "LI__cyp2d6_allele2": Q(alleles.index(allele2), "dimensionless"),
        }

    def metabolizer_changes(self, metabolizer: str) -> dict[str, Quantity]:
        """Get the changes of a CYP2D6 phenotype, see `cyp2d6_activity_scores`.

        Raises:
            ValueError: for an unknown phenotype.
        """
        if metabolizer not in self.cyp2d6_activity_scores:
            raise ValueError(
                f"metabolizer type '{metabolizer}' not in supported "
                f"types {self.metabolizer_types}."
            )
        return self.cyp2d6_changes(self.cyp2d6_activity_scores[metabolizer])

    def application_changes(self, application: str) -> dict[str, Quantity]:
        """Get the changes of an application form, see `application_switches`.

        Raises:
            ValueError: for an unknown application form.
        """
        if application not in self.application_switches:
            raise ValueError(
                f"application type '{application}' not in supported "
                f"types {list(self.application_switches)}."
            )
        return {
            key: Q(value, "dimensionless")
            for key, value in self.application_switches[application].items()
        }

    def exercise_changes(self, exercise: str) -> dict[str, Quantity]:
        """Get the baseline of the heart rate of an exercise, see `exercise_heart_rates`.

        Raises:
            ValueError: for an unknown exercise.
        """
        if exercise not in self.exercise_heart_rates:
            raise ValueError(
                f"exercise type '{exercise}' not in supported "
                f"types {self.exercise_types}."
            )
        return {"HR": Q(self.exercise_heart_rates[exercise], "1/min")}

    # --- Pharmacokinetic parameters ---
    def calculate_metoprolol_pk(
        self, scans: Iterable[str] | None = None
    ) -> dict[str, pd.DataFrame]:
        """Calculate the pharmacokinetic parameters of the scans.

        Args:
            scans: keys of the simulations, all simulations by default.

        Returns:
            The parameters of every scan by simulation key, per draw of the
            fitted parameters in a run over them (`uncertainty`).
        """
        keys = self._simulations if scans is None else scans
        across = None if self.uncertainty is None else self.uncertainty.id
        return {
            key: calculate_metoprolol_pk(
                experiment=self, res=self.results[f"task_{key}"], across=across
            )
            for key in keys
        }
