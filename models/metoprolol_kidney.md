# Metoprolol kidney model

Model `metoprolol_kidney`, SBML Level 3 Version 1, read from metoprolol\_kidney.xml, written by sbmlode 0.3.0.

Metoprolol kidney model

Metoprolol, alpha-hydroxymetoprolol and metoprolol acid are excreted in the urine. The renal clearances are given relative to the glomerular filtration rate (GFR) and scale with the renal function (f\_renal\_function): the renal clearance of metoprolol is METEX\_f times the filtration of its unbound fraction in plasma (fup\_met \* GFR), the one of a metabolite &lt;X&gt;EX\_f times the GFR. The concentrations of the kidney model are blood concentrations, the plasma concentration of metoprolol is the blood concentration over the blood to plasma ratio BP\_met; the metabolites are taken to have a blood to plasma ratio of 1.

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
| $\mathrm{Vext}$ | `Vext` | blood | $1.5$ | l | ✓ |
| $\mathrm{Vki}$ | `Vki` | kidney | $0.3$ | l | ✓ |
| $\mathrm{Vurine}$ | `Vurine` | urine | $1$ | l | ✓ |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{met}_{\mathrm{ext}}$ | `met_ext` | metoprolol (blood) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{metoh}_{\mathrm{ext}}$ | `metoh_ext` | alpha-hydroxymetoprolol (blood) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{mam}_{\mathrm{ext}}$ | `mam_ext` | metoprolol acid (blood) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{met}_{\mathrm{urine}}$ | `met_urine` | metoprolol (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{metoh}_{\mathrm{urine}}$ | `metoh_urine` | alpha-hydroxymetoprolol (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{mam}_{\mathrm{urine}}$ | `mam_urine` | metoprolol acid (urine) | $\mathrm{Vurine}$ |  | mmol | amount |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $f_{\mathrm{renal\_function}}$ | `f_renal_function` | renal function | $1$ | \- | ✓ |
| $\mathrm{GFR}_{\mathrm{base}}$ | `GFR_base` | glomerular filtration rate (healthy) | $101$ | ml/min | ✓ |
| $\mathrm{fup}_{\mathrm{met}}$ | `fup_met` | fraction unbound in plasma metoprolol | $0.88$ | \- | ✓ |
| $\mathrm{BP}_{\mathrm{met}}$ | `BP_met` | blood to plasma ratio metoprolol | $1.2$ | \- | ✓ |
| $\mathrm{METEX}_{\mathrm{f}}$ | `METEX_f` | renal clearance of unbound metoprolol relative to the GFR | $0.815230242660216$ | \- | ✓ |
| $\mathrm{METOHEX}_{\mathrm{f}}$ | `METOHEX_f` | renal clearance of alpha-hydroxymetoprolol relative to the GFR | $6.76476495170102$ | \- | ✓ |
| $\mathrm{MAMEX}_{\mathrm{f}}$ | `MAMEX_f` | renal clearance of metoprolol acid relative to the GFR | $1.53417669140723$ | \- | ✓ |
| $\mathrm{GFR}$ | `GFR` | glomerular filtration rate |  | ml/min |  |

## Initial assignments and assignment rules

The initial assignments set the values at $t = 0$:

$$
\begin{aligned}
\mathrm{met}_{\mathrm{urine}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{metoh}_{\mathrm{urine}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{mam}_{\mathrm{urine}} &= 0 \cdot \mathrm{Vurine}
\end{aligned}
$$

The assignment rules hold at every time $t$:

$$
\begin{aligned}
\mathrm{GFR} &= f_{\mathrm{renal\_function}} \cdot \mathrm{GFR}_{\mathrm{base}}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation |
| --- | --- | --- | --- |
| $v_{\mathrm{METEX}}$ | `METEX` | metoprolol renal excretion | $\mathrm{met}_{\mathrm{ext}} \longrightarrow \mathrm{met}_{\mathrm{urine}}$ |
| $v_{\mathrm{METOHEX}}$ | `METOHEX` | alpha-hydroxymetoprolol renal excretion | $\mathrm{metoh}_{\mathrm{ext}} \longrightarrow \mathrm{metoh}_{\mathrm{urine}}$ |
| $v_{\mathrm{MAMEX}}$ | `MAMEX` | metoprolol acid renal excretion | $\mathrm{mam}_{\mathrm{ext}} \longrightarrow \mathrm{mam}_{\mathrm{urine}}$ |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{METEX}} &= \frac{\mathrm{GFR} \cdot 0.001 \cdot \mathrm{fup}_{\mathrm{met}} \cdot \mathrm{METEX}_{\mathrm{f}} \cdot \mathrm{met}_{\mathrm{ext}}}{\mathrm{BP}_{\mathrm{met}}} \\[1ex]
v_{\mathrm{METOHEX}} &= \mathrm{GFR} \cdot 0.001 \cdot \mathrm{METOHEX}_{\mathrm{f}} \cdot \mathrm{metoh}_{\mathrm{ext}} \\[1ex]
v_{\mathrm{MAMEX}} &= \mathrm{GFR} \cdot 0.001 \cdot \mathrm{MAMEX}_{\mathrm{f}} \cdot \mathrm{mam}_{\mathrm{ext}}
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{met}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{METEX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{metoh}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{METOHEX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{mam}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{MAMEX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{met}_{\mathrm{urine}}}{\mathrm{d} t} &= v_{\mathrm{METEX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{metoh}_{\mathrm{urine}}}{\mathrm{d} t} &= v_{\mathrm{METOHEX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{mam}_{\mathrm{urine}}}{\mathrm{d} t} &= v_{\mathrm{MAMEX}}
\end{aligned}
$$
