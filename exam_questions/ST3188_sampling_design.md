# ST3188 — Sampling Design & Sample Size Determination: 50 Exam Questions with Model Answers

---

## Part A: Sampling Fundamentals (Q1-10)

### Q1. Define the target population and sampling frame.
**Model answer:** Target population: the complete set of units about which inferences are made. Sampling frame: the actual list or procedure from which the sample is drawn. Frame errors (incomplete, outdated, or misaligned frames) cause sampling bias — the sample fails to represent the population.

### Q2. What is a sampling unit?
**Model answer:** The individual element selected in the sampling process. Could be a person, household, firm, or event. Must be clearly defined to avoid ambiguity. For household surveys, the sampling unit is often the household, with within-household selection rules for individuals.

### Q3. Distinguish probability and non-probability sampling.
**Model answer:** Probability: every unit has a known, non-zero probability of selection. Permits valid statistical inference with known error bounds. Non-probability: selection is judgemental or convenient. Cannot calculate sampling error; results are suggestive, not generalisable to population.

### Q4. State the main probability sampling techniques.
**Model answer:** (1) Simple random sampling (SRS). (2) Systematic sampling. (3) Stratified sampling. (4) Cluster sampling. (5) Multistage sampling. Each has specific advantages for different populations and research constraints.

### Q5. State the main non-probability sampling techniques.
**Model answer:** (1) Convenience — whoever is easy to reach. (2) Judgemental — selected by researcher's judgement. (3) Quota — meet pre-specified category counts. (4) Snowball — existing participants refer others. Used when probability sampling is infeasible, but limits inference.

### Q6. Define sampling error vs non-sampling error.
**Model answer:** Sampling error: random variability between sample statistic and population parameter due to only observing a subset. Decreases with larger n. Non-sampling error: systematic errors from design, measurement, non-response, data processing. Often larger than sampling error in practice.

### Q7. Why is random sampling important?
**Model answer:** (1) Eliminates selection bias. (2) Enables probability-based inference (confidence intervals, p-values). (3) Provides representative sample on expectation. (4) Sets theoretical basis for generalisation. Without randomisation, inference is suggestive, not conclusive.

### Q8. What is sampling bias?
**Model answer:** Systematic error due to non-random selection, causing the sample to differ consistently from the population. Sources: (i) frame coverage errors, (ii) self-selection, (iii) non-response bias, (iv) researcher judgement. Cannot be fixed by larger samples — only by better design.

### Q9. Explain the "1936 Literary Digest poll" as a sampling failure.
**Model answer:** Polling 10 million from telephone and auto registries (wealthy biased toward Republicans), predicted Landon to beat Roosevelt. Roosevelt won in landslide. Problems: (1) frame coverage — phones/cars proxy for wealth; (2) response bias. Demonstrates that large non-random samples can be systematically wrong; a small random sample is better.

### Q10. What is a self-weighting sample?
**Model answer:** A sample where each unit has equal probability of selection — like SRS. Analysis requires no weights; simple averages estimate population means. Contrast with stratified or cluster designs where unequal probabilities require design weights in analysis.

---

## Part B: Sampling Methods (Q11-20)

### Q11. Describe simple random sampling (SRS).
**Model answer:** Every unit has equal probability of selection, and every possible sample of size n is equally likely. Implemented via random number generator. Simplest design; basis for theory. Weakness: may not capture rare subgroups; variance can be high if population is heterogeneous.

### Q12. Describe systematic sampling.
**Model answer:** Select every k-th unit from a sorted frame, starting from a random position between 1 and k, where k = N/n. Easier than SRS. Caution: if frame has periodic structure matching k, creates bias (e.g., every 7th unit in a weekly cycle).

### Q13. Describe stratified sampling.
**Model answer:** Divide population into homogeneous strata. Sample within each stratum (often SRS). Ensures representation of each stratum. Can be proportional (by stratum size) or disproportionate (oversample important strata). Reduces sampling variance if strata are more homogeneous than overall population.

### Q14. When should you use stratified sampling?
**Model answer:** When: (1) you have a variable of interest that partitions the population, (2) variation within strata is less than overall variation, (3) stratum-specific estimates are desired, (4) you want to ensure representation of minority groups. Stratification improves precision when strata differ meaningfully on the outcome.

### Q15. Describe cluster sampling.
**Model answer:** Population divided into clusters (e.g., neighbourhoods, schools). Random selection of whole clusters; then sample or census within selected clusters. Cheaper for geographically dispersed populations. Cost: design effect increases variance (due to within-cluster similarity).

### Q16. What is the design effect?
**Model answer:** Deff = actual variance of estimator / variance under SRS. Cluster sampling typically Deff > 1. Stratified sampling often Deff < 1. Effective sample size = n/Deff. Accounts for clustering in sample size calculations and statistical tests.

### Q17. Describe multistage sampling.
**Model answer:** Combines sampling techniques at different levels. E.g., stage 1: randomly select regions (clusters); stage 2: randomly select cities within regions; stage 3: SRS within cities. Balances cost and precision. Common in large national surveys.

### Q18. What is PPS (probability proportional to size) sampling?
**Model answer:** In cluster or multistage sampling, select clusters with probability proportional to their size. Combined with SRS of equal numbers within selected clusters, yields an approximately self-weighting sample. Ensures unbiased estimation despite unequal cluster sizes.

### Q19. Explain quota sampling.
**Model answer:** Non-probability method. Identify key characteristics (age, gender, region) and set quotas matching population distribution. Interviewer selects respondents freely until quotas are met. Fast, cheap. Weaknesses: interviewer selection bias within quotas; unknown probability of selection.

### Q20. Compare stratified and quota sampling.
**Model answer:** Stratified: probability sampling within each stratum; valid statistical inference. Quota: non-probability; selection within quotas is arbitrary. Both match population on known characteristics. Stratified is more rigorous; quota is more practical but inference is limited.

---

## Part C: Sample Size Determination (Q21-30)

### Q21. State the formula for sample size to estimate a mean with margin of error E.
**Model answer:** n = (z_{α/2} · σ/E)² where E is the desired margin of error, σ is the population standard deviation (from pilot or literature), z is critical value for confidence level. Round up.

### Q22. State the formula for sample size to estimate a proportion.
**Model answer:** n = (z_{α/2})² · p(1−p)/E². Use p = 0.5 for conservative (maximum) n when no prior estimate is available. Example: 95% confidence, E = 0.03, p = 0.5 → n = 1.96² · 0.25/0.0009 = 1068.

### Q23. What factors increase required sample size?
**Model answer:** (1) Higher confidence level (e.g., 99% vs 95%). (2) Smaller margin of error (E). (3) Larger population variance (σ²). (4) Closer p to 0.5 (maximum variance for proportions). (5) Design effects (cluster sampling). (6) Anticipated non-response rate.

### Q24. Adjust sample size for finite population correction.
**Model answer:** n_adjusted = n / [1 + (n−1)/N]. When n is a large fraction of N, finite population correction reduces the needed sample. Typically applied when n/N > 0.05. For N = 1000 and n = 200: adjusted n ≈ 200/1.2 = 167.

### Q25. Adjust sample size for expected non-response rate.
**Model answer:** n_target = n_required / response rate. Example: need 400 completes, expect 40% response → survey 1000. Always over-sample to account for non-response. Budget accordingly.

### Q26. State the general formula for sample size given desired statistical power.
**Model answer:** n ≈ (z_{α/2} + z_β)² · σ² / Δ², where Δ = effect size to detect, 1−β = power, α = significance level. For proportion comparison: n per group = (z_{α/2} + z_β)² · 2p̂(1−p̂) / (p₁ − p₂)². Standard tables or power software (G*Power) used.

### Q27. What is statistical power?
**Model answer:** Probability of correctly rejecting a false null hypothesis: Power = 1 − β = P(reject H₀ | H₁ true). Conventionally aim for 0.8. Low power = likely to miss real effects. Determined by effect size, sample size, α, and variability.

### Q28. What is an effect size?
**Model answer:** The magnitude of difference or association, independent of sample size. For means: Cohen's d = (μ₁ − μ₂)/σ. Small = 0.2, medium = 0.5, large = 0.8. For proportions: h = 2·arcsin(√p). For correlation: r itself is the effect size. Report alongside p-values.

### Q29. Why is it unethical to run an underpowered study?
**Model answer:** (1) Low probability of detecting a real effect — waste of participants and resources. (2) Null results are inconclusive (could be no effect OR underpowered). (3) Can lead to false-positive findings being over-interpreted. IRBs require power justification for sample size. Running underpowered pilot is acceptable; underpowered confirmatory study is not.

### Q30. Given a prior estimate r = 0.3 and α = 0.05, required power = 0.8, find n for testing H₀: ρ = 0.
**Model answer:** Use Fisher's z-transformation: z_r = 0.5 ln((1+0.3)/(1−0.3)) = 0.31. Required n ≈ [(z_{α/2} + z_β)/z_r]² + 3 = [(1.96 + 0.84)/0.31]² + 3 = 82. Approximate formula; use software for precise calculation. Minimum sample ~82 to detect r = 0.3 with 80% power at α = 0.05.

---

## Part D: Non-Response and Bias (Q31-40)

### Q31. What are the main sources of non-response?
**Model answer:** (1) Non-contact — cannot reach respondent. (2) Refusal — contacted but declined. (3) Incapacity — unable to respond (language, illness). (4) Partial response — started but didn't complete. Each may introduce bias if correlated with the variable of interest.

### Q32. How to reduce non-response?
**Model answer:** (1) Multiple contact attempts. (2) Interviewer training and matching. (3) Advance notice by letter. (4) Incentives (cash, vouchers). (5) Short, well-designed questionnaires. (6) Multiple modes (web, phone, mail). (7) Clear privacy assurances. Even small improvements in response rate can reduce bias substantially.

### Q33. Define non-response bias.
**Model answer:** Systematic difference between respondents and non-respondents on the variable of interest. Example: people with strong opinions more likely to respond to political surveys. Non-response bias ≈ (difference in means) × (non-response rate). Larger non-response → larger potential bias.

### Q34. How do you assess non-response bias?
**Model answer:** (1) Compare respondents to population via known auxiliary variables (age, gender, region). (2) Wave analysis: compare early vs late responders. (3) Follow-up a non-respondent sub-sample. (4) Sensitivity analyses for different assumptions about non-respondents. (5) Report response rate and likely biases.

### Q35. What is weighting adjustment?
**Model answer:** Assigning weights to respondents to compensate for non-response or unequal selection probabilities. Example: if women are underrepresented, weight their responses higher. Methods: post-stratification, raking (iterative proportional fitting), propensity weighting. Reduces bias but increases variance.

### Q36. Distinguish design weights, non-response weights, and post-stratification weights.
**Model answer:** Design weights: 1/selection probability (e.g., in stratified or cluster sampling). Non-response weights: compensate for differential response. Post-stratification weights: align sample to population on demographic cells. Final weights may be product of all three. Increases SE but reduces bias.

### Q37. Describe the Mahalonobis distance method in matching.
**Model answer:** Multivariate distance metric for matching: d = (X_i − X_j)'Σ⁻¹(X_i − X_j), where Σ is covariance matrix. Treated units matched to controls with smallest distance. Accounts for covariate correlations. Alternative to propensity scores for quasi-experimental matching.

### Q38. What is snowball sampling and its uses?
**Model answer:** Existing participants refer others. Useful for hard-to-reach populations (drug users, rare medical conditions, activists). Chain referrals expand sample. Weaknesses: highly correlated with initial respondents' networks; biased; non-probability. Never a substitute for probability sampling when alternatives exist.

### Q39. What is non-probability quota sampling's limitation for inference?
**Model answer:** Since selection within quotas is non-random, classical inferential statistics (CIs, p-values) lack theoretical basis. Results describe the sample but cannot formally generalise. Practical use: market research where speed trumps rigour. Caution when interpreting as population estimates.

### Q40. What is weighting calibration?
**Model answer:** Adjusting weights iteratively to match known population margins (e.g., gender × age × region distributions). Improves estimation when sample differs from population. Used in government surveys (e.g., US Current Population Survey) and academic research with complex designs.

---

## Part E: Calculations and Examples (Q41-45)

### Q41. A survey needs ±3% margin at 95% confidence, p unknown. Sample size?
**Model answer:** Use p = 0.5 (conservative): n = (1.96)²(0.25)/(0.03)² = 3.8416 · 0.25/0.0009 = 1067. Round up to 1068. Standard for political polls.

### Q42. Estimate mean income within ±$500 at 99% confidence, σ = $5,000.
**Model answer:** z_{0.005} = 2.576. n = (2.576 · 5000/500)² = (25.76)² = 663.5 → 664. Note: higher confidence (99%) requires larger n vs 95%.

### Q43. Sample size for two-proportion comparison: p₁ = 0.4, p₂ = 0.5, α = 0.05, power = 0.8.
**Model answer:** n per group = (z_{0.025} + z_{0.2})² · [p₁(1−p₁) + p₂(1−p₂)] / (p₁−p₂)² = (1.96+0.84)² · (0.24+0.25) / 0.01 = 7.84 · 49 = 385. About 385 per group, 770 total.

### Q44. Population N = 1000, calculated n = 500. Apply finite population correction.
**Model answer:** n_adjusted = 500 / [1 + (500−1)/1000] = 500/1.499 = 333.6 → 334. When sampling a substantial fraction of the population, the finite correction reduces required size.

### Q45. Anticipate 25% response rate; need 400 completes. Target contacts?
**Model answer:** n_target = 400 / 0.25 = 1600. Must contact 1600 to expect 400 completes. Budget for multiple follow-ups to push response rate higher.

---

## Part F: Application (Q46-50)

### Q46. A retailer wants to survey customers across 5 regions. How to design the sample?
**Model answer:** Stratified random sampling. (1) Define strata as regions. (2) Determine sample sizes per region — proportional to region size or equal if subregional estimates needed. (3) SRS within each region. (4) Total n calculated from desired national margin of error plus within-region precision needs. (5) Include design weights if proportionate allocation violated. Report results at national and regional levels.

### Q47. A political pollster in the UK wants to predict an election with ±2% margin. Walk through the design.
**Model answer:** (1) Target margin E = 0.02, confidence 95%, p = 0.5 (conservative) → n ≈ 2401. (2) Stratified by region (or constituency type) and demographics. (3) Use random-digit-dial or online panel for frame. (4) Weight responses by age, gender, region, 2019 vote to match 2024 turnout model. (5) Report with clearly stated assumptions, margin, method. Adjust for non-response bias using wave analysis.

### Q48. A hospital wants to study patient satisfaction. N = 10,000 patients. Estimate proportion satisfied ±2% at 95% confidence.
**Model answer:** (1) n = (1.96)² · 0.5(0.5)/(0.02)² = 2401. (2) Apply finite correction: n_adj = 2401/(1 + 2400/10000) = 2401/1.24 = 1937. (3) Anticipate 70% response rate: contact 1937/0.7 ≈ 2767. (4) Stratify by ward (surgery, medicine, paediatrics) to ensure representation. (5) Use mailed or online questionnaire with follow-up. (6) Assess non-response bias by comparing demographic profile of respondents to hospital population.

### Q49. You need to survey 500 small-business owners. Business register not available. Design?
**Model answer:** Without complete frame, probability sampling is limited. Options: (1) Purchase a commercial list (quality varies). (2) Snowball from business association members. (3) Quota sampling at trade events. (4) Random sampling from tax registries if accessible. Acknowledge coverage limits; use multiple sources. Report sample characteristics compared to national economic data for generalizability assessment. Use weighted analysis if possible.

### Q50. Your survey has 400 responses but you suspect non-response differs by age. How to handle and report?
**Model answer:** (1) Compare sample age distribution to population (census or customer database). If younger people underrepresented, that signals bias. (2) Apply post-stratification weights: sample_weight_i = population_proportion_i / sample_proportion_i, by age cell. (3) Re-estimate key metrics with weighted and unweighted results. (4) Report: response rate, evidence of non-response pattern, sensitivity analysis. (5) Acknowledge residual bias if the outcome is correlated with age in ways not captured by weighting (unobserved variable problem). (6) Recommend additional follow-up with random non-respondent sub-sample in future studies.

---

**Exam tip:** For sampling questions, always: (1) state the target population and sampling frame, (2) identify the appropriate method (justify), (3) calculate required sample size showing the formula used, (4) adjust for non-response and finite population corrections, (5) discuss potential sources of non-sampling error, (6) specify how weights will be applied for unequal selection probabilities.
