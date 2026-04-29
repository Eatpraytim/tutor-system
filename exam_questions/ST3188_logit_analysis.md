# ST3188 — Logit & Logistic Regression Analysis: 50 Exam Questions with Model Answers

---

## Part A: Fundamentals (Q1-10)

### Q1. What is logistic regression?
**Model answer:** A regression method for binary (or categorical) outcomes. Models the probability of an event as a function of predictors using the logistic function. Unlike OLS, outputs bounded [0, 1]. Uses maximum likelihood estimation.

### Q2. State the logistic regression model.
**Model answer:** log(p/(1−p)) = β₀ + β₁X₁ + ... + β_k X_k, where p = P(Y = 1). The left side is the "log-odds" (logit). Equivalently: p = 1/(1 + e^(−(β₀+β₁X₁+...))). The function is S-shaped, mapping linear combinations to probabilities.

### Q3. Define the logit function.
**Model answer:** logit(p) = log(p/(1−p)). Transforms probability (0,1) to log-odds (−∞, +∞), making linear modelling appropriate. Its inverse is the logistic (sigmoid) function.

### Q4. Why not use OLS on binary outcomes?
**Model answer:** (1) Predictions unbounded — can exceed [0,1]. (2) Heteroscedastic errors — variance depends on p. (3) Non-normal errors (binomial, not normal). (4) Linear relationship between X and Y inappropriate for probabilities. Linear Probability Model (LPM) sometimes used as approximation but inferior to logistic.

### Q5. Describe maximum likelihood estimation (MLE) in logistic regression.
**Model answer:** Choose β to maximise likelihood of observed data. Log-likelihood: L(β) = Σ [y_i log(p_i) + (1−y_i) log(1−p_i)], where p_i depends on β and X_i. Iterative estimation (Newton-Raphson, Fisher scoring). Produces consistent, asymptotically normal estimates.

### Q6. Interpret a logistic regression coefficient.
**Model answer:** A one-unit increase in X_j is associated with a β_j increase in log-odds of Y = 1, holding other variables constant. Exponentiated: e^β_j = odds ratio. Example: β = 0.7 → e^0.7 = 2.01, odds double with 1-unit increase in X.

### Q7. Define odds ratio.
**Model answer:** Ratio of odds of event across two conditions: OR = odds_1/odds_2 = (p₁/(1−p₁))/(p₂/(1−p₂)). In logistic: OR = e^β for unit change in X. OR = 1: no effect. OR > 1: positive. OR < 1: negative. Key output of logistic regression.

### Q8. Compare odds ratio and relative risk.
**Model answer:** Odds ratio: ratio of odds. Relative risk: ratio of probabilities = p₁/p₂. For rare outcomes (p < 10%), OR ≈ RR. For common outcomes, they diverge substantially: OR exaggerates. Both report effect; choice depends on study design (case-control usually OR).

### Q9. What are the assumptions of logistic regression?
**Model answer:** (1) Binary dependent variable (multinomial/ordinal are extensions). (2) Independence of observations. (3) Linearity of log-odds in continuous predictors (test: Box-Tidwell). (4) No perfect multicollinearity. (5) Large sample — rule of thumb: 10 events per predictor. (6) No severe outliers.

### Q10. Compare logistic regression and discriminant analysis.
**Model answer:** LR: no distributional assumption on X; more flexible; widely applicable. DA: assumes multivariate normal predictors with equal covariance; more efficient when assumptions hold. LR preferred when assumptions uncertain, categorical predictors present, or interpretation of probabilities desired.

---

## Part B: Model Building (Q11-20)

### Q11. What is the Wald test?
**Model answer:** Tests H₀: β_j = 0 for individual coefficients. z = β̂_j / SE(β̂_j), follows standard normal (or z² follows chi-squared with df=1). p-value from normal distribution. Standard in SPSS output. Caveat: unreliable for small samples or large coefficients.

### Q12. What is the likelihood ratio (LR) test?
**Model answer:** Compares nested models. LR = −2[log L_restricted − log L_full] ~ χ²(df = difference in parameters). Tests multiple coefficients simultaneously. More reliable than Wald for small samples. Used to compare full vs reduced models.

### Q13. State the likelihood ratio test for overall significance.
**Model answer:** LR = −2(log L_null − log L_full). Compares null model (intercept only) to full model. Under H₀: all slopes zero, LR ~ χ²(k). Significant result indicates model explains data better than constant probability. Analog to overall F-test in OLS.

### Q14. What are pseudo R² measures?
**Model answer:** Analogs to R² in logistic regression, but don't have same interpretation. (1) Cox-Snell R² = 1 − (L_null/L_full)^(2/n). Upper bound < 1. (2) Nagelkerke R² = Cox-Snell / max. Bound [0,1]. (3) McFadden R² = 1 − log L_full/log L_null. Each useful for comparison. Interpret as "relative improvement in likelihood".

### Q15. What is the Hosmer-Lemeshow test?
**Model answer:** Tests goodness-of-fit. Groups observations into 10 deciles by predicted probability. Compares observed vs expected events per decile via chi-squared. H₀: model fits well. p > 0.05 = good fit. Caveat: sensitive to sample size; useful but not definitive.

### Q16. Describe classification accuracy for logistic regression.
**Model answer:** At a threshold (default 0.5): classify predicted probability > 0.5 as event. Compute: sensitivity (true positive rate), specificity (true negative rate), accuracy, precision (positive predictive value). Use confusion matrix and ROC curve for comprehensive evaluation.

### Q17. What is the ROC curve?
**Model answer:** Receiver Operating Characteristic: plots sensitivity vs (1 − specificity) across all possible thresholds. AUC (Area Under Curve): 0.5 = random, 1.0 = perfect. AUC > 0.7 acceptable, > 0.8 good, > 0.9 excellent. Robust evaluation that doesn't depend on specific threshold.

### Q18. Explain the AUC metric.
**Model answer:** AUC = probability that a randomly chosen event case has higher predicted probability than a randomly chosen non-event case. Equivalent to rank-based measure. Threshold-free evaluation. Preferred over accuracy when class balance is important or no specific threshold is prescribed.

### Q19. What is the optimal cutpoint for classification?
**Model answer:** Depends on goals. (1) 0.5 by default. (2) Youden's J: maximise sensitivity + specificity − 1. (3) Cost-based: minimise expected cost given class imbalance and misclassification costs. (4) Maximise F1 (harmonic mean of precision and recall). Often, clinical/business context dictates.

### Q20. Describe stepwise logistic regression.
**Model answer:** Adds/removes predictors based on statistical criteria (Wald or LR test). Forward/backward/stepwise algorithms. Issues: inflated Type I error, unstable variable selection. Alternatives: LASSO regularisation, cross-validation for variable importance, theory-driven selection. Use cautiously and report all selected models.

---

## Part C: Interpretation and Effect Sizes (Q21-30)

### Q21. Given β = 0.5 for age, interpret.
**Model answer:** A 1-year increase in age increases log-odds of the event by 0.5, holding other variables constant. Odds ratio: e^0.5 = 1.65. Odds of event increase by 65% per year of age. For 10-year increase: OR = e^(10·0.5) = 148 — log-odds don't scale linearly in probability terms.

### Q22. Interpret odds ratio = 2.5 for gender (male = 1 vs female = 0).
**Model answer:** Males have 2.5 times the odds of the event compared to females, holding other variables constant. Equivalently: P(event|male)/(1−P(event|male)) = 2.5 × P(event|female)/(1−P(event|female)). Does NOT mean males have 2.5× the probability.

### Q23. For a continuous X with coefficient 0.02, interpret.
**Model answer:** Each 1-unit increase in X increases log-odds by 0.02. OR = e^0.02 = 1.02. Odds increase by 2% per unit. For small coefficients, β ≈ (OR − 1) — percentage change in odds. For 10-unit increase: OR = e^0.2 = 1.22, or 22% increase.

### Q24. Given predicted probability 0.70, interpret.
**Model answer:** The model estimates 70% chance of the event for this observation with these predictor values. Calibration check: among observations with predicted probability ~0.70, does approximately 70% actually experience the event? If yes, model is well-calibrated; if no, recalibration needed.

### Q25. Compute odds ratio's 95% CI given β = 0.8, SE = 0.3.
**Model answer:** 95% CI for β = 0.8 ± 1.96(0.3) = [0.21, 1.39]. Exponentiate: 95% CI for OR = [e^0.21, e^1.39] = [1.23, 4.01]. Since 1 is not in the interval, OR is statistically significantly different from 1.

### Q26. Model has Nagelkerke R² = 0.35. Interpret.
**Model answer:** Moderate model fit. Approximately 35% improvement in likelihood relative to null model (adjusted). Generally: > 0.20 acceptable, > 0.40 substantial. Log-odds don't decompose variance like linear models, so R² analogs are rough guides. Report alongside classification metrics and calibration.

### Q27. Hosmer-Lemeshow p = 0.85. Interpret.
**Model answer:** Fail to reject H₀: model fits the data. p > 0.05 indicates acceptable fit between predicted and observed frequencies across risk groups. Note: Hosmer-Lemeshow has low power for small samples and may fail to detect misfit. Complement with other checks (residual patterns, ROC curve).

### Q28. Classification accuracy = 85%; baseline (always predicting majority class) = 80%. Evaluate.
**Model answer:** Only 5 percentage-point improvement over baseline. Model's added value is modest. If majority class is "no event" at 80%, 85% accuracy may mean few events correctly predicted. Check sensitivity (recall for events): if very low, model fails at its primary purpose despite high accuracy. Report sensitivity/specificity and AUC.

### Q29. A model has AUC = 0.65. Is it useful?
**Model answer:** Marginal — AUC 0.5 is random, 0.65 is weak. May still be useful if: (1) No better alternative exists. (2) Combined with other decision rules. (3) Calibration is good (probabilities are meaningful even if ranking is weak). (4) Cost of misclassification is low. For critical decisions, improve model (more features, better methods) before deployment.

### Q30. Interpret a logistic regression where β_{income} = −0.001 and income ranges 20,000 to 150,000.
**Model answer:** Tiny per-unit effect: OR = e^(−0.001) = 0.999. Per £1: 0.1% decrease in odds. Per £10,000: OR = e^(−10) ≈ 0 — but that's wrong; linear extrapolation exceeds model's applicability. For meaningful interpretation: OR per £10,000 = e^(−0.001 × 10000) = e^(−10) ≈ 0. So large income increases associated with large decreases in odds. Scale coefficients appropriately.

---

## Part D: Multinomial and Ordinal Logistic (Q31-40)

### Q31. What is multinomial logistic regression?
**Model answer:** Extension for categorical outcomes with more than 2 unordered levels (e.g., product A, B, C). Estimates k−1 equations comparing each category to a reference. Probabilities sum to 1. More complex interpretation — each β measures effect on log-odds of that category vs reference.

### Q32. State the multinomial logit form.
**Model answer:** log(P(Y=j)/P(Y=ref)) = β_0j + β_1j·X₁ + ... for j = 1,...,J−1 (ref is the base). Probabilities: P(Y=j) = exp(linear combo)/Σ exp(all combos). Each equation has its own coefficients; total parameters = (J−1) × (k+1).

### Q33. What is ordinal logistic regression?
**Model answer:** For ordered categorical outcomes (e.g., low, medium, high). Assumes proportional odds: effect of X on log-odds of exceeding any cutpoint is constant. Fewer parameters than multinomial. Test proportional odds (PO) assumption with Brant test.

### Q34. What is the proportional odds assumption?
**Model answer:** log(P(Y ≤ j)/P(Y > j)) = α_j − β'X, with different intercepts (α_j) per category but same slopes. Assumes effect of X is same across category thresholds. If violated, use: (1) generalised ordinal logit (different slopes per threshold), (2) multinomial (ignores order), (3) simplified groupings.

### Q35. How to test proportional odds assumption?
**Model answer:** (1) Brant test (Wald-type): tests equality of coefficients across equations. (2) Score test. (3) Graphical check: cumulative plots of logits for each cutpoint should be parallel. (4) Compare ordinal vs generalised ordinal models. p < 0.05 in Brant → PO violated.

### Q36. Interpret a multinomial logit coefficient.
**Model answer:** β_{jk} for category j (vs reference) and predictor k: a 1-unit increase in X_k changes log-odds of being in category j vs reference by β_{jk}, holding other variables constant. Exponentiate: OR for category j vs reference. Must interpret each equation separately.

### Q37. Describe the relative risk ratio (RRR) in multinomial logit.
**Model answer:** Synonym for exponentiated coefficient in multinomial logit. RRR > 1: predictor increases odds of that category relative to reference. Interpretation same as odds ratio but remember: comparing one specific category to a specific reference category.

### Q38. State the independence of irrelevant alternatives (IIA) assumption in multinomial logit.
**Model answer:** Odds of choosing A over B unaffected by availability of C. Example: if odds of red vs blue car = 2:1, adding yellow shouldn't change this ratio. Violated when alternatives are similar (red vs red-imitation). Test: Hausman-McFadden. Remedy: nested logit or mixed logit models.

### Q39. Compare multinomial logit and probit models.
**Model answer:** Logit: uses logistic link (S-shape); common in academic and business. Probit: uses cumulative normal link. Both produce similar fits; differ by scaling factor ~π/√3. Logit more interpretable (odds ratios); probit theoretically grounded in latent normal utility. Software default often logit.

### Q40. When would you use conditional logit?
**Model answer:** When choices vary across observations. Each observation faces different alternatives (e.g., products available), and attributes of alternatives (not individuals) drive choice. Used in discrete choice modelling (transport, purchase). Relies on alternative-specific attributes, not just decision-maker characteristics.

---

## Part E: True/False and Interpretation (Q41-45)

### Q41. T/F: Logistic regression can be used for continuous Y.
**Model answer:** FALSE. Logistic regression is for binary or categorical Y. For continuous Y, use OLS or other regression methods. For Y constrained to [0, 1] (proportions), use fractional logit or beta regression, which relate to logistic but are designed for proportions.

### Q42. T/F: An odds ratio of 1.5 means the probability increases 50%.
**Model answer:** FALSE. OR = 1.5 means odds increase 50%, not probability. Probability change depends on baseline. Example: if baseline p = 0.1, OR = 1.5 → odds from 0.111 to 0.167, p = 0.143. Probability increased 4.3 pp, or 43% relatively. Be precise about odds vs probability.

### Q43. T/F: A significant logistic regression implies high predictive accuracy.
**Model answer:** FALSE. Statistical significance (Wald/LR test) measures if coefficient differs from zero. Predictive accuracy (classification rates, AUC) measures how well the model predicts new cases. Both can be high, or only one can be. Evaluate both independently.

### Q44. T/F: Logistic regression coefficients have direct probability interpretation.
**Model answer:** FALSE. Coefficients are in log-odds units. Direct probability interpretation requires the full model (p = 1/(1 + e^(−(β₀+β₁X₁+...)))). Report probability predictions for specific X values; don't directly translate coefficients to probability changes.

### Q45. T/F: Multicollinearity biases logistic regression estimates.
**Model answer:** FALSE. Multicollinearity inflates standard errors (reducing precision) but doesn't bias coefficients. Estimates remain consistent; they're just less reliably estimated. Check VIF; address if VIF > 10 by removing or combining variables, or using regularisation.

---

## Part F: Application (Q46-50)

### Q46. A credit scoring logistic regression predicts default. OR for 1-year increase in age is 0.95. Interpret.
**Model answer:** Each additional year of age is associated with 5% lower odds of default (OR = 0.95), holding income, debt, and other predictors constant. Over 10 years: OR = 0.95^10 = 0.60 — 40% lower odds. Indicates older borrowers are less risky on average. Include alongside other predictors in scoring; monitor for changes over time.

### Q47. Design a logistic regression study predicting customer churn.
**Model answer:** (1) Outcome: churn in next 6 months (binary). (2) Predictors: tenure, usage, satisfaction score, customer service interactions, plan type, demographics. (3) Sample: historical customers with known churn outcome. (4) Pre-process: handle missing data, encode categoricals, check multicollinearity (VIF). (5) Fit model; examine Wald tests, Hosmer-Lemeshow, AUC on validation set. (6) Interpret key predictors via odds ratios. (7) Identify at-risk customers for retention outreach. (8) Monitor model performance over time — re-fit regularly.

### Q48. Your model predicts disease from lab tests. Sensitivity = 95%, specificity = 70%. Evaluate.
**Model answer:** Excellent sensitivity — catches most diseased cases (5% missed). Modest specificity — 30% of healthy flagged as positive. Appropriate if missing disease is costly (fatal conditions); overkill if false positives cause panic/cost. Report positive and negative predictive values (depend on prevalence). Adjust threshold if the trade-off isn't optimal — lower threshold raises sensitivity at cost of specificity.

### Q49. Class imbalance: 99% non-events, 1% events. How do you build a logistic regression?
**Model answer:** (1) Standard logistic will predict mostly non-events — accuracy ~99% trivially. (2) Address imbalance: (a) Weighted likelihood — up-weight event class. (b) SMOTE: synthetic minority oversampling. (c) Sampling: under-sample majority or over-sample minority. (d) Evaluate with AUC, precision-recall curve, F1 — not accuracy. (3) Adjust threshold: lower threshold for detecting events. (4) Consider alternative models if imbalance is extreme (XGBoost, anomaly detection).

### Q50. Critique: "The logistic regression showed income is a significant predictor of purchasing, so raising incomes will increase purchasing."
**Model answer:** Critique: (1) Association ≠ causation. Observational data with income as predictor doesn't establish that raising income causes more purchasing. (2) Reverse causation: maybe people who purchase have higher income (confounded with wealth, success). (3) Confounding: education, age, occupation may drive both income and purchasing. (4) Policy implication invalid: raising incomes may not produce predicted purchasing increase if mechanism is different. Causal claims require experimental or quasi-experimental design (RCT, IV, natural experiment). Report finding as "higher incomes are associated with higher purchasing", leave causal claims for appropriate designs.

---

**Exam tip:** For logistic regression questions, always: (1) state the outcome variable clearly (binary, multinomial, ordinal), (2) interpret coefficients in log-odds and exponentiate to odds ratios, (3) check assumptions (linearity of logits, multicollinearity), (4) evaluate model with Hosmer-Lemeshow AND classification metrics AND AUC, (5) discuss sample size requirements (10+ events per predictor), (6) address class imbalance if present.
