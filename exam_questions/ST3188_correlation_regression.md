# ST3188 — Correlation & Regression: 50 Exam Questions with Model Answers

---

## Part A: Correlation Fundamentals (Q1-10)

### Q1. Define the Pearson correlation coefficient.
**Model answer:** A measure of linear association between two continuous variables: r = Cov(X, Y) / (σ_X · σ_Y). Ranges from −1 to +1. r = 0 implies no linear relationship (but may have non-linear). Symmetric: r(X, Y) = r(Y, X).

### Q2. State the assumptions of Pearson correlation.
**Model answer:** (1) Both variables continuous. (2) Approximately linear relationship. (3) Variables approximately normally distributed (bivariate normal). (4) No severe outliers (r sensitive to outliers). (5) Random sampling. For large samples, normality assumption relaxes via CLT.

### Q3. When should you use Spearman instead of Pearson?
**Model answer:** When: (1) data are ordinal, (2) relationship is monotonic but non-linear, (3) outliers distort Pearson, (4) data are severely non-normal. Spearman = Pearson on ranked data, more robust to outliers and non-linearity (monotonic).

### Q4. Compare Pearson, Spearman, and Kendall's tau.
**Model answer:** Pearson: measures linear relationships, sensitive to outliers. Spearman: measures monotonic relationships via ranks, more robust. Kendall's τ: proportion of concordant minus discordant pairs; interpretable probabilistically but similar to Spearman. Use Pearson for continuous linear data; Spearman or Kendall for ordinal or non-linear.

### Q5. Why can correlation be zero for related variables?
**Model answer:** Pearson measures linear association. Non-linear relationships (e.g., Y = X²) can yield r = 0 despite perfect dependence. Always examine a scatter plot before concluding "no relationship" from r ≈ 0.

### Q6. Interpret r = 0.75.
**Model answer:** Strong positive linear association. As X increases, Y tends to increase. About 56% (r² = 0.5625) of variance in Y is shared with X in a linear sense. "Strong" is conventional: |r| > 0.7 often called strong; 0.3-0.7 moderate; < 0.3 weak (depending on context).

### Q7. Why is r not a measure of causation?
**Model answer:** Correlation only measures association. Could be: (1) X causes Y, (2) Y causes X (reverse), (3) Z causes both X and Y (confounding), (4) coincidence. Causation requires experimental control (randomised trials) or careful quasi-experimental design (IV, RDD).

### Q8. What is the coefficient of determination r²?
**Model answer:** The proportion of variance in Y explained by linear regression on X. r² ∈ [0, 1]. r² = 0.6 means 60% of Y's variance is linearly explained by X. Unlike r, r² doesn't capture direction. Interpretable as explanatory power.

### Q9. State the test for H₀: ρ = 0.
**Model answer:** t = r · √[(n−2)/(1−r²)], df = n−2. Under H₀, t ~ t(n−2). Two-sided critical value t_{α/2, n−2}. Equivalent to F-test in simple regression.

### Q10. How do you interpret a confidence interval for ρ?
**Model answer:** Use Fisher's z-transformation: z_r = 0.5 · ln((1+r)/(1−r)). Compute CI for z_r (approximately normal), then back-transform. A CI excluding 0 indicates significant correlation. Wider CIs indicate less precision (smaller n or weaker evidence).

---

## Part B: Simple Linear Regression (Q11-20)

### Q11. State the simple linear regression model.
**Model answer:** Y_i = β₀ + β₁X_i + ε_i, where Y is the response, X the predictor, β₀ intercept, β₁ slope, ε error term with E(ε|X) = 0 and Var(ε|X) = σ². Conditional mean: E(Y|X) = β₀ + β₁X.

### Q12. How does OLS minimise the sum of squared residuals?
**Model answer:** OLS finds β̂₀, β̂₁ minimising Σ(Y_i − β̂₀ − β̂₁X_i)². Setting partial derivatives to zero gives the normal equations. Solution: β̂₁ = Cov(X,Y)/Var(X), β̂₀ = Ȳ − β̂₁X̄.

### Q13. Interpret the slope in a business context.
**Model answer:** A one-unit increase in X is associated with an average change of β̂₁ units in Y. Include units and the "on average" qualifier. Example: if X = advertising spend ($k), Y = sales ($k), β̂₁ = 3 means "£1k more advertising → £3k more sales on average."

### Q14. Interpret the intercept.
**Model answer:** β̂₀ is the expected Y when X = 0. Often not meaningful if X = 0 is outside the data range or nonsensical (e.g., regressing weight on height). Still necessary for prediction; interpret only when the value X = 0 is plausible.

### Q15. What is the standard error of the estimate (s_e)?
**Model answer:** s_e = √(SSE/(n−2)) measures typical residual size in Y's units. Roughly ±2s_e covers 95% of residuals. Used in prediction intervals and SE of slope. Smaller s_e indicates better fit.

### Q16. State the formula for R² in simple regression.
**Model answer:** R² = 1 − SSE/SST = SSR/SST. In simple regression, R² = r² (square of Pearson correlation). R² ∈ [0, 1]. Proportion of Y's variance explained by the model.

### Q17. Explain the difference between a confidence interval for the mean response and a prediction interval.
**Model answer:** Confidence interval: for E(Y|X = x₀) — the mean Y at a given X. Prediction interval: for a new single observation Y at X = x₀. Prediction intervals are wider because they include both the uncertainty in estimating the mean AND the inherent variability σ² of individual Y values.

### Q18. How does sample size affect regression inference?
**Model answer:** Larger n → (i) smaller standard errors for β̂, (ii) narrower CIs, (iii) higher power. The CI width scales as 1/√n. Also, large n makes p-values tiny even for trivial effects — always pair statistical significance with effect size and CI.

### Q19. What is the F-test in simple regression?
**Model answer:** Tests H₀: β₁ = 0 vs H₁: β₁ ≠ 0 using F = MSR/MSE = (SSR/1)/(SSE/(n−2)). In simple regression, F = t². Equivalent to t-test of slope but reported alongside ANOVA table.

### Q20. When is a non-linear transformation appropriate?
**Model answer:** When residual plots show systematic curvature, or theory suggests non-linearity. Common transforms: log(Y), √Y, 1/Y, X², log(X). Check assumptions after transformation. Interpretation changes: log transforms yield percentage-change interpretations.

---

## Part C: Multiple Regression (Q21-30)

### Q21. State the multiple regression model.
**Model answer:** Y_i = β₀ + β₁X_{1i} + β₂X_{2i} + ... + β_k X_{ki} + ε_i. β_j is the partial effect of X_j on Y, holding all other predictors constant. Coefficients are interpreted controlling for other variables in the model.

### Q22. Interpret a coefficient with "holding all else constant".
**Model answer:** β̂_j is the expected change in Y for a one-unit increase in X_j, holding all other predictors in the model fixed. Example: β̂(education) = 2000 in a salary regression means "one more year of education → £2,000 higher salary, given same experience and other variables."

### Q23. What is adjusted R² and why does it matter?
**Model answer:** Adjusted R² = 1 − [(1−R²)(n−1)/(n−k−1)]. Penalises addition of predictors. Unlike R², can decrease when adding variables that don't improve fit enough. Use adjusted R² (not R²) to compare models with different numbers of predictors.

### Q24. What is multicollinearity and how to detect it?
**Model answer:** High correlation among predictors. Detection: VIF_j = 1/(1−R²_j); values > 10 indicate serious multicollinearity. Condition index > 30 also signals. Consequences: inflated SEs, unstable coefficients, sign changes — but predictions are unaffected.

### Q25. State the assumption of no perfect multicollinearity.
**Model answer:** No exact linear relationship among predictors. If violated, (X'X) is singular and OLS has no unique solution. Near-multicollinearity (high VIF) inflates variances but OLS still estimable. Common cause: redundant or overly correlated variables.

### Q26. Explain dummy variable coding.
**Model answer:** For a categorical variable with g levels, create g−1 dummies (0/1). One level serves as reference (omitted). Coefficients compare each level to the reference. Include all g dummies + intercept → "dummy variable trap" (perfect collinearity).

### Q27. When should you use interaction terms?
**Model answer:** When the effect of one predictor depends on another. Add X₁·X₂ to the model: Y = β₀ + β₁X₁ + β₂X₂ + β₃(X₁X₂) + ε. The effect of X₁ becomes (β₁ + β₃X₂) — it varies with X₂. Interpret carefully: slopes are conditional.

### Q28. State the six assumptions of multiple regression.
**Model answer:** (1) Linearity in parameters. (2) Random sampling. (3) No perfect multicollinearity. (4) Zero conditional mean: E(ε|X) = 0. (5) Homoscedasticity: Var(ε|X) = σ². (6) Normality of errors (for exact inference in small samples).

### Q29. What are common ways to check regression assumptions?
**Model answer:** (1) Residuals vs fitted plot — linearity and homoscedasticity. (2) Q-Q plot of residuals — normality. (3) VIF — multicollinearity. (4) Durbin-Watson — autocorrelation. (5) Cook's distance — influential observations. (6) Scale-location plot — homoscedasticity.

### Q30. How do you interpret the overall F-test in multiple regression?
**Model answer:** F tests H₀: β₁ = β₂ = ... = β_k = 0 (all slopes simultaneously zero) vs H₁: at least one β_j ≠ 0. Rejecting means the model has explanatory power — some predictor(s) are useful. Follow up with individual t-tests.

---

## Part D: Numerical Problems (Q31-40)

### Q31. Given r = 0.6, n = 25, test H₀: ρ = 0.
**Model answer:** t = 0.6·√(23/0.64) = 0.6·√35.94 = 0.6·5.996 = 3.60. df = 23. Critical t_{0.025, 23} ≈ 2.07. Since |3.60| > 2.07, reject H₀ — correlation is significantly different from 0.

### Q32. Given Σ(x−x̄)² = 150, Σ(x−x̄)(y−ȳ) = 75, x̄ = 10, ȳ = 25. Find the regression equation.
**Model answer:** β̂₁ = 75/150 = 0.5. β̂₀ = 25 − 0.5(10) = 20. Regression: ŷ = 20 + 0.5x. Interpretation: a 1-unit increase in x is associated with a 0.5-unit increase in y.

### Q33. SSR = 80, SSE = 20, n = 12. Compute R², s_e, and test overall significance.
**Model answer:** SST = SSR + SSE = 100. R² = 80/100 = 0.80. s_e = √(20/10) = √2 = 1.41. F = (SSR/1)/(SSE/(n−2)) = 80/2 = 40. df = (1, 10). Critical F_{0.05, 1, 10} = 4.96. Since 40 > 4.96, reject H₀ — model is highly significant.

### Q34. β̂₁ = 2.5, SE = 0.8, n = 30. Construct 95% CI for β₁.
**Model answer:** df = 28. t_{0.025, 28} ≈ 2.048. CI = 2.5 ± 2.048(0.8) = 2.5 ± 1.64 = [0.86, 4.14]. Since 0 is not in the interval, reject H₀ at 5% level.

### Q35. In multiple regression, R² = 0.75, n = 50, k = 4. Compute adjusted R² and F.
**Model answer:** Adj R² = 1 − (1−0.75)(49)/(45) = 1 − 0.272 = 0.728. F = (R²/k)/((1−R²)/(n−k−1)) = (0.75/4)/(0.25/45) = 0.1875/0.00556 = 33.75. df = (4, 45). p << 0.05. Model highly significant.

### Q36. VIF for a predictor is 8. Interpret.
**Model answer:** VIF = 8 means SE of that coefficient is √8 ≈ 2.83 times larger than it would be without multicollinearity. This is moderate concern — above 5 threshold but below serious 10. Consider whether this predictor is redundant with others.

### Q37. Given y = 50 + 3x₁ − 1.5x₂ + 0.8x₃, predict y when x₁ = 10, x₂ = 8, x₃ = 5.
**Model answer:** ŷ = 50 + 3(10) − 1.5(8) + 0.8(5) = 50 + 30 − 12 + 4 = 72. Confidence in prediction depends on whether these x values are within the sample range (interpolation) or outside (extrapolation — riskier).

### Q38. 95% CI for E(Y|x=5) = [45, 55]. Predict and interpret.
**Model answer:** The CI for the mean response at x = 5 is [45, 55]. We are 95% confident the true average Y for all observations with x = 5 lies in [45, 55]. For a single new observation at x = 5, use a prediction interval, which is wider (includes σ²).

### Q39. Residual plot shows curvature. What should you do?
**Model answer:** Linearity assumption violated. Options: (1) Add polynomial terms (X², X³). (2) Transform Y (log, √). (3) Transform X. (4) Use non-linear regression or splines. After fitting new model, re-examine residual plot.

### Q40. With n = 100, β̂₁ = 0.02, SE = 0.008. Is this significant? Practically important?
**Model answer:** t = 0.02/0.008 = 2.5, df = 98. p ≈ 0.014 < 0.05 — statistically significant. However, magnitude is tiny (0.02 units of Y per unit X). Practical importance depends on scale and context — is 0.02 meaningful? With very large n, even trivial effects become significant. Report effect size (perhaps standardised β) and discuss context.

---

## Part E: True/False and Interpretation (Q41-45)

### Q41. T/F: A significant correlation implies a strong correlation.
**Model answer:** FALSE. "Significant" means statistically distinguishable from zero. With large n, weak correlations (r = 0.1) can be significant but not strong. Always report r alongside p-value and evaluate strength on its own terms.

### Q42. T/F: OLS regression requires normally distributed X variables.
**Model answer:** FALSE. OLS requires normally distributed residuals (errors), not X. X can be fixed or any distribution. For exact small-sample inference, residuals should be approximately normal. Large n relaxes this via CLT.

### Q43. T/F: If two predictors are correlated, one must be removed.
**Model answer:** FALSE. Correlation alone doesn't require removal. Check VIF. If VIF > 10, multicollinearity is severe and removing one variable or combining them is prudent. For VIF < 10, keep both if each has theoretical justification.

### Q44. T/F: R² = 1 means the model is perfect and will predict new data perfectly.
**Model answer:** FALSE. R² = 1 means the model fits the training data perfectly. It does NOT imply perfect out-of-sample predictions. Overfitting produces high training R² but poor generalisation. Use cross-validation to assess true predictive performance.

### Q45. T/F: A non-significant slope means X and Y are independent.
**Model answer:** FALSE. Non-significance = failure to reject H₀: β₁ = 0. Could be weak linear effect, non-linear dependence, or small sample. Independence is a stronger claim — examine a scatter plot and consider non-linear relationships.

---

## Part F: Application (Q46-50)

### Q46. A regression of sales on advertising spend gives β̂₁ = 2.5, p = 0.001, R² = 0.45. Recommend.
**Model answer:** Statistically significant positive relationship — each £1k increase in ad spend is associated with £2.5k more sales. 45% of variance in sales explained. Recommendation: continue advertising investment; however, 55% unexplained suggests other drivers (seasonality, competition, pricing) — extend model with these predictors. Check for diminishing returns: is the linear model valid across the advertising range? Consider adding advertising² term.

### Q47. You're given salary data vs education (yrs), experience (yrs), and gender. Describe the modelling approach.
**Model answer:** Model: log(salary) = β₀ + β₁·education + β₂·experience + β₃·Female + β₄·(exp)² + ε. (1) Log Y captures multiplicative effects and skewed income distribution. (2) Dummy for gender (male = reference). (3) Experience² for diminishing returns. (4) Interaction Female·experience if gender differences vary with experience. Check assumptions; interpret coefficients as approximate percentages. Report unadjusted and adjusted gender gap.

### Q48. Your regression has R² = 0.9 but out-of-sample R² = 0.3. Diagnose.
**Model answer:** Severe overfitting. In-sample fit is deceptive — the model has memorised noise rather than capturing generalisable patterns. Causes: too many predictors relative to sample size, polynomial/interaction terms that fit random variation, colinear predictors. Remedies: (1) simpler model (fewer predictors), (2) regularisation (ridge, LASSO), (3) cross-validation during model selection, (4) larger training sample. Report out-of-sample performance as the honest measure.

### Q49. Regression of house price on size, bedrooms, location gives residuals with fan shape over fitted values. Diagnose and remedy.
**Model answer:** Heteroscedasticity — variance of errors increases with fitted values (possibly with price). Remedies: (1) Log-transform price: log(price) = β₀ + β₁·size + ... — often stabilises variance and produces elasticity interpretations. (2) Weighted Least Squares with weights 1/fitted. (3) Robust (White) standard errors for valid inference without changing model. (4) Report robust SE alongside OLS for transparency.

### Q50. You have 50 potential predictors and only n = 100 observations. Describe your regression strategy.
**Model answer:** Classical multiple regression is infeasible (n/k ratio too low). Strategy: (1) Theoretical pre-screening — drop predictors without substantive justification. (2) Domain knowledge selection — retain ~10 hypothesised drivers. (3) Regularisation: LASSO (α = 1) or Ridge (α = 0) or Elastic Net to handle high-dimensional regression and perform shrinkage. (4) Cross-validation to choose penalty. (5) Report model's out-of-sample performance. (6) If remaining is still too many, use PCA to reduce dimension first. (7) Cautious with interpretation — shrunk coefficients have biased magnitudes.

---

**Exam tip:** For correlation/regression questions, always: (1) state the model mathematically, (2) check assumptions (linearity, homoscedasticity, normality, no multicollinearity), (3) report coefficients with SE, t-stat, p, CI, (4) report R², adjusted R², and F for overall fit, (5) interpret coefficients with units and "holding all else constant", (6) discuss assumption violations and remedies.
