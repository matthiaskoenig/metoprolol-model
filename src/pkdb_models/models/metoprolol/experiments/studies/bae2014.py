"""Simulation experiment of the study Bae2014."""

from typing import ClassVar, override

from pkpdsim.metadata import (
    ApplicationForm,
    Dosing,
    Fasting,
    Health,
    Phenotype,
    PKPDData,
    PKPDMappingMetaData,
    Route,
    Tissue,
)
from sbmlsim.data import DataSet
from sbmlsim.fit import FitData, FitMapping
from sbmlsim.plot import Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.metoprolol import MODEL
from pkdb_models.models.metoprolol.experiments.base_experiment import (
    MetoprololSimulationExperiment,
)
from pkdb_models.models.metoprolol.experiments.figure_templates import (
    EXCRETION_LINESTYLES,
    fig_metoprolol,
)


class Bae2014(MetoprololSimulationExperiment):
    """Simulation experiment of Bae2014.

    Seven healthy Korean men, CYP2D6*1/*1 (n=4) and *10/*10 (n=3), a single
    oral dose of 100 mg metoprolol tartrate (Betaloc, conventional immediate
    release tablets); fasting, body weight and age are not reported. Fig 3:
    metoprolol and alpha-hydroxymetoprolol in plasma, mean and SD (the bars
    at the peaks equal the SD of Cmax of Table 4).
    """

    #: the CYP2D6 diplotypes of the groups
    genotypes: ClassVar[dict[str, tuple[str, str]]] = {
        "11": ("*1", "*1"),
        "1010": ("*10", "*10"),
    }
    #: the group of the data per diplotype
    data_groups: ClassVar[dict[str, str]] = {"11": "genotype1", "1010": "genotype10"}
    #: the CYP2D6 phenotype by the activity score (*1/*1 2, *10/*10 0.5)
    phenotypes: ClassVar[dict[str, Phenotype]] = {
        "11": Phenotype.CYP2D6_EM,
        "1010": Phenotype.CYP2D6_IM,
    }
    genotype_labels: ClassVar[dict[str, str]] = {"11": "*1/*1", "1010": "*10/*10"}
    genotype_colors: ClassVar[dict[str, str]] = {"11": "black", "1010": "tab:blue"}
    genotype_markers: ClassVar[dict[str, str]] = {"11": "s", "1010": "o"}

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig3"]:
            dframes = self.load_dataframes_by_substance(fig_id)
            for substance, df in dframes.items():
                dset = DataSet.from_df(df, self.ureg)
                if substance == "metoprolol":
                    dset.unit_conversion("mean", 1 / self.Mr.met)
                elif substance == "alpha-hydroxymetoprolol":
                    dset.unit_conversion("mean", 1 / self.Mr.metoh)
                for group_name in df.group.unique():
                    dsets[self.to_sid(f"{fig_id.lower()}_{substance}_{group_name}")] = (
                        dset[dset.group == group_name]
                    )
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        # a single oral dose of 100 mg metoprolol tartrate (78.1 mg metoprolol)
        # as immediate release tablets per CYP2D6 diplotype
        return {
            self.to_sid(f"met_po100_{genotype}"): Simulation(
                time_unit="hr",
                end=24,
                preinit_changes={
                    **self.default_changes(),
                    **self.application_changes("ir"),
                    **self.genotype_changes(*alleles),
                    "PODOSE_met": self.dose_base(100, "tartrate"),
                },
            )
            for genotype, alleles in self.genotypes.items()
        }

    def dataset_id(self, substance: str, genotype: str) -> str:
        """Get the key of the dataset of a substance and a diplotype."""
        return self.to_sid(f"fig3_{substance}_{self.data_groups[genotype]}")

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for sid, substance in [
            ("met", "metoprolol"),
            ("metoh", "alpha-hydroxymetoprolol"),
        ]:
            for genotype in self.genotypes:
                mappings[self.to_sid(f"fm_{sid}_{genotype}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.dataset_id(substance, genotype),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_met_po100_{genotype}"),
                        xid="time",
                        yid=f"[Cveplasma_{sid}]",
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.IMMEDIATE_RELEASE,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        phenotype=self.phenotypes[genotype],
                        fasting=Fasting.NR,
                        data=PKPDData.PK,
                    ),
                )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig, plots = fig_metoprolol(
            self, fig_id="Fig1", name=f"{self.sid} (100 mg metoprolol tartrate PO)"
        )

        for genotype in self.genotypes:
            label = self.genotype_labels[genotype]
            color = self.genotype_colors[genotype]
            task_id = self.to_sid(f"task_met_po100_{genotype}")

            # data
            for k, substance in enumerate(["metoprolol", "alpha-hydroxymetoprolol"]):
                plots[k].add_data(
                    dataset=self.dataset_id(substance, genotype),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    label=label,
                    color=color,
                    marker=self.genotype_markers[genotype],
                )

            # simulations
            for k, sid in enumerate(["met", "metoh", "mam"]):
                plots[k].add_data(
                    task=task_id,
                    xid="time",
                    yid=f"[Cveplasma_{sid}]",
                    label=label,
                    color=color,
                )
                plots[3].add_data(
                    task=task_id,
                    xid="time",
                    yid=f"KI__{sid.upper()}EX",
                    label=f"{label} {sid}",
                    color=color,
                    linestyle=EXCRETION_LINESTYLES[sid],
                )
            plots[4].add_data(
                task=task_id, xid="time", yid="HReff", label=label, color=color
            )
            plots[5].add_data(
                task=task_id, xid="time", yid="HRred", label=label, color=color
            )

        return {"fig1": fig}


if __name__ == "__main__":
    MODEL.run_experiments(Bae2014, output_dir="test")
