# ST3189 — Trees & Ensembles: 50 Exam Questions with Model Answers

---

## Part A: Decision Trees (Q1-15)

### Q1. What is a decision tree?
**Model answer:** Non-parametric model that recursively partitions the predictor space into regions and predicts within each region. For regression: predict mean of y in each terminal node. For classification: predict majority class. Visual and interpretable. Foundation for random forests and boosting.

### Q2. Describe the CART algorithm.
**Model answer:** Classification and Regression Trees. Greedy recursive partitioning: at each node, split data into two by a single predictor value to maximise purity (classification) or minimise variance (regression). Continue until stopping criterion (e.g., minimum node size, maximum depth).

### Q3. How are splits chosen for regression trees?
**Model answer:** At each node, for each predictor and candidate split point: compute SSR after splitting. Choose split minimising total SSR: SSR_left + SSR_right. Equivalently, maximise the reduction in variance. Greedy: doesn't look ahead, may miss globally optimal splits.

### Q4. How are splits chosen for classification trees?
**Model answer:** Maximise node "purity" after splitting. Common impurity measures: (1) Gini index: G = Σp_k(1−p_k). (2) Cross-entropy: E = −Σp_k log p_k. (3) Classification error rate: 1 − max(p_k). Gini and entropy sensitive to probabilities; error rate less so. Gini and entropy preferred for growing trees.

### Q5. State the Gini impurity formula.
**Model answer:** Gini = Σ_k p_k(1 − p_k), where p_k is proportion of class k in node. Range: 0 (pure) to (K−1)/K (uniform). Minimised for pure nodes. Probability of misclassifying a randomly chosen item if labelled randomly according to distribution.

### Q6. Describe the cross-entropy criterion.
**Model answer:** Entropy = −Σ_k p_k log p_k. Related to information theory — measures uncertainty. Minimised for pure nodes (log 1 = 0). Similar to Gini in practice; gradients may differ. Common in classification. Used by ID3 and C4.5 algorithms.

### Q7. Why do trees overfit and how to prevent?
**Model answer:** Greedy splits can grow arbitrarily complex trees with perfect training accuracy but poor generalisation. Prevention: (1) Pre-pruning (early stopping): limit depth, minimum leaf size, maximum features. (2) Post-pruning: grow full tree, then cut back via cost-complexity pruning.

### Q8. Describe cost-complexity pruning.
**Model answer:** Add complexity penalty: minimise RSS + α|T|, where |T| is number of terminal nodes. α controls penalty: α = 0 gives full tree; α large gives minimal tree. Choose α via cross-validation. Creates sequence of optimal trees for each α. Selects best trade-off.

### Q9. State the advantages of decision trees.
**Model answer:** (1) Interpretable — visual representation of decisions. (2) Handle continuous and categorical predictors. (3) No feature scaling needed. (4) Capture non-linearities and interactions automatically. (5) Robust to outliers in predictors. (6) Handle missing data naturally (surrogate splits).

### Q10. State the disadvantages of decision trees.
**Model answer:** (1) Unstable — small changes in data can produce very different trees. (2) High variance. (3) Greedy — locally optimal, not globally. (4) Often lower accuracy than ensemble methods. (5) Biased toward splits with many values. (6) Can't capture linear relationships efficiently (many splits needed for a diagonal line).

### Q11. Compare trees with linear regression.
**Model answer:** Linear regression: parametric, captures linear relationships, interpolates smoothly. Trees: non-parametric, captures non-linear and interactions, predictions are step functions. Linear better for: smooth effects, few predictors, interpretation via coefficients. Trees better for: complex interactions, heterogeneous populations, interpretability via decision path.

### Q12. Describe surrogate splits for missing data.
**Model answer:** If primary split variable is missing, use a highly correlated surrogate variable. Trained during tree building — each node stores primary and backup splits. Allows trees to handle missing data without imputation. Good feature of CART software.

### Q13. Describe categorical variable handling in trees.
**Model answer:** For categorical with K levels: naive approach tries all 2^{K−1} − 1 subsets — exponential. CART simplification: sort categories by mean y and treat as ordinal. Efficient. For random forests, one-hot encode and handle in bootstrap. Careful: high-cardinality categoricals can bias splitting.

### Q14. What is bias-variance in trees?
**Model answer:** Deep trees: low bias (fit training well), high variance (sensitive to data). Shallow trees: high bias, low variance. Trade-off controlled by tree depth, leaf size, and pruning. Ensembles (random forests, boosting) reduce variance dramatically.

### Q15. Describe regression tree prediction.
**Model answer:** For new x: traverse tree from root using splits. Reach terminal node. Prediction = mean of y values in that node from training. Step-function prediction. Uncertainty via residual variance within node or bootstrap estimates.

---

## Part B: Bagging and Random Forests (Q16-30)

### Q16. Describe bootstrap aggregating (bagging).
**Model answer:** (1) Generate B bootstrap samples of training data. (2) Fit a tree on each sample (unpruned). (3) Predict by averaging (regression) or majority vote (classification). Reduces variance of trees by averaging many. Doesn't reduce bias. Typically B = 100-500.

### Q17. Why does bagging reduce variance?
**Model answer:** Var(average of B iid variables) = σ²/B. For correlated variables: Var(Σ X_i/B) = σ²(1 + (B−1)ρ)/B, where ρ is correlation. Bagging reduces variance of the mean as B grows. Benefit depends on how uncorrelated individual predictions are. Higher ρ → less benefit.

### Q18. Describe random forests.
**Model answer:** Improvement over bagging. At each split, consider only a random subset of m predictors (not all p). Default: m = √p for classification, m = p/3 for regression. De-correlates trees — each tree sees different features. Further variance reduction. Breiman (2001).

### Q19. Why does random forest outperform bagging?
**Model answer:** In bagging, if one predictor is very strong, every tree uses it at the top — highly correlated trees. Random feature selection forces tree diversity. Lower correlation ρ → lower variance of ensemble. Typically 5-15% accuracy improvement.

### Q20. Describe out-of-bag (OOB) error.
**Model answer:** Each bootstrap sample leaves out about 37% of observations. These OOB observations can evaluate each tree. Aggregate OOB predictions across trees for each observation. OOB error is unbiased estimate of test error — no need for separate validation set.

### Q21. State hyperparameters of random forests.
**Model answer:** (1) Number of trees B: more is better, no overfitting risk; diminishing returns. (2) Max features m: controls tree diversity. (3) Tree depth / min samples per leaf: controls individual tree complexity. (4) Bootstrap sample size. Defaults often excellent; tune m and tree depth if needed.

### Q22. Describe variable importance in random forests.
**Model answer:** Two types: (1) Gini importance: sum of Gini reductions when variable splits. (2) Permutation importance: OOB error increase when variable's values are randomly permuted. Permutation is more reliable — doesn't inflate importance for high-cardinality variables.

### Q23. What are the advantages of random forests?
**Model answer:** (1) High accuracy. (2) Handles non-linearities and interactions. (3) No tuning required for reasonable performance. (4) Built-in OOB estimate. (5) Variable importance. (6) Handles missing data. (7) Parallelisable. (8) Works for regression and classification. (9) Robust to outliers in predictors.

### Q24. What are the disadvantages of random forests?
**Model answer:** (1) Less interpretable than single trees. (2) Memory-intensive (many trees stored). (3) Slower at prediction time than simpler models. (4) Doesn't extrapolate — predictions bounded by training data. (5) Biased for outcomes near 0 or 1 in classification. (6) Correlated categorical variables issue.

### Q25. Compare random forest and gradient boosting.
**Model answer:** Random forest: parallel, bagging-based, low-variance trees. Gradient boosting: sequential, each tree corrects previous errors, lower bias. Random forest: easier to tune, less overfitting. Gradient boosting: higher accuracy potential, more tuning, overfitting risk. Current: XGBoost, LightGBM often win competitions.

### Q26. When should you prefer random forest over linear regression?
**Model answer:** (1) Non-linear relationships. (2) Complex interactions. (3) Heterogeneous populations. (4) Mixed data types. (5) Don't need exact coefficient interpretation. Linear regression preferred: (1) Small data. (2) Simple relationships. (3) Interpretable coefficients. (4) Statistical inference. In practice, start simple, use RF as strong baseline for prediction.

### Q27. Describe hyperparameter tuning for random forests.
**Model answer:** (1) n_estimators: try 100, 500, 1000 — more doesn't hurt. (2) max_features: √p default; try p/3, p/2 for regression. (3) max_depth: unlimited usually fine. (4) min_samples_leaf: 1 to 5. (5) Use grid or random search with CV. RF often works well with defaults.

### Q28. Describe extremely randomized trees (Extra Trees).
**Model answer:** Variant of random forests. Additional randomness: (1) Random splits instead of optimal. (2) Use full data (no bootstrap). Further de-correlates trees. Faster than RF. Slight accuracy decrease; better variance. Good alternative especially for small data.

### Q29. Describe proximity measures from random forests.
**Model answer:** For each pair of observations, count trees where both fall in the same leaf. Divide by number of trees. High proximity = similar observations according to the forest. Used for: (1) Outlier detection. (2) Imputation of missing values. (3) Clustering.

### Q30. How does random forest handle class imbalance?
**Model answer:** Standard RF biased toward majority class. Solutions: (1) Balanced random forest: bootstrap equal samples from each class. (2) Weighted random forest: weight minority class higher in splits. (3) Threshold adjustment. (4) Post-hoc calibration. For extreme imbalance, consider other methods (anomaly detection, isolation forest).

---

## Part C: Boosting (Q31-40)

### Q31. Describe boosting.
**Model answer:** Sequential ensemble: each model corrects errors of previous models. Start with weak learners (shallow trees). Each subsequent learner focuses on misclassified points or residuals. Weighted combination. Reduces bias. Historical: AdaBoost (1996). Modern: Gradient Boosting, XGBoost.

### Q32. Describe AdaBoost.
**Model answer:** (1) Initialise uniform weights. (2) Fit weak learner to weighted data. (3) Compute error rate. (4) Compute learner weight based on error. (5) Update sample weights: increase for misclassified, decrease for correct. (6) Repeat. Final prediction: weighted majority vote. Exponential loss.

### Q33. Describe gradient boosting.
**Model answer:** Generalises boosting to any differentiable loss. At each step: (1) Compute negative gradient of loss with respect to current predictions (pseudo-residuals). (2) Fit weak learner to these. (3) Add to ensemble with shrinkage (learning rate). More flexible than AdaBoost — handles regression, custom losses.

### Q34. State the objective function of gradient boosting.
**Model answer:** At iteration t: minimise Σ L(y_i, F_{t−1}(x_i) + h(x_i)), where F_{t−1} is current ensemble prediction and h is new learner. h_t ≈ −η ∂L/∂F at F_{t−1}. η is learning rate (shrinkage). L: squared error, logistic, custom.

### Q35. Describe hyperparameters of gradient boosting.
**Model answer:** (1) Number of trees: too many → overfit. (2) Learning rate (shrinkage, η): smaller = more trees but better generalisation. Typical: 0.01-0.1. (3) Max depth: shallow (3-5) common. (4) Subsample: stochastic gradient boosting uses random subset each iteration. (5) Regularisation (L1/L2 on weights).

### Q36. Describe the bias-variance trade-off in boosting.
**Model answer:** Each tree reduces bias. Too many trees → overfitting (high variance). Regularise via: (1) Smaller learning rate. (2) Fewer trees. (3) Shallow trees. (4) Subsampling. (5) Early stopping based on validation loss. Unlike random forest, boosting can overfit with too many trees.

### Q37. Describe XGBoost.
**Model answer:** Optimised gradient boosting. Key features: (1) Regularisation (L1/L2) in objective. (2) Handles missing values natively. (3) Sparsity-aware split finding. (4) Parallelised tree construction. (5) Weighted quantile sketch for split candidates. (6) Early stopping. Dominant method in ML competitions. Xu et al. (2016).

### Q38. Compare gradient boosting and random forests.
**Model answer:** Random forest: parallel, independent trees, reduces variance, works with defaults. Boosting: sequential, each tree depends on previous, reduces bias, more tuning needed. Boosting typically achieves higher accuracy but requires more care. Random forest more forgiving for beginners.

### Q39. Describe LightGBM.
**Model answer:** Microsoft's gradient boosting framework. Innovations: (1) Gradient-based One-Side Sampling (GOSS) — keeps instances with large gradients. (2) Exclusive Feature Bundling (EFB) — combines mutually exclusive features. Faster and more memory-efficient than XGBoost. Also dominates competitions.

### Q40. When should you use boosting over random forest?
**Model answer:** (1) Maximum accuracy required. (2) Have time to tune hyperparameters. (3) Moderate to large data. (4) Structured data (tabular). (5) Competitive ML context (Kaggle). Random forest when: (1) Need quick baseline. (2) Limited tuning time. (3) Stability over peak accuracy. (4) Small data. Both excellent; boosting typically wins head-to-head when properly tuned.

---

## Part D: Evaluation and Hyperparameters (Q41-45)

### Q41. Describe hyperparameter tuning for tree ensembles.
**Model answer:** Grid or random search over: n_estimators, max_depth, min_samples_leaf, max_features (RF) or learning_rate (GBM). Use cross-validation to select. Bayesian optimisation (Hyperopt, Optuna) more efficient for large spaces. Start with defaults; tune key parameters first.

### Q42. Why should you not include all predictors in a tree?
**Model answer:** With many predictors: (1) Some are irrelevant — noise. (2) Tree may split on noise rather than signal. (3) Interpretability suffers. In RF, max_features restriction helps. Feature selection pre-step can help for boosting. Regularised methods (LASSO) automatic. Cross-validation diagnoses.

### Q43. Describe SHAP values.
**Model answer:** SHapley Additive exPlanations. Game-theoretic approach to feature importance. Allocates prediction to each feature fairly. Provides local (per-prediction) importance. More robust than default feature importance measures. Used to explain complex models (random forest, gradient boosting, neural networks).

### Q44. Evaluate time-series forecasting with tree ensembles.
**Model answer:** Tree ensembles don't handle temporal dependence natively. Solutions: (1) Feature engineering with lags, rolling means. (2) Target encoding by time. (3) Use time-aware CV (expanding window, not random shuffling). (4) Compare to traditional time-series (ARIMA, exponential smoothing). XGBoost often competitive on tabular time series.

### Q45. When should you worry about overfitting in random forests?
**Model answer:** RF is relatively robust to overfitting but can occur if: (1) Trees too deep for small dataset. (2) Too few trees. (3) m too large (low diversity). (4) Noise features dominate. Monitor: OOB error vs training error — large gap = overfitting. Remedy: limit depth, reduce m, increase n_estimators.

---

## Part E: Application (Q46-50)

### Q46. Building a random forest for fraud detection.
**Model answer:** (1) Highly imbalanced data (~0.1% fraud). Use balanced class weights or balanced bootstrap. (2) Feature engineering: transaction history, behavioural patterns, time-based features. (3) Train/test split respecting time (no future leakage). (4) Evaluate on AUPR (not accuracy). (5) Tune hyperparameters via CV. (6) Feature importance for investigation. (7) Deploy with threshold tuning by cost of misses. (8) Monitor for drift.

### Q47. Compare XGBoost and random forest on tabular data.
**Model answer:** Both excellent for tabular. XGBoost: higher accuracy potential (10% or more), more tuning. RF: simpler, more stable, good defaults. Rule of thumb: start with RF for baseline, try XGBoost if accuracy insufficient. For competition: XGBoost. For production stability: RF.

### Q48. Interpret a feature importance ranking from random forest.
**Model answer:** (1) Identify top features by Gini or permutation importance. (2) Verify with domain knowledge — are they theoretically relevant? (3) Partial dependence plots show how each feature affects prediction. (4) SHAP values explain individual predictions. (5) Caveat: feature importance isn't the same as causal effect — correlated features may share importance or get inflated. (6) Cross-validate importance across folds for stability.

### Q49. Your XGBoost model overfits with default parameters. Tune.
**Model answer:** (1) Reduce max_depth (try 3, 5 instead of unlimited). (2) Decrease learning_rate (0.01 instead of 0.1). (3) Increase min_child_weight (regularisation). (4) Subsample rows (0.8). (5) Subsample columns per split (colsample_bytree = 0.8). (6) Add L1/L2 regularisation. (7) Early stopping on validation set. (8) Cross-validate. Smaller models generalise better.

### Q50. Describe a complete tree ensemble pipeline.
**Model answer:** (1) Data exploration and feature engineering. (2) Handle missing values (RF native; XGBoost native). (3) Train-test split (time-aware if needed). (4) Baseline: single tree, logistic regression. (5) Random forest with defaults. (6) XGBoost with default tuning. (7) Cross-validation for hyperparameter tuning. (8) Evaluate on test set with appropriate metrics. (9) Feature importance + SHAP for interpretation. (10) Deploy with monitoring. (11) Compare variants; retrain periodically.

---

**Exam tip:** For tree/ensemble questions, always: (1) identify tree type (regression or classification), (2) describe splitting criterion (Gini, entropy, MSE), (3) explain how ensembles reduce variance (bagging) or bias (boosting), (4) state key hyperparameters and tuning approach, (5) evaluate via CV with appropriate metrics, (6) discuss interpretability (feature importance, SHAP), (7) compare to linear alternatives.
