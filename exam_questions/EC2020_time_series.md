# EC2020 — Time Series Econometrics: 50 Exam Questions with Model Answers

---

## Part A: Fundamentals (Q1-10)

### Q1. Define a time series.
**Model answer:** A sequence of observations on a variable ordered in time: {Y_t}. Key feature: order matters; observations not independent. Examples: GDP, stock prices, unemployment rate. Requires specialised methods due to temporal dependence.

### Q2. Define stationarity.
**Model answer:** A time series is (weakly) stationary if: (1) E(Y_t) = μ (constant mean over time). (2) Var(Y_t) = σ² (constant variance). (3) Cov(Y_t, Y_{t−k}) = γ_k depends only on lag k, not on t. Strictly stationary: joint distribution invariant to time shifts. Key prerequisite for many econometric methods.

### Q3. Why does stationarity matter?
**Model answer:** Non-stationary series cause: (1) Spurious regression — apparent relationships with unrelated non-stationary variables. (2) Invalid t-statistics (non-standard distributions). (3) Inconsistent parameter estimates. (4) Misleading forecasts. Pre-testing for stationarity is essential before standard regression.

### Q4. Describe a random walk.
**Model answer:** Y_t = Y_{t−1} + ε_t, where ε_t is white noise. Non-stationary: Var(Y_t) = tσ² grows with t. Shocks are permanent. Differencing: ΔY_t = ε_t is stationary (white noise). First-difference operator makes it stationary. Classic example of unit root process.

### Q5. Describe white noise.
**Model answer:** Sequence {ε_t} with E(ε_t) = 0, Var(ε_t) = σ², and Cov(ε_t, ε_s) = 0 for t ≠ s. No autocorrelation. Residuals of a correctly specified time-series model should approximate white noise. Key building block in ARIMA models.

### Q6. Define autocovariance and autocorrelation.
**Model answer:** Autocovariance: γ_k = Cov(Y_t, Y_{t−k}). Autocorrelation: ρ_k = γ_k / γ_0, where γ_0 = Var(Y_t). ρ_k measures correlation at lag k, scaled to [-1, 1]. ACF plots ρ_k vs k — diagnoses dependence structure.

### Q7. What is partial autocorrelation?
**Model answer:** PACF at lag k: correlation between Y_t and Y_{t−k} after removing the linear effects of Y_{t−1}, ..., Y_{t−k+1}. Isolates direct effect at lag k. PACF plot cuts off at lag p for AR(p) processes. Used for model identification.

### Q8. State the Wold decomposition.
**Model answer:** Any stationary series can be decomposed as: Y_t = deterministic + Σ ψ_k ε_{t−k}, where ε_t is white noise. Implies any stationary series is equivalent to an MA(∞) process. Theoretical foundation for ARMA models.

### Q9. Describe an AR(1) process.
**Model answer:** Y_t = c + φY_{t−1} + ε_t. Stationary iff |φ| < 1. Mean: μ = c/(1−φ). Variance: σ² / (1−φ²). ACF: ρ_k = φ^k (geometric decay). PACF: cuts off at lag 1. Captures momentum/persistence.

### Q10. Describe an MA(1) process.
**Model answer:** Y_t = c + ε_t + θε_{t−1}. Always stationary (constant mean, finite variance). ACF: ρ₁ = θ/(1+θ²), ρ_k = 0 for k ≥ 2 (cuts off at lag 1). PACF: decays geometrically. Captures short-term shocks.

---

## Part B: ARMA and ARIMA Models (Q11-20)

### Q11. State the general ARMA(p,q) model.
**Model answer:** Y_t = c + φ₁Y_{t−1} + ... + φ_pY_{t−p} + ε_t + θ₁ε_{t−1} + ... + θ_qε_{t−q}. Combines AR and MA components. Stationary iff AR roots outside unit circle. Identifies: AR order from PACF cutoff; MA order from ACF cutoff.

### Q12. Define integration order I(d).
**Model answer:** A series is I(d) if it becomes stationary after d differences. Y_t ~ I(0): already stationary. Y_t ~ I(1): first difference ΔY_t stationary (random walk-like). Y_t ~ I(2): second difference stationary (rare in practice).

### Q13. State the ARIMA(p,d,q) model.
**Model answer:** Apply ARMA(p, q) to the d-th difference of Y_t. Examples: ARIMA(1,1,0) — first-differenced AR(1). ARIMA(0,1,1) — first-differenced MA(1), equivalent to simple exponential smoothing. Used when raw series is non-stationary.

### Q14. Describe the Box-Jenkins methodology.
**Model answer:** Systematic ARIMA model building: (1) Identification — test stationarity, difference if needed, examine ACF/PACF to choose p, q. (2) Estimation — fit parameters via MLE. (3) Diagnostic checking — residuals should be white noise (Ljung-Box test). Iterative: revise model if diagnostics fail.

### Q15. Describe the Ljung-Box Q test.
**Model answer:** Tests H₀: no autocorrelation in residuals up to lag h. Q = n(n+2) Σ ρ̂²_k/(n−k) ~ χ²(h−p−q). Reject H₀ = residuals correlated; model misspecified. Standard post-estimation diagnostic for ARMA models.

### Q16. State information criteria for model selection.
**Model answer:** (1) AIC = 2k − 2ℓ. Tends to overfit. (2) BIC = k log n − 2ℓ. More parsimonious. (3) HQIC = 2k log log n − 2ℓ. Compromise. Select model minimising criterion. BIC consistent for true model; AIC minimises out-of-sample error.

### Q17. What is the characteristic equation of AR(p)?
**Model answer:** 1 − φ₁z − φ₂z² − ... − φ_pz^p = 0. Roots of this polynomial must lie outside the unit circle for stationarity. All |z_i| > 1. Equivalently, eigenvalues of companion matrix inside unit circle. Condition determines whether shocks decay or explode.

### Q18. What is invertibility of an MA process?
**Model answer:** MA(q) is invertible iff roots of θ(z) = 1 + θ₁z + ... + θ_qz^q = 0 lie outside the unit circle. Invertible MA can be expressed as AR(∞), allowing unique parameter identification. Non-invertible MA has multiple representations — problematic for estimation.

### Q19. Describe seasonal ARIMA (SARIMA).
**Model answer:** SARIMA(p,d,q)(P,D,Q)_s extends ARIMA with seasonal components of period s. Seasonal differencing (1 − B^s) removes seasonality. Example: airline model is SARIMA(0,1,1)(0,1,1)_12 for monthly data. Common for monthly or quarterly economic data.

### Q20. What is the backshift operator?
**Model answer:** B^k Y_t = Y_{t−k}. Simplifies notation: AR(1) as (1 − φB)Y_t = ε_t. Differencing: (1 − B)Y_t = ΔY_t. Seasonal: (1 − B^s)Y_t. Enables compact representation of ARIMA models.

---

## Part C: Unit Roots and Cointegration (Q21-30)

### Q21. Define a unit root.
**Model answer:** In AR(p) model, one of the characteristic roots equals 1. Y_t has unit root if its characteristic equation has a root at z = 1. Implies non-stationarity. First differencing often makes it stationary. Y_t = Y_{t−1} + ε_t is the simplest unit root process.

### Q22. Describe the Dickey-Fuller test.
**Model answer:** Tests H₀: unit root (non-stationary). Estimate ΔY_t = α + ρY_{t−1} + ε_t. Test H₀: ρ = 0. Non-standard distribution under H₀ — use DF critical values (stronger than standard t). Extended to include trend: ΔY_t = α + δt + ρY_{t−1} + ε_t.

### Q23. State the augmented Dickey-Fuller (ADF) test.
**Model answer:** Add lags of ΔY_t to control for higher-order autocorrelation: ΔY_t = α + δt + ρY_{t−1} + Σ β_iΔY_{t−i} + ε_t. Test H₀: ρ = 0 using DF critical values. Choose lag length by AIC/BIC. Most commonly used unit root test.

### Q24. Describe the Phillips-Perron (PP) test.
**Model answer:** Non-parametric correction for autocorrelation and heteroscedasticity in DF regression. Same H₀ (unit root) as ADF. Uses HAC correction instead of lags. More robust to serial correlation of unknown form. Often used as robustness check alongside ADF.

### Q25. Describe the KPSS test.
**Model answer:** Reverses hypothesis: H₀: stationarity (around trend), H₁: unit root. Complements ADF — rejecting KPSS + failing to reject ADF → strong evidence of unit root. Failing KPSS and rejecting ADF → strong evidence of stationarity. Used jointly with ADF for robust conclusions.

### Q26. What is spurious regression?
**Model answer:** Apparent significant relationship between non-stationary series that are actually unrelated. Due to common time trends or coincident patterns. Granger-Newbold (1974): regressing one random walk on another gives significant t-stats despite no true relationship. Remedy: check for cointegration or use differenced series.

### Q27. Define cointegration.
**Model answer:** Two (or more) non-stationary (I(1)) series are cointegrated if a linear combination is stationary (I(0)). Indicates a long-run equilibrium relationship. Examples: prices of similar goods, exchange rates, consumption and income. Not spurious — genuine economic link.

### Q28. Describe the Engle-Granger cointegration test.
**Model answer:** Two-step: (1) Regress Y on X (cointegrating regression). (2) Test residuals for unit root using modified DF critical values. If residuals stationary → cointegrated. Limitations: order of variables matters, low power. Works for two variables.

### Q29. Describe the Johansen cointegration test.
**Model answer:** Vector autoregression-based test for cointegration among multiple variables. Tests number of cointegrating vectors via trace and maximum eigenvalue statistics. Allows multiple cointegrating relationships. More powerful than Engle-Granger; standard in modern time-series work.

### Q30. Describe an error correction model (ECM).
**Model answer:** ΔY_t = α + β·ΔX_t + γ(Y_{t−1} − δX_{t−1}) + ε_t. Short-run dynamics (ΔX_t) plus long-run equilibrium correction term (Y_{t−1} − δX_{t−1}). γ < 0: speed of adjustment back to equilibrium. Granger representation theorem: cointegration implies ECM and vice versa.

---

## Part D: Forecasting and Volatility (Q31-40)

### Q31. Describe point forecasting for AR(1).
**Model answer:** For Y_{t+h}: Ŷ_{t+h} = c + φŶ_{t+h−1}. Iterate forward. Long-run forecast: converges to unconditional mean μ = c/(1−φ) as h → ∞. Variance of forecast error grows with horizon.

### Q32. Compute forecast error variance for AR(1) at horizon h.
**Model answer:** Var(Y_{t+h} − Ŷ_{t+h}) = σ² · (1 + φ² + φ^4 + ... + φ^{2(h−1)}) = σ² · (1 − φ^{2h})/(1 − φ²). For large h: approaches σ²/(1−φ²) = unconditional variance. Long-horizon forecasts are very uncertain.

### Q33. Compute prediction interval for a forecast.
**Model answer:** 95% PI: Ŷ_{t+h} ± 1.96 · √Var(Y_{t+h} − Ŷ_{t+h}). Wider at longer horizons. Assumes normality. Valid only if model is correctly specified — structural breaks, regime shifts expand true uncertainty beyond PI.

### Q34. What are common forecast accuracy metrics?
**Model answer:** (1) MSE = (1/n) Σ e²_t. (2) RMSE = √MSE. (3) MAE = (1/n) Σ |e_t|. (4) MAPE = (1/n) Σ |e_t / y_t| × 100%. Unit-dependent vs percentage. Choose based on context: MAPE for cross-series comparison; MSE for statistical optimality.

### Q35. Describe the Diebold-Mariano test.
**Model answer:** Tests equal predictive accuracy of two forecasts. Null: E(loss_1 − loss_2) = 0. Computes mean loss differential and its HAC standard error. Asymptotic z-test. Used to formally compare models — e.g., ARIMA vs structural model. Sensitive to loss function choice.

### Q36. What is ARCH?
**Model answer:** AutoRegressive Conditional Heteroscedasticity. σ²_t = α₀ + α₁ε²_{t−1} + ... + α_qε²_{t−q}. Variance depends on lagged squared shocks. Captures volatility clustering: high-variance periods follow high variance. Common in financial returns.

### Q37. Describe the GARCH(1,1) model.
**Model answer:** σ²_t = α₀ + α₁ε²_{t−1} + β₁σ²_{t−1}. Extends ARCH by including lagged variance. More parsimonious: often GARCH(1,1) fits well. Persistence parameter: α₁ + β₁ close to 1 indicates persistent volatility. Widely used in finance.

### Q38. Describe the ARCH-LM test.
**Model answer:** Tests for ARCH effects in residuals. (1) Estimate original model; obtain residuals. (2) Regress û² on û²_{t−1}, ..., û²_{t−q}. (3) nR² ~ χ²(q). Reject H₀ of no ARCH → heteroscedasticity; model volatility via GARCH.

### Q39. What are structural breaks?
**Model answer:** Fundamental changes in data-generating process — parameters change over time. Examples: oil crisis (1973), financial crisis (2008). Cause: parameter instability, biased estimates, forecast failure. Tests: Chow test (known break date), Bai-Perron (unknown dates). Remedy: model regime changes or use time-varying parameters.

### Q40. Describe the Chow test for structural break.
**Model answer:** Tests whether coefficients differ before and after a specified date. Split sample, estimate separately. F-statistic compares pooled vs separate RSS. H₀: no structural break. Simple but requires known break date. For unknown dates, use Bai-Perron or Quandt-Andrews.

---

## Part E: VAR and Causality (Q41-45)

### Q41. What is a Vector Autoregression (VAR)?
**Model answer:** Multivariate extension of AR: all variables in the system depend on their own lags and lags of other variables. VAR(p): Y_t = c + A₁Y_{t−1} + ... + A_pY_{t−p} + ε_t. Captures interdependencies. Used when theory is agnostic about direction.

### Q42. Define Granger causality.
**Model answer:** X Granger-causes Y if past values of X help predict Y beyond what past values of Y alone can. Test by including lagged X in regression of Y on its own lags; F-test for joint significance of X's lags. Statistical concept, not philosophical causality — X's lags predict Y.

### Q43. Describe impulse response functions.
**Model answer:** In VAR, IRF traces the effect of a one-time shock in one variable on all variables over time. Plot shows dynamic response. Useful for understanding transmission mechanisms. Requires identification (e.g., Cholesky decomposition for orthogonalised IRFs).

### Q44. What is variance decomposition?
**Model answer:** Proportion of forecast error variance of each variable attributed to shocks in each variable. Complement to IRF. Reveals which variables contribute most to uncertainty at different horizons.

### Q45. When should you use ARIMA vs VAR?
**Model answer:** ARIMA: single variable, focus on univariate forecasting. VAR: multivariate system, interactions matter. VAR when: (1) relationships between variables important, (2) theory suggests joint dynamics, (3) Granger causality of interest. ARIMA when: (1) single series is all that matters, (2) no strong theoretical links to other variables.

---

## Part F: Application (Q46-50)

### Q46. You have quarterly GDP data. Walk through the modelling process.
**Model answer:** (1) Plot the series — check for trend, seasonality, structural breaks. (2) ADF test for unit root in levels. If non-stationary, difference; re-test. (3) ACF/PACF of differenced series. (4) Estimate candidate models (e.g., ARIMA(1,1,1), ARIMA(2,1,0), SARIMA with s = 4). (5) Compare AIC/BIC. (6) Ljung-Box on residuals. (7) Forecast out-of-sample; evaluate with RMSE. (8) Update model as new data arrives.

### Q47. A regression of inflation on money supply gives R² = 0.95 over 30 years. Suspicious?
**Model answer:** Likely spurious — both are non-stationary (likely I(1)). Extremely high R² is red flag. (1) ADF tests on each variable. (2) If both I(1), test for cointegration (Engle-Granger or Johansen). (3) If cointegrated, use ECM for long-run and short-run dynamics. (4) If not cointegrated, use differenced series (cointegration relationship doesn't exist). (5) Don't interpret level-level regression coefficients without cointegration evidence.

### Q48. GARCH(1,1) estimates: α₀ = 0.02, α₁ = 0.08, β₁ = 0.90. Evaluate.
**Model answer:** Persistence α₁ + β₁ = 0.98 — highly persistent volatility (near unit root in variance). Typical of financial data (stock returns, exchange rates). Unconditional variance: α₀/(1 − α₁ − β₁) = 0.02/0.02 = 1 (baseline). Shocks decay slowly — volatility is clustered and persistent. For forecasting: model captures "calm" and "turbulent" regimes.

### Q49. Forecast inflation 12 months ahead using ARIMA(1,1,1). Comment on precision.
**Model answer:** (1) Point forecast iterates ARIMA one step at a time. (2) Variance grows with horizon: 12-month forecast variance substantially larger than 1-step. (3) 95% PI widens correspondingly. (4) Assumes stationarity of differenced series and stability of parameters. (5) External shocks (policy changes, crises) can invalidate forecast. (6) Report point forecast and PI; acknowledge structural uncertainty. Consider updating as new data arrives.

### Q50. Describe a complete time-series econometric analysis.
**Model answer:** (1) Plot and inspect for patterns. (2) Test stationarity (ADF, KPSS). (3) If non-stationary, difference appropriately. (4) Identify ARMA structure (ACF/PACF + information criteria). (5) Estimate model (ML preferred). (6) Diagnose residuals (Ljung-Box, ARCH-LM). (7) If multiple series: test cointegration, use ECM/VAR. (8) Consider seasonality (SARIMA). (9) Out-of-sample forecast validation. (10) Compare alternatives; report with uncertainty. (11) Discuss structural breaks and regime changes. (12) Interpret economically — link coefficients to theory.

---

**Exam tip:** For time-series questions, always: (1) check stationarity first (ADF + KPSS), (2) identify model via ACF/PACF patterns, (3) diagnose residuals are white noise (Ljung-Box), (4) compare models via AIC/BIC and out-of-sample performance, (5) warn about structural breaks and non-stationarity, (6) for cointegration: use Engle-Granger or Johansen and estimate ECM, (7) for volatility: model ARCH/GARCH separately.
