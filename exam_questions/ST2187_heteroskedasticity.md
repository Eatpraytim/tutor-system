# ST2187 — Heteroscedasticity & Probability: 50 Exam Questions with Model Answers

---

## Part A: Heteroscedasticity Concepts (Q1-10)

### Q1. Define heteroscedasticity.
**Model answer:** Heteroscedasticity is the condition where the variance of the error term varies with the predictors: Var(εᵢ|Xᵢ) ≠ constant. It violates the homoscedasticity assumption of the classical linear model. "Hetero" = different, "skedastic" = spread.

### Q2. What are the consequences of heteroscedasticity for OLS?
**Model answer:** (i) OLS estimators remain unbiased and consistent. (ii) OLS is no longer BLUE (not minimum variance). (iii) Standard errors calculated with the usual formula are biased, making t-tests, F-tests, and confidence intervals invalid.

### Q3. How do you visually detect heteroscedasticity?
**Model answer:** Plot residuals (or squared residuals) against fitted values or against each predictor. A fan shape, funnel shape, or any systematic pattern where spread changes with X indicates heteroscedasticity. Random scatter with constant spread suggests homoscedasticity.

### Q4. Describe the Breusch-Pagan test.
**Model answer:** Regress the squared residuals ε̂² on the predictors: ε̂² = δ₀ + δ₁X₁ + ... + δₖXₖ + v. Test H₀: all δⱼ = 0 using an F-test or n·R² (LM statistic, ~χ²(k)). Rejecting H₀ indicates heteroscedasticity.

### Q5. Describe the White test.
**Model answer:** A more general test than Breusch-Pagan. Regress ε̂² on all predictors, their squares, and cross-products. Test H₀: all coefficients (except intercept) equal zero. More flexible but loses power with many predictors due to high df.

### Q6. What is Goldfeld-Quandt test?
**Model answer:** Split data into two groups based on the variable suspected of causing heteroscedasticity, run separate OLS, and compare variances with F = σ̂²₁/σ̂²₂. Under H₀ of homoscedasticity, this follows an F-distribution. Simple but only detects monotonic heteroscedasticity.

### Q7. What are heteroscedasticity-robust (White) standard errors?
**Model answer:** Robust SEs correct the variance-covariance matrix of β̂ to account for heteroscedasticity without assuming its form: Var_robust(β̂) = (X'X)⁻¹ (X'ΩX) (X'X)⁻¹ where Ω is a diagonal matrix of ε̂²ᵢ. They allow valid inference without fixing the model.

### Q8. Explain Weighted Least Squares (WLS).
**Model answer:** WLS minimises Σ wᵢ(yᵢ − x'ᵢβ)² where weights wᵢ = 1/σ²ᵢ downweight high-variance observations. If σ²ᵢ is known or estimated correctly, WLS is BLUE. The estimator is β̂_WLS = (X'WX)⁻¹X'Wy with W = diag(wᵢ).

### Q9. What is Feasible Generalised Least Squares (FGLS)?
**Model answer:** When the form of heteroscedasticity is unknown, first estimate σ²ᵢ (e.g., by regressing log(ε̂²) on X), then apply WLS with estimated weights. FGLS gives more efficient estimates than OLS when heteroscedasticity is correctly modelled.

### Q10. Compare OLS with robust SEs vs WLS.
**Model answer:** OLS with robust SEs gives consistent inference without modelling heteroscedasticity — simple but inefficient. WLS is more efficient if the variance structure is correctly specified but biased if mis-specified. In practice, OLS + robust SE is the safer default; WLS when you have strong theory about the variance.

---

## Part B: Probability Fundamentals (Q11-20)

### Q11. State the three axioms of probability.
**Model answer:** (1) Non-negativity: P(A) ≥ 0 for any event A. (2) Normalisation: P(S) = 1 where S is the sample space. (3) Countable additivity: for disjoint events A₁, A₂, ..., P(∪Aᵢ) = ΣP(Aᵢ).

### Q12. Define conditional probability and state Bayes' theorem.
**Model answer:** Conditional probability: P(A|B) = P(A∩B)/P(B) when P(B) > 0. Bayes' theorem: P(A|B) = P(B|A)P(A)/P(B). Used to invert conditioning — compute P(cause|effect) from P(effect|cause).

### Q13. State the law of total probability.
**Model answer:** If B₁, B₂, ..., Bₖ partition the sample space, then P(A) = ΣP(A|Bᵢ)P(Bᵢ). It decomposes the probability of A across mutually exclusive, exhaustive scenarios.

### Q14. Define independence for two events.
**Model answer:** Events A and B are independent if P(A∩B) = P(A)·P(B), equivalently P(A|B) = P(A) or P(B|A) = P(B). Independence means B's occurrence gives no information about A.

### Q15. Compare mutually exclusive and independent events.
**Model answer:** Mutually exclusive: P(A∩B) = 0 — cannot occur together. Independent: P(A∩B) = P(A)P(B) — one does not affect the other. For non-trivial events (P > 0), mutually exclusive implies dependent, because P(A|B) = 0 ≠ P(A).

### Q16. State properties of expectation.
**Model answer:** (1) Linearity: E(aX + bY + c) = aE(X) + bE(Y) + c. (2) Monotonicity: X ≤ Y implies E(X) ≤ E(Y). (3) If X ≥ 0, then E(X) ≥ 0. (4) Jensen's inequality: for convex f, E(f(X)) ≥ f(E(X)).

### Q17. Derive the variance formula Var(X) = E(X²) − [E(X)]².
**Model answer:** Var(X) = E[(X − μ)²] = E(X² − 2μX + μ²) = E(X²) − 2μE(X) + μ² = E(X²) − 2μ² + μ² = E(X²) − μ² = E(X²) − [E(X)]².

### Q18. State properties of variance.
**Model answer:** (1) Var(X) ≥ 0, with equality iff X is constant. (2) Var(aX + b) = a²Var(X). (3) For independent X, Y: Var(X + Y) = Var(X) + Var(Y). (4) General: Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y).

### Q19. Define the covariance.
**Model answer:** Cov(X, Y) = E[(X − μₓ)(Y − μᵧ)] = E(XY) − E(X)E(Y). Positive values indicate variables move together; negative indicate opposite. Independence implies Cov = 0, but Cov = 0 does not imply independence (except under multivariate normality).

### Q20. Define correlation and state its range.
**Model answer:** ρ(X, Y) = Cov(X,Y) / (σₓ·σᵧ). Range: −1 ≤ ρ ≤ 1. ρ = ±1 indicates perfect linear relationship; ρ = 0 indicates no linear relationship. It is a scale-free measure of linear association.

---

## Part C: Distributions (Q21-30)

### Q21. State the PDF of the normal distribution.
**Model answer:** f(x) = (1/(σ√(2π))) · exp(−(x−μ)²/(2σ²)) for x ∈ ℝ, with mean μ and variance σ². Standard normal has μ = 0, σ = 1.

### Q22. State the Central Limit Theorem.
**Model answer:** If X₁,...,Xₙ are iid with mean μ and finite variance σ², then as n → ∞, (X̄ − μ)/(σ/√n) converges in distribution to N(0, 1). Consequently, the distribution of X̄ is approximately N(μ, σ²/n) for large n regardless of the original distribution.

### Q23. State the weak law of large numbers.
**Model answer:** If X₁,...,Xₙ are iid with E(X) = μ, then X̄_n converges in probability to μ: for any ε > 0, P(|X̄ − μ| > ε) → 0 as n → ∞. Sample means stabilise to the population mean in large samples.

### Q24. State the Binomial distribution.
**Model answer:** X ~ Bin(n, p): count of successes in n independent Bernoulli(p) trials. P(X = k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ for k = 0,1,...,n. E(X) = np, Var(X) = np(1−p).

### Q25. State the Poisson distribution and its mean/variance.
**Model answer:** X ~ Poisson(λ): counts of rare events in fixed interval. P(X = k) = e⁻λλᵏ/k! for k = 0,1,2,... E(X) = Var(X) = λ. Used when events occur at a constant rate independently.

### Q26. When does Binomial approximate to Poisson?
**Model answer:** When n is large and p is small with np = λ held constant (np stable). Rule of thumb: n ≥ 100 and p ≤ 0.05. The Poisson with mean λ = np approximates Bin(n, p).

### Q27. When does Binomial approximate to Normal?
**Model answer:** When np ≥ 5 and n(1−p) ≥ 5, Bin(n,p) ≈ N(np, np(1−p)). Use continuity correction when applying: P(X ≤ k) ≈ P(Z ≤ (k + 0.5 − np)/√(np(1−p))).

### Q28. State the exponential distribution.
**Model answer:** X ~ Exp(λ): models waiting time to next event with constant hazard rate λ. f(x) = λe⁻λˣ for x ≥ 0. E(X) = 1/λ, Var(X) = 1/λ². Memoryless: P(X > s+t | X > s) = P(X > t).

### Q29. State the uniform distribution on [a, b].
**Model answer:** X ~ U(a, b): f(x) = 1/(b−a) for x ∈ [a, b]. E(X) = (a+b)/2, Var(X) = (b−a)²/12. All sub-intervals of equal length have equal probability.

### Q30. How does a chi-squared distribution arise?
**Model answer:** If Z₁,...,Zₖ are iid standard normal, then ΣZ²ᵢ ~ χ²(k) with k degrees of freedom. E(X) = k, Var(X) = 2k. Used for: variance tests, goodness-of-fit, independence in contingency tables, LR tests.

---

## Part D: Numerical Probability (Q31-40)

### Q31. If P(A) = 0.6, P(B) = 0.4, P(A∩B) = 0.2, find P(A∪B) and P(A|B).
**Model answer:** P(A∪B) = P(A) + P(B) − P(A∩B) = 0.6 + 0.4 − 0.2 = 0.8. P(A|B) = P(A∩B)/P(B) = 0.2/0.4 = 0.5. Are A, B independent? P(A)P(B) = 0.24 ≠ 0.2, so no.

### Q32. A test is 95% accurate; disease prevalence is 1%. Given a positive test, find P(disease).
**Model answer:** By Bayes: P(D|+) = P(+|D)P(D) / [P(+|D)P(D) + P(+|¬D)P(¬D)] = (0.95)(0.01) / [(0.95)(0.01) + (0.05)(0.99)] = 0.0095 / (0.0095 + 0.0495) = 0.0095/0.059 = 0.161 or 16.1%. Base-rate fallacy — intuition overestimates this.

### Q33. X ~ Bin(10, 0.3). Find P(X = 3).
**Model answer:** P(X = 3) = C(10,3)(0.3)³(0.7)⁷ = 120 · 0.027 · 0.0824 = 0.267.

### Q34. X ~ Poisson(3). Find P(X ≤ 2).
**Model answer:** P(X ≤ 2) = e⁻³[1 + 3 + 9/2] = e⁻³(8.5) = 0.0498 × 8.5 = 0.423.

### Q35. X ~ N(50, 10²). Find P(40 < X < 65).
**Model answer:** Standardise: P((40−50)/10 < Z < (65−50)/10) = P(−1 < Z < 1.5) = Φ(1.5) − Φ(−1) = 0.9332 − 0.1587 = 0.7745.

### Q36. X̄ from n = 25, μ = 100, σ = 15. Find P(X̄ > 105).
**Model answer:** X̄ ~ N(100, 15²/25) = N(100, 9). SE = 3. P(X̄ > 105) = P(Z > (105−100)/3) = P(Z > 1.67) = 1 − 0.9525 = 0.0475.

### Q37. Given Var(X) = 4, Var(Y) = 9, Cov(X,Y) = −2, find Var(X + Y) and Var(2X − Y).
**Model answer:** Var(X + Y) = 4 + 9 + 2(−2) = 9. Var(2X − Y) = 4Var(X) + Var(Y) − 4Cov(X,Y) = 16 + 9 − 4(−2) = 33.

### Q38. Find ρ(X, Y) given Cov(X,Y) = 6, σₓ = 3, σᵧ = 4.
**Model answer:** ρ = Cov/(σₓσᵧ) = 6/(3·4) = 0.5. Moderate positive linear association.

### Q39. E(X) = 5, E(X²) = 30. Find Var(X) and σₓ.
**Model answer:** Var(X) = E(X²) − [E(X)]² = 30 − 25 = 5. σₓ = √5 = 2.24.

### Q40. X ~ U(0, 10). Find P(X > 7 | X > 4).
**Model answer:** P(X > 7 | X > 4) = P(X > 7 ∩ X > 4)/P(X > 4) = P(X > 7)/P(X > 4) = (3/10)/(6/10) = 0.5.

---

## Part E: Hypothesis Testing for Variance (Q41-45)

### Q41. State the chi-squared test for variance.
**Model answer:** For H₀: σ² = σ²₀ vs H₁: σ² ≠ σ²₀, test statistic is χ² = (n−1)s²/σ²₀ with df = n−1. Under H₀ (and normality of X), this follows chi-squared with n−1 df. Reject if χ² > χ²_{α/2} or χ² < χ²_{1−α/2}.

### Q42. State the F-test for equality of two variances.
**Model answer:** For H₀: σ²₁ = σ²₂ from two independent normal samples, F = s²₁/s²₂ with df = (n₁−1, n₂−1). Under H₀ (and normality), follows F-distribution. Place the larger variance in the numerator by convention.

### Q43. Why is the F-test sensitive to non-normality?
**Model answer:** The F-test for variances assumes both populations are normally distributed. Even mild non-normality inflates type I error rates — the test is not robust like t-tests are under the CLT. Use Levene's or Brown-Forsythe test when normality is suspect.

### Q44. When would you prefer Bartlett's test over Levene's for variance equality?
**Model answer:** Bartlett's test is more powerful under normality but highly sensitive to departures from normality. Levene's test is more robust to non-normality (using absolute deviations from the median) but less powerful under normality. Prefer Levene in applied work where normality is not guaranteed.

### Q45. What does a significant variance test imply for subsequent mean comparisons?
**Model answer:** If variances are unequal (reject H₀ in F-test), use Welch's t-test instead of the standard pooled t-test. Welch's test does not assume equal variances, calculates a modified df, and is preferable as default even without a formal variance test.

---

## Part F: True/False and Applications (Q46-50)

### Q46. T/F: If Cov(X, Y) = 0, then X and Y are independent.
**Model answer:** FALSE in general. Zero covariance means no linear association, but non-linear dependencies can exist. Example: X ~ U(−1, 1) and Y = X²; Cov(X, Y) = 0 but clearly dependent. TRUE under multivariate normality: jointly normal with zero covariance implies independence.

### Q47. T/F: The sample mean X̄ is always normally distributed.
**Model answer:** FALSE. X̄ is exactly normal only if the underlying X is normal. For non-normal X, X̄ is approximately normal by the CLT for large n, but not exactly. Small samples from skewed distributions can give non-normal X̄.

### Q48. T/F: Heteroscedasticity biases the OLS coefficient estimates.
**Model answer:** FALSE. Heteroscedasticity does not bias coefficients — they remain unbiased and consistent. It biases the standard errors, making t-tests and CIs unreliable. Remedy: robust standard errors or WLS.

### Q49. A dataset of 1,000 customer wait times shows residuals fan outward when regressed on order size. What do you conclude and do?
**Model answer:** This is classic heteroscedasticity — larger orders have larger variance in wait times (plausibly). OLS estimates are still unbiased, but standard errors and inference are invalid. Remedy: (i) recompute with White's robust standard errors, (ii) model the variance structure (e.g., log-transform wait time), (iii) use WLS with weights proportional to 1/order_size if the variance structure is clear. Report the issue and the correction used.

### Q50. In a quality control setting, you want to verify defective parts follow Poisson(λ = 2). Over 50 periods you observe sample mean = 2.3, variance = 5.8. What does this suggest?
**Model answer:** For Poisson, mean = variance. Here mean = 2.3 but variance = 5.8 — clear overdispersion (variance >> mean). This violates the Poisson assumption. Likely causes: (i) clustering of defects (non-independent), (ii) heterogeneous rates across sub-populations. Remedy: use a Negative Binomial distribution, which allows mean ≠ variance. Conduct a formal goodness-of-fit or overdispersion test before concluding.

---

**Exam tip:** For heteroscedasticity problems, always: (1) state both visual evidence (residual plot) and formal test (Breusch-Pagan / White), (2) note that OLS is unbiased but inefficient, (3) recommend a specific correction (robust SEs or WLS), (4) re-run inference with the correction before interpreting coefficients.
