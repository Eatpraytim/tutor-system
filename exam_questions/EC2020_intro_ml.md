# EC2020 — Multiple Regression & Intro to Machine Learning: 50 Exam Questions with Model Answers

---

## Part A: Multiple Regression Review (Q1-10)

### Q1. State the multiple linear regression model.
**Model answer:** Y_i = β₀ + β₁X_{1i} + β₂X_{2i} + ... + β_k X_{ki} + u_i, for i = 1, ..., n. Each β_j is the partial (ceteris paribus) effect of X_j on Y. In matrix form: y = Xβ + u, where X is n × (k+1) including intercept column.

### Q2. Derive the OLS estimator in matrix form.
**Model answer:** Minimise SSR = (y − Xβ)'(y − Xβ). FOC: ∂SSR/∂β = −2X'(y − Xβ) = 0 → X'y = X'Xβ → β̂ = (X'X)⁻¹X'y. Requires (X'X) invertible (no perfect multicollinearity).

### Q3. Prove OLS unbiasedness under Gauss-Markov assumptions.
**Model answer:** β̂ = (X'X)⁻¹X'(Xβ + u) = β + (X'X)⁻¹X'u. Taking expectations conditional on X: E(β̂|X) = β + (X'X)⁻¹X'E(u|X) = β (by MLR.4). Unconditional: E(β̂) = β by iterated expectations.

### Q4. State and interpret the Gauss-Markov theorem.
**Model answer:** Under MLR.1-MLR.5 (linearity, random sampling, no perfect multicollinearity, zero conditional mean, homoscedasticity), OLS is BLUE — the Best Linear Unbiased Estimator. Among all linear unbiased estimators, OLS has minimum variance. No other linear estimator outperforms OLS in this sense.

### Q5. Explain what "holding all else constant" means in multiple regression.
**Model answer:** β̂_j measures the expected change in Y for a one-unit increase in X_j, assuming all other X's are held fixed. By the Frisch-Waugh-Lovell theorem, β̂_j equals the coefficient from regressing Y on the part of X_j orthogonal to other predictors. Not a counterfactual claim unless assumptions (especially no OVB) hold.

### Q6. State the formula for σ̂² in MLR.
**Model answer:** σ̂² = SSR/(n − k − 1), where SSR = Σû²_i. The divisor n − k − 1 is the degrees of freedom, accounting for the k + 1 estimated parameters. Used in Var(β̂) = σ²(X'X)⁻¹ for standard errors.

### Q7. Describe the F-test for overall model significance.
**Model answer:** H₀: β₁ = β₂ = ... = β_k = 0 (all slopes zero) vs H₁: at least one ≠ 0. F = (R²/k) / ((1−R²)/(n−k−1)) ~ F(k, n−k−1). Reject if F > F_{α,k,n−k−1}. Analogue of t-test for multiple coefficients jointly.

### Q8. Describe dummy variables.
**Model answer:** Binary (0/1) variables for categorical data. For g categories, use g−1 dummies with one as reference. Coefficient represents mean difference between category and reference, holding others constant. Dummy variable trap: including all g dummies + intercept causes perfect multicollinearity.

### Q9. Describe interaction terms.
**Model answer:** Products of variables (e.g., X₁·X₂). Model: Y = β₀ + β₁X₁ + β₂X₂ + β₃(X₁X₂) + u. Marginal effect of X₁: ∂Y/∂X₁ = β₁ + β₃X₂, depends on X₂. Captures how effect of one variable depends on another. Test significance via t-test on β₃.

### Q10. Interpret log-level, level-log, and log-log functional forms.
**Model answer:** Log-level: log(Y) = β₀ + β₁X. β₁·100 = approximate % change in Y per unit increase in X. Level-log: Y = β₀ + β₁log(X). β₁/100 = change in Y per 1% increase in X. Log-log: log(Y) = β₀ + β₁log(X). β₁ = elasticity — % change in Y per % change in X.

---

## Part B: Machine Learning Fundamentals (Q11-20)

### Q11. What is machine learning?
**Model answer:** A field of computer science and statistics focused on building models that learn patterns from data to make predictions or decisions. Emphasises predictive accuracy over causal interpretation. Includes supervised (labelled outcomes) and unsupervised (clustering, dimensionality reduction) methods.

### Q12. Distinguish supervised and unsupervised learning.
**Model answer:** Supervised: data includes labels (y_i values). Goal: predict y from x. Examples: regression (continuous y), classification (categorical y). Unsupervised: no labels. Goal: find structure (clusters, principal components). Examples: k-means, factor analysis.

### Q13. Distinguish prediction and causal inference.
**Model answer:** Prediction: what is the expected value of y given x? Doesn't require causal interpretation. Causal: how would y change if we manipulated x? Requires exogeneity assumption. ML excels at prediction; econometrics excels at causal inference. Different goals, different methods.

### Q14. What is a loss function?
**Model answer:** A function quantifying the error between predicted and actual values. For regression: squared error (y − ŷ)². For classification: 0-1 loss, log-loss. Training minimises average loss over data. Loss function choice affects what we optimise and the resulting model.

### Q15. Describe the bias-variance trade-off.
**Model answer:** Expected prediction error decomposes: E[(y − ŷ)²] = Bias² + Variance + Irreducible Error. Bias: systematic error from oversimplified model. Variance: error from model sensitivity to training data. Complex models: low bias, high variance. Simple models: high bias, low variance. Optimal: balance.

### Q16. Define overfitting.
**Model answer:** Model fits training data too well — captures random noise, not just signal. Symptoms: high training accuracy but poor out-of-sample performance. Causes: too many predictors, too complex models (high-order polynomials), insufficient regularisation. Cross-validation and holdout samples diagnose.

### Q17. Define underfitting.
**Model answer:** Model too simple to capture underlying patterns. Symptoms: poor performance on both training and test data. Causes: few features, overly restrictive functional form, excessive regularisation. Solutions: more features, complex models, less regularisation.

### Q18. Describe the training-validation-test split.
**Model answer:** Standard data partition: (1) Training set (60-70%) — fit model parameters. (2) Validation set (15-20%) — tune hyperparameters. (3) Test set (15-20%) — final evaluation, use once. Prevents overfitting to test data. Alternative: k-fold cross-validation on training + validation.

### Q19. Describe k-fold cross-validation.
**Model answer:** Partition training data into k folds. Train on k-1 folds, evaluate on held-out fold. Rotate so each fold serves as validation once. Average k performance estimates. Standard k = 5 or 10. Provides more robust performance estimate than single validation split.

### Q20. What is leave-one-out cross-validation (LOOCV)?
**Model answer:** Special case of k-fold with k = n. Each observation serves as validation once. Computationally intensive for large n. Unbiased but high variance (each training set nearly identical). Balance: 5- or 10-fold often preferred for practical performance.

---

## Part C: Regularisation (Q21-30)

### Q21. What is regularisation?
**Model answer:** Adding a penalty to the loss function to prevent overfitting. Shrinks coefficients toward zero. Reduces variance at some cost to bias. Common methods: ridge (L2 penalty), LASSO (L1 penalty), elastic net (combination). Particularly useful with many predictors.

### Q22. State the ridge regression objective.
**Model answer:** Minimise Σ(y_i − x_i'β)² + λΣβ_j². The L2 penalty shrinks coefficients toward zero but rarely to exactly zero. λ = 0 gives OLS; λ → ∞ shrinks all coefficients to zero. Use cross-validation to select λ.

### Q23. State the LASSO objective.
**Model answer:** Minimise Σ(y_i − x_i'β)² + λΣ|β_j|. L1 penalty. Unlike ridge, LASSO can set coefficients exactly to zero — provides variable selection. Useful when many predictors are irrelevant. λ controls sparsity: higher λ = fewer variables retained.

### Q24. Compare ridge and LASSO.
**Model answer:** Ridge: shrinks all coefficients; retains all variables. Better when many small effects. LASSO: shrinks and selects — some coefficients exactly zero. Better for variable selection with few important features. Elastic Net combines L1 and L2 penalties.

### Q25. How is λ selected in regularised regression?
**Model answer:** Cross-validation: for each candidate λ, compute average CV error across folds. Choose λ minimising CV error or using "1-SE rule" (largest λ within 1 SE of minimum, for parsimony). Automated via lasso/ridge routines in R (glmnet) or Python (scikit-learn).

### Q26. Describe elastic net regression.
**Model answer:** Combines L1 and L2 penalties: Σ(y − x'β)² + λ[(1−α)Σβ² + αΣ|β|]. α = 1 is LASSO; α = 0 is ridge. α ∈ (0,1) gives elastic net. Good when predictors are correlated — LASSO tends to select one from correlated group, elastic net keeps all.

### Q27. Why is standardisation important in regularised regression?
**Model answer:** Penalty applies equally to all coefficients, so variables with large scales get penalised disproportionately less. Standardise all predictors (mean 0, variance 1) before fitting. Software (scikit-learn, glmnet) typically standardises automatically. Coefficients reported should be back-transformed or on standardised scale.

### Q28. Describe the difference between OLS and ridge regression coefficients.
**Model answer:** Both solve for β. OLS: β̂ = (X'X)⁻¹X'y. Ridge: β̂ = (X'X + λI)⁻¹X'y. Adding λI shrinks coefficients and makes inversion stable even with multicollinearity. Ridge always has a solution; OLS fails with perfect multicollinearity.

### Q29. Describe dimensionality reduction (PCA).
**Model answer:** Principal Component Analysis: finds orthogonal linear combinations (components) of original predictors capturing maximum variance. Use first few components in regression. Reduces multicollinearity and dimensionality. Components are uninterpretable (unlike original variables).

### Q30. When is PCA regression appropriate?
**Model answer:** (1) Many highly correlated predictors. (2) Dimensionality reduction for stability. (3) When interpretability is less important than prediction. Limitations: loss of interpretation (components are mathematical constructs); may discard directions important for prediction.

---

## Part D: Model Evaluation (Q31-40)

### Q31. Compare R², adjusted R², and cross-validated R².
**Model answer:** R²: fit to training data (inflated with more predictors). Adjusted R²: penalises predictors but still training-based. CV-R²: estimates out-of-sample performance. Preferred: CV-R² for model selection; adjusted R² for descriptive purposes; R² alone is misleading.

### Q32. Define Mean Squared Error (MSE) and its uses.
**Model answer:** MSE = (1/n)Σ(y_i − ŷ_i)². Average squared prediction error. Standard performance metric for regression. Sensitive to large errors (quadratic). Alternative: Root MSE (RMSE) in original units; Mean Absolute Error (MAE) for robustness.

### Q33. Distinguish in-sample and out-of-sample performance.
**Model answer:** In-sample: fit to training data; measures model fit on data used for estimation. Can be optimistically biased (overfitting). Out-of-sample: performance on held-out data; measures true generalisation. Always report out-of-sample performance for prediction models.

### Q34. Describe the nested vs non-nested model comparison.
**Model answer:** Nested: one model's variables are subset of another. Use F-test on restrictions. Non-nested: neither is subset. Use: (1) Non-nested tests (J-test, Cox test). (2) Information criteria (AIC, BIC). (3) CV comparison. Non-nested comparison more complex than nested.

### Q35. State the AIC and BIC criteria.
**Model answer:** AIC = 2k − 2ln(L). Penalises k (number of parameters). BIC = k·ln(n) − 2ln(L). Penalises more heavily for larger n. BIC prefers parsimony; AIC prefers predictive accuracy. Lower is better. Asymptotically: AIC selects best predictive model; BIC selects true model (if in candidate set).

### Q36. Describe stepwise model selection.
**Model answer:** Forward: start empty, add best predictor iteratively. Backward: start full, remove worst. Stepwise: combination. Criticisms: inflated Type I error, unstable variable selection. Modern approach: LASSO for principled variable selection.

### Q37. What is the difference between model selection and hypothesis testing?
**Model answer:** Hypothesis testing: evaluate a specific claim about population (e.g., β_1 = 0). Model selection: choose among multiple models based on predictive criteria. Different goals: testing is confirmatory; selection is exploratory. Combining them (select then test) inflates error rates.

### Q38. Describe out-of-sample R².
**Model answer:** 1 − (SSE_out / SST_out), where SSE_out is prediction error on held-out sample. Measures how well model predicts new data. Can be negative (worse than predicting mean). Preferred metric for predictive model evaluation.

### Q39. What is a regression tree?
**Model answer:** Non-parametric method. Recursively splits data by predictor values to minimise within-region variance. Predictions are mean of y in each terminal region. Advantages: captures non-linearities, interactions. Disadvantages: unstable, prone to overfitting. Typically improved via ensemble methods (random forests).

### Q40. When would you use ML over classical econometrics?
**Model answer:** (1) Prediction is primary goal, not causal interpretation. (2) Many predictors (k approaches or exceeds n). (3) Non-linear and interaction patterns. (4) Need for automated variable selection. Stick with econometrics: (1) causal questions, (2) small k, (3) tight interpretation requirements. Increasingly overlap via "causal ML".

---

## Part E: Numerical and Application (Q41-45)

### Q41. Given 10-fold CV MSE = 4.2, and overall mean y = 50. Evaluate.
**Model answer:** RMSE = √4.2 = 2.05. Typical prediction error is 2.05 units around true value. For mean y = 50, that's about 4.1% relative error — acceptable depending on application. Report alongside baseline (e.g., always predicting mean: SE = SD of y). Compare to business requirements.

### Q42. LASSO with λ = 0.1 retains 5 of 20 predictors. Interpret.
**Model answer:** LASSO has performed variable selection. 15 predictors set to zero — considered uninformative. 5 retained carry the predictive signal. Verify: (1) Selected predictors make theoretical sense. (2) CV optimal λ? Higher λ = more shrinkage, may under-select. (3) Robustness: does selection change with different seeds or folds?

### Q43. Out-of-sample R² = 0.35; in-sample R² = 0.75. Diagnose.
**Model answer:** Substantial overfitting — model performs much better on training than new data. Causes: too many predictors relative to n, complex features, insufficient regularisation. Remedies: (1) Fewer predictors. (2) Add regularisation. (3) Increase training sample. (4) Cross-validated model selection. Trust out-of-sample R² = 0.35 as honest estimate.

### Q44. 5-fold CV R² across folds: 0.45, 0.50, 0.60, 0.25, 0.55. Interpret.
**Model answer:** Mean CV R² = 0.47 with substantial variance (0.25 to 0.60). Model performance is unstable across subsets. Investigate: (1) Are folds similar in size and composition? (2) Are some observations particularly hard to predict? (3) Does model assumptions vary? Instability is a flag for further investigation; report variance alongside mean.

### Q45. Ridge regression reduces coefficient from 2.5 (OLS) to 1.8. Interpret.
**Model answer:** Shrinkage: ridge pulls coefficient toward zero due to L2 penalty. Reduces variance of estimate at cost of some bias. Trade-off often worthwhile when collinearity present. Interpretation: "Best linear unbiased estimator is 2.5; biased but more stable ridge estimate is 1.8." Report both; choose based on out-of-sample validation.

---

## Part F: Application and Extension (Q46-50)

### Q46. Compare OLS and LASSO for predicting firm returns with 100 financial ratios.
**Model answer:** (1) OLS: all 100 ratios retained; high multicollinearity; unstable estimates. (2) LASSO: automatic variable selection; e.g., retains 15 most predictive ratios. (3) Cross-validate λ. (4) Compare CV performance. (5) LASSO likely dominates for prediction due to overfitting in OLS. Interpretation: LASSO-selected ratios are "drivers" of returns. Caveats: selection depends on sample; replicate on independent data.

### Q47. Your ridge model has very small coefficients across 50 variables. Evaluate.
**Model answer:** Small coefficients suggest: (1) Weak individual effects. (2) Correlated predictors — ridge distributes variance across all correlated variables. (3) High regularisation (λ large). Actions: (a) Check CV: was optimal λ very high? (b) Compare to LASSO — does it select a subset? (c) Business interpretation: model works, but no "dominant" predictor. Multiple small effects characterise many empirical contexts.

### Q48. Interpret a stepwise regression outcome: 3 models with different variables. Which to choose?
**Model answer:** Stepwise's instability shown — different variables selected in different runs. Actions: (1) Don't trust stepwise output. (2) Use LASSO or theory-driven selection. (3) If stepwise must be used: bootstrap for stability; report uncertainty in variable selection. (4) Consider model averaging (e.g., Bayesian Model Averaging) to incorporate uncertainty about model structure.

### Q49. Combine economic theory and ML: when to use?
**Model answer:** (1) Exploration: use ML to find unexpected patterns, then test theoretically. (2) Forecasting: econometrics for causal structure, ML for residual prediction. (3) Feature engineering: theory-driven feature creation, ML for selection. (4) Robustness: cross-validate econometric models. (5) Counterfactuals: use causal methods (IV, DiD); predictive ML for expected outcomes. Complementary rather than competing.

### Q50. Describe a complete ML analysis pipeline.
**Model answer:** (1) Define prediction goal and metrics. (2) Collect and clean data. (3) Exploratory analysis. (4) Feature engineering. (5) Train-validation-test split or CV. (6) Baseline model (e.g., mean prediction). (7) Try multiple methods (OLS, LASSO, tree, random forest). (8) Cross-validate to select best. (9) Evaluate on test set. (10) Diagnostic analysis (residuals, influential cases). (11) Deploy with performance monitoring. (12) Retrain with new data.

---

**Exam tip:** For ML questions in econometrics, always: (1) distinguish prediction from causal goal, (2) report train AND test performance, (3) use cross-validation for hyperparameter selection, (4) standardise before regularised methods, (5) discuss bias-variance trade-off explicitly, (6) prefer simpler models when performance is similar (parsimony principle).
