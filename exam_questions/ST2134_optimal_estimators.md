# ST2134 — Optimal Estimators & Tests: 50 Exam Questions with Model Answers

---

## Part A: Cramér-Rao Lower Bound (Q1-10)

### Q1. State the Cramér-Rao inequality.
**Model answer:** For any unbiased estimator T of τ(θ) in a regular model: Var(T) ≥ [τ'(θ)]² / I(θ), where I(θ) = E[(∂log f/∂θ)²] = Fisher information. Special case (τ(θ) = θ): Var(T) ≥ 1/I(θ).

### Q2. Define the CRLB for parameter θ.
**Model answer:** For unbiased T estimating θ: Var(T) ≥ 1/I(θ). For n iid observations: I_n(θ) = n·I(θ), so Var(T) ≥ 1/(n·I(θ)). Lower bound is O(1/n). Any estimator below CRLB must be biased.

### Q3. Define efficiency of an estimator.
**Model answer:** Efficiency e(T) = CRLB / Var(T). Ratio of lower bound to actual variance. Range (0, 1]. e = 1: fully efficient (achieves CRLB). e < 1: inefficient. Asymptotic efficiency = limit as n → ∞.

### Q4. Define Fisher information.
**Model answer:** I(θ) = E[(∂log f(X|θ)/∂θ)²] = −E[∂²log f(X|θ)/∂θ²] (equivalent under regularity). Measures information per observation. Multiplicative for iid: I_n(θ) = n·I(θ). Reciprocal relates to variance of efficient estimators.

### Q5. Derive CRLB via the Cramér-Rao inequality proof (sketch).
**Model answer:** Start with E(T) = τ(θ). Differentiate: ∫ T(x) ∂f/∂θ dx = τ'(θ). Note ∂f/∂θ = f · ∂log f/∂θ. So E[T · ∂log f/∂θ] = τ'(θ). Apply Cauchy-Schwarz: [τ'(θ)]² ≤ Var(T) · Var(∂log f/∂θ) = Var(T) · I(θ). Rearrange: Var(T) ≥ [τ'(θ)]²/I(θ).

### Q6. Conditions required for CRLB.
**Model answer:** (1) Regularity: differentiability of f in θ. (2) E(∂log f/∂θ) = 0 (validity of interchange of expectation and differentiation). (3) Support of X does not depend on θ. Violations (e.g., Uniform(0, θ)) mean CRLB doesn't apply or estimators can beat it.

### Q7. Describe what achieves CRLB.
**Model answer:** Estimator T achieves CRLB iff T is linear function of score: ∂log L/∂θ = k(θ) · (T − θ). In exponential family, sufficient statistic achieves CRLB for certain parameters. MLE asymptotically achieves CRLB under regularity.

### Q8. Derive CRLB for Bernoulli(p).
**Model answer:** ℓ(p) = x log p + (1−x) log(1−p). Score: ∂ℓ/∂p = x/p − (1−x)/(1−p). Fisher information: I(p) = E[(score)²] = 1/(p(1−p)). For n observations: I_n(p) = n/(p(1−p)). CRLB: 1/I_n(p) = p(1−p)/n. X̄ achieves this.

### Q9. Derive CRLB for Normal(μ, σ²) with σ² known.
**Model answer:** ℓ(μ) = −(x − μ)²/(2σ²). Score: ∂ℓ/∂μ = (x − μ)/σ². I(μ) = E[(X − μ)²/σ⁴] = σ²/σ⁴ = 1/σ². For n: I_n(μ) = n/σ². CRLB = σ²/n. X̄ achieves this.

### Q10. Derive CRLB for Poisson(λ).
**Model answer:** ℓ(λ) = x log λ − λ − log x!. Score: ∂ℓ/∂λ = x/λ − 1. I(λ) = E[(X − λ)²]/λ² = λ/λ² = 1/λ. For n: I_n(λ) = n/λ. CRLB: λ/n. X̄ achieves this.

---

## Part B: Most Powerful Tests (Q11-20)

### Q11. State the Neyman-Pearson lemma.
**Model answer:** For testing simple H₀: θ = θ₀ vs simple H₁: θ = θ₁, the most powerful test of size α rejects H₀ when L(θ₁|x)/L(θ₀|x) > k, where k is chosen so P(reject | H₀) = α. This likelihood-ratio test is uniformly most powerful (UMP) among all size-α tests.

### Q12. Describe the proof sketch of Neyman-Pearson.
**Model answer:** Consider any other test φ of size ≤ α. Compare expected values under H₁: E_{θ₁}[φ_NP − φ] ≥ 0. Use integral with rejection regions. Difference is positive, showing NP is at least as powerful. Rigorous proof uses indicator functions.

### Q13. Apply NP to simple binomial test.
**Model answer:** H₀: p = p₀ vs H₁: p = p₁ with p₁ > p₀. LR = [p₁/p₀]^X · [(1−p₁)/(1−p₀)]^{n−X}. Reject if large X (since p₁ > p₀). Equivalent to: reject if X > k, where k chosen so P(X > k | p = p₀) = α.

### Q14. Apply NP to simple normal mean test.
**Model answer:** H₀: μ = μ₀ vs H₁: μ = μ₁ with μ₁ > μ₀. LR = exp[(μ₁ − μ₀)·(n·X̄ − n(μ₀+μ₁)/2)/σ²]. Reject if LR > k, equivalent to X̄ > c for some c. Z = (X̄ − μ₀)/(σ/√n) > z_α gives most powerful test.

### Q15. Define uniformly most powerful (UMP) test.
**Model answer:** A test is UMP of size α if for every θ ∈ H₁, its power is at least that of any other size-α test. Stronger than NP (which is MP for specific θ₁). Exists when H₁ is one-sided with monotone likelihood ratio; doesn't exist for two-sided H₁ usually.

### Q16. Describe monotone likelihood ratio (MLR).
**Model answer:** Density family f(x; θ) has MLR in statistic T if f(x; θ₂)/f(x; θ₁) is monotone in T for θ₂ > θ₁. Implies UMP test for one-sided hypotheses: reject for large T. Common in exponential family.

### Q17. UMP tests for one-sided hypotheses.
**Model answer:** For H₀: θ ≤ θ₀ vs H₁: θ > θ₀ with MLR property: UMP test rejects for large T (sufficient statistic). Power monotonically increases as θ moves right. Rare situation where UMP exists.

### Q18. Why doesn't UMP exist for two-sided?
**Model answer:** For H₀: θ = θ₀ vs H₁: θ ≠ θ₀, optimal test for θ > θ₀ differs from optimal test for θ < θ₀. Cannot dominate on both sides simultaneously. Use UMP-unbiased (UMPU) tests that are power-maximising within unbiased class.

### Q19. Describe UMP unbiased (UMPU) tests.
**Model answer:** Tests that are unbiased (power ≥ α for θ ∈ H₁) and UMP within this class. For two-sided problems in exponential family, UMPU tests often exist and correspond to standard tests (e.g., two-sided t-test).

### Q20. Compute the power of UMP test for Normal mean.
**Model answer:** One-sided test for H₀: μ = 0 vs H₁: μ > 0, σ known. Reject if Z > z_α. Power at μ_1: P(Z > z_α | μ_1) = P((X̄ − 0)/(σ/√n) > z_α | μ = μ_1) = P(Z* > z_α − μ_1√n/σ) = 1 − Φ(z_α − μ_1√n/σ). Increases with μ_1, n, α.

---

## Part C: Estimator Properties (Q21-30)

### Q21. Define consistency.
**Model answer:** θ̂_n is consistent for θ if θ̂_n →_p θ as n → ∞. Necessary but not sufficient condition: variance → 0 and bias → 0. MLE consistent under regularity; MoM often consistent too.

### Q22. Prove consistency via MSE.
**Model answer:** If MSE(θ̂_n) → 0 as n → ∞, then θ̂_n →_p θ (by Chebyshev: P(|θ̂_n − θ| > ε) ≤ MSE/ε² → 0). MSE = Var + Bias² — both must vanish.

### Q23. Define asymptotic normality.
**Model answer:** θ̂_n is asymptotically normal if √n(θ̂_n − θ) →_d N(0, σ²(θ)) for some σ²(θ). Allows construction of CIs and tests for large n. MLE is asymptotically normal under regularity with σ² = 1/I(θ).

### Q24. Define asymptotic efficiency.
**Model answer:** Sequence θ̂_n is asymptotically efficient if its asymptotic variance equals the reciprocal of Fisher information: σ²(θ) = 1/I(θ). Achieves CRLB asymptotically. MLE is asymptotically efficient. Other estimators may have variance > 1/I.

### Q25. Prove MLE achieves asymptotic efficiency.
**Model answer:** Under regularity: (1) MLE is consistent. (2) Taylor expansion: √n(θ̂ − θ) ≈ −U(θ)/√n / (−I(θ)/n) = (1/√n)U(θ)/I(θ). By CLT: U(θ)/√n →_d N(0, I(θ)). So √n(θ̂ − θ) →_d N(0, 1/I(θ)).

### Q26. State the invariance property of MLE.
**Model answer:** If θ̂ is MLE of θ, then g(θ̂) is MLE of g(θ) for any function g. Example: σ̂² MLE → σ̂ = √σ̂² MLE of σ. Key property — MLE transforms under reparameterisation.

### Q27. Compare different types of convergence.
**Model answer:** (1) Convergence in probability: P(|X_n − X| > ε) → 0. (2) Almost sure: P(X_n → X) = 1. Strongest. (3) Convergence in distribution: F_{X_n} → F_X. Weakest. Relationships: a.s. → prob → dist. Prob + bounded → a.s. (by subsequences).

### Q28. State the Slutsky theorem.
**Model answer:** If X_n →_d X and Y_n →_p c (constant): X_n + Y_n →_d X + c, X_n · Y_n →_d cX, X_n/Y_n →_d X/c (c ≠ 0). Combines convergence types. Used to derive asymptotic distributions of functions.

### Q29. Apply Slutsky to t-statistic.
**Model answer:** T = (X̄ − μ)/(s/√n) = [(X̄ − μ)/(σ/√n)] × [σ/s]. By CLT: first term →_d N(0,1). By consistency of s (s →_p σ): σ/s →_p 1. By Slutsky: T →_d N(0,1) × 1 = N(0,1). So T is asymptotically standard normal.

### Q30. Describe the delta method.
**Model answer:** If √n(θ̂ − θ) →_d N(0, σ²), and g differentiable at θ with g'(θ) ≠ 0, then √n(g(θ̂) − g(θ)) →_d N(0, [g'(θ)]²σ²). Provides asymptotic distribution of transformations. Used in MLE inference, delta method CIs.

---

## Part D: UMVUE via Rao-Blackwell (Q31-40)

### Q31. Describe the Rao-Blackwell theorem.
**Model answer:** If W unbiased for τ(θ) and T sufficient, then W* = E(W|T) is: (1) unbiased (E(W*) = τ(θ)), (2) has no larger variance (Var(W*) ≤ Var(W)). Conditioning on sufficient statistic can only improve.

### Q32. Describe the Lehmann-Scheffé theorem.
**Model answer:** If T is complete and sufficient for θ, then any unbiased function of T is the UMVUE (uniformly minimum variance unbiased estimator). Unique — two UMVUEs would have variance difference = 0.

### Q33. Outline process for finding UMVUE.
**Model answer:** (1) Find complete sufficient T. (2) If easy: find statistic W = h(T) that is unbiased — then UMVUE. (3) If harder: find any unbiased W; then W* = E(W|T) is UMVUE by Rao-Blackwell + Lehmann-Scheffé.

### Q34. UMVUE for p in Bernoulli.
**Model answer:** T = Σx complete sufficient for p. X̄ = T/n unbiased for p. By Lehmann-Scheffé: X̄ is UMVUE. Variance: p(1−p)/n = CRLB. Efficient: e = 1.

### Q35. UMVUE for p² in Bernoulli.
**Model answer:** T = Σx sufficient complete. Want unbiased for p². E(T(T−1)) = n(n−1)p². So T(T−1)/(n(n−1)) unbiased. By Lehmann-Scheffé: UMVUE. Variance: complicated, smaller than (X̄)² (which is biased for p²).

### Q36. UMVUE for σ² in Normal (μ known).
**Model answer:** T = Σ(X−μ)² complete sufficient. E(T) = nσ². Unbiased: T/n. By Lehmann-Scheffé: UMVUE. Variance: 2σ⁴/n = CRLB. Efficient.

### Q37. UMVUE for σ² in Normal (μ unknown).
**Model answer:** (X̄, T) = (X̄, Σ(X−X̄)²) complete sufficient. s² = T/(n−1) unbiased. UMVUE. Variance: 2σ⁴/(n−1). Greater than CRLB = 2σ⁴/n due to estimating μ.

### Q38. Why can UMVUE miss CRLB?
**Model answer:** CRLB is a lower bound; not always achievable by unbiased estimators. Example: UMVUE of σ² in Normal (μ unknown) has variance 2σ⁴/(n−1) > CRLB = 2σ⁴/n. Cost of estimating unknown μ. Achievability requires exponential family and specific conditions.

### Q39. Alternative: biased estimators with lower MSE.
**Model answer:** MLE σ̂² = (1/n)Σ(X−X̄)² biased (E = σ²(n−1)/n). MSE(MLE) = 2σ⁴(n−1)/n² < 2σ⁴/(n−1) = MSE(UMVUE). MLE has lower MSE despite bias. Stein's paradox: shrinkage estimators (biased) can dominate unbiased in high dimensions.

### Q40. Describe bias-variance trade-off in estimation.
**Model answer:** MSE = Variance + Bias². Unbiased estimators constrain bias = 0. Allowing some bias can reduce variance substantially, improving MSE. Example: ridge regression biased but lower MSE for prediction. UMVUE is optimal within unbiased class; not globally optimal in MSE.

---

## Part E: Admissibility and Minimax (Q41-45)

### Q41. Define admissibility.
**Model answer:** Estimator T is admissible if no other estimator dominates it — i.e., no T' exists with R(θ, T') ≤ R(θ, T) for all θ with strict inequality for some θ. Here R = risk (e.g., MSE). Non-admissible = inadmissible, dominated.

### Q42. What are examples of inadmissible estimators?
**Model answer:** (1) X̄ in n-dimensional normal with n ≥ 3: Stein's paradox — shrinkage James-Stein estimator dominates X̄ (lower MSE for all μ). (2) Any constant estimator is inadmissible (dominated by MLE in limit). Non-trivial to prove inadmissibility.

### Q43. State Stein's paradox.
**Model answer:** In n-dimensional normal (n ≥ 3), MLE X̄ is inadmissible. James-Stein estimator (1 − (n−2)σ²/(|X̄|²))·X̄ has lower MSE everywhere. Counterintuitive — shrinking MLE toward zero dominates. Doesn't apply for n = 1 or 2.

### Q44. Define minimax estimator.
**Model answer:** T* minimax if sup_θ R(θ, T*) = inf_T sup_θ R(θ, T). Minimises worst-case risk. Conservative approach. Exists for many problems. Example: in normal mean estimation, sample mean is minimax under squared loss.

### Q45. Compare UMVUE, admissible, and minimax.
**Model answer:** UMVUE: optimal within unbiased class, not necessarily globally. Admissible: cannot be dominated. Minimax: best worst-case. Relationships: UMVUE may not be admissible (Stein). Minimax often admissible but not always UMVUE. Different optimality criteria emphasising different aspects.

---

## Part F: Application (Q46-50)

### Q46. Show X̄ is UMVUE for Normal(μ, σ²) and efficient.
**Model answer:** (X̄, s²) complete sufficient for (μ, σ²). X̄ unbiased: E(X̄) = μ. By Lehmann-Scheffé: X̄ is UMVUE. Variance = σ²/n. CRLB = σ²/n (known σ). So achieves CRLB — fully efficient.

### Q47. Find UMVUE for parameter of exponential distribution.
**Model answer:** X₁, ..., Xₙ iid Exp(λ). T = Σx sufficient complete for λ (by exponential family property). E(T) = n/λ, so n/T = nX̄⁻¹... wait — correct: E(T) = n/λ, so T/n = X̄ unbiased for 1/λ. By Lehmann-Scheffé: X̄ is UMVUE for 1/λ.

### Q48. Compute Wald test using Fisher information.
**Model answer:** H₀: θ = θ₀. Fisher information I(θ), estimated by I(θ̂). W = (θ̂ − θ₀)²·I(θ̂)/n = n(θ̂ − θ₀)²·I(θ̂). Under H₀ and regularity: W ~_a χ²(1). Critical 3.84 at α = 0.05. Equivalent to Z² test.

### Q49. Apply NP to design optimal test.
**Model answer:** Given power requirements: for specific (α, 1−β, θ₁), find minimum sample size. Use NP test: reject if LR > k, with k from size. Power calculation: P(LR > k | θ₁). Iterate n until power threshold met. Essential in clinical trials, quality control.

### Q50. Describe optimal estimation practice.
**Model answer:** (1) State the model and parameter of interest. (2) Choose estimation criterion: minimum MSE, unbiasedness, efficiency. (3) Identify sufficient statistics. (4) Find MLE; check regularity for asymptotic properties. (5) Consider Rao-Blackwell to improve any unbiased estimator. (6) Check CRLB to assess efficiency. (7) For prediction: consider biased estimators with lower MSE (ridge, shrinkage). (8) Report SE, CI, and optimality criteria.

---

**Exam tip:** For optimal estimators/tests questions, always: (1) state optimality criterion explicitly, (2) identify sufficient statistics and verify completeness, (3) derive CRLB and compare to estimator's variance, (4) apply Rao-Blackwell/Lehmann-Scheffé procedure systematically, (5) for tests: state NP lemma and show likelihood ratio structure, (6) check regularity conditions.
