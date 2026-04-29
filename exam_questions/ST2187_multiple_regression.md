# ST2187 — Multiple Regression: 50 Exam Questions with Model Answers

---

## Part A: Definitions and Conceptual (Q1-10)

### Q1. State the multiple linear regression model in general form.
**Model answer:** Yᵢ = β₀ + β₁X₁ᵢ + β₂X₂ᵢ + ... + βₖXₖᵢ + εᵢ where Y is the response, X₁,...,Xₖ are k predictors, β₀ is the intercept, β₁,...,βₖ are partial slope coefficients, and εᵢ is the error term with E(εᵢ|X) = 0.

### Q2. What does it mean to interpret a coefficient "holding all else constant"?
**Model answer:** It means the coefficient βⱼ represents the expected change in Y for a one-unit increase in Xⱼ, assuming all other predictors in the model remain fixed. This isolates the partial effect of Xⱼ, controlling for the influence of the other variables. Omitting this qualifier loses marks in exams.

### Q3. What is the difference between R² and adjusted R²?
**Model answer:** R² = 1 − SSE/SST measures the proportion of variance explained but always increases when adding predictors. Adjusted R² = 1 − [(1−R²)(n−1)/(n−k−1)] penalises additional predictors by adjusting for degrees of freedom. Adjusted R² can decrease if a predictor does not improve the model enough to offset the df cost.

### Q4. Define multicollinearity and why it matters.
**Model answer:** Multicollinearity is high linear correlation among predictors. It inflates standard errors, making coefficients statistically insignificant despite a significant overall model, and can cause unstable and sign-reversed estimates. It does not bias estimates, only their precision.

### Q5. State the F-test hypotheses for overall model significance.
**Model answer:** H₀: β₁ = β₂ = ... = βₖ = 0 (all slopes are zero; the model has no explanatory power). H₁: at least one βⱼ ≠ 0. Rejecting H₀ means the model as a whole is statistically significant.

### Q6. Why is it possible for the F-test to be significant while no individual t-test is?
**Model answer:** This happens under severe multicollinearity. The predictors jointly explain Y (significant F) but each individual predictor's contribution, holding others fixed, is uncertain (insignificant t). The variance inflation from collinearity makes individual effects hard to isolate.

### Q7. Explain the Variance Inflation Factor (VIF).
**Model answer:** VIFⱼ = 1/(1−R²ⱼ) where R²ⱼ is from regressing Xⱼ on all other predictors. VIF = 1 means no collinearity; VIF > 5 indicates concern; VIF > 10 indicates serious multicollinearity. High VIF inflates SE(β̂ⱼ) by √VIF.

### Q8. What is a dummy variable and why is one category omitted?
**Model answer:** A dummy variable takes value 1 for a category and 0 otherwise. For a categorical variable with g categories, use g−1 dummies to avoid perfect multicollinearity (the "dummy variable trap"). The omitted category becomes the reference group against which others are compared.

### Q9. Explain an interaction term in regression.
**Model answer:** An interaction term X₁·X₂ allows the effect of X₁ on Y to depend on the value of X₂. The model becomes Y = β₀ + β₁X₁ + β₂X₂ + β₃(X₁X₂) + ε. The slope of X₁ is (β₁ + β₃X₂), varying with X₂ instead of being constant.

### Q10. What is model specification error?
**Model answer:** Model specification error occurs when the model is mis-specified — wrong functional form, omitted relevant variables, or included irrelevant ones. Omitting relevant variables biases the remaining coefficients (OVB). Including irrelevant ones loses efficiency but does not bias. Incorrect functional form biases all estimates.

---

## Part B: Formula Recall (Q11-17)

### Q11. Write the matrix form of OLS estimator.
**Model answer:** β̂ = (X'X)⁻¹X'Y where X is the n×(k+1) design matrix (including a column of 1s for the intercept) and Y is the n×1 response vector. This gives all coefficient estimates simultaneously.

### Q12. State the formula for adjusted R².
**Model answer:** Adjusted R² = 1 − [(1−R²) · (n−1)/(n−k−1)] where n is sample size and k is the number of predictors. It equals R² when k = 0 and is always less than R² for k ≥ 1.

### Q13. State the F-statistic for overall model significance.
**Model answer:** F = (SSR/k) / (SSE/(n−k−1)) = (R²/k) / ((1−R²)/(n−k−1)) with df = (k, n−k−1). Under H₀ (all slopes zero), F follows an F-distribution.

### Q14. State the formula for a nested F-test (comparing restricted vs unrestricted models).
**Model answer:** F = [(SSE_R − SSE_U)/q] / [SSE_U/(n−k−1)] where SSE_R is restricted (fewer predictors), SSE_U is unrestricted (more predictors), q is number of restrictions, and df = (q, n−k−1).

### Q15. Write the t-statistic for an individual slope βⱼ.
**Model answer:** tⱼ = β̂ⱼ / SE(β̂ⱼ) with df = n−k−1. Tests H₀: βⱼ = 0 vs H₁: βⱼ ≠ 0 (two-sided), controlling for all other predictors.

### Q16. State the formula for VIF.
**Model answer:** VIFⱼ = 1/(1 − R²ⱼ) where R²ⱼ is the R² from regressing Xⱼ on all other predictors. Also equivalently SE(β̂ⱼ) = [s_e · √VIFⱼ] / [s_{Xⱼ} · √(n−1)].

### Q17. State the formula for a CI of a coefficient.
**Model answer:** β̂ⱼ ± t_{α/2, n−k−1} · SE(β̂ⱼ). For a 95% CI with large n, t_{0.025} ≈ 1.96.

---

## Part C: Interpretation Questions (Q18-30)

### Q18. Given ŷ = 20 + 3.5x₁ − 2.1x₂ + 0.8x₃ with x₁ = hours worked, x₂ = age, x₃ = experience, interpret β̂₁.
**Model answer:** Each additional hour worked is associated with an expected increase of 3.5 units in Y, holding age and experience constant. Always mention the units, "expected/on average", and the "holding all else constant" qualifier.

### Q19. The coefficient on X₂ is −2.1 with p = 0.04. Interpret.
**Model answer:** Holding all other predictors constant, a one-unit increase in age is associated with an expected decrease of 2.1 units in Y. The effect is statistically significant at the 5% level (p = 0.04 < 0.05). We reject H₀: β₂ = 0.

### Q20. Dummy variable D = 1 for "female" has coefficient −5,200 in a salary regression. Interpret.
**Model answer:** On average, females earn £5,200 less than males with equivalent values of all other predictors in the model. Males are the reference category. Statistical significance must be checked — if significant, this suggests an unexplained gender pay gap after controlling for observable factors.

### Q21. Interpret R² = 0.82 and adjusted R² = 0.79 for a model with 4 predictors, n = 40.
**Model answer:** The model explains 82% of the variation in Y. After penalising for the number of predictors, adjusted R² is 79%, suggesting that the predictors genuinely add explanatory power (the gap is modest). The model has strong explanatory fit.

### Q22. In model ŷ = β₀ + β₁·age + β₂·age², β₁ = 5 and β₂ = −0.1. Interpret the relationship.
**Model answer:** The relationship between age and Y is quadratic (inverted U-shape given β₂ < 0). The marginal effect of age on Y is ∂Y/∂age = 5 − 0.2·age. Y increases with age up to age = 25 (= 5/0.2), then decreases. Always test individual coefficients and joint significance.

### Q23. Given interaction term coefficient β(X₁·D) = 3.0 where D is a gender dummy, interpret.
**Model answer:** The effect of X₁ on Y is 3.0 units larger for the group where D = 1 compared to the reference group. If X₁ is years of experience and D = 1 for female, the return to experience is 3.0 units higher for females.

### Q24. F-statistic = 45.2, p < 0.001. Interpret.
**Model answer:** The overall model is highly statistically significant (p < 0.001). At least one predictor has a non-zero effect on Y. The joint explanatory power of the predictors is significantly greater than zero; we reject H₀: all slopes = 0.

### Q25. In a log-wage regression, β(education) = 0.12. Interpret.
**Model answer:** Each additional year of education is associated with approximately a 12% increase in wages, holding other factors constant. More precisely, the exact percentage change is (e^0.12 − 1) × 100% = 12.75%, but for small coefficients the approximation β × 100% is sufficient.

### Q26. Adjusted R² decreased from 0.65 to 0.63 after adding a predictor. What does this mean?
**Model answer:** The new predictor did not add enough explanatory power to offset the cost of an additional parameter. Although R² increased (mechanically), adjusted R² decreased, suggesting the new variable is not useful and may introduce noise. Consider removing it.

### Q27. Interpret VIF = 25 for predictor X₃.
**Model answer:** Serious multicollinearity — X₃ is highly correlated with other predictors. The variance of β̂₃ is inflated 25× compared to a model with no collinearity. SE(β̂₃) is √25 = 5× larger. Consider removing X₃, combining with another variable, or using ridge regression.

### Q28. Coefficient of 0.85 on a log-transformed X (log-level). Interpret.
**Model answer:** A 1% increase in X is associated with an increase of 0.85/100 = 0.0085 units in Y, holding other factors constant. This is a semi-elasticity — small percentage changes in X yield the corresponding absolute change in Y.

### Q29. In log(Y) = β₀ + β₁log(X₁) + ..., β̂₁ = 0.4. Interpret.
**Model answer:** This is an elasticity. A 1% increase in X₁ is associated with a 0.4% increase in Y, holding other factors constant. Log-log models express effects in terms of percentage changes, making coefficients unit-free.

### Q30. All individual t-tests are insignificant but F-test is significant. Diagnose.
**Model answer:** Classic sign of multicollinearity. Predictors are jointly informative but redundant individually. Check VIFs, consider dropping one of a highly correlated pair, combining variables into an index, or using principal component regression. Report the multicollinearity finding with caveats.

---

## Part D: Assumptions and Diagnostics (Q31-37)

### Q31. List the assumptions of multiple linear regression.
**Model answer:** (1) Linearity in parameters. (2) Random sampling / independence. (3) No perfect multicollinearity. (4) Zero conditional mean E(ε|X₁,...,Xₖ) = 0. (5) Homoscedasticity Var(ε|X) = σ². (6) Normality of errors (for exact small-sample inference).

### Q32. How do you detect non-linearity in multiple regression?
**Model answer:** Plot residuals vs each predictor and vs fitted values. Patterns (U-shape, curvature) indicate non-linearity. Use the Ramsey RESET test formally. Remedies: add polynomial terms, log transformations, or use non-parametric methods.

### Q33. What does the BLUE property mean in multiple regression?
**Model answer:** Under Gauss-Markov assumptions, OLS estimators are Best Linear Unbiased Estimators — among all linear unbiased estimators, they have minimum variance. Adding the normality assumption makes OLS maximum likelihood and gives exact t and F distributions for inference.

### Q34. How do you detect outliers and influential observations?
**Model answer:** (i) Standardised residuals > |3| indicate outliers in Y. (ii) Leverage > 2(k+1)/n indicates unusual X values. (iii) Cook's Distance > 4/n indicates influential points that change the fit substantially. (iv) DFFITS and DFBETAS quantify individual influence. Always investigate outliers — don't simply drop them.

### Q35. What is endogeneity and what are its three sources?
**Model answer:** Endogeneity is correlation between a predictor and the error term: Cov(Xⱼ, ε) ≠ 0, violating E(ε|X) = 0. Three sources: (1) Omitted variable bias, (2) Measurement error in X, (3) Simultaneity / reverse causality. Consequence: OLS is biased and inconsistent. Remedy: instrumental variables.

### Q36. State the consequence of heteroscedasticity in multiple regression.
**Model answer:** OLS coefficient estimates remain unbiased and consistent, but standard errors are incorrect. Conventional t-tests, F-tests, and CIs are invalid. Use heteroscedasticity-robust (White) standard errors. Alternatively, apply weighted least squares if the form of heteroscedasticity is known.

### Q37. How do you test nested models?
**Model answer:** Use the F-test for nested models: F = [(SSE_R − SSE_U)/q] / [SSE_U/(n−k−1)] where the restricted model imposes q restrictions on the unrestricted one. df = (q, n−k−1). Reject H₀ if F exceeds the critical value, indicating the restrictions are not supported.

---

## Part E: Numerical Computation (Q38-43)

### Q38. Compute adjusted R² given R² = 0.70, n = 50, k = 5.
**Model answer:** Adjusted R² = 1 − (1−0.70)(50−1)/(50−5−1) = 1 − (0.30)(49)/44 = 1 − 14.7/44 = 1 − 0.334 = 0.666. The adjusted value 0.666 is meaningfully lower than R² = 0.70 due to the 5 predictor penalty.

### Q39. Test overall significance given R² = 0.55, n = 30, k = 4.
**Model answer:** F = (R²/k)/((1−R²)/(n−k−1)) = (0.55/4)/((0.45)/25) = 0.1375/0.018 = 7.64. df = (4, 25). Critical value F_{0.05, 4, 25} ≈ 2.76. Since 7.64 > 2.76, reject H₀. Model is highly significant.

### Q40. Given β̂₁ = 3.2, SE = 1.5, n = 30, k = 3, construct 95% CI.
**Model answer:** df = 30 − 3 − 1 = 26. t_{0.025, 26} = 2.056. CI = 3.2 ± 2.056(1.5) = 3.2 ± 3.08 = [0.12, 6.28]. Since zero is not included, coefficient is significant at 5%.

### Q41. Conduct a nested F-test: SSE_R = 800 (k=2), SSE_U = 600 (k=5), n = 40.
**Model answer:** q = 3 restrictions. F = [(800−600)/3] / [600/(40−5−1)] = (66.67)/(17.65) = 3.78. df = (3, 34). Critical F_{0.05, 3, 34} ≈ 2.88. Since 3.78 > 2.88, reject H₀: the three additional predictors jointly significantly improve the model.

### Q42. Compute VIF if R²ⱼ from regressing Xⱼ on other predictors = 0.85.
**Model answer:** VIFⱼ = 1/(1−0.85) = 1/0.15 = 6.67. Standard error of β̂ⱼ is √6.67 ≈ 2.58× larger than it would be without multicollinearity. This is moderate concern (above 5 but below 10 threshold).

### Q43. Given TSS = 1000, SSR = 700, n = 25, k = 3. Compute R², adjusted R², and s_e.
**Model answer:** SSE = 300. R² = 700/1000 = 0.70. Adjusted R² = 1 − (0.30)(24)/21 = 1 − 0.343 = 0.657. s_e = √(SSE/(n−k−1)) = √(300/21) = √14.29 = 3.78.

---

## Part F: True/False with Justification (Q44-48)

### Q44. T/F: Adding an irrelevant predictor biases all other coefficients.
**Model answer:** FALSE. Adding an irrelevant variable does not bias remaining coefficients; it only reduces efficiency (increases SEs). However, omitting a relevant correlated variable does bias remaining coefficients. Inclusion errors are "cheaper" than omission errors.

### Q45. T/F: In a multiple regression, β̂₁ equals the Pearson correlation r(X₁, Y).
**Model answer:** FALSE. β̂₁ is the partial slope controlling for other predictors; r is the raw pairwise association. In simple regression β̂₁ = r · s_Y/s_X. In multiple regression, β̂₁ typically differs from the raw correlation due to the effect of other predictors.

### Q46. T/F: The sign of a coefficient can change when you add another predictor.
**Model answer:** TRUE. This is Simpson's paradox or omitted variable bias in action. Adding a confounding variable can reverse the apparent effect direction. Example: wage vs education may show positive effect alone but negative effect after controlling for experience.

### Q47. T/F: Multicollinearity biases OLS coefficients.
**Model answer:** FALSE. Multicollinearity inflates standard errors (reducing precision) but does not bias OLS estimates. Coefficients remain unbiased and consistent; they are just less reliably estimated. The F-test of overall fit is unaffected.

### Q48. T/F: In a model with a quadratic term X², you should interpret β₁ alone to describe the effect of X.
**Model answer:** FALSE. With X² in the model, the total effect of X on Y is ∂Y/∂X = β₁ + 2β₂X, which depends on the value of X. Interpret both coefficients together and compute marginal effects at meaningful values of X (mean, median, policy-relevant points).

---

## Part G: Application and Recommendations (Q49-50)

### Q49. A regression of house price on size (x₁), bedrooms (x₂), location dummy (D = 1 for city centre) gives: price = 50,000 + 150·size + 8,000·x₂ + 40,000·D. R² = 0.78, all p < 0.01, n = 150. Write a business summary.
**Model answer:** (1) The model explains 78% of variation in house prices and is highly significant (all coefficients p < 0.01). (2) Each additional square foot adds £150 to the expected price; each additional bedroom adds £8,000, holding other features constant. (3) City-centre properties command an average £40,000 premium over non-centre ones with identical size and bedrooms. (4) Size is the dominant driver — a 100 sq ft increase (£15,000) exceeds adding a bedroom (£8,000). (5) Recommendation: prioritise listings by location and size; verify assumptions (no heteroscedasticity, no omitted features like age or condition) before using for pricing decisions.

### Q50. Your regression has R² = 0.95 but VIF > 20 for two predictors. How do you report this?
**Model answer:** The model fits in-sample extremely well (R² = 0.95) but suffers severe multicollinearity (VIF > 20 on two predictors). While overall predictions may be accurate, the individual coefficient estimates are unreliable — their signs and magnitudes can shift substantially with small data changes. Do not interpret individual coefficients at face value. Recommend: (i) combining the collinear predictors into an index, (ii) dropping one of each collinear pair after domain justification, or (iii) using ridge regression if predictive accuracy matters more than interpretation. Report R², adjusted R², and the multicollinearity caveat prominently.

---

**Exam tip:** In multiple regression answers, always: (1) state the model in full notation, (2) report F for overall significance, (3) report t-statistic, p-value, and CI for the specific coefficient of interest, (4) interpret with units and "holding all else constant", (5) discuss assumption caveats (especially multicollinearity and heteroscedasticity), (6) provide a business recommendation where asked.
