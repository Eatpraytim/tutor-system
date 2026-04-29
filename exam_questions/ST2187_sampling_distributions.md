# ST2187 — Sampling Distributions: 50 Exam Questions with Model Answers

---

## Part A: Fundamentals (Q1-10)

### Q1. Define a sampling distribution.
**Model answer:** The probability distribution of a statistic (e.g., X̄, p̂, s²) computed from all possible samples of a given size from a population. It describes how the statistic varies across repeated samples.

### Q2. Distinguish between a sample and a sampling distribution.
**Model answer:** A sample is one set of observations from the population. A sampling distribution is the distribution of a particular statistic computed across many hypothetical samples of the same size. Samples generate observations; sampling distributions describe the behaviour of statistics.

### Q3. State the mean and variance of X̄ when sampling from a population with mean μ and variance σ².
**Model answer:** E(X̄) = μ (unbiased). Var(X̄) = σ²/n. The standard deviation of X̄ — called the standard error — is σ/√n. It decreases with √n, not linearly.

### Q4. Define the standard error and contrast with standard deviation.
**Model answer:** Standard deviation (σ) measures variability of individual observations. Standard error (SE = σ/√n) measures variability of a sample statistic. SE is smaller than σ by factor 1/√n; SE reflects uncertainty in the estimate, σ reflects variability in the data.

### Q5. State the Central Limit Theorem.
**Model answer:** For iid X₁,...,Xₙ with mean μ and finite variance σ², (X̄ − μ)/(σ/√n) →_d N(0,1) as n → ∞. Consequently, for large n, X̄ ~ approximately N(μ, σ²/n) regardless of the population distribution.

### Q6. When can you apply the CLT — what's the rule of thumb?
**Model answer:** n ≥ 30 is a common rule. For symmetric populations, smaller n (≥ 15) often suffices. For very skewed or heavy-tailed populations, larger n may be required. The CLT doesn't apply if variance is infinite (e.g., Cauchy distribution).

### Q7. State the sampling distribution of the sample proportion p̂.
**Model answer:** E(p̂) = p. Var(p̂) = p(1−p)/n. For large n (np ≥ 5 and n(1−p) ≥ 5), p̂ ~ approximately N(p, p(1−p)/n) by CLT. Used for one-sample tests and CIs for proportions.

### Q8. State the sampling distribution of s² for a normal population.
**Model answer:** If X₁,...,Xₙ ~ N(μ, σ²) iid, then (n−1)s²/σ² ~ χ²(n−1). Consequence: s² has a skewed right distribution; E(s²) = σ²; Var(s²) = 2σ⁴/(n−1).

### Q9. State the sampling distribution of (X̄ − μ)/(s/√n).
**Model answer:** For iid samples from a normal population, t = (X̄ − μ)/(s/√n) ~ t(n−1). The Student's t-distribution accounts for using s instead of σ. As n → ∞, t → N(0, 1).

### Q10. Why is the t-distribution wider than the normal?
**Model answer:** The t-distribution incorporates additional uncertainty from estimating σ with s. For small n, this uncertainty is large, resulting in heavier tails than N(0,1). As df increases, s → σ and the t-distribution converges to N(0,1).

---

## Part B: Confidence Intervals (Q11-20)

### Q11. State the general structure of a confidence interval.
**Model answer:** CI = estimate ± (critical value × standard error). Critical value comes from the appropriate sampling distribution (z, t, χ²), and SE measures estimator variability. The confidence level (e.g., 95%) determines the critical value.

### Q12. Construct a 95% CI for μ when σ is known.
**Model answer:** X̄ ± z_{α/2} · σ/√n where z_{0.025} = 1.96. Assumptions: either population is normal, or n is large (CLT).

### Q13. Construct a 95% CI for μ when σ is unknown.
**Model answer:** X̄ ± t_{α/2, n−1} · s/√n. Use t-critical value with df = n−1. Assumption: population approximately normal, or n sufficiently large.

### Q14. Construct a 95% CI for p, the population proportion.
**Model answer:** p̂ ± z_{α/2} · √(p̂(1−p̂)/n) for large samples (np̂, n(1−p̂) ≥ 10). For small samples, use Wilson or Clopper-Pearson intervals which are more accurate.

### Q15. Construct a 95% CI for σ² from a normal population.
**Model answer:** [(n−1)s² / χ²_{α/2, n−1}, (n−1)s² / χ²_{1−α/2, n−1}]. Note: asymmetric because χ² is skewed. For σ, take square roots.

### Q16. How does sample size affect CI width?
**Model answer:** Width ∝ 1/√n. To halve the width, you must quadruple the sample size. Diminishing returns: large samples yield small precision gains per extra observation.

### Q17. Explain the difference between confidence level and CI coverage.
**Model answer:** Confidence level (e.g., 95%) is the theoretical long-run proportion of CIs from repeated samples containing the true parameter. Coverage probability is the actual proportion. For correctly specified CIs, they coincide; for approximations, coverage may differ.

### Q18. Interpret a 95% CI for μ of [40, 60].
**Model answer:** We are 95% confident the population mean μ lies between 40 and 60. The "95% confidence" refers to the procedure: 95% of such intervals constructed from repeated samples would contain μ. It is NOT P(μ ∈ [40,60]) = 0.95 — in frequentist inference, μ is fixed.

### Q19. Explain margin of error.
**Model answer:** The margin of error is the half-width of the CI: ME = critical value × SE. It quantifies estimation precision. Polls often report "±3 percentage points at 95% confidence", meaning ME = 0.03.

### Q20. Sample size calculation for estimating μ within ±E at confidence 1−α.
**Model answer:** n = (z_{α/2} · σ / E)². Requires a prior estimate of σ (from pilot study or conservative value). For proportions: n = (z_{α/2})² · p(1−p)/E², where p = 0.5 gives conservative maximum.

---

## Part C: Hypothesis Testing Basics (Q21-30)

### Q21. State the null and alternative hypotheses structure.
**Model answer:** H₀: null (status quo or no effect). H₁: alternative (research claim). Either one-tailed (H₁: μ > μ₀ or μ < μ₀) or two-tailed (H₁: μ ≠ μ₀). Always state H₀ and H₁ in exam answers before testing.

### Q22. State the four steps of hypothesis testing.
**Model answer:** (1) State H₀ and H₁. (2) Choose significance level α and compute test statistic. (3) Compare test statistic to critical value or p-value to α. (4) State decision and interpret in context.

### Q23. Define Type I and Type II errors.
**Model answer:** Type I (α): rejecting H₀ when it is true (false positive). Type II (β): failing to reject H₀ when it is false (false negative). Power = 1 − β = probability of rejecting H₀ when H₁ is true. Trade-off: reducing α increases β unless n increases.

### Q24. State the z-test statistic for one mean, σ known.
**Model answer:** z = (X̄ − μ₀)/(σ/√n). Under H₀, z ~ N(0,1). Reject H₀ if |z| > z_{α/2} (two-sided) or z > z_α / z < −z_α (one-sided).

### Q25. State the t-test statistic for one mean, σ unknown.
**Model answer:** t = (X̄ − μ₀)/(s/√n), df = n−1. Under H₀ with normal data, t ~ t(n−1). Reject if |t| > t_{α/2, n−1}. Robust to moderate non-normality for large n.

### Q26. State the z-test for one proportion.
**Model answer:** z = (p̂ − p₀)/√(p₀(1−p₀)/n). Under H₀, z ~ N(0,1) approximately (for np₀, n(1−p₀) ≥ 5). Note: use p₀ (not p̂) in the SE for hypothesis testing.

### Q27. Define the p-value.
**Model answer:** The p-value is the probability, under H₀, of observing a test statistic as extreme or more extreme than what was observed. Small p-values indicate data are inconsistent with H₀. Reject H₀ if p < α.

### Q28. Common misinterpretations of the p-value.
**Model answer:** (1) "P(H₀ true | data)" — FALSE; it's P(data | H₀). (2) "P(data arose by chance)" — misleading. (3) "Effect size" — FALSE; p-values say nothing about magnitude. (4) "1 − p = P(H₁)" — FALSE. Always pair p-value with effect size and CI.

### Q29. When should you use a one-sided vs two-sided test?
**Model answer:** One-sided when only one direction of effect is of interest and the other is either impossible or equivalent to the null. Two-sided when either direction is meaningful. Two-sided is the default; one-sided must be justified before seeing the data (not post-hoc).

### Q30. State the connection between hypothesis testing and CIs.
**Model answer:** Duality: a two-sided level-α test rejects H₀: θ = θ₀ iff the 100(1−α)% CI excludes θ₀. Equivalent ways of presenting the same inference. Always report both.

---

## Part D: Two-Sample Tests (Q31-40)

### Q31. State the two-sample t-test (independent samples, equal variances).
**Model answer:** t = (X̄₁ − X̄₂) / [s_p√(1/n₁ + 1/n₂)], where pooled variance s²_p = [(n₁−1)s²₁ + (n₂−1)s²₂]/(n₁+n₂−2). df = n₁+n₂−2. Assumes normality and σ₁² = σ₂².

### Q32. State Welch's t-test (unequal variances).
**Model answer:** t = (X̄₁ − X̄₂)/√(s²₁/n₁ + s²₂/n₂). df = [s²₁/n₁ + s²₂/n₂]² / [(s²₁/n₁)²/(n₁−1) + (s²₂/n₂)²/(n₂−1)] (Welch-Satterthwaite). Preferred default when equal-variance assumption is doubtful.

### Q33. State the paired t-test.
**Model answer:** For matched pairs (before/after), compute differences d_i = X_i − Y_i. Then t = d̄/(s_d/√n), df = n−1. Tests H₀: μ_d = 0. Uses within-pair comparison to eliminate individual-level variation — more powerful than independent-samples test when pairing is informative.

### Q34. State the two-sample z-test for proportions.
**Model answer:** z = (p̂₁ − p̂₂)/√(p̂(1−p̂)(1/n₁ + 1/n₂)) where pooled p̂ = (x₁+x₂)/(n₁+n₂). Under H₀: p₁ = p₂, z ~ N(0,1). Requires large samples.

### Q35. Describe the F-test for equality of two variances.
**Model answer:** F = s²₁/s²₂, df = (n₁−1, n₂−1). Sensitive to non-normality. Conventionally place larger variance in numerator. Alternative robust tests: Levene's, Brown-Forsythe.

### Q36. When do you use Welch vs pooled t-test?
**Model answer:** Use Welch's as default — it performs nearly as well as pooled under equal variances and avoids the risk of inflated Type I error under unequal variances. Use pooled only when equal variances are strongly supported (by theory or a formal test at low α).

### Q37. What are assumptions of the two-sample t-test?
**Model answer:** (1) Independent random samples. (2) Each sample from approximately normal populations (robust for n ≥ 30 by CLT). (3) Equal variances (for pooled version) — dropped for Welch. (4) Continuous or approximately continuous data.

### Q38. Difference between Welch and Mann-Whitney tests?
**Model answer:** Welch's t: tests difference in means, assumes approximate normality or large n. Mann-Whitney: tests equal medians (or stochastic dominance), non-parametric, based on ranks. Use Mann-Whitney for small samples from non-normal distributions or ordinal data.

### Q39. What is the sampling distribution of the difference X̄₁ − X̄₂ from independent normal populations?
**Model answer:** X̄₁ − X̄₂ ~ N(μ₁ − μ₂, σ²₁/n₁ + σ²₂/n₂). Mean of difference equals difference of means; variance of difference equals sum of variances when samples are independent.

### Q40. Give the chi-squared test for independence in a contingency table.
**Model answer:** χ² = Σ(O−E)²/E with df = (r−1)(c−1) where r = rows, c = columns. E_{ij} = (row total × column total)/grand total. Assumptions: E_{ij} ≥ 5 for most cells. Reject H₀ = variables are dependent.

---

## Part E: Numerical Problems (Q41-45)

### Q41. n = 50, X̄ = 75, s = 12. Construct 95% CI for μ.
**Model answer:** df = 49. t_{0.025, 49} ≈ 2.01. SE = 12/√50 = 1.70. CI = 75 ± 2.01(1.70) = 75 ± 3.41 = [71.59, 78.41]. 95% confidence that μ is between 71.6 and 78.4.

### Q42. Test H₀: μ = 100 vs H₁: μ ≠ 100. Sample: n = 25, X̄ = 105, s = 8.
**Model answer:** t = (105 − 100)/(8/√25) = 5/1.6 = 3.125. df = 24. Critical value t_{0.025, 24} = 2.064. Since |3.125| > 2.064, reject H₀ at 5%. Alternatively, p-value ≈ 0.0046 < 0.05. Strong evidence that mean differs from 100.

### Q43. Two-sample t: n₁ = 20, X̄₁ = 50, s₁ = 6; n₂ = 25, X̄₂ = 45, s₂ = 8. Welch test at α = 0.05.
**Model answer:** SE = √(36/20 + 64/25) = √(1.8 + 2.56) = √4.36 = 2.088. t = (50−45)/2.088 = 2.394. df ≈ (1.8+2.56)²/[(1.8)²/19 + (2.56)²/24] = 19.0/(0.170 + 0.273) = 42.9; use df = 42. Critical t_{0.025, 42} ≈ 2.02. Since 2.394 > 2.02, reject H₀. Means significantly differ.

### Q44. Sample proportion p̂ = 0.35 in n = 400. Test H₀: p = 0.30 at 5% (two-sided).
**Model answer:** z = (0.35 − 0.30)/√(0.30·0.70/400) = 0.05/√(0.000525) = 0.05/0.0229 = 2.18. |z| > 1.96, reject H₀. p-value = 2·P(Z > 2.18) = 2(0.0146) = 0.029 < 0.05. Evidence p ≠ 0.30.

### Q45. Required sample size for estimating μ within ±2 units at 95% confidence, σ ≈ 15.
**Model answer:** n = (1.96 · 15 / 2)² = (14.7)² = 216.09. Round up to n = 217. With this sample, the 95% CI will have width at most ±2.

---

## Part F: Applications (Q46-50)

### Q46. A survey of 500 voters shows 55% support policy. Can we conclude majority support at α = 0.05?
**Model answer:** H₀: p = 0.5 vs H₁: p > 0.5. z = (0.55 − 0.50)/√(0.50·0.50/500) = 0.05/0.0224 = 2.236. p-value = P(Z > 2.236) = 0.0127 < 0.05. Reject H₀; evidence of majority support. Report also 95% CI: 0.55 ± 1.96·√(0.55·0.45/500) = [0.506, 0.594] — doesn't include 0.5.

### Q47. Before/after measurements on 12 patients' blood pressure. Mean difference = −8, s_d = 6. Did the drug reduce BP?
**Model answer:** Paired t-test. H₀: μ_d = 0 vs H₁: μ_d < 0. t = −8/(6/√12) = −8/1.732 = −4.62. df = 11. t_{0.05, 11} = −1.796. Since −4.62 < −1.796, reject H₀. Strong evidence drug reduces BP. 95% CI: −8 ± 2.20(1.732) = [−11.8, −4.2].

### Q48. A company claims average delivery time ≤ 3 days. Sample: n = 36, X̄ = 3.5 days, s = 0.8. Test the claim at α = 0.05.
**Model answer:** H₀: μ ≤ 3 vs H₁: μ > 3. t = (3.5 − 3)/(0.8/6) = 0.5/0.133 = 3.75. df = 35. t_{0.05, 35} = 1.69. Since 3.75 > 1.69, reject H₀. Strong evidence delivery time exceeds 3 days; the claim is not supported.

### Q49. You test 20 hypotheses at α = 0.05 individually. What is P(at least one false positive) under H₀?
**Model answer:** If all nulls true and tests independent: P(no Type I errors) = (0.95)^20 = 0.358. P(at least one false positive) = 1 − 0.358 = 0.642. That's 64% — inflated Type I error. Use Bonferroni (α_individual = 0.05/20 = 0.0025) or Benjamini-Hochberg for FDR control.

### Q50. A marketing A/B test shows 5.5% vs 5.0% conversion (n = 2000 each). Is the difference significant?
**Model answer:** Pooled p̂ = (110+100)/4000 = 0.0525. SE = √(0.0525·0.9475·(1/2000+1/2000)) = √(0.0000497) = 0.00705. z = (0.055 − 0.050)/0.00705 = 0.709. p-value = 2(0.239) = 0.478. Fail to reject H₀ — no significant difference. Practical question: with n = 2000, we lack power to detect small but potentially meaningful differences; consider larger sample or accept there's no meaningful effect.

---

**Exam tip:** Every hypothesis test answer must include: (1) clearly stated H₀ and H₁, (2) chosen significance level α, (3) test statistic with its distribution under H₀, (4) critical value or p-value, (5) explicit decision (reject or fail to reject), (6) interpretation in the original context, (7) check of assumptions. Missing any of these loses marks.
