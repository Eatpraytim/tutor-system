# ST2134 — Sufficient Statistics: 50 Exam Questions with Model Answers

---

## Part A: Fundamentals (Q1-10)

### Q1. Define a sufficient statistic.
**Model answer:** A statistic T(X) is sufficient for θ if the conditional distribution of the sample given T does not depend on θ. Formally: P(X = x | T = t, θ) = P(X = x | T = t) for all θ. Intuition: T captures "all the information" in X about θ.

### Q2. State the factorisation theorem.
**Model answer:** T(X) is sufficient for θ iff the joint density factorises as: f(x; θ) = g(T(x); θ) · h(x), where g depends on data only through T, and h does not depend on θ. Fundamental tool for identifying sufficient statistics.

### Q3. Why is sufficiency important?
**Model answer:** (1) Data reduction — reduces n observations to one (or few) statistics without losing information about θ. (2) Efficient estimation: any function of sufficient statistic is a legitimate estimator. (3) Rao-Blackwellisation uses sufficient statistics to improve estimators. (4) Computationally simpler inference.

### Q4. Show T = ΣX is sufficient for p in Bernoulli(p).
**Model answer:** Joint density: f(x; p) = Π p^{xᵢ}(1−p)^{1−xᵢ} = p^{Σxᵢ}(1−p)^{n−Σxᵢ}. Factorise: g(T(x); p) = p^T (1−p)^{n−T}, where T = Σxᵢ. h(x) = 1. Hence T = Σxᵢ is sufficient for p.

### Q5. Show T = ΣX is sufficient for λ in Poisson(λ).
**Model answer:** f(x; λ) = Π e^{−λ}λ^{xᵢ}/xᵢ! = e^{−nλ}λ^{Σxᵢ}/Π(xᵢ!). Factorise: g(T; λ) = e^{−nλ}λ^T, h(x) = 1/Π(xᵢ!). T = Σxᵢ is sufficient for λ.

### Q6. Show (ΣX, ΣX²) is sufficient for (μ, σ²) in Normal.
**Model answer:** f(x; μ, σ²) = (2πσ²)^{−n/2} exp[−Σ(xᵢ − μ)²/(2σ²)]. Expand exponent: −(Σxᵢ² − 2μΣxᵢ + nμ²)/(2σ²). So f factorises with g(ΣX, ΣX²; μ, σ²) as the exponential and h(x) = (2π)^{−n/2}. Hence (ΣX, ΣX²) is sufficient.

### Q7. Define minimal sufficient statistic.
**Model answer:** A sufficient statistic T is minimal if every other sufficient statistic is a function of T. Represents the maximum data reduction preserving sufficiency. Unique up to one-to-one transformation. Typically MLE is a function of minimal sufficient statistic.

### Q8. State the Lehmann-Scheffé characterisation of minimal sufficient.
**Model answer:** T is minimal sufficient iff: f(x; θ)/f(y; θ) does not depend on θ if and only if T(x) = T(y). Equivalently, T(x) = T(y) captures when likelihoods are proportional in θ.

### Q9. Show X̄ is minimal sufficient for Normal(μ, 1).
**Model answer:** f(x; μ)/f(y; μ) = exp[−Σ(xᵢ − μ)²/2 + Σ(yᵢ − μ)²/2] = exp[−(Σxᵢ² − Σyᵢ²)/2 + μ(Σxᵢ − Σyᵢ)]. Independent of μ iff Σxᵢ = Σyᵢ, i.e., X̄(x) = X̄(y). Hence X̄ is minimal sufficient.

### Q10. Why do MLEs often equal sufficient statistics?
**Model answer:** MLE maximises L(θ|x), which equals g(T; θ) by factorisation. So MLE maximises g(T; θ) — a function of T only. Hence MLE is a function of sufficient T. Reverse often holds: MLE is (minimal) sufficient.

---

## Part B: The Rao-Blackwell Theorem (Q11-20)

### Q11. State the Rao-Blackwell theorem.
**Model answer:** If W(X) is an unbiased estimator of τ(θ) and T is sufficient for θ, then W*(X) = E(W | T) satisfies: (1) E(W*) = τ(θ) (still unbiased), (2) Var(W*) ≤ Var(W). Conditioning on sufficient statistic cannot increase variance.

### Q12. Prove E(W | T) is unbiased.
**Model answer:** E(W*) = E[E(W | T)] = E(W) (law of iterated expectations) = τ(θ). Unbiasedness preserved.

### Q13. Prove Var(E(W | T)) ≤ Var(W).
**Model answer:** Var(W) = Var(E(W | T)) + E(Var(W | T)). Since E(Var(W | T)) ≥ 0 (variance non-negative), Var(W) ≥ Var(E(W | T)). Equality iff W = W* a.s. (W already function of T).

### Q14. Define complete statistic.
**Model answer:** T is complete for family {f(x; θ)} if: E_θ[g(T)] = 0 for all θ implies g(T) = 0 a.s. Completeness ensures uniqueness of unbiased estimators based on T. Combined with sufficiency, yields UMVUE (Uniformly Minimum Variance Unbiased Estimator).

### Q15. State the Lehmann-Scheffé theorem.
**Model answer:** If T is complete sufficient for θ and W(T) is an unbiased estimator of τ(θ), then W(T) is the UMVUE of τ(θ). Stronger than Rao-Blackwell — provides a unique best estimator within unbiased class.

### Q16. Combine Rao-Blackwell and Lehmann-Scheffé.
**Model answer:** Strategy to find UMVUE: (1) Find any unbiased estimator W. (2) Find complete sufficient statistic T. (3) Compute E(W | T) = W* — this is UMVUE. Alternatively: find any statistic W(T) that's unbiased. By Lehmann-Scheffé, it's UMVUE.

### Q17. Find UMVUE for p in Bernoulli using sufficiency.
**Model answer:** T = ΣX is complete sufficient for p. X̄ = T/n is unbiased: E(X̄) = p. By Lehmann-Scheffé: X̄ is UMVUE of p. Variance: p(1−p)/n. This achieves Cramér-Rao lower bound (1/I(p) = p(1−p)/n).

### Q18. Find UMVUE for μ in Normal(μ, σ²).
**Model answer:** X̄ is sufficient and complete for μ (in exponential family). E(X̄) = μ. By Lehmann-Scheffé: X̄ is UMVUE. Variance: σ²/n.

### Q19. Find UMVUE for σ² in Normal(μ, σ²) with μ known.
**Model answer:** T = Σ(Xᵢ − μ)² sufficient for σ². T/σ² ~ χ²(n), so E(T) = nσ². Unbiased: σ̂² = T/n = (1/n)Σ(Xᵢ − μ)². This is UMVUE. Variance: 2σ⁴/n (achieves CRLB for normal with known mean).

### Q20. Find UMVUE for σ² in Normal(μ, σ²) with μ unknown.
**Model answer:** Both μ and σ² unknown. Sufficient statistic: (X̄, s²) complete sufficient. s² = (1/(n−1))Σ(Xᵢ − X̄)² unbiased: E(s²) = σ². By Lehmann-Scheffé: s² is UMVUE. Variance: 2σ⁴/(n−1).

---

## Part C: Exponential Family (Q21-30)

### Q21. State the general form of exponential family.
**Model answer:** f(x; θ) = h(x)·c(θ)·exp[Σᵢ w_i(θ) t_i(x)]. "Natural" parameters: w_i(θ). "Sufficient" functions: t_i(x). Examples: normal, Poisson, Bernoulli, Gamma, Beta — most standard distributions.

### Q22. State the natural parameter form.
**Model answer:** Reparameterise η_i = w_i(θ). Then f(x; η) = h(x) exp[Σ η_i T_i(x) − A(η)], where A(η) is log-normaliser. Natural parameter space. Common in modern statistics and generalised linear models.

### Q23. Show Bernoulli is exponential family.
**Model answer:** f(x; p) = p^x (1−p)^{1−x} = exp[x log p + (1−x) log(1−p)] = (1−p) · exp[x · log(p/(1−p))]. Natural parameter: η = log(p/(1−p)) (logit). Sufficient: T(x) = x. h(x) = 1. c(p) = 1−p.

### Q24. Show Normal(μ, σ²) is exponential family.
**Model answer:** f(x; μ, σ²) = (2πσ²)^{−1/2} exp[−(x−μ)²/(2σ²)] = (2πσ²)^{−1/2} exp[−x²/(2σ²) + xμ/σ² − μ²/(2σ²)]. Two natural parameters: η₁ = μ/σ², η₂ = −1/(2σ²). Sufficient: T(x) = (x, x²).

### Q25. Show sufficient statistics in exponential family.
**Model answer:** For n iid observations: joint density = Π f(xᵢ; θ). In exponential form: joint has form ~ exp[Σᵢ w_j(θ) · Σᵢ t_j(xᵢ)] × (products of h). Sufficient: T = (ΣT₁, ΣT₂, ...). Fundamental: sums of t_j are sufficient.

### Q26. State properties of sufficient stats in exponential family.
**Model answer:** (1) T = (Σt₁, ..., Σt_k) is sufficient. (2) T is minimal sufficient (for non-degenerate family). (3) T is complete for "full-rank" family. (4) Sample distribution of T is also exponential family. Deep connection between exponential family structure and sufficiency.

### Q27. Describe the MLE in exponential family.
**Model answer:** MLE of natural parameters satisfies: T(x) = E_η[T(X)] (sample sufficient = expected sufficient under fitted η). Regular score equation in exponential family. Closed-form for many distributions; numerical otherwise.

### Q28. Apply exponential family result to Poisson.
**Model answer:** f(x; λ) = e^{−λ}λ^x/x! = (1/x!) exp[x log λ − λ]. Natural parameter: log λ. Sufficient: T(x) = x. For n observations: T_n = Σxᵢ, sufficient. E(T_n) = nλ under correct model. MLE equation: Σx/n = λ, giving λ̂ = X̄.

### Q29. Why is exponential family central in statistics?
**Model answer:** (1) Includes most common distributions. (2) Simple sufficiency structure. (3) Closed-form MLE often. (4) Conjugate priors exist (Bayesian). (5) Generalises to GLMs. (6) Asymptotic properties well understood. (7) Computationally tractable.

### Q30. What distributions are NOT exponential family?
**Model answer:** (1) Uniform(0, θ) — support depends on parameter. (2) Cauchy — no finite moments. (3) Mixtures — not single exponential family member. (4) Other heavy-tailed distributions. Non-exponential distributions often have non-standard sufficient statistics.

---

## Part D: Ancillary and Basu's Theorem (Q31-40)

### Q31. Define an ancillary statistic.
**Model answer:** A statistic A(X) is ancillary for θ if its distribution does not depend on θ. Examples: (1) Normal: sample range is ancillary for μ (if σ known). (2) For location-scale family: (X_i − X̄)/s is ancillary for (μ, σ).

### Q32. State Basu's theorem.
**Model answer:** If T is complete sufficient for θ and A is ancillary for θ, then T and A are independent. Independence under sufficiency + ancillarity + completeness. Powerful tool for independence proofs.

### Q33. Apply Basu to prove X̄ and s² independence under normality.
**Model answer:** In Normal(μ, σ²) with σ² known: X̄ is complete sufficient for μ. Statistic s² depends only on (X − X̄) which is ancillary for μ. By Basu: X̄ and s² independent. Standard proof of this classical result.

### Q34. What is the relationship between sufficiency and ancillarity?
**Model answer:** Sufficient: carries all information about θ. Ancillary: carries no information about θ. Complementary concepts. Together with completeness, Basu's theorem establishes independence. Different "directions" of data structure.

### Q35. Describe conditional inference using ancillary statistics.
**Model answer:** Conditional on ancillary A: base inference on conditional distribution f(T|A; θ). Justified by Basu if conditions hold. Reduces variability; uses only information in T, not A. Common in non-standard problems.

### Q36. Define the sufficiency principle.
**Model answer:** Inference about θ should only depend on the data through a sufficient statistic T. Reasonable: T contains all information. But: a strong principle — sometimes criticised. Forms basis for frequentist inference.

### Q37. Define the likelihood principle.
**Model answer:** Inference about θ should depend on data only through the likelihood function L(θ|x). Equivalent to sufficiency principle plus conditionality principle. Strictly stronger. Adopted by Bayesian statistics; some frequentists oppose.

### Q38. Compare sufficiency and likelihood principles.
**Model answer:** Sufficiency: inference only through sufficient T. Likelihood: inference only through shape of L. Sufficiency weaker. Likelihood principle implies sufficiency. Bayesian: both principles. Frequentist: often only sufficiency; likelihood principle debated.

### Q39. Describe situations where likelihood principle fails (for frequentist).
**Model answer:** Two experiments with different designs but same likelihood. Likelihood principle says inference should be same. Frequentist: p-values can differ (e.g., fixed n vs sequential sampling). Example: binomial (fixed n) vs negative binomial (fixed successes) give same likelihood but different p-values.

### Q40. State the conditionality principle.
**Model answer:** If an experiment E is chosen randomly among several, inference should be conditional on which experiment was actually performed. Combined with sufficiency principle: implies likelihood principle. Strengthens inference by respecting actual observation context.

---

## Part E: Applications (Q41-45)

### Q41. Show (X_(1), X_(n)) is sufficient for (a, b) in Uniform(a, b).
**Model answer:** f(x; a, b) = (1/(b−a))ⁿ · I(a ≤ all xᵢ ≤ b) = (1/(b−a))ⁿ · I(a ≤ X_(1), X_(n) ≤ b). Factorises: g(X_(1), X_(n); a, b) = (1/(b−a))ⁿ · I(a ≤ X_(1), X_(n) ≤ b), h(x) = 1. Hence (X_(1), X_(n)) sufficient.

### Q42. Find UMVUE of θ in Uniform(0, θ).
**Model answer:** X_(n) = max sufficient and complete for θ. E(X_(n)) = nθ/(n+1). Unbiased version: (n+1)/n · X_(n). By Lehmann-Scheffé: (n+1)/n · X_(n) is UMVUE. Variance: θ²/[n(n+2)]. Beats MoM's 2X̄ in MSE.

### Q43. Find UMVUE for 1/λ in Poisson(λ).
**Model answer:** Σxᵢ is complete sufficient for λ. E(X̄) = λ, so X̄ is unbiased for λ. For 1/λ: (n−1)/Σxᵢ unbiased (under Σxᵢ ≥ 1). By Lehmann-Scheffé: (n−1)/Σxᵢ = (n−1)/(nX̄) is UMVUE of 1/λ. Not simply 1/X̄!

### Q44. Apply Rao-Blackwell to improve an estimator.
**Model answer:** Given unbiased W for τ(θ) and sufficient T. Compute E(W | T). Example: for Bernoulli(p), W₁(X) = X₁ unbiased for p (naive). T = Σxᵢ sufficient. E(X₁ | T = t) = t/n = X̄. So W* = X̄ — Rao-Blackwell improves to the UMVUE.

### Q45. Describe importance of completeness alongside sufficiency.
**Model answer:** Sufficient alone: Rao-Blackwell gives an improved estimator, but not necessarily unique minimum variance. Complete + sufficient: Lehmann-Scheffé gives UMVUE. Without completeness: multiple "best" estimators possible; Rao-Blackwell doesn't pin down unique.

---

## Part F: Application (Q46-50)

### Q46. In Gamma(α, β) with α known, find minimal sufficient statistic for β.
**Model answer:** f(x; β) = β^α x^{α−1} e^{−βx}/Γ(α). For n iid: L(β) = β^{nα} (Π xᵢ)^{α−1} e^{−β Σxᵢ}/[Γ(α)]ⁿ. Factorise: g(Σxᵢ; β) = β^{nα} e^{−β Σxᵢ}, h(x) = (Π xᵢ)^{α−1}/[Γ(α)]ⁿ. So Σxᵢ minimal sufficient for β.

### Q47. Compute UMVUE for Poisson(λ) squared parameter λ².
**Model answer:** T = Σxᵢ sufficient. Note E(T) = nλ, E(T²) = (nλ)² + nλ, so E(T(T−1)) = n²λ². Hence T(T−1)/n² is unbiased for λ². By Lehmann-Scheffé: this is UMVUE. Check: E(X̄²) = λ²/n + λ² = λ²(1 + 1/n), biased.

### Q48. Relationship between sufficiency and Bayesian inference.
**Model answer:** Bayesian posterior: π(θ|x) ∝ L(θ|x) · π(θ). By factorisation: L = g(T; θ) · h(x). So π(θ|x) ∝ g(T; θ) · π(θ) — depends on data only through T. Hence T is sufficient for Bayesian analysis too. Sufficiency is fundamental.

### Q49. Design a study using sufficiency principle.
**Model answer:** (1) Identify model family. (2) Find sufficient statistics. (3) Data collection focuses on quantities required to compute T. (4) Inference uses only T. (5) Simplifies reporting, storage, and reanalysis. Example: binomial sample — only need to record count, not each trial.

### Q50. Describe the significance of sufficiency in modern statistics.
**Model answer:** (1) Exact inference: uses full information in T. (2) Bayesian inference: posterior depends only on T. (3) Computational: reduces data to summary statistics. (4) Sufficient statistics define summary measures. (5) Cox's "partial likelihood" extends sufficiency ideas. (6) ML: feature engineering often seeks sufficiency-like summaries. Fundamental concept across all statistical theory.

---

**Exam tip:** For sufficiency questions, always: (1) state factorisation theorem clearly, (2) identify g(T; θ) and h(x) explicitly, (3) compute conditional distribution E(·|T) if Rao-Blackwellising, (4) verify completeness when claiming UMVUE, (5) use Basu's theorem for independence proofs, (6) connect sufficiency to MLE and Bayes.
