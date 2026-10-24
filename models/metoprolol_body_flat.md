# Metoprolol body model

Model `metoprolol_body`, SBML Level 3 Version 1, read from metoprolol\_body\_flat.xml, written by sbmlode 0.3.0.

Metoprolol whole-body model

Whole-body model of metoprolol and its metabolites alpha-hydroxymetoprolol and metoprolol acid with the blood circulation, the tissue distribution, the oral and intravenous dosing, the submodels of the liver (metabolism by CYP2D6 and other enzymes) and of the kidneys (renal excretion), and the reduction of the exercise heart rate by metoprolol.

The circulating species are whole blood concentrations: the blood flows transport the blood concentrations, the plasma concentration is the blood concentration over the blood to plasma ratio BP\_&lt;sid&gt; (metoprolol 1.2, Regardh1974; the metabolites 1). The tissues exchange with the blood by the flow ftissue\_&lt;sid&gt; towards the tissue/blood partition coefficient Kp\_&lt;sid&gt;, which sets the volume of distribution (metoprolol about 4.5 l/kg of plasma, Regardh1974).

The content of this model has been carefully created in a manual research effort.

Terms of use

Copyright © 2026 Matthias König.

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

Redistribution and use of any part of this model, with or without modification, are permitted provided that the following conditions are met:

Redistributions of this SBML file must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions in a different form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

This model is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Units

| Time | Substance | Extent | Volume | Area | Length |
| --- | --- | --- | --- | --- | --- |
| min | mmol | mmol | l | m<sup>2</sup> | m |

## Compartments

| Symbol | Id | Name | Size | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $\mathrm{Vgu}$ | `Vgu` | gastrointestinal tract |  | l |  |
| $\mathrm{Vhe}$ | `Vhe` | heart |  | l |  |
| $\mathrm{Vki}$ | `Vki` | kidney |  | l |  |
| $\mathrm{Vli}$ | `Vli` | liver |  | l |  |
| $\mathrm{Vlu}$ | `Vlu` | lung |  | l |  |
| $\mathrm{Vre}$ | `Vre` | rest |  | l |  |
| $\mathrm{Var}$ | `Var` | arterial blood |  | l |  |
| $\mathrm{Vve}$ | `Vve` | venous blood |  | l |  |
| $\mathrm{Vpo}$ | `Vpo` | portal vein |  | l |  |
| $\mathrm{Vhv}$ | `Vhv` | hepatic vein |  | l |  |
| $\mathrm{Vurine}$ | `Vurine` | urine | $1$ | l | ✓ |
| $\mathrm{Vfeces}$ | `Vfeces` | feces | $1$ | l | ✓ |
| $\mathrm{Vgu}_{\mathrm{tissue}}$ | `Vgu_tissue` | gastrointestinal tract tissue |  | l |  |
| $\mathrm{Vgu}_{\mathrm{blood}}$ | `Vgu_blood` | gastrointestinal tract blood |  | l |  |
| $\mathrm{Vhe}_{\mathrm{tissue}}$ | `Vhe_tissue` | heart tissue |  | l |  |
| $\mathrm{Vhe}_{\mathrm{blood}}$ | `Vhe_blood` | heart blood |  | l |  |
| $\mathrm{Vki}_{\mathrm{tissue}}$ | `Vki_tissue` | kidney tissue |  | l |  |
| $\mathrm{Vki}_{\mathrm{blood}}$ | `Vki_blood` | kidney blood |  | l |  |
| $\mathrm{Vli}_{\mathrm{tissue}}$ | `Vli_tissue` | liver tissue |  | l |  |
| $\mathrm{Vli}_{\mathrm{blood}}$ | `Vli_blood` | liver blood |  | l |  |
| $\mathrm{Vlu}_{\mathrm{tissue}}$ | `Vlu_tissue` | lung tissue |  | l |  |
| $\mathrm{Vlu}_{\mathrm{blood}}$ | `Vlu_blood` | lung blood |  | l |  |
| $\mathrm{Vre}_{\mathrm{tissue}}$ | `Vre_tissue` | rest tissue |  | l |  |
| $\mathrm{Vre}_{\mathrm{blood}}$ | `Vre_blood` | rest blood |  | l |  |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{Cgu}_{\mathrm{blood\_met}}$ | `Cgu_blood_met` | metoprolol (gastrointestinal tract blood) | $\mathrm{Vgu}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Che}_{\mathrm{blood\_met}}$ | `Che_blood_met` | metoprolol (heart blood) | $\mathrm{Vhe}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cki}_{\mathrm{blood\_met}}$ | `Cki_blood_met` | metoprolol (kidney blood) | $\mathrm{Vki}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cli}_{\mathrm{blood\_met}}$ | `Cli_blood_met` | metoprolol (liver blood) | $\mathrm{Vli}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{blood\_met}}$ | `Clu_blood_met` | metoprolol (lung blood) | $\mathrm{Vlu}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{blood\_met}}$ | `Cre_blood_met` | metoprolol (rest blood) | $\mathrm{Vre}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{met}}$ | `Car_met` | metoprolol (arterial blood) | $\mathrm{Var}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{met}}$ | `Cve_met` | metoprolol (venous blood) | $\mathrm{Vve}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{met}}$ | `Cpo_met` | metoprolol (portal vein) | $\mathrm{Vpo}$ | $0$ | mmol/l | concentration |
| $\mathrm{Chv}_{\mathrm{met}}$ | `Chv_met` | metoprolol (hepatic vein) | $\mathrm{Vhv}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{met}}$ | `Cgu_met` | metoprolol (gastrointestinal tract tissue) | $\mathrm{Vgu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Che}_{\mathrm{met}}$ | `Che_met` | metoprolol (heart tissue) | $\mathrm{Vhe}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cki}_{\mathrm{met}}$ | `Cki_met` | metoprolol (kidney tissue) | $\mathrm{Vki}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{met}}$ | `Clu_met` | metoprolol (lung tissue) | $\mathrm{Vlu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{met}}$ | `Cre_met` | metoprolol (rest tissue) | $\mathrm{Vre}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{met}}$ | `Aurine_met` | metoprolol (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{Cgu}_{\mathrm{blood\_metoh}}$ | `Cgu_blood_metoh` | alpha-hydroxymetoprolol (gastrointestinal tract blood) | $\mathrm{Vgu}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Che}_{\mathrm{blood\_metoh}}$ | `Che_blood_metoh` | alpha-hydroxymetoprolol (heart blood) | $\mathrm{Vhe}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cki}_{\mathrm{blood\_metoh}}$ | `Cki_blood_metoh` | alpha-hydroxymetoprolol (kidney blood) | $\mathrm{Vki}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cli}_{\mathrm{blood\_metoh}}$ | `Cli_blood_metoh` | alpha-hydroxymetoprolol (liver blood) | $\mathrm{Vli}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{blood\_metoh}}$ | `Clu_blood_metoh` | alpha-hydroxymetoprolol (lung blood) | $\mathrm{Vlu}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{blood\_metoh}}$ | `Cre_blood_metoh` | alpha-hydroxymetoprolol (rest blood) | $\mathrm{Vre}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{metoh}}$ | `Car_metoh` | alpha-hydroxymetoprolol (arterial blood) | $\mathrm{Var}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{metoh}}$ | `Cve_metoh` | alpha-hydroxymetoprolol (venous blood) | $\mathrm{Vve}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{metoh}}$ | `Cpo_metoh` | alpha-hydroxymetoprolol (portal vein) | $\mathrm{Vpo}$ | $0$ | mmol/l | concentration |
| $\mathrm{Chv}_{\mathrm{metoh}}$ | `Chv_metoh` | alpha-hydroxymetoprolol (hepatic vein) | $\mathrm{Vhv}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{metoh}}$ | `Cgu_metoh` | alpha-hydroxymetoprolol (gastrointestinal tract tissue) | $\mathrm{Vgu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Che}_{\mathrm{metoh}}$ | `Che_metoh` | alpha-hydroxymetoprolol (heart tissue) | $\mathrm{Vhe}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cki}_{\mathrm{metoh}}$ | `Cki_metoh` | alpha-hydroxymetoprolol (kidney tissue) | $\mathrm{Vki}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{metoh}}$ | `Clu_metoh` | alpha-hydroxymetoprolol (lung tissue) | $\mathrm{Vlu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{metoh}}$ | `Cre_metoh` | alpha-hydroxymetoprolol (rest tissue) | $\mathrm{Vre}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{metoh}}$ | `Aurine_metoh` | alpha-hydroxymetoprolol (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{Cgu}_{\mathrm{blood\_mam}}$ | `Cgu_blood_mam` | metoprolol acid (gastrointestinal tract blood) | $\mathrm{Vgu}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Che}_{\mathrm{blood\_mam}}$ | `Che_blood_mam` | metoprolol acid (heart blood) | $\mathrm{Vhe}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cki}_{\mathrm{blood\_mam}}$ | `Cki_blood_mam` | metoprolol acid (kidney blood) | $\mathrm{Vki}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cli}_{\mathrm{blood\_mam}}$ | `Cli_blood_mam` | metoprolol acid (liver blood) | $\mathrm{Vli}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{blood\_mam}}$ | `Clu_blood_mam` | metoprolol acid (lung blood) | $\mathrm{Vlu}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{blood\_mam}}$ | `Cre_blood_mam` | metoprolol acid (rest blood) | $\mathrm{Vre}_{\mathrm{blood}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{mam}}$ | `Car_mam` | metoprolol acid (arterial blood) | $\mathrm{Var}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{mam}}$ | `Cve_mam` | metoprolol acid (venous blood) | $\mathrm{Vve}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{mam}}$ | `Cpo_mam` | metoprolol acid (portal vein) | $\mathrm{Vpo}$ | $0$ | mmol/l | concentration |
| $\mathrm{Chv}_{\mathrm{mam}}$ | `Chv_mam` | metoprolol acid (hepatic vein) | $\mathrm{Vhv}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{mam}}$ | `Cgu_mam` | metoprolol acid (gastrointestinal tract tissue) | $\mathrm{Vgu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Che}_{\mathrm{mam}}$ | `Che_mam` | metoprolol acid (heart tissue) | $\mathrm{Vhe}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cki}_{\mathrm{mam}}$ | `Cki_mam` | metoprolol acid (kidney tissue) | $\mathrm{Vki}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{mam}}$ | `Clu_mam` | metoprolol acid (lung tissue) | $\mathrm{Vlu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{mam}}$ | `Cre_mam` | metoprolol acid (rest tissue) | $\mathrm{Vre}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{mam}}$ | `Aurine_mam` | metoprolol acid (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{met}}$ | `Afeces_met` | metoprolol (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{Cveplasma}_{\mathrm{met}}$ | `Cveplasma_met` | metoprolol (venous plasma) | $\mathrm{Vve}$ |  | mmol/l | concentration |
| $\mathrm{Cveplasma}_{\mathrm{metoh}}$ | `Cveplasma_metoh` | alpha-hydroxymetoprolol (venous plasma) | $\mathrm{Vve}$ |  | mmol/l | concentration |
| $\mathrm{Cveplasma}_{\mathrm{mam}}$ | `Cveplasma_mam` | metoprolol acid (venous plasma) | $\mathrm{Vve}$ |  | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_met}}$ | `LI__met` | metoprolol (liver) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_metoh}}$ | `LI__metoh` | alpha-hydroxymetoprolol (liver) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_mam}}$ | `LI__mam` | metoprolol acid (liver) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $\mathrm{BW}$ | `BW` | body weight \[kg\] | $75$ | kg | ✓ |
| $\mathrm{BW}_{\mathrm{ref}}$ | `BW_ref` | reference body weight \[kg\] | $75$ | kg | ✓ |
| $\mathrm{HEIGHT}$ | `HEIGHT` | height \[cm\] | $170$ | cm | ✓ |
| $\mathrm{BSA}$ | `BSA` | body surface area \[m^2\] |  | m<sup>2</sup> |  |
| $\mathrm{COBW}$ | `COBW` | cardiac output per bodyweight \[ml/s/kg\] | $1.548$ | ml/s/kg | ✓ |
| $\mathrm{CO}$ | `CO` | cardiac output \[ml/s\] |  | ml/s |  |
| $\mathrm{QC}$ | `QC` | cardiac output \[L/min\] |  | l/min |  |
| $\mathrm{Fblood}$ | `Fblood` | blood fraction of organ volume | $0.02$ | \- | ✓ |
| $\mathrm{FVgu}$ | `FVgu` | gastrointestinal tract fractional tissue volume | $0.0297$ | l/kg | ✓ |
| $\mathrm{FVhe}$ | `FVhe` | heart fractional tissue volume | $0.0047$ | l/kg | ✓ |
| $\mathrm{FVki}$ | `FVki` | kidney fractional tissue volume | $0.0044$ | l/kg | ✓ |
| $\mathrm{FVli}$ | `FVli` | liver fractional tissue volume | $0.021$ | l/kg | ✓ |
| $\mathrm{FVlu}$ | `FVlu` | lung fractional tissue volume | $0.0076$ | l/kg | ✓ |
| $\mathrm{FVre}$ | `FVre` | rest of body fractional tissue volume |  | l/kg |  |
| $\mathrm{FVve}$ | `FVve` | venous fractional tissue volume | $0.0514$ | l/kg | ✓ |
| $\mathrm{FVar}$ | `FVar` | arterial fractional tissue volume | $0.0257$ | l/kg | ✓ |
| $\mathrm{FVpo}$ | `FVpo` | portal fractional tissue volume | $0.001$ | l/kg | ✓ |
| $\mathrm{FVhv}$ | `FVhv` | hepatic venous fractional tissue volume | $0.001$ | l/kg | ✓ |
| $\mathrm{FQgu}$ | `FQgu` | gastrointestinal tract fractional tissue blood flow | $0.18$ | \- | ✓ |
| $\mathrm{FQhe}$ | `FQhe` | heart fractional tissue blood flow | $0.04$ | \- | ✓ |
| $\mathrm{FQki}$ | `FQki` | kidney fractional tissue blood flow | $0.19$ | \- | ✓ |
| $\mathrm{FQh}$ | `FQh` | hepatic (venous side) fractional tissue blood flow | $0.215$ | \- | ✓ |
| $\mathrm{FQlu}$ | `FQlu` | lung fractional tissue blood flow | $1$ | \- | ✓ |
| $\mathrm{FQre}$ | `FQre` | rest of body fractional tissue blood flow |  | \- |  |
| $f_{\mathrm{GFR\_Qki}}$ | `f_GFR_Qki` | relationship GFR and Qki | $76.3105006271061$ | ml/l | ✓ |
| $\mathrm{GFR}_{\mathrm{base}}$ | `GFR_base` | glomerular filtration rate (healthy) |  | ml/min |  |
| $\mathrm{Mr}_{\mathrm{met}}$ | `Mr_met` | molecular weight met \[g/mole\] | $267.36394$ | g/mol | ✓ |
| $\mathrm{ftissue}_{\mathrm{met}}$ | `ftissue_met` | tissue distribution met | $45.7990376734909$ | l/min | ✓ |
| $\mathrm{Kp}_{\mathrm{met}}$ | `Kp_met` | tissue/blood partition coefficient met | $2.77928372755195$ | \- | ✓ |
| $\mathrm{BP}_{\mathrm{met}}$ | `BP_met` | blood to plasma ratio met | $1.2$ | \- | ✓ |
| $\mathrm{fup}_{\mathrm{met}}$ | `fup_met` | fraction unbound in plasma met | $0.88$ | \- | ✓ |
| $\mathrm{Mr}_{\mathrm{metoh}}$ | `Mr_metoh` | molecular weight metoh \[g/mole\] | $283.36334$ | g/mol | ✓ |
| $\mathrm{ftissue}_{\mathrm{metoh}}$ | `ftissue_metoh` | tissue distribution metoh | $1$ | l/min | ✓ |
| $\mathrm{Kp}_{\mathrm{metoh}}$ | `Kp_metoh` | tissue/blood partition coefficient metoh | $1.76572892659072$ | \- | ✓ |
| $\mathrm{BP}_{\mathrm{metoh}}$ | `BP_metoh` | blood to plasma ratio metoh | $1$ | \- | ✓ |
| $\mathrm{Mr}_{\mathrm{mam}}$ | `Mr_mam` | molecular weight mam \[g/mole\] | $267.32$ | g/mol | ✓ |
| $\mathrm{ftissue}_{\mathrm{mam}}$ | `ftissue_mam` | tissue distribution mam | $1$ | l/min | ✓ |
| $\mathrm{Kp}_{\mathrm{mam}}$ | `Kp_mam` | tissue/blood partition coefficient mam | $1$ | \- | ✓ |
| $\mathrm{BP}_{\mathrm{mam}}$ | `BP_mam` | blood to plasma ratio mam | $1$ | \- | ✓ |
| $\mathrm{IVDOSE}_{\mathrm{met}}$ | `IVDOSE_met` | IV bolus dose metoprolol \[mg\] | $0$ | mg |  |
| $\mathrm{ti}_{\mathrm{met}}$ | `ti_met` | injection time metoprolol \[s\] | $10$ | s | ✓ |
| $\mathrm{Ki}_{\mathrm{met}}$ | `Ki_met` | Ki \[1/min\] injection metoprolol |  | 1/min |  |
| $\mathrm{Ri}_{\mathrm{met}}$ | `Ri_met` | Ri \[mg/min\] rate of infusion metoprolol | $0$ | mg/min |  |
| $\mathrm{PODOSE}_{\mathrm{met}}$ | `PODOSE_met` | oral dose metoprolol \[mg\] | $0$ | mg |  |
| $\mathrm{GUTDOSE}_{\mathrm{met}}$ | `GUTDOSE_met` | dose dissolved in gut metoprolol \[mg\] | $0$ | mg |  |
| $\mathrm{Ka}_{\mathrm{dis\_met}}$ | `Ka_dis_met` | dissolution metoprolol, immediate release \[1/hr\] | $2.52589996541947$ | 1/hr | ✓ |
| $\mathrm{Ka}_{\mathrm{dis\_sr\_met}}$ | `Ka_dis_sr_met` | dissolution metoprolol, slow release \[1/hr\] | $0.257836823158639$ | 1/hr | ✓ |
| $\mathrm{Ka}_{\mathrm{dis\_cr\_met}}$ | `Ka_dis_cr_met` | dissolution metoprolol, controlled release \[1/hr\] | $0.0700335069680276$ | 1/hr | ✓ |
| $\mathrm{form}_{\mathrm{sr}}$ | `form_sr` | slow release form (0 or 1) | $0$ | \- | ✓ |
| $\mathrm{form}_{\mathrm{cr}}$ | `form_cr` | controlled release form (0 or 1) | $0$ | \- | ✓ |
| $\mathrm{Ka}_{\mathrm{abs\_met}}$ | `Ka_abs_met` | absorption metoprolol \[1/hr\] | $1.00037907679797$ | 1/hr | ✓ |
| $F_{\mathrm{met}}$ | `F_met` | fraction absorbed metoprolol | $1$ | \- | ✓ |
| $F_{\mathrm{cr\_met}}$ | `F_cr_met` | fraction absorbed metoprolol, controlled release | $1$ | \- | ✓ |
| $\mathrm{HR}$ | `HR` | heart rate without metoprolol \[1/min\] | $70$ | 1/min | ✓ |
| $\mathrm{HRred}_{\mathrm{Emax}}$ | `HRred_Emax` | maximal relative reduction of the heart rate | $0.285016435425259$ | \- | ✓ |
| $\mathrm{HRred}_{\mathrm{EC50}}$ | `HRred_EC50` | metoprolol plasma concentration of the half-maximal reduction | $0.000121648311940819$ | mmol/l | ✓ |
| $\mathrm{HRred}_{\mathrm{n}}$ | `HRred_n` | Hill coefficient of the reduction of the heart rate | $1$ | \- | ✓ |
| $\mathrm{Qgu}$ | `Qgu` | gut blood flow |  | l/min |  |
| $\mathrm{Qhe}$ | `Qhe` | heart blood flow |  | l/min |  |
| $\mathrm{Qki}$ | `Qki` | kidney blood flow |  | l/min |  |
| $\mathrm{Qh}$ | `Qh` | hepatic (venous side) blood flow |  | l/min |  |
| $\mathrm{Qha}$ | `Qha` | hepatic artery blood flow |  | l/min |  |
| $\mathrm{Qlu}$ | `Qlu` | lung blood flow |  | l/min |  |
| $\mathrm{Qre}$ | `Qre` | rest of body blood flow |  | l/min |  |
| $\mathrm{Qpo}$ | `Qpo` | portal blood flow |  | l/min |  |
| $\mathrm{Ka}_{\mathrm{dis\_form\_met}}$ | `Ka_dis_form_met` | dissolution metoprolol of the application form |  | 1/hr |  |
| $F_{\mathrm{form\_met}}$ | `F_form_met` | fraction absorbed metoprolol of the application form |  | \- |  |
| $\mathrm{dissolution}_{\mathrm{met}}$ | `dissolution_met` | dissolution metoprolol |  | mmol/min |  |
| $\mathrm{HRred}$ | `HRred` | relative reduction of the heart rate |  | \- |  |
| $\mathrm{HReff}$ | `HReff` | heart rate with metoprolol |  | 1/min |  |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a0}}$ | `LI__cyp2d6_a0` | \*1 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a1}}$ | `LI__cyp2d6_a1` | \*10 activity | $0.25$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a2}}$ | `LI__cyp2d6_a2` | \*100 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a3}}$ | `LI__cyp2d6_a3` | \*101 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a4}}$ | `LI__cyp2d6_a4` | \*10x2 activity | $0.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a5}}$ | `LI__cyp2d6_a5` | \*11 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a6}}$ | `LI__cyp2d6_a6` | \*114 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a7}}$ | `LI__cyp2d6_a7` | \*12 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a8}}$ | `LI__cyp2d6_a8` | \*120 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a9}}$ | `LI__cyp2d6_a9` | \*124 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a10}}$ | `LI__cyp2d6_a10` | \*129 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a11}}$ | `LI__cyp2d6_a11` | \*13 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a12}}$ | `LI__cyp2d6_a12` | \*14 activity | $0.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a13}}$ | `LI__cyp2d6_a13` | \*15 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a14}}$ | `LI__cyp2d6_a14` | \*17 activity | $0.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a15}}$ | `LI__cyp2d6_a15` | \*17x2 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a16}}$ | `LI__cyp2d6_a16` | \*18 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a17}}$ | `LI__cyp2d6_a17` | \*19 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a18}}$ | `LI__cyp2d6_a18` | \*1x2 activity | $2$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a19}}$ | `LI__cyp2d6_a19` | \*1x3 activity | $3$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a20}}$ | `LI__cyp2d6_a20` | \*1x4 activity | $4$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a21}}$ | `LI__cyp2d6_a21` | \*1x5 activity | $5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a22}}$ | `LI__cyp2d6_a22` | \*1x6 activity | $6$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a23}}$ | `LI__cyp2d6_a23` | \*2 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a24}}$ | `LI__cyp2d6_a24` | \*20 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a25}}$ | `LI__cyp2d6_a25` | \*21 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a26}}$ | `LI__cyp2d6_a26` | \*27 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a27}}$ | `LI__cyp2d6_a27` | \*29 activity | $0.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a28}}$ | `LI__cyp2d6_a28` | \*29x2 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a29}}$ | `LI__cyp2d6_a29` | \*2x2 activity | $2$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a30}}$ | `LI__cyp2d6_a30` | \*2x3 activity | $3$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a31}}$ | `LI__cyp2d6_a31` | \*2x4 activity | $4$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a32}}$ | `LI__cyp2d6_a32` | \*2x5 activity | $5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a33}}$ | `LI__cyp2d6_a33` | \*2x6 activity | $6$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a34}}$ | `LI__cyp2d6_a34` | \*3 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a35}}$ | `LI__cyp2d6_a35` | \*31 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a36}}$ | `LI__cyp2d6_a36` | \*33 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a37}}$ | `LI__cyp2d6_a37` | \*34 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a38}}$ | `LI__cyp2d6_a38` | \*35 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a39}}$ | `LI__cyp2d6_a39` | \*35x2 activity | $2$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a40}}$ | `LI__cyp2d6_a40` | \*36 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a41}}$ | `LI__cyp2d6_a41` | \*36x2 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a42}}$ | `LI__cyp2d6_a42` | \*38 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a43}}$ | `LI__cyp2d6_a43` | \*39 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a44}}$ | `LI__cyp2d6_a44` | \*3x2 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a45}}$ | `LI__cyp2d6_a45` | \*4 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a46}}$ | `LI__cyp2d6_a46` | \*40 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a47}}$ | `LI__cyp2d6_a47` | \*41 activity | $0.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a48}}$ | `LI__cyp2d6_a48` | \*41x2 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a49}}$ | `LI__cyp2d6_a49` | \*41x3 activity | $1.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a50}}$ | `LI__cyp2d6_a50` | \*42 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a51}}$ | `LI__cyp2d6_a51` | \*44 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a52}}$ | `LI__cyp2d6_a52` | \*45 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a53}}$ | `LI__cyp2d6_a53` | \*45x2 activity | $2$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a54}}$ | `LI__cyp2d6_a54` | \*46 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a55}}$ | `LI__cyp2d6_a55` | \*47 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a56}}$ | `LI__cyp2d6_a56` | \*48 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a57}}$ | `LI__cyp2d6_a57` | \*49 activity | $0.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a58}}$ | `LI__cyp2d6_a58` | \*4x2 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a59}}$ | `LI__cyp2d6_a59` | \*4x3 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a60}}$ | `LI__cyp2d6_a60` | \*4x4 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a61}}$ | `LI__cyp2d6_a61` | \*4x5 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a62}}$ | `LI__cyp2d6_a62` | \*5 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a63}}$ | `LI__cyp2d6_a63` | \*50 activity | $0.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a64}}$ | `LI__cyp2d6_a64` | \*51 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a65}}$ | `LI__cyp2d6_a65` | \*53 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a66}}$ | `LI__cyp2d6_a66` | \*54 activity | $0.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a67}}$ | `LI__cyp2d6_a67` | \*55 activity | $0.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a68}}$ | `LI__cyp2d6_a68` | \*56 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a69}}$ | `LI__cyp2d6_a69` | \*57 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a70}}$ | `LI__cyp2d6_a70` | \*59 activity | $0.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a71}}$ | `LI__cyp2d6_a71` | \*6 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a72}}$ | `LI__cyp2d6_a72` | \*60 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a73}}$ | `LI__cyp2d6_a73` | \*62 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a74}}$ | `LI__cyp2d6_a74` | \*68 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a75}}$ | `LI__cyp2d6_a75` | \*69 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a76}}$ | `LI__cyp2d6_a76` | \*6x2 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a77}}$ | `LI__cyp2d6_a77` | \*7 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a78}}$ | `LI__cyp2d6_a78` | \*8 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a79}}$ | `LI__cyp2d6_a79` | \*81 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a80}}$ | `LI__cyp2d6_a80` | \*9 activity | $0.5$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a81}}$ | `LI__cyp2d6_a81` | \*92 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a82}}$ | `LI__cyp2d6_a82` | \*96 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a83}}$ | `LI__cyp2d6_a83` | \*99 activity | $0$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_a84}}$ | `LI__cyp2d6_a84` | \*9x2 activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_ac}}$ | `LI__cyp2d6_ac` | custom allele activity | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}}$ | `LI__cyp2d6_allele1` | allele 1 | $0$ | \- |  |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}}$ | `LI__cyp2d6_allele2` | allele 2 | $0$ | \- |  |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_activity1}}$ | `LI__cyp2d6_activity1` | activity of allele 1 |  | \- |  |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_activity2}}$ | `LI__cyp2d6_activity2` | activity of allele 2 |  | \- |  |
| $\mathrm{LI}_{\mathrm{\_f\_cyp2d6}}$ | `LI__f_cyp2d6` | CYP2D6 activity relative to \*1/\*1 |  | \- |  |
| $\mathrm{LI}_{\mathrm{\_CYP2D6\_Km\_met}}$ | `LI__CYP2D6_Km_met` | Km of metoprolol for CYP2D6 | $0.015$ | mmol/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_METOH\_Vmax}}$ | `LI__METOH_Vmax` | Vmax of the alpha-hydroxylation (CYP2D6, \*1/\*1) | $0.00230494292103704$ | mmol/min/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_ODM2D6\_Vmax}}$ | `LI__ODM2D6_Vmax` | Vmax of the O-demethylation by CYP2D6 (\*1/\*1) | $0.012600231875494$ | mmol/min/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_ODM\_Vmax}}$ | `LI__ODM_Vmax` | Vmax of the O-demethylation by other enzymes than CYP2D6 | $0.00158382422456946$ | mmol/min/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_ODM\_Km\_met}}$ | `LI__ODM_Km_met` | Km of metoprolol for the O-demethylation by other enzymes | $0.015$ | mmol/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_METIM\_k}}$ | `LI__METIM_k` | rate of the metoprolol exchange of the liver | $100$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_METOHEX\_k}}$ | `LI__METOHEX_k` | rate of the alpha-hydroxymetoprolol export | $100$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_MAMEX\_k}}$ | `LI__MAMEX_k` | rate of the metoprolol acid export | $100$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2d6\_activity}}$ | `LI__cyp2d6_activity` | activity of CYP2D6 diplotype |  | \- |  |
| $\mathrm{KI}_{\mathrm{\_f\_renal\_function}}$ | `KI__f_renal_function` | renal function | $1$ | \- | ✓ |
| $\mathrm{KI}_{\mathrm{\_METEX\_f}}$ | `KI__METEX_f` | renal clearance of unbound metoprolol relative to the GFR | $0.815230242660216$ | \- | ✓ |
| $\mathrm{KI}_{\mathrm{\_METOHEX\_f}}$ | `KI__METOHEX_f` | renal clearance of alpha-hydroxymetoprolol relative to the GFR | $6.76476495170102$ | \- | ✓ |
| $\mathrm{KI}_{\mathrm{\_MAMEX\_f}}$ | `KI__MAMEX_f` | renal clearance of metoprolol acid relative to the GFR | $1.53417669140723$ | \- | ✓ |
| $\mathrm{KI}_{\mathrm{\_GFR}}$ | `KI__GFR` | glomerular filtration rate |  | ml/min |  |

## Initial assignments and assignment rules

The initial assignments set the values at $t = 0$:

$$
\begin{aligned}
\mathrm{Aurine}_{\mathrm{met}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{Aurine}_{\mathrm{metoh}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{Aurine}_{\mathrm{mam}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{Afeces}_{\mathrm{met}} &= 0 \cdot \mathrm{Vfeces}
\end{aligned}
$$

The assignment rules hold at every time $t$:

$$
\begin{aligned}
\mathrm{FVre} &= 1 - \mathrm{FVgu} - \mathrm{FVhe} - \mathrm{FVki} \\
&\quad {} - \mathrm{FVli} - \mathrm{FVlu} - \mathrm{FVve} - \mathrm{FVar} \\[1ex]
\mathrm{FQre} &= 1 - \mathrm{FQki} - \mathrm{FQhe} - \mathrm{FQh} \\[1ex]
\mathrm{BSA} &= 0.024265 \cdot \mathopen{}\left(\frac{\mathrm{BW}}{1}\right)^{0.5378} \cdot \mathopen{}\left(\frac{\mathrm{HEIGHT}}{1}\right)^{0.3964} \\[1ex]
\mathrm{CO} &= \mathrm{BW} \cdot \mathrm{COBW} \\[1ex]
\mathrm{QC} &= \frac{\mathrm{CO}}{1000} \cdot 60 \\[1ex]
\mathrm{Vgu} &= \mathrm{BW} \cdot \mathrm{FVgu} \\[1ex]
\mathrm{Vhe} &= \mathrm{BW} \cdot \mathrm{FVhe} \\[1ex]
\mathrm{Vki} &= \mathrm{BW} \cdot \mathrm{FVki} \\[1ex]
\mathrm{Vli} &= \mathrm{BW} \cdot \mathrm{FVli} \\[1ex]
\mathrm{Vlu} &= \mathrm{BW} \cdot \mathrm{FVlu} \\[1ex]
\mathrm{Vre} &= \mathrm{BW} \cdot \mathrm{FVre} \\[1ex]
\mathrm{Vve} &= \mathrm{BW} \cdot \mathrm{FVve} - \frac{\mathrm{FVve}}{\mathrm{FVar} + \mathrm{FVve} + \mathrm{FVpo} + \mathrm{FVhv}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVar} - \mathrm{FVve} - \mathrm{FVpo} - \mathrm{FVhv}\right) \\[1ex]
\mathrm{Var} &= \mathrm{BW} \cdot \mathrm{FVar} - \frac{\mathrm{FVar}}{\mathrm{FVar} + \mathrm{FVve} + \mathrm{FVpo} + \mathrm{FVhv}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVar} - \mathrm{FVve} - \mathrm{FVpo} - \mathrm{FVhv}\right) \\[1ex]
\mathrm{Vpo} &= \mathrm{BW} \cdot \mathrm{FVpo} - \frac{\mathrm{FVpo}}{\mathrm{FVar} + \mathrm{FVve} + \mathrm{FVpo} + \mathrm{FVhv}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVar} - \mathrm{FVve} - \mathrm{FVpo} - \mathrm{FVhv}\right) \\[1ex]
\mathrm{Vhv} &= \mathrm{BW} \cdot \mathrm{FVhv} - \frac{\mathrm{FVhv}}{\mathrm{FVar} + \mathrm{FVve} + \mathrm{FVpo} + \mathrm{FVhv}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVar} - \mathrm{FVve} - \mathrm{FVpo} - \mathrm{FVhv}\right) \\[1ex]
\mathrm{Qgu} &= \mathrm{QC} \cdot \mathrm{FQgu} \\[1ex]
\mathrm{Qhe} &= \mathrm{QC} \cdot \mathrm{FQhe} \\[1ex]
\mathrm{Qki} &= \mathrm{QC} \cdot \mathrm{FQki} \\[1ex]
\mathrm{Qh} &= \mathrm{QC} \cdot \mathrm{FQh} \\[1ex]
\mathrm{Qha} &= \mathrm{Qh} - \mathrm{Qgu} \\[1ex]
\mathrm{Qlu} &= \mathrm{QC} \cdot \mathrm{FQlu} \\[1ex]
\mathrm{Qre} &= \mathrm{QC} \cdot \mathrm{FQre} \\[1ex]
\mathrm{Qpo} &= \mathrm{Qgu} \\[1ex]
\mathrm{GFR}_{\mathrm{base}} &= f_{\mathrm{GFR\_Qki}} \cdot \mathrm{Qki} \\[1ex]
\mathrm{Ki}_{\mathrm{met}} &= \frac{0.693}{\mathrm{ti}_{\mathrm{met}}} \cdot 60 \\[1ex]
\mathrm{Ka}_{\mathrm{dis\_form\_met}} &= \mathopen{}\left(1 - \mathrm{form}_{\mathrm{sr}} - \mathrm{form}_{\mathrm{cr}}\right) \cdot \mathrm{Ka}_{\mathrm{dis\_met}} + \mathrm{form}_{\mathrm{sr}} \cdot \mathrm{Ka}_{\mathrm{dis\_sr\_met}} + \mathrm{form}_{\mathrm{cr}} \cdot \mathrm{Ka}_{\mathrm{dis\_cr\_met}} \\[1ex]
F_{\mathrm{form\_met}} &= F_{\mathrm{met}} \cdot \mathopen{}\left(1 - \mathrm{form}_{\mathrm{cr}} \cdot \mathopen{}\left(1 - F_{\mathrm{cr\_met}}\right)\right) \\[1ex]
\mathrm{dissolution}_{\mathrm{met}} &= \frac{\frac{\mathrm{Ka}_{\mathrm{dis\_form\_met}}}{60} \cdot \mathrm{PODOSE}_{\mathrm{met}}}{\mathrm{Mr}_{\mathrm{met}}} \\[1ex]
\mathrm{Vgu}_{\mathrm{blood}} &= \mathrm{Vgu} \cdot \mathrm{Fblood} \\[1ex]
\mathrm{Vgu}_{\mathrm{tissue}} &= \mathrm{Vgu} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vhe}_{\mathrm{blood}} &= \mathrm{Vhe} \cdot \mathrm{Fblood} \\[1ex]
\mathrm{Vhe}_{\mathrm{tissue}} &= \mathrm{Vhe} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vki}_{\mathrm{blood}} &= \mathrm{Vki} \cdot \mathrm{Fblood} \\[1ex]
\mathrm{Vki}_{\mathrm{tissue}} &= \mathrm{Vki} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vli}_{\mathrm{blood}} &= \mathrm{Vli} \cdot \mathrm{Fblood} \\[1ex]
\mathrm{Vli}_{\mathrm{tissue}} &= \mathrm{Vli} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vlu}_{\mathrm{blood}} &= \mathrm{Vlu} \cdot \mathrm{Fblood} \\[1ex]
\mathrm{Vlu}_{\mathrm{tissue}} &= \mathrm{Vlu} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vre}_{\mathrm{blood}} &= \mathrm{Vre} \cdot \mathrm{Fblood} \\[1ex]
\mathrm{Vre}_{\mathrm{tissue}} &= \mathrm{Vre} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Cveplasma}_{\mathrm{met}} &= \frac{\mathrm{Cve}_{\mathrm{met}}}{\mathrm{BP}_{\mathrm{met}}} \\[1ex]
\mathrm{Cveplasma}_{\mathrm{metoh}} &= \frac{\mathrm{Cve}_{\mathrm{metoh}}}{\mathrm{BP}_{\mathrm{metoh}}} \\[1ex]
\mathrm{Cveplasma}_{\mathrm{mam}} &= \frac{\mathrm{Cve}_{\mathrm{mam}}}{\mathrm{BP}_{\mathrm{mam}}} \\[1ex]
\mathrm{HRred} &= \frac{\mathrm{HRred}_{\mathrm{Emax}} \cdot \mathopen{}\left(\frac{\mathrm{Cveplasma}_{\mathrm{met}}}{\mathrm{HRred}_{\mathrm{EC50}}}\right)^{\mathrm{HRred}_{\mathrm{n}}}}{1 + \mathopen{}\left(\frac{\mathrm{Cveplasma}_{\mathrm{met}}}{\mathrm{HRred}_{\mathrm{EC50}}}\right)^{\mathrm{HRred}_{\mathrm{n}}}} \\[1ex]
\mathrm{HReff} &= \mathrm{HR} \cdot \mathopen{}\left(1 - \mathrm{HRred}\right) \\[1ex]
\mathrm{LI}_{\mathrm{\_cyp2d6\_activity1}} &= \begin{cases} \frac{\mathrm{LI}_{\mathrm{\_cyp2d6\_ac}}}{2} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = -1 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a0}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 0 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a1}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 1 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a2}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 2 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a3}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 3 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a4}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 4 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a5}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 5 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a6}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 6 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a7}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 7 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a8}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 8 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a9}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 9 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a10}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 10 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a11}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 11 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a12}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 12 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a13}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 13 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a14}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 14 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a15}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 15 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a16}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 16 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a17}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 17 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a18}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 18 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a19}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 19 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a20}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 20 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a21}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 21 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a22}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 22 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a23}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 23 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a24}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 24 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a25}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 25 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a26}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 26 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a27}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 27 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a28}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 28 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a29}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 29 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a30}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 30 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a31}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 31 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a32}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 32 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a33}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 33 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a34}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 34 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a35}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 35 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a36}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 36 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a37}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 37 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a38}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 38 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a39}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 39 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a40}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 40 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a41}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 41 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a42}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 42 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a43}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 43 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a44}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 44 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a45}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 45 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a46}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 46 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a47}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 47 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a48}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 48 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a49}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 49 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a50}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 50 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a51}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 51 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a52}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 52 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a53}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 53 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a54}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 54 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a55}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 55 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a56}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 56 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a57}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 57 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a58}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 58 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a59}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 59 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a60}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 60 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a61}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 61 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a62}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 62 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a63}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 63 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a64}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 64 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a65}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 65 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a66}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 66 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a67}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 67 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a68}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 68 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a69}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 69 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a70}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 70 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a71}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 71 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a72}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 72 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a73}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 73 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a74}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 74 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a75}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 75 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a76}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 76 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a77}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 77 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a78}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 78 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a79}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 79 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a80}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 80 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a81}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 81 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a82}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 82 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a83}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 83 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a84}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele1}} = 84 \\ \frac{\mathrm{LI}_{\mathrm{\_cyp2d6\_ac}}}{2} & \text{otherwise} \end{cases} \\[1ex]
\mathrm{LI}_{\mathrm{\_cyp2d6\_activity2}} &= \begin{cases} \frac{\mathrm{LI}_{\mathrm{\_cyp2d6\_ac}}}{2} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = -1 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a0}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 0 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a1}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 1 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a2}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 2 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a3}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 3 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a4}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 4 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a5}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 5 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a6}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 6 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a7}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 7 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a8}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 8 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a9}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 9 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a10}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 10 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a11}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 11 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a12}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 12 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a13}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 13 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a14}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 14 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a15}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 15 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a16}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 16 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a17}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 17 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a18}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 18 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a19}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 19 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a20}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 20 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a21}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 21 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a22}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 22 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a23}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 23 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a24}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 24 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a25}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 25 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a26}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 26 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a27}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 27 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a28}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 28 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a29}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 29 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a30}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 30 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a31}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 31 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a32}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 32 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a33}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 33 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a34}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 34 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a35}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 35 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a36}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 36 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a37}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 37 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a38}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 38 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a39}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 39 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a40}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 40 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a41}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 41 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a42}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 42 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a43}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 43 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a44}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 44 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a45}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 45 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a46}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 46 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a47}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 47 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a48}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 48 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a49}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 49 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a50}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 50 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a51}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 51 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a52}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 52 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a53}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 53 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a54}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 54 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a55}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 55 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a56}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 56 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a57}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 57 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a58}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 58 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a59}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 59 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a60}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 60 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a61}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 61 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a62}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 62 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a63}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 63 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a64}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 64 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a65}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 65 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a66}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 66 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a67}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 67 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a68}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 68 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a69}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 69 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a70}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 70 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a71}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 71 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a72}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 72 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a73}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 73 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a74}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 74 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a75}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 75 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a76}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 76 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a77}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 77 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a78}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 78 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a79}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 79 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a80}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 80 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a81}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 81 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a82}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 82 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a83}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 83 \\ \mathrm{LI}_{\mathrm{\_cyp2d6\_a84}} & \text{if } \mathrm{LI}_{\mathrm{\_cyp2d6\_allele2}} = 84 \\ \frac{\mathrm{LI}_{\mathrm{\_cyp2d6\_ac}}}{2} & \text{otherwise} \end{cases} \\[1ex]
\mathrm{LI}_{\mathrm{\_cyp2d6\_activity}} &= \mathrm{LI}_{\mathrm{\_cyp2d6\_activity1}} + \mathrm{LI}_{\mathrm{\_cyp2d6\_activity2}} \\[1ex]
\mathrm{LI}_{\mathrm{\_f\_cyp2d6}} &= \frac{\mathrm{LI}_{\mathrm{\_cyp2d6\_activity}}}{2} \\[1ex]
\mathrm{KI}_{\mathrm{\_GFR}} &= \mathrm{KI}_{\mathrm{\_f\_renal\_function}} \cdot \mathrm{GFR}_{\mathrm{base}}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation |
| --- | --- | --- | --- |
| $v_{\mathrm{transport\_gu\_met}}$ | `transport_gu_met` | transport metoprolol (gastrointestinal tract) | $\mathrm{Cgu}_{\mathrm{blood\_met}} \rightleftharpoons \mathrm{Cgu}_{\mathrm{met}}$ |
| $v_{\mathrm{transport\_he\_met}}$ | `transport_he_met` | transport metoprolol (heart) | $\mathrm{Che}_{\mathrm{blood\_met}} \rightleftharpoons \mathrm{Che}_{\mathrm{met}}$ |
| $v_{\mathrm{transport\_ki\_met}}$ | `transport_ki_met` | transport metoprolol (kidney) | $\mathrm{Cki}_{\mathrm{blood\_met}} \rightleftharpoons \mathrm{Cki}_{\mathrm{met}}$ |
| $v_{\mathrm{transport\_lu\_met}}$ | `transport_lu_met` | transport metoprolol (lung) | $\mathrm{Clu}_{\mathrm{blood\_met}} \rightleftharpoons \mathrm{Clu}_{\mathrm{met}}$ |
| $v_{\mathrm{transport\_re\_met}}$ | `transport_re_met` | transport metoprolol (rest) | $\mathrm{Cre}_{\mathrm{blood\_met}} \rightleftharpoons \mathrm{Cre}_{\mathrm{met}}$ |
| $v_{\mathrm{Flow\_ve\_lu\_met}}$ | `Flow_ve_lu_met` | blood flow metoprolol (ve to lu\_blood) | $\mathrm{Cve}_{\mathrm{met}} \longrightarrow \mathrm{Clu}_{\mathrm{blood\_met}}$ |
| $v_{\mathrm{Flow\_lu\_ar\_met}}$ | `Flow_lu_ar_met` | blood flow metoprolol (lu\_blood to ar) | $\mathrm{Clu}_{\mathrm{blood\_met}} \longrightarrow \mathrm{Car}_{\mathrm{met}}$ |
| $v_{\mathrm{Flow\_ar\_ki\_met}}$ | `Flow_ar_ki_met` | blood flow metoprolol (ar to ki\_blood) | $\mathrm{Car}_{\mathrm{met}} \longrightarrow \mathrm{Cki}_{\mathrm{blood\_met}}$ |
| $v_{\mathrm{Flow\_ki\_ve\_met}}$ | `Flow_ki_ve_met` | blood flow metoprolol (ki\_blood to ve) | $\mathrm{Cki}_{\mathrm{blood\_met}} \longrightarrow \mathrm{Cve}_{\mathrm{met}}$ |
| $v_{\mathrm{Flow\_ar\_he\_met}}$ | `Flow_ar_he_met` | blood flow metoprolol (ar to he\_blood) | $\mathrm{Car}_{\mathrm{met}} \longrightarrow \mathrm{Che}_{\mathrm{blood\_met}}$ |
| $v_{\mathrm{Flow\_he\_ve\_met}}$ | `Flow_he_ve_met` | blood flow metoprolol (he\_blood to ve) | $\mathrm{Che}_{\mathrm{blood\_met}} \longrightarrow \mathrm{Cve}_{\mathrm{met}}$ |
| $v_{\mathrm{Flow\_ar\_re\_met}}$ | `Flow_ar_re_met` | blood flow metoprolol (ar to re\_blood) | $\mathrm{Car}_{\mathrm{met}} \longrightarrow \mathrm{Cre}_{\mathrm{blood\_met}}$ |
| $v_{\mathrm{Flow\_re\_ve\_met}}$ | `Flow_re_ve_met` | blood flow metoprolol (re\_blood to ve) | $\mathrm{Cre}_{\mathrm{blood\_met}} \longrightarrow \mathrm{Cve}_{\mathrm{met}}$ |
| $v_{\mathrm{Flow\_ar\_gu\_met}}$ | `Flow_ar_gu_met` | blood flow metoprolol (ar to gu\_blood) | $\mathrm{Car}_{\mathrm{met}} \longrightarrow \mathrm{Cgu}_{\mathrm{blood\_met}}$ |
| $v_{\mathrm{Flow\_gu\_po\_met}}$ | `Flow_gu_po_met` | blood flow metoprolol (gu\_blood to po) | $\mathrm{Cgu}_{\mathrm{blood\_met}} \longrightarrow \mathrm{Cpo}_{\mathrm{met}}$ |
| $v_{\mathrm{Flow\_ar\_li\_met}}$ | `Flow_ar_li_met` | blood flow metoprolol (ar to li\_blood) | $\mathrm{Car}_{\mathrm{met}} \longrightarrow \mathrm{Cli}_{\mathrm{blood\_met}}$ |
| $v_{\mathrm{Flow\_po\_li\_met}}$ | `Flow_po_li_met` | blood flow metoprolol (po to li\_blood) | $\mathrm{Cpo}_{\mathrm{met}} \longrightarrow \mathrm{Cli}_{\mathrm{blood\_met}}$ |
| $v_{\mathrm{Flow\_li\_hv\_met}}$ | `Flow_li_hv_met` | blood flow metoprolol (li\_blood to hv) | $\mathrm{Cli}_{\mathrm{blood\_met}} \longrightarrow \mathrm{Chv}_{\mathrm{met}}$ |
| $v_{\mathrm{Flow\_hv\_ve\_met}}$ | `Flow_hv_ve_met` | blood flow metoprolol (hv to ve) | $\mathrm{Chv}_{\mathrm{met}} \longrightarrow \mathrm{Cve}_{\mathrm{met}}$ |
| $v_{\mathrm{transport\_gu\_metoh}}$ | `transport_gu_metoh` | transport alpha-hydroxymetoprolol (gastrointestinal tract) | $\mathrm{Cgu}_{\mathrm{blood\_metoh}} \rightleftharpoons \mathrm{Cgu}_{\mathrm{metoh}}$ |
| $v_{\mathrm{transport\_he\_metoh}}$ | `transport_he_metoh` | transport alpha-hydroxymetoprolol (heart) | $\mathrm{Che}_{\mathrm{blood\_metoh}} \rightleftharpoons \mathrm{Che}_{\mathrm{metoh}}$ |
| $v_{\mathrm{transport\_ki\_metoh}}$ | `transport_ki_metoh` | transport alpha-hydroxymetoprolol (kidney) | $\mathrm{Cki}_{\mathrm{blood\_metoh}} \rightleftharpoons \mathrm{Cki}_{\mathrm{metoh}}$ |
| $v_{\mathrm{transport\_lu\_metoh}}$ | `transport_lu_metoh` | transport alpha-hydroxymetoprolol (lung) | $\mathrm{Clu}_{\mathrm{blood\_metoh}} \rightleftharpoons \mathrm{Clu}_{\mathrm{metoh}}$ |
| $v_{\mathrm{transport\_re\_metoh}}$ | `transport_re_metoh` | transport alpha-hydroxymetoprolol (rest) | $\mathrm{Cre}_{\mathrm{blood\_metoh}} \rightleftharpoons \mathrm{Cre}_{\mathrm{metoh}}$ |
| $v_{\mathrm{Flow\_ve\_lu\_metoh}}$ | `Flow_ve_lu_metoh` | blood flow alpha-hydroxymetoprolol (ve to lu\_blood) | $\mathrm{Cve}_{\mathrm{metoh}} \longrightarrow \mathrm{Clu}_{\mathrm{blood\_metoh}}$ |
| $v_{\mathrm{Flow\_lu\_ar\_metoh}}$ | `Flow_lu_ar_metoh` | blood flow alpha-hydroxymetoprolol (lu\_blood to ar) | $\mathrm{Clu}_{\mathrm{blood\_metoh}} \longrightarrow \mathrm{Car}_{\mathrm{metoh}}$ |
| $v_{\mathrm{Flow\_ar\_ki\_metoh}}$ | `Flow_ar_ki_metoh` | blood flow alpha-hydroxymetoprolol (ar to ki\_blood) | $\mathrm{Car}_{\mathrm{metoh}} \longrightarrow \mathrm{Cki}_{\mathrm{blood\_metoh}}$ |
| $v_{\mathrm{Flow\_ki\_ve\_metoh}}$ | `Flow_ki_ve_metoh` | blood flow alpha-hydroxymetoprolol (ki\_blood to ve) | $\mathrm{Cki}_{\mathrm{blood\_metoh}} \longrightarrow \mathrm{Cve}_{\mathrm{metoh}}$ |
| $v_{\mathrm{Flow\_ar\_he\_metoh}}$ | `Flow_ar_he_metoh` | blood flow alpha-hydroxymetoprolol (ar to he\_blood) | $\mathrm{Car}_{\mathrm{metoh}} \longrightarrow \mathrm{Che}_{\mathrm{blood\_metoh}}$ |
| $v_{\mathrm{Flow\_he\_ve\_metoh}}$ | `Flow_he_ve_metoh` | blood flow alpha-hydroxymetoprolol (he\_blood to ve) | $\mathrm{Che}_{\mathrm{blood\_metoh}} \longrightarrow \mathrm{Cve}_{\mathrm{metoh}}$ |
| $v_{\mathrm{Flow\_ar\_re\_metoh}}$ | `Flow_ar_re_metoh` | blood flow alpha-hydroxymetoprolol (ar to re\_blood) | $\mathrm{Car}_{\mathrm{metoh}} \longrightarrow \mathrm{Cre}_{\mathrm{blood\_metoh}}$ |
| $v_{\mathrm{Flow\_re\_ve\_metoh}}$ | `Flow_re_ve_metoh` | blood flow alpha-hydroxymetoprolol (re\_blood to ve) | $\mathrm{Cre}_{\mathrm{blood\_metoh}} \longrightarrow \mathrm{Cve}_{\mathrm{metoh}}$ |
| $v_{\mathrm{Flow\_ar\_gu\_metoh}}$ | `Flow_ar_gu_metoh` | blood flow alpha-hydroxymetoprolol (ar to gu\_blood) | $\mathrm{Car}_{\mathrm{metoh}} \longrightarrow \mathrm{Cgu}_{\mathrm{blood\_metoh}}$ |
| $v_{\mathrm{Flow\_gu\_po\_metoh}}$ | `Flow_gu_po_metoh` | blood flow alpha-hydroxymetoprolol (gu\_blood to po) | $\mathrm{Cgu}_{\mathrm{blood\_metoh}} \longrightarrow \mathrm{Cpo}_{\mathrm{metoh}}$ |
| $v_{\mathrm{Flow\_ar\_li\_metoh}}$ | `Flow_ar_li_metoh` | blood flow alpha-hydroxymetoprolol (ar to li\_blood) | $\mathrm{Car}_{\mathrm{metoh}} \longrightarrow \mathrm{Cli}_{\mathrm{blood\_metoh}}$ |
| $v_{\mathrm{Flow\_po\_li\_metoh}}$ | `Flow_po_li_metoh` | blood flow alpha-hydroxymetoprolol (po to li\_blood) | $\mathrm{Cpo}_{\mathrm{metoh}} \longrightarrow \mathrm{Cli}_{\mathrm{blood\_metoh}}$ |
| $v_{\mathrm{Flow\_li\_hv\_metoh}}$ | `Flow_li_hv_metoh` | blood flow alpha-hydroxymetoprolol (li\_blood to hv) | $\mathrm{Cli}_{\mathrm{blood\_metoh}} \longrightarrow \mathrm{Chv}_{\mathrm{metoh}}$ |
| $v_{\mathrm{Flow\_hv\_ve\_metoh}}$ | `Flow_hv_ve_metoh` | blood flow alpha-hydroxymetoprolol (hv to ve) | $\mathrm{Chv}_{\mathrm{metoh}} \longrightarrow \mathrm{Cve}_{\mathrm{metoh}}$ |
| $v_{\mathrm{transport\_gu\_mam}}$ | `transport_gu_mam` | transport metoprolol acid (gastrointestinal tract) | $\mathrm{Cgu}_{\mathrm{blood\_mam}} \rightleftharpoons \mathrm{Cgu}_{\mathrm{mam}}$ |
| $v_{\mathrm{transport\_he\_mam}}$ | `transport_he_mam` | transport metoprolol acid (heart) | $\mathrm{Che}_{\mathrm{blood\_mam}} \rightleftharpoons \mathrm{Che}_{\mathrm{mam}}$ |
| $v_{\mathrm{transport\_ki\_mam}}$ | `transport_ki_mam` | transport metoprolol acid (kidney) | $\mathrm{Cki}_{\mathrm{blood\_mam}} \rightleftharpoons \mathrm{Cki}_{\mathrm{mam}}$ |
| $v_{\mathrm{transport\_lu\_mam}}$ | `transport_lu_mam` | transport metoprolol acid (lung) | $\mathrm{Clu}_{\mathrm{blood\_mam}} \rightleftharpoons \mathrm{Clu}_{\mathrm{mam}}$ |
| $v_{\mathrm{transport\_re\_mam}}$ | `transport_re_mam` | transport metoprolol acid (rest) | $\mathrm{Cre}_{\mathrm{blood\_mam}} \rightleftharpoons \mathrm{Cre}_{\mathrm{mam}}$ |
| $v_{\mathrm{Flow\_ve\_lu\_mam}}$ | `Flow_ve_lu_mam` | blood flow metoprolol acid (ve to lu\_blood) | $\mathrm{Cve}_{\mathrm{mam}} \longrightarrow \mathrm{Clu}_{\mathrm{blood\_mam}}$ |
| $v_{\mathrm{Flow\_lu\_ar\_mam}}$ | `Flow_lu_ar_mam` | blood flow metoprolol acid (lu\_blood to ar) | $\mathrm{Clu}_{\mathrm{blood\_mam}} \longrightarrow \mathrm{Car}_{\mathrm{mam}}$ |
| $v_{\mathrm{Flow\_ar\_ki\_mam}}$ | `Flow_ar_ki_mam` | blood flow metoprolol acid (ar to ki\_blood) | $\mathrm{Car}_{\mathrm{mam}} \longrightarrow \mathrm{Cki}_{\mathrm{blood\_mam}}$ |
| $v_{\mathrm{Flow\_ki\_ve\_mam}}$ | `Flow_ki_ve_mam` | blood flow metoprolol acid (ki\_blood to ve) | $\mathrm{Cki}_{\mathrm{blood\_mam}} \longrightarrow \mathrm{Cve}_{\mathrm{mam}}$ |
| $v_{\mathrm{Flow\_ar\_he\_mam}}$ | `Flow_ar_he_mam` | blood flow metoprolol acid (ar to he\_blood) | $\mathrm{Car}_{\mathrm{mam}} \longrightarrow \mathrm{Che}_{\mathrm{blood\_mam}}$ |
| $v_{\mathrm{Flow\_he\_ve\_mam}}$ | `Flow_he_ve_mam` | blood flow metoprolol acid (he\_blood to ve) | $\mathrm{Che}_{\mathrm{blood\_mam}} \longrightarrow \mathrm{Cve}_{\mathrm{mam}}$ |
| $v_{\mathrm{Flow\_ar\_re\_mam}}$ | `Flow_ar_re_mam` | blood flow metoprolol acid (ar to re\_blood) | $\mathrm{Car}_{\mathrm{mam}} \longrightarrow \mathrm{Cre}_{\mathrm{blood\_mam}}$ |
| $v_{\mathrm{Flow\_re\_ve\_mam}}$ | `Flow_re_ve_mam` | blood flow metoprolol acid (re\_blood to ve) | $\mathrm{Cre}_{\mathrm{blood\_mam}} \longrightarrow \mathrm{Cve}_{\mathrm{mam}}$ |
| $v_{\mathrm{Flow\_ar\_gu\_mam}}$ | `Flow_ar_gu_mam` | blood flow metoprolol acid (ar to gu\_blood) | $\mathrm{Car}_{\mathrm{mam}} \longrightarrow \mathrm{Cgu}_{\mathrm{blood\_mam}}$ |
| $v_{\mathrm{Flow\_gu\_po\_mam}}$ | `Flow_gu_po_mam` | blood flow metoprolol acid (gu\_blood to po) | $\mathrm{Cgu}_{\mathrm{blood\_mam}} \longrightarrow \mathrm{Cpo}_{\mathrm{mam}}$ |
| $v_{\mathrm{Flow\_ar\_li\_mam}}$ | `Flow_ar_li_mam` | blood flow metoprolol acid (ar to li\_blood) | $\mathrm{Car}_{\mathrm{mam}} \longrightarrow \mathrm{Cli}_{\mathrm{blood\_mam}}$ |
| $v_{\mathrm{Flow\_po\_li\_mam}}$ | `Flow_po_li_mam` | blood flow metoprolol acid (po to li\_blood) | $\mathrm{Cpo}_{\mathrm{mam}} \longrightarrow \mathrm{Cli}_{\mathrm{blood\_mam}}$ |
| $v_{\mathrm{Flow\_li\_hv\_mam}}$ | `Flow_li_hv_mam` | blood flow metoprolol acid (li\_blood to hv) | $\mathrm{Cli}_{\mathrm{blood\_mam}} \longrightarrow \mathrm{Chv}_{\mathrm{mam}}$ |
| $v_{\mathrm{Flow\_hv\_ve\_mam}}$ | `Flow_hv_ve_mam` | blood flow metoprolol acid (hv to ve) | $\mathrm{Chv}_{\mathrm{mam}} \longrightarrow \mathrm{Cve}_{\mathrm{mam}}$ |
| $v_{\mathrm{iv\_met}}$ | `iv_met` | iv metoprolol | $\varnothing \longrightarrow \mathrm{Cve}_{\mathrm{met}}$ |
| $v_{\mathrm{absorption\_met}}$ | `absorption_met` | absorption metoprolol | $\varnothing \longrightarrow \mathrm{Cgu}_{\mathrm{blood\_met}}$ |
| $v_{\mathrm{excretion\_met}}$ | `excretion_met` | fecal excretion metoprolol | $\varnothing \longrightarrow \mathrm{Afeces}_{\mathrm{met}}$ |
| $v_{\mathrm{LI\_\_METIM}}$ | `LI__METIM` | metoprolol exchange (blood, hepatocyte) | $\mathrm{Cli}_{\mathrm{blood\_met}} \rightleftharpoons \mathrm{LI}_{\mathrm{\_met}}$ |
| $v_{\mathrm{LI\_\_METOH}}$ | `LI__METOH` | alpha-hydroxylation of metoprolol (CYP2D6) | $\mathrm{LI}_{\mathrm{\_met}} \longrightarrow \mathrm{LI}_{\mathrm{\_metoh}}$ |
| $v_{\mathrm{LI\_\_ODM2D6}}$ | `LI__ODM2D6` | O-demethylation of metoprolol (CYP2D6) | $\mathrm{LI}_{\mathrm{\_met}} \longrightarrow \mathrm{LI}_{\mathrm{\_mam}}$ |
| $v_{\mathrm{LI\_\_ODM}}$ | `LI__ODM` | O-demethylation of metoprolol (other enzymes) | $\mathrm{LI}_{\mathrm{\_met}} \longrightarrow \mathrm{LI}_{\mathrm{\_mam}}$ |
| $v_{\mathrm{LI\_\_METOHEX}}$ | `LI__METOHEX` | alpha-hydroxymetoprolol export | $\mathrm{LI}_{\mathrm{\_metoh}} \rightleftharpoons \mathrm{Cli}_{\mathrm{blood\_metoh}}$ |
| $v_{\mathrm{LI\_\_MAMEX}}$ | `LI__MAMEX` | metoprolol acid export | $\mathrm{LI}_{\mathrm{\_mam}} \rightleftharpoons \mathrm{Cli}_{\mathrm{blood\_mam}}$ |
| $v_{\mathrm{KI\_\_METEX}}$ | `KI__METEX` | metoprolol renal excretion | $\mathrm{Cki}_{\mathrm{blood\_met}} \longrightarrow \mathrm{Aurine}_{\mathrm{met}}$ |
| $v_{\mathrm{KI\_\_METOHEX}}$ | `KI__METOHEX` | alpha-hydroxymetoprolol renal excretion | $\mathrm{Cki}_{\mathrm{blood\_metoh}} \longrightarrow \mathrm{Aurine}_{\mathrm{metoh}}$ |
| $v_{\mathrm{KI\_\_MAMEX}}$ | `KI__MAMEX` | metoprolol acid renal excretion | $\mathrm{Cki}_{\mathrm{blood\_mam}} \longrightarrow \mathrm{Aurine}_{\mathrm{mam}}$ |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{transport\_gu\_met}} &= \frac{\mathrm{ftissue}_{\mathrm{met}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cgu}_{\mathrm{blood\_met}} \cdot \mathrm{Kp}_{\mathrm{met}} - \mathrm{Cgu}_{\mathrm{met}}\right) \\[1ex]
v_{\mathrm{transport\_he\_met}} &= \frac{\mathrm{ftissue}_{\mathrm{met}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Che}_{\mathrm{blood\_met}} \cdot \mathrm{Kp}_{\mathrm{met}} - \mathrm{Che}_{\mathrm{met}}\right) \\[1ex]
v_{\mathrm{transport\_ki\_met}} &= \frac{\mathrm{ftissue}_{\mathrm{met}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cki}_{\mathrm{blood\_met}} \cdot \mathrm{Kp}_{\mathrm{met}} - \mathrm{Cki}_{\mathrm{met}}\right) \\[1ex]
v_{\mathrm{transport\_lu\_met}} &= \frac{\mathrm{ftissue}_{\mathrm{met}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Clu}_{\mathrm{blood\_met}} \cdot \mathrm{Kp}_{\mathrm{met}} - \mathrm{Clu}_{\mathrm{met}}\right) \\[1ex]
v_{\mathrm{transport\_re\_met}} &= \frac{\mathrm{ftissue}_{\mathrm{met}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cre}_{\mathrm{blood\_met}} \cdot \mathrm{Kp}_{\mathrm{met}} - \mathrm{Cre}_{\mathrm{met}}\right) \\[1ex]
v_{\mathrm{Flow\_ve\_lu\_met}} &= \mathrm{Qlu} \cdot \mathrm{Cve}_{\mathrm{met}} \\[1ex]
v_{\mathrm{Flow\_lu\_ar\_met}} &= \mathrm{Qlu} \cdot \mathrm{Clu}_{\mathrm{blood\_met}} \\[1ex]
v_{\mathrm{Flow\_ar\_ki\_met}} &= \mathrm{Qki} \cdot \mathrm{Car}_{\mathrm{met}} \\[1ex]
v_{\mathrm{Flow\_ki\_ve\_met}} &= \mathrm{Qki} \cdot \mathrm{Cki}_{\mathrm{blood\_met}} \\[1ex]
v_{\mathrm{Flow\_ar\_he\_met}} &= \mathrm{Qhe} \cdot \mathrm{Car}_{\mathrm{met}} \\[1ex]
v_{\mathrm{Flow\_he\_ve\_met}} &= \mathrm{Qhe} \cdot \mathrm{Che}_{\mathrm{blood\_met}} \\[1ex]
v_{\mathrm{Flow\_ar\_re\_met}} &= \mathrm{Qre} \cdot \mathrm{Car}_{\mathrm{met}} \\[1ex]
v_{\mathrm{Flow\_re\_ve\_met}} &= \mathrm{Qre} \cdot \mathrm{Cre}_{\mathrm{blood\_met}} \\[1ex]
v_{\mathrm{Flow\_ar\_gu\_met}} &= \mathrm{Qgu} \cdot \mathrm{Car}_{\mathrm{met}} \\[1ex]
v_{\mathrm{Flow\_gu\_po\_met}} &= \mathrm{Qgu} \cdot \mathrm{Cgu}_{\mathrm{blood\_met}} \\[1ex]
v_{\mathrm{Flow\_ar\_li\_met}} &= \mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{met}} \\[1ex]
v_{\mathrm{Flow\_po\_li\_met}} &= \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{met}} \\[1ex]
v_{\mathrm{Flow\_li\_hv\_met}} &= \mathrm{Qh} \cdot \mathrm{Cli}_{\mathrm{blood\_met}} \\[1ex]
v_{\mathrm{Flow\_hv\_ve\_met}} &= \mathrm{Qh} \cdot \mathrm{Chv}_{\mathrm{met}} \\[1ex]
v_{\mathrm{transport\_gu\_metoh}} &= \frac{\mathrm{ftissue}_{\mathrm{metoh}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cgu}_{\mathrm{blood\_metoh}} \cdot \mathrm{Kp}_{\mathrm{metoh}} - \mathrm{Cgu}_{\mathrm{metoh}}\right) \\[1ex]
v_{\mathrm{transport\_he\_metoh}} &= \frac{\mathrm{ftissue}_{\mathrm{metoh}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Che}_{\mathrm{blood\_metoh}} \cdot \mathrm{Kp}_{\mathrm{metoh}} - \mathrm{Che}_{\mathrm{metoh}}\right) \\[1ex]
v_{\mathrm{transport\_ki\_metoh}} &= \frac{\mathrm{ftissue}_{\mathrm{metoh}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cki}_{\mathrm{blood\_metoh}} \cdot \mathrm{Kp}_{\mathrm{metoh}} - \mathrm{Cki}_{\mathrm{metoh}}\right) \\[1ex]
v_{\mathrm{transport\_lu\_metoh}} &= \frac{\mathrm{ftissue}_{\mathrm{metoh}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Clu}_{\mathrm{blood\_metoh}} \cdot \mathrm{Kp}_{\mathrm{metoh}} - \mathrm{Clu}_{\mathrm{metoh}}\right) \\[1ex]
v_{\mathrm{transport\_re\_metoh}} &= \frac{\mathrm{ftissue}_{\mathrm{metoh}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cre}_{\mathrm{blood\_metoh}} \cdot \mathrm{Kp}_{\mathrm{metoh}} - \mathrm{Cre}_{\mathrm{metoh}}\right) \\[1ex]
v_{\mathrm{Flow\_ve\_lu\_metoh}} &= \mathrm{Qlu} \cdot \mathrm{Cve}_{\mathrm{metoh}} \\[1ex]
v_{\mathrm{Flow\_lu\_ar\_metoh}} &= \mathrm{Qlu} \cdot \mathrm{Clu}_{\mathrm{blood\_metoh}} \\[1ex]
v_{\mathrm{Flow\_ar\_ki\_metoh}} &= \mathrm{Qki} \cdot \mathrm{Car}_{\mathrm{metoh}} \\[1ex]
v_{\mathrm{Flow\_ki\_ve\_metoh}} &= \mathrm{Qki} \cdot \mathrm{Cki}_{\mathrm{blood\_metoh}} \\[1ex]
v_{\mathrm{Flow\_ar\_he\_metoh}} &= \mathrm{Qhe} \cdot \mathrm{Car}_{\mathrm{metoh}} \\[1ex]
v_{\mathrm{Flow\_he\_ve\_metoh}} &= \mathrm{Qhe} \cdot \mathrm{Che}_{\mathrm{blood\_metoh}} \\[1ex]
v_{\mathrm{Flow\_ar\_re\_metoh}} &= \mathrm{Qre} \cdot \mathrm{Car}_{\mathrm{metoh}} \\[1ex]
v_{\mathrm{Flow\_re\_ve\_metoh}} &= \mathrm{Qre} \cdot \mathrm{Cre}_{\mathrm{blood\_metoh}} \\[1ex]
v_{\mathrm{Flow\_ar\_gu\_metoh}} &= \mathrm{Qgu} \cdot \mathrm{Car}_{\mathrm{metoh}} \\[1ex]
v_{\mathrm{Flow\_gu\_po\_metoh}} &= \mathrm{Qgu} \cdot \mathrm{Cgu}_{\mathrm{blood\_metoh}} \\[1ex]
v_{\mathrm{Flow\_ar\_li\_metoh}} &= \mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{metoh}} \\[1ex]
v_{\mathrm{Flow\_po\_li\_metoh}} &= \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{metoh}} \\[1ex]
v_{\mathrm{Flow\_li\_hv\_metoh}} &= \mathrm{Qh} \cdot \mathrm{Cli}_{\mathrm{blood\_metoh}} \\[1ex]
v_{\mathrm{Flow\_hv\_ve\_metoh}} &= \mathrm{Qh} \cdot \mathrm{Chv}_{\mathrm{metoh}} \\[1ex]
v_{\mathrm{transport\_gu\_mam}} &= \frac{\mathrm{ftissue}_{\mathrm{mam}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cgu}_{\mathrm{blood\_mam}} \cdot \mathrm{Kp}_{\mathrm{mam}} - \mathrm{Cgu}_{\mathrm{mam}}\right) \\[1ex]
v_{\mathrm{transport\_he\_mam}} &= \frac{\mathrm{ftissue}_{\mathrm{mam}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Che}_{\mathrm{blood\_mam}} \cdot \mathrm{Kp}_{\mathrm{mam}} - \mathrm{Che}_{\mathrm{mam}}\right) \\[1ex]
v_{\mathrm{transport\_ki\_mam}} &= \frac{\mathrm{ftissue}_{\mathrm{mam}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cki}_{\mathrm{blood\_mam}} \cdot \mathrm{Kp}_{\mathrm{mam}} - \mathrm{Cki}_{\mathrm{mam}}\right) \\[1ex]
v_{\mathrm{transport\_lu\_mam}} &= \frac{\mathrm{ftissue}_{\mathrm{mam}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Clu}_{\mathrm{blood\_mam}} \cdot \mathrm{Kp}_{\mathrm{mam}} - \mathrm{Clu}_{\mathrm{mam}}\right) \\[1ex]
v_{\mathrm{transport\_re\_mam}} &= \frac{\mathrm{ftissue}_{\mathrm{mam}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cre}_{\mathrm{blood\_mam}} \cdot \mathrm{Kp}_{\mathrm{mam}} - \mathrm{Cre}_{\mathrm{mam}}\right) \\[1ex]
v_{\mathrm{Flow\_ve\_lu\_mam}} &= \mathrm{Qlu} \cdot \mathrm{Cve}_{\mathrm{mam}} \\[1ex]
v_{\mathrm{Flow\_lu\_ar\_mam}} &= \mathrm{Qlu} \cdot \mathrm{Clu}_{\mathrm{blood\_mam}} \\[1ex]
v_{\mathrm{Flow\_ar\_ki\_mam}} &= \mathrm{Qki} \cdot \mathrm{Car}_{\mathrm{mam}} \\[1ex]
v_{\mathrm{Flow\_ki\_ve\_mam}} &= \mathrm{Qki} \cdot \mathrm{Cki}_{\mathrm{blood\_mam}} \\[1ex]
v_{\mathrm{Flow\_ar\_he\_mam}} &= \mathrm{Qhe} \cdot \mathrm{Car}_{\mathrm{mam}} \\[1ex]
v_{\mathrm{Flow\_he\_ve\_mam}} &= \mathrm{Qhe} \cdot \mathrm{Che}_{\mathrm{blood\_mam}} \\[1ex]
v_{\mathrm{Flow\_ar\_re\_mam}} &= \mathrm{Qre} \cdot \mathrm{Car}_{\mathrm{mam}} \\[1ex]
v_{\mathrm{Flow\_re\_ve\_mam}} &= \mathrm{Qre} \cdot \mathrm{Cre}_{\mathrm{blood\_mam}} \\[1ex]
v_{\mathrm{Flow\_ar\_gu\_mam}} &= \mathrm{Qgu} \cdot \mathrm{Car}_{\mathrm{mam}} \\[1ex]
v_{\mathrm{Flow\_gu\_po\_mam}} &= \mathrm{Qgu} \cdot \mathrm{Cgu}_{\mathrm{blood\_mam}} \\[1ex]
v_{\mathrm{Flow\_ar\_li\_mam}} &= \mathrm{Qha} \cdot \mathrm{Car}_{\mathrm{mam}} \\[1ex]
v_{\mathrm{Flow\_po\_li\_mam}} &= \mathrm{Qpo} \cdot \mathrm{Cpo}_{\mathrm{mam}} \\[1ex]
v_{\mathrm{Flow\_li\_hv\_mam}} &= \mathrm{Qh} \cdot \mathrm{Cli}_{\mathrm{blood\_mam}} \\[1ex]
v_{\mathrm{Flow\_hv\_ve\_mam}} &= \mathrm{Qh} \cdot \mathrm{Chv}_{\mathrm{mam}} \\[1ex]
v_{\mathrm{iv\_met}} &= \frac{\mathrm{Ki}_{\mathrm{met}} \cdot \mathrm{IVDOSE}_{\mathrm{met}}}{\mathrm{Mr}_{\mathrm{met}}} \\[1ex]
v_{\mathrm{absorption\_met}} &= \frac{\frac{\mathrm{Ka}_{\mathrm{abs\_met}}}{60} \cdot \mathrm{GUTDOSE}_{\mathrm{met}}}{\mathrm{Mr}_{\mathrm{met}}} \\[1ex]
v_{\mathrm{excretion\_met}} &= \mathopen{}\left(1 - F_{\mathrm{form\_met}}\right) \cdot \mathrm{dissolution}_{\mathrm{met}} \\[1ex]
v_{\mathrm{LI\_\_METIM}} &= \mathrm{LI}_{\mathrm{\_METIM\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathopen{}\left(\mathrm{Cli}_{\mathrm{blood\_met}} - \mathrm{LI}_{\mathrm{\_met}}\right) \\[1ex]
v_{\mathrm{LI\_\_METOH}} &= \frac{\mathrm{LI}_{\mathrm{\_f\_cyp2d6}} \cdot \mathrm{LI}_{\mathrm{\_METOH\_Vmax}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_met}}}{\mathrm{LI}_{\mathrm{\_CYP2D6\_Km\_met}} + \mathrm{LI}_{\mathrm{\_met}}} \\[1ex]
v_{\mathrm{LI\_\_ODM2D6}} &= \frac{\mathrm{LI}_{\mathrm{\_f\_cyp2d6}} \cdot \mathrm{LI}_{\mathrm{\_ODM2D6\_Vmax}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_met}}}{\mathrm{LI}_{\mathrm{\_CYP2D6\_Km\_met}} + \mathrm{LI}_{\mathrm{\_met}}} \\[1ex]
v_{\mathrm{LI\_\_ODM}} &= \frac{\mathrm{LI}_{\mathrm{\_ODM\_Vmax}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_met}}}{\mathrm{LI}_{\mathrm{\_ODM\_Km\_met}} + \mathrm{LI}_{\mathrm{\_met}}} \\[1ex]
v_{\mathrm{LI\_\_METOHEX}} &= \mathrm{LI}_{\mathrm{\_METOHEX\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathopen{}\left(\mathrm{LI}_{\mathrm{\_metoh}} - \mathrm{Cli}_{\mathrm{blood\_metoh}}\right) \\[1ex]
v_{\mathrm{LI\_\_MAMEX}} &= \mathrm{LI}_{\mathrm{\_MAMEX\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathopen{}\left(\mathrm{LI}_{\mathrm{\_mam}} - \mathrm{Cli}_{\mathrm{blood\_mam}}\right) \\[1ex]
v_{\mathrm{KI\_\_METEX}} &= \frac{\mathrm{KI}_{\mathrm{\_GFR}} \cdot 0.001 \cdot \mathrm{fup}_{\mathrm{met}} \cdot \mathrm{KI}_{\mathrm{\_METEX\_f}} \cdot \mathrm{Cki}_{\mathrm{blood\_met}}}{\mathrm{BP}_{\mathrm{met}}} \\[1ex]
v_{\mathrm{KI\_\_METOHEX}} &= \mathrm{KI}_{\mathrm{\_GFR}} \cdot 0.001 \cdot \mathrm{KI}_{\mathrm{\_METOHEX\_f}} \cdot \mathrm{Cki}_{\mathrm{blood\_metoh}} \\[1ex]
v_{\mathrm{KI\_\_MAMEX}} &= \mathrm{KI}_{\mathrm{\_GFR}} \cdot 0.001 \cdot \mathrm{KI}_{\mathrm{\_MAMEX\_f}} \cdot \mathrm{Cki}_{\mathrm{blood\_mam}}
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions and the rate rules:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{blood\_met}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_gu\_met}} + v_{\mathrm{Flow\_ar\_gu\_met}} - v_{\mathrm{Flow\_gu\_po\_met}} + v_{\mathrm{absorption\_met}}}{\mathrm{Vgu}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Che}_{\mathrm{blood\_met}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_he\_met}} + v_{\mathrm{Flow\_ar\_he\_met}} - v_{\mathrm{Flow\_he\_ve\_met}}}{\mathrm{Vhe}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{blood\_met}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_ki\_met}} + v_{\mathrm{Flow\_ar\_ki\_met}} - v_{\mathrm{Flow\_ki\_ve\_met}} - v_{\mathrm{KI\_\_METEX}}}{\mathrm{Vki}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cli}_{\mathrm{blood\_met}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_li\_met}} + v_{\mathrm{Flow\_po\_li\_met}} - v_{\mathrm{Flow\_li\_hv\_met}} - v_{\mathrm{LI\_\_METIM}}}{\mathrm{Vli}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{blood\_met}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_lu\_met}} + v_{\mathrm{Flow\_ve\_lu\_met}} - v_{\mathrm{Flow\_lu\_ar\_met}}}{\mathrm{Vlu}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{blood\_met}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_re\_met}} + v_{\mathrm{Flow\_ar\_re\_met}} - v_{\mathrm{Flow\_re\_ve\_met}}}{\mathrm{Vre}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{met}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}} \Bigl( v_{\mathrm{Flow\_lu\_ar\_met}} - v_{\mathrm{Flow\_ar\_ki\_met}} - v_{\mathrm{Flow\_ar\_he\_met}} - v_{\mathrm{Flow\_ar\_re\_met}} \\
&\quad {} - v_{\mathrm{Flow\_ar\_gu\_met}} - v_{\mathrm{Flow\_ar\_li\_met}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{met}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vve}} \Bigl( -v_{\mathrm{Flow\_ve\_lu\_met}} + v_{\mathrm{Flow\_ki\_ve\_met}} + v_{\mathrm{Flow\_he\_ve\_met}} + v_{\mathrm{Flow\_re\_ve\_met}} \\
&\quad {} + v_{\mathrm{Flow\_hv\_ve\_met}} + v_{\mathrm{iv\_met}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{met}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_gu\_po\_met}} - v_{\mathrm{Flow\_po\_li\_met}}}{\mathrm{Vpo}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Chv}_{\mathrm{met}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_li\_hv\_met}} - v_{\mathrm{Flow\_hv\_ve\_met}}}{\mathrm{Vhv}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{met}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_gu\_met}}}{\mathrm{Vgu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Che}_{\mathrm{met}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_he\_met}}}{\mathrm{Vhe}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{met}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_ki\_met}}}{\mathrm{Vki}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{met}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_lu\_met}}}{\mathrm{Vlu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{met}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_re\_met}}}{\mathrm{Vre}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Aurine}_{\mathrm{met}}}{\mathrm{d} t} &= v_{\mathrm{KI\_\_METEX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{blood\_metoh}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_gu\_metoh}} + v_{\mathrm{Flow\_ar\_gu\_metoh}} - v_{\mathrm{Flow\_gu\_po\_metoh}}}{\mathrm{Vgu}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Che}_{\mathrm{blood\_metoh}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_he\_metoh}} + v_{\mathrm{Flow\_ar\_he\_metoh}} - v_{\mathrm{Flow\_he\_ve\_metoh}}}{\mathrm{Vhe}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{blood\_metoh}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_ki\_metoh}} + v_{\mathrm{Flow\_ar\_ki\_metoh}} - v_{\mathrm{Flow\_ki\_ve\_metoh}} - v_{\mathrm{KI\_\_METOHEX}}}{\mathrm{Vki}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cli}_{\mathrm{blood\_metoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_li\_metoh}} + v_{\mathrm{Flow\_po\_li\_metoh}} - v_{\mathrm{Flow\_li\_hv\_metoh}} + v_{\mathrm{LI\_\_METOHEX}}}{\mathrm{Vli}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{blood\_metoh}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_lu\_metoh}} + v_{\mathrm{Flow\_ve\_lu\_metoh}} - v_{\mathrm{Flow\_lu\_ar\_metoh}}}{\mathrm{Vlu}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{blood\_metoh}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_re\_metoh}} + v_{\mathrm{Flow\_ar\_re\_metoh}} - v_{\mathrm{Flow\_re\_ve\_metoh}}}{\mathrm{Vre}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{metoh}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}} \Bigl( v_{\mathrm{Flow\_lu\_ar\_metoh}} - v_{\mathrm{Flow\_ar\_ki\_metoh}} - v_{\mathrm{Flow\_ar\_he\_metoh}} - v_{\mathrm{Flow\_ar\_re\_metoh}} \\
&\quad {} - v_{\mathrm{Flow\_ar\_gu\_metoh}} - v_{\mathrm{Flow\_ar\_li\_metoh}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{metoh}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vve}} \Bigl( -v_{\mathrm{Flow\_ve\_lu\_metoh}} + v_{\mathrm{Flow\_ki\_ve\_metoh}} + v_{\mathrm{Flow\_he\_ve\_metoh}} + v_{\mathrm{Flow\_re\_ve\_metoh}} \\
&\quad {} + v_{\mathrm{Flow\_hv\_ve\_metoh}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{metoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_gu\_po\_metoh}} - v_{\mathrm{Flow\_po\_li\_metoh}}}{\mathrm{Vpo}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Chv}_{\mathrm{metoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_li\_hv\_metoh}} - v_{\mathrm{Flow\_hv\_ve\_metoh}}}{\mathrm{Vhv}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{metoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_gu\_metoh}}}{\mathrm{Vgu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Che}_{\mathrm{metoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_he\_metoh}}}{\mathrm{Vhe}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{metoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_ki\_metoh}}}{\mathrm{Vki}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{metoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_lu\_metoh}}}{\mathrm{Vlu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{metoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_re\_metoh}}}{\mathrm{Vre}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Aurine}_{\mathrm{metoh}}}{\mathrm{d} t} &= v_{\mathrm{KI\_\_METOHEX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{blood\_mam}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_gu\_mam}} + v_{\mathrm{Flow\_ar\_gu\_mam}} - v_{\mathrm{Flow\_gu\_po\_mam}}}{\mathrm{Vgu}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Che}_{\mathrm{blood\_mam}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_he\_mam}} + v_{\mathrm{Flow\_ar\_he\_mam}} - v_{\mathrm{Flow\_he\_ve\_mam}}}{\mathrm{Vhe}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{blood\_mam}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_ki\_mam}} + v_{\mathrm{Flow\_ar\_ki\_mam}} - v_{\mathrm{Flow\_ki\_ve\_mam}} - v_{\mathrm{KI\_\_MAMEX}}}{\mathrm{Vki}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cli}_{\mathrm{blood\_mam}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_li\_mam}} + v_{\mathrm{Flow\_po\_li\_mam}} - v_{\mathrm{Flow\_li\_hv\_mam}} + v_{\mathrm{LI\_\_MAMEX}}}{\mathrm{Vli}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{blood\_mam}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_lu\_mam}} + v_{\mathrm{Flow\_ve\_lu\_mam}} - v_{\mathrm{Flow\_lu\_ar\_mam}}}{\mathrm{Vlu}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{blood\_mam}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_re\_mam}} + v_{\mathrm{Flow\_ar\_re\_mam}} - v_{\mathrm{Flow\_re\_ve\_mam}}}{\mathrm{Vre}_{\mathrm{blood}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{mam}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}} \Bigl( v_{\mathrm{Flow\_lu\_ar\_mam}} - v_{\mathrm{Flow\_ar\_ki\_mam}} - v_{\mathrm{Flow\_ar\_he\_mam}} - v_{\mathrm{Flow\_ar\_re\_mam}} \\
&\quad {} - v_{\mathrm{Flow\_ar\_gu\_mam}} - v_{\mathrm{Flow\_ar\_li\_mam}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{mam}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vve}} \Bigl( -v_{\mathrm{Flow\_ve\_lu\_mam}} + v_{\mathrm{Flow\_ki\_ve\_mam}} + v_{\mathrm{Flow\_he\_ve\_mam}} + v_{\mathrm{Flow\_re\_ve\_mam}} \\
&\quad {} + v_{\mathrm{Flow\_hv\_ve\_mam}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{mam}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_gu\_po\_mam}} - v_{\mathrm{Flow\_po\_li\_mam}}}{\mathrm{Vpo}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Chv}_{\mathrm{mam}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_li\_hv\_mam}} - v_{\mathrm{Flow\_hv\_ve\_mam}}}{\mathrm{Vhv}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{mam}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_gu\_mam}}}{\mathrm{Vgu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Che}_{\mathrm{mam}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_he\_mam}}}{\mathrm{Vhe}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{mam}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_ki\_mam}}}{\mathrm{Vki}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{mam}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_lu\_mam}}}{\mathrm{Vlu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{mam}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_re\_mam}}}{\mathrm{Vre}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Aurine}_{\mathrm{mam}}}{\mathrm{d} t} &= v_{\mathrm{KI\_\_MAMEX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{met}}}{\mathrm{d} t} &= v_{\mathrm{excretion\_met}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_met}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_METIM}} - v_{\mathrm{LI\_\_METOH}} - v_{\mathrm{LI\_\_ODM2D6}} - v_{\mathrm{LI\_\_ODM}}}{\mathrm{Vli}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_metoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_METOH}} - v_{\mathrm{LI\_\_METOHEX}}}{\mathrm{Vli}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_mam}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_ODM2D6}} + v_{\mathrm{LI\_\_ODM}} - v_{\mathrm{LI\_\_MAMEX}}}{\mathrm{Vli}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{IVDOSE}_{\mathrm{met}}}{\mathrm{d} t} &= -v_{\mathrm{iv\_met}} \cdot \mathrm{Mr}_{\mathrm{met}} + \mathrm{Ri}_{\mathrm{met}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PODOSE}_{\mathrm{met}}}{\mathrm{d} t} &= -\mathrm{dissolution}_{\mathrm{met}} \cdot \mathrm{Mr}_{\mathrm{met}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GUTDOSE}_{\mathrm{met}}}{\mathrm{d} t} &= F_{\mathrm{form\_met}} \cdot \mathrm{dissolution}_{\mathrm{met}} \cdot \mathrm{Mr}_{\mathrm{met}} - v_{\mathrm{absorption\_met}} \cdot \mathrm{Mr}_{\mathrm{met}} \qquad \text{(rate rule)}
\end{aligned}
$$
