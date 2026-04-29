# ST2134 — Sampling Distributions & Point Estimation: 50 Exam Questions with Model Answers

---

## Part A: Estimators and Their Properties (Q1-10)

### Q1. Define a point estimator.
**Model answer:** A statistic θ̂ = T(X₁, ..., Xₙ) that takes the sample and produces a single value intended to approximate the unknown parameter θ. Examples: X̄ estimates μ; s² estimates σ². θ̂ is a random variable with its own sampling distribution.

### Q2. Define unbiasedness.
**Model answer:** Estimator θ̂ is unbiased for θ if E(θ̂) = θ for all θ in the parameter space. Example: X̄ is unbiased for μ. s² is unbiased for σ². MLE of σ² (dividing by n) is biased; bias = −σ²/n. Important but not sufficient alone for good estimation.

### Q3. Define bias formally.
**Model answer:** Bias(θ̂) = E(θ̂) − θ. Can be positive or negative. If E(θ̂) = θ, bias is zero (unbiased). Example: biased MLE of σ² has bias = (n−1)σ²/n − σ² = −σ²/n (underestimates).

### Q4. Define mean squared error (MSE).
**Model answer:** MSE(θ̂) = E[(θ̂ − θ)²]. Measures average squared distance from true value. Decomposition: MSE = Var(θ̂) + [Bias(θ̂)]². Combines precision (variance) and accuracy (bias). Used to compare estimators — lower MSE is better.

### Q5. Derive the MSE decomposition.
**Model answer:** MSE(θ̂) = E[(θ̂ − θ)²] = E[(θ̂ − E(θ̂) + E(θ̂) − θ)²] = E[(θ̂ − E(θ̂))²] + 2E[(θ̂ − E(θ̂))(E(θ̂) − θ)] + (E(θ̂) − θ)². Middle term is 0. So MSE = Var(θ̂) + Bias²(θ̂).

### Q6. Define consistency.
**Model answer:** Estimator θ̂_n is consistent for θ if θ̂_n →_p θ as n → ∞. Equivalent: for any ε > 0, P(|θ̂_n − θ| > ε) → 0. Desirable property — more data brings estimate closer to truth.

### Q7. State Chebyshev-based sufficient condition for consistency.
**Model answer:** If lim E(θ̂_n) = θ (asymptotically unbiased) and lim Var(θ̂_n) = 0, then θ̂_n →_p θ (consistent). Proof via Chebyshev: P(|θ̂ − θ| > ε) ≤ E[(θ̂ − θ)²]/ε² = MSE/ε² → 0.

### Q8. Compare unbiased and biased estimators.
**Model answer:** Unbiased: E(θ̂) = θ. Does not guarantee low variance or good MSE. A biased estimator with lower variance may have lower MSE (bias-variance trade-off). Example: for normal mean, X̄ is unbiased; shrinkage estimators are biased but can have lower MSE in high dimensions (Stein's paradox).

### Q9. Define efficiency of an estimator.
**Model answer:** Efficiency compares variance of an estimator to the Cramér-Rao lower bound (CRLB). An estimator is efficient if its variance equals CRLB. Measures "how much information is extracted" from the sample. MLE is asymptotically efficient under regularity conditions.

### Q10. State the Cramér-Rao lower bound.
**Model answer:** For any unbiased estimator θ̂ of θ: Var(θ̂) ≥ 1/I(θ), where I(θ) = E[(∂log f/∂θ)²] is the Fisher information. No unbiased estimator can have variance below CRLB. Achieved by MLE asymptotically.

---

## Part B: Method of Moments Estimation (Q11-15)

### Q11. Describe the method of moments (MoM).
**Model answer:** Equate population moments to sample moments and solve for parameters. For parameter θ with E(X) = g₁(θ): sample equation X̄ = g₁(θ̂_MoM). Multiple parameters: use more sample moments. Simple, always works; often less efficient than MLE.

### Q12. Method of moments for Normal(μ, σ²).
**Model answer:** E(X) = μ, Var(X) = σ² = E(X²) − μ². Sample: X̄ = μ̂, (1/n)ΣX² = σ̂² + μ̂². So μ̂ = X̄ and σ̂² = (1/n)ΣXᵢ² − X̄² = (1/n)Σ(Xᵢ − X̄)². Same as MLE (divisor n); biased by factor (n−1)/n.

### Q13. Method of moments for Uniform(0, θ).
**Model answer:** E(X) = θ/2. Sample: X̄ = θ̂/2, so θ̂_MoM = 2X̄. Alternative: MLE gives θ̂_MLE = max(X₁, ..., Xₙ) — biased but more efficient. MoM uses only mean, ignoring max information.

### Q14. Method of moments for Gamma(α, β).
**Model answer:** E(X) = α/β, Var(X) = α/β². So E(X)² / Var(X) = α. Sample: α̂ = X̄²/s̃², β̂ = X̄/s̃², where s̃² = (1/n) Σ(Xᵢ − X̄)². Closed form but less efficient than MLE for this distribution.

### Q15. Method of moments for Beta(α, β).
**Model answer:** E(X) = α/(α+β), Var(X) = αβ/[(α+β)²(α+β+1)]. Let μ = E(X), σ² = Var(X). Solve: α+β = μ(1-μ)/σ² − 1. Then α̂ = μ̂(μ̂(1−μ̂)/σ̂² − 1); β̂ = (1−μ̂)(μ̂(1−μ̂)/σ̂² − 1). Works but gets complex.

---

## Part C: Maximum Likelihood Estimation (Q16-30)

### Q16. Define the likelihood function.
**Model answer:** For observed data x₁, ..., xₙ from density f(·|θ): L(θ|x) = Π f(xᵢ|θ). Function of θ (not of x). Gives probability (or density) of observed data under each candidate θ. MLE picks θ maximising L.

### Q17. Define the log-likelihood.
**Model answer:** ℓ(θ) = log L(θ|x) = Σ log f(xᵢ|θ). Easier to maximise than L (turns product into sum, avoids numerical underflow). MLE: same for L and ℓ (log is monotonic). Fundamental building block.

### Q18. Derive MLE for Bernoulli(p).
**Model answer:** L(p) = Π p^{xᵢ}(1−p)^{1−xᵢ} = p^{Σxᵢ}(1−p)^{n−Σxᵢ}. ℓ(p) = (Σxᵢ) log p + (n − Σxᵢ) log(1−p). dℓ/dp = Σxᵢ/p − (n − Σxᵢ)/(1−p) = 0. Solving: p̂ = Σxᵢ/n = X̄.

### Q19. Derive MLE for Normal(μ, σ²) with known σ².
**Model answer:** L(μ) = Π (1/√(2πσ²)) exp[−(xᵢ − μ)²/(2σ²)]. ℓ(μ) = const − (1/(2σ²)) Σ(xᵢ − μ)². dℓ/dμ = (1/σ²) Σ(xᵢ − μ) = 0. Hence μ̂ = X̄. (Same as MoM for μ.)

### Q20. Derive MLE for Normal(μ, σ²) with both unknown.
**Model answer:** ℓ(μ, σ²) = −(n/2) log(2π) − (n/2) log σ² − (1/(2σ²)) Σ(xᵢ − μ)². Setting partial derivatives = 0: ∂ℓ/∂μ = 0 → μ̂ = X̄. ∂ℓ/∂σ² = 0 → σ̂² = (1/n) Σ(xᵢ − X̄)². The MLE for σ² is biased (divisor n, not n−1).

### Q21. Derive MLE for Exp(λ).
**Model answer:** L(λ) = Π λe^{−λxᵢ} = λⁿ e^{−λΣxᵢ}. ℓ(λ) = n log λ − λΣxᵢ. dℓ/dλ = n/λ − Σxᵢ = 0. So λ̂ = n/Σxᵢ = 1/X̄. Sample mean gives estimate of 1/λ.

### Q22. Derive MLE for Poisson(λ).
**Model answer:** L(λ) = Π e^{−λ}λ^{xᵢ}/xᵢ! = e^{−nλ} λ^{Σxᵢ} / Π xᵢ!. ℓ(λ) = −nλ + Σxᵢ log λ − Σ log(xᵢ!). dℓ/dλ = −n + Σxᵢ/λ = 0. So λ̂ = Σxᵢ/n = X̄.

### Q23. Derive MLE for Uniform(0, θ).
**Model answer:** L(θ) = Π (1/θ) · I(0 ≤ xᵢ ≤ θ) = (1/θⁿ) I(max xᵢ ≤ θ). Maximise by taking θ as small as possible subject to θ ≥ max xᵢ. So θ̂_MLE = max(X₁, ..., Xₙ) = X_(n). Not found by taking derivative (support depends on θ).

### Q24. What is the invariance property of MLE?
**Model answer:** If θ̂ is the MLE of θ, then g(θ̂) is the MLE of g(θ) for any function g. Example: if σ̂² is MLE of σ², then σ̂ = √σ̂² is MLE of σ. Useful when target parameter is a transformation of the natural parameter.

### Q25. Is MLE always unbiased?
**Model answer:** No. Example: MLE of σ² for normal sample is biased (divisor n gives E(σ̂²) = (n−1)σ²/n < σ²). However, MLE is asymptotically unbiased under regularity conditions — bias → 0 as n → ∞.

### Q26. State asymptotic properties of MLE.
**Model answer:** Under regularity: (1) Consistency: θ̂_MLE →_p θ. (2) Asymptotic normality: √n(θ̂_MLE − θ) →_d N(0, 1/I(θ)), where I is Fisher information. (3) Asymptotic efficiency: achieves CRLB. (4) Invariance: g(θ̂) is MLE of g(θ).

### Q27. Define Fisher information.
**Model answer:** I(θ) = E[(∂log f(X|θ)/∂θ)²] = −E[∂²log f(X|θ)/∂θ²] (under regularity). Measures the information in one observation about θ. Larger I(θ) = more information; smaller CRLB. For n iid observations: I_n(θ) = n · I(θ).

### Q28. State the Score function.
**Model answer:** Score: U(θ) = ∂log L/∂θ = ∂ℓ/∂θ. Properties: E(U) = 0 under regularity. Var(U) = I(θ). MLE satisfies U(θ̂_MLE) = 0 (score equation). Used in LM (score) tests.

### Q29. Derive the score function for Bernoulli(p).
**Model answer:** ℓ(p) = (Σxᵢ) log p + (n − Σxᵢ) log(1 − p). Score U(p) = Σxᵢ/p − (n − Σxᵢ)/(1 − p). Check E(U) = 0: E(Σxᵢ) = np, so E(U) = np/p − (n − np)/(1 − p) = n − n = 0. ✓

### Q30. Derive the Fisher information for Bernoulli(p).
**Model answer:** I(p) = −E(d²ℓ/dp²) for single observation. ℓ(p) = x log p + (1−x) log(1−p). d²ℓ/dp² = −x/p² − (1−x)/(1−p)². −E of this: p/p² + (1−p)/(1−p)² = 1/p + 1/(1−p) = 1/[p(1−p)]. So I(p) = 1/[p(1−p)]. For n observations: I_n(p) = n/[p(1−p)].

---

## Part D: Asymptotic Inference (Q31-40)

### Q31. State the asymptotic distribution of MLE.
**Model answer:** Under regularity: √n(θ̂_MLE − θ₀) →_d N(0, 1/I(θ₀)). Equivalently, θ̂_MLE ~ N(θ₀, 1/(n·I(θ₀))) approximately. Variance = 1/n·I(θ) — the Cramér-Rao lower bound achieved.

### Q32. Use MLE asymptotic normality for CI.
**Model answer:** Approximate 95% CI for θ: θ̂_MLE ± 1.96 · √(1/(n·I(θ̂))). Plug in θ̂ for unknown I(θ). Valid for large n. Examples: (1) Bernoulli: p̂ ± 1.96 √(p̂(1−p̂)/n). (2) Poisson: λ̂ ± 1.96 √(λ̂/n).

### Q33. Compute information for sample size n.
**Model answer:** For iid sample: total information I_n(θ) = Σ I_1(θ) = n · I_1(θ), where I_1 = information per observation. So information additive under iid. Variance of MLE decreases as 1/n (consistent with increasing information).

### Q34. Describe the Delta method.
**Model answer:** If √n(θ̂ − θ) →_d N(0, σ²) and g is differentiable at θ: √n(g(θ̂) − g(θ)) →_d N(0, [g'(θ)]²σ²). Gives asymptotic distribution of functions of MLE. Application: derive CI for g(θ) from CI for θ.

### Q35. Apply Delta method to log-transformed MLE.
**Model answer:** If λ̂ ~ N(λ, λ/n) (MLE of Poisson rate), consider g(λ) = log λ. g'(λ) = 1/λ. By Delta: log(λ̂) ~ N(log λ, (1/λ)² · λ/n) = N(log λ, 1/(nλ)). CI for log λ: log λ̂ ± 1.96/√(nλ̂). Exponentiate for asymmetric CI for λ.

### Q36. When do regularity conditions fail?
**Model answer:** Key failure: support depends on parameter. Example: Uniform(0, θ) — MLE is θ̂ = max(Xᵢ), not normally distributed asymptotically. Rate of convergence is n, not √n. Distribution of n(θ − θ̂)/θ converges to Exp(1). Distinct from standard asymptotics.

### Q37. Asymptotic distribution of MLE for Uniform(0, θ).
**Model answer:** θ̂_MLE = X_(n) = max. P(X_(n) ≤ x) = (x/θ)^n for x ∈ [0, θ]. Let Y_n = n(θ − X_(n))/θ. P(Y_n > y) = P(X_(n) < θ − θy/n) = (1 − y/n)^n → e^{−y}. So Y_n →_d Exp(1). Non-standard asymptotics.

### Q38. Describe the likelihood ratio (LR) statistic.
**Model answer:** For testing H₀: θ = θ₀: LR = 2[ℓ(θ̂) − ℓ(θ₀)]. Under H₀ and regularity: LR →_d χ²(1). Larger LR = more evidence against H₀. For multi-parameter: LR = 2[ℓ(θ̂) − ℓ(θ̃)], where θ̃ is constrained MLE. df = # restrictions.

### Q39. Describe the Wald statistic.
**Model answer:** Tests H₀: g(θ) = 0. W = g(θ̂)'[Var(g(θ̂))]⁻¹g(θ̂). Under H₀ and regularity: W →_d χ²(q). Uses unrestricted MLE θ̂. Simple: no constrained estimation needed. Asymptotically equivalent to LR and score tests.

### Q40. Compare LR, Wald, and score tests.
**Model answer:** All asymptotically equivalent under H₀ and regularity. LR: requires estimating under H₀ and H₁. Wald: only unrestricted. Score: only restricted. In finite samples: LR ≥ score (often), Wald depends on parameterisation. LR preferred for its invariance to parameterisation; score useful when unrestricted estimation difficult.

---

## Part E: Numerical and Conceptual (Q41-45)

### Q41. Compute bias of biased MLE of σ² for n = 20.
**Model answer:** σ̂²_MLE = (1/n)Σ(Xᵢ − X̄)². E(σ̂²_MLE) = (n−1)σ²/n = 19σ²/20. Bias = E(σ̂²_MLE) − σ² = −σ²/20 = 0.05σ². Unbiased version: s² = σ̂²_MLE · n/(n−1) = (1/(n−1))Σ(Xᵢ − X̄)².

### Q42. Compare MSE of σ̂²_MLE and s² for n = 10, σ² = 1.
**Model answer:** s² is unbiased: MSE(s²) = Var(s²) = 2σ⁴/(n−1) = 2/9 ≈ 0.222. σ̂²_MLE: biased. E(σ̂²_MLE) = 0.9. Var(σ̂²_MLE) = (n−1)²/n² · 2σ⁴/(n−1) = (n−1)/n · 2σ⁴/n = 9·2/100 = 0.18. MSE = Var + Bias² = 0.18 + 0.01 = 0.19. So MLE has lower MSE despite bias!

### Q43. Compute Fisher information for Poisson(λ).
**Model answer:** ℓ(λ) = x log λ − λ − log(x!). d²ℓ/dλ² = −x/λ². I(λ) = −E(−x/λ²) = E(X)/λ² = λ/λ² = 1/λ. For n observations: I_n(λ) = n/λ. Asymptotic variance of λ̂_MLE = 1/(n · 1/λ) = λ/n. So λ̂_MLE ~ N(λ, λ/n).

### Q44. Apply CRLB to sample mean.
**Model answer:** For Normal(μ, σ²) with known σ²: I(μ) = 1/σ². CRLB = 1/(n · 1/σ²) = σ²/n. X̄ has Var(X̄) = σ²/n = CRLB. Hence X̄ is efficient. Similarly for other unbiased estimators achieving CRLB — they're minimum variance among unbiased.

### Q45. Show MLE achieves CRLB asymptotically.
**Model answer:** Under regularity: √n(θ̂_MLE − θ) →_d N(0, 1/I(θ)). Asymptotic variance = 1/(n · I(θ)) = CRLB. So MLE is asymptotically efficient. In finite samples, MLE may or may not achieve CRLB depending on model.

---

## Part F: Application (Q46-50)

### Q46. Derive MLE for Gamma(α, β) with known α.
**Model answer:** L(β) = Π (β^α xᵢ^{α−1} e^{−βxᵢ})/Γ(α). ℓ(β) = nα log β − β Σxᵢ + const. dℓ/dβ = nα/β − Σxᵢ = 0. So β̂ = nα/Σxᵢ = α/X̄. For α unknown: requires numerical solution (trigamma function).

### Q47. MLE of Binomial(n, p) with n known.
**Model answer:** Single observation X ~ Bin(n, p). L(p) = C(n, x) p^x (1−p)^{n−x}. ℓ(p) = x log p + (n−x) log(1−p) + const. dℓ/dp = x/p − (n−x)/(1−p) = 0. Solving: p̂ = x/n (sample proportion).

### Q48. Compare MoM and MLE for Uniform(0, θ) with n = 20.
**Model answer:** MoM: θ̂_MoM = 2X̄. Unbiased. Var(θ̂_MoM) = 4 · Var(X̄) = 4 · (θ²/12)/20 = θ²/60 ≈ 0.017θ². MLE: θ̂_MLE = max(Xᵢ). Biased (underestimates). Var(θ̂_MLE) = nθ²/[(n+1)²(n+2)] = 20θ²/[21²·22] ≈ 0.00204θ². MSE(MLE) = Var + Bias² ≈ 0.0021θ² + 0.0023θ² ≈ 0.0044θ². MSE(MoM) = Var ≈ 0.017θ². MLE much better despite bias.

### Q49. Large-sample hypothesis test using MLE.
**Model answer:** H₀: θ = θ₀ vs H₁: θ ≠ θ₀. MLE θ̂ ≈ N(θ, 1/(nI(θ))). Under H₀: Z = (θ̂ − θ₀)·√(nI(θ̂)) ≈ N(0, 1). Reject H₀ if |Z| > 1.96. Equivalent Wald test. For one-sided: compare to 1.645.

### Q50. Describe a complete point-estimation analysis.
**Model answer:** (1) Specify distribution family f(x|θ). (2) Obtain data x₁, ..., xₙ. (3) Choose method (MoM, MLE). (4) Compute estimator θ̂. (5) Assess properties: bias, MSE, consistency. (6) Compute standard error √(1/(nI(θ̂))). (7) Construct CI: θ̂ ± 1.96·SE. (8) Test hypotheses using asymptotic normality. (9) Report estimate, SE, CI with sample size and assumed distribution. (10) Check assumptions and sensitivity.

---

**Exam tip:** For point estimation questions: (1) write likelihood explicitly and take logs, (2) derive score, set to zero for MLE, (3) compute Fisher information via second derivatives, (4) state asymptotic distribution, (5) verify unbiasedness (not guaranteed for MLE), (6) compute MSE = Var + Bias², (7) compare estimators on MSE, not bias alone.
