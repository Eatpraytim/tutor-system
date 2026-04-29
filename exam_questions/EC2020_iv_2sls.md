# EC2020 — IV, 2SLS & Measurement Error: 50 Exam Questions with Model Answers

---

## Part A: Endogeneity and Its Sources (Q1-10)

### Q1. What is endogeneity?
**Model answer:** A regressor X is endogenous if Cov(X, u) ≠ 0. Violates the zero conditional mean assumption E(u|X) = 0. Consequences: OLS is biased and inconsistent — even in very large samples, β̂ does not converge to β. Inference invalid.

### Q2. State the three main sources of endogeneity.
**Model answer:** (1) Omitted variable bias — relevant variable correlated with X is omitted. (2) Measurement error in X. (3) Simultaneity / reverse causality — Y and X jointly determined (e.g., supply and demand). Each requires different remedies.

### Q3. Why is OLS biased under endogeneity?
**Model answer:** β̂ = β + (X'X)⁻¹X'u. If E(X'u) ≠ 0, then E(β̂) ≠ β. Intuitively: OLS attributes variation in Y correlated with X to β, but some of this variation comes from u (via the endogeneity). The bias persists in large samples — inconsistent.

### Q4. Give a classic example of omitted variable bias.
**Model answer:** Wage regression: wage = β₀ + β₁·educ + u. Ability is omitted; correlated with education (more able students get more education). β̂₁ overestimates the return to education because β̂₁ captures both (i) causal effect of education and (ii) part of the effect of (omitted) ability.

### Q5. Describe classical measurement error.
**Model answer:** True X is measured with error: observed X* = X + e, where e is independent of X and u with E(e) = 0. OLS using X* gives attenuation bias: plim β̂_OLS = β · σ²_X / (σ²_X + σ²_e) < β. OLS underestimates β (biased toward zero).

### Q6. What is simultaneity bias?
**Model answer:** Occurs when Y affects X as well as X affects Y. Example: Price and quantity — consumers respond to price, but producers set price based on quantity. OLS gives neither the supply curve nor the demand curve but a mixture. Requires simultaneous equations or IV methods.

### Q7. How does measurement error in Y differ from measurement error in X?
**Model answer:** Y* = Y + v: effect absorbed into error term, doesn't bias OLS (just reduces efficiency by increasing error variance). X* = X + e: creates correlation between observed X* and error → bias (attenuation). Fundamental asymmetry — measurement error in Y is less problematic.

### Q8. Define "reverse causality".
**Model answer:** When the outcome Y causes the predictor X, not just vice versa. Example: "police presence causes crime" — both may be true, but high-crime areas get more police. OLS confounds. Often addressed via temporal precedence, IV, or natural experiments.

### Q9. What is an instrumental variable?
**Model answer:** A variable Z that: (1) Affects X (relevance, Cov(Z,X) ≠ 0). (2) Does not affect Y directly (exclusion/exogeneity, Cov(Z, u) = 0). Z influences Y only through its effect on X. Enables identification of the causal effect of X on Y even when X is endogenous.

### Q10. What makes a valid IV?
**Model answer:** Both conditions required: (1) Relevance — instrument strongly correlates with endogenous regressor (first-stage F > 10). Testable. (2) Exogeneity (exclusion restriction) — instrument affects Y only through X. Untestable in exactly-identified models; requires theoretical argument. Both must hold.

---

## Part B: 2SLS Estimation (Q11-20)

### Q11. Describe the Two-Stage Least Squares (2SLS) procedure.
**Model answer:** (1) First stage: regress endogenous X on instruments Z (and exogenous regressors W). Get fitted values X̂. (2) Second stage: regress Y on X̂ (and W). Coefficient on X̂ is the 2SLS estimate β̂_2SLS. Consistent if instrument is valid. Use software's 2SLS routine — SE must account for first stage.

### Q12. State the 2SLS estimator in matrix form.
**Model answer:** β̂_2SLS = (X'P_Z X)⁻¹ X'P_Z y, where P_Z = Z(Z'Z)⁻¹Z' is the projection matrix onto Z. X'P_Z X is the cross-product of predicted Xs. Alternatively: β̂_2SLS = (X̂'X)⁻¹ X̂'y, where X̂ = P_Z X.

### Q13. Show that 2SLS is consistent.
**Model answer:** plim β̂_2SLS = β + plim (X'P_Z X / n)⁻¹ · plim (X'P_Z u / n). Under relevance, first term converges to non-singular matrix. Under exclusion (E(Z'u) = 0), plim X'P_Z u / n = 0. Hence plim β̂_2SLS = β — consistent.

### Q14. State the asymptotic variance of 2SLS.
**Model answer:** Asymp Var(β̂_2SLS) = σ² (X'P_Z X)⁻¹. Use σ̂² = (ŷ − Xβ̂_2SLS)'(ŷ − Xβ̂_2SLS)/n. Note: residuals use actual X (not X̂) — common mistake. Robust SE also available: (X'P_Z X)⁻¹ Σ ûᵢ² xᵢxᵢ' (X'P_Z X)⁻¹.

### Q15. Compare OLS and 2SLS standard errors.
**Model answer:** 2SLS SE typically larger than OLS because instruments are less informative than direct regressors. Using Z loses information vs X. Bias-variance trade-off: OLS may be more precise but biased; 2SLS unbiased but less precise. Under endogeneity, 2SLS preferred for unbiasedness.

### Q16. What are just-identified, over-identified, and under-identified models?
**Model answer:** Just-identified: number of instruments (excluded) = number of endogenous regressors. Unique IV estimator. Over-identified: more instruments than endogenous regressors. Can test overidentifying restrictions. Under-identified: fewer instruments than endogenous regressors. IV cannot identify all coefficients.

### Q17. Describe the Sargan test for overidentifying restrictions.
**Model answer:** In over-identified models: H₀: all instruments are exogenous. (1) Compute 2SLS residuals ũ. (2) Regress ũ on all instruments Z (and W). (3) Statistic: nR² ~ χ²(q−p), where q = # instruments, p = # endogenous regressors. Reject H₀ → at least one instrument invalid. Requires exactness of at least some instruments.

### Q18. Compare IV and OLS when both are consistent.
**Model answer:** When X is exogenous, both are consistent but OLS is efficient (minimum variance). IV wastes information. Use OLS unless evidence of endogeneity. Hausman test formalises: if OLS and IV give similar estimates, use OLS for precision; if different, use IV for consistency.

### Q19. Describe the Hausman test.
**Model answer:** Tests H₀: X is exogenous (OLS consistent and efficient) vs H₁: X endogenous (IV consistent). H = (β̂_IV − β̂_OLS)' [Var(β̂_IV) − Var(β̂_OLS)]⁻¹ (β̂_IV − β̂_OLS) ~ χ²(k). Under H₀, should be small. Reject → use IV.

### Q20. State the assumptions of 2SLS for valid inference.
**Model answer:** (1) Relevance: Cov(Z, X) ≠ 0. (2) Exclusion: Cov(Z, u) = 0. (3) No perfect multicollinearity among Z. (4) Sample size adequate for asymptotic approximation. (5) Appropriate SE (conventional or robust). Inference invalid under weak instruments.

---

## Part C: Weak Instruments (Q21-30)

### Q21. What are weak instruments?
**Model answer:** Instruments Z with weak correlation to endogenous X. Symptoms: (1) First-stage F < 10 (Stock-Yogo threshold). (2) Small R² in first stage. (3) 2SLS has large SE despite reasonable n. Weak instruments cause severe bias even in large samples.

### Q22. Describe consequences of weak instruments.
**Model answer:** (1) 2SLS bias toward OLS: plim β̂_2SLS ≈ β + ρ · bias_OLS, where ρ depends on instrument strength. (2) Even huge sample doesn't fix this — weak-instrument bias persists. (3) Standard 2SLS SE unreliable. (4) Conventional tests incorrect. Best: find stronger IVs or use weak-IV-robust inference.

### Q23. State the Stock-Yogo rule of thumb.
**Model answer:** First-stage F > 10 for single endogenous regressor to ensure weak-instrument bias < 10% of OLS bias. More stringent: F > 16.4 for 15% relative bias; 24.6 for 10% relative size of 5% test. Critical values depend on number of instruments and acceptable bias threshold.

### Q24. Describe the first-stage F-statistic.
**Model answer:** Test joint significance of excluded instruments in the first-stage regression. F = [(SSR_R − SSR_U)/q] / [SSR_U/(n−k−1)], where R = without Z's, U = with Z's, q = # excluded instruments. Large F = strong instruments. Report alongside 2SLS estimates.

### Q25. What is the LIML estimator?
**Model answer:** Limited Information Maximum Likelihood. Alternative to 2SLS in overidentified models. Less biased under weak instruments. Computationally different (eigenvalue problem). In Stata: ivreg2 with liml option. Report LIML alongside 2SLS as robustness check.

### Q26. Describe the Anderson-Rubin test.
**Model answer:** Weak-IV-robust test for H₀: β = β₀. Estimate residuals under H₀: ũ(β₀) = y − X·β₀. Test joint significance of Z in regression of ũ on Z. Under H₀, follows F-distribution. Valid even with weak instruments. Provides weak-IV-robust confidence interval.

### Q27. When do standard 2SLS confidence intervals fail?
**Model answer:** Under weak instruments. Conventional CIs assume asymptotic normality of β̂_2SLS, which fails with weak Z. CIs can have incorrect coverage (too narrow). Use: (1) Anderson-Rubin CIs, (2) Conditional likelihood ratio CIs, (3) Bootstrap. Never rely on conventional CIs when F < 10.

### Q28. What is the Cragg-Donald statistic?
**Model answer:** Multivariate generalisation of first-stage F for multiple endogenous regressors. Tests whether instruments collectively identify the endogenous variables. Compare to Stock-Yogo critical values (different tables). Used with multiple endogenous regressors; limited instrument relevance analysis.

### Q29. Strategies for strengthening instruments.
**Model answer:** (1) Find more theoretically-motivated instruments. (2) Combine multiple weak IVs (may increase relevance). (3) Use jackknife IV (jIVE) which has better finite-sample properties. (4) Relax exclusion restriction slightly — use many plausible IVs with sensitivity analysis. (5) Report weak-IV-robust results.

### Q30. Evaluating instrument quality: best practice.
**Model answer:** (1) Report first-stage F. (2) Discuss plausibility of exclusion restriction (theoretical). (3) Run Sargan test for overidentification. (4) Compare 2SLS to OLS (Hausman). (5) Use weak-IV-robust inference where needed. (6) Sensitivity analysis: how robust is β̂ to potentially invalid IVs? Transparency about IV strength is essential.

---

## Part D: Measurement Error (Q31-40)

### Q31. State the classical errors-in-variables assumption.
**Model answer:** X* = X + e, where e is classical measurement error: E(e) = 0, independent of X (Corr(X, e) = 0) and u (Corr(e, u) = 0). Adds noise. Under these, OLS with X* gives attenuation bias.

### Q32. Derive the attenuation bias.
**Model answer:** Y = βX + u. Using X*: Y = βX* − βe + u = βX* + v, where v = u − βe. Cov(X*, v) = Cov(X+e, u−βe) = −βσ²_e. OLS β̂ = Cov(X*, Y)/Var(X*) = β · σ²_X / (σ²_X + σ²_e). Plim β̂ = β · λ, where λ = σ²_X / (σ²_X + σ²_e) < 1.

### Q33. What is the reliability ratio?
**Model answer:** λ = σ²_X / (σ²_X + σ²_e). Proportion of variance in X* that is "signal" vs "noise". Ranges [0, 1]: λ = 1 means no error (perfect measurement); λ = 0.5 means half the variance is error; λ → 0 means mostly noise. Determines attenuation factor.

### Q34. How does measurement error affect multiple regression?
**Model answer:** (1) Measurement error in X_j biases β̂_j toward zero. (2) Also biases other coefficients β̂_k due to correlations. (3) Bias direction and magnitude depend on entire correlation structure. (4) Even if only one variable has measurement error, other coefficients are distorted. Complex to interpret — use IV or replicate measurements.

### Q35. Remedies for measurement error.
**Model answer:** (1) Better measurement instruments. (2) Multiple independent measurements; use average (reduces σ²_e by 1/m for m replicates). (3) Instrumental variable Z for X (must satisfy IV conditions). (4) Errors-in-variables regression (if reliability ratio known). (5) Report acknowledgment in limitations.

### Q36. Compare classical measurement error with Berkson measurement error.
**Model answer:** Classical: X* = X + e (observed = true + error). OLS attenuates. Berkson: X = X* + e (true = observed + error); often in designed experiments. Berkson: OLS is still unbiased (e uncorrelated with X*). Less problematic. Distinguish based on what is known and what is measured.

### Q37. Measurement error in Y — consequences?
**Model answer:** Y* = Y + v. Regression: Y* = βX + u + v = βX + w. OLS remains unbiased: β̂ = β, E(β̂) = β. Increased variance of residuals → larger SE, wider CIs. Less efficient but still consistent. Less problematic than measurement error in X.

### Q38. Non-classical measurement error.
**Model answer:** Measurement error correlated with true value or with u. Examples: (1) Top-coding (high incomes truncated). (2) Recall bias (varies by characteristic). (3) Social desirability bias. Complex — can bias coefficients in unpredictable directions. Requires careful specification.

### Q39. Describe the Frisch-Lovell bound on measurement error bias.
**Model answer:** In bivariate OLS with classical measurement error, the true coefficient β lies between β̂_OLS (attenuated) and the reverse regression coefficient (inflated if regressing X on Y). Provides bounds on β without requiring λ. Useful for sensitivity analysis.

### Q40. Practical advice for research with potential measurement error.
**Model answer:** (1) Use best available measures. (2) Report reliability of measures. (3) Use multiple indicators if possible; combine via factor analysis. (4) Conduct sensitivity analysis: estimate under different error assumptions. (5) Discuss likely direction of bias. (6) Collect validation data (gold standard measurements on subsample). Transparency about measurement limitations.

---

## Part E: True/False and Interpretation (Q41-45)

### Q41. T/F: OLS is consistent under endogeneity as long as n is large enough.
**Model answer:** FALSE. OLS is biased and inconsistent under endogeneity — the bias persists even as n → ∞. Large sample does not fix endogeneity bias. Only instrumental variables, randomised experiments, or careful quasi-experimental designs provide consistent estimates.

### Q42. T/F: Measurement error in X always biases the coefficient toward zero.
**Model answer:** PARTIALLY TRUE. Classical measurement error causes attenuation (toward zero). But non-classical measurement error (correlated with true X or u) can bias in any direction. State assumption explicitly before concluding direction.

### Q43. T/F: If an instrument is statistically significant in the first stage, it's strong.
**Model answer:** PARTIALLY TRUE. Significance (p < 0.05) is necessary but not sufficient for strength. First-stage F > 10 (roughly equivalent to t > 3.2 for single IV) is the operational criterion. Small t-statistic just above 2 indicates weak instrument that may cause 2SLS bias.

### Q44. T/F: The Hausman test always correctly identifies endogeneity.
**Model answer:** FALSE. Hausman tests for differences between OLS and IV estimates. Non-rejection may occur if: (1) instrument is weak (small IV precision), (2) small sample. Failure to reject doesn't prove exogeneity. Should be used alongside theoretical reasoning about endogeneity.

### Q45. T/F: Exclusion restriction can be tested statistically.
**Model answer:** FALSE in just-identified models. Exclusion (Cov(Z, u) = 0) is untestable — u is unobserved. Over-identified models allow Sargan test, but this only checks if instruments agree, not whether at least one is valid. Exclusion restriction requires theoretical justification.

---

## Part F: Application (Q46-50)

### Q46. Distance to college as an IV for education in wage regression.
**Model answer:** (1) Relevance: Distance to nearest college affects education choice (closer → more likely to attend). Test: first-stage regression of education on distance; F-stat should exceed 10. (2) Exclusion: Distance affects wages only through education, not directly. Plausible if location is exogenous (not chosen because of wages). Could be violated if distance correlates with labour market conditions. (3) Use 2SLS: β̂_2SLS captures causal effect of education on wages, avoiding ability bias. Report both OLS (biased) and 2SLS; Hausman to test for endogeneity.

### Q47. Your first-stage F = 6.5. How to proceed?
**Model answer:** Weak instrument — F < 10. (1) Do not rely on conventional 2SLS inference. (2) Report and acknowledge weak IV problem. (3) Use Anderson-Rubin confidence interval (valid with weak IVs). (4) Search for stronger or additional instruments. (5) Consider LIML (more robust to weak IVs than 2SLS). (6) Sensitivity analysis. (7) Report OLS as baseline for comparison. Transparency about limitations.

### Q48. A study IV's education with parental education. Evaluate.
**Model answer:** (1) Relevance: parents' education strongly predicts children's education. Likely strong first stage. (2) Exclusion: debatable. Parents' education may affect child's income through (a) inherited ability/genetics (violates exclusion); (b) networks and resources (violates exclusion); (c) cultural values about work (violates exclusion). (3) Likely NOT valid IV — violates exclusion restriction. Don't trust 2SLS results. Report as sensitivity check only. Better IVs: policy changes, distance to schools.

### Q49. OLS β̂ = 0.08; 2SLS β̂ = 0.15. Hausman p = 0.05. Interpret.
**Model answer:** (1) Hausman reject/marginal — evidence of endogeneity. (2) 2SLS estimate larger than OLS — consistent with attenuation bias from measurement error OR positive OVB actually understated by OLS. (3) Direction suggests naive OLS underestimates true effect. (4) Report 2SLS as primary; OLS as attenuated. (5) Caveat: 2SLS SE typically larger (less precision). (6) Provide theoretical discussion of why endogeneity present (what is omitted or mis-measured).

### Q50. Design an IV study to estimate the effect of police presence on crime.
**Model answer:** (1) Endogeneity: crime → police presence (cities with more crime deploy more police). OLS biased upward or ambiguous. (2) Instruments: (a) Election-driven police budget changes (plausibly exogenous, affects police presence). (b) Federal grants for police (Brown-era spending). (c) Firefighter counts (may proxy general municipal capacity; risky). (3) 2SLS: regress crime on instrumented police presence with city/time controls. (4) Validity checks: first-stage F, theoretical discussion of exclusion, Sargan if over-identified. (5) Compare to OLS — if 2SLS smaller, OLS was upward biased (police deployed to high-crime areas). (6) Alternative: natural experiments (terror alerts) identify exogenous police variation.

---

**Exam tip:** For IV/2SLS questions, always: (1) state the endogeneity problem explicitly, (2) justify relevance (first-stage) AND exclusion (theoretical argument) for each IV, (3) report first-stage F, 2SLS estimate, SE, Sargan (if applicable), (4) compare with OLS and conduct Hausman test, (5) acknowledge limitations and conduct sensitivity analysis, (6) interpret coefficient as causal only if IV assumptions plausible.
