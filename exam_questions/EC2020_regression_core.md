# EC2020 — Regression Core (SLR & MLR): 50 Exam Questions with Model Answers

---

## Part A: Simple Linear Regression (Q1-10)

### Q1. State the SLR population model.
**Model answer:** Y = β₀ + β₁X + u, where Y is the response, X the regressor, β₀ the population intercept, β₁ the population slope, and u the unobserved error term. Conditional expectation: E(Y|X) = β₀ + β₁X.

### Q2. State the zero conditional mean assumption and its importance.
**Model answer:** E(u|X) = 0. Implies u is uncorrelated with X and E(u) = 0. Crucial because it means OLS is unbiased. If violated (e.g., omitted variable bias), β̂ is biased and inconsistent. Often stated as "exogeneity".

### Q3. Derive the OLS slope estimator.
**Model answer:** Minimise Σ(yᵢ − β̂₀ − β̂₁xᵢ)². Take partial derivatives, set to zero. Solving gives: β̂₁ = Σ(xᵢ − x̄)(yᵢ − ȳ) / Σ(xᵢ − x̄)² = Cov(x,y)/Var(x). β̂₀ = ȳ − β̂₁x̄.

### Q4. Prove E(β̂₁) = β₁ under SLR assumptions.
**Model answer:** β̂₁ = Σ(xᵢ−x̄)(yᵢ−ȳ)/Σ(xᵢ−x̄)² = β₁ + Σ(xᵢ−x̄)uᵢ/Σ(xᵢ−x̄)². Conditional on X: E(β̂₁|X) = β₁ + Σ(xᵢ−x̄)E(uᵢ|X)/Σ(xᵢ−x̄)² = β₁ (by zero conditional mean). So β̂₁ is unbiased.

### Q5. State the variance of the OLS slope under homoscedasticity.
**Model answer:** Var(β̂₁|X) = σ² / Σ(xᵢ − x̄)², where σ² = Var(u|X). Decreases with more variation in X (larger Σ(xᵢ−x̄)²) or smaller error variance.

### Q6. Interpret R² in SLR.
**Model answer:** R² = SSE/SST = proportion of variance in Y explained by X linearly. Range [0, 1]. Equals squared Pearson correlation (R² = r²). Does not measure causation, predictive accuracy, or magnitude of effect.

### Q7. State the relationship between t and F tests in SLR.
**Model answer:** In simple regression, F = t² where F is the overall F-statistic testing H₀: β₁ = 0 and t is the slope t-statistic. df_F = (1, n−2) and df_t = n−2. Give identical p-values for the two-sided test.

### Q8. Show that the OLS residuals sum to zero.
**Model answer:** First-order condition for β̂₀: Σ(yᵢ − β̂₀ − β̂₁xᵢ) = 0 → Σûᵢ = 0. This is a property of OLS with an intercept — not an assumption. Similarly, Σxᵢûᵢ = 0 (residuals orthogonal to X).

### Q9. Describe the Gauss-Markov theorem for SLR.
**Model answer:** Under the Gauss-Markov assumptions (linearity, random sampling, zero conditional mean, homoscedasticity, no perfect collinearity in MLR), the OLS estimators are BLUE — Best Linear Unbiased Estimators. "Best" = minimum variance.

### Q10. State the five key SLR assumptions (Wooldridge notation).
**Model answer:** (SLR.1) Linear in parameters. (SLR.2) Random sampling. (SLR.3) Variation in X (Σ(xᵢ−x̄)² > 0). (SLR.4) Zero conditional mean: E(u|X) = 0. (SLR.5) Homoscedasticity: Var(u|X) = σ². Plus SLR.6 normality for exact small-sample inference.

---

## Part B: Multiple Linear Regression (Q11-20)

### Q11. State the MLR model in matrix form.
**Model answer:** y = Xβ + u, where y is n×1, X is n×(k+1) design matrix (column of 1s plus k regressors), β is (k+1)×1 coefficient vector, u is n×1 error vector. Assumption: E(u|X) = 0, Var(u|X) = σ²I (homoscedasticity).

### Q12. Derive the OLS estimator in matrix form.
**Model answer:** Minimise u'u = (y−Xβ)'(y−Xβ). Expand: y'y − 2β'X'y + β'X'Xβ. Derivative with respect to β: −2X'y + 2X'Xβ = 0. Solve: β̂ = (X'X)⁻¹X'y. Requires (X'X) invertible (no perfect multicollinearity).

### Q13. Show β̂ is unbiased.
**Model answer:** β̂ = (X'X)⁻¹X'y = (X'X)⁻¹X'(Xβ + u) = β + (X'X)⁻¹X'u. Given X: E(β̂|X) = β + (X'X)⁻¹X'E(u|X) = β (by MLR.4: E(u|X) = 0). Unconditional: E(β̂) = β.

### Q14. State Var(β̂) under homoscedasticity.
**Model answer:** Var(β̂|X) = σ²(X'X)⁻¹, where σ² = Var(u|X). Diagonal elements give Var(β̂_j); square root = SE(β̂_j). Off-diagonal elements: Cov(β̂_j, β̂_k). Used for t-tests and CIs.

### Q15. State the Gauss-Markov assumptions for MLR.
**Model answer:** (MLR.1) Linear in parameters. (MLR.2) Random sampling. (MLR.3) No perfect multicollinearity — columns of X are linearly independent. (MLR.4) Zero conditional mean: E(u|X) = 0. (MLR.5) Homoscedasticity: Var(u|X) = σ². With normality (MLR.6), exact inference follows.

### Q16. Interpret a multiple regression coefficient.
**Model answer:** β_j = expected change in Y for a one-unit increase in X_j, holding all other regressors constant. "Partial effect", "ceteris paribus", or "controlling for others" are equivalent expressions. Central to causal interpretation in MLR.

### Q17. Define perfect multicollinearity.
**Model answer:** One regressor is an exact linear combination of others. Causes (X'X) singular — cannot compute β̂. Example: including both dummies for "male" and "female" with intercept (dummy variable trap). Solution: drop one redundant variable.

### Q18. Describe imperfect multicollinearity.
**Model answer:** High but not perfect correlation among regressors. Inflates Var(β̂_j) = σ²/(SST_j · (1−R²_j)), where R²_j is from regressing X_j on others. VIF = 1/(1−R²_j). High multicollinearity → imprecise estimates but not biased.

### Q19. Describe the Frisch-Waugh-Lovell theorem.
**Model answer:** In MLR, β̂_j equals the coefficient from regressing residuals of Y (after regressing on all other X's) on residuals of X_j (same). I.e., partial effect of X_j captured by residuals after removing linear effects of other regressors. Explains "holding others constant" precisely.

### Q20. Interpret adjusted R².
**Model answer:** R̄² = 1 − (1−R²)(n−1)/(n−k−1). Adjusts R² for degrees of freedom. Can decrease when adding predictors. Used to compare models with different numbers of regressors. Can be negative for very poor fits.

---

## Part C: Hypothesis Testing and Inference (Q21-30)

### Q21. State the t-statistic for testing β_j = 0.
**Model answer:** t = β̂_j / SE(β̂_j), with df = n − k − 1 under H₀. Under normality (MLR.6), t ~ t(n−k−1). For large n, t approximates N(0,1). Reject H₀ if |t| > t_{α/2, n−k−1}.

### Q22. State the F-test for overall model significance.
**Model answer:** F = (R²/k) / ((1−R²)/(n−k−1)) = [(SSR/k) / (SSE/(n−k−1))]. df = (k, n−k−1). Tests H₀: β₁ = β₂ = ... = β_k = 0. Reject if F > F_{α, k, n−k−1}. Large F → model explains significant variation.

### Q23. State the F-test for a subset of coefficients.
**Model answer:** F = [(SSR_R − SSR_U)/q] / [SSE_U/(n−k−1)], where R = restricted (fewer regressors), U = unrestricted, q = number of restrictions, k = unrestricted predictors. df = (q, n−k−1). Tests H₀ that q coefficients are jointly zero.

### Q24. Interpret a 95% CI for β_j.
**Model answer:** CI: β̂_j ± t_{α/2, n−k−1} · SE(β̂_j). We are 95% confident the true β_j lies in this interval. If 0 is not in the interval, reject H₀: β_j = 0 at 5%. CI width decreases with n, σ known precisely, and less multicollinearity.

### Q25. Distinguish statistical and economic significance.
**Model answer:** Statistical significance: p-value small; effect distinguishable from zero. Economic significance: magnitude is meaningful in context. With large n, tiny effects become statistically significant. Always report magnitude alongside p-value; interpret economic importance with respect to relevant scales and baseline values.

### Q26. When does the classical t-test become reliable with large samples?
**Model answer:** Even if u is not normal, by the CLT, β̂ is asymptotically normal with mean β and variance consistently estimated by the sandwich or conventional formula. For n > 30, t-approximation is typically reliable. Exact distribution requires normality (MLR.6).

### Q27. Describe the Wald test.
**Model answer:** Tests joint hypotheses: H₀: Rβ = r, where R is q×(k+1). W = (Rβ̂ − r)' [R(X'X)⁻¹R']⁻¹ (Rβ̂ − r) / σ̂². Under H₀, W ~ χ²(q) asymptotically (or W/q ~ F). Generalises t and F tests. Reject for large W.

### Q28. Describe a log-level functional form.
**Model answer:** log(Y) = β₀ + β₁X + u. Interpretation: a one-unit increase in X is associated with a β₁ × 100% change in Y (approximately). Exact: (e^β₁ − 1) × 100%. Used when Y varies multiplicatively or is positively skewed.

### Q29. Describe a log-log functional form.
**Model answer:** log(Y) = β₀ + β₁ log(X) + u. β₁ is the elasticity of Y with respect to X: a 1% increase in X is associated with a β₁% change in Y. Constant elasticity over the observed range. Used in economics (demand, production functions).

### Q30. Interpret a level-log form.
**Model answer:** Y = β₀ + β₁ log(X) + u. A 1% increase in X is associated with a (β₁/100) unit change in Y. Semi-elasticity: Y is in absolute units, X in percent changes. Example: wage = β₀ + β₁log(exp) — returns to experience diminish.

---

## Part D: Omitted Variable Bias and Endogeneity (Q31-40)

### Q31. Define omitted variable bias.
**Model answer:** Occurs when a relevant variable is omitted from the regression, and the omitted variable is correlated with an included regressor. Bias in β̂_j: bias = β_omit · δ, where δ is the partial effect of the omitted variable on X_j. β̂_j is biased and inconsistent.

### Q32. State the omitted variable bias formula.
**Model answer:** If true model: Y = β₀ + β₁X₁ + β₂X₂ + u, but we estimate Y = β₀ + β̃₁X₁ + ũ (omitting X₂), then E(β̃₁) = β₁ + β₂·δ where δ is the slope of the auxiliary regression X₂ = δ₀ + δX₁ + v. Bias direction: sign(β₂) × sign(δ).

### Q33. Describe the direction of OVB for two positive correlations.
**Model answer:** If β₂ > 0 (X₂ positively affects Y) and Corr(X₁, X₂) > 0, then bias > 0 — β̃₁ overestimates β₁. Intuition: X₁ partly picks up X₂'s effect through their correlation. Symmetric for other sign combinations. Essential diagnostic for causal regression.

### Q34. What is endogeneity?
**Model answer:** When a regressor is correlated with the error term (Cov(X, u) ≠ 0). Violates MLR.4. Consequences: OLS biased and inconsistent. Sources: (1) omitted variables, (2) measurement error in X, (3) simultaneity (reverse causation or joint determination). Remedy: instrumental variables.

### Q35. What is measurement error in the regressor?
**Model answer:** Observed X* = X + e, where e is measurement error, independent of true X and u. OLS using X* gives attenuated estimate: plim(β̂) = β · Var(X)/(Var(X) + Var(e)) < β. Bias toward zero — "attenuation bias". Remedy: instrumental variables or reduce measurement error.

### Q36. What is simultaneity bias?
**Model answer:** Y and X determined simultaneously (e.g., supply and demand). X is endogenous — responds to Y. OLS biased. Example: price and quantity — OLS gives neither supply nor demand curve but a mixture. Remedy: simultaneous equations models or instrumental variables.

### Q37. State conditions for a valid instrumental variable.
**Model answer:** Z is a valid IV for X if: (1) Relevance: Cov(Z, X) ≠ 0 — Z correlates with X. (2) Exogeneity (exclusion restriction): Cov(Z, u) = 0 — Z does not directly affect Y (only through X). Both must hold; typically (1) testable, (2) untestable (must argue theoretically).

### Q38. Describe Two-Stage Least Squares (2SLS).
**Model answer:** (1) First stage: regress X on Z (and any exogenous regressors). Obtain fitted X̂. (2) Second stage: regress Y on X̂ (and exogenous regressors). 2SLS estimator is consistent if Z is valid IV. SE must account for first-stage estimation — use software's 2SLS routines, not two separate OLS steps.

### Q39. What are weak instruments?
**Model answer:** Instruments Z that are only weakly correlated with X (Cov(Z,X) small). Symptoms: first-stage F-statistic < 10. Consequences: 2SLS estimates biased (even in large samples), imprecise, SE unreliable. Stock-Yogo critical values formalise. Remedy: find stronger IVs or use weak-IV-robust methods (Anderson-Rubin).

### Q40. Describe the Hausman test.
**Model answer:** Tests exogeneity of a regressor: H₀: regressor is exogenous (OLS and IV both consistent, OLS efficient); H₁: regressor endogenous (only IV consistent). Statistic: H = (β̂_IV − β̂_OLS)' [Var(β̂_IV) − Var(β̂_OLS)]⁻¹ (β̂_IV − β̂_OLS) ~ χ²(k). Reject H₀ = use IV.

---

## Part E: Heteroscedasticity (Q41-45)

### Q41. What is heteroscedasticity?
**Model answer:** Var(u|X) ≠ constant. Error variance depends on regressors. Violates MLR.5 (homoscedasticity). Consequences: OLS estimates remain unbiased and consistent but standard errors are wrong → invalid t-tests, F-tests, CIs.

### Q42. State White's heteroscedasticity-consistent standard errors.
**Model answer:** Var̂(β̂)_robust = (X'X)⁻¹ [Σ ûᵢ²xᵢxᵢ'] (X'X)⁻¹. Consistent under heteroscedasticity of unknown form. Replaces σ²(X'X)⁻¹. Use with t-statistics for valid inference. Available in Stata (robust option), R (vcovHC).

### Q43. Describe the Breusch-Pagan test.
**Model answer:** Tests for heteroscedasticity. (1) Fit OLS; obtain residuals û. (2) Regress û² on X. (3) Test H₀: δ = 0 (no heteroscedasticity) via nR² ~ χ²(k) or F-test. Large stat → reject, heteroscedasticity present.

### Q44. Describe the White test.
**Model answer:** More general than BP. Regress û² on all X's, their squares, and cross-products. Test nR² against χ² with df = number of regressors in auxiliary model. Detects heteroscedasticity and nonlinearity. Power decreases with many regressors (df inflation).

### Q45. Describe Weighted Least Squares (WLS).
**Model answer:** If heteroscedasticity is known form, WLS minimises Σ wᵢûᵢ². Weights wᵢ = 1/σᵢ². Produces BLUE under correct variance specification. Alternative: Feasible GLS — estimate weights from data (e.g., regress log(û²) on X). More efficient than OLS with robust SE, but requires correct specification.

---

## Part F: Application (Q46-50)

### Q46. A wage regression: log(wage) = β₀ + β₁·educ + β₂·exper + β₃·exper² + u. Interpret β₁.
**Model answer:** β₁ is the approximate percentage increase in wage for one additional year of education, holding experience constant. Log-level interpretation. If β₁ = 0.08, each year of education associated with about 8% higher wage. Ceteris paribus — if ability is omitted and correlated with education, β̂₁ overestimates returns to education (classic OVB).

### Q47. Regress returns on market returns and volatility. R² = 0.25, VIF on volatility = 3.5. Interpret.
**Model answer:** 25% of return variance explained — typical for returns models. VIF = 3.5 is moderate — volatility somewhat collinear with market return but not problematic (threshold 5). Standard errors slightly inflated. Coefficients reliable. Recommendation: retain both variables; interpretation valid.

### Q48. Suspect OVB in a regression of income on education (omitted ability). Direction?
**Model answer:** Omitted: ability. β_ability > 0 (ability raises income). Corr(educ, ability) > 0 (ability helps education). Bias in β̂_educ = β_ability × Corr(educ, ability) > 0 — OLS overestimates return to education. Remedy: include proxy for ability (IQ, test scores), family background, or IV (distance to college).

### Q49. A first-stage regression of X on Z has F = 8.5. Evaluate.
**Model answer:** Below the Stock-Yogo critical value of 10 — weak instrument. 2SLS estimates likely biased (possibly severely) and SE unreliable. Actions: (1) Find additional or stronger instruments. (2) Use weak-IV-robust inference (Anderson-Rubin confidence sets). (3) Report first-stage F and caveat results. Don't rely on 2SLS point estimates with F < 10.

### Q50. You fit a model; BP test p = 0.01. Heteroscedasticity present. Recommend.
**Model answer:** (1) Use heteroscedasticity-robust (White) standard errors — simplest remedy, coefficients unchanged. (2) Investigate: residual plot to identify pattern. (3) Consider WLS if variance depends on known regressor. (4) Log-transform Y if variance increases with level. (5) Report robust SE alongside OLS for transparency. (6) Do not ignore — conventional SE will be wrong.

---

**Exam tip:** For regression derivation questions, always: (1) state the model and assumptions explicitly, (2) show each algebraic step — Wooldridge-style derivations, (3) identify which assumptions each step uses, (4) state what the result shows (unbiasedness, consistency, etc.). For applied questions: (1) write the model, (2) state hypotheses clearly, (3) compute test statistic with correct df, (4) interpret with units and "holding all else constant", (5) diagnose assumption violations and propose remedies.
