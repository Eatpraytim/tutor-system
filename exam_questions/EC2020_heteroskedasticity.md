# EC2020 — Heteroscedasticity: 50 Exam Questions with Model Answers

---

## Part A: Fundamentals (Q1-10)

### Q1. Define heteroscedasticity formally.
**Model answer:** Violation of the homoscedasticity assumption: Var(u|X) ≠ constant across observations. Specifically: Var(uᵢ|xᵢ) = σᵢ² varies with i. In vector notation: Var(u|X) = diag(σ₁², σ₂², ..., σₙ²), not σ²I.

### Q2. What are the consequences of heteroscedasticity for OLS?
**Model answer:** (1) OLS coefficient estimates remain unbiased and consistent. (2) OLS is no longer BLUE (not minimum variance). (3) Usual standard errors are biased, usually downward (overconfident). (4) t-statistics, F-statistics, CIs, p-values are invalid.

### Q3. Why does heteroscedasticity not bias OLS coefficients?
**Model answer:** Unbiasedness requires E(u|X) = 0 (exogeneity), not homoscedasticity. Since β̂ = β + (X'X)⁻¹X'u, its mean depends only on conditional mean assumption. Variance of u doesn't enter. Only efficiency and inference are affected.

### Q4. Give three common causes of heteroscedasticity.
**Model answer:** (1) Scale effects — variance grows with level of a variable (e.g., income, sales, firm size). (2) Data collection — combining aggregated and disaggregated observations. (3) Model mis-specification — omitted variables causing heteroscedastic residuals. (4) Discrete choice / binary outcomes inherently heteroscedastic.

### Q5. State the correct formula for Var(β̂) under heteroscedasticity.
**Model answer:** Var(β̂|X) = (X'X)⁻¹ X'ΩX (X'X)⁻¹, where Ω = diag(σ₁², ..., σₙ²) is the true error covariance matrix. The "sandwich" formula. Under homoscedasticity, Ω = σ²I, simplifying to σ²(X'X)⁻¹.

### Q6. State White's heteroscedasticity-consistent estimator.
**Model answer:** V̂_robust(β̂) = (X'X)⁻¹ [Σᵢ ûᵢ² xᵢxᵢ'] (X'X)⁻¹. Replaces unknown σᵢ² with ûᵢ². Consistent estimator of Var(β̂) under any form of heteroscedasticity. "HC0" in software; variants (HC1, HC2, HC3) adjust for small-sample bias.

### Q7. Distinguish HC0 and HC1 standard errors.
**Model answer:** HC0: White's original estimator. HC1: small-sample correction × n/(n−k−1). Similar to adjusting OLS SE by degrees of freedom. HC1 is default in Stata (vce(robust)); slightly more conservative. HC3 further adjusts using leverage — better for small samples.

### Q8. What is the practical significance of using robust SE?
**Model answer:** Insulates inference from heteroscedasticity of unknown form. Current best practice: always report robust SE for cross-sectional regression. Small cost when homoscedasticity holds (SE slightly larger), large benefit when it doesn't. Eliminates need to test and specify variance structure.

### Q9. When are robust SE asymptotically equivalent to OLS SE?
**Model answer:** When errors are homoscedastic. Ω = σ²I makes robust SE collapse to conventional OLS SE. Under heteroscedasticity, robust SE differ; under homoscedasticity, they coincide asymptotically. Choice is low-cost.

### Q10. Describe asymptotic properties of OLS with heteroscedasticity.
**Model answer:** β̂ is consistent (→ β in probability) under exogeneity. Asymptotic normal: √n(β̂ − β) → N(0, plim n·(X'X)⁻¹X'ΩX(X'X)⁻¹). Inference is asymptotically valid using robust SE. Does not require homoscedasticity for asymptotic results.

---

## Part B: Testing for Heteroscedasticity (Q11-20)

### Q11. Describe the Breusch-Pagan test.
**Model answer:** H₀: homoscedastic (Var(u|X) = σ²). (1) Estimate OLS model; get residuals û. (2) Regress û² on X (or a subset). (3) Test statistic: nR² from this auxiliary regression, ~ χ²(k) under H₀. Reject H₀ → heteroscedasticity.

### Q12. State the Breusch-Pagan assumption of normality.
**Model answer:** Original BP test assumes normal errors. Violation makes size of test incorrect. Koenker (1981) modified BP test doesn't require normality — uses a studentised version more robust to non-normal errors. Most software implements Koenker's version.

### Q13. Describe the White test.
**Model answer:** More general than BP. (1) Obtain OLS residuals û. (2) Regress û² on X, X², and cross-products X_jX_k. (3) Test: nR² ~ χ²(q), where q = number of regressors in auxiliary. Detects heteroscedasticity and non-linearity (model misspecification).

### Q14. Compare the Breusch-Pagan and White tests.
**Model answer:** BP: parsimonious, assumes linear relationship between û² and X. Powerful against this specific form. White: general, includes squares and interactions. More flexible, but loses df with many regressors — power can drop. BP preferred when variance structure is suspected linear; White for general screening.

### Q15. What is the Goldfeld-Quandt test?
**Model answer:** (1) Order observations by suspected variance-driver. (2) Split sample into two parts (drop middle 20%). (3) Fit OLS separately to each half. (4) Compute F = s²_upper/s²_lower. F ~ F(df, df). Reject H₀ of homoscedasticity if F is large. Simple; limited to one known variance driver.

### Q16. Describe a residual plot for heteroscedasticity.
**Model answer:** Plot residuals û vs fitted ŷ (or vs each X). Random scatter = homoscedasticity. Fan/funnel shape = heteroscedasticity (variance grows/shrinks with ŷ or X). Systematic pattern (curve) = misspecification. Essential diagnostic before and after heteroscedasticity tests.

### Q17. How do you interpret a significant BP test?
**Model answer:** Reject H₀ of homoscedasticity. Evidence that Var(u|X) depends on regressors. Implications: (1) OLS inference unreliable. (2) Use robust SE. (3) Consider weighted LS or transformation. (4) Check for omitted variables or misspecification. Significant BP alone is not alarming if robust SE used.

### Q18. What if BP is non-significant but residual plot shows funnel?
**Model answer:** BP may lack power (small n, weak variance structure). Trust the visual pattern over the statistical test. Use robust SE or transformation. Conversely, BP significant with no visual pattern may reflect non-normality, not true heteroscedasticity — Koenker's modified test preferred.

### Q19. Describe Park's test.
**Model answer:** Regress log(û²) on log(X_j) for suspected variance-driver. If coefficient significantly differs from 0, evidence of heteroscedasticity proportional to a power of X_j. Specific functional form test. Useful for identifying variance structure for WLS.

### Q20. What are some other heteroscedasticity tests?
**Model answer:** Glejser test (regress |û| on X), Harvey-Godfrey (log(û²) on X), White without cross-products, Koenker's LM. All are variants of the same idea: regressing a function of squared residuals on regressors. Report test choice and results.

---

## Part C: Handling Heteroscedasticity (Q21-30)

### Q21. Describe Weighted Least Squares (WLS).
**Model answer:** Minimise Σ wᵢ (yᵢ − x'ᵢβ)². Weights wᵢ = 1/σᵢ² downweight high-variance observations. If weights are correctly specified, WLS is BLUE under heteroscedasticity — more efficient than OLS. Matrix form: β̂_WLS = (X'WX)⁻¹X'Wy.

### Q22. State the assumption required for WLS to be BLUE.
**Model answer:** Correctly specified variance structure: σᵢ² known up to a proportionality constant. Under correct specification, WLS minimises variance among linear unbiased estimators. Under misspecification, may be worse than OLS with robust SE.

### Q23. Describe Feasible Generalised Least Squares (FGLS).
**Model answer:** When σᵢ² is unknown, estimate it from data first. (1) Run OLS; get û. (2) Specify functional form, e.g., log(û²) = α₀ + α₁log(Xᵢ) + vᵢ. (3) Use fitted ûᵢ² as weights in WLS. Iterate if needed. Consistent under correct specification; more efficient than OLS + robust SE.

### Q24. When is WLS preferred over OLS with robust SE?
**Model answer:** (1) When correct variance structure is known from theory. (2) Large sample with strong evidence of a specific heteroscedasticity pattern. (3) Efficiency gain over OLS is substantial. (4) Small samples where robust SE may be unreliable. Otherwise, OLS with robust SE is the safer default.

### Q25. What if WLS is misspecified?
**Model answer:** WLS with wrong weights can be less efficient than OLS. Generally: OLS is consistent regardless; WLS is only BLUE under correct specification. Report robust SE for WLS estimates too — protects against misspecification of the variance structure.

### Q26. Describe variance-stabilising transformations.
**Model answer:** Transform Y to achieve homoscedasticity. Common: (1) log(Y) if variance increases with mean. (2) √Y for count data (Poisson). (3) arcsine√p for proportions. (4) Box-Cox for flexible power. Change interpretation: log-Y gives percentage effects; √Y gives changes in √. Re-fit and recheck residuals.

### Q27. When does log-transforming Y help with heteroscedasticity?
**Model answer:** When the variance of Y increases proportionally to its mean (coefficient of variation constant). Example: income data. Log-transform compresses high values more than low, stabilising variance. Check residuals after log transform — often homoscedastic in log. Caveat: interpretation in percentage changes.

### Q28. Describe clustered standard errors.
**Model answer:** When observations cluster (e.g., students in schools, employees in firms), errors may be correlated within clusters. Clustered SE account for within-cluster correlation. Formula: V̂_cluster = (X'X)⁻¹ [Σ_g X'_g ûûᵀ X_g] (X'X)⁻¹, summed over clusters g. Standard in panel data.

### Q29. When do you use clustered SE?
**Model answer:** (1) Grouped data with possible within-group correlation (workers in firms, students in schools). (2) Panel data with serial correlation within units. (3) Sampling clusters rather than individuals. Common rule: cluster at the level of treatment assignment. Number of clusters matters — need G ≥ 30-50 for reliable SE.

### Q30. Compare robust and clustered SE.
**Model answer:** Robust: heteroscedasticity only. Clustered: heteroscedasticity + within-cluster correlation. Clustered is more general but requires defined clusters. Use clustered when grouping is known; otherwise robust. Difference can be large when within-cluster correlation is high.

---

## Part D: Specific Heteroscedasticity Patterns (Q31-40)

### Q31. Describe heteroscedasticity proportional to a regressor.
**Model answer:** σᵢ² = σ² · X_{ji}. Weights wᵢ = 1/X_{ji}. Equivalent to dividing both sides of the regression by √X_{ji}. WLS easy when you know which regressor drives the variance. Common in cross-sectional data where variance scales with size.

### Q32. Describe heteroscedasticity in cross-country panels.
**Model answer:** Countries may have very different error variances (small vs large economies). Solutions: (1) Cluster SE by country. (2) Normalise variables (per capita, log). (3) Include country fixed effects. (4) Heteroscedasticity-robust SE for cross-sectional queries.

### Q33. What is "multiplicative heteroscedasticity"?
**Model answer:** log(σᵢ²) = α₀ + α₁X_{ji}. Variance grows exponentially with X_j. After fitting, weights wᵢ = 1/exp(α̂₀ + α̂₁X_{ji}). Harvey (1976) test examines this directly. Common when underlying data-generating process is lognormal.

### Q34. When can fixed effects eliminate heteroscedasticity?
**Model answer:** If heteroscedasticity is between-unit only (each unit has own variance, constant over time), fixed effects transformation (demean within unit) eliminates unit-level variance differences. Remaining heteroscedasticity within unit must still be addressed via robust SE.

### Q35. Heteroscedasticity in time-series context.
**Model answer:** Time-varying variance can be: (1) Level-dependent (variance grows with Y). (2) Volatility clustering (ARCH/GARCH). Tests: ARCH-LM test. Remedies: (1) Log-transform. (2) Model variance explicitly (GARCH). (3) Robust SE (Newey-West for serial correlation + heteroscedasticity).

### Q36. Describe GARCH models for heteroscedasticity.
**Model answer:** Generalised Autoregressive Conditional Heteroscedasticity. σᵢ² = α₀ + α₁uᵢ₋₁² + β₁σᵢ₋₁². Variance depends on past squared errors and past variances. Captures volatility clustering (common in finance). Estimate via MLE. Applications: return volatility, VaR.

### Q37. Describe Newey-West standard errors.
**Model answer:** HAC (Heteroscedasticity and Autocorrelation Consistent) estimator for time series. Accounts for heteroscedasticity AND serial correlation simultaneously. Based on kernel weighting of lagged autocovariances. Bandwidth parameter (lag length) must be chosen. Standard for time-series regression.

### Q38. What is the first step in suspecting heteroscedasticity?
**Model answer:** (1) Visual inspection of residual plots (û vs ŷ, û vs each X). (2) Economic reasoning — is variance likely to vary? Example: wages probably heteroscedastic by age or tenure. (3) Descriptive statistics of residuals by sub-group. (4) Formal tests (BP, White). Don't skip visual inspection — tests miss some patterns.

### Q39. Describe GLS under heteroscedasticity.
**Model answer:** General version of WLS: minimise (y − Xβ)'Ω⁻¹(y − Xβ). β̂_GLS = (X'Ω⁻¹X)⁻¹X'Ω⁻¹y. Requires knowing Ω (variance-covariance matrix). Generalises to serial correlation too. GLS is BLUE under correct specification. In practice, use FGLS with estimated Ω̂.

### Q40. Practical advice: what's your default strategy?
**Model answer:** (1) Always use heteroscedasticity-robust (White) SE. (2) Plot residuals to inspect pattern. (3) Consider log-transforming Y if variance increases with level. (4) Use cluster-robust SE if data have natural groups. (5) WLS only when variance structure is theoretically clear. (6) Report results with both OLS and robust SE if substantive.

---

## Part E: Numerical Problems (Q41-45)

### Q41. Given BP statistic = 12.3, df = 3. Interpret.
**Model answer:** Compare to χ²_{0.05, 3} = 7.815. 12.3 > 7.815, so reject H₀ at 5%. Heteroscedasticity present. p-value ≈ 0.006. Use robust SE for inference. Investigate variance structure with residual plots.

### Q42. Sample split into two halves by firm size: s²_large = 2,500; s²_small = 500. Goldfeld-Quandt test, 20 firms each.
**Model answer:** F = 2500/500 = 5.0, df = (19, 19). Critical F_{0.05, 19, 19} ≈ 2.17. Since 5.0 > 2.17, reject H₀ of equal variances. Heteroscedasticity present — variance grows with firm size.

### Q43. In WLS, weights wᵢ = 1/X_{ji}. Compute weighted regression coefficient if data has xᵢ = 10, 20, 30 and yᵢ = 50, 100, 160.
**Model answer:** Weights: 1/10, 1/20, 1/30 = 0.1, 0.05, 0.033. Equivalent transformation: dividing equation by √xᵢ. Transformed: yᵢ* = yᵢ/√xᵢ, xᵢ* = √xᵢ. Transformed data: y* = 15.81, 22.36, 29.22; x* = 3.16, 4.47, 5.48. OLS on transformed gives β̂_WLS. Computing: β̂₁ ≈ 5.4 (approximation; actual calculation shows WLS vs OLS differences).

### Q44. OLS SE = 0.5; White robust SE = 0.9. Interpret.
**Model answer:** Robust SE is 80% larger than OLS SE — substantial heteroscedasticity. OLS inference was overconfident. Using conservative robust SE: t-stat = β̂/0.9 (using robust) vs β̂/0.5 (OLS). Hypothesis test conclusions may differ. Always report robust SE.

### Q45. Forecasting with WLS gives RMSE 2.1; OLS RMSE 2.5. Evaluate.
**Model answer:** WLS yields better fit in weighted metric. OLS RMSE 2.5 — in unweighted terms, WLS may not improve. Depends on weighting scheme. Efficiency gain only if variance structure specified correctly. Cross-validate against true variance structure.

---

## Part F: Application (Q46-50)

### Q46. A regression of expenditure on income shows classic funnel shape. Recommend.
**Model answer:** Heteroscedasticity — variance of expenditure grows with income. Remedies: (1) Use White's robust SE — quick, no model change. (2) Log-transform both: log(exp) = α + β log(inc) — interprets as elasticity, usually stabilises variance. (3) WLS with wᵢ = 1/income. Examine which approach gives stable residuals; report with appropriate SE.

### Q47. Panel data of firms over 10 years. Test for heteroscedasticity?
**Model answer:** (1) Test firm-level heteroscedasticity via Breusch-Pagan on residuals after including firm fixed effects. (2) Use cluster-robust SE clustered by firm — accounts for within-firm correlation and heteroscedasticity. (3) If time trends differ by firm, consider random coefficients model. (4) Report with clustered SE as default for panel data.

### Q48. Your OLS has R² = 0.45, but robust SE are very different from OLS SE. What does this indicate?
**Model answer:** Strong heteroscedasticity. OLS coefficients are unbiased but OLS SE are wrong. Robust SE is the correct inference — may change significance of variables. Pattern: (1) Examine residual plots. (2) Consider WLS if variance structure is clear. (3) Report robust SE as primary. (4) Do not rely on OLS SE.

### Q49. Finance returns model: OLS gives insignificant coefficient; HAC gives significant. Which to trust?
**Model answer:** Trust the HAC-based inference. Financial data typically exhibit heteroscedasticity AND autocorrelation. HAC (Newey-West) corrects for both, giving valid SE. OLS SE are biased, often underestimated, but can also be overstated. HAC is the correct standard for time-series regression.

### Q50. A BP test has p = 0.15. Researcher claims "no heteroscedasticity present". Critique.
**Model answer:** Statistical non-rejection doesn't prove H₀. Power may be low (small n, weak pattern). Recommendations: (1) Examine residual plots visually — formal tests miss some patterns. (2) Use robust SE anyway — low-cost insurance. (3) Try Koenker's version (robust to non-normality). (4) Consider alternative tests (White, GQ). (5) Statistical non-rejection with visual heteroscedasticity: trust the data, use robust SE. Don't dismiss heteroscedasticity concerns based on one non-significant test.

---

**Exam tip:** For heteroscedasticity questions, always: (1) state what heteroscedasticity is and why it matters, (2) present visual and formal test evidence, (3) recommend specific remedies (robust SE preferred; WLS if structure known), (4) interpret consequences for inference (invalid t, F, CI), (5) show the sandwich formula for robust variance when asked.
