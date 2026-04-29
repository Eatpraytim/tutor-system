# ST3188 — Factor Analysis: 50 Exam Questions with Model Answers

---

## Part A: Fundamentals (Q1-10)

### Q1. What is factor analysis?
**Model answer:** A multivariate technique that identifies underlying latent variables (factors) explaining correlations among observed variables. Reduces many observed variables to fewer factors. Used for: data reduction, construct identification, scale development, psychometric analysis.

### Q2. Distinguish EFA and CFA.
**Model answer:** Exploratory Factor Analysis (EFA): no prior structure imposed; data-driven factor extraction and interpretation. Used in early research and scale development. Confirmatory Factor Analysis (CFA): tests a pre-specified factor structure against data. Used to validate scales with established structures. CFA produces fit indices.

### Q3. Compare factor analysis with principal component analysis (PCA).
**Model answer:** FA: models common variance attributable to latent factors plus unique variance. Factor model: X = Λf + e. PCA: produces components that are linear combinations of observed variables, capturing total variance (no distinction). PCA is data reduction; FA is structural modelling. Practically: often produce similar results; differ philosophically.

### Q4. When is factor analysis appropriate?
**Model answer:** (1) Many correlated observed variables suspect of measuring fewer constructs. (2) Scale development — checking dimensionality. (3) Data reduction with preserved meaning. (4) Exploratory investigation of latent structure. Not appropriate for: small samples (< 100), categorical predictors, independent variables.

### Q5. State the main assumptions.
**Model answer:** (1) Metric-level (interval or ratio) variables. (2) Adequate correlations among variables (else no factors). (3) Sample size: minimum 100, 5+ observations per variable, preferably 10+. (4) Linearity. (5) Multivariate normality (for ML estimation). (6) No severe outliers.

### Q6. What is communality?
**Model answer:** Proportion of each variable's variance explained by the extracted factors. h²_i = Σ λ²_{ij} across factors j. Range [0, 1]. High communality (> 0.50) indicates the factor solution captures the variable well. Low communality indicates unique variance dominates — variable may not fit the factor structure.

### Q7. What is factor loading?
**Model answer:** Correlation between an observed variable and a factor. Represents contribution of factor to variable. |λ| > 0.30 typically considered meaningful; > 0.50 strong. Squared loading = proportion of variable's variance explained by that factor. Basis for interpreting factor meaning.

### Q8. What is an eigenvalue?
**Model answer:** Total variance explained by a factor across all variables. Eigenvalue = Σ (loadings²) for that factor. Used to determine factor retention: factors with eigenvalue > 1 contribute more than a single variable. Sum of all eigenvalues = total variance (for PCA).

### Q9. What are the three main factor extraction methods?
**Model answer:** (1) Principal Components Analysis (PCA): captures total variance. (2) Principal Axis Factoring (PAF): common factor model; estimates communality. (3) Maximum Likelihood (ML): requires normality; provides goodness-of-fit. PCA most common for data reduction; ML for CFA and fit testing.

### Q10. Distinguish orthogonal and oblique rotation.
**Model answer:** Orthogonal (varimax, quartimax): factors uncorrelated. Simpler interpretation. Promotes simple structure. Oblique (promax, direct oblimin): factors allowed to correlate. More realistic when factors truly correlate. Produces pattern and structure matrices. Oblique generally recommended in behavioural sciences where constructs often correlate.

---

## Part B: Rotation Methods (Q11-20)

### Q11. Why rotate factors?
**Model answer:** Initial extraction maximises variance on Factor 1 — not interpretable. Rotation redistributes variance to achieve "simple structure": each variable loads heavily on one factor, minimally on others. Does not change total variance, just its distribution. Key for interpretability.

### Q12. Describe varimax rotation.
**Model answer:** Orthogonal rotation maximising sum of variances of squared loadings within each factor. Produces a simpler pattern: each variable tends to load heavily on one factor, near zero on others. Most popular orthogonal rotation. Assumes uncorrelated factors.

### Q13. Describe direct oblimin rotation.
**Model answer:** Oblique rotation allowing factor correlations. Controlled by delta parameter: δ = 0 (most oblique), negative (more orthogonal). Produces pattern matrix (loadings) and structure matrix (correlations) differently. Better for correlated latent constructs.

### Q14. Describe promax rotation.
**Model answer:** Oblique rotation: first orthogonal varimax, then oblique relaxation via Procrustes. Faster than direct oblimin for large datasets. Parameter kappa controls obliqueness; κ = 4 typical. Widely used when factor correlations expected.

### Q15. When would you use oblique vs orthogonal rotation?
**Model answer:** Start with oblique: if factor correlations are low (< 0.30), orthogonal solution is similar and simpler. If correlations meaningful (> 0.30), use oblique — forcing orthogonal distorts structure. Behavioural constructs typically correlate (e.g., extraversion and openness); orthogonality is unrealistic.

### Q16. What is simple structure?
**Model answer:** Thurstone's ideal: each variable loads on one factor, with zero or minimal loadings elsewhere. Each factor has a meaningful set of high-loading variables. Makes interpretation straightforward. Real data rarely achieves perfect simple structure; rotation approximates it.

### Q17. What is the pattern matrix in oblique rotation?
**Model answer:** Shows partial regression coefficients of variables on factors, controlling for other factors. Analogous to regression beta. Used for interpreting what each factor represents (unique contribution of each factor to each variable).

### Q18. What is the structure matrix in oblique rotation?
**Model answer:** Shows correlations between variables and factors. Includes shared and unique variance. With uncorrelated factors, pattern = structure. With correlated factors, structure > pattern. Use pattern for interpretation; structure for zero-order correlations.

### Q19. How to interpret factor correlations in oblique rotation?
**Model answer:** Factor correlations matrix shows r between factors. If |r| > 0.30, factors are correlated. Examine whether they represent: (1) Sub-factors of a higher-order factor. (2) Distinct but related constructs. (3) Over-factored solution — one broader factor may suffice. Test alternative factor counts.

### Q20. What is cross-loading?
**Model answer:** Variable loads meaningfully on multiple factors. Problematic because unclear which factor it represents. Decisions: (1) Assign to dominant factor if much higher loading. (2) Remove from scale if ambiguous. (3) Revisit theoretical classification. Reduces simple structure and interpretability.

---

## Part C: Factor Retention and Evaluation (Q21-30)

### Q21. State common criteria for factor retention.
**Model answer:** (1) Kaiser criterion: eigenvalue > 1. Fast but may over-extract. (2) Scree plot: retain factors before "elbow". (3) Parallel analysis: retain factors with eigenvalues exceeding those from random data. Most recommended. (4) Theory-driven: based on prior expectations. (5) Interpretability: retain until factors become uninterpretable.

### Q22. Describe the scree plot.
**Model answer:** Plots eigenvalue on y-axis against factor number on x-axis. Look for an "elbow" — point where curve flattens. Retain factors before the elbow. Subjective but widely used visual tool. Often complemented by other criteria.

### Q23. Describe parallel analysis.
**Model answer:** Generate many random datasets of same size. For each, compute eigenvalues. Retain only factors whose eigenvalues exceed the 95th percentile of random eigenvalues. More accurate than Kaiser. Available in SPSS (via syntax), R (psych package), dedicated software.

### Q24. What are Kaiser-Meyer-Olkin (KMO) and Bartlett's tests?
**Model answer:** (1) KMO: measure of sampling adequacy. Range [0, 1]. > 0.6 acceptable, > 0.8 good. Proportion of variance that is common vs unique. Low KMO = data not suitable for factor analysis. (2) Bartlett's test of sphericity: H₀: correlation matrix is identity (variables uncorrelated). p < 0.05 = correlations present, factor analysis appropriate.

### Q25. What does an anti-image correlation matrix show?
**Model answer:** Diagonal elements: Measure of Sampling Adequacy (MSA) for each variable. < 0.50 = variable doesn't fit factor structure; consider removing. Off-diagonals: partial correlations (controlling for other variables). Small values support factor structure. Examine before deciding on final set of variables.

### Q26. How do you interpret factor loadings?
**Model answer:** (1) Identify loadings ≥ 0.30 (or stricter threshold). (2) Group variables by factor of highest loading. (3) Name factor based on common theme of grouped variables. (4) Report all loadings in table. (5) Note cross-loadings and discuss. (6) Substantive interpretation supports empirical factor structure.

### Q27. What is the reproduced correlation matrix?
**Model answer:** Correlations predicted by the factor model. Compare to observed correlations; residuals = differences. Small residuals (< 0.05) indicate good fit. Large residuals (> 0.10) indicate factors fail to capture relationships — consider more factors or different specification.

### Q28. State criteria for good factor analysis output.
**Model answer:** (1) KMO > 0.6. (2) Bartlett's significant. (3) Cumulative variance explained > 60-70%. (4) Eigenvalues and parallel analysis agree on factor number. (5) Simple structure after rotation (few cross-loadings). (6) Interpretable factors with theoretical meaning. (7) Low residual correlations.

### Q29. What variance percentage should the extracted factors explain?
**Model answer:** Rule of thumb: cumulative ≥ 60% in social sciences. In psychometrics, often 40-60% acceptable (reflecting measurement error). In natural sciences, ≥ 80% expected. Depends on complexity of construct and quality of measurement. Report and justify the threshold used.

### Q30. How many variables per factor are recommended?
**Model answer:** Minimum 3 per factor for stability. 4-6 preferred — provides robustness and reliable factor scores. Single-variable factors are unstable and meaningless. Scale development typically aims for 4-8 items per factor after refinement.

---

## Part D: Numerical and Interpretation (Q31-40)

### Q31. KMO = 0.82. Evaluate.
**Model answer:** Very good (> 0.80 threshold). Data highly suitable for factor analysis — high proportion of common variance. Factor analysis is justified. KMO over 0.9 = excellent, 0.8-0.9 = very good, 0.7-0.8 = good, 0.6-0.7 = mediocre.

### Q32. Bartlett's test: χ² = 350, df = 66, p < 0.001. Evaluate.
**Model answer:** Highly significant. Correlation matrix differs from identity. Variables are correlated, justifying factor analysis. Typically significant in large samples with any correlations present; complementary to KMO, not sufficient alone.

### Q33. Eigenvalues: 4.2, 2.1, 1.3, 0.9, 0.6. How many factors?
**Model answer:** Kaiser criterion: 3 factors (eigenvalues > 1). Scree plot: likely 3 (elbow after third). Parallel analysis with 95th percentile: compare actual to random — depends on sample. Typically retain 3 factors; verify with interpretability.

### Q34. Cumulative variance: 4.2/20 + 2.1/20 + 1.3/20 = 38%. Evaluate.
**Model answer:** Low. 38% cumulative variance after 3 factors is below typical 60% threshold. Consider: (1) Extracting more factors. (2) Different extraction (PAF vs PCA differ). (3) Weaker sample or construct — if subject matter really involves much unique variance, 38% may be realistic. Document and explain.

### Q35. Factor loadings for variable X: F1 = 0.70, F2 = 0.40, F3 = 0.10. Interpret.
**Model answer:** Primary factor is F1 (0.70, strong loading). Secondary loading on F2 (0.40) suggests cross-loading — X relates to both F1 and F2. Assign to F1 for interpretation. Note the cross-loading — may reflect overlap between F1 and F2 or dual nature of X. Reconsider factor structure if cross-loadings are common.

### Q36. Communality of variable = 0.30. Evaluate.
**Model answer:** Low — only 30% of variable's variance explained by factors. Unique variance dominates. Possible actions: (1) Variable doesn't belong to factor structure — remove. (2) Variable measures unique construct — add more factors. (3) Poorly measured variable — refine. Typically aim for communalities > 0.50.

### Q37. Factor correlation r = 0.45 in oblique solution. Interpret.
**Model answer:** Factors moderately correlated. Oblique rotation was appropriate (orthogonal would have distorted). The constructs are related but distinct. Could indicate a higher-order factor — if factors are both positive correlates of a superordinate construct, consider hierarchical factor model.

### Q38. After promax rotation, three factors labelled: F1 = "Service Quality", F2 = "Pricing Fairness", F3 = "Product Variety". Describe interpretation.
**Model answer:** Factor structure corresponds to distinct retail dimensions. F1 captures items about staff, cleanliness, response time. F2 captures price vs competitors, perceived value. F3 captures range, freshness, availability. Each factor is a meaningful, interpretable construct. These become sub-scales in a customer satisfaction framework.

### Q39. Reproduced correlations residuals: 10% exceed 0.05. Evaluate.
**Model answer:** Acceptable. Guidelines: < 50% residuals above 0.05 is adequate; ideally < 25%. 10% is within good range. If > 50% exceeded 0.05, consider more factors or alternative model.

### Q40. Factor analysis of 20 items: 3 factors retained, explaining 62% variance, all loadings > 0.40, no cross-loadings. Evaluate.
**Model answer:** Excellent structure. Simple structure achieved with meaningful variance explained. Each variable loads cleanly on one factor. Further steps: (1) Label factors based on loading variables. (2) Compute internal consistency (Cronbach's α) for each subscale. (3) Validate on independent sample via CFA. (4) Document for publication or scale use.

---

## Part E: True/False and Applications (Q41-45)

### Q41. T/F: Factor analysis requires multivariate normality.
**Model answer:** PARTIALLY TRUE. Standard ML factor analysis assumes multivariate normality for fit statistics and chi-squared tests. PCA does not require normality for extraction. PAF is relatively robust. For severe non-normality, use non-parametric methods or robust estimators. Report distributional properties.

### Q42. T/F: Varimax rotation is always preferred.
**Model answer:** FALSE. Varimax assumes uncorrelated factors, often unrealistic. Oblique rotations (promax, oblimin) preferred when factor correlations are plausible. Default to oblique; switch to orthogonal if factor correlations are truly near zero.

### Q43. T/F: PCA and factor analysis are interchangeable.
**Model answer:** FALSE. Different philosophically. PCA: components are weighted averages of variables (formative). FA: factors are latent causes of variables (reflective). Practically often give similar results, but interpretation differs. Choose based on research goal and theoretical model.

### Q44. T/F: Factor analysis proves the existence of latent constructs.
**Model answer:** FALSE. Factor analysis identifies patterns that are consistent with latent construct interpretations but does not prove they exist. Factors are mathematical combinations; interpretation is theoretical. Strong construct validity requires converging evidence from multiple methods.

### Q45. T/F: A variable loading 0.50 on Factor 1 means 25% of its variance is explained by Factor 1.
**Model answer:** TRUE. Squared loading = variance explained. 0.50² = 0.25. So 25% of variable's variance comes from Factor 1. For a single variable in a multi-factor model, total explained variance = sum of squared loadings = communality.

---

## Part F: Application (Q46-50)

### Q46. Develop an employee engagement scale with 20 items and 500 employees. Walk through FA.
**Model answer:** (1) Check KMO (> 0.6) and Bartlett's (p < 0.05). (2) Extract with PAF or ML; use Kaiser + parallel analysis for number of factors. Target 3-5 factors. (3) Rotate (promax for correlated constructs). (4) Interpret loadings: each factor should have 3+ items with loadings > 0.40. (5) Remove cross-loaded items (< 0.20 on dominant). (6) Repeat until stable structure. (7) Label factors (e.g., cognitive, emotional, behavioural engagement). (8) Compute subscale α > 0.70. (9) Validate via CFA on new sample. (10) Check convergent/discriminant validity with other scales.

### Q47. A market researcher has 15 product attribute ratings. How to use FA for market segmentation?
**Model answer:** (1) FA reduces 15 attributes to 3-4 underlying dimensions (e.g., quality, value, brand image). (2) Compute factor scores for each customer. (3) Use factor scores in cluster analysis to identify segments (e.g., "quality-focused", "value-focused"). (4) Profile each segment by demographics, behaviour. (5) Develop targeted offerings. Advantages: reduces dimensionality and measurement error; produces interpretable segments.

### Q48. Factor analysis of personality items yields 5 factors consistent with Big Five. Evaluate validity.
**Model answer:** (1) Strong convergent validity if factors match expected constructs (Extraversion, Agreeableness, Conscientiousness, Neuroticism, Openness). (2) Loadings meaningful (> 0.40 on primary factor). (3) Factor correlations reasonable (< 0.50). (4) Cross-validate on independent sample — must replicate. (5) Compare to established Big Five inventories via convergent/discriminant validity study. (6) Publish validation report. Consistent structure across samples establishes construct validity.

### Q49. An FA fails: KMO = 0.45, eigenvalue plot flat. Diagnose.
**Model answer:** KMO below threshold (0.6) indicates data unsuitable. Flat eigenvalue plot (no clear elbow) suggests weak correlation structure. Possible issues: (1) Variables uncorrelated — no common factors to extract. (2) Single-item constructs with no latent structure. (3) Very heterogeneous sample — sub-groups may have different structures. Actions: (1) Examine correlation matrix — are correlations meaningful? (2) Check individual variables' MSAs — remove weak ones. (3) Review theoretical basis — perhaps variables genuinely don't share factors. (4) Consider alternative analyses (cluster, network).

### Q50. Your FA of 12 customer satisfaction items yields 2 factors explaining 55% variance. Factor 1 = 8 items, Factor 2 = 4 items. Interpret and use.
**Model answer:** (1) Two-factor solution reduces 12 items to 2 subscales. (2) Factor 1 (8 items): main satisfaction dimension — e.g., overall quality experience. (3) Factor 2 (4 items): secondary dimension — possibly ease/convenience or pricing. (4) 55% variance is moderate — consider whether additional factors would improve fit. (5) Internal consistency for each subscale (aim α > 0.70). (6) Use factor scores (or sum scores) as subscale measures. (7) Segment analysis or predictive modelling with 2 subscales rather than 12 individual items — reduces multicollinearity and complexity. (8) Report two-factor structure with loadings table in dashboards or reports.

---

**Exam tip:** For factor analysis questions, always: (1) report sample adequacy (KMO, Bartlett), (2) justify number of factors with multiple criteria (Kaiser + scree + parallel analysis), (3) specify extraction method (PAF/ML/PCA) and rotation (oblique preferred), (4) present factor loadings table with interpretations, (5) discuss simple structure and cross-loadings, (6) report cumulative variance and communalities, (7) validate via CFA on independent data for confirmatory claims.
