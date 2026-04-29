# ST2134 — Hypothesis Testing Fundamentals: 50 Exam Questions with Model Answers

---

## Part A: Framework (Q1-10)

### Q1. Define a hypothesis test.
**Model answer:** A statistical procedure for making a decision about a parameter based on sample data. Starts with H₀ (null hypothesis) and H₁ (alternative). Uses a test statistic T(X) and a rejection region R. Decision: reject H₀ if T(X) ∈ R; otherwise fail to reject.

### Q2. Define null and alternative hypotheses.
**Model answer:** H₀: null, the status-quo claim to be challenged. H₁: alternative, the claim we'd need evidence to support. Example: H₀: μ = 0; H₁: μ ≠ 0. Formulated before seeing data. Asymmetric roles: test is designed to have small Type I error.

### Q3. Define simple and composite hypotheses.
**Model answer:** Simple: H₀: θ = θ₀ specifies a single distribution. Example: H₀: μ = 0 with σ known. Composite: H₀: θ ∈ Θ₀ specifies a set. Example: H₀: μ ≤ 0 or H₀ has unknown nuisance parameters. Most real tests have composite H₀ or H₁.

### Q4. Define Type I and Type II errors.
**Model answer:** Type I (α): reject H₀ when H₀ true. False positive. Type II (β): fail to reject H₀ when H₀ false. False negative. P(Type I) = α (significance level). P(Type II) = β, depends on true parameter in H₁. Power = 1 − β.

### Q5. Define the significance level and power.
**Model answer:** Significance level α = P(Type I error) = P(reject H₀ | H₀ true). Usually set to 0.05. Power 1 − β = P(reject H₀ | H₁ true). Depends on true θ ∈ H₁, sample size, α, variance.

### Q6. Define a test statistic.
**Model answer:** A function T(X) of the sample whose sampling distribution is known (or approximable) under H₀. Provides the basis for deciding whether to reject H₀. Examples: Z = (X̄ − μ₀)/(σ/√n), t, F, χ². Should be sensitive to departures from H₀ in the direction of H₁.

### Q7. Define the rejection region.
**Model answer:** A set R in the range of T(X) such that we reject H₀ if T(X) ∈ R. Designed so P(T ∈ R | H₀) = α. Placement depends on H₁: two-sided R = {T : |T| > c}, one-sided R = {T > c} or {T < c}.

### Q8. Define the p-value.
**Model answer:** Probability, under H₀, of observing a test statistic at least as extreme as the one observed. For two-sided: p = P(|T| ≥ |t_obs| | H₀). Small p-value = data inconsistent with H₀. Reject H₀ if p < α.

### Q9. Compare fixed-α and p-value approaches.
**Model answer:** Fixed α: decide α in advance (e.g., 0.05); reject if T in rejection region. Binary decision. P-value: report continuous measure of evidence. More informative; allows reader to choose α. Standard practice: report p-value alongside decision.

### Q10. State the four-step testing protocol.
**Model answer:** (1) State H₀ and H₁. (2) Choose α (usually 0.05) and identify test statistic with its null distribution. (3) Compute T from data; compare to critical value OR compute p-value. (4) State decision and interpret in context of the research question.

---

## Part B: Standard Tests (Q11-20)

### Q11. Describe the one-sample z-test.
**Model answer:** Tests H₀: μ = μ₀ when σ is known. Assumes iid sample from N(μ, σ²) (or large n via CLT). Z = (X̄ − μ₀)/(σ/√n) ~ N(0, 1) under H₀. Rejection region: |Z| > z_{α/2} for two-sided; Z > z_α for one-sided right.

### Q12. Describe the one-sample t-test.
**Model answer:** Tests H₀: μ = μ₀ when σ is unknown. Assumes iid sample from N(μ, σ²) or large n. T = (X̄ − μ₀)/(s/√n) ~ t(n−1) under H₀. Same rejection rules as z-test but with t critical values. Robust to mild non-normality for n ≥ 30.

### Q13. Describe the two-sample t-test (pooled).
**Model answer:** Tests H₀: μ₁ = μ₂ assuming equal variances. T = (X̄₁ − X̄₂)/(s_p · √(1/n₁ + 1/n₂)), where s²_p = [(n₁−1)s²₁ + (n₂−1)s²₂]/(n₁+n₂−2). Under H₀ and normality: T ~ t(n₁+n₂−2).

### Q14. Describe Welch's t-test.
**Model answer:** Tests H₀: μ₁ = μ₂ without assuming equal variances. T = (X̄₁ − X̄₂)/√(s²₁/n₁ + s²₂/n₂). Uses Welch-Satterthwaite df. Recommended default — comparable power to pooled when variances equal, robust when unequal.

### Q15. Describe the paired t-test.
**Model answer:** For matched pairs, compute differences d_i = X_i − Y_i. T = d̄/(s_d/√n) ~ t(n−1) under H₀: μ_d = 0. More powerful than independent samples when pairing removes between-subjects variance.

### Q16. Describe the chi-squared test for variance.
**Model answer:** Tests H₀: σ² = σ²₀ for normal data. Statistic: χ² = (n−1)s²/σ²₀ ~ χ²(n−1) under H₀. Rejection region depends on H₁: two-sided uses two critical values. Sensitive to non-normality.

### Q17. Describe the F-test for equality of two variances.
**Model answer:** Tests H₀: σ²₁ = σ²₂ from two independent normal samples. F = s²₁/s²₂ ~ F(n₁−1, n₂−1) under H₀. Assumes normality — sensitive to violations. Alternative: Levene's test (robust).

### Q18. State the z-test for one proportion.
**Model answer:** Tests H₀: p = p₀. Z = (p̂ − p₀)/√(p₀(1−p₀)/n). Under H₀ and large n (np₀, n(1−p₀) ≥ 10): Z ~ N(0, 1). Uses null value p₀ in SE (not p̂).

### Q19. State the z-test for two proportions.
**Model answer:** Tests H₀: p₁ = p₂. Z = (p̂₁ − p̂₂)/√(p̂(1−p̂)(1/n₁ + 1/n₂)), where pooled p̂ = (x₁+x₂)/(n₁+n₂). Uses pooled proportion under H₀.

### Q20. State the chi-squared test for independence.
**Model answer:** Tests H₀: two categorical variables independent. χ² = Σ (O−E)²/E, df = (r−1)(c−1). E = (row total × col total)/grand total. Requires expected counts ≥ 5 in most cells. Sensitive to large n (even small effects become significant).

---

## Part C: Rejection Region and Critical Values (Q21-30)

### Q21. Construct the rejection region for one-sided z-test.
**Model answer:** H₁: μ > μ₀ (right-tailed). R = {Z > z_α}. For α = 0.05: z_{0.05} = 1.645. Reject H₀ if computed z exceeds 1.645. Only extreme positive values reject.

### Q22. Construct two-sided rejection region.
**Model answer:** H₁: μ ≠ μ₀. R = {|Z| > z_{α/2}}. For α = 0.05: z_{0.025} = 1.96. Reject if |z| > 1.96. Symmetric; both extremes reject. Uses α/2 on each side.

### Q23. Compare one-sided and two-sided tests.
**Model answer:** One-sided: more powerful to detect effects in specified direction; cannot detect opposite direction. Two-sided: catches departures in either direction; less powerful per direction. Choice by research question — use one-sided only when opposite direction is theoretically impossible or equivalent to null.

### Q24. Define the critical value.
**Model answer:** Boundary between rejection and non-rejection regions. For z-test two-sided at α = 0.05: critical values are ±z_{0.025} = ±1.96. Reject if |Z| > 1.96; fail to reject if |Z| ≤ 1.96.

### Q25. Relate rejection region to p-value.
**Model answer:** Reject H₀ iff p-value < α iff T in rejection region. Two equivalent decisions. P-value provides more information (strength of evidence); rejection region is binary. Report both.

### Q26. Type I error probability under H₀.
**Model answer:** P(Type I) = P(T ∈ R | H₀) = α. Designed by construction of R. If R = {|Z| > 1.96} and Z ~ N(0,1) under H₀: P(|Z| > 1.96) = 0.05 = α. Controls false positives at designed rate.

### Q27. Compute Type II error.
**Model answer:** β = P(fail to reject H₀ | true θ = θ_1 ∈ H₁). Depends on specific θ_1. Example: test H₀: μ = 0, H₁: μ ≠ 0; true μ = 2. β = P(|Z| ≤ 1.96 when μ = 2). With larger θ_1 − θ_0, β smaller (higher power).

### Q28. Calculate power for specific alternative.
**Model answer:** For H₀: μ = 0, H₁: μ = δ, σ known, sample size n: power = P(Z > z_α | μ = δ) = 1 − Φ(z_α − δ√n/σ). Increases with: δ (effect size), n (sample size), α (test level). Decreases with σ.

### Q29. How does sample size affect Type I and Type II errors?
**Model answer:** Type I (α) controlled by test design — doesn't change with n. Type II (β) decreases as n increases. So power increases. Larger n = more precise estimation = more sensitive test. Trade-off: cost of data.

### Q30. What does effect size mean in hypothesis testing?
**Model answer:** Effect size = magnitude of departure from H₀. Standardised examples: Cohen's d (mean difference), Pearson's r (correlation), φ (chi-squared). Affects power: larger effect = more power. Report effect size alongside p-value for interpretation.

---

## Part D: Common Mistakes (Q31-40)

### Q31. What is the "failure to reject = accept H₀" mistake?
**Model answer:** Statistical logic: if p > α, we fail to reject H₀. This means the data don't contradict H₀, but don't confirm it. Absence of evidence is not evidence of absence. Correct language: "insufficient evidence to reject H₀".

### Q32. P-value vs probability of H₀.
**Model answer:** p-value = P(data | H₀), not P(H₀ | data). Common misinterpretation. To compute P(H₀ | data) requires Bayesian analysis with prior probabilities. Treating small p as "probability H₀ is true" conflates conditional probabilities.

### Q33. What is p-hacking?
**Model answer:** Manipulating data or analysis to achieve p < 0.05. Forms: (1) Running many tests, reporting only significant. (2) Stopping data collection at first significant result. (3) Selecting predictors post-hoc. (4) Multiple analyses, choosing favorable one. Produces false positives. Remedies: pre-registration, correction for multiple testing.

### Q34. Multiple comparisons problem.
**Model answer:** With m independent tests at α = 0.05, P(at least one false positive) = 1 − (0.95)^m. With m = 20: 0.64. Remedies: (1) Bonferroni: α_i = α/m. (2) Holm: sequential rejection. (3) False discovery rate (Benjamini-Hochberg). (4) Pre-registered primary hypothesis.

### Q35. Statistical vs practical significance.
**Model answer:** Statistical significance: p < α, detecting that effect ≠ null. Practical significance: effect size meaningful in context. Large n can produce p < 0.001 for trivial differences (e.g., 0.001 mm difference in heights). Always report effect size alongside p-value.

### Q36. Power analysis for sample size.
**Model answer:** Compute required n given desired power (1−β), effect size δ, α, σ. Formula for two-sided z-test: n = [(z_{α/2} + z_β)·σ/δ]². Conventional: power = 0.80, α = 0.05. Essential before data collection to avoid underpowered studies.

### Q37. Overpowered study risk.
**Model answer:** Very large sample can make trivial effects statistically significant. Risk: over-interpreting minor deviations as meaningful. Remedy: pre-specify minimum practical effect; assess effect size, not just p-value. Report CI width: narrow CI with small estimate is uninformative.

### Q38. Underpowered study risk.
**Model answer:** Too small n: high β, likely to miss real effects. Risks: (1) False negatives. (2) Winner's curse: if significant despite low power, effect likely overestimated. (3) Publication bias. Prevention: power analysis pre-study. Result: inability to make definitive claims.

### Q39. Fishing expeditions.
**Model answer:** Testing many hypotheses post-hoc without correction. Inflates Type I error. Distinguishable from exploratory analysis: (a) Generate hypothesis from data (not confirm). (b) Report all analyses, not just significant. (c) Validate on independent data. Pre-registration clarifies.

### Q40. Publication bias.
**Model answer:** Tendency to publish significant results over null results. Creates distorted literature. Effects appear larger than truth. Meta-analyses may over-estimate. Remedies: (1) Publish null results. (2) Pre-register studies. (3) Funnel plots in meta-analysis. (4) File-drawer effect analyses.

---

## Part E: Examples (Q41-45)

### Q41. Test H₀: μ = 100, H₁: μ ≠ 100, given X̄ = 104, σ = 10, n = 25.
**Model answer:** Z = (104 − 100)/(10/5) = 4/2 = 2. Two-sided p = 2·P(Z > 2) = 2·0.0228 = 0.046 < 0.05. Reject H₀. Evidence that μ ≠ 100. Effect size (standardised): (104−100)/10 = 0.4 (moderate). CI: 104 ± 1.96·2 = [100.08, 107.92] (consistent with rejection of 100).

### Q42. Paired t-test: d̄ = 3, s_d = 5, n = 20.
**Model answer:** T = 3/(5/√20) = 3/1.118 = 2.68. df = 19. Two-sided p ≈ 2·P(t_{19} > 2.68) ≈ 0.015 < 0.05. Reject H₀: μ_d = 0. Evidence of mean difference. 95% CI: 3 ± t_{0.025, 19}·1.118 = 3 ± 2.094·1.118 = [0.66, 5.34]. Practically meaningful depending on context.

### Q43. Two-proportion z-test: n₁ = 200, x₁ = 80; n₂ = 250, x₂ = 75.
**Model answer:** p̂₁ = 0.40, p̂₂ = 0.30. Pooled p̂ = 155/450 = 0.344. SE = √(0.344·0.656·(1/200+1/250)) = √(0.0010) = 0.0448. Z = (0.40 − 0.30)/0.0448 = 2.23. p = 2(0.013) = 0.026 < 0.05. Reject H₀: p₁ = p₂. Evidence of different proportions.

### Q44. Chi-squared for independence in 3×2 table, χ² = 8.5.
**Model answer:** df = (3−1)(2−1) = 2. Critical χ²_{0.05, 2} = 5.99. Since 8.5 > 5.99, reject H₀ of independence. p ≈ 0.014. Variables associated. Examine cell residuals to find which combinations drive the association. Report Cramér's V for effect size.

### Q45. Power analysis for two-sample t: find n for d = 0.5, α = 0.05, power = 0.80.
**Model answer:** For two-sample with equal n per group: n_per_group = (z_{α/2} + z_β)² · 2 / d² = (1.96 + 0.84)² · 2 / 0.25 = 7.84 · 8 = 62.72. Round up to 63 per group, 126 total. Medium effect, conventional power requirements.

---

## Part F: Application (Q46-50)

### Q46. A quality engineer claims mean bolt length = 10 cm. Sample n = 50, X̄ = 10.3, s = 0.8. Test at α = 0.05.
**Model answer:** H₀: μ = 10 vs H₁: μ ≠ 10. T = (10.3 − 10)/(0.8/√50) = 0.3/0.113 = 2.65. df = 49. Two-sided p ≈ 2(0.005) = 0.010 < 0.05. Reject H₀. Mean bolt length differs from claimed 10 cm. Report 95% CI: [10.07, 10.53]. Practical: 0.3 cm difference may or may not matter for application.

### Q47. Randomised trial: treatment mean 55.2 (SD 10, n=40); control 50.1 (SD 12, n=40).
**Model answer:** Welch's t-test: T = (55.2 − 50.1)/√(100/40 + 144/40) = 5.1/2.47 = 2.07. df ≈ 76. Two-sided p ≈ 0.042 < 0.05. Reject H₀. Treatment effect significant. Effect size: Cohen's d = 5.1/√((100+144)/2) ≈ 0.46 (small-medium). Report CI and clinical significance.

### Q48. Test for fairness of a coin: 58 heads in 100 flips.
**Model answer:** H₀: p = 0.5 vs H₁: p ≠ 0.5. Z = (0.58 − 0.5)/√(0.5·0.5/100) = 0.08/0.05 = 1.6. Two-sided p = 0.110 > 0.05. Fail to reject. Insufficient evidence coin is unfair. Note: marginal — with n = 200 and same rate, would likely reject. Report sample size consideration.

### Q49. Compare pre-test and post-test scores for 30 students: paired t-test.
**Model answer:** Paired design. Compute d_i = post − pre. Calculate d̄ and s_d. T = d̄/(s_d/√30). df = 29. Compare to t_{0.025, 29} = 2.045. Decision based on |T| vs critical value. Advantages of paired: removes between-student variability, focuses on learning gain. Report mean improvement and CI.

### Q50. Describe the full hypothesis testing process.
**Model answer:** (1) Identify research question and appropriate test. (2) State H₀ and H₁ precisely. (3) Choose α based on context (default 0.05). (4) Check assumptions (normality, independence, equal variance, etc.). (5) Compute test statistic and its null distribution. (6) Compare to critical value OR compute p-value. (7) State decision: reject or fail to reject. (8) Interpret in context with effect size and CI. (9) Discuss limitations (power, assumption violations, multiple testing). (10) Document for reproducibility.

---

**Exam tip:** For hypothesis testing questions, always: (1) state H₀ and H₁ in notation, (2) identify test statistic and its null distribution, (3) check assumptions explicitly, (4) compute test statistic showing arithmetic, (5) report p-value or compare to critical value, (6) state decision and interpret in context, (7) address effect size and practical significance, (8) consider power for non-rejection cases.
