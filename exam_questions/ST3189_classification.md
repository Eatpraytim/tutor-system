# ST3189 — Classification: 50 Exam Questions with Model Answers

---

## Part A: Classification Fundamentals (Q1-10)

### Q1. What is classification?
**Model answer:** Supervised learning task predicting a categorical output y ∈ {1, 2, ..., K}. Models P(y = k | x) or a decision boundary. Examples: spam detection (2 classes), digit recognition (10 classes), disease diagnosis. Contrasts with regression (continuous y).

### Q2. Distinguish binary and multiclass classification.
**Model answer:** Binary: K = 2 (e.g., pass/fail, spam/not). Simpler, many algorithms designed for binary. Multiclass: K > 2 (e.g., digit recognition 0-9). Approaches: one-vs-rest, one-vs-one, native multiclass (softmax, tree-based). Multi-label extends to each input having multiple labels.

### Q3. Describe the Bayes classifier.
**Model answer:** Theoretically optimal: assign to class k that maximises P(Y = k | X). Bayes error rate: 1 − E[max_k P(k|X)] — lowest achievable error with known distributions. In practice, we estimate P(Y|X) from data — all classifiers approximate the Bayes classifier.

### Q4. Compare generative and discriminative classifiers.
**Model answer:** Generative: model joint P(X, Y), then compute P(Y|X) via Bayes. Examples: LDA, Naive Bayes. Discriminative: model P(Y|X) directly. Examples: logistic regression, SVM, neural networks. Discriminative often more accurate; generative better with small data or missing features.

### Q5. State the loss functions for classification.
**Model answer:** (1) 0-1 loss: I(y ≠ ŷ). (2) Cross-entropy / log-loss: −Σy_k log P̂(y_k). (3) Hinge loss: max(0, 1 − y·ŷ) (for SVM). Different losses produce different optimisation objectives. Log-loss is smooth and gradient-friendly.

### Q6. Describe the confusion matrix.
**Model answer:** Matrix of actual vs predicted classes. For binary: TP, TN, FP, FN. Diagonal = correct predictions. Basis for: accuracy = (TP+TN)/(all), precision = TP/(TP+FP), recall/sensitivity = TP/(TP+FN), specificity = TN/(TN+FP), F1 = harmonic mean of precision and recall.

### Q7. Compare accuracy and F1 score.
**Model answer:** Accuracy: overall correct / total. Misleading for imbalanced data (always predicting majority gives high accuracy). F1: harmonic mean of precision and recall. Better for imbalanced data. Prefer F1, AUC, or cost-sensitive metrics when classes are unequal.

### Q8. Describe the ROC curve.
**Model answer:** Plots true positive rate (sensitivity) against false positive rate (1 − specificity) for all thresholds. Traces performance across operating points. Area Under Curve (AUC): 0.5 = random, 1.0 = perfect. Threshold-free evaluation. AUC > 0.8 considered good.

### Q9. Describe precision-recall curves.
**Model answer:** Plot precision vs recall for various thresholds. Better than ROC when classes are imbalanced (ROC can appear optimistic with many negatives). AUPR (Area Under PR curve): preferred metric for rare positive class detection.

### Q10. What is class imbalance and how to address it?
**Model answer:** When one class is much more common than others. Issues: (1) Classifier biased toward majority. (2) Accuracy misleading. Solutions: (1) Resampling (oversample minority, undersample majority, SMOTE). (2) Class weights (weight minority class). (3) Use appropriate metrics (F1, AUPR). (4) Threshold adjustment.

---

## Part B: Logistic Regression (Q11-20)

### Q11. State the logistic regression model.
**Model answer:** P(Y=1|X) = σ(Xβ) = 1/(1 + e^(−Xβ)). log-odds: log[P/(1−P)] = Xβ. β_j: change in log-odds per unit X_j. Estimated by MLE on the log-likelihood ℓ(β) = Σ y_i log p_i + (1 − y_i) log(1 − p_i).

### Q12. State the log-likelihood for logistic regression.
**Model answer:** ℓ(β) = Σ [y_i log(σ(x_i'β)) + (1 − y_i) log(1 − σ(x_i'β))]. Negative is cross-entropy loss. Concave in β — unique global maximum. No closed-form MLE; use numerical optimisation (Newton-Raphson, IRLS, gradient descent).

### Q13. State the gradient of the log-likelihood.
**Model answer:** ∇ℓ(β) = Σ (y_i − σ(x_i'β)) x_i = X'(y − p), where p_i = σ(x_i'β). Setting to zero gives normal equations. This is a weighted residual equation — basis for iterative optimisation. Closed connection to generalised linear models.

### Q14. State the Hessian for logistic regression.
**Model answer:** H = −X'WX, where W = diag(p_i(1 − p_i)). Negative definite — confirms concavity. Used in Newton-Raphson: β_{t+1} = β_t + (X'W_t X)⁻¹ X'(y − p_t). Also gives variance of β̂: Var(β̂) = (X'WX)⁻¹.

### Q15. Describe regularised logistic regression.
**Model answer:** L2 (ridge): minimise −ℓ(β) + λΣβ². Shrinks coefficients. L1 (LASSO): minimise −ℓ(β) + λΣ|β|. Produces sparse coefficients. Elastic net: combines both. Use cross-validation to select λ. Regularisation essential when p is large relative to n.

### Q16. Describe multinomial logistic regression.
**Model answer:** For K classes: softmax function P(Y=k|X) = exp(x'β_k) / Σ exp(x'β_j). One reference class (β_ref = 0). K − 1 sets of coefficients estimated. Cross-entropy loss generalises. Standard method for multi-class problems.

### Q17. Compare logistic regression and LDA.
**Model answer:** LR: discriminative; models P(Y|X) directly; no distributional assumptions on X. LDA: generative; assumes X|Y = k ~ N(μ_k, Σ) (common covariance); works via Bayes' theorem. LR more robust; LDA more efficient when assumptions hold and with small n.

### Q18. When is logistic regression preferred?
**Model answer:** (1) Unknown or non-normal X distribution. (2) Interpretable linear effects. (3) Mix of continuous and categorical predictors. (4) Want probability outputs. (5) Baseline model before trying complex methods. LR is a standard starting point; often surprisingly competitive with more complex classifiers.

### Q19. Describe odds ratios and their interpretation.
**Model answer:** OR = e^β_j: odds of Y = 1 multiplied by OR for unit increase in X_j. OR > 1: positive effect. OR = 1.5: 50% higher odds. Useful for interpretation — doesn't depend on baseline probability. Distinct from risk ratio and probability change (which do depend).

### Q20. How to handle interactions in logistic regression?
**Model answer:** Include product terms: X₁X₂. Effect of X₁ now depends on X₂. Interpretation: log-odds change per X₁ varies with X₂. Test: likelihood ratio test comparing with and without interaction. Visualise: plot probability vs X₁ at different X₂ levels.

---

## Part C: Discriminant Analysis & Naive Bayes (Q21-30)

### Q21. Describe Linear Discriminant Analysis (LDA).
**Model answer:** Generative classifier. Assumes X|Y = k ~ N(μ_k, Σ) (common covariance Σ). By Bayes: P(Y = k|X) ∝ π_k N(X; μ_k, Σ). Log-posterior linear in X — linear decision boundary. Estimates μ_k, Σ, π_k from data.

### Q22. Derive LDA decision rule.
**Model answer:** P(Y = k|X) ∝ π_k exp(−½(x−μ_k)'Σ⁻¹(x−μ_k)). Log: log π_k − ½(x−μ_k)'Σ⁻¹(x−μ_k). Difference between class discriminants is linear in x (quadratic terms cancel due to common Σ). Classify to class with highest linear discriminant score.

### Q23. Describe Quadratic Discriminant Analysis (QDA).
**Model answer:** Each class has its own covariance Σ_k. Decision boundary quadratic. Log-posterior: log π_k − ½log|Σ_k| − ½(x−μ_k)'Σ_k⁻¹(x−μ_k). More flexible than LDA; captures different class structures. Requires more parameters — more data needed.

### Q24. When does LDA outperform QDA?
**Model answer:** (1) Classes have similar covariance structures. (2) Training data is limited (QDA overparameterised). (3) Fewer class-specific covariance parameters to estimate → lower variance. LDA is preferred default unless strong evidence of different covariances.

### Q25. Describe Naive Bayes classifier.
**Model answer:** Assumes features X_j are conditionally independent given class: P(X|Y) = Π P(X_j|Y). Greatly simplifies: P(Y=k|X) ∝ π_k Π P(X_j|Y=k). Models each P(X_j|Y) individually (Gaussian, multinomial, etc.). Works well despite "naive" assumption.

### Q26. Why does Naive Bayes work despite violating independence?
**Model answer:** Two reasons: (1) Even if probabilities are miscalibrated, argmax of P(Y|X) often correct. (2) High-dimensional spaces favour simple models. Applications where it excels: text classification, spam detection. Fast, interpretable, requires minimal data.

### Q27. Describe Gaussian Naive Bayes.
**Model answer:** Continuous features with P(X_j|Y = k) ~ N(μ_{jk}, σ²_{jk}). Estimate means and variances separately per class. Classification: product of Gaussian densities × prior, pick max. Fast; competitive with more complex methods on many datasets.

### Q28. Describe Multinomial Naive Bayes.
**Model answer:** For text (bag-of-words): X_j = count of word j. P(X|Y) ~ Multinomial. Estimate P(word_j | class_k) from training data. Smoothing (Laplace/Lidstone) for unseen words. Standard for text classification. Extension: TF-IDF weighting.

### Q29. Compare LDA, QDA, and Naive Bayes.
**Model answer:** LDA: generative, shared covariance, moderate flexibility. QDA: generative, class-specific covariance, flexible. Naive Bayes: generative, assumes feature independence, fastest, robust to high dimensionality. Choice: LDA default; QDA if covariances differ; Naive Bayes if many features or text data.

### Q30. State the assumption tests for LDA.
**Model answer:** (1) Multivariate normality of X within classes. (2) Equal covariance matrices (Box's M test). (3) Independence of observations. (4) Absence of outliers (LDA sensitive). Violations: use robust estimators, transformations, or QDA (for covariance inequality). Small violations often don't harm performance.

---

## Part D: Support Vector Machines (Q31-40)

### Q31. Describe the Support Vector Machine (SVM).
**Model answer:** Finds hyperplane maximising margin between classes. For linearly separable data: w·x + b = 0 with max margin to nearest points (support vectors). Decision: sign(w·x + b). For non-separable: soft margin with slack variables.

### Q32. State the SVM optimisation problem.
**Model answer:** Minimise ½||w||² + C Σξ_i subject to y_i(w·x_i + b) ≥ 1 − ξ_i, ξ_i ≥ 0. C is regularisation parameter: large C = hard margin (may overfit); small C = soft margin (may underfit). Dual form uses Lagrangian, allows kernel trick.

### Q33. What is the kernel trick?
**Model answer:** Allows SVMs to find non-linear decision boundaries. Replace inner product x_i · x_j with kernel K(x_i, x_j), implicitly mapping to high-dimensional space. Common kernels: linear, polynomial, Radial Basis Function (RBF), sigmoid. Avoids explicitly computing high-dimensional features.

### Q34. Describe the Radial Basis Function (RBF) kernel.
**Model answer:** K(x, x') = exp(−γ||x − x'||²). Creates smooth non-linear decision boundaries. Hyperparameter γ controls flexibility: large γ = local, wiggly; small γ = global, smoother. Widely used — excellent default for SVM. Tune γ and C via cross-validation.

### Q35. What are support vectors?
**Model answer:** Training points lying on or within the margin — they determine the decision boundary. Only support vectors influence the solution; other points could be removed without affecting the classifier. Typically a small fraction of data — efficient memory usage at prediction time.

### Q36. Compare SVM and logistic regression.
**Model answer:** SVM: margin-based; no probability outputs directly (need Platt scaling); better for small/medium data; kernel trick for non-linearity. Logistic: probabilistic outputs; efficient on large data; no direct non-linearity (but can add polynomial features). Often similar performance; SVM historically preferred in image/bioinformatics.

### Q37. Describe kernel regression and SVR.
**Model answer:** Support Vector Regression (SVR) extends SVM to regression. Uses ε-insensitive loss: predictions within ε of actual have zero loss. Margins around the regression line. RBF kernels give non-linear regression. Hyperparameters: C (regularisation), ε (margin width), γ (kernel).

### Q38. State the effect of C hyperparameter in SVM.
**Model answer:** C controls trade-off between margin width and classification errors on training set. Large C: narrow margin, few training errors (overfitting risk). Small C: wide margin, more training errors (underfitting risk). Tune via cross-validation; common range 0.01 to 100.

### Q39. Describe multiclass SVM.
**Model answer:** SVM naturally binary. Multiclass: (1) One-vs-rest (OvR): train K binary classifiers. Class with highest margin wins. (2) One-vs-one (OvO): train K(K−1)/2 pairwise classifiers; voting determines class. (3) Specialised multiclass (Crammer-Singer). OvO more common; more classifiers but smaller training sets each.

### Q40. When to choose SVM over other classifiers?
**Model answer:** (1) Medium-sized data (thousands, not millions). (2) Clear margin between classes. (3) High-dimensional feature spaces (especially with kernels). (4) Text classification (linear SVM). Avoid: (1) Very large data (computationally expensive). (2) Want probability estimates (requires post-processing). (3) Need interpretability.

---

## Part E: Evaluation (Q41-45)

### Q41. State cross-validation strategies for classification.
**Model answer:** (1) Stratified k-fold: maintains class proportions in each fold — essential for imbalanced data. (2) Leave-one-out: unbiased but high variance. (3) Stratified shuffle split. (4) Time-aware CV for temporal data (no shuffling). Choose stratified k-fold by default.

### Q42. Describe the F1 score.
**Model answer:** F1 = 2 · (Precision · Recall)/(Precision + Recall). Harmonic mean — penalises imbalance between precision and recall. Range [0, 1]. Used when both precision and recall matter (binary classification with imbalanced classes). F2 weights recall higher; F0.5 weights precision higher.

### Q43. What is a learning curve?
**Model answer:** Plot training and validation error vs training set size. Reveals: (1) High bias: both errors plateau high — need complex model. (2) High variance: large gap between training (low) and validation (high) — need more data or regularisation. Guides next steps.

### Q44. Describe AUC as a performance metric.
**Model answer:** Area Under ROC Curve. Probability that model ranks a random positive higher than a random negative. Invariant to threshold. AUC > 0.8 good, > 0.9 excellent. Used for: (1) Threshold-independent comparison. (2) Imbalanced data. (3) Ranking applications (recommendations). Limitation: can hide local patterns.

### Q45. What are calibration plots?
**Model answer:** Plot predicted probabilities vs actual frequencies in bins. Well-calibrated model: points on 45° line (predicted 0.7 → actual rate 70%). Miscalibrated: systematic deviation. Fix: Platt scaling or isotonic regression. Important for decision-making based on probabilities (e.g., threshold-based actions).

---

## Part F: Application (Q46-50)

### Q46. A credit card fraud detection task has 0.1% fraud rate. Design a classifier.
**Model answer:** (1) Highly imbalanced — accuracy misleading. Use AUPR, F1, or cost-sensitive loss. (2) Strategies: SMOTE oversampling, class weights, anomaly detection frameworks. (3) Try: logistic regression baseline, random forest, gradient boosting, neural networks. (4) Threshold tuning: if false negatives (missed fraud) costly, use low threshold. (5) Cross-validate with stratified k-fold. (6) Evaluate on confusion matrix, AUPR. (7) Monitor production model for drift.

### Q47. Email spam classifier: step-by-step.
**Model answer:** (1) Data collection: labelled spam/ham corpus. (2) Preprocessing: tokenise, lowercase, remove stopwords, stem/lemmatise. (3) Feature engineering: TF-IDF or word embeddings. (4) Baseline: Multinomial Naive Bayes. (5) Try logistic regression and linear SVM. (6) Evaluate on held-out set via AUC and F1. (7) Tune threshold based on cost of false positives (legitimate emails marked spam costs user). (8) Deploy with spam filter rules. (9) Monitor and retrain.

### Q48. Choose between logistic regression and random forest for customer churn.
**Model answer:** Logistic regression: (1) Interpretable coefficients — know why customers churn. (2) Fast training/prediction. (3) Probability outputs calibrated. (4) Good baseline. Random forest: (1) Higher accuracy typically. (2) Captures non-linear relationships and interactions automatically. (3) Feature importance available. (4) Less preprocessing needed. Recommendation: start LR for interpretation; compare with RF; use RF if accuracy gain is substantial and interpretation sacrificed.

### Q49. Your SVM has 95% CV accuracy but 70% on test set. Diagnose.
**Model answer:** Significant gap — overfitting or data leakage. Investigate: (1) Was CV done correctly? Did folds respect temporal/group structure? (2) Is test set from same distribution? (3) Hyperparameter tuning on CV might have overfit — use nested CV. (4) Check regularisation (C): if C is very large, SVM memorising training. (5) Feature leakage: features may contain information about test labels. Actions: reduce model complexity; re-split data properly; verify CV procedure.

### Q50. Compare a complete classification pipeline.
**Model answer:** Starting from raw data: (1) Exploratory analysis — class balance, feature distributions. (2) Preprocessing — handle missing, encode categorical, scale. (3) Train-test split (stratified). (4) Baseline model (majority class predictor). (5) Multiple models: logistic regression, LDA, random forest, SVM. (6) Cross-validation for hyperparameter tuning. (7) Compare CV metrics: accuracy, F1, AUC. (8) Final model evaluation on test set. (9) Calibration if probabilities needed. (10) Error analysis — which classes are confused? (11) Deployment with monitoring. (12) Retraining schedule as new data arrives.

---

**Exam tip:** For classification questions, always: (1) identify binary vs multiclass, (2) choose metric appropriate for class balance (F1, AUC, AUPR over accuracy when imbalanced), (3) stratified CV for model selection, (4) compare multiple algorithms, (5) address class imbalance explicitly (SMOTE, weights, threshold), (6) report confusion matrix and calibration.
