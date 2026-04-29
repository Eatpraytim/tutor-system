# ST3188 — ANOVA & ANCOVA: 50 Exam Questions with Model Answers

---

## Part A: One-Way ANOVA (Q1-15)

### Q1. What does ANOVA stand for and what does it test?
**Model answer:** Analysis of Variance. Tests whether the means of three or more groups are significantly different. H₀: μ₁ = μ₂ = ... = μ_k. H₁: at least one mean differs. It works by partitioning total variance into between-group and within-group components.

### Q2. Why not use multiple t-tests instead of ANOVA?
**Model answer:** Multiple pairwise t-tests inflate the Type I error rate. With k groups, there are k(k−1)/2 comparisons; at α = 0.05 per test, overall error approaches 1 − (0.95)^{number of tests}. ANOVA provides a single omnibus test controlling error at α. Follow up with post-hoc tests (Tukey, Bonferroni) only if ANOVA is significant.

### Q3. State the assumptions of one-way ANOVA.
**Model answer:** (1) Random sampling / independent observations. (2) Normality — residuals (or group samples) approximately normal. (3) Homogeneity of variance — equal variances across groups. (4) Continuous dependent variable. Test with Levene's (variance) and Shapiro-Wilk (normality).

### Q4. State the ANOVA partition of variance.
**Model answer:** SST = SSB + SSW. Total Sum of Squares = Between-Group + Within-Group. SSB captures variation between group means; SSW captures variation within each group (error). df: SST = N−1; SSB = k−1; SSW = N−k.

### Q5. State the F-ratio formula.
**Model answer:** F = MSB/MSW = [SSB/(k−1)] / [SSW/(N−k)]. Under H₀ and assumptions, F ~ F(k−1, N−k). Reject H₀ if F > F_{α, k−1, N−k}. Large F means between-group variance >> within-group variance, suggesting group differences.

### Q6. Interpret the F-statistic as a signal-to-noise ratio.
**Model answer:** Numerator (MSB): variability between group means — the "signal" if groups differ. Denominator (MSW): variability within groups — the "noise" or residual. Large F = signal dominates noise → groups really differ. Small F = noise dominates → no evidence of group differences.

### Q7. Interpret η² (eta-squared) in ANOVA.
**Model answer:** η² = SSB/SST = proportion of total variance explained by group membership. Analogous to R² in regression. Range [0, 1]. Conventional benchmarks: 0.01 small, 0.06 medium, 0.14 large. Always report alongside F and p-value.

### Q8. State Levene's test and its purpose.
**Model answer:** Tests homogeneity of variance: H₀: σ²₁ = σ²₂ = ... = σ²_k. Uses absolute deviations from group medians. Robust to non-normality. If significant (p < 0.05), variance assumption is violated — use Welch's ANOVA or transform data.

### Q9. When should you use Welch's ANOVA?
**Model answer:** When the equal-variance assumption is violated (Levene's test significant). Welch's adjusts degrees of freedom to account for unequal variances, analogous to Welch's t-test. SPSS labels this "Robust Tests of Equality of Means". Better default than standard ANOVA when variances are in doubt.

### Q10. What happens if ANOVA assumptions are violated?
**Model answer:** Normality: ANOVA is relatively robust for large samples (CLT). Equal variance: violations invalidate F-test; use Welch's. Independence: critical — violations (e.g., in cluster-randomised designs) require mixed-effects models. Non-robust violations inflate Type I error; transform data, use non-parametric alternatives (Kruskal-Wallis), or switch test.

### Q11. Describe Tukey's HSD test.
**Model answer:** Post-hoc test comparing all pairwise group means while controlling family-wise error at α. Uses a studentised range distribution. Reports p-values and CIs for each pair. Preferred when all pairwise comparisons are of interest and sample sizes are roughly equal.

### Q12. Describe the Bonferroni correction.
**Model answer:** Adjusts individual test α: α_corrected = α/m, where m is the number of comparisons. Ensures family-wise α ≤ original level. Simple and conservative — gets conservative with many comparisons. Alternative: Holm-Bonferroni is less conservative while preserving FWER control.

### Q13. When would you use planned contrasts vs post-hoc tests?
**Model answer:** Planned contrasts: hypotheses specified a priori (before data); tests only specific comparisons; more powerful. Post-hoc: exploratory, all pairs examined after seeing data; requires correction for multiple comparisons. Planned contrasts appropriate when theory dictates specific groups to compare.

### Q14. What is the Kruskal-Wallis test?
**Model answer:** Non-parametric alternative to one-way ANOVA. Tests H₀: groups have same distribution (location). Based on ranks rather than raw values. Use when: normality violated, small samples, ordinal data. Less powerful than ANOVA when assumptions hold; more robust otherwise.

### Q15. When reporting ANOVA, what should you include?
**Model answer:** F-statistic with df: F(k−1, N−k) = value. Exact p-value. Effect size η² or ω². Group means and standard deviations (descriptive). Post-hoc comparisons if significant. Homogeneity of variance test result. Sample sizes per group. Example: "F(2, 57) = 4.82, p = 0.012, η² = 0.14".

---

## Part B: Two-Way ANOVA (Q16-25)

### Q16. What does two-way ANOVA test?
**Model answer:** Tests the effects of two categorical factors (main effects) AND their interaction on a continuous dependent variable. Three F-tests: (1) Main effect of factor A, (2) Main effect of factor B, (3) A×B interaction.

### Q17. Define a main effect.
**Model answer:** The overall effect of one factor averaged across levels of the other factor. E.g., the main effect of gender on salary = difference between males and females averaged over all job types. Tests whether that factor matters ignoring interactions.

### Q18. Define an interaction effect.
**Model answer:** When the effect of one factor depends on the level of another factor. E.g., gender × job type interaction: gender gap differs across job types. Visually: non-parallel lines in an interaction plot. Always interpret main effects in light of interactions — significant interactions make main effect interpretation nuanced.

### Q19. State the two-way ANOVA partition.
**Model answer:** SST = SSA + SSB + SSA×B + SSE. Total variance = factor A effect + factor B effect + interaction + residual. Each has df: SSA (a−1), SSB (b−1), SSA×B ((a−1)(b−1)), SSE (N−ab).

### Q20. If the interaction is significant, how do you interpret main effects?
**Model answer:** Main effects become less meaningful when interactions are significant. Focus on simple main effects (effect of one factor at each level of the other). Use interaction plots. Avoid interpreting main effects in isolation — they can mislead if the effect flips direction across levels.

### Q21. What is a balanced vs unbalanced design?
**Model answer:** Balanced: equal sample sizes in each cell. Unbalanced: unequal. Two-way ANOVA is sensitive to imbalance in unbalanced designs — Type I, Type II, Type III sums of squares give different results. SPSS default is Type III, generally preferred for unbalanced data.

### Q22. Describe an interaction plot.
**Model answer:** Plots the cell means with one factor on x-axis, another shown as different lines (or colours). Parallel lines = no interaction. Non-parallel lines = interaction present. Crossed lines = strong interaction with reversed simple effects. Useful visualisation alongside F-tests.

### Q23. What is a simple main effect?
**Model answer:** The effect of one factor within a specific level of another factor. E.g., effect of training method within the "experienced" group. Tested with planned comparisons. Used to decompose significant interactions — where does the interaction manifest?

### Q24. Compare factorial ANOVA with separate one-way ANOVAs.
**Model answer:** Factorial (two-way): simultaneously examines multiple factors and their interaction. More powerful, more efficient use of data, identifies interactions. Separate one-way: misses interactions, less powerful, inflates Type I error across multiple tests. Always use factorial when multiple factors are of interest.

### Q25. Interpret a two-way ANOVA with significant A, non-significant B, significant A×B.
**Model answer:** Factor A has an overall effect; factor B does not on average. However, the interaction is significant — the effect of A depends on the level of B (or vice versa). Must examine simple main effects to understand the pattern. A plot of means will reveal how A's effect varies across B's levels.

---

## Part C: ANCOVA (Q26-35)

### Q26. What does ANCOVA stand for and when to use it?
**Model answer:** Analysis of Covariance. Extends ANOVA by including a continuous covariate (predictor) alongside categorical factors. Used to: (1) statistically control for variables that can't be manipulated, (2) increase power by reducing error variance, (3) examine factor effects after adjusting for the covariate.

### Q27. State the ANCOVA model.
**Model answer:** Y_{ij} = μ + τ_i + β(X_{ij} − X̄) + ε_{ij}, where τ_i is the effect of group i, β is the slope of the covariate X, and X̄ is the grand mean of X. Combines regression (on X) with ANOVA (on groups).

### Q28. State the ANCOVA assumptions.
**Model answer:** (1) Standard ANOVA assumptions (normality, equal variance, independence). (2) Linear relationship between covariate and DV. (3) Homogeneity of regression slopes — the covariate's slope is the same across groups. (4) Covariate measured without error. (5) Covariate independent of the treatment (i.e., measured BEFORE treatment).

### Q29. Explain "homogeneity of regression slopes".
**Model answer:** The slope of the covariate X on Y is assumed the same across groups. If violated (different slopes in different groups), ANCOVA inference is invalid. Test by including the group × covariate interaction in the model; if significant, homogeneity is violated.

### Q30. What happens if homogeneity of regression slopes is violated?
**Model answer:** Interpret main group effects becomes misleading — the treatment effect varies with X. Use: (1) Johnson-Neyman technique to find regions of X where groups differ; (2) Simple main effects at specific X values; (3) Mixed-effects or separate regression models per group. ANCOVA's key advantage (cleaner group comparisons) is lost.

### Q31. How does ANCOVA increase statistical power compared to ANOVA?
**Model answer:** By including a covariate X that predicts Y, we reduce residual variance (the "noise" in SSE). Smaller SSE → larger F for group effects → more power. Works best when the covariate is strongly correlated with Y. A weak covariate adds little benefit and costs df.

### Q32. Contrast ANCOVA with blocking.
**Model answer:** Both control for a source of variation. Blocking: the control variable is treated as a discrete factor (e.g., blocks of similar observations). ANCOVA: treats it as continuous covariate via regression adjustment. ANCOVA more efficient when the covariate is continuous and linearly related to Y. Blocking simpler but coarser.

### Q33. Explain adjusted means in ANCOVA.
**Model answer:** Group means adjusted for the covariate — what the group means would be if all groups had the same covariate value (typically the grand mean). Reports what the group differences are attributable to the grouping variable, controlling for the covariate. Reported in SPSS as "estimated marginal means".

### Q34. When would you NOT use ANCOVA?
**Model answer:** (1) When the covariate is affected by the treatment (post-treatment measure — controlling would remove part of the effect). (2) When covariate and grouping are highly correlated (confounded). (3) When the covariate-outcome relationship is non-linear (transform or use non-linear methods). (4) When the covariate is measured with substantial error.

### Q35. Interpret ANCOVA output: group effect F = 6.3 (p = 0.002), covariate F = 45.8 (p < 0.001).
**Model answer:** Both the grouping factor and the covariate significantly affect Y. The covariate has a stronger effect (higher F) — it's a useful adjustment variable. Group differences remain significant after controlling for the covariate, strengthening the claim that grouping matters beyond any baseline differences captured by the covariate. Report adjusted means and effect sizes.

---

## Part D: Numerical Problems (Q36-43)

### Q36. Given SSB = 120, SSW = 300, k = 3 groups, N = 30. Compute F.
**Model answer:** df_between = k−1 = 2. df_within = N−k = 27. MSB = 120/2 = 60. MSW = 300/27 = 11.11. F = 60/11.11 = 5.4. Critical F_{0.05, 2, 27} ≈ 3.35. Since 5.4 > 3.35, reject H₀ — groups differ significantly.

### Q37. Compute η² given SSB = 120, SSW = 300.
**Model answer:** SST = SSB + SSW = 120 + 300 = 420. η² = 120/420 = 0.286. About 28.6% of variance is explained by group membership — large effect size.

### Q38. For k = 4 groups, n = 10 per group, compute df for F-test.
**Model answer:** df between = k−1 = 3. df within = N−k = 40−4 = 36. F(3, 36) with critical value F_{0.05, 3, 36} ≈ 2.87.

### Q39. Three groups: X̄₁ = 50, X̄₂ = 55, X̄₃ = 60, n = 20 per group, MSW = 100. Compute F.
**Model answer:** Grand mean = (50+55+60)/3 = 55. SSB = 20·[(50−55)² + (55−55)² + (60−55)²] = 20·[25 + 0 + 25] = 1000. df_between = 2. MSB = 500. F = MSB/MSW = 500/100 = 5.0. df = (2, 57). Critical F_{0.05, 2, 57} ≈ 3.16. Reject H₀.

### Q40. Tukey's HSD: n = 10 per group, MSW = 25. Compute HSD at α = 0.05 for 3 groups.
**Model answer:** HSD = q_{0.05, k, df} · √(MSW/n) where q is the studentised range critical value. For k = 3 groups, df_within = 27: q ≈ 3.51. HSD = 3.51 · √(25/10) = 3.51 · 1.58 = 5.55. Any pair of group means differing by more than 5.55 is significantly different.

### Q41. Bonferroni-adjusted α for 6 pairwise comparisons at family-wise α = 0.05.
**Model answer:** α_adjusted = 0.05/6 = 0.0083. Each individual comparison is tested at 0.0083 significance to maintain overall family-wise rate at 0.05. Equivalently, multiply each raw p-value by 6 and compare to 0.05.

### Q42. In ANCOVA, covariate slope β = 0.6 (Y on X). Group A mean Y = 50, X̄_A = 8; Group B mean Y = 55, X̄_B = 6; grand X̄ = 7. Compute adjusted means.
**Model answer:** Adjusted Y_A = 50 − 0.6(8 − 7) = 50 − 0.6 = 49.4. Adjusted Y_B = 55 − 0.6(6 − 7) = 55 + 0.6 = 55.6. Adjusted difference = 55.6 − 49.4 = 6.2. Un-adjusted difference = 55 − 50 = 5.0. After controlling for covariate, group B's advantage is larger than raw data suggests.

### Q43. Kruskal-Wallis statistic H = 10.5, k = 4 groups. Interpret.
**Model answer:** df = k−1 = 3. Critical χ²_{0.05, 3} = 7.815. Since 10.5 > 7.815, reject H₀. At least one group differs in distribution. Use pairwise Mann-Whitney with Bonferroni correction for post-hoc comparisons. Kruskal-Wallis doesn't specify which groups differ.

---

## Part E: True/False and Interpretation (Q44-48)

### Q44. T/F: ANOVA only tests whether groups are different; it doesn't say which.
**Model answer:** TRUE. ANOVA's omnibus F-test tells you that at least one group differs, but not which. Follow up with post-hoc tests (Tukey, Bonferroni) or planned contrasts to identify specific group differences. Reporting just F is incomplete.

### Q45. T/F: ANOVA requires normality of the dependent variable.
**Model answer:** FALSE (technically). ANOVA assumes approximately normal residuals, not normal raw data. For large samples, ANOVA is robust due to the CLT. For small samples, transform data or use Kruskal-Wallis if normality is severely violated.

### Q46. T/F: A non-significant ANOVA means all group means are equal.
**Model answer:** FALSE. Non-significance means insufficient evidence to reject equality — could be due to small sample or small effect size. Cannot conclude means are identical. Report effect size (η²); small η² with large n is stronger evidence of true equivalence than small n.

### Q47. T/F: Significant interaction makes main effects uninterpretable.
**Model answer:** PARTIALLY TRUE. Significant interactions complicate main effect interpretation because the effect of one factor depends on another. Main effects can still be reported but must be qualified: "On average, X matters, but how much depends on Y (interaction)." Focus interpretation on simple main effects.

### Q48. T/F: ANCOVA removes the effect of a confounder.
**Model answer:** FALSE (overly strong). ANCOVA adjusts group means statistically for the covariate, which is not the same as removing a confounder. Random assignment is the gold standard for removing confounding. If the covariate is truly causally upstream and well-measured, ANCOVA provides reasonable adjustment; otherwise, residual confounding persists.

---

## Part F: Application (Q49-50)

### Q49. Three teaching methods (A, B, C) are compared on test scores. n = 25 per group. Mean scores: 75, 80, 85 with SDs 10, 12, 11. Conduct the analysis.
**Model answer:** (1) Check assumptions: Levene's test for equal variances; approximate normality (n = 25 per group, CLT applies). (2) Compute: Grand mean = 80. SSB = 25·[(75−80)² + (80−80)² + (85−80)²] = 25·50 = 1250. SSW = (25−1)(10² + 12² + 11²) = 24·365 = 8760. MSB = 625. MSW = 121.67. F = 625/121.67 = 5.14. df = (2, 72). p < 0.01. Reject H₀. (3) η² = 1250/10010 = 0.125 — medium effect. (4) Post-hoc Tukey to compare A-B, A-C, B-C. Report: "Teaching method significantly affects scores, F(2, 72) = 5.14, p < 0.01, η² = 0.13. Method C produced highest scores; specific pairwise differences via Tukey."

### Q50. A researcher compares depression scores across 4 treatment groups, controlling for pre-treatment depression as a covariate. ANCOVA shows F_group = 8.2 (p < 0.001), F_covariate = 120 (p < 0.001), no interaction. Interpret.
**Model answer:** (1) The covariate (pre-treatment depression) strongly predicts post-treatment depression — baseline matters. (2) After controlling for baseline, treatment groups differ significantly. (3) Homogeneity of regression slopes held (no interaction with treatment × covariate) — ANCOVA is valid. (4) Report adjusted group means and pairwise comparisons to identify which treatment(s) are most effective. (5) Effect size: partial η² for group effect quantifies treatment importance. (6) Caveat: observational vs randomised differs — ANCOVA does not create a randomised comparison from a confounded one; if pre-treatment scores differ systematically across groups due to selection, residual confounding may persist.

---

**Exam tip:** For ANOVA questions, always: (1) verify assumptions (Levene's, normality), (2) report F, df, p, η² together, (3) if significant, follow up with post-hoc tests (Tukey for all pairs, Bonferroni for planned subset), (4) interpret in research context, (5) discuss effect size alongside statistical significance.
