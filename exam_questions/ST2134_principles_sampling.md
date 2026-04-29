# ST2134 — Principles of Sampling: 50 Exam Questions with Model Answers

---

## Part A: Fundamentals of Sampling (Q1-10)

### Q1. Define a random sample.
**Model answer:** A random sample X₁, X₂, ..., Xₙ is a collection of random variables that are (i) independent and (ii) identically distributed (iid), drawn from a population with some distribution F. "iid" means: independent — outcomes of one Xᵢ don't affect others; identically distributed — all Xᵢ have the same distribution F.

### Q2. Define the sampling distribution of a statistic.
**Model answer:** The probability distribution of a statistic T = T(X₁, ..., Xₙ) computed from all possible samples of size n drawn from the population. Describes how T varies across repeated random samples. Fundamental for inference: the distribution of T determines standard errors, critical values, and p-values.

### Q3. Define a statistic.
**Model answer:** Any function of the sample that does not depend on unknown parameters: T = T(X₁, X₂, ..., Xₙ). Examples: X̄ (sample mean), s² (sample variance), max(Xᵢ). A statistic is a random variable itself. Contrasts with a parameter θ which is a fixed (but possibly unknown) feature of the population.

### Q4. Distinguish population and sample.
**Model answer:** Population: the complete collection of units about which we seek inference. Characterised by parameters (μ, σ², etc.) — fixed but usually unknown. Sample: a subset of the population actually observed. Characterised by statistics (X̄, s², etc.) — computed from data, used to estimate parameters.

### Q5. State the expectation of a linear combination of random variables.
**Model answer:** E(aX + bY + c) = aE(X) + bE(Y) + c. Linearity — does not require independence. General form: E(Σ aᵢXᵢ) = Σ aᵢE(Xᵢ). Used to derive E(X̄) = μ.

### Q6. State the variance of a sum of independent random variables.
**Model answer:** For independent X, Y: Var(X + Y) = Var(X) + Var(Y). More generally, Var(aX + bY) = a²Var(X) + b²Var(Y). If X and Y are dependent: add 2ab·Cov(X, Y). Requires independence for the simpler form.

### Q7. State and derive E(X̄) and Var(X̄) for a random sample.
**Model answer:** X₁, ..., Xₙ iid with E(Xᵢ) = μ, Var(Xᵢ) = σ². E(X̄) = E((1/n)Σ Xᵢ) = (1/n) Σ E(Xᵢ) = (1/n)(nμ) = μ. Var(X̄) = (1/n²)Σ Var(Xᵢ) = (1/n²)(nσ²) = σ²/n. Standard error: SE(X̄) = σ/√n.

### Q8. State the Central Limit Theorem.
**Model answer:** Let X₁, X₂, ..., Xₙ be iid with E(Xᵢ) = μ and Var(Xᵢ) = σ² < ∞. Then as n → ∞, (X̄ − μ)/(σ/√n) →_d N(0, 1). Equivalently, X̄ is approximately N(μ, σ²/n) for large n. Remarkably, this holds regardless of the parent distribution F (given finite variance).

### Q9. State the Weak Law of Large Numbers.
**Model answer:** Let X₁, ..., Xₙ be iid with E(Xᵢ) = μ. Then X̄ →_p μ: for any ε > 0, P(|X̄ − μ| > ε) → 0 as n → ∞. Sample mean converges in probability to the population mean. Justifies using X̄ to estimate μ for large samples.

### Q10. State the Strong Law of Large Numbers.
**Model answer:** Under conditions of WLLN plus independence: X̄ →_{a.s.} μ. "Almost sure" convergence: P(lim_{n→∞} X̄ = μ) = 1. Stronger than WLLN (which is convergence in probability). Implication: with probability 1, the sample mean converges to μ for large enough n.

---

## Part B: Standard Sample Statistics (Q11-20)

### Q11. Define the sample mean and its estimator property.
**Model answer:** X̄ = (1/n) Σ Xᵢ. Unbiased estimator of μ: E(X̄) = μ. Variance: Var(X̄) = σ²/n → 0 as n → ∞. Consistent estimator. BLUE (Best Linear Unbiased Estimator) under standard assumptions.

### Q12. Define the sample variance and its estimator property.
**Model answer:** s² = (1/(n−1)) Σ(Xᵢ − X̄)². Unbiased estimator of σ²: E(s²) = σ². The divisor n−1 (not n) compensates for the loss of one degree of freedom in computing X̄. The biased version (divide by n) is the MLE under normality.

### Q13. Derive why s² uses n−1 in the denominator.
**Model answer:** E[Σ(Xᵢ − X̄)²] = Σ E[(Xᵢ − μ)²] − n · E[(X̄ − μ)²] = nσ² − n(σ²/n) = (n−1)σ². So E[Σ(Xᵢ − X̄)²/(n−1)] = σ². Dividing by n instead of n−1 would give E(s²) = σ²(n−1)/n < σ² — biased downward.

### Q14. State the distribution of (n−1)s²/σ² under normality.
**Model answer:** If X₁, ..., Xₙ iid N(μ, σ²), then (n−1)s²/σ² ~ χ²(n−1). Key result: sample variance from normal data follows scaled chi-squared distribution with n−1 degrees of freedom. Foundation for CIs and tests of variance.

### Q15. State the independence of X̄ and s² under normality.
**Model answer:** If X₁, ..., Xₙ iid N(μ, σ²), then X̄ and s² are independent. This is a special property of the normal distribution (Basu's theorem). Consequence: Cov(X̄, s²) = 0; t-statistic (X̄ − μ)/(s/√n) has well-defined t-distribution.

### Q16. Derive the t-statistic distribution.
**Model answer:** Under normality: Z = (X̄ − μ)/(σ/√n) ~ N(0,1). V = (n−1)s²/σ² ~ χ²(n−1), independent of Z. By definition: T = Z/√(V/(n−1)) = (X̄ − μ)/(s/√n) ~ t(n−1). Student's t with n−1 degrees of freedom.

### Q17. Describe the sample proportion.
**Model answer:** p̂ = X/n = Σ Xᵢ/n, where Xᵢ ~ Bernoulli(p). E(p̂) = p, Var(p̂) = p(1−p)/n. By CLT: for large n, p̂ ≈ N(p, p(1−p)/n). Used for inference on proportions — CIs, hypothesis tests.

### Q18. State the convergence in distribution definition.
**Model answer:** X_n →_d X if F_{X_n}(x) → F_X(x) at every continuity point of F_X. Weaker than convergence in probability. Key for CLT and asymptotic inference. Also called "weak convergence" or "convergence in law".

### Q19. Define convergence in probability.
**Model answer:** X_n →_p X if for every ε > 0: P(|X_n − X| > ε) → 0 as n → ∞. Stronger than convergence in distribution when X is constant. Key for consistency of estimators — X̄ →_p μ.

### Q20. State the continuous mapping theorem.
**Model answer:** If X_n →_d X (or →_p X), and g is a continuous function, then g(X_n) →_d g(X) (or →_p g(X)). Allows deriving asymptotic distributions of transformed statistics. Example: (X̄ − μ)²/(σ²/n) →_d χ²(1).

---

## Part C: Independence and Joint Distributions (Q21-30)

### Q21. Define independence of random variables.
**Model answer:** X and Y are independent if their joint CDF factorises: F(x, y) = F_X(x) · F_Y(y). Equivalently, joint PDF: f(x, y) = f_X(x) · f_Y(y). Equivalently: P(X ∈ A, Y ∈ B) = P(X ∈ A) P(Y ∈ B) for all A, B. Implies zero correlation but converse not necessarily true.

### Q22. Define a joint probability density function.
**Model answer:** For continuous X, Y: f(x, y) such that P((X, Y) ∈ A) = ∫∫_A f(x, y) dx dy. Marginal densities: f_X(x) = ∫ f(x, y) dy. Conditional density: f(y|x) = f(x, y)/f_X(x). Foundation for multivariate analysis.

### Q23. Derive marginal from joint distribution.
**Model answer:** f_X(x) = ∫ f(x, y) dy (continuous) or f_X(x) = Σ_y f(x, y) (discrete). "Integrate out" or "sum over" the other variable. Gives the distribution of X ignoring Y.

### Q24. Derive conditional from joint distribution.
**Model answer:** f(y|x) = f(x, y)/f_X(x), provided f_X(x) > 0. Conditional distribution of Y given X = x. Key result: marginal = Σ conditional × marginal of conditioning: f_Y(y) = ∫ f(y|x) f_X(x) dx.

### Q25. State the law of total expectation.
**Model answer:** E(Y) = E[E(Y|X)]. The unconditional expectation equals the average of conditional expectations. Powerful tool for deriving marginal moments when conditional distribution is known. Generalises to E[g(Y)] = E[E(g(Y)|X)].

### Q26. State the law of total variance.
**Model answer:** Var(Y) = E[Var(Y|X)] + Var[E(Y|X)]. Decomposes variance into (1) average within-group variance + (2) between-group variance of conditional means. Used in ANOVA-type decompositions and compound distributions.

### Q27. State the transformation theorem.
**Model answer:** If Y = g(X) where g is strictly monotonic and differentiable: f_Y(y) = f_X(g⁻¹(y)) · |dg⁻¹/dy|. For vector: Jacobian transformation. Used to derive distributions of functions of random variables.

### Q28. Describe the moment generating function (MGF).
**Model answer:** M_X(t) = E(e^{tX}) = ∫ e^{tx} f(x) dx. Moments from MGF: E(X^k) = M^{(k)}(0) (k-th derivative at 0). Uniqueness: MGF determines distribution. Sum of independent: M_{X+Y}(t) = M_X(t) M_Y(t). Useful for finding distributions and moments.

### Q29. Describe the characteristic function.
**Model answer:** φ_X(t) = E(e^{itX}). Complex-valued analog of MGF. Always exists (unlike MGF, which may not). Uniqueness holds: φ determines distribution. Convergence: if φ_{X_n}(t) → φ_X(t), then X_n →_d X (Lévy's continuity theorem). Theoretical workhorse for convergence.

### Q30. Describe the Cramér-Wold theorem.
**Model answer:** X_n →_d X if and only if t'X_n →_d t'X for every vector t. Reduces multivariate convergence to univariate — useful technical device. Used in proofs of multivariate CLT and other asymptotic results.

---

## Part D: Standard Distributions (Q31-40)

### Q31. Describe the uniform distribution.
**Model answer:** U(a, b): f(x) = 1/(b−a) for a ≤ x ≤ b, 0 otherwise. E(X) = (a+b)/2. Var(X) = (b−a)²/12. MGF: (e^{tb} − e^{ta})/(t(b−a)). Used as prior in Bayesian analysis, and as basis for simulation.

### Q32. Describe the exponential distribution.
**Model answer:** Exp(λ): f(x) = λe^{−λx} for x ≥ 0. E(X) = 1/λ. Var(X) = 1/λ². Memoryless: P(X > s+t | X > s) = P(X > t). Models waiting times. MGF: λ/(λ−t) for t < λ.

### Q33. Describe the gamma distribution.
**Model answer:** Gamma(α, β): f(x) = β^α x^{α−1} e^{−βx}/Γ(α). E(X) = α/β. Var(X) = α/β². Generalises exponential (α = 1) and chi-squared (α = k/2, β = 1/2 gives χ²(k)). Sum of α independent Exp(β) is Gamma(α, β).

### Q34. Describe the beta distribution.
**Model answer:** Beta(α, β): f(x) = x^{α−1}(1−x)^{β−1}/B(α,β) for x ∈ [0, 1]. E(X) = α/(α+β). Var(X) = αβ/[(α+β)²(α+β+1)]. Models probabilities; conjugate prior for Binomial. α = β = 1 gives Uniform(0,1).

### Q35. Describe the chi-squared distribution.
**Model answer:** χ²(k): sum of k independent squared standard normals. f(x) = x^{(k/2)−1} e^{−x/2}/(2^{k/2} Γ(k/2)). E(X) = k. Var(X) = 2k. Used in variance tests, goodness-of-fit, LR tests. Special case of Gamma.

### Q36. Describe the t-distribution.
**Model answer:** t(k): T = Z/√(V/k), where Z ~ N(0,1), V ~ χ²(k), independent. Symmetric, heavier tails than normal. E(T) = 0 (k > 1). Var(T) = k/(k−2) (k > 2). Approaches N(0,1) as k → ∞. Used in t-tests of means with unknown σ².

### Q37. Describe the F-distribution.
**Model answer:** F(m, n): F = (U/m)/(V/n), where U ~ χ²(m), V ~ χ²(n), independent. f(x) has complicated form. E(F) = n/(n−2) for n > 2. Used in variance ratio tests, ANOVA. F(1, n) = [t(n)]².

### Q38. Describe the Poisson distribution.
**Model answer:** Poisson(λ): P(X = k) = e^{−λ}λ^k/k! for k = 0, 1, 2, ... E(X) = λ. Var(X) = λ. Models rare event counts. Limit of Binomial(n, p) as n → ∞, np → λ. Sum of independent Poissons: Poisson(sum of rates).

### Q39. Describe the binomial distribution.
**Model answer:** Bin(n, p): P(X = k) = C(n,k) p^k (1−p)^{n−k} for k = 0, 1, ..., n. E(X) = np. Var(X) = np(1−p). Sum of n iid Bernoullis. Normal approximation valid when np ≥ 5 and n(1−p) ≥ 5.

### Q40. Describe the multinomial distribution.
**Model answer:** Generalisation of binomial to k categories. P(X₁ = n₁, ..., X_k = n_k) = (n!/Π n_i!) Π p_i^{n_i}, with Σn_i = n, Σp_i = 1. E(Xᵢ) = np_i. Var(Xᵢ) = np_i(1−p_i). Cov(Xᵢ, Xⱼ) = −np_ip_j (negative correlation).

---

## Part E: Asymptotic Results (Q41-45)

### Q41. State the Delta method.
**Model answer:** If √n(X̄_n − μ) →_d N(0, σ²) and g is differentiable at μ with g'(μ) ≠ 0, then √n(g(X̄_n) − g(μ)) →_d N(0, [g'(μ)]²σ²). Provides asymptotic distribution of transformed statistics. Key tool in maximum likelihood theory.

### Q42. Apply the Delta method to variance of a transformation.
**Model answer:** Example: if X̄ ~ N(μ, σ²/n), find asymptotic variance of g(X̄) = 1/X̄. g'(μ) = −1/μ². By delta method: Var(g(X̄)) ≈ (g'(μ))² Var(X̄) = (1/μ⁴)(σ²/n). Allows CIs for transformed parameters.

### Q43. State Slutsky's theorem.
**Model answer:** If X_n →_d X and Y_n →_p c (constant), then: (1) X_n + Y_n →_d X + c. (2) X_n Y_n →_d cX. (3) X_n/Y_n →_d X/c (for c ≠ 0). Combines convergence modes. Used extensively in deriving asymptotic distributions.

### Q44. Apply Slutsky's theorem to t-statistic.
**Model answer:** (X̄ − μ)/(s/√n) = [(X̄ − μ)/(σ/√n)] × [σ/s]. Numerator →_d N(0,1) by CLT. Denominator: σ/s →_p 1 by consistency (s →_p σ). By Slutsky: the ratio →_d N(0,1). So for large n, t-statistic is approximately standard normal.

### Q45. State the multivariate CLT.
**Model answer:** If X₁, X₂, ... are iid random vectors with mean μ and covariance Σ (finite), then √n(X̄_n − μ) →_d N(0, Σ) in the multivariate sense. Applications: joint asymptotic inference, multivariate hypothesis tests, maximum likelihood with multiple parameters.

---

## Part F: Application (Q46-50)

### Q46. Given n = 30 iid samples with sample mean X̄ = 7.2, s = 1.5, construct a 95% CI for μ.
**Model answer:** Under normality: t-interval. CI = X̄ ± t_{0.025, 29} · s/√n = 7.2 ± 2.045 · (1.5/√30) = 7.2 ± 2.045 · 0.274 = 7.2 ± 0.560 = [6.64, 7.76]. Assumes normality; holds approximately by CLT for n = 30.

### Q47. Show that X̄² is biased for μ² using E(X̄²) = Var(X̄) + [E(X̄)]².
**Model answer:** E(X̄²) = Var(X̄) + μ² = σ²/n + μ². So X̄² overestimates μ² by σ²/n. Not unbiased (as expected — Jensen's inequality for convex g(x) = x²). Bias-corrected estimator: X̄² − s²/n is unbiased for μ² (assuming s² unbiased for σ²).

### Q48. Verify the variance formula for (n−1)s²/σ² ~ χ²(n−1).
**Model answer:** E(χ²(k)) = k and Var(χ²(k)) = 2k. With k = n−1: E[(n−1)s²/σ²] = n−1, so E(s²) = σ². Var[(n−1)s²/σ²] = 2(n−1), so Var(s²) = 2(n−1)σ⁴/(n−1)² = 2σ⁴/(n−1). Decreases with n.

### Q49. For iid Bernoulli(p) sample size n, derive MLE of p.
**Model answer:** Likelihood: L(p) = Π p^{xᵢ}(1−p)^{1−xᵢ} = p^{Σxᵢ}(1−p)^{n−Σxᵢ}. Log-likelihood: ℓ(p) = Σxᵢ log p + (n − Σxᵢ) log(1−p). Setting dℓ/dp = Σxᵢ/p − (n − Σxᵢ)/(1−p) = 0 gives p̂ = Σxᵢ/n = X̄.

### Q50. Describe a complete principles-of-sampling analysis.
**Model answer:** (1) Define population and parameter of interest (μ, σ², etc.). (2) Specify sampling mechanism (random sampling from population). (3) Define sample and relevant statistics (X̄, s²). (4) Derive distribution of statistic — exact where possible, asymptotic via CLT otherwise. (5) Construct confidence interval or hypothesis test. (6) Interpret: what does the sample tell us about the population? (7) Check assumptions: random sampling, independence, sufficient sample size for CLT.

---

**Exam tip:** For sampling principles, always: (1) state iid assumption explicitly, (2) distinguish population parameters (fixed) from sample statistics (random), (3) derive properties step-by-step — show each algebraic step, (4) state asymptotic results with conditions (finite variance, etc.), (5) apply CLT appropriately and acknowledge when finite-sample approximations may differ.
