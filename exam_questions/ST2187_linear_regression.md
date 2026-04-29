# ST2187 — Linear Regression: 50 Exam Questions with Model Answers

---

## Part A: Definitions and Conceptual (Q1-10)

### Q1. Define simple linear regression.
**Model answer:** Simple linear regression models the conditional mean of a response variable Y as a linear function of a single predictor X: E(Y|X) = β₀ + β₁X. It estimates two parameters (intercept β₀ and slope β₁) using sample data to quantify the average change in Y for a one-unit change in X.

### Q2. What does the OLS method minimise?
**Model answer:** Ordinary Least Squares minimises the sum of squared residuals: Σ(yᵢ − ŷᵢ)². It finds the line that is closest to all data points in squared vertical distance, giving equal weight to positive and negative errors and penalising large errors more than small ones.

### Q3. State the population regression equation and define each term.
**Model answer:** Yᵢ = β₀ + β₁Xᵢ + εᵢ where Yᵢ is the response, Xᵢ is the predictor, β₀ is the population intercept, β₁ is the population slope, and εᵢ is a random error term with E(εᵢ|X) = 0.

### Q4. What is the difference between correlation and simple linear regression?
**Model answer:** Correlation measures the strength and direction of linear association between two variables symmetrically — r(X,Y) = r(Y,X). Regression models the conditional mean of Y given X asymmetrically, producing a slope with units and allowing prediction. Correlation is bounded [-1,1]; slope is not.

### Q5. Why is R² = r² true only in simple linear regression?
**Model answer:** In simple regression with one predictor, R² equals the squared Pearson correlation because both measure the proportion of variance in Y linearly explained by X. In multiple regression, R² is the squared multiple correlation, which involves all predictors jointly, so the simple squared pairwise correlation no longer equals R².

### Q6. Define the residual.
**Model answer:** The residual for observation i is the difference between observed and fitted values: ε̂ᵢ = yᵢ − ŷᵢ. It is the sample analogue of the unobservable error εᵢ and is used to estimate σ² and check regression assumptions.

### Q7. Explain what R² measures and its limitations.
**Model answer:** R² measures the proportion of total variation in Y explained by the regression model: R² = 1 − SSE/SST. Limitations: (i) always increases when predictors are added, (ii) does not measure predictive accuracy on new data, (iii) high R² does not imply causation, (iv) low R² can still indicate a useful relationship if the slope is interpretable.

### Q8. What is the standard error of the estimate (s_e)?
**Model answer:** s_e = √(SSE/(n−2)) measures the typical size of residuals in the units of Y. Roughly 95% of observed Y values will fall within ±2s_e of fitted values. It is used in prediction intervals and to compute the standard error of the slope.

### Q9. State the Gauss-Markov theorem.
**Model answer:** Under the Gauss-Markov assumptions (linearity in parameters, random sampling, zero conditional mean, homoscedasticity, no perfect collinearity), the OLS estimators are the Best Linear Unbiased Estimators (BLUE) — they have the minimum variance among all linear unbiased estimators.

### Q10. Why is the intercept often not meaningfully interpretable?
**Model answer:** The intercept β₀ is the expected Y when X = 0. It is only meaningful if X = 0 lies within the observed range of the data and makes physical sense. For example, regressing salary on years of experience, the intercept is the expected salary at 0 years, which may be plausible; but regressing weight on height, the intercept at height = 0 is nonsensical.

---

## Part B: Formula Recall (Q11-17)

### Q11. State the OLS slope formula.
**Model answer:** β̂₁ = Σ(xᵢ − x̄)(yᵢ − ȳ) / Σ(xᵢ − x̄)² = Cov(X,Y)/Var(X) = r · (s_Y/s_X).

### Q12. State the OLS intercept formula and explain why it guarantees the line passes through (x̄, ȳ).
**Model answer:** β̂₀ = ȳ − β̂₁x̄. Substituting X = x̄ gives ŷ = ȳ − β̂₁x̄ + β̂₁x̄ = ȳ, so the fitted line passes through the point of means (x̄, ȳ) by construction.

### Q13. Write the formula for the standard error of the slope.
**Model answer:** SE(β̂₁) = s_e / √(Σ(xᵢ − x̄)²) = s_e / (s_X · √(n−1)). It decreases with larger n, larger variation in X, and smaller residual spread.

### Q14. State the t-statistic and its degrees of freedom for testing H₀: β₁ = 0.
**Model answer:** t = β̂₁ / SE(β̂₁) with df = n − 2. Under H₀ and normality, t follows a t-distribution with n − 2 degrees of freedom.

### Q15. State the formula for a 95% confidence interval for the slope.
**Model answer:** β̂₁ ± t_{0.025, n−2} · SE(β̂₁). The critical value depends on df; for large n, t_{0.025} ≈ 1.96.

### Q16. State the relationship between F and t in simple regression.
**Model answer:** In simple linear regression, F = t² where F tests overall model significance with df (1, n−2) and t tests the slope with df (n−2). They give identical p-values for the two-sided slope test.

### Q17. State the decomposition SST = SSR + SSE and define each term.
**Model answer:** SST = Σ(yᵢ − ȳ)² is the total sum of squares; SSR = Σ(ŷᵢ − ȳ)² is the regression sum of squares (explained); SSE = Σ(yᵢ − ŷᵢ)² is the residual sum of squares (unexplained). The identity holds because of OLS orthogonality.

---

## Part C: Interpretation Questions (Q18-30)

### Q18. Given ŷ = 25 + 3.2x with SE(β̂₁) = 0.8, n = 40, interpret the slope.
**Model answer:** A one-unit increase in X is associated with an estimated 3.2-unit increase in the expected value of Y, holding all else constant. (Always include units if given and the "expected/on average" qualifier.)

### Q19. Given R² = 0.65, interpret this value.
**Model answer:** 65% of the variation in the response variable Y is explained by variation in the predictor X through the linear model. 35% remains unexplained, suggesting other factors affect Y or the relationship is not purely linear.

### Q20. Given p-value = 0.003 for the slope, state the conclusion at α = 0.05.
**Model answer:** Since p = 0.003 < 0.05, we reject H₀: β₁ = 0. There is statistically significant evidence that X has a non-zero linear effect on Y at the 5% significance level.

### Q21. Given 95% CI for slope = [1.2, 4.8], interpret and link to hypothesis test.
**Model answer:** We are 95% confident the true population slope lies between 1.2 and 4.8. Because zero is not in the interval, this is equivalent to rejecting H₀: β₁ = 0 at the 5% level — the duality principle between CIs and two-sided tests.

### Q22. If ANOVA F = 48.2, p < 0.001, interpret.
**Model answer:** The model has highly statistically significant overall explanatory power. The predictors jointly explain a significant portion of variation in Y. In simple regression this is equivalent to the slope t-test.

### Q23. How would you interpret a dummy variable coefficient of −2.5 where dummy = 1 for "female" and 0 for "male"?
**Model answer:** On average, females have a Y value 2.5 units lower than males, holding all other variables constant. The male group is the reference category, and the coefficient captures the estimated mean difference between groups.

### Q24. The residual for observation 15 is 8.2 units. What does this tell you?
**Model answer:** Observation 15 has a Y value 8.2 units larger than the model predicts. It is a positive residual, meaning the model under-predicts for this point. Whether this is unusual depends on the typical residual size (compare to s_e).

### Q25. Interpret a negative slope of −0.45 for the regression of "hours of exercise" on "body fat percentage".
**Model answer:** An additional hour of exercise per week is associated with an average decrease of 0.45 percentage points in body fat, holding other variables constant. Note this is association, not causation — experimental design would be needed to claim causality.

### Q26. What does it mean if R² = 0.08?
**Model answer:** The model explains only 8% of variation in Y. The remaining 92% is due to other factors or non-linear relationships. A significant slope can still exist — a low R² with large n can produce small p-values — but the model has weak predictive power.

### Q27. Interpret the statement: "The 95% prediction interval for Y at X = 50 is [42, 78]."
**Model answer:** For a new observation with X = 50, we are 95% confident its Y value will fall between 42 and 78. Prediction intervals account for both the uncertainty in estimating the mean response and the inherent variability σ² of individual observations, so they are wider than confidence intervals for the mean response.

### Q28. A coefficient has p-value = 0.001 but magnitude 0.002. How do you interpret this?
**Model answer:** The effect is statistically significant but may not be practically significant. With very large n, even tiny effects achieve small p-values. Evaluate practical importance by comparing the magnitude to the standard deviation of Y or to decision-relevant thresholds. Report both statistical significance and effect size.

### Q29. Given s_e = 3.5, what does this mean for prediction accuracy?
**Model answer:** Approximately 95% of observed Y values fall within ±2(3.5) = ±7 units of their fitted values. s_e is the typical residual magnitude and serves as a measure of how well the model fits individual observations.

### Q30. How do you interpret the slope of a log(Y) ~ X regression? Coefficient = 0.03.
**Model answer:** A one-unit increase in X is associated with approximately a 3% increase in Y (since 100 × 0.03 = 3%). More precisely, the percentage change is (e^0.03 − 1) × 100% = 3.05%. For small coefficients, the approximation is accurate.

---

## Part D: Assumptions and Diagnostics (Q31-37)

### Q31. List the five key OLS assumptions.
**Model answer:** (1) Linearity — the regression function is linear in parameters. (2) Random sampling / independence of observations. (3) Zero conditional mean — E(ε|X) = 0. (4) Homoscedasticity — Var(ε|X) = σ² constant. (5) Normality of errors (for exact small-sample inference). For multiple regression, add: no perfect multicollinearity.

### Q32. What is heteroscedasticity, how is it detected, and what are its consequences?
**Model answer:** Heteroscedasticity occurs when error variance varies with X, violating Var(ε|X) = σ². Detect via a fan-shaped residual-vs-fitted plot or a Breusch-Pagan / White test. Consequence: OLS estimates remain unbiased but standard errors are wrong, making t-tests and CIs invalid. Fix: use robust (White) standard errors.

### Q33. What is autocorrelation and how is it detected?
**Model answer:** Autocorrelation is correlation between successive error terms, common in time-series data. Detect using the Durbin-Watson statistic — values near 2 indicate no autocorrelation, below 2 indicate positive autocorrelation, above 2 indicate negative. Consequence: underestimated standard errors leading to spurious significance.

### Q34. Describe the consequence of omitted variable bias.
**Model answer:** If a relevant variable correlated with X is omitted, the OLS slope estimate is biased. The bias direction equals the product of (a) the true effect of the omitted variable on Y and (b) its correlation with X. Zero conditional mean is violated, so estimates are neither unbiased nor consistent.

### Q35. How do you check the normality assumption?
**Model answer:** Plot a histogram or QQ-plot of residuals. Apply a Shapiro-Wilk test for small samples or a Kolmogorov-Smirnov test for larger samples. For n ≥ 30, the Central Limit Theorem often makes the normality assumption inessential for inference on coefficients.

### Q36. What is multicollinearity and how is it detected?
**Model answer:** Multicollinearity is high correlation among predictors in multiple regression. Detect using Variance Inflation Factor (VIF) — values above 10 indicate serious multicollinearity. Consequences: inflated standard errors, unstable coefficient estimates, coefficients with counter-intuitive signs, but overall R² unaffected.

### Q37. What should you do if the linearity assumption is violated?
**Model answer:** Transform variables — try log(Y), √Y, or 1/Y on the response; add polynomial terms in X (e.g., X², X³); or apply a Box-Cox transformation. Alternatively, use non-linear regression or spline methods. Always re-check residual plots after transformation.

---

## Part E: Numerical Computation (Q38-43)

### Q38. Given Σ(x−x̄)(y−ȳ) = 240, Σ(x−x̄)² = 80, x̄ = 10, ȳ = 25, find β̂₀ and β̂₁.
**Model answer:** β̂₁ = 240/80 = 3. β̂₀ = 25 − 3(10) = −5. Regression equation: ŷ = −5 + 3x.

### Q39. With n = 30, β̂₁ = 2.5, SE(β̂₁) = 1.0, test H₀: β₁ = 0 at 5%.
**Model answer:** t = 2.5/1.0 = 2.5, df = 28. Critical value t_{0.025, 28} = 2.048. Since |2.5| > 2.048, reject H₀. The slope is statistically significant at the 5% level.

### Q40. Construct a 95% CI for β̂₁ = 4.2, SE = 1.5, n = 25.
**Model answer:** df = 23, t_{0.025, 23} = 2.069. CI = 4.2 ± 2.069(1.5) = 4.2 ± 3.10 = [1.10, 7.30]. Since 0 is not in the interval, conclude slope is significant at 5%.

### Q41. Given SSR = 150, SSE = 50, find R² and s_e if n = 20.
**Model answer:** SST = SSR + SSE = 200. R² = 150/200 = 0.75 (75% of variation explained). s_e = √(SSE/(n−2)) = √(50/18) = √2.78 = 1.67.

### Q42. Compute the F-statistic if R² = 0.6, n = 25.
**Model answer:** F = [R²/1] / [(1−R²)/(n−2)] = 0.6 / (0.4/23) = 0.6/0.01739 = 34.5. df = (1, 23). Compare to F_{0.05, 1, 23} ≈ 4.28. Reject H₀: model has significant overall explanatory power.

### Q43. If β̂₁ = 0.8 and s_Y = 12, s_X = 5, what is r?
**Model answer:** Using β̂₁ = r · (s_Y/s_X), we get r = β̂₁ · (s_X/s_Y) = 0.8 · (5/12) = 0.333. The correlation is approximately 0.33 — a moderate positive linear association.

---

## Part F: True/False with Justification (Q44-48)

### Q44. T/F: A high R² proves that X causes Y. Justify.
**Model answer:** FALSE. R² measures strength of linear association, not causation. High R² can arise from reverse causation, confounding variables, or coincidence. Establishing causation requires experimental manipulation (randomised controlled trials) or careful quasi-experimental designs (IV, RDD, DiD).

### Q45. T/F: If the 95% CI for β₁ includes zero, we accept H₀: β₁ = 0. Justify.
**Model answer:** FALSE (partially). We fail to reject H₀ — we never "accept" the null, because absence of evidence is not evidence of absence. The data are consistent with β₁ = 0 but also with other values in the interval. The correct conclusion is "insufficient evidence to reject H₀".

### Q46. T/F: OLS is always unbiased regardless of assumptions. Justify.
**Model answer:** FALSE. OLS is unbiased only if the zero conditional mean assumption E(ε|X) = 0 holds. If there is omitted variable bias, measurement error in X, or simultaneity (endogeneity), OLS is biased. Other assumptions (homoscedasticity, normality) affect efficiency and inference but not unbiasedness alone.

### Q47. T/F: Adding more predictors always increases R². Justify.
**Model answer:** TRUE. R² never decreases when adding predictors because OLS minimises SSE and adding variables can only reduce or maintain SSE. Use adjusted R² instead, which penalises additional predictors and can decrease if the added variable does not improve fit enough.

### Q48. T/F: If the p-value is 0.04, there is a 96% probability that H₀ is false. Justify.
**Model answer:** FALSE. The p-value is P(data or more extreme | H₀ true), not P(H₀ false | data). It is the probability of observing this result under the null hypothesis, not a probability statement about the hypothesis itself. This is a common misinterpretation.

---

## Part G: Application and Recommendations (Q49-50)

### Q49. A regression of sales on advertising gives ŷ = 150 + 4.2x, R² = 0.62, p < 0.01, n = 36. Write a 5-sentence management recommendation.
**Model answer:** (1) Advertising has a statistically significant positive effect on sales (β̂₁ = 4.2, p < 0.01). (2) Each additional £1,000 in advertising is associated with an average increase of £4.2 thousand in sales, holding other factors constant. (3) The model explains 62% of the variation in sales, indicating a moderately strong relationship. (4) I recommend increasing advertising spend, but note that 38% of sales variation is unexplained — other drivers (seasonality, competition, product mix) should be investigated. (5) Before scaling up, check for diminishing returns by examining whether the linear model holds across the full advertising range.

### Q50. A regression output shows β̂₁ = 12.5, p = 0.003, but the Durbin-Watson = 1.1 and a fan-shaped residual plot. How do you report this?
**Model answer:** The coefficient appears statistically significant (p = 0.003), but the reported standard errors are unreliable. The Durbin-Watson of 1.1 indicates positive autocorrelation and the fan-shaped residual plot indicates heteroscedasticity. Both violations invalidate the standard t-test. I recommend: (i) recomputing with Newey-West heteroscedasticity and autocorrelation-consistent (HAC) standard errors; (ii) investigating model misspecification — omitted trend or lag variables may cause both issues; (iii) not interpreting the current p-value at face value until the errors are corrected. State this caveat explicitly to the client.

---

**Exam tip:** In every written-answer question, structure your response as: (i) state the hypothesis or claim, (ii) quote the test statistic and p-value, (iii) state the decision (reject/fail to reject), (iv) interpret in the context of the problem with units, (v) note any caveats about assumptions.
