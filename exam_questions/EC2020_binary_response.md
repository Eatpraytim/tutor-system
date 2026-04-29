# EC2020 — Binary Response Models & MLE: 50 Exam Questions with Model Answers

---

## Part A: Binary Response Models (Q1-10)

### Q1. What is a binary response model?
**Model answer:** A regression model where the dependent variable takes only two values (typically 0 or 1). Examples: employment (yes/no), default (yes/no), purchase (yes/no). Models P(Y=1|X) as a function of predictors, constrained to [0, 1].

### Q2. Describe the Linear Probability Model (LPM).
**Model answer:** LPM: P(Y=1|X) = β₀ + β₁X₁ + ... + β_kX_k. Estimated by OLS. Simple interpretation: β_j = marginal effect on probability. Problems: (1) fitted values can exceed [0,1], (2) heteroscedastic errors (Var(u|X) = P(1−P)), (3) linear relationship inappropriate near boundaries. Useful for quick approximations but inferior to probit/logit.

### Q3. What is a latent variable interpretation?
**Model answer:** Assume unobserved Y* = β'X + u, where Y = 1 if Y* > 0, Y = 0 otherwise. Observed Y is the indicator. P(Y=1|X) = P(u > −β'X) = F(β'X), where F is the CDF of −u. Probit: F = Φ (normal CDF). Logit: F = Λ (logistic CDF).

### Q4. State the probit model.
**Model answer:** P(Y=1|X) = Φ(β₀ + β₁X₁ + ... + β_kX_k), where Φ is the standard normal CDF. Arises from latent variable with u ~ N(0,1). Estimated by MLE. Marginal effects are non-linear: ∂P/∂X_j = β_j · φ(Xβ), where φ is normal PDF.

### Q5. State the logit model.
**Model answer:** P(Y=1|X) = Λ(Xβ) = 1/(1 + e^(−Xβ)), where Λ is the logistic CDF. Arises from latent variable with logistic error. Equivalent: log[P/(1−P)] = Xβ (log-odds linear in X). Marginal effects: ∂P/∂X_j = β_j · Λ(Xβ)(1 − Λ(Xβ)).

### Q6. Compare probit and logit.
**Model answer:** Very similar results in practice. Differences: (1) Logit uses logistic CDF (heavier tails). Probit uses normal. (2) Coefficients differ by scaling factor (β_logit ≈ β_probit × π/√3 ≈ 1.81). (3) Logit has simple odds-ratio interpretation; probit does not. (4) Computationally similar. Choice often by convention or software default.

### Q7. What's the issue with interpreting logit/probit coefficients directly?
**Model answer:** Coefficients are in latent variable or log-odds units, not probabilities. Sign and significance are meaningful, but magnitude requires computing marginal effects. Marginal effects depend on X values (typically computed at means or averages). Cannot simply say "β_j = 0.5 means 50 pp higher probability".

### Q8. Describe marginal effects in logit/probit.
**Model answer:** ∂P(Y=1|X)/∂X_j = β_j · f(Xβ), where f = φ for probit, Λ(1−Λ) for logit. Depends on X values. Common reports: (1) Marginal effect at the mean (MEM). (2) Average marginal effect (AME) = (1/n)Σ ∂P/∂X_j evaluated at each observation. AME often preferred.

### Q9. Interpret a probit coefficient β_j = 0.3.
**Model answer:** A one-unit increase in X_j increases the underlying latent variable (Y*) by 0.3 units. For marginal effect on probability, compute β_j · φ(Xβ) at appropriate X values. At mean X with φ(Xβ) = 0.2: marginal effect ≈ 0.3 × 0.2 = 0.06 = 6 pp increase in probability.

### Q10. State the assumption of independent errors.
**Model answer:** The errors across observations are independent. Violated by clustered data (students in schools), panel data with correlation over time, spatial dependence. Remedies: clustered SE, panel methods (random/fixed effects logit), multilevel models. Consequences: standard SE biased; coefficients typically unbiased.

---

## Part B: Maximum Likelihood Estimation (Q11-20)

### Q11. What is maximum likelihood estimation (MLE)?
**Model answer:** Method for estimating parameters by maximising the likelihood function L(θ; data) = joint probability of observed data given parameters θ. MLE finds θ̂ = argmax L(θ; data). Equivalently, maximise log-likelihood ℓ(θ) = log L. Optimal in many senses — consistent, asymptotically efficient, asymptotically normal.

### Q12. State the likelihood for a binary logit model.
**Model answer:** L(β) = Π Λ(xᵢβ)^{y_i} · (1 − Λ(xᵢβ))^{1−y_i}. Log-likelihood: ℓ(β) = Σ y_i log Λ(xᵢβ) + (1−y_i) log(1 − Λ(xᵢβ)). Maximise over β numerically (Newton-Raphson, Fisher scoring). Concave in β — unique global maximum.

### Q13. State the likelihood for a binary probit model.
**Model answer:** L(β) = Π Φ(xᵢβ)^{y_i} · (1 − Φ(xᵢβ))^{1−y_i}. Log-likelihood: ℓ(β) = Σ y_i log Φ(xᵢβ) + (1−y_i) log(1 − Φ(xᵢβ)). Structure identical to logit, with Φ replacing Λ. Maximised numerically.

### Q14. State properties of MLE estimators under regularity conditions.
**Model answer:** (1) Consistency: θ̂ →_p θ₀ as n → ∞. (2) Asymptotic normality: √n(θ̂ − θ₀) →_d N(0, I(θ₀)⁻¹), where I is Fisher information. (3) Asymptotic efficiency: achieves Cramér-Rao lower bound. (4) Invariance: MLE of g(θ) = g(θ̂_MLE). (5) Functional form flexibility.

### Q15. What is Fisher information?
**Model answer:** Measure of "how much information" the sample carries about θ. Defined as I(θ) = −E[∂²log L/∂θ²] (negative expected Hessian). At the true θ₀, 1/I(θ) is the asymptotic variance of θ̂ — the Cramér-Rao lower bound. Higher information = lower variance of θ̂.

### Q16. State the Wald test using MLE.
**Model answer:** Tests H₀: θ = θ₀. W = (θ̂ − θ₀)' V̂(θ̂)⁻¹ (θ̂ − θ₀) ~ χ²(q) asymptotically. Simple to compute. Small-sample issues: can be sensitive to parameterisation. Large samples: reliable.

### Q17. State the likelihood ratio (LR) test.
**Model answer:** LR = −2[ℓ(θ̂_R) − ℓ(θ̂_U)] ~ χ²(q), where R = restricted model (under H₀), U = unrestricted. Compares log-likelihoods. Requires estimating both models. Asymptotically equivalent to Wald but often better in small samples.

### Q18. State the Lagrange Multiplier (LM) / score test.
**Model answer:** Uses only the restricted model. LM = s(θ̂_R)' I(θ̂_R)⁻¹ s(θ̂_R) ~ χ²(q), where s = score (∂ℓ/∂θ). Fastest of the three (no unrestricted estimation needed). Same asymptotic distribution as Wald and LR.

### Q19. Compare Wald, LR, and LM tests.
**Model answer:** Asymptotically equivalent under H₀. Numerical differences in finite samples: LR ≥ LM or Wald typically. LR requires estimating both models. Wald requires unrestricted only. LM requires restricted only. Use LR for specification tests; Wald for simple significance. LR preferred when samples are small.

### Q20. Describe pseudo R-squared measures.
**Model answer:** Analogs to R² for MLE models. (1) McFadden: 1 − ℓ_full/ℓ_null. (2) Cox-Snell: 1 − (L_null/L_full)^(2/n). (3) Nagelkerke: Cox-Snell/max. All measure relative improvement in likelihood. No direct interpretation as "variance explained". Used for model comparison.

---

## Part C: Model Interpretation (Q21-30)

### Q21. Compute marginal effect for logit with β = 0.5 at P = 0.3.
**Model answer:** ME = β · P(1−P) = 0.5 · 0.3 · 0.7 = 0.105. A one-unit increase in X is associated with approximately 10.5 percentage-point increase in probability of Y = 1 (at this probability level). Note: marginal effect varies with P.

### Q22. Compute marginal effect for probit with β = 0.5 at Xβ = 0.
**Model answer:** φ(0) = 1/√(2π) ≈ 0.399. ME = 0.5 · 0.399 ≈ 0.20. A one-unit increase in X is associated with about 20 pp increase in probability, evaluated at Xβ = 0 (where P = 0.5). Maximum marginal effect at Xβ = 0 (symmetric normal).

### Q23. Interpret odds ratio e^β = 2.5.
**Model answer:** For logit: a one-unit increase in X is associated with odds of Y = 1 multiplied by 2.5 (or 150% higher odds), holding other variables constant. Not a 2.5× probability change. Specific to logit — probit doesn't have this interpretation.

### Q24. Describe the average marginal effect (AME).
**Model answer:** AME = (1/n) Σᵢ [β_j · f(xᵢ'β)], averaging marginal effects across the observed sample. Preferred over marginal effect at mean because it accounts for distribution of X. Reported in software (e.g., Stata's margins command). Standard errors computed via delta method.

### Q25. What is a predicted probability and how to compute?
**Model answer:** P̂(Y=1|X=x₀) = F(x₀'β̂), where F is appropriate CDF (Φ or Λ). Plug in specific X values to get predicted probabilities. Useful for: (1) Visualising effects. (2) Prediction. (3) Sensitivity analysis. (4) Converting coefficients to probabilities.

### Q26. Describe classification based on predicted probabilities.
**Model answer:** Classify Y = 1 if P̂ > threshold (often 0.5). Varying threshold trades off sensitivity and specificity. ROC curve shows all thresholds. Optimal threshold: depends on misclassification costs. Classification accuracy (% correct) can be misleading with imbalanced classes — use AUC or F1.

### Q27. State the ROC curve concept.
**Model answer:** Plot of true positive rate (sensitivity) vs false positive rate (1 − specificity) as threshold varies. AUC (area under curve): 0.5 = random, 1 = perfect. AUC > 0.7 acceptable, > 0.8 good, > 0.9 excellent. Preferred over accuracy for imbalanced data.

### Q28. Describe goodness-of-fit tests for binary response.
**Model answer:** (1) Hosmer-Lemeshow: compare observed vs expected frequencies by decile of predicted probability. χ² test. (2) Pearson χ²: compare observed vs expected counts in contingency table. (3) Deviance: −2 log likelihood. Report with degrees of freedom. Complement with visual check of calibration.

### Q29. What is model calibration?
**Model answer:** How well predicted probabilities match actual outcome rates. Plot mean predicted vs mean observed across deciles; should lie on 45° line. Poor calibration = probabilities systematically wrong despite correct ranking. Fix: recalibration (Platt scaling, isotonic regression) after fitting.

### Q30. How to handle rare events in binary response?
**Model answer:** When P(Y=1) is very small (< 5%): (1) Standard logit/probit may give biased estimates (King-Zeng correction). (2) Use weighted likelihood or penalised maximum likelihood (Firth method). (3) Over-sampling cases (retrospective sampling). (4) Rare events logit. Report standard and corrected estimates. Class imbalance affects precision and threshold choice.

---

## Part D: Extensions and Diagnostics (Q31-40)

### Q31. State the ordered probit model.
**Model answer:** For ordinal Y (e.g., ratings 1-5): Y* = β'X + u, u ~ N(0,1). Y = j if μ_{j−1} < Y* < μ_j (thresholds μ₁, μ₂, ..., μ_{k−1}). Estimate β and thresholds jointly by MLE. Preserves ordering. Common in opinion research.

### Q32. State the multinomial logit model.
**Model answer:** For nominal Y with k categories: P(Y=j|X) = exp(β_j'X) / Σ exp(β_i'X). Reference category has coefficients = 0. Coefficients give log-odds of category j vs reference. MLE estimation. Applications: discrete choice (transport, purchase).

### Q33. Describe the Independence of Irrelevant Alternatives (IIA) assumption.
**Model answer:** Multinomial logit: relative odds between two alternatives independent of presence of others. Violated when alternatives are close substitutes. Test: Hausman-McFadden. Remedy: nested logit, multinomial probit, mixed logit.

### Q34. What is heteroscedasticity in binary response?
**Model answer:** Var(u|X) depends on X. Violates model assumption. Causes biased and inconsistent estimates in binary response (unlike linear models). Remedy: heteroskedastic probit, logit with flexible error structure, or robust estimators. Significantly more serious than in linear models.

### Q35. Describe the link function concept.
**Model answer:** Generalised linear model framework: g(μ) = Xβ, where g is link function, μ = E(Y|X). For binary Y: logit (log-odds), probit (inverse normal), complementary log-log. Common link to GLMs — models Poisson, Gamma, binomial uniformly.

### Q36. When would you choose the complementary log-log?
**Model answer:** When modelling survival or asymmetric binary outcomes with skewed probability distribution. P(Y=1|X) = 1 − exp(−exp(Xβ)). Treats 0/1 asymmetrically: approaches 0 slowly, 1 quickly. Appropriate for survival/failure with low probability events.

### Q37. Describe the separation problem.
**Model answer:** Perfect or quasi-separation: predictor perfectly predicts outcome for subset of cases. MLE diverges (coefficients go to infinity). Causes: (1) small samples with certain subgroups all 0 or 1. (2) Too many covariates. Remedies: (1) Firth's penalised likelihood. (2) Remove perfectly predicting variables. (3) Combine sparse categories.

### Q38. Describe residuals in logit/probit.
**Model answer:** Pearson residuals: (y_i − P̂_i)/√(P̂_i(1−P̂_i)). Deviance residuals: based on likelihood contributions. Used for diagnostics. Large residuals flag observations poorly fit by the model. Check leverage and influence separately.

### Q39. How do you handle panel binary data?
**Model answer:** Use random or fixed effects panel logit/probit. Fixed effects logit (conditional logit): eliminates individual effects but requires some variation in Y within individual. Random effects: assumes individual effects uncorrelated with X. Panel probit estimation more computationally complex.

### Q40. What is the complementary log-log and survival connection?
**Model answer:** log(−log(1−P)) = Xβ. Hazard rate interpretation: P is probability of event by time t, β_j controls hazard rate. Links discrete-time survival to grouped continuous-time proportional hazards models. Useful when studying time-to-event with discrete observation.

---

## Part E: Numerical and Conceptual (Q41-45)

### Q41. Given logit with β₀ = −2, β₁ = 0.5, compute P(Y=1) at X₁ = 4.
**Model answer:** Xβ = −2 + 0.5(4) = 0. P = 1/(1+e⁰) = 1/2 = 0.5. At X = 4, probability is exactly 50%. Marginal effect at this point: β · P(1−P) = 0.5 · 0.25 = 0.125 — 12.5 pp increase per unit of X.

### Q42. Given probit with β₀ = −1, β₁ = 0.4, compute P(Y=1) at X = 3.
**Model answer:** Xβ = −1 + 0.4(3) = 0.2. P = Φ(0.2) ≈ 0.579. Marginal effect: 0.4 · φ(0.2) = 0.4 · 0.391 ≈ 0.156 — 15.6 pp per unit of X at this point.

### Q43. Log-likelihood full model = −100; null = −150. Compute LR test with k = 5 degrees of freedom.
**Model answer:** LR = −2(−150 − (−100)) = −2(−50) = 100. df = 5. Critical χ²_{0.05, 5} = 11.07. Since 100 > 11.07, reject H₀: all slopes zero. Model is highly significant. Pseudo R² (McFadden) = 1 − (−100)/(−150) = 0.33.

### Q44. AUC = 0.75. Interpret.
**Model answer:** Acceptable discrimination. 75% chance that a randomly chosen positive case has higher predicted probability than a randomly chosen negative case. Better than random (0.5) but not excellent (> 0.9). Reasonable for many applications; verify calibration separately.

### Q45. Model has 85% accuracy, 70% sensitivity, 90% specificity. Evaluate for fraud detection.
**Model answer:** High specificity minimises false alarms (good for customer experience). Lower sensitivity misses 30% of fraud cases. For fraud detection where missed fraud is costly: should lower threshold to increase sensitivity at cost of some specificity. AUC may be better metric than accuracy. Tune threshold to business cost structure.

---

## Part F: Application (Q46-50)

### Q46. A bank models loan approval with logit. Interpret an income coefficient of 0.0001 per £1.
**Model answer:** β_income = 0.0001 means log-odds of approval increase by 0.0001 per £1 extra income, holding other variables constant. OR = e^0.0001 ≈ 1.0001 — tiny per pound. For £10,000 more income: OR = e^1 ≈ 2.72, odds of approval roughly 2.7× higher. Compute marginal effect at specific income levels for probability change. Economic significance: £10k matters substantially; £1 does not.

### Q47. A logit model has McFadden R² = 0.15. Interpret.
**Model answer:** Modest fit. Improvement over null model in likelihood. McFadden > 0.2 considered good, > 0.4 excellent. 0.15 suggests model has some predictive value but substantial remaining uncertainty. Evaluate alongside classification accuracy, AUC, calibration. Model acceptable for inferences about coefficients; cautious for individual predictions.

### Q48. Interpret logit results for: marketing campaign → purchase.
**Model answer:** (1) Coefficient on campaign dummy = 0.8. OR = e^0.8 = 2.23 — odds of purchase in campaign group are 2.23× those in control. (2) Compute predicted probabilities at baseline vs with campaign: e.g., 20% baseline → 36% with campaign. (3) Report both coefficient and marginal effect (≈16 pp increase at baseline probability). (4) Check significance (z-test, LR test). (5) Discuss practical importance: 16 pp increase is business-relevant.

### Q49. Your probit model predicts default with AUC = 0.68. Recommend.
**Model answer:** Modest predictive power — AUC > 0.5 (random) but well below excellent. Actions: (1) Feature engineering — add behavioural and financial history variables. (2) Interaction terms or non-linear specifications. (3) Consider ensemble methods (random forest, gradient boosting) — often improve AUC. (4) Calibrate probabilities to actual default rates. (5) Economic use: model can flag risky applications, but combine with judgement and additional screens.

### Q50. How would you use logit to model consumer choice between 3 brands?
**Model answer:** Use multinomial logit with 3 categories. (1) Choose reference brand. (2) Predictors: price, brand loyalty, demographics, advertising exposure. (3) Separate equations for each non-reference brand's log-odds vs reference. (4) Estimate by MLE. (5) Interpret: e^β tells how predictor affects probability of choosing that brand vs reference. (6) Check IIA assumption via Hausman test; if violated, nested logit. (7) Predict market share by summing predicted probabilities across customer base. (8) Use for pricing simulation, brand launch forecasting, segmentation.

---

**Exam tip:** For binary response / MLE questions, always: (1) state the model and likelihood explicitly, (2) report coefficients with SE, z-tests (not t), (3) compute marginal effects for interpretation — not just coefficients, (4) report model fit (pseudo R², AUC, LR test), (5) diagnose with classification matrix and calibration, (6) check separation and convergence, (7) discuss sample size requirements (10 events per variable rule).
