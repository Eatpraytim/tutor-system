# ST2187 — Monte Carlo & Constrained Optimisation: 50 Exam Questions with Model Answers

---

## Part A: Monte Carlo Fundamentals (Q1-10)

### Q1. Define Monte Carlo simulation.
**Model answer:** A computational method that uses repeated random sampling to estimate properties of systems or distributions. For a target quantity θ = E[f(X)], generate random samples X₁,...,Xₙ, compute f(Xᵢ), and estimate θ ≈ (1/n)Σf(Xᵢ). Applications: integration, optimisation, risk analysis, prediction intervals.

### Q2. Why use Monte Carlo?
**Model answer:** (1) When analytical solutions are intractable (complex integrals, multidimensional problems). (2) When real-world experimentation is impossible or expensive. (3) For risk and scenario analysis where uncertainty propagates through a model. (4) For validating analytical approximations empirically.

### Q3. State the law of large numbers as it applies to Monte Carlo.
**Model answer:** If X₁,...,Xₙ are iid with E(X) = μ, then X̄ₙ → μ almost surely (strong LLN) or in probability (weak LLN) as n → ∞. Monte Carlo estimates are consistent — they converge to true values with increasing sample size.

### Q4. What is the standard error of a Monte Carlo estimate?
**Model answer:** SE = σ/√n where σ is the standard deviation of the quantity being estimated. To halve SE, need 4× samples. Accuracy improves slowly — a key limitation of MC for high-precision requirements.

### Q5. Describe inverse transform sampling.
**Model answer:** To sample from distribution F: (1) Generate U ~ Uniform(0,1). (2) Compute X = F⁻¹(U). Then X has distribution F. Requires an invertible CDF. Used to generate non-uniform random variables from uniform ones.

### Q6. Describe acceptance-rejection sampling.
**Model answer:** To sample from density f(x): (1) Choose proposal density g(x) easier to sample from with f(x) ≤ M·g(x). (2) Sample Y ~ g and U ~ Uniform(0,1). (3) Accept X = Y if U ≤ f(Y)/[M·g(Y)], else reject and repeat. Acceptance probability = 1/M.

### Q7. Explain variance reduction techniques.
**Model answer:** Methods to reduce MC estimator variance without increasing sample size: (1) Antithetic variates — use pairs (U, 1−U) to induce negative correlation. (2) Control variates — subtract known-mean auxiliary variable. (3) Stratified sampling — partition domain and sample proportionally. (4) Importance sampling — sample from modified distribution, reweight.

### Q8. What is importance sampling?
**Model answer:** Instead of sampling from f, sample from a different distribution g that emphasises regions where the integrand is large, then reweight: E_f[h(X)] = E_g[h(X)f(X)/g(X)]. Useful when direct sampling from f is inefficient or when estimating tail probabilities.

### Q9. Define a pseudo-random number generator.
**Model answer:** An algorithm producing a deterministic sequence of numbers that appear random. Modern generators (e.g., Mersenne Twister) pass statistical tests for uniformity and independence. They are seeded for reproducibility. True randomness requires physical sources (atmospheric noise, quantum devices).

### Q10. What is a random seed?
**Model answer:** An initial value setting the state of a pseudo-random generator. Setting the same seed reproduces the same sequence of "random" numbers. Essential for reproducible research, debugging, and validation. Common practice: set seed at the start of a simulation.

---

## Part B: Monte Carlo Applications (Q11-20)

### Q11. How do you estimate π using Monte Carlo?
**Model answer:** Generate (X, Y) uniformly on [0,1]². Count fraction falling within the quarter-circle X² + Y² ≤ 1. That fraction ≈ π/4, so π ≈ 4 × (count inside / total count). Converges slowly — requires many samples for high precision.

### Q12. How do you estimate an integral ∫₀¹ f(x) dx by Monte Carlo?
**Model answer:** Generate U₁,...,Uₙ ~ Uniform(0,1). Estimate ∫f(x)dx ≈ (1/n)Σf(Uᵢ). For ∫ₐᵇ f(x) dx, use (b−a)·(1/n)Σf(Xᵢ) with Xᵢ ~ Uniform(a,b). SE of estimate proportional to σ(f)/√n.

### Q13. Describe Monte Carlo option pricing.
**Model answer:** Simulate many stock price paths under risk-neutral dynamics (e.g., geometric Brownian motion). For each path, compute the option payoff at expiry. Price ≈ (1/n)Σ payoffs × e^(−rT). Used for options whose payoff depends on path (Asian, Lookback) where analytical solutions don't exist.

### Q14. Monte Carlo for Value at Risk (VaR).
**Model answer:** Generate many random scenarios of portfolio returns. Compute portfolio value change in each. VaR at α% confidence = negative of the α-th quantile of loss distribution. MC handles non-linear portfolios, fat tails, and correlations that closed-form methods cannot.

### Q15. Bootstrap as a special case of Monte Carlo.
**Model answer:** Bootstrap resamples (with replacement) from the observed data to approximate the sampling distribution of a statistic. It's MC-like but uses empirical distribution rather than a parametric one. Applications: CIs, SE estimates, distribution of complex estimators where analytical SE is intractable.

### Q16. Bootstrap confidence interval construction.
**Model answer:** (1) Draw B = 1,000+ bootstrap samples of size n (with replacement). (2) Compute statistic θ̂*_b for each. (3) Methods: Percentile CI = [θ̂*_{α/2}, θ̂*_{1−α/2}]; bias-corrected (BCa); normal approximation θ̂ ± z_{α/2}·SE*. BCa is most accurate for skewed distributions.

### Q17. When is bootstrap unreliable?
**Model answer:** (1) Small n — bootstrap samples don't capture population variability. (2) Dependent data — need block bootstrap for time series. (3) Maximum/minimum statistics — bootstrap of extremes misleading. (4) Weak conditions for central limit theorem on underlying statistic.

### Q18. Monte Carlo Markov Chain (MCMC) — key concept.
**Model answer:** Generates a correlated sequence of samples from a complex target distribution by constructing a Markov chain whose stationary distribution is the target. Algorithms: Metropolis-Hastings, Gibbs sampler. Used in Bayesian inference for posterior sampling when direct methods fail.

### Q19. What is the Metropolis algorithm?
**Model answer:** Start at x₀. At each step: propose x' from symmetric proposal q(x'|x). Accept with probability min(1, π(x')/π(x)) where π is target density. If accepted, x_{t+1} = x'; else x_{t+1} = x_t. Stationary distribution is π. Burn-in iterations are discarded.

### Q20. How do you validate a Monte Carlo simulation?
**Model answer:** (1) Compare MC results to analytical solutions where available. (2) Check convergence by plotting estimates vs sample size. (3) Replicate with different seeds. (4) Compute MC standard errors and verify they shrink as 1/√n. (5) Sanity-check means, variances, extreme quantiles against expectations.

---

## Part C: Constrained Optimisation Basics (Q21-30)

### Q21. State the standard form of a constrained optimisation problem.
**Model answer:** Minimise f(x) subject to gᵢ(x) ≤ 0 for i = 1,...,m (inequality constraints), hⱼ(x) = 0 for j = 1,...,p (equality constraints). Maximisation is minimisation of −f. x is the decision variable.

### Q22. Define feasible region.
**Model answer:** The set of x satisfying all constraints: F = {x : gᵢ(x) ≤ 0 ∀i, hⱼ(x) = 0 ∀j}. An optimal solution must lie in F. Non-convex feasible regions can yield multiple local optima.

### Q23. State the method of Lagrange multipliers for equality constraints.
**Model answer:** To minimise f(x) s.t. h(x) = 0: form Lagrangian L(x, λ) = f(x) + λh(x). Stationary points satisfy ∇f(x) + λ∇h(x) = 0 and h(x) = 0. Solve this system for candidate optima.

### Q24. State the KKT (Karush-Kuhn-Tucker) conditions.
**Model answer:** For minimise f s.t. g(x) ≤ 0, h(x) = 0: (1) Stationarity: ∇f + Σλᵢ∇gᵢ + Σμⱼ∇hⱼ = 0. (2) Primal feasibility: g ≤ 0, h = 0. (3) Dual feasibility: λᵢ ≥ 0. (4) Complementary slackness: λᵢgᵢ = 0. At optimality, active constraints have λ > 0; inactive constraints have λ = 0.

### Q25. Interpret Lagrange multipliers economically.
**Model answer:** The Lagrange multiplier λᵢ is the shadow price — the marginal change in optimal f per unit relaxation of constraint gᵢ. Business: "if I had one more unit of resource i, my profit would increase by λᵢ". Used to value resources at the margin.

### Q26. Distinguish linear and non-linear optimisation.
**Model answer:** Linear: objective and constraints are all linear functions. Solved by simplex or interior-point methods; global optimum always found. Non-linear: one or more non-linear functions. May have multiple local optima; numerical methods used; global optimum not guaranteed unless problem is convex.

### Q27. Define convex optimisation.
**Model answer:** Minimise a convex function over a convex set. Key property: any local minimum is a global minimum. Many practical problems (LP, QP, SOCP, SDP) are convex. Efficient algorithms exist.

### Q28. State linear programming canonical form.
**Model answer:** Maximise c'x subject to Ax ≤ b, x ≥ 0. c is the objective coefficient vector, A is constraint matrix, b is RHS, x ≥ 0 is non-negativity. The simplex method moves between vertices of the feasible polyhedron toward the optimum.

### Q29. What is duality in linear programming?
**Model answer:** Every LP (primal) has an associated dual LP. Strong duality: optimal primal = optimal dual (under regularity conditions). Dual variables are shadow prices. Solving the dual often provides economic insights and computational advantages.

### Q30. Explain sensitivity analysis in LP.
**Model answer:** How does the optimal solution change with changes in: (i) RHS values b (ranging), (ii) objective coefficients c, (iii) adding/removing constraints. Provides "what-if" analysis without re-solving. Shadow prices and reduced costs directly give these sensitivities within ranges.

---

## Part D: Optimisation Numerical Problems (Q31-40)

### Q31. Minimise f(x,y) = x² + y² subject to x + y = 10.
**Model answer:** Lagrangian L = x² + y² + λ(x + y − 10). ∂L/∂x = 2x + λ = 0. ∂L/∂y = 2y + λ = 0. So x = y. From constraint: 2x = 10, x = y = 5. f* = 25 + 25 = 50. Lagrange multiplier λ = −10 — relaxing the constraint by 1 unit reduces optimal by 10.

### Q32. Find max of f(x,y) = xy subject to x + y = 20.
**Model answer:** L = xy + λ(x + y − 20). ∂L/∂x = y + λ = 0 → y = −λ. ∂L/∂y = x + λ = 0 → x = −λ. So x = y. From constraint: x = y = 10. f* = 100. (AM-GM inequality confirms: product maximised when values equal given fixed sum.)

### Q33. Minimise cost 4x + 3y s.t. 2x + y ≥ 10, x + 3y ≥ 12, x, y ≥ 0. Use vertices.
**Model answer:** Vertices of feasible region: (6, 0), (0, 10), intersection of 2x+y=10 and x+3y=12 solves to 5x = 18, x = 3.6, y = 10 − 7.2 = 2.8. Costs: (6,0) → 24; (0,10) → 30; (3.6, 2.8) → 14.4 + 8.4 = 22.8. Minimum at (3.6, 2.8) with cost 22.8.

### Q34. Economic interpretation: shadow price of constraint "budget ≤ 100" is λ = 5. What does λ = 5 mean?
**Model answer:** Relaxing budget by $1 would increase optimal objective (profit, say) by approximately $5. If obtaining extra budget costs less than $5 per dollar, the firm should expand. Binding constraints (budget fully used) have λ > 0; non-binding constraints have λ = 0.

### Q35. A factory produces products A, B. Profit 3, 5; resource use (machine hrs): 2, 4 per unit, total 40 hrs available. Labour: 3, 2, total 30. Maximise profit.
**Model answer:** Max 3A + 5B s.t. 2A + 4B ≤ 40; 3A + 2B ≤ 30; A, B ≥ 0. Corners: (0,0) → 0; (10, 0) → 30; (0, 10) → 50; intersection of both: 4A + 8B = 80, 3A + 2B = 30; multiply second by 4: 12A + 8B = 120; subtract: 8A = 40, A = 5, B = 7.5. Check: 2(5) + 4(7.5) = 40 ✓, 3(5) + 2(7.5) = 30 ✓. Profit = 15 + 37.5 = 52.5. Optimum at (5, 7.5), profit 52.5.

### Q36. Compute MC estimate of E[X²] for X ~ Uniform(0, 1) with samples 0.2, 0.5, 0.8, 0.1, 0.9.
**Model answer:** Estimate = (1/5)(0.04 + 0.25 + 0.64 + 0.01 + 0.81) = 1.75/5 = 0.35. Analytical answer: E[X²] = 1/3 ≈ 0.333. Estimate close given small sample. SE = σ(X²)/√5 would quantify precision.

### Q37. Using antithetic variates to estimate ∫₀¹ eˣ dx with samples U = 0.3 and (1-U) = 0.7.
**Model answer:** Standard MC with single pair: (e^0.3 + e^0.7)/2 = (1.3499 + 2.0138)/2 = 1.6818. Analytical value: e − 1 = 1.7183. Antithetic pair reduces variance by inducing negative correlation between e^U and e^(1-U) — they cover the function more evenly.

### Q38. Estimate P(X > 2) for X ~ N(0, 1) using 1000 MC samples.
**Model answer:** Generate Z₁,...,Z₁₀₀₀ ~ N(0,1). Estimate = (1/1000) × count(Zᵢ > 2). True value = 1 − Φ(2) = 0.0228. With n = 1000, expected count ≈ 22.8 with SD ≈ 4.7 — estimate ≈ 0.023 with SE ≈ 0.0047.

### Q39. For n = 10,000 MC samples of a statistic with σ = 2, the 95% CI half-width is?
**Model answer:** SE = 2/√10000 = 0.02. Half-width = 1.96 × 0.02 = 0.0392. If true θ = 5, estimate typically falls within [5 − 0.0392, 5 + 0.0392].

### Q40. Bootstrap: 1,000 resamples of a mean. Sample has X̄ = 50, s = 10, n = 25. Compare theoretical vs bootstrap SE.
**Model answer:** Theoretical SE = s/√n = 10/5 = 2. Bootstrap SE: compute X̄ for each of 1,000 bootstrap samples, take SD of those means. For symmetric data, bootstrap SE should be very close to theoretical SE (~2). For small n or skewed data, they may differ.

---

## Part E: True/False and Interpretation (Q41-45)

### Q41. T/F: Monte Carlo always produces the exact answer.
**Model answer:** FALSE. MC produces estimates with sampling error. As n → ∞, estimates converge to truth by LLN, but for any finite n there is uncertainty. Quantify with SE and confidence intervals, not single point estimates.

### Q42. T/F: Variance reduction techniques reduce bias.
**Model answer:** FALSE. Variance reduction techniques (antithetic variates, control variates, importance sampling) reduce the variance of unbiased estimators. They don't introduce bias — they improve precision at given n.

### Q43. T/F: KKT conditions are necessary and sufficient for convex problems.
**Model answer:** TRUE for convex problems satisfying constraint qualification (e.g., Slater's condition). For non-convex problems, KKT are necessary at local optima but not sufficient — a point satisfying KKT need not be a global minimum.

### Q44. T/F: If the Lagrange multiplier for constraint i is zero, constraint i is not binding.
**Model answer:** TRUE by complementary slackness: if λᵢ = 0 and gᵢ(x) ≤ 0, then gᵢ(x) can be < 0 (non-binding) or = 0 (binding with slack multiplier). Conversely, binding constraints (gᵢ = 0) may have λ > 0 (informative) or λ = 0 (degenerate case).

### Q45. T/F: Simplex method is exponential time in the worst case but fast in practice.
**Model answer:** TRUE. Simplex has exponential worst-case complexity on pathological examples (Klee-Minty cubes) but is polynomial-time on average and extremely fast empirically. Interior-point methods are polynomial-time worst-case and competitive for large problems.

---

## Part F: Application (Q46-50)

### Q46. A company wants to estimate the 99th percentile of aggregate loss from 3 lines of business. How to use MC?
**Model answer:** (1) Model each line's loss distribution (e.g., fit from historical data). (2) Model correlations between lines (Gaussian copula or similar). (3) Generate 100,000+ joint samples. (4) Sum to get aggregate loss. (5) 99th percentile = sorted value at position 99,000. (6) Bootstrap or replicate to estimate MC uncertainty. Advantages: handles non-Gaussian tails, correlations, operational realities.

### Q47. Using MC, how do you price an Asian option with payoff based on average price?
**Model answer:** (1) Simulate many risk-neutral stock price paths using geometric Brownian motion. (2) For each path, compute the time-average price. (3) Compute payoff: max(Ā − K, 0) for average-price call. (4) Average payoffs across paths and discount at risk-free rate. (5) Report SE from path variance. Closed-form solutions don't exist for arithmetic Asian options; MC is standard.

### Q48. A portfolio optimisation: maximise return − λ·variance. How to set up and solve?
**Model answer:** Max μ'w − (λ/2)w'Σw s.t. Σw = 1, w ≥ 0 (no short selling). This is a quadratic program (QP). Convex (Σ positive semi-definite). Solve with QP solvers; get efficient frontier by varying λ. Shadow prices on constraints reveal binding restrictions (e.g., which holdings want to go negative).

### Q49. How would you use MC to validate a normal approximation for a statistic?
**Model answer:** (1) Define the statistic T and identify claimed normal approximation parameters. (2) Generate many samples from the underlying distribution; compute T for each. (3) Plot empirical distribution of T. (4) Compare to claimed normal: Q-Q plot, Kolmogorov-Smirnov test. (5) Check sample moments vs normal. (6) Report where approximation works (e.g., n ≥ 30) and where it fails (tail probabilities, small n).

### Q50. Retailer with 3 warehouses, 5 stores, shipping costs known. How to formulate and solve as LP?
**Model answer:** Variables x_{ij} = units shipped from warehouse i to store j. Objective: minimise Σc_{ij}x_{ij}. Constraints: (a) Σⱼ x_{ij} ≤ supply_i for each warehouse, (b) Σᵢ x_{ij} = demand_j for each store, (c) x_{ij} ≥ 0. Solve with simplex/interior-point. Output: optimal shipping plan. Shadow prices on supply constraints = value of extra warehouse capacity; on demand = cost of serving additional demand. Sensitivity analysis informs which constraints to relax first.

---

**Exam tip:** For MC questions, specify: (1) target quantity θ, (2) sampling distribution, (3) estimator, (4) sample size or convergence argument, (5) SE estimate. For optimisation questions: (1) state variables, (2) write objective and constraints in standard form, (3) identify method (Lagrange for equality, KKT for inequalities, LP for linear), (4) interpret shadow prices economically, (5) perform sensitivity analysis.
