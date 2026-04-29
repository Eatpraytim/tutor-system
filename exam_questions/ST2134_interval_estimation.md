# ST2134 — Interval Estimation: 50 Exam Questions with Model Answers

---

## Part A: Fundamentals (Q1-10)

### Q1. Define a confidence interval.
**Model answer:** A (1−α)·100% confidence interval for θ is a random interval [L(X), U(X)] such that P(L(X) ≤ θ ≤ U(X)) = 1 − α for all θ. Interpretation: if we repeatedly sampled and constructed intervals, 95% (for α = 0.05) would contain θ. θ is fixed; the interval is random.

### Q2. Define a pivot.
**Model answer:** A function Q(X, θ) whose distribution does not depend on θ. Example: (X̄ − μ)/(σ/√n) ~ N(0, 1) when σ known — distribution free of μ. Pivots are the foundation for constructing CIs: rearrange inequalities on Q to isolate θ.

### Q3. Construct a pivotal quantity for normal mean with known σ.
**Model answer:** Z = (X̄ − μ)/(σ/√n). For iid X_i ~ N(μ, σ²): Z ~ N(0, 1) exactly. Distribution doesn't depend on μ. P(−z_{α/2} ≤ Z ≤ z_{α/2}) = 1 − α. Rearrange: P(X̄ − z_{α/2}σ/√n ≤ μ ≤ X̄ + z_{α/2}σ/√n) = 1 − α.

### Q4. Construct a pivotal quantity for normal mean with unknown σ.
**Model answer:** T = (X̄ − μ)/(s/√n). For iid X_i ~ N(μ, σ²): T ~ t(n−1) regardless of σ². Foundation of t-interval: X̄ ± t_{α/2, n−1} s/√n. t has heavier tails than Z; wider interval for same confidence.

### Q5. State the duality between CIs and hypothesis tests.
**Model answer:** A (1−α) CI consists of all parameter values θ₀ that would NOT be rejected by a level-α two-sided test of H₀: θ = θ₀. Equivalently: test rejects iff θ₀ not in CI. Invertibility: CI construction and hypothesis testing are two sides of the same procedure.

### Q6. Compare exact and approximate CIs.
**Model answer:** Exact: CI has coverage P(θ ∈ CI) = 1 − α under assumptions (e.g., normality). Example: t-interval. Approximate: CI has coverage → 1 − α as n → ∞ (asymptotic). Example: CI based on MLE asymptotic normality. Use exact when assumptions plausible; asymptotic with large n.

### Q7. Define coverage probability.
**Model answer:** P(θ ∈ CI). For a good CI, coverage = 1 − α. Actual (empirical) coverage may deviate: approximate CIs for small samples or skewed distributions. Coverage < 1 − α indicates liberal interval (under-covers); > 1 − α conservative (over-covers).

### Q8. What are one-sided confidence intervals?
**Model answer:** Interval of form [L, ∞) or (−∞, U]. Constructed when only direction matters. Example: one-sided 95% CI for μ: [X̄ − z_{0.05} · σ/√n, ∞). Uses full α on one side (e.g., z_{0.05} = 1.645 instead of 1.96). Narrower on one side, no bound on the other.

### Q9. Describe symmetric vs asymmetric CIs.
**Model answer:** Symmetric: L = θ̂ − c, U = θ̂ + c (standard for normal-based). Asymmetric: if sampling distribution is skewed, CI should also be asymmetric. Example: log-transform, construct CI on log scale, back-transform. Correct for skewness.

### Q10. What is a prediction interval?
**Model answer:** Interval for a new observation Y (not parameter). Accounts for both sampling variability (CI for mean) and inherent variability σ². Wider than CI for mean. For normal data: Y_new ∈ X̄ ± t_{α/2, n−1} · s · √(1 + 1/n) with 1 − α probability.

---

## Part B: CIs for Normal Parameters (Q11-20)

### Q11. State a (1−α) CI for μ when σ is known.
**Model answer:** X̄ ± z_{α/2} · σ/√n. Uses normal distribution (since σ known). Critical value: z_{α/2} = Φ⁻¹(1 − α/2). For 95%: z_{0.025} = 1.96. Requires normality or large n (CLT).

### Q12. State a (1−α) CI for μ when σ is unknown.
**Model answer:** X̄ ± t_{α/2, n−1} · s/√n, with df = n−1. Uses t-distribution (since s estimates σ). Critical value wider than z for small n. For 95%, n = 10: t_{0.025, 9} = 2.262 (vs z = 1.96).

### Q13. Derive the t-interval formula.
**Model answer:** T = (X̄ − μ)/(s/√n) ~ t(n−1). P(−t_{α/2, n−1} ≤ T ≤ t_{α/2, n−1}) = 1 − α. Substitute T and rearrange: P(X̄ − t_{α/2, n−1} s/√n ≤ μ ≤ X̄ + t_{α/2, n−1} s/√n) = 1 − α.

### Q14. State a (1−α) CI for σ² from a normal sample.
**Model answer:** Using (n−1)s²/σ² ~ χ²(n−1): CI = [(n−1)s²/χ²_{α/2, n−1}, (n−1)s²/χ²_{1−α/2, n−1}]. Asymmetric (χ² is skewed). For σ: take square roots of endpoints.

### Q15. Derive the CI for σ².
**Model answer:** V = (n−1)s²/σ² ~ χ²(n−1). P(χ²_{1−α/2, n−1} ≤ V ≤ χ²_{α/2, n−1}) = 1 − α. Rearrange: P((n−1)s²/χ²_{α/2} ≤ σ² ≤ (n−1)s²/χ²_{1−α/2}) = 1 − α.

### Q16. State the CI for difference of means (independent samples, equal variances).
**Model answer:** (X̄₁ − X̄₂) ± t_{α/2, n₁+n₂−2} · s_p · √(1/n₁ + 1/n₂), where pooled variance s²_p = [(n₁−1)s²₁ + (n₂−1)s²₂]/(n₁+n₂−2). Uses pooled t-distribution with df = n₁ + n₂ − 2.

### Q17. State the Welch CI (unequal variances).
**Model answer:** (X̄₁ − X̄₂) ± t_{α/2, ν} · √(s²₁/n₁ + s²₂/n₂), where ν is Welch-Satterthwaite df: ν = (s²₁/n₁ + s²₂/n₂)² / [(s²₁/n₁)²/(n₁−1) + (s²₂/n₂)²/(n₂−1)]. Default when equal-variance assumption doubtful.

### Q18. State the paired t-interval.
**Model answer:** For matched pairs, compute differences d_i = X_i − Y_i. CI for mean difference μ_d: d̄ ± t_{α/2, n−1} · s_d/√n. Uses within-pair comparison, more efficient than independent samples when pairing is meaningful.

### Q19. CI for ratio of variances.
**Model answer:** σ²₁/σ²₂ · 1/F_{α/2, n₁−1, n₂−1} ≤ ratio ≤ σ²₁/σ²₂ · F_{α/2, n₂−1, n₁−1}. Uses F-distribution. Asymmetric. Test of equality: check if 1 is in interval.

### Q20. Interpret a 95% CI for μ of [48, 52].
**Model answer:** 95% confident that population mean lies between 48 and 52. NOT "P(μ ∈ [48, 52]) = 0.95" (μ is fixed). NOT "95% of observations are in [48, 52]". Interpretation refers to the long-run frequency of the procedure: 95% of such intervals constructed from repeated samples contain the true μ.

---

## Part C: Asymptotic CIs (Q21-30)

### Q21. Construct asymptotic CI using MLE.
**Model answer:** Under regularity, √n(θ̂_MLE − θ) →_d N(0, 1/I(θ)). Approximate 95% CI: θ̂_MLE ± 1.96 · √(1/(nI(θ̂))). Plug in θ̂ for unknown I. Valid for large n.

### Q22. CI for Bernoulli proportion (Wald form).
**Model answer:** p̂ ± z_{α/2} · √(p̂(1−p̂)/n). Uses asymptotic normality of p̂. Poor for small n or extreme p (close to 0 or 1). Use only when np̂ > 10 and n(1−p̂) > 10.

### Q23. CI for Bernoulli proportion (Wilson score interval).
**Model answer:** More accurate than Wald for small n or extreme p. Score-based: [p̂(1−p̂) + z²/(2n)] / (1 + z²/n), with appropriate ± term. Concentrates around p̂ with asymmetric width near boundaries. Preferred for most applications.

### Q24. CI for Poisson rate.
**Model answer:** Wald: λ̂ ± z_{α/2}√(λ̂/n). Alternative: exact gamma-based CI. For count data X ~ Poisson(nλ): [χ²_{1−α/2, 2X}/(2n), χ²_{α/2, 2(X+1)}/(2n)] using chi-squared quantiles.

### Q25. CI for ratio (Fieller's method).
**Model answer:** For ratio θ = μ₁/μ₂: construct CI by inverting test rather than simple transformation. Fieller's: solve quadratic in θ from P(|X̄₁ − θX̄₂|² ≤ c²) formulation. Provides exact (normal-based) CI. More complex than Delta-method approximation but more accurate.

### Q26. CI using the Delta method.
**Model answer:** If θ̂ ~ N(θ, σ²/n), find CI for g(θ). By Delta: g(θ̂) ~ N(g(θ), [g'(θ)]² σ²/n). CI: g(θ̂) ± z_{α/2}|g'(θ̂)|σ/√n. Valid for large n where linearisation holds.

### Q27. Apply Delta for CI of 1/μ.
**Model answer:** Let g(μ) = 1/μ. g'(μ) = −1/μ². g(X̄) = 1/X̄ ~ N(1/μ, σ²/(nμ⁴)) approximately. CI: 1/X̄ ± z_{α/2} · σ/(X̄²√n). Approximate; back-transforms are often better for strictly positive quantities.

### Q28. Transformation-based CIs.
**Model answer:** If g(θ) is more normal than θ, construct CI on g scale, back-transform. Examples: log for ratios, Fisher's z = (1/2)log((1+r)/(1−r)) for correlation. Advantages: better coverage, symmetric asymptotic distribution. Standard for skewed distributions.

### Q29. Fisher's z-transformation for correlation CI.
**Model answer:** Z = (1/2)log((1+r)/(1−r)) ~ approximately N((1/2)log((1+ρ)/(1−ρ)), 1/(n−3)). CI for Z: Z ± z_{α/2}/√(n−3). Back-transform: r_CI = (e^{2Z_CI} − 1)/(e^{2Z_CI} + 1). More accurate than direct normal approximation on r.

### Q30. CI for odds ratio.
**Model answer:** For 2×2 table with OR = ad/bc. log(OR) is approximately normal with SE ≈ √(1/a + 1/b + 1/c + 1/d). CI on log scale: log(OR) ± 1.96 · SE. Exponentiate for asymmetric CI on OR scale. Standard in epidemiology.

---

## Part D: Sample Size and Design (Q31-40)

### Q31. Calculate sample size for CI of specified width.
**Model answer:** For CI of μ with margin E at confidence 1−α: E = z_{α/2}·σ/√n, so n = (z_{α/2}·σ/E)². Requires σ estimate (from pilot or literature). Round up. Example: E = 2, σ = 10, 95%: n = (1.96·10/2)² = 96.

### Q32. Sample size for proportion CI.
**Model answer:** n = (z_{α/2})²·p(1−p)/E². Use p = 0.5 for max variance (conservative). Example: E = 0.03, 95%: n = (1.96)²·0.25/0.0009 = 1,068. Needed margin of error more than sampling proportion itself.

### Q33. Finite population correction.
**Model answer:** For sampling without replacement from finite N: n* = n / [1 + (n−1)/N]. Reduces required n when sampling fraction large (n/N > 5%). At n = N: n* = 1 (population enumerated). Important for surveys.

### Q34. Sample size vs precision trade-off.
**Model answer:** Precision (SE) ∝ 1/√n. To halve margin of error: quadruple n. Diminishing returns — each extra observation contributes less precision. Cost-benefit analysis: is extra precision worth additional data collection?

### Q35. Power analysis vs CI precision.
**Model answer:** Different goals. Power analysis: sample size to detect effect of given size. CI precision: sample size for margin of error. Related but distinct. For the same problem, power and precision requirements may give different n. Choose larger.

### Q36. Describe precision-based design.
**Model answer:** Design to achieve pre-specified CI width. Alternative to power-based design. Advantages: avoids subjective "minimum detectable effect" choice. Steps: (1) Set E (tolerable width). (2) Estimate σ. (3) Compute n = (z·σ/E)². Especially useful for estimation studies where magnitude (not significance) matters.

### Q37. CI width factors.
**Model answer:** Width proportional to: (1) Critical value z (increases with confidence level). (2) Standard error σ/√n (decreases with √n). (3) Skewness/transformation requirements. Reduce width by: (a) larger n, (b) stratification to reduce σ², (c) paired/matched designs.

### Q38. Describe stratified sampling benefit for CIs.
**Model answer:** Stratified: different means per stratum, but within-stratum variance lower than overall. SE = √(Σ (w_i² σ_i²/n_i)), where w_i = stratum weights, σ_i = within-stratum SD. Smaller than simple random SE when strata differ on outcome.

### Q39. Design effect.
**Model answer:** Deff = actual variance / SRS variance. Cluster sampling typically Deff > 1 (clusters correlated); stratified Deff < 1. Sample size adjustment: n_effective = n / Deff. Important in complex surveys (ONS, WHO).

### Q40. Margin of error vs standard error.
**Model answer:** Margin of error = critical value × SE. Half-width of CI. Example: 95% margin = 1.96 × SE. SE is about spread of estimator; margin is interpreted precision at chosen confidence. Both decrease with larger n.

---

## Part E: Applications and Interpretation (Q41-45)

### Q41. Interpret a 95% CI = [2.1, 5.8] for a treatment effect.
**Model answer:** 95% confident true treatment effect lies in [2.1, 5.8]. Not a probability statement about a fixed θ. Clinically: effect is positive (0 not in CI), magnitude between 2.1 and 5.8. Statistical significance: yes (0 excluded). Practical significance: depends on context — 2.1 may or may not be clinically meaningful.

### Q42. Compare a 95% CI vs a 99% CI.
**Model answer:** Same estimate, same data. 99% CI wider than 95% (larger critical value). Example: z_{0.025} = 1.96 vs z_{0.005} = 2.576. 99% CI is more conservative — less likely to miss the true value but longer. Trade-off between reliability and precision.

### Q43. What happens to CI as n increases?
**Model answer:** Width decreases ∝ 1/√n. For very large n, CI narrows to a single point (conceptually). But confidence level unchanged. Large n can produce narrow CIs that exclude even trivially-different parameter values — statistical but not practical significance.

### Q44. When might a CI contain an implausible value?
**Model answer:** If the parameter space is constrained (e.g., σ² ≥ 0) and the asymptotic CI is symmetric, the lower bound may be negative. Solutions: (1) Truncate at boundary (crude). (2) Use exact CIs (e.g., for σ²: chi-squared-based). (3) Transform (e.g., log for positive parameters) and back-transform CI.

### Q45. Describe a percentile-based (non-parametric) CI.
**Model answer:** Use bootstrap: resample data with replacement B times, compute θ̂* each time. CI: [θ̂*_{α/2}, θ̂*_{1−α/2}], the α/2 and 1−α/2 quantiles of bootstrap distribution. Doesn't require normality. Good for skewed distributions. Better alternatives: BCa (bias-corrected accelerated) for asymmetric.

---

## Part F: Application (Q46-50)

### Q46. A clinical trial shows mean effect = 3.2, SE = 1.5, n = 30. Construct 95% CI for true effect.
**Model answer:** df = 29, t_{0.025, 29} = 2.045. CI = 3.2 ± 2.045(1.5) = 3.2 ± 3.07 = [0.13, 6.27]. Interpretation: 95% confident true effect is between 0.13 and 6.27 units. Since 0 barely excluded, statistical significance marginal; effect size potentially meaningful. Report with caveats.

### Q47. Sample size calculation for a poll: predict election within ±2% at 99% confidence.
**Model answer:** E = 0.02, z_{0.005} = 2.576, p = 0.5 (conservative). n = (2.576)²(0.25)/(0.02)² = 6.64 · 0.25 / 0.0004 = 4,148. For 95% confidence: n = 2,401. Higher confidence requires substantially larger sample.

### Q48. Construct 95% CI for difference in proportions: p̂₁ = 0.55, n₁ = 500; p̂₂ = 0.45, n₂ = 450.
**Model answer:** Difference = 0.10. SE = √(p̂₁(1−p̂₁)/n₁ + p̂₂(1−p̂₂)/n₂) = √(0.000495 + 0.000550) = √0.001045 = 0.0323. CI = 0.10 ± 1.96(0.0323) = 0.10 ± 0.0633 = [0.037, 0.163]. Significantly positive (0 excluded).

### Q49. CI for variance from n = 20 observations, s² = 100.
**Model answer:** (n−1)s²/σ² ~ χ²(19). χ²_{0.025, 19} = 32.85, χ²_{0.975, 19} = 8.91. CI = [19·100/32.85, 19·100/8.91] = [57.85, 213.24]. For σ: [√57.85, √213.24] = [7.60, 14.60]. Asymmetric around s = 10.

### Q50. Interpret a 95% CI for β_1 = [1.2, 4.8] in a regression context.
**Model answer:** 95% confident true slope β₁ lies in [1.2, 4.8]. Interpretation: a one-unit increase in X₁ is associated with 1.2 to 4.8 unit increase in E(Y), holding other variables constant. 0 excluded → statistically significant. Economic significance: depends on whether 1.2-4.8 is meaningful in units of Y. Business action: appropriate to act on this relationship.

---

**Exam tip:** For CI questions, always: (1) identify correct pivot (Z, T, χ², F, or asymptotic), (2) state the assumptions (normality, large n), (3) show formula derivation via inversion of probability statement, (4) compute correctly with proper critical value, (5) interpret as frequentist coverage statement (not probability about θ), (6) check if CI makes sense (e.g., excludes negative for σ²).
