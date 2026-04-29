# ST2134 — Proof Fluency (Derivations & Formal Proofs): 50 Exam Questions with Model Answers

---

## Part A: Moment Derivations (Q1-10)

### Q1. Prove E(X) = μ when X₁, ..., Xₙ are iid with mean μ.
**Model answer:** E(X̄) = E((1/n)Σ Xᵢ) = (1/n)E(Σ Xᵢ) = (1/n)Σ E(Xᵢ) (linearity of E) = (1/n)(nμ) = μ. Uses only linearity of expectation — no independence needed.

### Q2. Prove Var(X̄) = σ²/n for iid sample.
**Model answer:** Var(X̄) = Var((1/n)Σ Xᵢ) = (1/n²)Var(Σ Xᵢ) = (1/n²)Σ Var(Xᵢ) (independence) = (1/n²)(nσ²) = σ²/n. Uses independence in second step.

### Q3. Prove that s² is unbiased for σ² with divisor n−1.
**Model answer:** Consider S = Σ(Xᵢ − X̄)². Show E(S) = (n−1)σ². Use Σ(Xᵢ − X̄)² = Σ(Xᵢ − μ)² − n(X̄ − μ)². Take expectation: E(S) = nσ² − n·σ²/n = (n−1)σ². Hence s² = S/(n−1) has E(s²) = σ².

### Q4. Derive Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y).
**Model answer:** Var(X + Y) = E[(X + Y − μ_X − μ_Y)²] = E[(X − μ_X)² + (Y − μ_Y)² + 2(X − μ_X)(Y − μ_Y)] = Var(X) + Var(Y) + 2E[(X − μ_X)(Y − μ_Y)] = Var(X) + Var(Y) + 2Cov(X, Y).

### Q5. Prove E[E(Y|X)] = E(Y) (law of total expectation).
**Model answer:** E[E(Y|X)] = ∫ [∫ y f(y|x) dy] f_X(x) dx = ∫ ∫ y f(y|x) f_X(x) dy dx = ∫ ∫ y f(x, y) dy dx = E(Y). Uses f(x, y) = f(y|x) f_X(x). "Unconditioning" step via integration.

### Q6. Prove Var(Y) = E[Var(Y|X)] + Var[E(Y|X)].
**Model answer:** Var(Y) = E[Y²] − (E Y)². Use E[Y²] = E[E(Y²|X)] = E[Var(Y|X) + (E(Y|X))²] = E[Var(Y|X)] + E[(E(Y|X))²]. Also (E Y)² = (E[E(Y|X)])². Combining: Var(Y) = E[Var(Y|X)] + Var[E(Y|X)].

### Q7. Derive Chebyshev's inequality from Markov's.
**Model answer:** Markov: for Y ≥ 0, P(Y ≥ a) ≤ E(Y)/a. Apply to Y = (X − μ)²: P((X − μ)² ≥ (kσ)²) ≤ E((X − μ)²)/(kσ)² = σ²/(k²σ²) = 1/k². Now (X − μ)² ≥ (kσ)² iff |X − μ| ≥ kσ, so P(|X − μ| ≥ kσ) ≤ 1/k².

### Q8. Prove Jensen's inequality for convex g.
**Model answer:** For convex g: g(tu + (1−t)v) ≤ tg(u) + (1−t)g(v). Extension: g(E(X)) ≤ E(g(X)). Proof via supporting line: g(x) ≥ g(μ) + g'(μ)(x − μ). Take expectation: E(g(X)) ≥ g(μ) + g'(μ)(E(X) − μ) = g(μ). Valid for convex g.

### Q9. Derive E(X²) = Var(X) + [E(X)]².
**Model answer:** Var(X) = E[(X − E(X))²] = E(X² − 2XE(X) + (E(X))²) = E(X²) − 2(E(X))² + (E(X))² = E(X²) − (E(X))². Rearranging: E(X²) = Var(X) + [E(X)]².

### Q10. Prove that if X and Y are independent, Cov(X, Y) = 0.
**Model answer:** Cov(X, Y) = E(XY) − E(X)E(Y). By independence: E(XY) = E(X)E(Y). Hence Cov(X, Y) = E(X)E(Y) − E(X)E(Y) = 0. Converse NOT true generally (zero correlation doesn't imply independence).

---

## Part B: Distribution Derivations (Q11-20)

### Q11. Derive the distribution of X + Y for independent Poisson.
**Model answer:** X ~ Poisson(λ₁), Y ~ Poisson(λ₂), independent. MGF: M_X(t) = e^{λ₁(e^t − 1)}, M_Y(t) = e^{λ₂(e^t − 1)}. By independence: M_{X+Y}(t) = M_X(t)·M_Y(t) = e^{(λ₁+λ₂)(e^t − 1)}. This is MGF of Poisson(λ₁ + λ₂). By uniqueness: X + Y ~ Poisson(λ₁ + λ₂).

### Q12. Derive distribution of sum of iid exponentials.
**Model answer:** X₁, ..., Xₙ iid Exp(λ). MGF of each: λ/(λ − t) for t < λ. MGF of sum S = Σ Xᵢ: [λ/(λ − t)]ⁿ. This is MGF of Gamma(n, λ). By uniqueness: S ~ Gamma(n, λ).

### Q13. Show X² ~ χ²(1) for X ~ N(0, 1).
**Model answer:** Y = X². F_Y(y) = P(X² ≤ y) = P(−√y ≤ X ≤ √y) = Φ(√y) − Φ(−√y) = 2Φ(√y) − 1 for y ≥ 0. Differentiate: f_Y(y) = 2φ(√y) · (1/(2√y)) = φ(√y)/√y = (1/√(2πy)) e^{−y/2}, which is χ²(1) pdf.

### Q14. Derive distribution of sample variance (scaled) under normality.
**Model answer:** For X₁, ..., Xₙ iid N(μ, σ²): (n−1)s²/σ² ~ χ²(n−1). Proof sketch: Σ(Xᵢ − μ)²/σ² ~ χ²(n). Decompose Σ(Xᵢ − μ)² = Σ(Xᵢ − X̄)² + n(X̄ − μ)². Second term: n(X̄ − μ)²/σ² ~ χ²(1). By independence and properties of chi-squared: (n−1)s²/σ² ~ χ²(n−1).

### Q15. Derive the t-distribution from Z and χ² components.
**Model answer:** If Z ~ N(0, 1) and V ~ χ²(k), independent. T = Z/√(V/k). Find density: f_T(t) ∝ (1 + t²/k)^{−(k+1)/2}. Specifically: f_T(t) = Γ((k+1)/2)/[√(kπ) · Γ(k/2)] · (1 + t²/k)^{−(k+1)/2}.

### Q16. Show (X̄ − μ)/(s/√n) ~ t(n−1) under normality.
**Model answer:** Z = (X̄ − μ)/(σ/√n) ~ N(0, 1). V = (n−1)s²/σ² ~ χ²(n−1). Z and V independent (Basu's theorem). By definition: T = Z/√(V/(n−1)) = (X̄ − μ)/(s/√n) ~ t(n−1).

### Q17. Derive the distribution of max of iid uniforms.
**Model answer:** X₁, ..., Xₙ iid Uniform(0, 1). F_{X_(n)}(x) = P(max ≤ x) = P(all Xᵢ ≤ x) = x^n for x ∈ [0, 1]. Density: f_{X_(n)}(x) = nx^{n−1}. Recognise as Beta(n, 1).

### Q18. Derive the distribution of the order statistic X_(k).
**Model answer:** For iid X_i with pdf f and CDF F: f_{X_(k)}(x) = [n!/((k−1)!(n−k)!)] F(x)^{k−1} f(x) [1 − F(x)]^{n−k}. Intuition: (k−1) below x, one at x, (n−k) above. Multinomial-like coefficient.

### Q19. Derive relationship between Binomial and Poisson.
**Model answer:** X ~ Bin(n, p). As n → ∞, p → 0 with np = λ fixed: P(X = k) = C(n, k) p^k (1−p)^{n−k} ≈ (n^k/k!) · (λ/n)^k · e^{−λ} = (λ^k/k!) e^{−λ} = Poisson(λ) pmf. Rare event approximation.

### Q20. Prove the normal-to-chi-squared relationship.
**Model answer:** If Z₁, ..., Z_k iid N(0, 1), then Σ Z_i² ~ χ²(k). MGF of Z² is (1 − 2t)^{−1/2} (from χ²(1)). Sum of k independent: [(1 − 2t)^{−1/2}]^k = (1 − 2t)^{−k/2}, which is MGF of χ²(k). By uniqueness, sum of squares is chi-squared.

---

## Part C: Estimator Derivations (Q21-30)

### Q21. Derive MLE of μ in Normal(μ, σ²) with known σ².
**Model answer:** L(μ) = ∏ (1/√(2πσ²)) exp[−(xᵢ − μ)²/(2σ²)]. ℓ(μ) = const − Σ(xᵢ − μ)²/(2σ²). dℓ/dμ = Σ(xᵢ − μ)/σ² = 0. Solving: μ̂ = (1/n) Σ xᵢ = X̄.

### Q22. Derive MLE of σ² in Normal(μ, σ²) with μ known.
**Model answer:** ℓ(σ²) = −(n/2) log(2π) − (n/2) log σ² − Σ(xᵢ − μ)²/(2σ²). dℓ/dσ² = −n/(2σ²) + Σ(xᵢ − μ)²/(2σ⁴) = 0. Solving: σ̂² = (1/n) Σ(xᵢ − μ)².

### Q23. Derive Fisher information for Bernoulli(p).
**Model answer:** ℓ(p) = x log p + (1−x) log(1−p). dℓ/dp = x/p − (1−x)/(1−p). d²ℓ/dp² = −x/p² − (1−x)/(1−p)². I(p) = −E(d²ℓ/dp²) = E(X)/p² + E(1−X)/(1−p)² = p/p² + (1−p)/(1−p)² = 1/p + 1/(1−p) = 1/[p(1−p)].

### Q24. Prove X̄ achieves CRLB in Normal(μ, σ²), σ known.
**Model answer:** I(μ) = 1/σ² (from score derivative). CRLB = 1/(n·I) = σ²/n. Var(X̄) = σ²/n. Hence Var(X̄) = CRLB — achieves the bound, is efficient.

### Q25. Prove unbiasedness of X̄ for μ (full proof).
**Model answer:** E(X̄) = E((1/n) ΣXᵢ) = (1/n) Σ E(Xᵢ) (linearity) = (1/n) · nμ = μ. So Bias(X̄) = E(X̄) − μ = 0. Note: only requires E(Xᵢ) exists, not full moments.

### Q26. Derive variance of MLE for Poisson.
**Model answer:** MLE λ̂ = X̄. Var(X̄) = λ/n (Poisson variance = mean). Fisher info: I(λ) = 1/λ. CRLB = 1/(n/λ) = λ/n. Var(λ̂) = CRLB, so MLE efficient. Formula holds by substitution; finite-sample as well as asymptotic.

### Q27. Apply method of moments to Gamma(α, β).
**Model answer:** E(X) = α/β, E(X²) = α(α+1)/β². Sample moments: X̄ = α̂/β̂, (1/n)ΣXᵢ² = X̄² + s̃² (for MoM with n divisor). Solve: β̂ = X̄/s̃², α̂ = X̄²/s̃² = X̄·β̂. Alternative: use rate parameter as per convention.

### Q28. Derive score equation and MLE for Bernoulli.
**Model answer:** For n iid X_i ~ Bernoulli(p): ℓ(p) = (Σx_i) log p + (n − Σx_i) log(1 − p). Score: U(p) = Σx_i/p − (n − Σx_i)/(1−p). Setting U = 0: Σx_i(1−p) = p(n − Σx_i) → Σx_i − pΣx_i = pn − pΣx_i → p̂ = Σx_i/n = X̄.

### Q29. Prove Rao-Blackwell improvement.
**Model answer:** Given W unbiased for τ(θ), T sufficient. Let W* = E(W|T). (1) Unbiasedness: E(W*) = E[E(W|T)] = E(W) = τ(θ). (2) Variance reduction: Var(W) = Var(E(W|T)) + E[Var(W|T)] (law of total variance). Since E[Var(W|T)] ≥ 0: Var(W) ≥ Var(E(W|T)) = Var(W*).

### Q30. Prove asymptotic normality of MLE (sketch).
**Model answer:** Taylor-expand score: 0 = U(θ̂) ≈ U(θ₀) + (θ̂ − θ₀)·U'(θ₀). So θ̂ − θ₀ ≈ −U(θ₀)/U'(θ₀) ≈ U(θ₀)/(n·I(θ₀)) (U' = −I by definition, expectation). By CLT: U(θ₀)/√n →_d N(0, I(θ₀)). Hence √n(θ̂ − θ₀) →_d N(0, 1/I(θ₀)).

---

## Part D: Test Derivations (Q31-40)

### Q31. Derive the Neyman-Pearson test for simple vs simple.
**Model answer:** Test H₀: f = f₀ vs H₁: f = f₁. NP test: reject if Λ(x) = f₁(x)/f₀(x) > k, where k such that P(Λ > k | H₀) = α. Proof uses Lagrange multiplier argument — maximise power subject to size α constraint. Result: LR test is MP.

### Q32. Show UMP test for one-sided normal mean exists.
**Model answer:** H₀: μ ≤ μ₀ vs H₁: μ > μ₀. Family N(μ, σ²) with σ² known has MLR in X̄. By Karlin-Rubin theorem: UMP test exists, rejects for large X̄. Specifically: reject if X̄ > μ₀ + z_α·σ/√n. Monotone likelihood ratio is key.

### Q33. Prove likelihood ratio test for Bernoulli.
**Model answer:** H₀: p = p₀ vs H₁: p ≠ p₀. LR statistic: λ = 2[ℓ(p̂) − ℓ(p₀)] = 2[Σx log(p̂/p₀) + (n − Σx) log((1−p̂)/(1−p₀))]. Under H₀: λ →_d χ²(1). Rejection: λ > χ²_{α, 1}.

### Q34. Derive the Wald test for Bernoulli.
**Model answer:** H₀: p = p₀. θ̂ = p̂. Asymptotic variance: Var(p̂) = p(1−p)/n, estimated p̂(1−p̂)/n. W = (p̂ − p₀)²/[p̂(1−p̂)/n]. Under H₀ and large n: W ~ χ²(1).

### Q35. Derive the score test for Bernoulli.
**Model answer:** U(p) = Σx_i/p − (n − Σx_i)/(1−p). At p₀: U(p₀) = n(X̄ − p₀)/(p₀(1−p₀)). I(p₀) = n/(p₀(1−p₀)). Score test: LM = U(p₀)²/I(p₀) = [n(X̄−p₀)/(p₀(1−p₀))]² · p₀(1−p₀)/n = n(X̄ − p₀)²/[p₀(1−p₀)]. Under H₀: ~χ²(1).

### Q36. Compare LR, Wald, score for Bernoulli.
**Model answer:** For large samples with p̂ ≈ p₀: LR, Wald, and score statistics are approximately equal. In finite samples, can differ. LR statistic ≥ score when derivatives aligned. Wald uses p̂; score uses p₀; so they differ by where information is estimated.

### Q37. Derive power function for Neyman-Pearson normal test.
**Model answer:** One-sided test for H₀: μ = 0 vs H₁: μ > 0, σ known. Reject if Z > z_α. Power(μ₁) = P(Z > z_α | μ = μ₁) = 1 − Φ(z_α − μ₁√n/σ). Monotonically increasing in μ₁. Power → 1 as μ₁ → ∞.

### Q38. Derive the chi-squared test for variance.
**Model answer:** H₀: σ² = σ₀². Statistic: χ² = (n−1)s²/σ₀². Under H₀ and normality: (n−1)s²/σ₀² ~ χ²(n−1). Two-sided: reject if < χ²_{1−α/2, n−1} or > χ²_{α/2, n−1}. Sensitive to non-normality.

### Q39. Prove the duality between tests and confidence intervals.
**Model answer:** Let A(θ) be acceptance region of level-α test of H₀: θ = θ₀. CI constructed by inverting: C(x) = {θ : x ∈ A(θ)}. Coverage: P(θ ∈ C(X) | θ) = P(X ∈ A(θ) | θ) = 1 − α. Inverting a test gives CI; CI construction = testing procedure.

### Q40. Derive ANOVA F-statistic from first principles.
**Model answer:** For k groups with common variance: decompose total SS as between (SSB) + within (SSW). Under H₀: μ₁ = ... = μ_k, (SSB/(k−1))/(SSW/(n−k)) ~ F(k−1, n−k). Numerator: variance among group means; denominator: within-group variance. F large: group differences dominate.

---

## Part E: Bayesian Derivations (Q41-45)

### Q41. Derive posterior for Beta-Binomial conjugacy.
**Model answer:** Prior: p ~ Beta(α, β). Data: x successes in n trials, likelihood ∝ p^x(1−p)^{n−x}. Posterior: π(p|x) ∝ p^{α−1}(1−p)^{β−1} · p^x(1−p)^{n−x} = p^{α+x−1}(1−p)^{β+n−x−1}. Recognise as Beta(α+x, β+n−x).

### Q42. Derive posterior for Normal-Normal conjugacy.
**Model answer:** Prior: μ ~ N(μ₀, τ₀²). Data: X_i ~ N(μ, σ²) iid, σ² known. Likelihood ∝ exp[−(Σ(X_i − μ)²)/(2σ²)]. Multiply with prior ∝ exp[−(μ − μ₀)²/(2τ₀²)]. Complete square in μ: posterior ∝ exp[−(μ − μ_n)²/(2τ_n²)], where τ_n² = (1/τ₀² + n/σ²)⁻¹, μ_n = τ_n²(μ₀/τ₀² + nX̄/σ²). Posterior ~ N(μ_n, τ_n²).

### Q43. Derive posterior predictive distribution.
**Model answer:** P(y_new | y_obs) = ∫ f(y_new | θ) · π(θ | y_obs) dθ. Example for Beta-Binomial: integrate over posterior Beta. Result: beta-binomial distribution for new observation. Accounts for parameter uncertainty.

### Q44. Show posterior mean is weighted average for Normal-Normal.
**Model answer:** Posterior mean: μ_n = τ_n²(μ₀/τ₀² + nX̄/σ²) = [μ₀/τ₀² + nX̄/σ²]/(1/τ₀² + n/σ²) = w₀·μ₀ + w₁·X̄, where w₀ = (1/τ₀²)/(1/τ₀² + n/σ²) and w₁ = (n/σ²)/(1/τ₀² + n/σ²). Weights proportional to precisions. As n → ∞, w₁ → 1 (data dominates).

### Q45. Derive Jeffrey's prior for Bernoulli.
**Model answer:** Jeffrey's prior: π(p) ∝ √I(p). I(p) = 1/[p(1−p)]. So π(p) ∝ [p(1−p)]^{−1/2} = p^{−1/2}(1−p)^{−1/2}. Recognise as Beta(1/2, 1/2). Invariant under reparameterisation (useful property).

---

## Part F: Application & Comprehensive Proofs (Q46-50)

### Q46. Provide full proof of CLT via MGFs.
**Model answer:** For iid X_i with mean μ, variance σ². Standardise Z_i = (X_i − μ)/σ. MGF: M_Z(t) = 1 + t²/2 + O(t³) (by Taylor). For S_n = (1/√n) ΣZ_i: M_{S_n}(t) = [M_Z(t/√n)]^n = [1 + t²/(2n) + O(1/n^{3/2})]^n → e^{t²/2} as n → ∞. This is MGF of N(0, 1). By uniqueness: S_n →_d N(0, 1).

### Q47. Prove consistency of MLE via convergence of likelihood.
**Model answer:** Under regularity: (1) ℓ_n(θ)/n → E[log f(X; θ)] uniformly. (2) E[log f(X; θ)] maximised at θ = θ₀ (Kullback-Leibler). (3) θ̂_n maximises ℓ_n/n → maximiser of E, which is θ₀. Hence θ̂_n →_p θ₀. Requires identifiability, bounded moments.

### Q48. Prove invariance of MLE under reparameterisation.
**Model answer:** Let ψ = g(θ). If L_θ has MLE θ̂, then for L_ψ = L_θ(g^{-1}(ψ)), the value maximising L_ψ is ψ such that g^{-1}(ψ) = θ̂, i.e., ψ̂ = g(θ̂). MLE of g(θ) is g(MLE of θ).

### Q49. Prove the central limit theorem for sums.
**Model answer:** Standard form: for iid with mean μ, variance σ²: (1/√n)(Σ X_i − nμ) →_d N(0, σ²). MGF proof: M_{standardized sum}(t) → e^{t²/2}. Requires finite variance. Extensions: Lindeberg-Lévy (iid), Lindeberg-Feller (non-iid with conditions).

### Q50. Complete proof sketch: UMVUE of p in Bernoulli.
**Model answer:** (1) X_i iid Bernoulli(p), L = p^{Σx}(1−p)^{n−Σx}. (2) By factorisation: T = Σx sufficient for p. (3) Show T complete: if E[g(T)] = 0 for all p, then g = 0 (polynomial identity argument). (4) X̄ = T/n is unbiased: E(X̄) = p. (5) By Lehmann-Scheffé: X̄ is UMVUE. (6) Check efficiency: Var(X̄) = p(1−p)/n = CRLB.

---

**Exam tip:** For proof-fluency questions in ST2134, remember: (1) state definitions and theorems before applying them, (2) show every algebraic step — don't skip, (3) identify which properties/assumptions are used at each step, (4) be careful with indices, signs, and limits, (5) conclude with what is proven, (6) write legibly and structure with lemmas/main result. Speed comes from practice — write out 5 proofs per day in the final weeks.
