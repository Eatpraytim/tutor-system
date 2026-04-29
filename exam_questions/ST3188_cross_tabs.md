# ST3188 — Cross-Tabs & Hypothesis Testing: 50 Exam Questions with Model Answers

---

## Part A: Cross-Tabulation Fundamentals (Q1-10)

### Q1. What is a cross-tabulation?
**Model answer:** A cross-tabulation (contingency table) displays the joint frequency distribution of two or more categorical variables. Rows represent categories of one variable, columns of another. Each cell shows the count of observations falling into that combination. Used for bivariate analysis of categorical data.

### Q2. Define marginal, conditional, and joint frequencies.
**Model answer:** Joint frequency: count in a specific cell (e.g., n_{ij}). Marginal frequency: row or column totals (n_{i.} or n_{.j}). Conditional frequency: frequency within a given category of one variable (e.g., distribution of Y given X = x). Marginals summarise univariate distributions; conditionals reveal dependencies.

### Q3. What are marginal and conditional probabilities in cross-tabs?
**Model answer:** Marginal P(Y=y): row/column total divided by grand total. Conditional P(Y=y | X=x): cell count divided by row or column total. Conditional probabilities reveal how Y's distribution changes with X. If conditional = marginal for all combinations, the variables are independent.

### Q4. Describe row percentages vs column percentages vs total percentages.
**Model answer:** Row %: within each row, percentages sum to 100% (conditional on row variable). Column %: within each column, sum to 100% (conditional on column variable). Total %: all cells sum to 100% (joint distribution). Choice depends on the research question — which variable is the "independent" or "predictor".

### Q5. What is Simpson's Paradox?
**Model answer:** A pattern in subgroups disappears or reverses when groups are aggregated. Example: two hospitals each have higher survival in a treatment group, but combined data shows treatment has lower survival because of confounding with hospital. Implication: always check for subgroup variation — aggregate-only analysis misleads.

### Q6. When would you prefer a cross-tab over other displays?
**Model answer:** (1) Both variables are categorical. (2) Want to see exact counts and proportions. (3) Need to present to non-technical audience. (4) Foundation for chi-squared tests. Limitations: hard to read with many categories; bar charts or mosaic plots may communicate patterns better visually.

### Q7. Define the total sample size in a 2×2 contingency table.
**Model answer:** n = Σ all cells = n_{11} + n_{12} + n_{21} + n_{22}. Also equals the sum of row totals or column totals. Essential for computing expected frequencies and chi-squared statistics.

### Q8. Explain odds and odds ratio.
**Model answer:** Odds = P(event)/P(no event) = p/(1−p). Odds ratio (OR) = odds₁/odds₂ = (p₁/(1−p₁))/(p₂/(1−p₂)). For 2×2 table with cells a,b,c,d: OR = (a·d)/(b·c). OR = 1: no association; OR > 1: positive; OR < 1: negative.

### Q9. What is relative risk (RR)?
**Model answer:** RR = P(event | group 1) / P(event | group 2) = p₁/p₂. Used in cohort studies. Different from OR: RR compares probabilities; OR compares odds. For rare events (p < 10%), OR ≈ RR. For common events, they diverge.

### Q10. Explain the purpose of a chi-squared test.
**Model answer:** Tests whether two categorical variables are independent. H₀: variables are independent (no association). H₁: variables are associated. Based on comparing observed frequencies with expected frequencies under independence. Can also test goodness of fit (H₀: observed matches hypothesised distribution).

---

## Part B: Chi-Squared Test (Q11-20)

### Q11. State the chi-squared test statistic formula.
**Model answer:** χ² = Σ (O − E)² / E, summed over all cells. O = observed frequency; E = expected frequency under independence = (row total × column total) / grand total. Under H₀, χ² ~ χ²(df) with df = (r−1)(c−1).

### Q12. State the assumptions of the chi-squared test.
**Model answer:** (1) Observations are independent. (2) Variables are categorical (nominal or ordinal). (3) Expected frequencies ≥ 5 in most cells (at least 80%). (4) Sample size reasonably large. For 2×2 tables with small expected counts, use Fisher's exact test instead.

### Q13. What are degrees of freedom for a chi-squared test?
**Model answer:** For independence test on r × c table: df = (r−1)(c−1). For goodness of fit with k categories and m estimated parameters: df = k − 1 − m. For 2×2 table: df = 1.

### Q14. How do you compute expected frequencies?
**Model answer:** Under H₀ (independence): E_{ij} = (row_i total × column_j total) / grand total. This assumes the probability of row i and column j is the product of marginals — the definition of independence.

### Q15. What is the continuity correction (Yates') and when to apply?
**Model answer:** For 2×2 tables with small samples, Yates' correction adjusts χ² = Σ (|O−E| − 0.5)² / E. Reduces upward bias of uncorrected chi-squared when expected frequencies are small. Applied only to 2×2 tables; modern practice often uses Fisher's exact test instead.

### Q16. Describe Fisher's exact test.
**Model answer:** Exact (not asymptotic) test of independence in 2×2 tables. Uses hypergeometric distribution to compute P(observed or more extreme | H₀). Preferred when expected frequencies are small (<5). Conservative and computationally intensive for large tables.

### Q17. What does a significant chi-squared result tell you?
**Model answer:** Variables are statistically significantly associated — observed frequencies differ from expected under independence. Does NOT tell: (i) strength of association, (ii) direction, (iii) which categories contribute. Must examine cell contributions or compute an effect size (Cramér's V, φ).

### Q18. Define Cramér's V.
**Model answer:** Effect size measure for chi-squared: V = √(χ² / [n · min(r−1, c−1)]). Range [0, 1]: 0 = no association; 1 = perfect. Unlike χ² (which grows with n), V is normalised. Rule of thumb: V > 0.3 moderate, V > 0.5 strong.

### Q19. What is the phi coefficient?
**Model answer:** φ = √(χ²/n). For 2×2 tables only. Range [0, 1] for 2×2. Equivalent to Pearson correlation for binary variables. Useful alternative to V when both variables have only two categories.

### Q20. When should you use a goodness-of-fit test rather than a test of independence?
**Model answer:** Goodness-of-fit: tests if one categorical variable's distribution matches a hypothesised distribution (e.g., theoretical probabilities, uniform, Poisson). Independence: tests association between two categorical variables. Choose based on the question: "does X fit a known distribution" (goodness-of-fit) vs "is X associated with Y" (independence).

---

## Part C: Hypothesis Testing for Means and Proportions (Q21-30)

### Q21. State the four steps in a hypothesis test.
**Model answer:** (1) State H₀ and H₁ (two-tailed or one-tailed). (2) Choose significance level α and compute test statistic. (3) Compare test statistic to critical value or compare p-value to α. (4) State decision (reject/fail to reject) and interpret in context of the research question.

### Q22. Define Type I and Type II errors in words.
**Model answer:** Type I error (α): rejecting H₀ when it's true — a "false alarm". Type II error (β): failing to reject H₀ when it's false — a "missed detection". Power (1−β) = probability of correctly rejecting a false null. Researcher can reduce α directly; reducing β requires increasing sample size or effect size.

### Q23. What is statistical power?
**Model answer:** Power = 1 − β = probability of correctly rejecting H₀ when H₁ is true. Depends on: (1) sample size, (2) true effect size, (3) significance level α, (4) population variability. Convention: aim for power ≥ 0.80. Low power means the study is unlikely to detect real effects.

### Q24. State the one-sample t-test statistic and conditions.
**Model answer:** t = (X̄ − μ₀) / (s/√n), df = n−1. Conditions: (1) random sample, (2) approximately normal data or large n (CLT). Tests H₀: μ = μ₀. Reject if |t| > t_{α/2, n−1} (two-tailed).

### Q25. Independent-samples t-test — state the pooled-variance formula.
**Model answer:** t = (X̄₁ − X̄₂) / [s_p · √(1/n₁ + 1/n₂)], where s²_p = [(n₁−1)s²₁ + (n₂−1)s²₂]/(n₁+n₂−2). df = n₁+n₂−2. Assumes equal variances and normality. For unequal variances, use Welch's t.

### Q26. State the paired samples t-test.
**Model answer:** Compute differences d_i = X_i − Y_i for each pair. t = d̄ / (s_d/√n), df = n−1. Tests H₀: μ_d = 0. More powerful than independent samples when pairs are correlated — reduces between-subjects variability.

### Q27. State the z-test for one proportion.
**Model answer:** z = (p̂ − p₀) / √(p₀(1−p₀)/n). Use p₀ in the SE for testing (since null assumes p = p₀). Conditions: np₀ ≥ 10, n(1−p₀) ≥ 10. Under H₀, z ~ N(0,1).

### Q28. State the z-test for two proportions.
**Model answer:** z = (p̂₁ − p̂₂) / √(p̂(1−p̂)(1/n₁ + 1/n₂)) where pooled p̂ = (x₁+x₂)/(n₁+n₂). Tests H₀: p₁ = p₂. Conditions: large samples, n_ip̂_i ≥ 10 and n_i(1−p̂_i) ≥ 10 for both groups.

### Q29. When do you use a non-parametric test?
**Model answer:** When: (1) data are ordinal or non-normal, (2) sample size is small and normality cannot be assumed, (3) distribution assumptions are violated. Examples: Mann-Whitney U (vs independent t-test), Wilcoxon signed-rank (vs paired t), Kruskal-Wallis (vs one-way ANOVA). Non-parametric tests use ranks rather than raw values.

### Q30. Explain the relationship between p-value, α, and reject/fail to reject.
**Model answer:** Reject H₀ if p < α (data are inconsistent with null). Fail to reject if p ≥ α (insufficient evidence against null). Smaller p-value = stronger evidence against H₀. Note: we "fail to reject" — we do NOT "accept" H₀. Absence of evidence is not evidence of absence.

---

## Part D: SPSS Output Interpretation (Q31-40)

### Q31. In SPSS, Pearson chi-squared value = 12.3, df = 2, p = 0.002. Interpret.
**Model answer:** With df = 2 (3×2 or 2×3 table), χ² = 12.3 exceeds critical value (χ²_{0.05, 2} = 5.99). p = 0.002 < 0.05. Reject H₀. The two variables are statistically significantly associated. Report effect size (e.g., Cramér's V) to quantify strength.

### Q32. How do you interpret "Continuity Correction" in SPSS chi-squared output?
**Model answer:** SPSS applies Yates' continuity correction automatically for 2×2 tables. The corrected chi-squared is typically slightly smaller. Use the continuity-corrected value for small samples. For larger samples (n > 30), the correction has minimal effect.

### Q33. SPSS output shows expected count < 5 in 25% of cells. What should you do?
**Model answer:** Chi-squared assumption violated. Options: (1) Fisher's exact test — SPSS reports it in 2×2 tables. (2) Combine adjacent categories if meaningful. (3) Collect more data. (4) Report results with explicit caveat. Never ignore small expected counts — inflated Type I error rate.

### Q34. In SPSS, a phi coefficient is 0.42. Interpret.
**Model answer:** Moderate association between the two binary variables. φ = 0.42 corresponds to a medium effect size. Positive sign indicates movement in the same direction. For a 2×2 table, φ = r (Pearson correlation for binary data).

### Q35. One-sample t-test: t(29) = 2.45, p = 0.021. Interpret.
**Model answer:** Sample mean is significantly different from the hypothesised value (typically zero or a benchmark) at α = 0.05. df = 29 (n = 30). Report with direction (positive t = sample mean > hypothesised). Examine 95% CI for effect size. Practical significance may still need separate evaluation.

### Q36. Independent-samples t: t = 2.1, df = 48, p = 0.041. Equal variances assumed. Interpret.
**Model answer:** The mean of group 1 is significantly higher (positive t) than group 2 at α = 0.05. Degrees of freedom 48 = n₁ + n₂ − 2, consistent with pooled-variance t. p = 0.041 < 0.05 → reject H₀: μ₁ = μ₂. Verify the equal-variance assumption with Levene's test before using pooled variance.

### Q37. Levene's test has p = 0.02 in your SPSS output. Implication?
**Model answer:** Levene's tests H₀: equal variances. p = 0.02 < 0.05 → reject — variances are unequal. Use the "Equal variances not assumed" row (Welch's t-test) for the hypothesis test. Pooled t-test with unequal variances inflates Type I error.

### Q38. Paired t-test: t = 4.2, df = 19, p < 0.001, mean diff = 8.5. Interpret.
**Model answer:** There is a highly statistically significant difference between paired measurements (p < 0.001). The mean difference of 8.5 units indicates the direction: condition 1 > condition 2 by 8.5 on average. n = 20 pairs. 95% CI excludes 0. Effect is both statistically and (depending on context) practically significant.

### Q39. SPSS confidence interval for mean difference = [2.1, 9.4]. Interpret.
**Model answer:** We are 95% confident that the true population mean difference lies between 2.1 and 9.4. Since 0 is not in the interval, the difference is statistically significant at α = 0.05 (two-sided). The CI also gives effect size: the difference is meaningful in applied terms, potentially between small and large depending on context.

### Q40. Chi-squared test output shows "Linear-by-Linear Association, p = 0.01". What's this?
**Model answer:** Tests for a linear trend when both variables are ordinal. Treats categories as scores and tests H₀: no linear trend in conditional means. More powerful than ordinary chi-squared when ordinal structure matters. Use when your variables have meaningful ordering (e.g., age groups, satisfaction levels).

---

## Part E: Practical Applications (Q41-45)

### Q41. A marketing survey cross-tabulates age group (3 levels) with preferred product (4 levels). n = 200. Chi-squared = 18.5. How to interpret?
**Model answer:** df = (3−1)(4−1) = 6. Critical value χ²_{0.05, 6} = 12.59. Since 18.5 > 12.59, reject H₀ — age and product preference are statistically significantly associated. Report p-value, Cramér's V for effect size, and examine cell residuals to identify which age-product combinations drive the association. Business implication: target marketing by age segments.

### Q42. In a 2×2 table testing whether a drug reduces recurrence, Fisher's exact gives p = 0.03. Interpret.
**Model answer:** Based on exact probabilities (appropriate for small samples), p = 0.03 < 0.05 → reject H₀ of no association. Drug treatment is associated with different recurrence rates. Direction must be checked: is the treatment group's rate lower? Report OR or RR to quantify magnitude. Clinical significance depends on absolute risk difference, not just p-value.

### Q43. A survey tests whether satisfaction (5-point Likert) differs between two stores. What test?
**Model answer:** Satisfaction is ordinal. Choices: (1) Mann-Whitney U test — non-parametric, based on ranks. (2) Chi-squared on the cross-tab (though some information is lost by treating ordinal as nominal). (3) Treat Likert as interval and use independent-samples t-test — acceptable if distribution is symmetric. Mann-Whitney is generally safest.

### Q44. Hypothesising that customer satisfaction has improved compared to last year's mean of 7.2. Sample: n = 100, X̄ = 7.5, s = 1.2.
**Model answer:** One-sample t-test. H₀: μ = 7.2 vs H₁: μ > 7.2 (one-sided). t = (7.5 − 7.2)/(1.2/10) = 0.3/0.12 = 2.5. df = 99. One-sided critical value t_{0.05, 99} ≈ 1.66. Since 2.5 > 1.66, reject H₀. Statistically significant improvement. Report 95% CI and consider whether 0.3 is a practically meaningful improvement.

### Q45. How do you report a hypothesis test result in an academic paper?
**Model answer:** Include: (1) Sample size and groups. (2) Descriptive statistics (M, SD). (3) Test name and statistic with df: t(48) = 2.1. (4) Exact p-value (p = 0.041). (5) Effect size (Cohen's d, Cramér's V). (6) Confidence interval for the parameter. (7) One-sentence interpretation tied to the research question. Example: "Group A (M = 50, SD = 5) scored significantly higher than Group B (M = 45, SD = 6), t(48) = 3.1, p = 0.003, d = 0.91, 95% CI [1.8, 8.2]."

---

## Part F: True/False and Application (Q46-50)

### Q46. T/F: A non-significant chi-squared means the variables are independent.
**Model answer:** FALSE. Failing to reject H₀ is not the same as confirming independence. Could be due to small sample size (low power) or weak association. Report effect size (V, φ) to assess practical independence, and discuss whether n was sufficient to detect meaningful associations.

### Q47. T/F: If p = 0.049, the effect is substantially more real than if p = 0.051.
**Model answer:** FALSE. The difference between these p-values is essentially none — both represent roughly the same strength of evidence. Arbitrary cutoffs (α = 0.05) create artificial sharp distinctions. Modern practice: report exact p-values, effect sizes, and CIs; don't dichotomise at α.

### Q48. T/F: Larger sample sizes always give more reliable p-values.
**Model answer:** TRUE in terms of power to detect real effects, but beware: with very large n, trivial differences become "statistically significant". Always pair p-values with effect sizes to distinguish statistical from practical significance. Large samples reveal genuine effects; they also magnify noise to appear significant.

### Q49. A health survey wants to test if smoking rates differ between two regions (n₁ = 500, n₂ = 450, p̂₁ = 0.25, p̂₂ = 0.20). Conduct the test.
**Model answer:** Pooled p̂ = (125 + 90)/950 = 0.226. SE = √(0.226 · 0.774 · (1/500 + 1/450)) = √(0.175 · 0.00422) = √0.000738 = 0.0272. z = (0.25 − 0.20)/0.0272 = 1.84. Two-sided p = 0.066. Marginally significant (p > 0.05) → fail to reject H₀. 95% CI for difference: 0.05 ± 1.96(0.0280) = [−0.005, 0.105] — just includes 0. Evidence is suggestive but not conclusive; larger study may be warranted.

### Q50. A researcher's cross-tab reveals that customers who received a promotion bought the product 40% of the time, vs 25% for controls (n = 300 each). Test and recommend.
**Model answer:** χ² test of independence: pooled p̂ = (120+75)/600 = 0.325. E cells = 300·0.325 = 97.5 per cell (promo sale), 300·0.675 = 202.5 (promo no sale), same for control. χ² = Σ(O−E)²/E = (120−97.5)²/97.5 + (75−97.5)²/97.5 + (180−202.5)²/202.5 + (225−202.5)²/202.5 = 5.19 + 5.19 + 2.50 + 2.50 = 15.38. df = 1. Critical χ²_{0.05, 1} = 3.84. Reject H₀ — promotion is associated with purchases. OR = (120·225)/(75·180) = 27,000/13,500 = 2.0. The promoted group has twice the odds of buying. Recommendation: deploy promotion broadly, subject to cost analysis; investigate whether the effect is sustainable or only a short-term lift.

---

**Exam tip:** In SPSS-based hypothesis testing questions, always: (1) state null and alternative hypotheses, (2) check assumptions (Levene's for variance, normality, expected frequencies), (3) quote the exact SPSS output (test statistic, df, p-value), (4) state reject/fail to reject, (5) interpret in the business/research context with units, (6) report effect size and CI.
