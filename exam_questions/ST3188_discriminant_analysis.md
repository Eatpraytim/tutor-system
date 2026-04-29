# ST3188 — Discriminant Analysis: 50 Exam Questions with Model Answers

---

## Part A: Fundamentals (Q1-10)

### Q1. What is discriminant analysis?
**Model answer:** A multivariate technique that classifies observations into two or more pre-defined groups based on continuous predictor variables. Finds linear combinations of predictors (discriminant functions) that best separate the groups. Used for classification and understanding group differences.

### Q2. Distinguish linear and quadratic discriminant analysis.
**Model answer:** Linear Discriminant Analysis (LDA) assumes equal covariance matrices across groups — produces linear decision boundaries. Quadratic (QDA) relaxes this assumption, allowing each group its own covariance — produces curved boundaries. QDA more flexible but requires more data; LDA simpler and more stable.

### Q3. Compare discriminant analysis with logistic regression.
**Model answer:** Both classify into groups. LDA: assumes predictors are multivariate normal with equal covariances; estimates via class means and pooled covariance. Logistic regression: makes weaker distributional assumptions; estimates via maximum likelihood. Logistic more robust to violations; LDA more efficient when assumptions hold.

### Q4. State the two main applications of discriminant analysis.
**Model answer:** (1) Classification — assign new observations to groups (predicting which group a new customer belongs to). (2) Inference — understanding which variables differentiate the groups (explaining what drives group membership). Both use the same discriminant functions.

### Q5. State the assumptions of LDA.
**Model answer:** (1) Predictor variables are multivariate normal within each group. (2) Equal covariance matrices across groups (homoscedasticity). (3) Independence of observations. (4) No severe multicollinearity among predictors. (5) Adequate sample size (typically 20 cases per group × variables).

### Q6. What is a discriminant function?
**Model answer:** Linear combination of predictors: D = a₁X₁ + a₂X₂ + ... + aₖXₖ. Coefficients chosen to maximise between-group variation relative to within-group variation. With g groups, up to (g−1) functions; first explains most variation.

### Q7. What is Fisher's linear discriminant?
**Model answer:** For two groups: find linear combination maximising (d)² / s² = (X̄₁ − X̄₂)² / pooled variance. Provides single function separating groups. Assumes equal covariances. Generalises to g groups via multiple functions.

### Q8. What is Wilks' Lambda?
**Model answer:** Multivariate test statistic for overall group differences: Λ = |within| / |total| = Π 1/(1+λᵢ), where λᵢ are eigenvalues of the between/within matrix. Range [0, 1]: smaller = more separation. Test: transformed to F or χ²; p < 0.05 indicates significant differences.

### Q9. Explain Mahalonobis distance.
**Model answer:** Multivariate distance accounting for correlations: D² = (x − μ)ᵀ Σ⁻¹ (x − μ). Observations assigned to group with smallest distance. Unlike Euclidean, accounts for scale and correlation of variables. Fundamental to LDA classification.

### Q10. Define prior probability in discriminant analysis.
**Model answer:** Probability of group membership before observing predictors. Options: (1) Equal priors (1/g each). (2) Proportional to sample sizes (reflects population). (3) Based on theory or external data. Priors affect classification — shifts boundaries toward larger groups. Report prior assumption in output.

---

## Part B: Model Building (Q11-20)

### Q11. Describe the stepwise method in discriminant analysis.
**Model answer:** Iteratively add/remove variables based on statistical criteria (e.g., F-to-enter, F-to-remove). Forward: start empty, add best predictor. Backward: start full, remove weakest. Stepwise: combination. Controversial — increases Type I error, unstable variable selection. Better: theory-driven selection or regularisation.

### Q12. What is structure correlation?
**Model answer:** Correlation between original variable and discriminant function. Also called "loading". Indicates contribution to the function. Preferred over standardised coefficients when predictors are correlated (multicollinearity inflates coefficient magnitudes). |r| > 0.30 commonly considered meaningful.

### Q13. Compare standardised coefficients and structure correlations.
**Model answer:** Standardised coefficients: partial contribution holding other predictors constant (like partial regression coefficients). Structure correlations: total contribution (like simple correlation). They agree when predictors are uncorrelated; diverge with multicollinearity. Interpret both but weight structure correlations when correlations are high.

### Q14. How do you evaluate classification accuracy?
**Model answer:** (1) Classification matrix (confusion matrix): actual vs predicted. (2) Overall percent correct. (3) Per-group accuracy. (4) Compare to chance (Cohen's kappa). (5) Use cross-validation or leave-one-out to avoid over-fitting. Report both training and validation accuracy.

### Q15. Describe leave-one-out cross-validation.
**Model answer:** Exclude each case one at a time, estimate LDA from remaining n−1 cases, predict the excluded case. Compute classification accuracy on these hold-out predictions. More realistic than in-sample accuracy (which overfits). Standard in SPSS under "leave-one-out classification".

### Q16. What is the holdout method?
**Model answer:** Split sample into training (70%) and test (30%). Build LDA on training; evaluate on test. Simpler than cross-validation; faster. Weakness: depends on random split — one sample may be lucky or unlucky. Repeat with different splits for robustness.

### Q17. What is the jackknife method?
**Model answer:** Another name for leave-one-out cross-validation. Systematic holding out of one observation at a time for unbiased accuracy estimation. Widely reported in SPSS discriminant output as "unbiased estimates".

### Q18. What is the cutting score?
**Model answer:** Value of discriminant function used to classify cases. For two groups with equal priors and costs: cutting score = (D̄₁ + D̄₂)/2 (midpoint of group centroids). Adjusted for unequal priors: biased toward the larger group. Unequal misclassification costs: biased toward costlier error group.

### Q19. What is a centroid in discriminant analysis?
**Model answer:** Mean discriminant function score for each group (D̄_g). Used for classification: assign to group with nearest centroid (smallest Mahalonobis distance). Visualised in discriminant plots as group centres.

### Q20. Describe canonical discriminant functions.
**Model answer:** Multiple discriminant functions used when there are more than two groups. Number = min(g−1, k). First function explains most between-group variance; subsequent are orthogonal and explain residual. Reported with eigenvalues and canonical correlations.

---

## Part C: Numerical and Interpretation (Q21-30)

### Q21. Interpret Wilks' Lambda = 0.65, p = 0.003.
**Model answer:** The model explains 35% of variance between groups (1 − 0.65 = 0.35). p < 0.05 indicates groups are significantly different on the discriminant functions. Model is statistically meaningful. Report the canonical correlation as effect size: r_canonical = √(1 − Λ) = 0.59 — moderate-to-strong group separation.

### Q22. Canonical correlation = 0.72. Interpret.
**Model answer:** The discriminant function is strongly correlated with group membership. Squared = 0.52, meaning 52% of variance in function is group-related. Values > 0.50 considered strong. Combined with Wilks' Lambda and classification accuracy for full evaluation.

### Q23. Eigenvalue of first discriminant function = 2.5, explains 80% of variance. Interpret.
**Model answer:** Eigenvalue = ratio of between-group SS to within-group SS. Large eigenvalue indicates strong discrimination by this function. 80% of variance concentrated in function 1 means subsequent functions contribute little — often report just function 1 for simplicity.

### Q24. Structure correlations: X1 = 0.75, X2 = 0.40, X3 = −0.25. Interpret.
**Model answer:** X1 is strongly related to the function — major contributor to group separation. X2 moderate. X3 weak and negative — marginally contributes in opposite direction. For interpretation: "The function is primarily driven by X1 (positively) and X2 (positively). X3's role is minor." Use for theoretical understanding.

### Q25. Classification table: correctly classified = 75%, by chance = 50%. Evaluate.
**Model answer:** 75% overall accuracy vs 50% chance — substantial improvement. Press's Q statistic formalises: Q = (N − g·H)² / (N(g−1)), compared to χ²(1). Also report proportional chance (Σpᵢ²): if groups are unequal, proportional chance differs from 50%. Cohen's κ = (observed − expected)/(1 − expected) = (0.75 − 0.50)/0.50 = 0.50 — moderate.

### Q26. Group 1 sensitivity 85%, group 2 sensitivity 50%. Interpret asymmetry.
**Model answer:** Model classifies group 1 well but misclassifies half of group 2. Possible causes: (1) unequal sample sizes — group 1 dominates, priors shift boundary. (2) Group 2 more heterogeneous. (3) Predictors less informative for group 2. Remedies: (a) equal priors to balance, (b) different cutting scores, (c) investigate group 2 sub-structure.

### Q27. A case has posterior probabilities: P(group 1) = 0.70, P(group 2) = 0.30. Classify.
**Model answer:** Assign to group 1 (higher posterior probability, assuming equal costs). Confidence: 0.70 probability — moderate. Could report as "classified as group 1 but with 30% probability of being group 2". For high-stakes decisions (medical, legal), require higher threshold (>0.80).

### Q28. A model has 95% accuracy on training data but 65% on validation. Diagnose.
**Model answer:** Severe overfitting. Training accuracy is unrealistic; validation is the honest estimate. Remedies: (1) Fewer predictors (parsimony). (2) Regularisation. (3) Larger training sample. (4) Cross-validation during model building. (5) Feature selection based on domain knowledge. Never report only training accuracy for decision-making.

### Q29. Interpret a Box's M test result: p < 0.001.
**Model answer:** Box's M tests homogeneity of covariance matrices across groups. p < 0.001 rejects equality — violates LDA's key assumption. Note: Box's M is very sensitive, often rejecting with large n. Practical solutions: (1) Use QDA if variances differ substantially. (2) Inspect covariance matrices; proceed with LDA if differences are small practically. (3) Log/transform skewed predictors.

### Q30. Two predictors: Education and Income. Standardised coefficients: Education = 0.80, Income = 0.30. Interpret.
**Model answer:** Education contributes more to the discriminant function than income after controlling for other predictors. For one standard deviation increase in education, the discriminant score changes 0.80 units (controlling for income). Education is the dominant variable differentiating groups. Verify with structure correlations — if different, multicollinearity present.

---

## Part D: Applications and Examples (Q31-40)

### Q31. A bank uses DA to predict loan default. What are the groups and predictors?
**Model answer:** Groups: defaulters vs non-defaulters (2 groups, binary). Predictors: income, debt ratio, credit score, employment length, loan amount, loan purpose. Apply DA or logistic regression. Outputs: function identifying high-risk vs low-risk applicants; classification rule used in application scoring. Regular model monitoring required.

### Q32. A marketer wants to classify customers as high/medium/low value. How to use DA?
**Model answer:** Groups: three value tiers (defined by revenue, frequency, LTV). Predictors: demographics (age, income), behaviours (purchase frequency, basket size, channel). LDA with 2 discriminant functions (3 groups − 1). Report Wilks' Lambda, canonical correlations, structure correlations for interpretation. Use for segmentation and targeted marketing.

### Q33. Hospital triage: classify patients into critical/urgent/stable. Design.
**Model answer:** Three-group DA. Predictors: vital signs (HR, BP, O₂), lab results (white count, lactate), patient characteristics (age, comorbidities). Requires fast, accurate classification. Validate: sensitivity for critical group should be very high (even at cost of specificity). May combine with decision rules. Ethical: misclassifying critical as stable is costly; weight priors accordingly.

### Q34. Fraud detection in credit card transactions. Discriminant analysis applicability?
**Model answer:** Possible but limited. Challenges: (1) Severe class imbalance (fraud ≈ 0.1%). (2) Adversarial — fraudsters change tactics. (3) Assumptions (normal predictors) often violated. Better options: logistic regression with class-weighted loss, random forests, neural networks, anomaly detection. DA may serve as baseline.

### Q35. A study classifies movies as hits/flops based on production variables. Suitable method?
**Model answer:** DA or logistic regression. Groups: hit (defined by box office threshold) vs flop. Predictors: budget, genre, star power, release date, marketing. Features likely continuous and categorical (mix). Logistic regression handles better. If using DA, ensure categorical variables are dummy-coded and check assumptions.

### Q36. When would you use DA over logistic regression?
**Model answer:** (1) Predictors clearly multivariate normal. (2) Small samples (DA more efficient under assumptions). (3) Need classification boundary in observed data space. (4) Multi-group classification (DA handles naturally; logistic requires multinomial extension). (5) Teaching/intuitive interpretation of group separation. In practice, logistic regression more commonly used due to robustness.

### Q37. A 3-group DA has eigenvalues 3.0 and 0.3 for two functions. How many to report?
**Model answer:** Function 1: dominates (3.0 eigenvalue, ~91% of variance). Function 2: small (0.3, ~9%). Retain only Function 1 for interpretation. Check significance: if only Function 1 is significant, report it alone. A 1D representation captures most discrimination.

### Q38. Interpret a DA output where all structure correlations are small (|r| < 0.30).
**Model answer:** No single predictor strongly associated with discriminant function. Possibilities: (1) Weak overall discrimination (check Wilks' Lambda — if non-significant, model doesn't work well). (2) Multicollinearity distributing variance across many predictors. (3) Many predictors each contribute modestly — need composite interpretation. (4) Pattern effect, not single-variable driver.

### Q39. A classification matrix shows strong diagonal but substantial off-diagonal between adjacent groups (e.g., low vs medium). Interpret.
**Model answer:** Groups are not sharply distinct — natural gradient (low, medium, high). Adjacent groups overlap more than distant ones. Expected when groups are defined by cutoffs on a continuous underlying variable. Consider: (1) Ordinal logistic regression preserves order. (2) Merging adjacent groups if distinctions are not meaningful. (3) Report confusion pattern explicitly.

### Q40. Describe discriminant scores for visualisation.
**Model answer:** Each observation gets a discriminant score(s) from the function(s). Plot Function 1 score vs Function 2 score (if 3+ groups), colour-code by true group. Visually: tight clusters = good separation; overlapping clouds = poor separation. Reveal: classification errors (points in wrong cluster), outliers, sub-structure. Essential exploratory tool.

---

## Part E: True/False and Interpretation (Q41-45)

### Q41. T/F: Discriminant analysis can handle categorical predictors.
**Model answer:** PARTIALLY TRUE. LDA assumes continuous predictors (multivariate normal). Dummy-coded categorical variables violate normality — can be used but assumption is violated. For many categorical predictors, logistic regression or CART is preferred. If combining, check assumptions carefully.

### Q42. T/F: A significant Wilks' Lambda proves good classification.
**Model answer:** FALSE. Significant Λ means groups differ statistically on the predictors — but statistical significance is not classification accuracy. Must separately report classification matrix and validation accuracy. Highly significant Λ can coexist with modest classification accuracy.

### Q43. T/F: Discriminant analysis and logistic regression give identical classifications.
**Model answer:** FALSE generally. LDA uses equal-covariance assumption; logistic uses logit link with no distributional assumption. Under LDA's assumptions, they are asymptotically equivalent. In practice, they produce similar but not identical classifications. Differ more when LDA's assumptions are violated.

### Q44. T/F: You should always use stepwise DA to select variables.
**Model answer:** FALSE. Stepwise has known problems: inflated Type I errors, unstable variable selection, biased coefficients. Better: (1) Theory-driven selection. (2) Enter all theoretically justified variables. (3) Regularisation (LASSO). (4) Cross-validation for variable importance. Report stepwise selection with caveats if used.

### Q45. T/F: With 3 groups, you need 3 discriminant functions.
**Model answer:** FALSE. Maximum number of functions = min(g − 1, k). For g = 3 groups and any k predictors, at most 2 functions. Often Function 1 dominates; interpret only those functions adding meaningful variance (typically eigenvalue > 1 or significant).

---

## Part F: Application (Q46-50)

### Q46. Your DA classifies applicants with 72% accuracy (chance = 50%). Evaluate the practical value.
**Model answer:** Accuracy of 72% is 22 percentage points above chance — substantial. Metrics to report: (1) Sensitivity and specificity per group. (2) Press's Q or Cohen's κ for chance-adjusted agreement. (3) Cost-benefit: what's the business impact of 28% misclassification? If false positives are expensive (granting loan to default), false negatives costly (denying good applicant), compare expected costs vs simpler rules. Validate on new data before deployment.

### Q47. A DA shows that "company size" is the dominant discriminator of customer type. Recommend business action.
**Model answer:** (1) Segment marketing by company size explicitly. (2) Design tailored offerings for small vs mid vs large firms. (3) Sales team specialisation by segment. (4) Allocate resources proportional to segment value. Validate: (a) statistical significance of finding, (b) stability over time, (c) integration with other known segmentation dimensions. Report in dashboard; monitor for changes.

### Q48. Your DA's Box's M is highly significant (p < 0.001) but sample is large. What now?
**Model answer:** Box's M is sensitive — significance with large n may reflect minor departures. Actions: (1) Inspect covariance matrices visually and by magnitude — are differences substantive? (2) Consider QDA if differences are meaningful; compare classification accuracy. (3) Use proportional priors if reasonable. (4) Transform skewed predictors. (5) Report Box's M with caveat; document robustness checks.

### Q49. Compare DA predictions across two banks' customer loan default models. Reliability?
**Model answer:** If both use same predictors and similar populations: expect convergent classifications. Divergence suggests: (1) different populations (region, demographics), (2) different data quality, (3) different time periods (economic conditions), (4) different model specifications. Validate: (a) cross-validate bank A's model on bank B's data, (b) examine discriminant function composition, (c) ensemble the models. Inter-model reliability informs model stability.

### Q50. Design a DA study to classify consumers into lifestyle segments.
**Model answer:** (1) Define segments a priori (from theory, prior research, or cluster analysis): e.g., traditional, innovator, value-conscious, luxury-oriented. (2) Predictors: demographics (age, income, education), psychographics (values, interests), behaviours (media consumption, shopping). (3) Sample: stratified by expected segment proportions, n ≥ 20 per predictor. (4) Build LDA with cross-validation. (5) Report: Wilks' Lambda, canonical correlations, structure correlations to interpret. (6) Classify new respondents. (7) Validate: classifications correlate with known purchase data. (8) Business use: targeted marketing, product development, pricing strategy.

---

**Exam tip:** For discriminant analysis questions, always: (1) state groups and predictors, (2) check and report assumption tests (Box's M, normality), (3) report Wilks' Lambda with significance, (4) interpret via structure correlations (preferred over coefficients with multicollinearity), (5) evaluate with cross-validated classification accuracy (not training), (6) compare to chance and consider costs of misclassification.
