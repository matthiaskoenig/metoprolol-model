#set page(paper: "a4", margin: 2cm)
#set text(size: 10pt)
#set heading(numbering: "1.1")
#set math.equation(numbering: "(1)")
// a table longer than a page continues on the next page, its
// caption above it and its header repeated
#show figure.where(kind: table): set block(breakable: true)
#show figure.where(kind: table): set figure.caption(position: top)

#align(center, text(size: 16pt, weight: "bold")[Metoprolol PBPK\/PD model: fit PD])

= Methods: Metoprolol PBPK\/PD model: fit PD

== Parameters and data

2 parameters were optimized: maximal relative reduction of the heart rate (#raw("HRred_Emax")) and metoprolol plasma concentration of the half-maximal reduction (#raw("HRred_EC50")). The parameters of the adopted fit PK\_20261017\_183259\_\_fc82a were fixed at their fitted values.

A fit mapping is a curve of a study, the data and the observable of the model it is compared with. The fit has 15 fit mappings of training data with 81 data points, whose residuals enter the objective; and 4 fit mappings of validation data with 15 data points, which were simulated and evaluated with the fitted parameters but not fitted. The fit was set up and run with sbmlsim #cite(<Koenig2026_sbmlsim>).

== Objective function

The parameters were estimated by minimizing the objective function

$ F(arrow(p)) = 1/2 sum_k sum_i rho(w_(i,k) r_(i,k)(arrow(p))^2) $

where $k$ runs over the fit mappings of the training data and $i$ over their data points, $r_(i,k)$ is the residual, $w_(i,k) = w_k w^p_(i,k)$ the weight of the data point and $rho$ the loss function, applied to the squared weighted residual $z = w_(i,k) r_(i,k)^2$. The loss function is linear, $rho(z) = z$, i.e. a standard least squares problem.

The residuals are normalized by the mean $overline(y)_k$ of the data of their curve, which makes curves of different quantities and magnitudes comparable:

$ r_(i,k) = (y_(i,k) - f_k(x_(i,k), arrow(p))) / overline(y)_k $

The weight of curve $k$ is $w_k = n_k / N_k$, the weight $n_k$ of its fit mapping (the weight its fit mapping collection assigns, 1 by default, or, for a collection which uses the weights of its mappings, the weight of the mapping, by default the number of subjects of its data) divided by the number $N_k$ of its data points.

A data point is weighted with the inverse of its coefficient of variation, $w^p_(i,k) = |y_(i,k)| / sigma_(i,k)$, with $sigma_(i,k)$ the standard deviation of the data point, or its standard error for data without a standard deviation. An error of zero is missing, a missing error of a curve with errors is replaced by the largest error of the curve, and the data points of a curve without errors have the weight $w^p_(i,k) = 2$, the weight of a coefficient of variation of 0.5.

== Optimization

The optimizer searched the parameters in log10 space within their bounds; bounds, values and intervals are given in the units of the fit parameters, the units of the table of the parameters.

The objective was minimized in 3 runs with differential evolution #cite(<Storn1997>) of SciPy #cite(<Virtanen2020>) within the bounds of the parameters, with the strategy #raw("best1bin"), a population of 15 times the number of parameters, at most 1000 generations, the relative tolerance 0.01 of convergence, the recombination constant 0.7 and a mutation dithered between 0.5 and 1. The initial population of a run was drawn by latin hypercube sampling #cite(<McKay1979>), with a seed of every run derived from the seed 1234 of the fit. The best member of the final population was polished with the L-BFGS-B method of SciPy.

The convergence of the runs was assessed from the traces of their cost and the waterfall plot of their final costs, and the parameter set with the lowest cost was used.

The models were simulated with libRoadRunner #cite(<Welsh2023>) and its integrator CVODE #cite(<Hindmarsh2005>) with the relative tolerance $10^(-6)$ and the absolute tolerances $10^(-11)$ of an amount, $10^(-11)$ of a concentration and $10^(-6)$ of the other states, which for a species in a concentration is multiplied by the initial volume of its compartment. It ran with the variable step size of libRoadRunner, i.e. with an output at every step of the integrator. A data point at the time of a change after the start of a simulation, e.g. a dose or the reset of a collection, was compared with the state before the change, except the first data point of a curve with data at later times, which starts a collection and was compared with the state after the change.

== Goodness of fit

The goodness of fit is given per kind of data (training data and validation data) by metrics over its $n$ data points with the residuals $e_i = y_i - f(x_i, hat(arrow(p)))$ at the fitted parameters $hat(arrow(p))$, the mean squared error, its root and the root mean squared error normalized by the mean $overline(y)_(k(i))$ of the data of the curve of a point:

$ "MSE" = 1/n sum_(i=1)^n e_i^2, quad "RMSE" = sqrt("MSE"), quad "NRMSE" = sqrt(1/n sum_(i=1)^n (e_i / overline(y)_(k(i)))^2) $

The root mean square of the residuals of the objective, i.e. what the fit minimizes, and the coefficient of determination:

$ "RMSE"_w = sqrt(1/n sum_(i=1)^n rho(w_i r_i^2)), quad R^2 = 1 - (sum_i e_i^2) / (sum_i (y_i - overline(y))^2) $

The predictions of a non-linear model are no linear regression of the data, so $R^2$ can be negative: the prediction is worse than the mean of the data. The information criteria of Akaike #cite(<Akaike1974>) and Schwarz #cite(<Schwarz1978>) with the number $n_p$ of fitted parameters are those of a least squares fit with normally distributed residuals, up to an additive constant, so only differences between models fitted to the same data are meaningful:

$ "AIC" = n ln("MSE") + 2 n_p, quad "BIC" = n ln("MSE") + n_p ln(n) $

The percentage of the data points whose prediction $f_i = f(x_i, hat(arrow(p)))$ lies within twofold of the data is taken over the $n_(+)$ data points with positive data $y_i > 0$ and a positive prediction $f_i > 0$; the others have no ratio and are not counted, and a kind of data without such a point has no percentage:

$ P_2 = 100 / n_(+) abs(\{ i : 1/2 <= f_i / y_i <= 2 \}) $

The goodness of fit plot shows the predictions against the data on logarithmic axes, with the lines of twofold $f = 2y$ and $f = y/2$. The Bland-Altman plot #cite(<Bland1986>) shows the ratio of prediction and data as $d_i = log_10(f_i / y_i)$ against the geometric mean $sqrt(f_i y_i)$ for the data points with positive values, with the bias $overline(d)$ and the limits of agreement $overline(d) plus.minus 1.96 s_d$, with the sample standard deviation $s_d$ of $d_i$, of the training data; they are read as the fold factors $10^(overline(d))$ and $10^(overline(d) plus.minus 1.96 s_d)$.

== Identifiability

The identifiability of the parameters was analysed with the profile likelihood #cite(<Raue2009>) #cite(<Kreutz2013>). The profile of a parameter is the lowest objective with the parameter fixed:

$ "PL"(p_j) = min_(p_(l != j)) F(arrow(p)) $

At every point of a scan the other parameters were re-optimized from the previous point with the least squares optimizer of SciPy with the relative step 0.05. A scan ran from the optimum in both directions in the space of the optimizer, with steps in decades of the parameter, starting at 0.1. A step which raised the objective by more than 0.2 of the distance between the objective at the optimum and the threshold was reduced by the factor 2 and repeated, down to 0.01, and the step after one which raised it by less than that divided by the factor was enlarged by the factor, up to 1. A scan stopped at the threshold, at the bound of the parameter, at a point which failed or after 50 points.

The confidence intervals are the values at which the profile crosses the threshold of the likelihood ratio test

$ F_"thr" = F_"min" + chi^2_alpha ("df") / 2 $

with $F_"min"$ the lowest objective of the fit and of all profiles and $chi^2_alpha ("df")$ the quantile of the $chi^2$ distribution at the confidence level $alpha = 0.95$ with df \= 1 degrees of freedom, i.e. 1.92 above the lowest objective. The threshold has this confidence level if $F$ is the negative log-likelihood of the data up to a constant, i.e. if the weighted residuals are independent and normally distributed with unit variance; otherwise the level is approximate. A crossing is interpolated between two points of the profile, on the logarithm of a parameter on a logarithmic scale. A parameter is identifiable if its profile reaches the threshold within the scan on both sides of the optimum, i.e. its confidence interval is finite; practically non-identifiable towards the lower bound if its profile reaches the threshold above the optimum but not below it within the scan, which ends at the lower bound or after 50 points; practically non-identifiable towards the upper bound if its profile reaches the threshold below the optimum but not above it within the scan, which ends at the upper bound or after 50 points; practically non-identifiable if its profile reaches the threshold on neither side within the scans, which end at the bounds or after 50 points, and is not flat; and structurally non-identifiable if its profile is flat on both sides. A side of a profile is flat if it rises by less than 0.05 of the distance between the lowest objective and the threshold, and a profile with a point which failed or did not converge is not classified. The profile likelihood is preferred over the intervals of the Fisher information, its intervals are invariant under a transformation of the parameters and can be asymmetric #cite(<Wieland2021>).

The Fisher information is the local alternative to the profiles: it is the Gauss-Newton approximation of the curvature of the objective at the optimum, from the Jacobian $J$ of the weighted residuals of the training data with respect to the parameters $arrow(p)$ in the space of the optimizer, computed by central finite differences with the step $h_j = epsilon max(|p_j|, 1), space epsilon = 10^(-6)$ of the parameter $p_j$:

$ I = J^top J, quad "cov" = sigma^2 I^(-1), quad sigma^2 = (2 F) / (n - n_p) $

with the number $n$ of data points of the training data and the number $n_p$ of parameters. The information has rank 2 of 2, the number of its eigenvalues above $10^(-8)$ of the largest one, and the condition number 67.5; the covariance of an information of a lower rank is computed with the pseudo-inverse. The Wald intervals are $hat(p)_j plus.minus t_((1+alpha)/2, n-n_p) "SE"_j$ with the standard errors $"SE"_j = sqrt("cov"_(j j))$ at the confidence level $alpha = 0.95$, transformed back into the units of the fit parameters.

== Provenance

The fit PD\_20261017\_193512\_\_e995e was run on 2026-10-17 17:35:16 UTC with sbmlsim 0.10.0 #cite(<Koenig2026_sbmlsim>), libRoadRunner 2.10.0 #cite(<Welsh2023>), SciPy 1.18.1 #cite(<Virtanen2020>), NumPy 2.5.3 #cite(<Harris2020>) and Python 3.14.4 (seed 1234). The models and data were those of commit #raw("c3d109c6e1cf45ce2a0d30b45c1386b1abb71399") of #raw("/home/mkoenig/git/pkdb_models-metoprolol"); their SHA-256 checksums are listed in #ref(<tab:checksums:PD_20261017_193512__e995e>). The fit kept the values #raw("Kp_met") \= 2.77928, #raw("ftissue_met") \= 45.799, #raw("LI__METOH_Vmax") \= 0.00230494, #raw("LI__ODM2D6_Vmax") \= 0.0126002, #raw("LI__ODM_Vmax") \= 0.00158382, #raw("KI__METEX_f") \= 0.81523, #raw("KI__METOHEX_f") \= 6.76476, #raw("KI__MAMEX_f") \= 1.53418, #raw("Kp_metoh") \= 1.76573, #raw("Ka_abs_met") \= 1.00038, #raw("Ka_dis_met") \= 2.5259, #raw("Ka_dis_sr_met") \= 0.257837, #raw("Ka_dis_cr_met") \= 0.0700335 and #raw("F_cr_met") \= 1 of the model fixed.

#figure(
  table(
  columns: 2,
  align: (left, left,),
  table.header([File], [SHA-256]),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Bae2014/.Bae2014_Fig3.tsv"),
  raw("2098988e813f..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Bae2014/.Bae2014_Tab4.tsv"),
  raw("7e83fb395bab..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Bae2014/.Bae2014_TabGroups.tsv"),
  raw("891751814b28..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Bae2014/.Bae2014_TabInterventions.tsv"),
  raw("f00c9ddd8575..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Blomqvist1988/.Blomqvist1988_Fig1.tsv"),
  raw("9b9a18fa0bd9..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Blomqvist1988/.Blomqvist1988_Fig2.tsv"),
  raw("51e6d9f52706..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Blomqvist1988/.Blomqvist1988_Tab1.tsv"),
  raw("cacc36aedc6d..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Blomqvist1988/.Blomqvist1988_Tab2.tsv"),
  raw("5a305808921c..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Blomqvist1988/.Blomqvist1988_TabGroups.tsv"),
  raw("a146f0bae479..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Blomqvist1988/.Blomqvist1988_TabInterventions.tsv"),
  raw("54ee8807c47d..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2003/.Cerqueira2003_Fig4.tsv"),
  raw("ad516e5d0342..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2003/.Cerqueira2003_Fig5.tsv"),
  raw("eed88234c426..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2003/.Cerqueira2003_Tab1.tsv"),
  raw("81f9b955e771..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2003/.Cerqueira2003_Tab6.tsv"),
  raw("6d974ba5502b..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2003/.Cerqueira2003_TabGroups.tsv"),
  raw("a69039e9d852..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2003/.Cerqueira2003_TabIndividuals.tsv"),
  raw("7092dd68c68d..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2003/.Cerqueira2003_TabInterventions.tsv"),
  raw("c2794bf78056..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2005/.Cerqueira2005_Fig2.tsv"),
  raw("7fcb2f80df04..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2005/.Cerqueira2005_Fig3.tsv"),
  raw("cb56eae7b115..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2005/.Cerqueira2005_Tab1.tsv"),
  raw("fe936ec349fe..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2005/.Cerqueira2005_Tab2.tsv"),
  raw("5ca017bb3120..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2005/.Cerqueira2005_Tab3.tsv"),
  raw("8951c6be2a90..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2005/.Cerqueira2005_Tab4.tsv"),
  raw("d463a1b76eda..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2005/.Cerqueira2005_Tab5.tsv"),
  raw("1a23dbdd9572..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2005/.Cerqueira2005_TabGroups.tsv"),
  raw("596361adfc0e..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2005/.Cerqueira2005_TabIndividuals.tsv"),
  raw("b7b806fe43aa..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Cerqueira2005/.Cerqueira2005_TabInterventions.tsv"),
  raw("df2cc6a93824..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Fux2005/.Fux2005_Fig2.tsv"),
  raw("938f136d171b..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Fux2005/.Fux2005_Tab2.tsv"),
  raw("724e38692d21..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Fux2005/.Fux2005_Tab4.tsv"),
  raw("c92d74acdc60..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Fux2005/.Fux2005_TabGroups.tsv"),
  raw("b4e8cd91e736..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Fux2005/.Fux2005_TabIndividuals.tsv"),
  raw("ea7e26e0f2cc..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Fux2005/.Fux2005_TabInterventions.tsv"),
  raw("15cc18e86af3..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Jin2008/.Jin2008_Fig1.tsv"),
  raw("221ab456e392..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Jin2008/.Jin2008_Fig2.tsv"),
  raw("d6a0faecd577..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Jin2008/.Jin2008_Fig3.tsv"),
  raw("7b0cbfcd04a7..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Jin2008/.Jin2008_Tab2.tsv"),
  raw("c1b2539b9869..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Jin2008/.Jin2008_TabGroups.tsv"),
  raw("078e211f43af..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Jin2008/.Jin2008_TabInterventions.tsv"),
  raw("551f33b26d8b..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Johnsson1975/.Johnsson1975_Fig2.tsv"),
  raw("cb0d76455ed8..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Johnsson1975/.Johnsson1975_Fig3.tsv"),
  raw("01e413621336..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Johnsson1975/.Johnsson1975_Fig4.tsv"),
  raw("6ada84626965..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Johnsson1975/.Johnsson1975_Fig5.tsv"),
  raw("87df1ac4bc82..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Johnsson1975/.Johnsson1975_Fig6.tsv"),
  raw("eada6338b151..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Johnsson1975/.Johnsson1975_Fig7.tsv"),
  raw("d2214cc1577c..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Johnsson1975/.Johnsson1975_Fig8.tsv"),
  raw("6f1057d6392e..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Johnsson1975/.Johnsson1975_Tab1.tsv"),
  raw("bf73e8176b46..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Johnsson1975/.Johnsson1975_TabGroups.tsv"),
  raw("af2b9fbd0567..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Johnsson1975/.Johnsson1975_TabIndividuals.tsv"),
  raw("bf641a1107f2..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Johnsson1975/.Johnsson1975_TabInterventions.tsv"),
  raw("2fbfbd05a398..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Kirchheiner2004/.Kirchheiner2004_Fig1.tsv"),
  raw("56dec4eb6f6f..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Kirchheiner2004/.Kirchheiner2004_Fig1Mean.tsv"),
  raw("d44b2233ebd5..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Kirchheiner2004/.Kirchheiner2004_Fig2.tsv"),
  raw("bb60ae687416..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Kirchheiner2004/.Kirchheiner2004_Fig3.tsv"),
  raw("5f44f41bbb09..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Kirchheiner2004/.Kirchheiner2004_Tab2.tsv"),
  raw("1a424874be04..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Kirchheiner2004/.Kirchheiner2004_Tab3.tsv"),
  raw("379d2879d35e..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Kirchheiner2004/.Kirchheiner2004_TabGroups.tsv"),
  raw("3804bda2618b..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Kirchheiner2004/.Kirchheiner2004_TabIndividuals.tsv"),
  raw("623986f0ae00..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Kirchheiner2004/.Kirchheiner2004_TabInterventions.tsv"),
  raw("54d81b6ec317..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Lennard1982/.Lennard1982_Fig1.tsv"),
  raw("956e3511e6c4..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Lennard1982/.Lennard1982_Fig2.tsv"),
  raw("ff3538972b69..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Lennard1982/.Lennard1982_TabGroups.tsv"),
  raw("f46bbb0875b1..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Lennard1982/.Lennard1982_TabIndividuals.tsv"),
  raw("4ff277abd409..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Lennard1982/.Lennard1982_TabInterventions.tsv"),
  raw("ce14e72c2838..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Lennard1982/.Lennard1982_TabScatter.tsv"),
  raw("98c0831982d1..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Oosterhuis1988/.Oosterhuis1988_Fig1.tsv"),
  raw("69afd5903cbe..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Oosterhuis1988/.Oosterhuis1988_Fig2.tsv"),
  raw("800dee841966..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Oosterhuis1988/.Oosterhuis1988_Tab1.tsv"),
  raw("393787a4055e..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Oosterhuis1988/.Oosterhuis1988_Tab2A.tsv"),
  raw("754e6e643694..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Oosterhuis1988/.Oosterhuis1988_Tab2B.tsv"),
  raw("c23a9c1bd807..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Oosterhuis1988/.Oosterhuis1988_TabGroups.tsv"),
  raw("19e97aeed587..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Oosterhuis1988/.Oosterhuis1988_TabInterventions.tsv"),
  raw("1a822feb1b3f..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Regardh1974/.Regardh1974_Fig3.tsv"),
  raw("03ba528851c8..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Regardh1974/.Regardh1974_Fig4.tsv"),
  raw("687e5295497a..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Regardh1974/.Regardh1974_Fig6.tsv"),
  raw("5b682d635744..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Regardh1974/.Regardh1974_Fig7.tsv"),
  raw("9c3faba2e72b..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Regardh1974/.Regardh1974_Fig8.tsv"),
  raw("fc1515d06c27..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Regardh1974/.Regardh1974_TabGroups.tsv"),
  raw("bf755c35aa78..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Regardh1974/.Regardh1974_TabIndividuals.tsv"),
  raw("384c492cc9e8..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Regardh1974/.Regardh1974_TabInterventions.tsv"),
  raw("6786b713f174..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Sandberg1988/.Sandberg1988_Fig1.tsv"),
  raw("b5d305c1ad93..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Sandberg1988/.Sandberg1988_Fig2.tsv"),
  raw("065a76eb25e9..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Sandberg1988/.Sandberg1988_Fig3.tsv"),
  raw("a5b388ecfb37..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Sandberg1988/.Sandberg1988_Fig4.tsv"),
  raw("90c4a2bb9d60..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Sandberg1988/.Sandberg1988_Tab1.tsv"),
  raw("3ee0caf51adc..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Sandberg1988/.Sandberg1988_Tab2.tsv"),
  raw("08cacf6761ac..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Sandberg1988/.Sandberg1988_TabGroups.tsv"),
  raw("30ea637c3f49..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Sandberg1988/.Sandberg1988_TabInterventions.tsv"),
  raw("048df419a318..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Seeringer2008/.Seeringer2008_Fig1.tsv"),
  raw("d246103d1998..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Seeringer2008/.Seeringer2008_Fig2.tsv"),
  raw("d6af9f819603..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Seeringer2008/.Seeringer2008_Fig3.tsv"),
  raw("b265ab089a7a..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Seeringer2008/.Seeringer2008_Tab1.tsv"),
  raw("bbbfa91344d3..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Seeringer2008/.Seeringer2008_TabGroups.tsv"),
  raw("6475133fea81..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Seeringer2008/.Seeringer2008_TabIndividuals.tsv"),
  raw("439641ad55bb..."),
  raw("pkdb_models/models/metoprolol/data/metoprolol/Seeringer2008/.Seeringer2008_TabInterventions.tsv"),
  raw("54260b78987f..."),
  raw("pkdb_models/models/metoprolol/models/output/models/metoprolol_body_flat.xml"),
  raw("6ca6d55e3289..."),
  ),
  caption: [SHA-256 checksums of the models and data of the fit PD\_20261017\_193512\_\_e995e, their first 12 characters; the full checksums are in the provenance of the result (optimization\_result.json).],
) <tab:checksums:PD_20261017_193512__e995e>

= Results: Metoprolol PBPK\/PD model: fit PD

== Parameters

#figure(
  table(
  columns: 6,
  align: (left, left, right, left, right, left,),
  table.header([Parameter], [Description], [Value \[95% CI\]], [Unit], [Bounds], [Identifiable]),
  raw("HRred_Emax"),
  [maximal relative reduction of the heart rate],
  [0.285 \[0.215, 0.4\]],
  [dimensionless],
  [\[0.05, 0.8\]],
  [yes],
  raw("HRred_EC50"),
  [metoprolol plasma concentration of the half-maximal reduction],
  [0.000122 \[6.25e-05, 0.000234\]],
  [mmol\/l],
  [\[5e-06, 0.005\]],
  [yes],
  ),
  caption: [Parameters of the fit PD\_20261017\_193512\_\_e995e, the parameter set PD\_20261017\_193512\_\_e995e\_0, cost 5.26, with their bounds in the optimization. The 95% confidence intervals are those of the profile likelihood, LB and UB an interval which is open towards the lower or the upper bound, and the Wald intervals of the Fisher information for a parameter without a profile. Identifiable is the classification of the profile: yes, no (LB) or no (UB) if the profile does not reach the threshold towards the lower or the upper bound, no if it reaches it on neither side, structural if it is flat.],
) <tab:parameters:PD_20261017_193512__e995e>

== Data

#figure(
  table(
  columns: 5,
  align: (left, right, right, right, right,),
  table.header([Study], [Training], [Validation], [Outlier], [Total]),
  [Blomqvist1988],
  [2 (12)],
  [-],
  [-],
  [2 (12)],
  [Johnsson1975],
  [7 (35)],
  [-],
  [-],
  [7 (35)],
  [Kirchheiner2004],
  [2 (10)],
  [1 (5)],
  [-],
  [3 (15)],
  [Lennard1982],
  [-],
  [2 (4)],
  [-],
  [2 (4)],
  [Oosterhuis1988],
  [2 (12)],
  [-],
  [-],
  [2 (12)],
  [Sandberg1988],
  [2 (12)],
  [1 (6)],
  [-],
  [3 (18)],
  [Total],
  [15 (81)],
  [4 (15)],
  [-],
  [19 (96)],
  ),
  caption: [Data of the fit PD\_20261017\_193512\_\_e995e: the number of fit mappings and, in parentheses, of data points per study and kind. The training data enters the cost, the validation data and the outliers are evaluated only.],
) <tab:data:PD_20261017_193512__e995e>

== Goodness of fit

#figure(
  table(
  columns: 11,
  align: (left, right, right, right, right, right, right, right, right, right, right,),
  table.header([Kind], [n], [cost], [MSE], [RMSE], [NRMSE], [RMSE\_w], [R²], [2-fold \[%\]], [AIC], [BIC]),
  [training],
  [81],
  [5.26],
  [0.000635],
  [0.0252],
  [0.228],
  [0.36],
  [0.834],
  [90.0],
  [-592.3],
  [-587.5],
  [validation],
  [15],
  [-],
  [0.00118],
  [0.0343],
  [0.287],
  [0.598],
  [0.677],
  [73.3],
  [-97.2],
  [-95.8],
  ),
  caption: [Goodness of fit of the fit PD\_20261017\_193512\_\_e995e per kind of data, the parameter set PD\_20261017\_193512\_\_e995e\_0. The cost is defined on the training data only, 2-fold is the percentage of the data points with a positive value and prediction whose prediction is within twofold of the data.],
) <tab:metrics:PD_20261017_193512__e995e>

== Figures

#figure(
  image("plots/traces.svg", width: 100%),
  caption: [Cost of the optimizers over their steps, fit PD\_20261017\_193512\_\_e995e. The cost of every optimization run over its steps. Runs which end at the same cost found the same optimum; a run which stops much higher is stuck in a local minimum.],
) <fig:traces:PD_20261017_193512__e995e>

#figure(
  image("plots/waterfall.svg", width: 100%),
  caption: [Cost of the optimization runs, ordered, fit PD\_20261017\_193512\_\_e995e. The final cost of the runs, ordered. A flat plateau at the left is the global optimum found repeatedly, which is the evidence that the multistart converged; steps to the right are local minima.],
) <fig:waterfall:PD_20261017_193512__e995e>

#figure(
  image("plots/goodness_of_fit.svg", width: 100%),
  caption: [Prediction against the measured data points, per kind of fit mapping, with the agreement of the training data, the lines of twofold and the metrics of the panel, fit PD\_20261017\_193512\_\_e995e. Within twofold of the data are 72 of the 80 training data points (90.0%) and 11 of the 15 validation data points (73.3%); only the data points with a positive value and prediction are counted. Prediction against measurement, one point per data point, with a panel per kind of fit mapping. The points scatter around the diagonal when the model describes the data; a systematic deviation from it is a systematic error of the model. The band is the agreement of the training data, i.e. the same band the Bland-Altman plot draws, here as lines parallel to the diagonal. The dark red dotted lines are twofold, prediction \= 2 x measurement and prediction \= measurement \/ 2; the caption states the points between them of every kind. A point which is zero or negative is not drawn on the logarithmic axes and not counted, the title of a panel then states the points drawn of all. The validation panel shows how the fit describes data it was not fitted on, the outlier panel the data the fit dropped. The box of a panel carries its R², its normalized RMSE, the RMSE of the residuals of the cost and the percentage of its points within twofold.],
) <fig:goodness_of_fit:PD_20261017_193512__e995e>

#figure(
  image("plots/bland_altman.svg", width: 100%),
  caption: [Agreement of prediction and measurement as a ratio, per kind of fit mapping, with the agreement of the training data and the agreement of the panel, fit PD\_20261017\_193512\_\_e995e. The ratio of prediction and measurement over the geometric mean of the two, i.e. the goodness of fit with the diagonal turned into the horizontal. The band is the same, the bias and the limits of agreement #raw("bias ± 1.96 SD") of the training data as fold factors. A bias away from 1 is a systematic over- or underprediction, wide limits are a large scatter, and a trend over the mean is a model which describes the large or the small values better. The box of a panel carries the bias and the SD of its own points as fold factors and the share of them inside the limits of agreement of the training data.],
) <fig:bland_altman:PD_20261017_193512__e995e>

#figure(
  image("plots/profiles.svg", width: 100%),
  caption: [Profile likelihood of every parameter: the cost with the parameter fixed and the other parameters optimized, the threshold of the confidence level and the confidence interval, fit PD\_20261017\_193512\_\_e995e. One profile per parameter. A profile which crosses the dashed threshold on both sides gives a finite confidence interval; one which stays below it up to a bound is practically non-identifiable; a flat profile is structurally non-identifiable, the parameter is compensated by the others.],
) <fig:profiles:PD_20261017_193512__e995e>

== Provenance

#figure(
  table(
  columns: 2,
  align: (left, left,),
  table.header([Item], [Value]),
  [Fit],
  raw("PD_20261017_193512__e995e"),
  [Created],
  [2026-10-17 17:35:16 UTC],
  [Seed],
  [1234],
  [Python],
  [3.14.4],
  [sbmlsim],
  [0.10.0],
  [libRoadRunner],
  [2.10.0],
  [SciPy],
  [1.18.1],
  [NumPy],
  [2.5.3],
  [Repository],
  raw("/home/mkoenig/git/pkdb_models-metoprolol"),
  [Commit],
  raw("c3d109c6e1cf45ce2a0d30b45c1386b1abb71399"),
  [Uncommitted changes],
  [no],
  ),
  caption: [Provenance of the fit PD\_20261017\_193512\_\_e995e: the versions it ran with and the revision of its models and data; the SHA-256 checksums of the models and data are listed in #ref(<tab:checksums:PD_20261017_193512__e995e>).],
) <tab:provenance:PD_20261017_193512__e995e>

#bibliography("references.bib", style: "references.csl")
