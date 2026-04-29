# ST2134 — Moments & Order Statistics: 50 Exam Questions with Model Answers

---

## Part A: Moments (Q1-15)

### Q1. Define the k-th moment of a random variable.
**Model answer:** The k-th moment (about the origin) of a random variable X is μ'_k = E(X^k). Exists if the integral/sum converges absolutely. The first moment is the mean: μ'_1 = E(X) = μ.

### Q2. Define the k-th central moment.
**Model answer:** The k-th central moment is μ_k = E[(X − μ)^k], where μ = E(X). The second central moment is the variance: μ_2 = Var(X) = σ². Central moments quantify spread around the mean.

### Q3. Define skewness.
**Model answer:** Skewness = μ_3/σ³ = E[((X − μ)/σ)³]. Measures asymmetry of distribution. Positive: right-skewed (long right tail). Negative: left-skewed. Zero: symmetric (e.g., normal). Standardised to be scale-invariant.

### Q4. Define kurtosis.
**Model answer:** Kurtosis = μ_4/σ⁴ = E[((X − μ)/σ)⁴]. Measures tail heaviness. Normal has kurtosis = 3. Excess kurtosis = kurtosis − 3. Leptokurtic (heavy tails, kurtosis > 3): t-distribution. Platykurtic (thin tails, < 3): uniform. Mesokurtic (=3): normal.

### Q5. State the moment generating function (MGF).
**Model answer:** M_X(t) = E(e^{tX}) = Σ P(X=x)e^{tx} (discrete) or ∫ f(x)e^{tx} dx (continuous), for t in a neighbourhood of 0. If MGF exists and is finite in a neighbourhood, it uniquely determines the distribution.

### Q6. Derive moments from the MGF.
**Model answer:** M_X(t) = Σ t^k E(X^k)/k!. Taking k-th derivative at t = 0: M^{(k)}(0) = E(X^k). First derivative at 0 gives mean; second gives E(X²), from which Var(X) = E(X²) − [E(X)]².

### Q7. State the key properties of MGF.
**Model answer:** (1) Linearity: M_{aX+b}(t) = e^{bt} M_X(at). (2) Independence: M_{X+Y}(t) = M_X(t) M_Y(t) for independent X, Y. (3) Uniqueness: If MGF exists in neighbourhood of 0, it determines distribution. (4) Some distributions lack MGF (e.g., Cauchy).

### Q8. Find the MGF of the exponential distribution.
**Model answer:** For X ~ Exp(λ): M_X(t) = E(e^{tX}) = ∫₀^∞ e^{tx} λe^{−λx} dx = λ ∫₀^∞ e^{−(λ−t)x} dx = λ/(λ−t) for t < λ. From this: E(X) = M'(0) = 1/λ; E(X²) = M''(0) = 2/λ². So Var(X) = 2/λ² − 1/λ² = 1/λ².

### Q9. Find the MGF of the normal distribution.
**Model answer:** For X ~ N(μ, σ²): M_X(t) = E(e^{tX}) = e^{μt + σ²t²/2}. Derivation: complete the square in the exponent. Use to verify: E(X) = M'(0) = μ; E(X²) = M''(0) = σ² + μ²; Var(X) = σ².

### Q10. State the characteristic function (CF).
**Model answer:** φ_X(t) = E(e^{itX}) = E(cos(tX)) + iE(sin(tX)). Complex-valued. Always exists (unlike MGF). Uniqueness: determines distribution. For independent X, Y: φ_{X+Y}(t) = φ_X(t) φ_Y(t). Central tool in proofs of CLT.

### Q11. State Chebyshev's inequality.
**Model answer:** For any random variable X with E(X) = μ, Var(X) = σ², and k > 0: P(|X − μ| ≥ kσ) ≤ 1/k². Distribution-free bound. Weak but universal. Example: P(|X − μ| ≥ 2σ) ≤ 1/4. Strengthens by factor 4 for normal: P(|X − μ| ≥ 2σ) ≈ 0.046.

### Q12. State Markov's inequality.
**Model answer:** For X ≥ 0 with finite mean: P(X ≥ a) ≤ E(X)/a for a > 0. More general than Chebyshev. Basic building block. Example: if E(X) = 10, then P(X ≥ 100) ≤ 10/100 = 0.1.

### Q13. Derive Chebyshev from Markov.
**Model answer:** Let Y = (X − μ)². Y ≥ 0 and E(Y) = σ². By Markov: P(Y ≥ k²σ²) ≤ σ²/(k²σ²) = 1/k². Now P(Y ≥ k²σ²) = P(|X − μ| ≥ kσ). Hence P(|X − μ| ≥ kσ) ≤ 1/k².

### Q14. State Jensen's inequality.
**Model answer:** For a convex function g and random variable X with finite mean: g(E(X)) ≤ E(g(X)). Example: Var(X) ≥ 0 because g(x) = x² is convex: E(X²) ≥ [E(X)]². For concave g (e.g., log): g(E(X)) ≥ E(g(X)).

### Q15. State the Cauchy-Schwarz inequality.
**Model answer:** For random variables X, Y with finite second moments: |E(XY)| ≤ √(E(X²) E(Y²)). Equality holds iff X = aY a.s. Derives correlation bound: |ρ(X,Y)| ≤ 1. Fundamental tool in probability theory.

---

## Part B: Order Statistics Fundamentals (Q16-30)

### Q16. Define order statistics.
**Model answer:** For a sample X₁, ..., Xₙ, the order statistics X_(1) ≤ X_(2) ≤ ... ≤ X_(n) are the values arranged in increasing order. X_(1) = min(X₁, ..., Xₙ), X_(n) = max(X₁, ..., Xₙ), X_((n+1)/2) = median (odd n).

### Q17. Derive the CDF of the maximum X_(n).
**Model answer:** F_{X_(n)}(x) = P(max ≤ x) = P(X₁ ≤ x, X₂ ≤ x, ..., Xₙ ≤ x) = Π P(Xᵢ ≤ x) = F(x)^n (assuming iid). Intuition: all observations must be below x.

### Q18. Derive the CDF of the minimum X_(1).
**Model answer:** F_{X_(1)}(x) = P(min ≤ x) = 1 − P(min > x) = 1 − P(all Xᵢ > x) = 1 − [1 − F(x)]^n. Intuition: at least one observation must be below x.

### Q19. Derive the PDF of the maximum.
**Model answer:** f_{X_(n)}(x) = dF_{X_(n)}/dx = n F(x)^{n−1} f(x). Intuition: arrange n values, one at x and n−1 below. The factor n accounts for which position is the maximum.

### Q20. Derive the PDF of the minimum.
**Model answer:** f_{X_(1)}(x) = n [1 − F(x)]^{n−1} f(x). One observation at x, n−1 above. Similar structure to maximum.

### Q21. State the general formula for the k-th order statistic PDF.
**Model answer:** f_{X_(k)}(x) = [n!/((k−1)!(n−k)!)] F(x)^{k−1} [1 − F(x)]^{n−k} f(x). Combinatorial: (k−1) below x, one at x, (n−k) above. Essential result for order statistics inference.

### Q22. Derive the PDF of X_(k) from first principles.
**Model answer:** Consider arranging n values: (k−1) below x, one at x, (n−k) above. Ways: n!/((k−1)!·1!·(n−k)!). Probabilities: F(x)^{k−1} · f(x)dx · [1−F(x)]^{n−k}. So f_{X_(k)}(x) = [n!/((k−1)!(n−k)!)] F(x)^{k−1} f(x) [1−F(x)]^{n−k}.

### Q23. Derive the joint PDF of two order statistics.
**Model answer:** For j < k, f_{(j,k)}(u, v) = [n!/((j−1)!(k−j−1)!(n−k)!)] F(u)^{j−1} f(u) [F(v)−F(u)]^{k−j−1} f(v) [1−F(v)]^{n−k}, for u < v. Accounts for arranging (j−1), (k−j−1), and (n−k) observations in respective regions.

### Q24. State the joint PDF of all order statistics.
**Model answer:** f_{(1,...,n)}(x_1, ..., x_n) = n! Π f(x_i), for x_1 < x_2 < ... < x_n. Otherwise 0. Factor n! accounts for n! ways to order the sample. All orderings equally likely under iid.

### Q25. Derive the distribution of the range X_(n) − X_(1).
**Model answer:** Joint of (X_(1), X_(n)): f_{(1,n)}(u, v) = n(n−1) [F(v) − F(u)]^{n−2} f(u) f(v), for u < v. Range R = V − U. Find f_R by transformation. For uniform parent: R follows Beta-related distribution.

### Q26. For Uniform(0, 1), find E(X_(k)).
**Model answer:** For U_(k) where U_1, ..., U_n ~ Uniform(0,1): E(U_(k)) = k/(n+1). Order statistics from uniform are Beta distributed: U_(k) ~ Beta(k, n−k+1). Fundamental result — often used in proofs.

### Q27. For Uniform(0, 1), find Var(X_(k)).
**Model answer:** Var(U_(k)) = k(n−k+1)/[(n+1)²(n+2)]. Maximum at k = (n+1)/2 (median). Decreases as k approaches endpoints. Variance → 0 as n → ∞ for fixed k/n — order statistics concentrate.

### Q28. Distribution of minimum of iid exponentials.
**Model answer:** X_(1) = min(X₁, ..., Xₙ) where Xᵢ ~ Exp(λ) iid. P(X_(1) > x) = P(all Xᵢ > x) = [e^{−λx}]^n = e^{−nλx}. So X_(1) ~ Exp(nλ). Minimum of exponentials is exponential with sum of rates.

### Q29. State the relationship between order statistics and Beta.
**Model answer:** For U₁, ..., Uₙ iid Uniform(0, 1): U_(k) ~ Beta(k, n−k+1). For general F: transform to uniform via probability integral (F(X) ~ Uniform(0,1)). Hence F(X_(k)) ~ Beta(k, n−k+1). Powerful tool for derivations.

### Q30. Find the distribution of the sample median.
**Model answer:** For odd n = 2m+1: median = X_((m+1)). For uniform parent: median ~ Beta(m+1, m+1), symmetric about 0.5 with mean 0.5 and variance 1/(4n+8) approximately. For general parent: asymptotic result via Central Limit Theorem for quantiles.

---

## Part C: Moments and Functions of Random Variables (Q31-40)

### Q31. Derive E(X) for Uniform(a, b).
**Model answer:** E(X) = ∫_a^b x · [1/(b−a)] dx = [1/(b−a)] · [x²/2]_a^b = (b² − a²)/[2(b−a)] = (b+a)/2. Midpoint of the interval.

### Q32. Derive Var(X) for Uniform(a, b).
**Model answer:** E(X²) = [1/(b−a)] · [x³/3]_a^b = (b³ − a³)/[3(b−a)] = (b² + ab + a²)/3. Var(X) = E(X²) − [E(X)]² = (b² + ab + a²)/3 − (b+a)²/4. Simplification: Var(X) = (b−a)²/12.

### Q33. Derive MGF of Bin(n, p).
**Model answer:** X = X₁ + ... + Xₙ where Xᵢ ~ Bernoulli(p) iid. M_{Bernoulli}(t) = 1 − p + pe^t. By independence: M_X(t) = (1 − p + pe^t)^n. From this: E(X) = np, Var(X) = np(1−p).

### Q34. Derive MGF of Poisson(λ).
**Model answer:** M(t) = Σ P(X=k) e^{kt} = Σ (e^{−λ}λ^k/k!) e^{kt} = e^{−λ} Σ (λe^t)^k/k! = e^{−λ} e^{λe^t} = e^{λ(e^t − 1)}. From this: E(X) = λ, Var(X) = λ (mean = variance).

### Q35. Use MGF to find E(X³) for X ~ Exp(λ).
**Model answer:** M_X(t) = λ/(λ−t). M'(t) = λ/(λ−t)². M''(t) = 2λ/(λ−t)³. M'''(t) = 6λ/(λ−t)⁴. E(X³) = M'''(0) = 6/λ³. Also E(X^k) = k!/λ^k — factorial moment structure.

### Q36. Derive Var(aX + bY + c) for independent X, Y.
**Model answer:** Var(aX + bY + c) = a²Var(X) + b²Var(Y) + 0 (constant has zero variance, independence means no covariance). For dependent: add 2ab·Cov(X, Y).

### Q37. Find the distribution of Y = X² for X ~ N(0, 1).
**Model answer:** Y = X² has CDF P(Y ≤ y) = P(−√y ≤ X ≤ √y) = Φ(√y) − Φ(−√y) = 2Φ(√y) − 1 for y ≥ 0. Differentiating: f_Y(y) = 2 · φ(√y) · (1/(2√y)) = φ(√y)/√y = (1/√(2πy)) e^{−y/2}. This is the χ²(1) density.

### Q38. Derive MGF of sum of independent exponentials.
**Model answer:** X₁, ..., Xₙ iid Exp(λ). M(t) = λ/(λ−t). Sum Y = ΣXᵢ has MGF M_Y(t) = [λ/(λ−t)]^n, which is MGF of Gamma(n, λ). So Y ~ Gamma(n, λ). Generalises: sum of n iid Exp(λ) is Gamma.

### Q39. Derive the distribution of |X| for X ~ N(0, 1).
**Model answer:** Y = |X|. CDF: P(Y ≤ y) = P(−y ≤ X ≤ y) = Φ(y) − Φ(−y) = 2Φ(y) − 1. PDF: f_Y(y) = 2φ(y) = (2/√(2π)) e^{−y²/2}. Half-normal distribution.

### Q40. Use Jensen's inequality to bound E(1/X).
**Model answer:** g(x) = 1/x is convex (for x > 0). Jensen: E(1/X) ≥ 1/E(X). So 1/X̄ systematically over-estimates 1/μ. Important for bias in transformations. Taylor expansion: E(1/X) ≈ 1/μ + σ²/μ³ — the bias term.

---

## Part D: Applications and Theorems (Q41-45)

### Q41. Apply CLT with moments.
**Model answer:** Xᵢ ~ iid with E(X) = μ, Var(X) = σ². For large n, X̄ ≈ N(μ, σ²/n). The normalised variable Z = (X̄ − μ)/(σ/√n) →_d N(0, 1). Requires only finite variance — doesn't need moments beyond 2 (though higher moments speed convergence).

### Q42. Find asymptotic variance of X̄² using delta method.
**Model answer:** Let g(x̄) = x̄². g'(μ) = 2μ. √n(X̄ − μ) →_d N(0, σ²). By delta method: √n(X̄² − μ²) →_d N(0, (2μ)² · σ²) = N(0, 4μ²σ²). So asymptotic variance of X̄² is 4μ²σ²/n.

### Q43. Apply moments to find correlation.
**Model answer:** ρ(X, Y) = Cov(X, Y)/√(Var(X) Var(Y)) = E[(X − μ_X)(Y − μ_Y)]/√(σ_X² σ_Y²). Compute via moments: Cov(X, Y) = E(XY) − E(X)E(Y). Correlation bounded: |ρ| ≤ 1 by Cauchy-Schwarz.

### Q44. Chebyshev applied to sample mean.
**Model answer:** For X̄ with mean μ, variance σ²/n: P(|X̄ − μ| ≥ k · σ/√n) ≤ 1/k². So P(|X̄ − μ| ≥ 0.1) ≤ Var(X̄)/0.01 = σ²/(0.01·n). Shows consistency: probability → 0 as n → ∞.

### Q45. Moments and the method of moments estimator.
**Model answer:** Method of moments: set population moments equal to sample moments, solve for parameters. Example: for Normal(μ, σ²): μ̂ = X̄, σ̂² = (1/n)Σ(Xᵢ − X̄)². Simple but often less efficient than MLE.

---

## Part E: Application (Q46-50)

### Q46. Find E(X_(n)) for X_i iid Uniform(0, 1), n = 10.
**Model answer:** X_(n) ~ Beta(n, 1) = Beta(10, 1). E(X_(n)) = n/(n+1) = 10/11 ≈ 0.909. Max of sample tends to 1 as n → ∞. Distribution: f(x) = 10x^9 for x ∈ [0,1].

### Q47. Find P(X_(n) > 0.9) for X_i iid Uniform(0, 1), n = 20.
**Model answer:** P(X_(n) ≤ 0.9) = F(0.9)^n = 0.9^20 ≈ 0.122. So P(X_(n) > 0.9) = 1 − 0.122 = 0.878. With 20 observations, almost certain that the maximum exceeds 0.9.

### Q48. Use MGF to find the distribution of a sum.
**Model answer:** X ~ Poisson(λ₁), Y ~ Poisson(λ₂) independent. M_X(t) = e^{λ₁(e^t − 1)}. M_Y(t) = e^{λ₂(e^t − 1)}. M_{X+Y}(t) = M_X(t) · M_Y(t) = e^{(λ₁+λ₂)(e^t − 1)}. This is MGF of Poisson(λ₁ + λ₂). So sum of independent Poissons is Poisson.

### Q49. Method of moments for Gamma(α, β).
**Model answer:** E(X) = α/β, E(X²) = α(α+1)/β². Sample moments: X̄ and (1/n)ΣXᵢ². Solve: α̂/β̂ = X̄, (α̂(α̂+1))/β̂² = (1/n)ΣXᵢ². From these: α̂ = X̄²/s̃², β̂ = X̄/s̃², where s̃² = sample variance (with n divisor).

### Q50. Apply Chebyshev to bound a Bayesian credible region.
**Model answer:** Posterior of θ: posterior mean μ_π, variance σ²_π. By Chebyshev: P(|θ − μ_π| ≥ 2σ_π | data) ≤ 0.25. So 75% of posterior mass lies within ±2σ_π of μ_π. Conservative bound — often tighter intervals exist under specific distributions.

---

**Exam tip:** For moments questions: (1) show step-by-step algebraic derivations, (2) state which moment assumptions are needed, (3) use MGFs to find distributions of sums and transformations, (4) for order statistics: use combinatorial argument with (k−1), (1), (n−k) structure. For bounds (Chebyshev, Markov): always state the assumption (non-negativity, finite moment) before applying.
