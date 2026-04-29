# ST3189 — Intro ML, Linear Regression & Bayesian Inference: 50 Exam Questions with Model Answers

---

## Part A: ML Fundamentals (Q1-10)

### Q1. Define machine learning.
**Model answer:** Algorithms that learn patterns from data to make predictions or decisions. Includes supervised (labelled outputs), unsupervised (no labels, find structure), reinforcement (learn from rewards), semi-supervised. Emphasises predictive accuracy over interpretability.

### Q2. Distinguish supervised and unsupervised learning.
**Model answer:** Supervised: data includes labels (y_i). Methods: regression, classification. Goal: predict y from x. Unsupervised: no labels. Methods: clustering, PCA, association rules. Goal: discover structure. Semi-supervised: some labels, most unlabelled — intermediate.

### Q3. Define training, validation, and test sets.
**Model answer:** Training: data used to fit parameters. Validation: used to select hyperparameters (e.g., regularisation strength, tree depth). Test: held out until the end; used once for final evaluation. Prevents overfitting to decisions. Typical split: 60-20-20 or 70-15-15.

### Q4. State the bias-variance trade-off.
**Model answer:** Expected prediction error = Bias² + Variance + Irreducible Error. Bias: systematic error from model simplicity. Variance: error from sensitivity to training data. Complex models: low bias, high variance. Simple models: high bias, low variance. Optimal complexity minimises total error.

### Q5. Describe overfitting.
**Model answer:** Model fits training data too closely — memorises noise, not just signal. Training error very low; test error high. Causes: too many parameters, insufficient regularisation, small training data. Diagnostic: gap between training and test performance. Cure: regularisation, cross-validation, more data.

### Q6. Describe underfitting.
**Model answer:** Model too simple to capture underlying pattern. Both training and test error high. Causes: insufficient features, overly restrictive functional form, too much regularisation. Cure: more features, flexible models, less regularisation.

### Q7. Describe k-fold cross-validation.
**Model answer:** Partition training data into k roughly equal folds. For each fold: train on k−1 folds, evaluate on held-out fold. Average the k errors. Common: k = 5 or 10. Trade-off: more folds → less bias, more computation. LOOCV is k = n.

### Q8. What is a loss function?
**Model answer:** Function measuring error between predicted and true values. Regression: squared loss (y − ŷ)², absolute loss |y − ŷ|. Classification: 0-1 loss, log-loss. Training minimises empirical average loss. Choice affects what model optimises.

### Q9. Define generalisation.
**Model answer:** Ability of a model to perform well on new, unseen data. Goal of ML. Generalisation error: expected loss on new data. Training error ≠ generalisation error. Good generalisation: small gap between training and test performance.

### Q10. Describe the no free lunch theorem.
**Model answer:** No single ML algorithm is best for all problems. Different problems require different models. Implications: (1) Try multiple methods. (2) Domain knowledge matters. (3) Don't chase universal "best" algorithm. Tailoring methods to data characteristics is essential.

---

## Part B: Linear Regression in ML (Q11-20)

### Q11. State the linear regression model and OLS.
**Model answer:** y = Xβ + ε. OLS: β̂ = (X'X)⁻¹X'y minimises Σ(y_i − x_i'β)². Solution requires (X'X) non-singular. Predictions: ŷ = Xβ̂ = X(X'X)⁻¹X'y = Py, where P is the projection matrix.

### Q12. Why is R² not sufficient for evaluating ML models?
**Model answer:** R² measures fit to training data. Adding predictors always increases R² (can't decrease SSE). Doesn't penalise complexity. Doesn't measure out-of-sample performance. Better: (1) Adjusted R². (2) Cross-validated R². (3) Information criteria. (4) Held-out test performance.

### Q13. Describe ridge regression.
**Model answer:** L2 regularisation: minimise Σ(y − x'β)² + λ Σβ². Shrinks coefficients toward zero but rarely exactly to zero. Closed-form: β̂_ridge = (X'X + λI)⁻¹X'y. Hyperparameter λ selected via CV. Handles multicollinearity; all variables retained.

### Q14. Describe LASSO regression.
**Model answer:** L1 regularisation: minimise Σ(y − x'β)² + λ Σ|β|. L1 penalty produces exactly zero coefficients — automatic variable selection. No closed form; optimisation via coordinate descent or LARS. λ chosen by CV. Sparse solutions interpretable.

### Q15. Compare ridge and LASSO.
**Model answer:** Ridge: shrinks all coefficients, retains all variables. Best when many small effects. LASSO: selects and shrinks, produces sparse solutions. Best when few important variables. Elastic Net: α·L1 + (1−α)·L2 combines both.

### Q16. When should you use LASSO for variable selection?
**Model answer:** (1) High-dimensional data (p approaches or exceeds n). (2) Want to identify subset of important predictors. (3) Interpretability matters. (4) Many correlated predictors. Limitations: LASSO arbitrary picks one variable from group of correlated ones; unstable selection across samples.

### Q17. Describe elastic net regression.
**Model answer:** Minimises Σ(y − x'β)² + λ[(1−α)·Σβ² + α·Σ|β|]. α ∈ [0, 1] controls mix: α = 0 ridge, α = 1 LASSO. Preferred when correlated predictors present — LASSO picks one randomly, elastic net keeps all but shrinks.

### Q18. State the bias-variance decomposition for regression.
**Model answer:** E[(y − ŷ)²] = (Bias)² + Variance + σ². Where Bias = E(ŷ) − y_true; Variance = E[(ŷ − E(ŷ))²]; σ² = irreducible noise. Optimal complexity minimises total. OLS: low bias, potentially high variance. Ridge/LASSO: some bias for lower variance.

### Q19. Why can't bias and variance both be zero?
**Model answer:** Constraints on model complexity force trade-off. Low bias → fit training data closely → high variance (sensitive to training sample). Low variance → stable predictions → may miss true patterns (high bias). Exception: unlimited data and perfect model — impractical.

### Q20. How does sample size affect bias and variance?
**Model answer:** Larger n reduces variance (more data, stable estimates). Doesn't directly affect bias — that depends on model specification. So with n → ∞, variance → 0, bias persists. Small n: may appear like high variance; actually inability to distinguish signal from noise.

---

## Part C: Bayesian Inference (Q21-35)

### Q21. State Bayes' theorem for inference.
**Model answer:** P(θ|data) = P(data|θ) · P(θ) / P(data). Posterior ∝ Likelihood × Prior. Updates beliefs about parameters based on observed data. P(data) normalises the posterior. Core of Bayesian statistics — "rational belief update".

### Q22. Define prior, likelihood, and posterior.
**Model answer:** Prior P(θ): belief about parameters before seeing data. Likelihood P(data|θ): probability of data given parameters. Posterior P(θ|data): updated belief after seeing data. Posterior combines prior and data; fully summarises uncertainty about θ.

### Q23. Compare Bayesian and frequentist inference.
**Model answer:** Frequentist: parameter θ is fixed unknown; data is random. Uses sampling distributions, p-values, CIs. Bayesian: θ is random (has distribution). Updates via Bayes. Produces probability statements about θ. Different philosophies; sometimes converge in large samples.

### Q24. What is a conjugate prior?
**Model answer:** Prior that yields posterior in the same family. Example: for normal likelihood with known σ², normal prior gives normal posterior. Analytically tractable, computationally cheap. Common pairs: Beta-Binomial, Dirichlet-Multinomial, Normal-Normal, Gamma-Poisson.

### Q25. Derive the posterior for normal data with normal prior.
**Model answer:** Data: y_i ~ N(μ, σ²) iid, n observations. Prior: μ ~ N(μ₀, τ₀²). Posterior: μ|y ~ N(μ_n, τ_n²) where τ_n² = (1/τ₀² + n/σ²)⁻¹ and μ_n = τ_n²(μ₀/τ₀² + nȳ/σ²). Posterior mean = weighted average of prior mean and sample mean, weights proportional to precisions.

### Q26. Describe a credible interval.
**Model answer:** Bayesian analogue of CI. 95% credible interval: P(θ ∈ [a, b] | data) = 0.95. Direct probability statement about θ (unlike frequentist CI). Computed from posterior distribution. For symmetric posteriors, central 95% equivalent to HPD interval.

### Q27. State the posterior for Beta-Binomial model.
**Model answer:** Data: x successes in n trials, likelihood ~ Binomial. Prior: p ~ Beta(α, β). Posterior: p | x ~ Beta(α + x, β + n − x). Beta is conjugate for Binomial. Posterior mean: (α + x)/(α + β + n) — weighted average of prior mean α/(α+β) and sample proportion x/n.

### Q28. What is a non-informative (flat) prior?
**Model answer:** Prior that conveys minimal information — aims to let data dominate. Examples: uniform on parameter space. Issues: (1) Not always proper (integrates to ∞). (2) Changes under reparameterisation (Jeffreys prior invariant). (3) In large samples, posterior dominated by likelihood, so non-informative prior acceptable.

### Q29. Describe the Jeffreys prior.
**Model answer:** π(θ) ∝ √|I(θ)|, where I is Fisher information. Invariant under reparameterisation — key advantage over flat priors. Examples: Jeffreys for binomial p is Beta(0.5, 0.5). Principled "non-informative" choice; often improper but yields proper posteriors.

### Q30. What is the posterior predictive distribution?
**Model answer:** P(y_new | y_obs) = ∫ P(y_new | θ) · P(θ | y_obs) dθ. Distribution of new observation given data — marginalises over posterior uncertainty. More conservative (wider) than plug-in prediction using θ̂_posterior.

### Q31. Describe maximum a posteriori (MAP) estimation.
**Model answer:** θ̂_MAP = argmax P(θ | data) = argmax [P(data | θ) · P(θ)]. Mode of posterior. Point estimate. Equivalent to penalised maximum likelihood with penalty = negative log prior. Ridge regression = MAP with normal prior; LASSO = MAP with Laplace prior.

### Q32. What is Markov Chain Monte Carlo (MCMC)?
**Model answer:** Methods to sample from complex posteriors when analytical solution intractable. Construct Markov chain whose stationary distribution = target posterior. Algorithms: Metropolis-Hastings, Gibbs sampling. Produces correlated samples. Requires convergence diagnostics.

### Q33. Describe Gibbs sampling.
**Model answer:** MCMC method: cycle through each parameter, sampling from its conditional posterior given others. Requires knowing conditionals (often tractable in conjugate models). Advantages: simple, widely applicable. Limitations: sensitive to parameterisation; slow mixing for correlated parameters.

### Q34. Describe the Metropolis-Hastings algorithm.
**Model answer:** (1) Start at θ_t. (2) Propose θ* from q(·|θ_t). (3) Accept θ* with probability min(1, π(θ*)q(θ_t|θ*) / [π(θ_t)q(θ*|θ_t)]). (4) If accept: θ_{t+1} = θ*; else θ_{t+1} = θ_t. Stationary distribution: π (target). Very general — works even with unknown normalising constant.

### Q35. What is credible interval vs confidence interval?
**Model answer:** Credible interval: Bayesian; P(θ ∈ [a,b] | data) = 0.95. θ is random; interval is fixed. Confidence interval: Frequentist; 95% of intervals constructed this way contain θ. θ is fixed; interval is random. Different interpretations despite similar names.

---

## Part D: Numerical Problems (Q36-45)

### Q36. Given prior Beta(2, 3), observed 8 successes in 12 trials. Find posterior.
**Model answer:** Beta-Binomial conjugacy: posterior = Beta(2 + 8, 3 + 12 − 8) = Beta(10, 7). Posterior mean = 10/17 = 0.588. Prior mean = 2/5 = 0.4. Sample proportion = 8/12 = 0.667. Posterior balances both, closer to data due to larger sample.

### Q37. Linear regression with ridge λ = 1, OLS β̂ = 5. Compute ridge estimate if X'X = 4.
**Model answer:** β̂_ridge = (X'X + λ)⁻¹ X'y. Using OLS form: β̂_OLS = (X'X)⁻¹ X'y = 5, so X'y = 5(X'X) = 20. β̂_ridge = (4 + 1)⁻¹ × 20 = 4. Ridge shrinks from 5 to 4 — 20% reduction.

### Q38. OLS MSE = 4.0; ridge MSE = 3.5. Evaluate.
**Model answer:** Ridge outperforms by MSE. Bias-variance trade: ridge introduces slight bias, substantial variance reduction. Net: lower total error. Report with CV: is 3.5 stable across folds? Apply ridge to new data. Check coefficient shrinkage — some variables heavily affected suggest strong regularisation benefit.

### Q39. CV MSE at λ = 0.01, 0.1, 1.0, 10: 2.1, 1.8, 1.9, 2.5. Choose λ.
**Model answer:** Minimum at λ = 0.1 (MSE = 1.8). This is optimal regularisation strength. λ too small (0.01) = close to OLS, overfitting. λ too large (10) = too much shrinkage, underfitting. 1-SE rule: could choose λ = 1.0 for parsimony if MSE difference (1.9 vs 1.8) within standard error.

### Q40. Prior N(0, 4), data N(y|μ, 1), sample mean ȳ = 3, n = 10. Find posterior.
**Model answer:** τ₀² = 4, σ² = 1, n = 10, μ₀ = 0. τ_n² = (1/4 + 10)⁻¹ = 0.0976. μ_n = 0.0976 × (0/4 + 10·3/1) = 0.0976 × 30 = 2.93. Posterior ~ N(2.93, 0.0976). Posterior concentrated near sample mean; prior pulled slightly toward 0.

### Q41. Posterior P(θ = 0.5 | data) = 0.82. Interpret.
**Model answer:** Given the data, there is an 82% probability that θ = 0.5. Direct probability statement about parameter (unlike frequentist). High credibility for specific value — data strongly supports H: θ = 0.5. Report with broader credible interval for context.

### Q42. 95% credible interval = [2.5, 4.0]. Interpret.
**Model answer:** Given observed data, probability that θ lies in [2.5, 4.0] is 0.95. Valid probability statement about θ. If critical value θ₀ = 3 falls inside, consistent with H: θ = 3. Difference from frequentist CI: direct probability interpretation.

### Q43. MAP estimate = 2.3; posterior mean = 2.5. Interpret discrepancy.
**Model answer:** MAP: mode of posterior. Mean: expected value. Differ when posterior is asymmetric (skewed). MAP is like classical point estimator; mean is optimal under squared error loss. Report both + credible interval. Difference suggests non-normal posterior — visualise with histogram.

### Q44. Posterior predictive interval for y_new: [50, 150]. Interpret.
**Model answer:** For a new observation, 95% probability it lies in [50, 150]. Wider than credible interval for mean — includes both parameter uncertainty AND residual variability of individual observation. Appropriate for individual predictions. Use for prediction; use credible interval for mean.

### Q45. Bayesian model comparison: Bayes factor = 10. Interpret.
**Model answer:** Model 1 is 10 times more supported by data than Model 2. Evidence thresholds: 3-10 moderate, 10-30 strong, > 100 decisive. Report with Bayes factor and prior model probabilities. Posterior odds = Bayes factor × prior odds.

---

## Part E: Application and Extension (Q46-50)

### Q46. Compare OLS and Bayesian regression for predicting house prices.
**Model answer:** OLS: point estimate of β with frequentist CI; no uncertainty about model. Bayesian: posterior over β capturing uncertainty; prior encodes knowledge (e.g., size should matter). Advantages Bayesian: (1) Incorporates prior knowledge. (2) Full uncertainty quantification. (3) Posterior predictive intervals. (4) Easy to combine multiple datasets. Drawbacks: prior choice, computation.

### Q47. Design a Bayesian analysis to test if a coin is fair.
**Model answer:** (1) Model: x ~ Binomial(n, p). (2) Prior: p ~ Beta(1, 1) (uniform, uninformative). (3) Observe 60 heads in 100 flips. (4) Posterior: p | x ~ Beta(1 + 60, 1 + 40) = Beta(61, 41). (5) Posterior mean = 61/102 = 0.598. (6) 95% CI: approximately [0.50, 0.69]. (7) P(p > 0.5 | data) using posterior CDF. (8) Compare Bayes factor vs frequentist p-value. Conclusion: moderate evidence against fairness.

### Q48. How does Bayesian inference handle small samples?
**Model answer:** Prior regularises estimates — provides shrinkage toward reasonable values when data scarce. Avoids extreme MLE estimates in small samples. Produces proper CIs via posterior (no asymptotic approximations). Examples: zero successes with flat prior gives proper posterior, unlike frequentist (0/n = 0 with no uncertainty). Valuable for rare events, small clinical trials.

### Q49. Compare ridge regression and Bayesian regression with normal prior.
**Model answer:** Mathematically equivalent: ridge is MAP under normal prior with variance 1/λ. Same point estimate. Different interpretation: ridge is penalised optimisation; Bayesian gives full posterior (uncertainty quantification). Bayesian advantage: credible intervals, model averaging, handles missing data naturally. Choose: ridge for prediction; Bayesian for inference + uncertainty.

### Q50. Describe a complete Bayesian analysis pipeline.
**Model answer:** (1) Specify model: likelihood P(data|θ). (2) Choose prior P(θ) — informative if justified, non-informative otherwise. (3) Derive or approximate posterior: analytical (conjugate), numerical (MCMC), variational. (4) Diagnose convergence (trace plots, Rhat for MCMC). (5) Summarise: posterior mean, credible interval, predictive distribution. (6) Model checking: posterior predictive checks, cross-validation. (7) Compare models: Bayes factor, LOOIC, WAIC. (8) Sensitivity analysis: vary prior. (9) Report prior, data, posterior, and conclusions.

---

**Exam tip:** For Bayesian questions on ST3189, always: (1) write Bayes' theorem with proper notation, (2) show prior and likelihood explicitly, (3) derive posterior step-by-step if analytical, (4) interpret posterior probabilistically (not frequentist), (5) provide credible interval alongside point estimate, (6) discuss prior sensitivity where relevant. Bayesian inference is a 25-mark question EVERY year — master the conjugate derivations.
