# ST3189 — Model Selection & Shrinkage: 50 Exam Questions with Model Answers

---

## Part A: Model Selection Principles (Q1-10)

### Q1. Why is model selection important?
**Model answer:** With many possible models (different predictors, functional forms, hyperparameters), we need a principled way to choose. Poor choice: overfitting, underfitting, misleading inferences. Good choice: optimal bias-variance balance, generalisation, interpretability. Systematic approach prevents arbitrary decisions.

### Q2. State the bias-variance trade-off in model selection.
**Model answer:** Expected prediction error = Bias² + Variance + Irreducible Error. Complex models: low bias, high variance (overfitting). Simple models: high bias, low variance (underfitting). Optimal complexity balances both. Model selection aims for minimum expected error.

### Q3. Distinguish model selection and hypothesis testing.
**Model answer:** Hypothesis testing: evaluate whether specific parameter equals specific value (e.g., β₁ = 0). Model selection: choose between candidate models based on predictive criteria. Different goals. Combining them (select then test) inflates error rates — should use separate data or holdout.

### Q4. Describe training vs test error.
**Model answer:** Training error: loss on data used to fit. Decreases with complexity. Test error: loss on new data. Decreases then increases with complexity (U-shape). Gap: training always ≤ test; large gap indicates overfitting. Test error approximates true generalisation error.

### Q5. Define cross-validation.
**Model answer:** Resampling approach to estimate test error. k-fold CV: (1) Partition data into k folds. (2) For each fold: train on k−1 folds, test on held-out fold. (3) Average k errors. Standard k = 5 or 10. Balances computation (vs LOOCV) and variance (vs single split).

### Q6. State information criteria (AIC, BIC).
**Model answer:** AIC = 2k − 2ℓ. Penalises k (parameters). BIC = k·ln(n) − 2ℓ. Heavier penalty for larger n. Lower = better. AIC: asymptotic predictive optimality. BIC: consistent model selection (true model identified as n → ∞). BIC favours parsimony.

### Q7. Compare AIC and BIC.
**Model answer:** AIC: good for prediction, may overfit. BIC: good for identifying true model, tends to be more parsimonious. BIC penalty k·ln(n) grows with n; AIC penalty 2k is constant. For large n, BIC selects smaller model than AIC. Use AIC for prediction; BIC for inference/parsimony.

### Q8. Describe the AICc criterion.
**Model answer:** Small-sample corrected AIC: AICc = AIC + 2k(k+1)/(n−k−1). Reduces to AIC for large n. Preferred when n/k < 40 (small samples). Less overfitting risk. Popular in ecology and similar fields with smaller datasets.

### Q9. Describe Mallows' Cp.
**Model answer:** Cp = (SSR + 2kσ²)/n. Asymptotically equivalent to AIC in linear regression. Penalises model complexity. Used to compare models with different k. Similar to adjusted R² but with different scaling.

### Q10. What is the best subset selection?
**Model answer:** Fits regression for every possible combination of predictors (2^p subsets for p variables). Selects best by CV, AIC, BIC, or adjusted R². Exhaustive but computationally expensive for large p. For p > 40, alternatives needed (forward/backward stepwise, regularisation).

---

## Part B: Stepwise Selection (Q11-20)

### Q11. Describe forward stepwise selection.
**Model answer:** (1) Start with null model (intercept only). (2) Add predictor that improves fit most (by CV, AIC, or p-value). (3) Repeat until no predictor improves fit significantly. Greedy algorithm. Produces sequence of nested models. Computationally feasible for large p.

### Q12. Describe backward stepwise selection.
**Model answer:** (1) Start with full model (all predictors). (2) Remove least useful predictor. (3) Repeat until removal significantly harms fit. Greedy like forward. Can miss models forward misses and vice versa. Typically use forward when n > p; backward requires n > p.

### Q13. Describe mixed (bidirectional) stepwise.
**Model answer:** Combines forward and backward: at each step can add or remove. More thorough search. Still greedy. SPSS default for regression; includes/excludes at each step based on significance levels.

### Q14. Criticise stepwise methods.
**Model answer:** (1) Inflated Type I error — selection inflates significance of retained variables. (2) Unstable: small data perturbations change selection. (3) Biased coefficients: post-selection inference invalid. (4) Doesn't consider all models (greedy). (5) Underestimates uncertainty. Modern alternative: LASSO, Bayesian averaging, or careful theory-driven selection.

### Q15. Why are stepwise p-values misleading?
**Model answer:** p-values assume single hypothesis test, not repeated testing with selection. Stepwise effectively performs many tests, inflating chance of spurious inclusion. Post-selection inference requires specialised methods (e.g., Berk et al. 2013, selective inference).

### Q16. Describe the partial F-test.
**Model answer:** Tests whether adding predictors to a nested model improves fit. F = [(RSS_R − RSS_U)/q] / [RSS_U/(n−k−1)]. q = additional parameters. Under H₀: new predictors have zero coefficients, F ~ F(q, n−k−1). Used in hierarchical model building.

### Q17. What's the difference between nested and non-nested model comparison?
**Model answer:** Nested: one model is a special case of the other (e.g., dropped variables). Use F-test or LR test. Non-nested: neither is a subset (different variables). Use: (1) Non-nested tests (Vuong test for non-nested LR). (2) Information criteria. (3) Cross-validation.

### Q18. How does multicollinearity affect model selection?
**Model answer:** Correlated predictors: (1) Inflated SEs — hard to distinguish which matter. (2) Unstable selection — small changes flip which variable is selected. (3) Misleading partial effects. Remedies: (1) Drop one of each correlated pair. (2) Combine into index. (3) Use ridge (keeps all) or elastic net. (4) Don't rely solely on t-tests.

### Q19. Describe forward regression with AIC.
**Model answer:** Add variable whose inclusion reduces AIC most. Stop when no variable reduces AIC. Unlike forward with p-values, uses fit criterion — less biased. Preferred over p-value forward selection. AIC-based stepwise is default in R's step() function.

### Q20. State when to prefer LASSO over stepwise.
**Model answer:** (1) Large p (LASSO handles p > n). (2) Variable selection bias: LASSO shrinks + selects simultaneously. (3) Reproducibility: more stable than stepwise. (4) Automated tuning via CV. (5) Handles multicollinearity better. Stepwise retained mainly for historical and teaching purposes.

---

## Part C: Regularisation (Q21-30)

### Q21. State the ridge regression objective.
**Model answer:** Minimise Σ(y − x'β)² + λΣβ². L2 penalty shrinks coefficients toward zero. Closed-form: β̂ = (X'X + λI)⁻¹X'y. λ = 0 gives OLS; λ → ∞ shrinks all to zero. λ chosen by cross-validation.

### Q22. State the LASSO objective.
**Model answer:** Minimise Σ(y − x'β)² + λΣ|β|. L1 penalty creates sparsity — some coefficients exactly zero. No closed-form solution; uses coordinate descent or LARS. Equivalent to MAP with double-exponential (Laplace) prior. Variable selection automatic.

### Q23. State the elastic net objective.
**Model answer:** Minimise Σ(y − x'β)² + λ[(1−α)Σβ² + αΣ|β|]. α ∈ [0, 1]: α = 0 is ridge, α = 1 is LASSO. Combines properties: some shrinkage + some selection. Handles correlated predictors better than LASSO (retains groups, not arbitrary subsets).

### Q24. Compare ridge and LASSO geometrically.
**Model answer:** Ridge: constraint region is a circle (L2 ball). LASSO: constraint region is a diamond (L1 ball). Corners of LASSO diamond align with axes — constrained solution often on axes (zero coefficients). Ridge solutions rarely on axes. Visualises why LASSO selects.

### Q25. Why does LASSO produce exactly zero coefficients?
**Model answer:** L1 penalty is non-differentiable at zero. Optimal solution often at "kink" where one or more coefficients are zero. Unlike ridge (smooth penalty), which never produces exact zeros. Mathematical property of L1 norm.

### Q26. Describe tuning λ via cross-validation.
**Model answer:** (1) For each candidate λ, compute k-fold CV error. (2) Choose λ minimising mean CV error. (3) Or use "1-SE rule": largest λ with CV error within 1 SE of minimum — more parsimonious. Common λ grid: logarithmic from 10⁻⁴ to 10².

### Q27. Why standardise before regularisation?
**Model answer:** Penalty applies equally to all coefficients. Variables with larger scales have smaller coefficients mechanically — penalised less. Standardising (mean 0, variance 1) gives equal penalty. Standard practice in regularised methods.

### Q28. Describe the LARS algorithm.
**Model answer:** Least Angle Regression — efficient algorithm for LASSO path. (1) Start with zero coefficients. (2) Add variable most correlated with residual. (3) Move in equiangular direction. (4) Stop when another variable becomes equally correlated, then move in both directions. (5) Continues until LASSO path complete.

### Q29. Describe coordinate descent for LASSO.
**Model answer:** Cyclically update one coefficient at a time, holding others fixed. Each step has closed-form (soft thresholding): β_j = sign(β_j^OLS) · max(|β_j^OLS| − λ, 0). Efficient, especially for sparse solutions. Used in glmnet package.

### Q30. Describe group LASSO.
**Model answer:** Extends LASSO to grouped variables (e.g., all dummies for a categorical variable). Penalty: λ Σ_g √(Σ β²_j in group g). Either whole group included or excluded together. Useful when structure is hierarchical (categorical variables, temporal lags).

---

## Part D: Dimensionality Reduction (Q31-40)

### Q31. Describe Principal Component Analysis (PCA).
**Model answer:** Finds orthogonal linear combinations of predictors with maximum variance. First PC: direction of greatest variance. Subsequent PCs: orthogonal directions with decreasing variance. Reduces dimensionality while preserving information.

### Q32. How do you compute principal components?
**Model answer:** (1) Standardise data. (2) Compute covariance matrix Σ. (3) Eigendecomposition: Σ = VΛV'. Eigenvectors V (columns) are principal directions; eigenvalues λ (diagonal of Λ) are variances. (4) PCs: Z = XV (project data onto eigenvectors).

### Q33. What proportion of variance is captured by first k PCs?
**Model answer:** (λ₁ + λ₂ + ... + λ_k) / (λ₁ + λ₂ + ... + λ_p). Cumulative proportion of variance. Often retain components until 90-95% cumulative variance. Alternatively: eigenvalues > 1 (Kaiser rule) or scree plot elbow.

### Q34. Describe PCA regression.
**Model answer:** (1) Compute PCs of X. (2) Select first k PCs. (3) Regress Y on k PCs. Advantages: reduces dimensionality, avoids multicollinearity. Disadvantages: PCs capture variance in X, not necessarily relevance to Y; interpretability lost.

### Q35. Compare PCA regression and partial least squares (PLS).
**Model answer:** PCA regression: components maximise variance in X. PLS: components maximise covariance between X and Y. PLS directly optimises for predicting Y. PLS often outperforms PCA regression when not all PC variance is relevant to Y.

### Q36. What are the limitations of PCA?
**Model answer:** (1) Linear — doesn't capture non-linear structure. (2) Sensitive to scale — must standardise. (3) Assumes high variance = important (not always true). (4) Components hard to interpret. (5) Supervised goals (regression, classification) ignored — unsupervised.

### Q37. Describe how to choose number of PCs.
**Model answer:** (1) Scree plot: retain before "elbow". (2) Cumulative variance threshold (90%). (3) Kaiser: eigenvalues > 1. (4) Cross-validation: use each k PC count, pick best CV. (5) Parallel analysis: compare to random data. Multiple methods; compare.

### Q38. Describe kernel PCA.
**Model answer:** Non-linear generalisation: implicitly map to high-dimensional space via kernel, then perform PCA. Captures non-linear structure. Same as regular PCA if linear kernel. Useful for data with curved manifolds. Common kernels: RBF, polynomial.

### Q39. Describe t-SNE.
**Model answer:** t-Distributed Stochastic Neighbor Embedding. Non-linear dimensionality reduction for visualisation. Preserves local neighborhood structure. Not for general dimension reduction (non-deterministic, sensitive to hyperparameters). Great for visualising clusters in high-dim data.

### Q40. Describe UMAP.
**Model answer:** Uniform Manifold Approximation and Projection. Alternative to t-SNE. Preserves both local and global structure. Faster and more stable than t-SNE. Commonly used for visualisation and as preprocessing for clustering or classification. Hyperparameters: n_neighbors, min_dist.

---

## Part E: Evaluation and Applications (Q41-45)

### Q41. Describe nested cross-validation.
**Model answer:** Two layers: outer CV for test error estimation, inner CV for hyperparameter tuning. Inner: tune hyperparameters on each fold of outer training set. Outer: evaluate tuned model on outer test fold. Prevents overfitting to CV during tuning. Unbiased estimate of generalisation error.

### Q42. What is double-dipping?
**Model answer:** Using same data for both model selection and inference. Produces biased test error estimates and inflated confidence. Avoid by: separate holdout set, nested CV, or corrections for selective inference. Common violation in applied research.

### Q43. Describe bootstrap for model evaluation.
**Model answer:** (1) Resample training data B times with replacement. (2) Fit model on each bootstrap sample. (3) Assess on out-of-bag samples (not selected). Estimator variance, bias, CI. Often used for ensemble methods (bagging). Alternative to CV.

### Q44. Compare cross-validation and bootstrap.
**Model answer:** CV: deterministic resampling, evaluates on held-out data. Bootstrap: random sampling with replacement, evaluates on OOB samples. CV: preferred for model selection, clearer interpretation. Bootstrap: standard errors, CIs for statistics, ensemble methods. Use appropriate method for purpose.

### Q45. Evaluate when to use regularisation over variable selection.
**Model answer:** Regularisation (ridge): continuous shrinkage, stable, handles multicollinearity. Variable selection (LASSO): explicit subset, interpretability, when truly sparse. Criteria: (1) If some predictors might be truly zero → LASSO. (2) If predictors are correlated or all potentially matter → ridge or elastic net. (3) Interpretability → LASSO for sparsity.

---

## Part F: Application (Q46-50)

### Q46. With 500 predictors and n = 200, design a prediction model.
**Model answer:** (1) p >> n: traditional OLS infeasible. (2) Options: (a) LASSO for variable selection + shrinkage. (b) Ridge for shrinkage without selection. (c) Elastic net for balance. (3) Cross-validate λ. (4) Pre-screen: remove predictors with near-zero variance. (5) If structure exists: group LASSO for categorical variables. (6) Report top selected predictors and their stability (e.g., bootstrapping). Trust CV performance, not R² on training.

### Q47. Compare AIC, BIC, and cross-validation for model choice.
**Model answer:** AIC: likelihood-based, optimistic predictive criterion. BIC: consistent selection, penalises more. CV: direct estimate of predictive error, more computationally expensive but most accurate. Recommendation: CV as primary when computational budget allows; use AIC/BIC for quick comparisons or large model sets. In large samples (> 1000), often agree.

### Q48. How would you present results from a LASSO analysis?
**Model answer:** (1) Plot CV error vs λ — show minimum and "1-SE" rule. (2) Coefficient plot: show shrinkage as λ changes. (3) Selected variables table at optimal λ. (4) Stability analysis: variables selected across bootstrap samples. (5) CV R² / MSE: honest predictive performance. (6) Report both CV-optimal and parsimonious models. (7) Caveats about post-selection inference.

### Q49. Your LASSO CV chose λ giving 5 predictors; 1-SE rule gives 12. Which?
**Model answer:** CV-optimal: 5 predictors, best predictive performance. 1-SE: 12 predictors, slightly larger CV error but may generalise better due to model parsimony not favoured by raw minimum. Choice: (1) If predictive accuracy is primary: λ at minimum. (2) If interpretability and stability matter: 1-SE rule. (3) Report both. Often 1-SE is preferred in applied statistics for robustness.

### Q50. Describe a complete model selection pipeline.
**Model answer:** (1) Define prediction goal and success metric. (2) Split data: train, validation, test. (3) Baseline: simple model (mean, naive). (4) Candidate models: OLS, ridge, LASSO, random forest, gradient boosting. (5) Train with CV on training set for hyperparameter tuning. (6) Evaluate on validation for model comparison. (7) Final model evaluation on test set. (8) Sensitivity analysis: how does performance vary with predictor choice? (9) Interpret selected features/predictors. (10) Deploy with monitoring; retrain as needed. Always report cross-validated performance, not training fit.

---

**Exam tip:** For model selection questions, always: (1) state bias-variance principle clearly, (2) specify criterion (AIC/BIC/CV) and justify, (3) describe hyperparameter tuning via cross-validation, (4) compare multiple models, (5) report honest out-of-sample performance, (6) discuss limitations (data-driven bias, stability, interpretability).
