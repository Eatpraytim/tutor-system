# ST2134 — Likelihood Testing Structure: 50 Exam Questions with Model Answers

---

## Part A: Likelihood Ratio Test Basics (Q1-15)

### Q1. State the likelihood ratio (LR) definition.
**Model answer:** LR(x) = L(θ₀|x)/L(θ̂|x), where θ̂ is the unrestricted MLE and θ₀ is the null value. Measures relative support for H₀ vs alternative. 0 < LR ≤ 1. Smaller LR = less support for H₀.

### Q2. State the LR statistic.
**Model answer:** λ(x) = 2[ℓ(θ̂) − ℓ(θ₀)] where ℓ = log-likelihood. Equivalently: λ = −2 log LR = 2(log L(θ̂) − log L(θ₀)). Always ≥ 0. Larger λ = more evidence against H₀.

### Q3. State Wilks' theorem.
**Model answer:** Under H₀: θ ∈ Θ₀ with dimension k₀, and the full model has dimension k: λ = 2[ℓ(θ̂) − ℓ(θ̃)] →_d χ²(k − k₀) as n → ∞, where θ̃ is the constrained MLE under H₀. Provides asymptotic distribution for inference.

### Q4. When does Wilks' theorem fail?
**Model answer:** Regularity conditions required: (1) Model identifiable. (2) Likelihood differentiable in neighborhood of θ₀. (3) Parameter not on boundary of space. (4) Fisher information positive definite. Failures: non-identifiability, boundary points (e.g., H₀: σ² = 0), nonstandard likelihoods.

### Q5. Compare LR test and Wald test.
**Model answer:** LR: requires estimating under H₀ and H₁. Invariant to parameterisation. Better finite-sample properties typically. Wald: requires only unrestricted estimate. Simpler computation. Not invariant to non-linear transformations of parameters. Asymptotically equivalent.

### Q6. Compare LR test and score (LM) test.
**Model answer:** LR: requires both restricted and unrestricted MLE. Score: only restricted MLE. Useful when unrestricted estimation is difficult. Asymptotically equivalent to LR and Wald. Also called Rao's test.

### Q7. State the likelihood ratio for Bernoulli with simple vs simple H₀.
**Model answer:** For p = p₀ vs p = p₁: LR(x) = [p₀^x (1−p₀)^{n−x}] / [p₁^x (1−p₁)^{n−x}]. Depends on sample via x alone. Sufficient statistic emerges naturally. By Neyman-Pearson lemma, this LR yields most powerful test.

### Q8. Describe the generalised LR test.
**Model answer:** For composite H₀: θ ∈ Θ₀, composite H₁: θ ∈ Θ \ Θ₀. Λ(x) = sup_{θ ∈ Θ₀} L(θ|x) / sup_{θ ∈ Θ} L(θ|x). Ratio of max likelihood under H₀ to max over all parameter space. Under regularity: −2 log Λ ~_a χ²(df).

### Q9. State the connection to hypothesis testing.
**Model answer:** LR test: reject H₀ if −2 log LR > χ²_{α, df}. Equivalent to rejecting if LR < threshold. For simple vs simple: LR test is most powerful (Neyman-Pearson). For composite: generalised LR test is commonly used.

### Q10. Derive LR statistic for normal mean, σ known.
**Model answer:** H₀: μ = μ₀ vs H₁: μ ≠ μ₀. ℓ(μ) = const − n(μ − X̄)²/(2σ²) − n·s²/(2σ²). ℓ(X̄) − ℓ(μ₀) = n(μ₀ − X̄)²/(2σ²). So λ = n(X̄ − μ₀)²/σ² = Z². Under H₀, Z² ~ χ²(1). Wilks' applies.

### Q11. Derive LR statistic for Bernoulli(p).
**Model answer:** H₀: p = p₀ vs H₁: p ≠ p₀. ℓ(p) = x log p + (n−x) log(1−p). ℓ(p̂) − ℓ(p₀) = x log(x/(np₀)) + (n−x) log((n−x)/(n(1−p₀))). λ = 2 times this. Under H₀: λ ~ χ²(1) asymptotically.

### Q12. Derive LR statistic for Poisson(λ).
**Model answer:** H₀: λ = λ₀. ℓ(λ) = (Σx) log λ − nλ. ℓ(λ̂) − ℓ(λ₀) = (Σx) log(λ̂/λ₀) + nλ₀ − nλ̂ = (Σx)[log(X̄/λ₀) − 1 + λ₀/X̄]. Twice this is λ-statistic.

### Q13. Describe LR test computation procedure.
**Model answer:** (1) Compute unrestricted MLE θ̂, log-likelihood ℓ(θ̂). (2) Compute constrained MLE θ̃ under H₀, log-likelihood ℓ(θ̃). (3) Compute λ = 2(ℓ(θ̂) − ℓ(θ̃)). (4) Compare to χ²_{α, df} where df = # restrictions. (5) Reject if λ exceeds critical value.

### Q14. State the power function of an LR test.
**Model answer:** For simple H₀ vs simple H₁: power = P(reject H₀ | θ ∈ H₁). Given rejection threshold c: power = P(LR < c | θ₁) = P(test statistic in rejection region). Power approaches 1 with: larger n, larger distance from H₀, larger α.

### Q15. Describe the Neyman-Pearson lemma.
**Model answer:** For testing simple H₀: θ = θ₀ vs simple H₁: θ = θ₁: the most powerful (MP) test at level α rejects when L(θ₁|x)/L(θ₀|x) > c (LR test). Maximises power subject to Type I error constraint. Cornerstone of classical testing theory.

---

## Part B: Score Test (Lagrange Multiplier) (Q16-25)

### Q16. Define the score function.
**Model answer:** U(θ) = ∂ℓ/∂θ = ∂log L/∂θ = Σ ∂log f(x_i|θ)/∂θ. Gradient of log-likelihood. Properties: E(U|θ₀) = 0, Var(U|θ₀) = I(θ₀). MLE satisfies U(θ̂) = 0.

### Q17. Derive the score function for Normal(μ, σ²) with σ² known.
**Model answer:** ℓ(μ) = −(1/(2σ²)) Σ(x_i − μ)². U(μ) = ∂ℓ/∂μ = (1/σ²) Σ(x_i − μ) = n(X̄ − μ)/σ². E(U|μ) = 0. Var(U) = n²σ²/(σ⁴·n²) = n/σ² = I(μ)·n.

### Q18. Derive the score function for Bernoulli(p).
**Model answer:** ℓ(p) = (Σx_i) log p + (n − Σx_i) log(1 − p). U(p) = Σx_i/p − (n − Σx_i)/(1−p). Simplify: U = (Σx_i − np)/(p(1−p)) = (X̄ − p)·n/(p(1−p)).

### Q19. State the score (LM) test.
**Model answer:** Tests H₀: θ = θ₀ using only the restricted MLE θ̃ (= θ₀ for simple null). Statistic: LM = U(θ₀)² / I(θ₀) (for single parameter). Under H₀: LM ~_a χ²(1). For multiple parameters: LM = U'(θ₀) I(θ₀)⁻¹ U(θ₀) ~_a χ²(q).

### Q20. Advantages of score test.
**Model answer:** (1) Needs only restricted MLE (often easier than unrestricted). (2) Useful when unrestricted MLE is hard to compute. (3) Invariant to parameterisation (asymptotically). (4) Common for large-model testing (e.g., testing entire additional variable is zero).

### Q21. Derive score test for Normal mean, σ² known.
**Model answer:** U(μ₀) = n(X̄ − μ₀)/σ². I(μ₀) = n/σ². LM = U²/I = [n(X̄ − μ₀)/σ²]² / (n/σ²) = n(X̄ − μ₀)²/σ². Same as LR for this case. Equals Z². Under H₀: ~χ²(1).

### Q22. Describe the Hessian connection to Fisher information.
**Model answer:** Fisher information I(θ) = E[−∂²ℓ/∂θ²]. Empirically estimated via observed information J(θ) = −∂²ℓ(x)/∂θ² evaluated at θ̂. Both used in Wald and score tests. Expected (I) vs observed (J) important distinction.

### Q23. Use score test when computing MLE is hard.
**Model answer:** For complex models, unrestricted MLE requires numerical optimisation. Score test: only restricted MLE needed (often θ₀ for simple null). Computes gradient and information at θ₀. Reject if LM > χ²_{α, q}. Efficient alternative to full MLE.

### Q24. Compute score test for Poisson(λ) H₀: λ = 2.
**Model answer:** U(λ) = Σx/λ − n. At λ₀ = 2: U(2) = Σx/2 − n. I(λ) = n/λ. At λ₀ = 2: I(2) = n/2. LM = U²/I = [Σx/2 − n]² / (n/2) = 2(Σx/2 − n)²/n = (Σx − 2n)²/(2n). Reject H₀ if LM > χ²_{0.05, 1} = 3.84.

### Q25. State score test for simple linear regression.
**Model answer:** Test H₀: β = 0. Score at β = 0: Σx_i(y_i − β₀). I for β: Σx²_i/σ². LM = [Σx_i(y_i − ȳ)]² / [σ² Σx²_i]. Equivalent to F-test up to scaling. Under H₀: χ²(1) asymptotically.

---

## Part C: Wald Test (Q26-35)

### Q26. State the Wald test statistic.
**Model answer:** Tests H₀: g(θ) = 0 (possibly vector). W = g(θ̂)' [Var(g(θ̂))]⁻¹ g(θ̂). For scalar g: W = g(θ̂)² / Var(g(θ̂)). Uses asymptotic variance of estimator. Under H₀: W ~_a χ²(q), where q = number of restrictions.

### Q27. Derive the Wald test for Bernoulli.
**Model answer:** H₀: p = p₀. θ̂ = p̂ = X̄. Var(p̂) = p(1−p)/n, estimated as p̂(1−p̂)/n. W = (p̂ − p₀)² / [p̂(1−p̂)/n] = n(p̂ − p₀)²/(p̂(1−p̂)). Under H₀ and large n: W ~ χ²(1).

### Q28. Compare Wald and LR for small samples.
**Model answer:** LR typically preferred for small samples — better coverage, more invariant. Wald can be inflated or misleading with non-linear transformations (not invariant). For very small samples, compute both; LR more reliable.

### Q29. Describe Wald test for multiple linear hypothesis.
**Model answer:** H₀: Rβ = r. W = (Rβ̂ − r)' [R Var(β̂) R']⁻¹ (Rβ̂ − r). Under H₀: W ~_a χ²(q) where q = number of rows in R. Alternative: F-form W/q ~ F(q, n−k−1).

### Q30. Non-invariance of Wald test.
**Model answer:** Wald test for H₀: g(θ) = 0 can differ from Wald test for H₀: g*(θ) = 0 even if mathematically equivalent hypotheses. Example: testing H₀: log ratio = 0 vs H₀: ratio = 1. Cause: linearisation via delta method is parameterisation-dependent. LR is invariant.

### Q31. Describe robust Wald tests.
**Model answer:** Use heteroscedasticity-robust (sandwich) estimators of Var(β̂). W_robust = β̂² / Var_robust(β̂). Valid under heteroscedasticity. Standard for regression with potential model misspecification. Clustered version accounts for within-cluster correlation.

### Q32. Compute Wald test for OLS coefficient.
**Model answer:** β̂ with SE(β̂). W = β̂²/SE(β̂)². Equivalent to t² if t ~ t(df). Asymptotically: W ~ χ²(1). For multiple coefficients: W = β̂'Var(β̂)⁻¹β̂. Reject if W > χ²_{0.05, q}.

### Q33. Wald test for ratio of two estimates.
**Model answer:** For θ̂₁/θ̂₂, standard error via delta method: SE_ratio ≈ |θ̂₁/θ̂₂| · √(Var(θ̂₁)/θ̂₁² + Var(θ̂₂)/θ̂₂² − 2Cov(θ̂₁, θ̂₂)/(θ̂₁θ̂₂)). Wald statistic: [ratio − 1]/SE_ratio. Note: ratios near zero cause problems.

### Q34. Variance estimation for Wald.
**Model answer:** Typically use asymptotic variance from MLE: Var(θ̂) ≈ 1/(n·I(θ̂)) (observed information). For OLS: σ̂²(X'X)⁻¹ or robust version. Substitute for unknown variance. For complex functions: delta method. Consistency ensures asymptotic validity.

### Q35. When does Wald fail catastrophically?
**Model answer:** (1) At boundary of parameter space (e.g., variance = 0). (2) When parameter is near identification boundary. (3) For transformations where linearisation is poor. (4) When estimator is irregular. In these cases, LR test performs better.

---

## Part D: Relationships and Properties (Q36-45)

### Q36. Demonstrate asymptotic equivalence of LR, Wald, score tests.
**Model answer:** Under H₀ and regularity: LR = Wald + O_p(1/√n) and similarly for score. All three converge to the same limiting χ²(q) distribution. For local alternatives, same non-central χ² — equivalent power. In finite samples, can differ substantially.

### Q37. State the LR upper bound by Wald.
**Model answer:** In some regularity contexts: LR ≤ Wald. More generally, LR and Wald can cross. Relative magnitudes depend on likelihood curvature and parameterisation. Neither strictly dominates; choose based on computational convenience and accuracy concerns.

### Q38. Describe the global vs local nature.
**Model answer:** LR uses global information (likelihood over parameter space). Wald and score use local information (at MLE or null value). LR more robust to parameterisation. Wald can be very misleading when likelihood is skewed.

### Q39. Describe the sign of the score.
**Model answer:** Score U(θ₀) at null: if U > 0, likelihood increases from θ₀ → MLE larger; if U < 0, smaller. Directional information. For one-sided tests, combine LM with sign for one-sided rejection regions.

### Q40. Describe iterated testing sequences.
**Model answer:** Testing nested hypotheses sequentially (e.g., add predictors one at a time). Each test at α. Overall probability of false positive inflated. Remedies: Bonferroni at each step; forward selection with p-to-enter; pre-register testing plan.

### Q41. Relationship to CIs.
**Model answer:** CI is set of θ₀ that are not rejected at level α. Wald CI: θ̂ ± z_{α/2}·SE. LR CI: {θ : 2(ℓ(θ̂) − ℓ(θ)) ≤ χ²_{α, 1}}. Score CI: {θ : U(θ)²/I(θ) ≤ χ²_{α, 1}}. Three CIs agree asymptotically but differ in finite samples.

### Q42. LR CI asymmetric — why?
**Model answer:** LR CI is implicit — defined by curvature of log-likelihood. If likelihood is asymmetric, CI also. Wald CI symmetric by construction. Score CI also typically asymmetric. LR CI honest reflection of likelihood shape, especially for skewed distributions.

### Q43. Describe the profile likelihood.
**Model answer:** For multi-parameter model, profile likelihood of θ_1 is L(θ_1, θ̂₂(θ_1)), where θ̂₂(θ_1) is constrained MLE of θ₂ given θ_1. Used for inference on single parameter in presence of nuisance parameters. Constructs CI by setting LR on profile.

### Q44. LR test for non-nested models.
**Model answer:** Standard LR theory requires nested models. For non-nested: Vuong test uses log-likelihood difference. Under equivalence: converges to normal. Used to compare competing models (e.g., logit vs probit vs AIC rankings).

### Q45. Relation to Bayesian model comparison.
**Model answer:** Bayes factor analogous to LR but integrates over parameter space with priors. BF = ∫ L(θ|x) π_1(θ) dθ / ∫ L(θ|x) π_0(θ) dθ. LR uses MLE (peak); BF averages. Bayesian incorporates prior information, provides posterior probabilities.

---

## Part E: Numerical Examples (Q46-50)

### Q46. Given ℓ(θ̂) = −50, ℓ(θ₀) = −60. Compute LR statistic and test at α = 0.05 with df = 1.
**Model answer:** λ = 2(ℓ(θ̂) − ℓ(θ₀)) = 2(−50 − (−60)) = 20. χ²_{0.05, 1} = 3.84. Since 20 > 3.84, reject H₀. Strong evidence against H₀. p-value ≈ 0.00001. Much more extreme than critical value.

### Q47. Test for 4 restrictions: ℓ_U = −100, ℓ_R = −115.
**Model answer:** λ = 2(−100 − (−115)) = 30. df = 4. χ²_{0.05, 4} = 9.49. Since 30 > 9.49, reject H₀. Restrictions substantially worsen fit. p ≈ 0.00001.

### Q48. Compute score test for Bernoulli H₀: p = 0.5, observed x = 65 in n = 100.
**Model answer:** U(0.5) = (Σx − np)/(p(1−p)) = (65 − 50)/(0.25) = 60. I(0.5) = n/(p(1−p)) = 100/0.25 = 400. LM = U²/I = 3600/400 = 9. Under H₀: ~χ²(1). Critical 3.84. Since 9 > 3.84, reject H₀. Evidence p ≠ 0.5.

### Q49. Compute Wald test for Bernoulli H₀: p = 0.5, p̂ = 0.6, n = 100.
**Model answer:** W = (p̂ − p₀)² / [p̂(1−p̂)/n] = 0.01 / (0.0024) = 4.17. Under H₀: ~χ²(1). Critical 3.84. Since 4.17 > 3.84, reject H₀. Note: LR statistic for same data: λ = 2·100·[0.6 log(0.6/0.5) + 0.4 log(0.4/0.5)] = 2·100·(0.0728) = 14.56. LR suggests stronger evidence than Wald in this case.

### Q50. Apply LR test to compare linear and quadratic regression.
**Model answer:** H₀: quadratic coefficient = 0 (linear model). H₁: include quadratic. Fit both models via OLS (equivalent to MLE with normal errors). LR = 2(ℓ_Q − ℓ_L) = 2 × (1/2)(1/σ²)(SSR_L − SSR_Q) for normal errors. Equivalently: F = (SSR_L − SSR_Q)/1 / (SSR_Q/(n−k_Q−1)). Reject H₀ if LR > χ²_{0.05, 1} = 3.84.

---

**Exam tip:** For likelihood testing questions, always: (1) write log-likelihood explicitly, (2) distinguish which test (LR, Wald, score), (3) state formula and derive carefully, (4) compute score and information at the right point, (5) report asymptotic distribution under H₀ (usually χ²), (6) compare to critical value or p-value, (7) state decision and interpretation.
