# ST2187 — Time Series Analysis: 50 Exam Questions with Model Answers

---

## Part A: Definitions and Components (Q1-10)

### Q1. What are the four classical components of a time series?
**Model answer:** (1) Trend (T) — long-term directional movement. (2) Seasonality (S) — regular pattern of fixed period (e.g., quarterly sales peaks). (3) Cyclical (C) — longer-term fluctuations of varying period (e.g., business cycles). (4) Irregular / Random (I) — unpredictable noise.

### Q2. Compare additive and multiplicative time-series models.
**Model answer:** Additive: Y_t = T_t + S_t + C_t + I_t — appropriate when seasonal amplitude is roughly constant. Multiplicative: Y_t = T_t × S_t × C_t × I_t — appropriate when seasonal swings grow/shrink proportionally with the level. Take logs of multiplicative to convert to additive.

### Q3. What is stationarity?
**Model answer:** A time series is strictly stationary if its joint distribution is invariant to time shifts. Weakly (covariance) stationary: constant mean, constant variance, and autocovariance depending only on lag (not time). Most econometric methods assume weak stationarity.

### Q4. Why is stationarity important?
**Model answer:** Stationarity ensures statistical properties are stable over time, making estimation and inference valid. Non-stationary series lead to spurious regressions (apparent significance with nonsense relationships) and invalid t-statistics. Many models (ARMA, OLS) require stationary data.

### Q5. Define a random walk.
**Model answer:** Y_t = Y_{t-1} + ε_t where ε_t is white noise. It is non-stationary — variance grows linearly with t, and shocks have permanent effects. Stock prices are often modelled as random walks. First differencing makes it stationary: ΔY_t = ε_t.

### Q6. What is a unit root?
**Model answer:** A unit root in an AR process means the characteristic equation has a root equal to 1, implying non-stationarity. For AR(1): Y_t = φY_{t-1} + ε_t, a unit root means φ = 1. The process integrates shocks permanently rather than reverting to a mean.

### Q7. Describe the Augmented Dickey-Fuller (ADF) test.
**Model answer:** Tests H₀: unit root (non-stationary) vs H₁: stationary. Regress ΔY_t = α + βt + γY_{t-1} + Σδ_iΔY_{t-i} + ε_t and test H₀: γ = 0. Compare to ADF critical values (not standard t). Reject H₀ = series is stationary.

### Q8. Define autocorrelation.
**Model answer:** The correlation between Y_t and Y_{t-k} for lag k: ρ_k = Cov(Y_t, Y_{t-k})/Var(Y_t). Autocorrelation function (ACF) plots ρ_k vs k. Non-zero autocorrelation indicates dependence over time.

### Q9. Define partial autocorrelation.
**Model answer:** The PACF at lag k is the correlation between Y_t and Y_{t-k} after removing the influence of Y_{t-1},...,Y_{t-k+1}. It isolates the direct effect at lag k. Used to identify AR order — PACF cuts off after lag p for AR(p).

### Q10. What is white noise?
**Model answer:** A sequence {ε_t} with E(ε_t) = 0, Var(ε_t) = σ² (constant), and Cov(ε_t, ε_s) = 0 for t ≠ s. It has no predictable pattern. Residuals from a good time-series model should approximate white noise.

---

## Part B: Forecasting Methods (Q11-20)

### Q11. Describe simple moving averages.
**Model answer:** SMA_t = (Y_t + Y_{t-1} + ... + Y_{t-k+1})/k. Smooths noise by averaging the last k periods equally. Longer windows smooth more but lag more. Used for de-trending and visual smoothing, not sophisticated forecasting.

### Q12. What is exponential smoothing?
**Model answer:** Ŷ_{t+1} = αY_t + (1−α)Ŷ_t where 0 < α < 1. Recent observations weighted more heavily; weights decay geometrically. α close to 1 = responsive to recent changes; α close to 0 = stable.

### Q13. State Holt's linear trend method.
**Model answer:** Combines level and trend components:
- Level: L_t = αY_t + (1−α)(L_{t-1} + T_{t-1})
- Trend: T_t = β(L_t − L_{t-1}) + (1−β)T_{t-1}
- Forecast: Ŷ_{t+h} = L_t + h·T_t
Two smoothing parameters α, β ∈ (0,1).

### Q14. State Holt-Winters seasonal method.
**Model answer:** Extends Holt's method with a seasonal component S_t, updated with parameter γ. Additive: Ŷ_{t+h} = L_t + h·T_t + S_{t+h−m}. Multiplicative: Ŷ_{t+h} = (L_t + h·T_t) × S_{t+h−m}. Where m = seasonal period.

### Q15. What is an ARIMA(p,d,q) model?
**Model answer:** AutoRegressive Integrated Moving Average. p = AR order, d = degree of differencing to achieve stationarity, q = MA order. ARIMA(0,1,0) is a random walk. ARIMA(1,1,1) is common for trending data.

### Q16. Describe the Box-Jenkins methodology.
**Model answer:** Three-step iterative process: (1) Identification — check stationarity (ADF), difference if needed, examine ACF/PACF to choose p, q. (2) Estimation — fit the chosen ARIMA by MLE. (3) Diagnostic checking — residual ACF should show white noise; Ljung-Box test confirms.

### Q17. State the Ljung-Box test.
**Model answer:** Tests H₀: residuals are white noise up to lag h vs H₁: at least one autocorrelation is non-zero. Statistic Q = n(n+2)·Σρ²_k/(n−k) ~ χ²(h−p−q). Reject H₀ = model mis-specified; autocorrelation remains in residuals.

### Q18. Compare AR(1) and MA(1) models.
**Model answer:** AR(1): Y_t = φY_{t-1} + ε_t — persistent shocks decay geometrically. PACF cuts off at lag 1; ACF decays. MA(1): Y_t = ε_t + θε_{t-1} — shocks only last 1 period. ACF cuts off at lag 1; PACF decays.

### Q19. How is seasonality modelled in ARIMA?
**Model answer:** SARIMA(p,d,q)(P,D,Q)_s extends ARIMA with seasonal components of period s. Seasonal differencing (1−B^s) removes periodic patterns. Example: monthly data with annual pattern uses s = 12.

### Q20. What is forecast horizon and why does accuracy degrade?
**Model answer:** The number of periods ahead (h) that we forecast. Accuracy degrades because: (i) forecast errors accumulate, (ii) model misspecification amplifies over longer horizons, (iii) structural changes may occur. Prediction intervals widen with h. Short-horizon forecasts are generally more reliable.

---

## Part C: Decomposition and Adjustments (Q21-30)

### Q21. Explain classical decomposition.
**Model answer:** Decomposes Y_t = T_t + S_t + R_t (additive) or T_t × S_t × R_t (multiplicative). Typically: (1) estimate T by centred moving average, (2) de-trend to get seasonal + residual, (3) average across seasons for each season index, (4) residual = observed − estimated T and S.

### Q22. Describe seasonal indexes.
**Model answer:** Seasonal indexes quantify the deviation of each period from the trend. For additive: average deviation per season. For multiplicative: average ratio of actual to trend. Normalised so they average to 0 (additive) or 1 (multiplicative).

### Q23. Explain a centred moving average for even-period seasonality.
**Model answer:** For quarterly data, a 4-quarter MA is not centred on a specific quarter. Take a 2-step process: compute a 4-term MA, then a 2-term MA of those. This yields values centred on original periods, providing a smooth trend estimate.

### Q24. What is seasonal adjustment?
**Model answer:** Removing the seasonal component to reveal underlying trend/cyclical movements. Additive: Y_t − S_t. Multiplicative: Y_t / S_t. Used in economic indicators (e.g., unemployment figures reported seasonally adjusted).

### Q25. Compare X-13 ARIMA-SEATS and STL decomposition.
**Model answer:** X-13 ARIMA-SEATS: model-based, handles outliers and calendar effects, industry standard for official statistics. STL (Seasonal and Trend decomposition using Loess): non-parametric, handles any seasonality period, robust to outliers, simpler. STL is easier; X-13 is more thorough for economic time series.

### Q26. Define autoregressive order p.
**Model answer:** The number of lagged values of Y included as predictors. AR(p): Y_t = φ₁Y_{t-1} + φ₂Y_{t-2} + ... + φ_pY_{t-p} + ε_t. Higher p captures more complex dependencies but requires more parameters.

### Q27. What conditions ensure AR(1) stationarity?
**Model answer:** AR(1) Y_t = φY_{t-1} + ε_t is stationary iff |φ| < 1. If φ = 1, it is a random walk (non-stationary). If |φ| > 1, explosive (non-stationary). For AR(p), all roots of the characteristic polynomial must lie outside the unit circle.

### Q28. What is cointegration?
**Model answer:** Two non-stationary series X_t, Y_t are cointegrated if a linear combination aX_t + bY_t is stationary. Indicates a long-run equilibrium relationship. Test with Engle-Granger or Johansen procedures. If cointegrated, use error-correction models, not simple differences.

### Q29. Describe error correction models (ECM).
**Model answer:** Models short-run dynamics while preserving long-run equilibrium: ΔY_t = α + β·ΔX_t + γ(Y_{t-1} − δX_{t-1}) + ε_t. The term (Y − δX) is the disequilibrium; γ < 0 measures speed of return to equilibrium.

### Q30. State the lag length selection criteria.
**Model answer:** (1) AIC = −2 log L + 2k — lower is better; tends to overfit. (2) BIC = −2 log L + k·log(n) — penalises more heavily; consistent. (3) HQIC = −2 log L + 2k·log(log n) — compromise. Choose p, q minimising chosen criterion.

---

## Part D: Numerical Computations (Q31-40)

### Q31. Given data 10, 12, 15, 14, 16, 18, 17, 20, compute 3-period MA at t = 4.
**Model answer:** MA₄ = (15 + 14 + 16)/3 = 45/3 = 15.0 (using Y₃, Y₄, Y₅) or centred at t = 4: (12 + 15 + 14)/3 = 41/3 = 13.67. Specify the convention — usually centred MA uses the current observation and the surrounding ones.

### Q32. Apply exponential smoothing with α = 0.3, Y₁ = 100, Y₂ = 110, Y₃ = 105. Find Ŷ₄.
**Model answer:** Ŷ₂ = Y₁ = 100. Ŷ₃ = 0.3(110) + 0.7(100) = 33 + 70 = 103. Ŷ₄ = 0.3(105) + 0.7(103) = 31.5 + 72.1 = 103.6.

### Q33. AR(1) with φ = 0.8, Y_{t−1} = 50, ε_t = 2. Find Y_t.
**Model answer:** Y_t = 0.8(50) + 2 = 40 + 2 = 42. The high φ indicates strong persistence — shocks decay slowly.

### Q34. Given ACF values: ρ₁ = 0.7, ρ₂ = 0.5, ρ₃ = 0.3, ρ₄ = 0.15. What model is suggested?
**Model answer:** Exponentially decaying ACF suggests AR process. If PACF cuts off sharply at lag 1, AR(1) with φ ≈ 0.7. The ratio ρ_k/ρ_{k−1} ≈ 0.7 confirms AR(1) structure where ρ_k = φ^k.

### Q35. Compute seasonal index for Q1 if de-trended ratios are 0.85, 0.88, 0.87.
**Model answer:** Q1 seasonal index = average = (0.85 + 0.88 + 0.87)/3 = 0.867. Q1 sales are typically 86.7% of the trend value — below average (typical for off-peak quarter).

### Q36. MSE = 100, MAE = 8. Which is easier to interpret and why?
**Model answer:** MAE is easier: average forecast error in original units (8 units). MSE = 100 implies RMSE = 10 units. MSE penalises large errors more heavily (quadratic). Use MAE for interpretability; use MSE/RMSE when large errors are especially costly.

### Q37. Apply Holt's method: L_{t−1} = 100, T_{t−1} = 5, Y_t = 108, α = 0.4, β = 0.3. Compute L_t, T_t.
**Model answer:** L_t = 0.4(108) + 0.6(100 + 5) = 43.2 + 63 = 106.2. T_t = 0.3(106.2 − 100) + 0.7(5) = 1.86 + 3.5 = 5.36. Forecast Ŷ_{t+1} = L_t + T_t = 106.2 + 5.36 = 111.56.

### Q38. Given RMSE = 12 and mean Y = 50, assess forecast quality.
**Model answer:** Relative RMSE = 12/50 = 24%. This is high — forecasts typically miss by about a quarter of the mean. Depends on context: for volatile series, acceptable; for stable demand, poor. Benchmark against a naive forecast (Ŷ_t = Y_{t-1}) to assess genuine improvement.

### Q39. Box-Jenkins identification: ACF decays gradually, PACF cuts off after lag 2. What model?
**Model answer:** AR(2). Gradual ACF decay indicates AR component; PACF cut-off at lag 2 identifies the order. Try Y_t = φ₁Y_{t-1} + φ₂Y_{t-2} + ε_t. Verify with residual diagnostics.

### Q40. ARIMA(0,1,1) is equivalent to what simple method? Explain.
**Model answer:** ARIMA(0,1,1) is equivalent to simple exponential smoothing. It models ΔY_t = ε_t + θε_{t−1}, and the corresponding level update is a weighted average of the observation and the prior level — the exponential smoothing formula. The relationship: α = 1 + θ.

---

## Part E: Interpretation and Diagnostics (Q41-45)

### Q41. Residual ACF shows significant spike at lag 12 (monthly data). What does this suggest?
**Model answer:** Seasonal autocorrelation not captured by the model. Add a seasonal AR or MA term at lag 12 (SARIMA with period 12). Alternatively, apply seasonal differencing before fitting. Re-check ACF of new residuals.

### Q42. Durbin-Watson = 0.8 in time series OLS. Interpret.
**Model answer:** DW close to 0 indicates strong positive autocorrelation in residuals. Standard errors are underestimated, t-statistics inflated, CIs too narrow. The OLS estimates are unbiased but inefficient. Remedy: Newey-West HAC standard errors, or use a dynamic model with lagged dependent variables.

### Q43. How do you test two forecast models for accuracy?
**Model answer:** (1) Compare MAE, MAPE, RMSE on out-of-sample holdout data. (2) Diebold-Mariano test compares predictive accuracy formally: H₀: equal accuracy vs H₁: one better. (3) Combine forecasts if each has distinct strengths (simple average often beats individuals).

### Q44. What is a naive forecast and why is it a useful benchmark?
**Model answer:** Naive: Ŷ_t = Y_{t-1} (or seasonally naive: Ŷ_t = Y_{t-m} for seasonal data). It's a baseline; any sophisticated model should beat it. If your complex model doesn't outperform naive, simplify. Mean Absolute Scaled Error (MASE) normalises by naive forecast's error.

### Q45. Plot shows residuals fan-shaped over time. Diagnosis?
**Model answer:** Variance increases with time — heteroscedastic errors (non-stationarity in variance). Take log transformation of Y before modelling. Alternatively, use ARCH/GARCH models that explicitly model time-varying variance. Don't interpret the model's CIs at face value until addressed.

---

## Part F: Application (Q46-50)

### Q46. Quarterly sales data (16 observations) shows trend and seasonality. Outline your modelling approach.
**Model answer:** (1) Plot the series to visualise trend and seasonality. (2) Check for stationarity (ADF). (3) Apply seasonal differencing (1−B⁴) plus regular differencing if needed. (4) Examine ACF/PACF on the differenced series to identify SARIMA(p,d,q)(P,D,Q)_4 orders. (5) Fit model via MLE; compare AIC/BIC across candidates. (6) Diagnose residuals (Ljung-Box, ACF plot). (7) Split data, validate out-of-sample. (8) Forecast with prediction intervals.

### Q47. Stock returns show no autocorrelation but squared returns do. Diagnosis?
**Model answer:** Classic evidence of volatility clustering — returns are uncorrelated but their magnitudes are. This violates the constant variance assumption. Model with ARCH(q): σ²_t = α₀ + Σα_iε²_{t-i}, or GARCH(p,q) which also models lagged σ². Essential in finance.

### Q48. A trend + seasonality regression with time + quarterly dummies has DW = 2.1 and R² = 0.88. Assess.
**Model answer:** DW ≈ 2 suggests no significant autocorrelation — the dummies and time trend have absorbed the systematic patterns. R² = 0.88 indicates strong fit. Check: (i) residuals appear white noise, (ii) forecast on a holdout period, (iii) monitor stability over time. Good model if residual diagnostics pass.

### Q49. Compare using ARIMA vs exponential smoothing vs regression with time dummies.
**Model answer:** (1) ARIMA: flexible for many patterns; requires stationarity; more complex; best for short-term forecasting. (2) Exponential smoothing: simple, data-driven, robust; captures level/trend/seasonality; often competitive. (3) Regression with time dummies: transparent; allows external predictors; assumes fixed pattern. Recommendation: start with exponential smoothing or regression; use ARIMA if structure is more complex.

### Q50. A company's demand forecasting model has MAPE of 5% for most months but 25% in December. Assess and recommend.
**Model answer:** December's high MAPE indicates the model is poorly calibrated for the holiday period — likely due to promotions, holiday effects, or other non-seasonal drivers not captured. Recommendations: (i) add promotional indicator variables, (ii) use longer December history to refine seasonal index, (iii) consider regime-switching or state-dependent models, (iv) for critical periods, supplement with expert judgement. Report overall MAPE and December-specific MAPE separately to avoid misleading aggregate metrics.

---

**Exam tip:** Time-series answers should always: (1) verify stationarity first, (2) use ACF/PACF for model identification, (3) confirm with residual diagnostics (Ljung-Box, residual ACF), (4) validate out-of-sample before deploying, (5) caveat forecasts with prediction intervals — point forecasts alone are meaningless without uncertainty quantification.
