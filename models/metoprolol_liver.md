# Metoprolol liver model

Model `metoprolol_liver`, SBML Level 3 Version 1, read from metoprolol\_liver.xml, written by sbmlode 0.3.0.

Metoprolol liver model

Metoprolol is a lipophilic, highly permeable drug (BCS class I). It equilibrates fast between the blood of the liver and the hepatocytes (METIM), its hepatic clearance is set by the enzymes. The metabolism has three routes \[Article:2222517\]\[Article:30087611\]:

alpha-hydroxylation to alpha-hydroxymetoprolol (METOH), specific for CYP2D6; about 10 % of a dose are excreted as alpha-hydroxymetoprolol in the urine of extensive metabolizers, less than 1 % in poor metabolizers (Lennard1982, Kirchheiner2004).

O-demethylation and the oxidation to metoprolol acid by CYP2D6 (ODM2D6), the main route (60-65 % of a dose in the urine as metoprolol acid).

O-demethylation by other enzymes (CYP3A4, CYP2B6, CYP2C9; ODM), the clearance of poor metabolizers (Kirchheiner2004: the systemic clearance is 30.6 l/hr without an active CYP2D6 gene and increases by 20.9 l/hr per active gene).

The N-dealkylation (about 10 %) is part of the O-demethylation, its products are counted as metoprolol acid. The CYP2D6 reactions scale with the activity of the CYP2D6 diplotype (f\_cyp2d6 = cyp2d6\_activity/2, 1 for \*1/\*1), see the model of the CYP2D6 activity. The concentrations of the liver model are blood concentrations, the intrinsic clearances are clearances of blood.

\[Ruedesheim2020\] Km(met, → OH-M &amp; ODM) = 10 \[8.8-12.4\] µM \[Madani1999\] Km(met → OH-M &amp; ODM) = 26 +/- 9 µM (in liver) \[Yang2019\] Km(met, → OH-M &amp; ODM) = 11.31 ± 1.21 µM \[Kim1991\] Km(met, → OH-M &amp; ODM) = 20 \[15.6-26.0\] µM

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
| $\mathrm{Vli}$ | `Vli` | liver | $1.5$ | l | ✓ |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{met}_{\mathrm{ext}}$ | `met_ext` | metoprolol (blood) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{metoh}_{\mathrm{ext}}$ | `metoh_ext` | alpha-hydroxymetoprolol (blood) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{mam}_{\mathrm{ext}}$ | `mam_ext` | metoprolol acid (blood) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{met}$ | `met` | metoprolol (liver) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |
| $\mathrm{metoh}$ | `metoh` | alpha-hydroxymetoprolol (liver) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |
| $\mathrm{mam}$ | `mam` | metoprolol acid (liver) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $\mathrm{cyp2d6}_{\mathrm{a0}}$ | `cyp2d6_a0` | \*1 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a1}}$ | `cyp2d6_a1` | \*10 activity | $0.25$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a2}}$ | `cyp2d6_a2` | \*100 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a3}}$ | `cyp2d6_a3` | \*101 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a4}}$ | `cyp2d6_a4` | \*10x2 activity | $0.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a5}}$ | `cyp2d6_a5` | \*11 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a6}}$ | `cyp2d6_a6` | \*114 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a7}}$ | `cyp2d6_a7` | \*12 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a8}}$ | `cyp2d6_a8` | \*120 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a9}}$ | `cyp2d6_a9` | \*124 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a10}}$ | `cyp2d6_a10` | \*129 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a11}}$ | `cyp2d6_a11` | \*13 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a12}}$ | `cyp2d6_a12` | \*14 activity | $0.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a13}}$ | `cyp2d6_a13` | \*15 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a14}}$ | `cyp2d6_a14` | \*17 activity | $0.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a15}}$ | `cyp2d6_a15` | \*17x2 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a16}}$ | `cyp2d6_a16` | \*18 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a17}}$ | `cyp2d6_a17` | \*19 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a18}}$ | `cyp2d6_a18` | \*1x2 activity | $2$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a19}}$ | `cyp2d6_a19` | \*1x3 activity | $3$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a20}}$ | `cyp2d6_a20` | \*1x4 activity | $4$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a21}}$ | `cyp2d6_a21` | \*1x5 activity | $5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a22}}$ | `cyp2d6_a22` | \*1x6 activity | $6$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a23}}$ | `cyp2d6_a23` | \*2 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a24}}$ | `cyp2d6_a24` | \*20 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a25}}$ | `cyp2d6_a25` | \*21 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a26}}$ | `cyp2d6_a26` | \*27 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a27}}$ | `cyp2d6_a27` | \*29 activity | $0.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a28}}$ | `cyp2d6_a28` | \*29x2 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a29}}$ | `cyp2d6_a29` | \*2x2 activity | $2$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a30}}$ | `cyp2d6_a30` | \*2x3 activity | $3$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a31}}$ | `cyp2d6_a31` | \*2x4 activity | $4$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a32}}$ | `cyp2d6_a32` | \*2x5 activity | $5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a33}}$ | `cyp2d6_a33` | \*2x6 activity | $6$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a34}}$ | `cyp2d6_a34` | \*3 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a35}}$ | `cyp2d6_a35` | \*31 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a36}}$ | `cyp2d6_a36` | \*33 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a37}}$ | `cyp2d6_a37` | \*34 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a38}}$ | `cyp2d6_a38` | \*35 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a39}}$ | `cyp2d6_a39` | \*35x2 activity | $2$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a40}}$ | `cyp2d6_a40` | \*36 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a41}}$ | `cyp2d6_a41` | \*36x2 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a42}}$ | `cyp2d6_a42` | \*38 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a43}}$ | `cyp2d6_a43` | \*39 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a44}}$ | `cyp2d6_a44` | \*3x2 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a45}}$ | `cyp2d6_a45` | \*4 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a46}}$ | `cyp2d6_a46` | \*40 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a47}}$ | `cyp2d6_a47` | \*41 activity | $0.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a48}}$ | `cyp2d6_a48` | \*41x2 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a49}}$ | `cyp2d6_a49` | \*41x3 activity | $1.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a50}}$ | `cyp2d6_a50` | \*42 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a51}}$ | `cyp2d6_a51` | \*44 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a52}}$ | `cyp2d6_a52` | \*45 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a53}}$ | `cyp2d6_a53` | \*45x2 activity | $2$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a54}}$ | `cyp2d6_a54` | \*46 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a55}}$ | `cyp2d6_a55` | \*47 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a56}}$ | `cyp2d6_a56` | \*48 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a57}}$ | `cyp2d6_a57` | \*49 activity | $0.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a58}}$ | `cyp2d6_a58` | \*4x2 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a59}}$ | `cyp2d6_a59` | \*4x3 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a60}}$ | `cyp2d6_a60` | \*4x4 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a61}}$ | `cyp2d6_a61` | \*4x5 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a62}}$ | `cyp2d6_a62` | \*5 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a63}}$ | `cyp2d6_a63` | \*50 activity | $0.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a64}}$ | `cyp2d6_a64` | \*51 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a65}}$ | `cyp2d6_a65` | \*53 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a66}}$ | `cyp2d6_a66` | \*54 activity | $0.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a67}}$ | `cyp2d6_a67` | \*55 activity | $0.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a68}}$ | `cyp2d6_a68` | \*56 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a69}}$ | `cyp2d6_a69` | \*57 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a70}}$ | `cyp2d6_a70` | \*59 activity | $0.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a71}}$ | `cyp2d6_a71` | \*6 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a72}}$ | `cyp2d6_a72` | \*60 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a73}}$ | `cyp2d6_a73` | \*62 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a74}}$ | `cyp2d6_a74` | \*68 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a75}}$ | `cyp2d6_a75` | \*69 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a76}}$ | `cyp2d6_a76` | \*6x2 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a77}}$ | `cyp2d6_a77` | \*7 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a78}}$ | `cyp2d6_a78` | \*8 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a79}}$ | `cyp2d6_a79` | \*81 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a80}}$ | `cyp2d6_a80` | \*9 activity | $0.5$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a81}}$ | `cyp2d6_a81` | \*92 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a82}}$ | `cyp2d6_a82` | \*96 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a83}}$ | `cyp2d6_a83` | \*99 activity | $0$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{a84}}$ | `cyp2d6_a84` | \*9x2 activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{ac}}$ | `cyp2d6_ac` | custom allele activity | $1$ | \- | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{allele1}}$ | `cyp2d6_allele1` | allele 1 | $0$ | \- |  |
| $\mathrm{cyp2d6}_{\mathrm{allele2}}$ | `cyp2d6_allele2` | allele 2 | $0$ | \- |  |
| $\mathrm{cyp2d6}_{\mathrm{activity1}}$ | `cyp2d6_activity1` | activity of allele 1 |  | \- |  |
| $\mathrm{cyp2d6}_{\mathrm{activity2}}$ | `cyp2d6_activity2` | activity of allele 2 |  | \- |  |
| $f_{\mathrm{cyp2d6}}$ | `f_cyp2d6` | CYP2D6 activity relative to \*1/\*1 |  | \- |  |
| $\mathrm{CYP2D6}_{\mathrm{Km\_met}}$ | `CYP2D6_Km_met` | Km of metoprolol for CYP2D6 | $0.015$ | mmol/l | ✓ |
| $\mathrm{METOH}_{\mathrm{Vmax}}$ | `METOH_Vmax` | Vmax of the alpha-hydroxylation (CYP2D6, \*1/\*1) | $0.00230494292103704$ | mmol/min/l | ✓ |
| $\mathrm{ODM2D6}_{\mathrm{Vmax}}$ | `ODM2D6_Vmax` | Vmax of the O-demethylation by CYP2D6 (\*1/\*1) | $0.012600231875494$ | mmol/min/l | ✓ |
| $\mathrm{ODM}_{\mathrm{Vmax}}$ | `ODM_Vmax` | Vmax of the O-demethylation by other enzymes than CYP2D6 | $0.00158382422456946$ | mmol/min/l | ✓ |
| $\mathrm{ODM}_{\mathrm{Km\_met}}$ | `ODM_Km_met` | Km of metoprolol for the O-demethylation by other enzymes | $0.015$ | mmol/l | ✓ |
| $\mathrm{METIM}_{\mathrm{k}}$ | `METIM_k` | rate of the metoprolol exchange of the liver | $100$ | 1/min | ✓ |
| $\mathrm{METOHEX}_{\mathrm{k}}$ | `METOHEX_k` | rate of the alpha-hydroxymetoprolol export | $100$ | 1/min | ✓ |
| $\mathrm{MAMEX}_{\mathrm{k}}$ | `MAMEX_k` | rate of the metoprolol acid export | $100$ | 1/min | ✓ |
| $\mathrm{cyp2d6}_{\mathrm{activity}}$ | `cyp2d6_activity` | activity of CYP2D6 diplotype |  | \- |  |

## Initial assignments and assignment rules

The assignment rules hold at every time $t$:

$$
\begin{aligned}
\mathrm{cyp2d6}_{\mathrm{activity1}} &= \begin{cases} \frac{\mathrm{cyp2d6}_{\mathrm{ac}}}{2} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = -1 \\ \mathrm{cyp2d6}_{\mathrm{a0}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 0 \\ \mathrm{cyp2d6}_{\mathrm{a1}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 1 \\ \mathrm{cyp2d6}_{\mathrm{a2}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 2 \\ \mathrm{cyp2d6}_{\mathrm{a3}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 3 \\ \mathrm{cyp2d6}_{\mathrm{a4}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 4 \\ \mathrm{cyp2d6}_{\mathrm{a5}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 5 \\ \mathrm{cyp2d6}_{\mathrm{a6}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 6 \\ \mathrm{cyp2d6}_{\mathrm{a7}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 7 \\ \mathrm{cyp2d6}_{\mathrm{a8}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 8 \\ \mathrm{cyp2d6}_{\mathrm{a9}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 9 \\ \mathrm{cyp2d6}_{\mathrm{a10}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 10 \\ \mathrm{cyp2d6}_{\mathrm{a11}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 11 \\ \mathrm{cyp2d6}_{\mathrm{a12}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 12 \\ \mathrm{cyp2d6}_{\mathrm{a13}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 13 \\ \mathrm{cyp2d6}_{\mathrm{a14}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 14 \\ \mathrm{cyp2d6}_{\mathrm{a15}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 15 \\ \mathrm{cyp2d6}_{\mathrm{a16}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 16 \\ \mathrm{cyp2d6}_{\mathrm{a17}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 17 \\ \mathrm{cyp2d6}_{\mathrm{a18}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 18 \\ \mathrm{cyp2d6}_{\mathrm{a19}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 19 \\ \mathrm{cyp2d6}_{\mathrm{a20}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 20 \\ \mathrm{cyp2d6}_{\mathrm{a21}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 21 \\ \mathrm{cyp2d6}_{\mathrm{a22}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 22 \\ \mathrm{cyp2d6}_{\mathrm{a23}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 23 \\ \mathrm{cyp2d6}_{\mathrm{a24}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 24 \\ \mathrm{cyp2d6}_{\mathrm{a25}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 25 \\ \mathrm{cyp2d6}_{\mathrm{a26}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 26 \\ \mathrm{cyp2d6}_{\mathrm{a27}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 27 \\ \mathrm{cyp2d6}_{\mathrm{a28}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 28 \\ \mathrm{cyp2d6}_{\mathrm{a29}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 29 \\ \mathrm{cyp2d6}_{\mathrm{a30}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 30 \\ \mathrm{cyp2d6}_{\mathrm{a31}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 31 \\ \mathrm{cyp2d6}_{\mathrm{a32}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 32 \\ \mathrm{cyp2d6}_{\mathrm{a33}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 33 \\ \mathrm{cyp2d6}_{\mathrm{a34}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 34 \\ \mathrm{cyp2d6}_{\mathrm{a35}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 35 \\ \mathrm{cyp2d6}_{\mathrm{a36}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 36 \\ \mathrm{cyp2d6}_{\mathrm{a37}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 37 \\ \mathrm{cyp2d6}_{\mathrm{a38}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 38 \\ \mathrm{cyp2d6}_{\mathrm{a39}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 39 \\ \mathrm{cyp2d6}_{\mathrm{a40}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 40 \\ \mathrm{cyp2d6}_{\mathrm{a41}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 41 \\ \mathrm{cyp2d6}_{\mathrm{a42}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 42 \\ \mathrm{cyp2d6}_{\mathrm{a43}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 43 \\ \mathrm{cyp2d6}_{\mathrm{a44}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 44 \\ \mathrm{cyp2d6}_{\mathrm{a45}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 45 \\ \mathrm{cyp2d6}_{\mathrm{a46}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 46 \\ \mathrm{cyp2d6}_{\mathrm{a47}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 47 \\ \mathrm{cyp2d6}_{\mathrm{a48}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 48 \\ \mathrm{cyp2d6}_{\mathrm{a49}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 49 \\ \mathrm{cyp2d6}_{\mathrm{a50}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 50 \\ \mathrm{cyp2d6}_{\mathrm{a51}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 51 \\ \mathrm{cyp2d6}_{\mathrm{a52}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 52 \\ \mathrm{cyp2d6}_{\mathrm{a53}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 53 \\ \mathrm{cyp2d6}_{\mathrm{a54}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 54 \\ \mathrm{cyp2d6}_{\mathrm{a55}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 55 \\ \mathrm{cyp2d6}_{\mathrm{a56}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 56 \\ \mathrm{cyp2d6}_{\mathrm{a57}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 57 \\ \mathrm{cyp2d6}_{\mathrm{a58}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 58 \\ \mathrm{cyp2d6}_{\mathrm{a59}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 59 \\ \mathrm{cyp2d6}_{\mathrm{a60}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 60 \\ \mathrm{cyp2d6}_{\mathrm{a61}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 61 \\ \mathrm{cyp2d6}_{\mathrm{a62}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 62 \\ \mathrm{cyp2d6}_{\mathrm{a63}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 63 \\ \mathrm{cyp2d6}_{\mathrm{a64}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 64 \\ \mathrm{cyp2d6}_{\mathrm{a65}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 65 \\ \mathrm{cyp2d6}_{\mathrm{a66}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 66 \\ \mathrm{cyp2d6}_{\mathrm{a67}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 67 \\ \mathrm{cyp2d6}_{\mathrm{a68}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 68 \\ \mathrm{cyp2d6}_{\mathrm{a69}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 69 \\ \mathrm{cyp2d6}_{\mathrm{a70}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 70 \\ \mathrm{cyp2d6}_{\mathrm{a71}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 71 \\ \mathrm{cyp2d6}_{\mathrm{a72}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 72 \\ \mathrm{cyp2d6}_{\mathrm{a73}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 73 \\ \mathrm{cyp2d6}_{\mathrm{a74}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 74 \\ \mathrm{cyp2d6}_{\mathrm{a75}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 75 \\ \mathrm{cyp2d6}_{\mathrm{a76}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 76 \\ \mathrm{cyp2d6}_{\mathrm{a77}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 77 \\ \mathrm{cyp2d6}_{\mathrm{a78}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 78 \\ \mathrm{cyp2d6}_{\mathrm{a79}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 79 \\ \mathrm{cyp2d6}_{\mathrm{a80}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 80 \\ \mathrm{cyp2d6}_{\mathrm{a81}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 81 \\ \mathrm{cyp2d6}_{\mathrm{a82}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 82 \\ \mathrm{cyp2d6}_{\mathrm{a83}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 83 \\ \mathrm{cyp2d6}_{\mathrm{a84}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele1}} = 84 \\ \frac{\mathrm{cyp2d6}_{\mathrm{ac}}}{2} & \text{otherwise} \end{cases} \\[1ex]
\mathrm{cyp2d6}_{\mathrm{activity2}} &= \begin{cases} \frac{\mathrm{cyp2d6}_{\mathrm{ac}}}{2} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = -1 \\ \mathrm{cyp2d6}_{\mathrm{a0}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 0 \\ \mathrm{cyp2d6}_{\mathrm{a1}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 1 \\ \mathrm{cyp2d6}_{\mathrm{a2}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 2 \\ \mathrm{cyp2d6}_{\mathrm{a3}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 3 \\ \mathrm{cyp2d6}_{\mathrm{a4}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 4 \\ \mathrm{cyp2d6}_{\mathrm{a5}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 5 \\ \mathrm{cyp2d6}_{\mathrm{a6}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 6 \\ \mathrm{cyp2d6}_{\mathrm{a7}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 7 \\ \mathrm{cyp2d6}_{\mathrm{a8}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 8 \\ \mathrm{cyp2d6}_{\mathrm{a9}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 9 \\ \mathrm{cyp2d6}_{\mathrm{a10}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 10 \\ \mathrm{cyp2d6}_{\mathrm{a11}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 11 \\ \mathrm{cyp2d6}_{\mathrm{a12}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 12 \\ \mathrm{cyp2d6}_{\mathrm{a13}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 13 \\ \mathrm{cyp2d6}_{\mathrm{a14}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 14 \\ \mathrm{cyp2d6}_{\mathrm{a15}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 15 \\ \mathrm{cyp2d6}_{\mathrm{a16}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 16 \\ \mathrm{cyp2d6}_{\mathrm{a17}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 17 \\ \mathrm{cyp2d6}_{\mathrm{a18}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 18 \\ \mathrm{cyp2d6}_{\mathrm{a19}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 19 \\ \mathrm{cyp2d6}_{\mathrm{a20}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 20 \\ \mathrm{cyp2d6}_{\mathrm{a21}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 21 \\ \mathrm{cyp2d6}_{\mathrm{a22}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 22 \\ \mathrm{cyp2d6}_{\mathrm{a23}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 23 \\ \mathrm{cyp2d6}_{\mathrm{a24}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 24 \\ \mathrm{cyp2d6}_{\mathrm{a25}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 25 \\ \mathrm{cyp2d6}_{\mathrm{a26}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 26 \\ \mathrm{cyp2d6}_{\mathrm{a27}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 27 \\ \mathrm{cyp2d6}_{\mathrm{a28}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 28 \\ \mathrm{cyp2d6}_{\mathrm{a29}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 29 \\ \mathrm{cyp2d6}_{\mathrm{a30}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 30 \\ \mathrm{cyp2d6}_{\mathrm{a31}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 31 \\ \mathrm{cyp2d6}_{\mathrm{a32}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 32 \\ \mathrm{cyp2d6}_{\mathrm{a33}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 33 \\ \mathrm{cyp2d6}_{\mathrm{a34}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 34 \\ \mathrm{cyp2d6}_{\mathrm{a35}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 35 \\ \mathrm{cyp2d6}_{\mathrm{a36}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 36 \\ \mathrm{cyp2d6}_{\mathrm{a37}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 37 \\ \mathrm{cyp2d6}_{\mathrm{a38}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 38 \\ \mathrm{cyp2d6}_{\mathrm{a39}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 39 \\ \mathrm{cyp2d6}_{\mathrm{a40}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 40 \\ \mathrm{cyp2d6}_{\mathrm{a41}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 41 \\ \mathrm{cyp2d6}_{\mathrm{a42}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 42 \\ \mathrm{cyp2d6}_{\mathrm{a43}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 43 \\ \mathrm{cyp2d6}_{\mathrm{a44}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 44 \\ \mathrm{cyp2d6}_{\mathrm{a45}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 45 \\ \mathrm{cyp2d6}_{\mathrm{a46}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 46 \\ \mathrm{cyp2d6}_{\mathrm{a47}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 47 \\ \mathrm{cyp2d6}_{\mathrm{a48}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 48 \\ \mathrm{cyp2d6}_{\mathrm{a49}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 49 \\ \mathrm{cyp2d6}_{\mathrm{a50}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 50 \\ \mathrm{cyp2d6}_{\mathrm{a51}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 51 \\ \mathrm{cyp2d6}_{\mathrm{a52}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 52 \\ \mathrm{cyp2d6}_{\mathrm{a53}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 53 \\ \mathrm{cyp2d6}_{\mathrm{a54}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 54 \\ \mathrm{cyp2d6}_{\mathrm{a55}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 55 \\ \mathrm{cyp2d6}_{\mathrm{a56}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 56 \\ \mathrm{cyp2d6}_{\mathrm{a57}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 57 \\ \mathrm{cyp2d6}_{\mathrm{a58}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 58 \\ \mathrm{cyp2d6}_{\mathrm{a59}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 59 \\ \mathrm{cyp2d6}_{\mathrm{a60}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 60 \\ \mathrm{cyp2d6}_{\mathrm{a61}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 61 \\ \mathrm{cyp2d6}_{\mathrm{a62}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 62 \\ \mathrm{cyp2d6}_{\mathrm{a63}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 63 \\ \mathrm{cyp2d6}_{\mathrm{a64}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 64 \\ \mathrm{cyp2d6}_{\mathrm{a65}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 65 \\ \mathrm{cyp2d6}_{\mathrm{a66}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 66 \\ \mathrm{cyp2d6}_{\mathrm{a67}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 67 \\ \mathrm{cyp2d6}_{\mathrm{a68}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 68 \\ \mathrm{cyp2d6}_{\mathrm{a69}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 69 \\ \mathrm{cyp2d6}_{\mathrm{a70}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 70 \\ \mathrm{cyp2d6}_{\mathrm{a71}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 71 \\ \mathrm{cyp2d6}_{\mathrm{a72}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 72 \\ \mathrm{cyp2d6}_{\mathrm{a73}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 73 \\ \mathrm{cyp2d6}_{\mathrm{a74}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 74 \\ \mathrm{cyp2d6}_{\mathrm{a75}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 75 \\ \mathrm{cyp2d6}_{\mathrm{a76}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 76 \\ \mathrm{cyp2d6}_{\mathrm{a77}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 77 \\ \mathrm{cyp2d6}_{\mathrm{a78}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 78 \\ \mathrm{cyp2d6}_{\mathrm{a79}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 79 \\ \mathrm{cyp2d6}_{\mathrm{a80}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 80 \\ \mathrm{cyp2d6}_{\mathrm{a81}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 81 \\ \mathrm{cyp2d6}_{\mathrm{a82}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 82 \\ \mathrm{cyp2d6}_{\mathrm{a83}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 83 \\ \mathrm{cyp2d6}_{\mathrm{a84}} & \text{if } \mathrm{cyp2d6}_{\mathrm{allele2}} = 84 \\ \frac{\mathrm{cyp2d6}_{\mathrm{ac}}}{2} & \text{otherwise} \end{cases} \\[1ex]
\mathrm{cyp2d6}_{\mathrm{activity}} &= \mathrm{cyp2d6}_{\mathrm{activity1}} + \mathrm{cyp2d6}_{\mathrm{activity2}} \\[1ex]
f_{\mathrm{cyp2d6}} &= \frac{\mathrm{cyp2d6}_{\mathrm{activity}}}{2}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation |
| --- | --- | --- | --- |
| $v_{\mathrm{METIM}}$ | `METIM` | metoprolol exchange (blood, hepatocyte) | $\mathrm{met}_{\mathrm{ext}} \rightleftharpoons \mathrm{met}$ |
| $v_{\mathrm{METOH}}$ | `METOH` | alpha-hydroxylation of metoprolol (CYP2D6) | $\mathrm{met} \longrightarrow \mathrm{metoh}$ |
| $v_{\mathrm{ODM2D6}}$ | `ODM2D6` | O-demethylation of metoprolol (CYP2D6) | $\mathrm{met} \longrightarrow \mathrm{mam}$ |
| $v_{\mathrm{ODM}}$ | `ODM` | O-demethylation of metoprolol (other enzymes) | $\mathrm{met} \longrightarrow \mathrm{mam}$ |
| $v_{\mathrm{METOHEX}}$ | `METOHEX` | alpha-hydroxymetoprolol export | $\mathrm{metoh} \rightleftharpoons \mathrm{metoh}_{\mathrm{ext}}$ |
| $v_{\mathrm{MAMEX}}$ | `MAMEX` | metoprolol acid export | $\mathrm{mam} \rightleftharpoons \mathrm{mam}_{\mathrm{ext}}$ |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{METIM}} &= \mathrm{METIM}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathopen{}\left(\mathrm{met}_{\mathrm{ext}} - \mathrm{met}\right) \\[1ex]
v_{\mathrm{METOH}} &= \frac{f_{\mathrm{cyp2d6}} \cdot \mathrm{METOH}_{\mathrm{Vmax}} \cdot \mathrm{Vli} \cdot \mathrm{met}}{\mathrm{CYP2D6}_{\mathrm{Km\_met}} + \mathrm{met}} \\[1ex]
v_{\mathrm{ODM2D6}} &= \frac{f_{\mathrm{cyp2d6}} \cdot \mathrm{ODM2D6}_{\mathrm{Vmax}} \cdot \mathrm{Vli} \cdot \mathrm{met}}{\mathrm{CYP2D6}_{\mathrm{Km\_met}} + \mathrm{met}} \\[1ex]
v_{\mathrm{ODM}} &= \frac{\mathrm{ODM}_{\mathrm{Vmax}} \cdot \mathrm{Vli} \cdot \mathrm{met}}{\mathrm{ODM}_{\mathrm{Km\_met}} + \mathrm{met}} \\[1ex]
v_{\mathrm{METOHEX}} &= \mathrm{METOHEX}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathopen{}\left(\mathrm{metoh} - \mathrm{metoh}_{\mathrm{ext}}\right) \\[1ex]
v_{\mathrm{MAMEX}} &= \mathrm{MAMEX}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathopen{}\left(\mathrm{mam} - \mathrm{mam}_{\mathrm{ext}}\right)
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{met}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{METIM}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{metoh}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{v_{\mathrm{METOHEX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{mam}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{v_{\mathrm{MAMEX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{met}}{\mathrm{d} t} &= \frac{v_{\mathrm{METIM}} - v_{\mathrm{METOH}} - v_{\mathrm{ODM2D6}} - v_{\mathrm{ODM}}}{\mathrm{Vli}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{metoh}}{\mathrm{d} t} &= \frac{v_{\mathrm{METOH}} - v_{\mathrm{METOHEX}}}{\mathrm{Vli}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{mam}}{\mathrm{d} t} &= \frac{v_{\mathrm{ODM2D6}} + v_{\mathrm{ODM}} - v_{\mathrm{MAMEX}}}{\mathrm{Vli}}
\end{aligned}
$$
