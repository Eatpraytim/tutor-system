# ST3188 — Conjoint Analysis: 50 Exam Questions with Model Answers

---

## Part A: Fundamentals (Q1-10)

### Q1. What is conjoint analysis?
**Model answer:** A technique for measuring consumer preferences by decomposing judgements on realistic product profiles into part-worth utilities for each attribute level. Respondents evaluate product combinations, and the analysis estimates how much each attribute level contributes to overall preference.

### Q2. Why use conjoint rather than direct attribute ratings?
**Model answer:** (1) Direct ratings inflate — respondents say everything matters. (2) Conjoint forces trade-offs, revealing true importance. (3) Captures realistic decision context. (4) Produces actionable willingness-to-pay and preference share estimates. (5) Distinguishes stated from revealed preferences.

### Q3. Describe part-worth utilities.
**Model answer:** Numerical values indicating preference for each attribute level. Higher utility = more preferred. Total utility of a product = sum of part-worths across its attributes. Base of all conjoint interpretation. Example: Attribute "Brand" might have part-worths: Apple = 3.2, Samsung = 2.1, Huawei = 1.5.

### Q4. Define attribute importance.
**Model answer:** Relative contribution of an attribute to overall preference: importance_j = (max part-worth − min part-worth)_j / Σ all such ranges, expressed as percentage. Sums to 100% across attributes. Example: Price 35%, Brand 25%, Battery 20%, Camera 15%, Weight 5%.

### Q5. State the main applications of conjoint.
**Model answer:** (1) Product design — which attributes drive preference. (2) Pricing strategy — willingness to pay, optimal price points. (3) Market segmentation — preference-based clusters. (4) Competitive analysis — simulate market share. (5) New product introduction forecasting. (6) Concept testing.

### Q6. State the main conjoint methods.
**Model answer:** (1) Traditional (full-profile) conjoint — rate or rank complete product descriptions. (2) Choice-based conjoint (CBC) — choose from alternative products in each task. (3) Adaptive conjoint (ACA) — customised to respondent preferences. (4) Menu-based conjoint. Most popular today: CBC.

### Q7. Describe choice-based conjoint (CBC).
**Model answer:** Respondents see multiple product profiles and choose preferred (or "none"). Realistic — mimics real purchase decisions. Analyses using multinomial logit. Advantages: task realism, forced trade-offs, price sensitivity. Weaknesses: more participants needed than traditional conjoint.

### Q8. Distinguish metric and non-metric conjoint.
**Model answer:** Metric: respondents rate profiles on continuous scale (1-100, likelihood to buy). Analyzed via OLS regression. Non-metric: respondents rank profiles. Analyzed via monotonic regression (MONANOVA). Metric preferred today — more informative per task; assumes interval-level judgement.

### Q9. State typical assumptions of conjoint analysis.
**Model answer:** (1) Additive utility model — total utility = sum of part-worths. (2) Linear or appropriate specification for each attribute. (3) Consistent preferences across tasks. (4) Respondent understands and engages with the task. (5) Attribute levels span realistic range. (6) Independence between attributes (no strong interactions unless modelled).

### Q10. What is the orthogonality of attributes?
**Model answer:** Attribute levels uncorrelated across profiles. Achieved by fractional factorial designs. Required to estimate each part-worth independently. Without orthogonality, attributes are confounded; cannot isolate individual effects.

---

## Part B: Designing a Conjoint Study (Q11-20)

### Q11. State the key steps in designing a conjoint study.
**Model answer:** (1) Define attributes and levels. (2) Construct profiles using experimental design (fractional factorial). (3) Select respondents. (4) Administer tasks (rating, ranking, or choice). (5) Estimate part-worths via regression/logit. (6) Compute importance and run simulations. (7) Interpret results and recommend.

### Q12. How to choose attributes and levels?
**Model answer:** (1) Attributes should be distinct, relevant, and controllable by the firm. (2) Levels span realistic range (don't use levels no one would consider). (3) Limit attributes: typically 4-8 (cognitive load). (4) Levels per attribute: 2-5 (usually 3-4). (5) Pre-test with consumers and experts. (6) Consider "price" as special attribute for WTP analysis.

### Q13. Describe the full-factorial design.
**Model answer:** All combinations of attribute levels. Example: 3 attributes with 3 levels = 27 profiles. Often too many for respondents. Solution: use a fractional factorial — subset that preserves orthogonality. Software (SPSS Orthogonal Design) generates efficient subsets.

### Q14. Describe an orthogonal array.
**Model answer:** Fractional factorial design where each level of each attribute appears equally, and each pair of level combinations appears equally. Ensures independence. Reduces full factorial to minimum needed for estimation. Example: L9 design for 3 attributes × 3 levels in 9 runs (instead of 27).

### Q15. How many profiles should respondents evaluate?
**Model answer:** Trade-off between information and fatigue. Guidelines: (1) 5-10 choice sets for CBC. (2) 15-30 profiles for traditional rating conjoint. (3) More for complex products; fewer for simple. (4) Include holdout tasks (not used in estimation) to validate. (5) Watch for straightlining and inconsistency.

### Q16. What are holdout tasks?
**Model answer:** Profiles set aside during model estimation. After estimating part-worths, predict preferences for holdouts. Compare predictions to actual responses. Validates model accuracy and checks for overfitting. Standard practice in conjoint.

### Q17. Describe balanced vs unbalanced designs.
**Model answer:** Balanced: each level appears equally often in the design. Unbalanced: levels appear with different frequencies. Balanced designs are more statistically efficient. Sometimes unbalanced for business reasons (e.g., oversample levels near market norm).

### Q18. Explain main effects vs interactions in conjoint.
**Model answer:** Main effects: effect of each attribute level independent of others. Interactions: effect of one attribute depends on another. Standard conjoint assumes additive (main effects only). Interactions require more profiles. Examples where important: "brand × price" (premium brands command premium price).

### Q19. What is prohibited pairs design?
**Model answer:** Restricting certain attribute combinations from appearing (e.g., BMW at $10,000 is unrealistic). Improves realism but complicates orthogonality. SPSS allows specifying prohibited pairs. Trade-off: realism vs estimation efficiency.

### Q20. How many respondents are needed?
**Model answer:** Minimum 100-200 for aggregate analysis. 300-500 preferred for segmentation. Individual-level analysis (HB): larger sample required to identify heterogeneity. Traditional conjoint: can work with smaller sample due to within-respondent design. Choice-based conjoint needs more respondents.

---

## Part C: Estimation and Analysis (Q21-30)

### Q21. How are part-worths estimated in rating-based conjoint?
**Model answer:** OLS regression. Dependent variable: preference rating. Predictors: dummy variables for each attribute level (minus reference). Coefficient = part-worth. Example: For "Brand" (Apple, Samsung, Huawei with Huawei as reference): β_Apple = part-worth for Apple relative to Huawei.

### Q22. How are part-worths estimated in choice-based conjoint?
**Model answer:** Multinomial logit (MNL). Choice probability: P(j) = e^U_j / Σ e^U_k across alternatives. Utility U_j = Σ β_l · X_{jl}. Estimate β by maximum likelihood. Produces part-worths for each attribute level.

### Q23. What is hierarchical Bayesian (HB) conjoint?
**Model answer:** Estimates individual-level part-worths using Bayesian methods. Assumes individuals drawn from population distribution. Combines aggregate and individual information. Superior to aggregate models for segmentation. Standard in modern conjoint software.

### Q24. How to interpret a part-worth of 0.8 for "Samsung"?
**Model answer:** Relative to the reference brand, Samsung contributes 0.8 utility units to the product's total utility. Compared to other brands' part-worths: if Apple = 1.2, Huawei = 0.3, then Samsung is moderately preferred — less than Apple, more than Huawei.

### Q25. How to calculate attribute importance?
**Model answer:** Range of part-worths within attribute: importance_j = (max − min)_j / Σ all ranges. Express as percentage (sum to 100%). Range captures the difference between best and worst level. Attributes with larger ranges have more influence on preference.

### Q26. Describe a conjoint simulator.
**Model answer:** Tool to predict market share for hypothetical products. Specify product configurations (including competitors). Compute total utilities → probabilities via logit (or first-choice rule). Simulates: launching new product, pricing changes, competitive response, portfolio optimisation. Widely used for strategy.

### Q27. What is a share of preference rule?
**Model answer:** Share_j = e^U_j / Σ e^U_k for all products in the market. Similar to multinomial logit probability. Predicts market share assuming respondents follow logit choice behaviour. Common assumption; may over-predict substitution.

### Q28. Describe a first-choice rule.
**Model answer:** Each respondent chooses only the product with highest utility. Market share = proportion of respondents choosing each product. Simpler than share-of-preference. May under-predict share for niche products. Use when discrete choice is expected.

### Q29. Explain willingness to pay (WTP).
**Model answer:** Amount a consumer is willing to pay for an attribute level change. Computed: WTP = Part-worth of attribute change / (slope of price attribute). Example: if cameras add 0.5 utility, and each £100 price increase reduces utility by 0.1, WTP for camera = £500.

### Q30. What is segmentation via conjoint?
**Model answer:** Cluster respondents based on their part-worth profiles. Segments differ in preferences. Actionable: design products tailored to each segment, or target segments with preferred offerings. Requires individual-level part-worths (HB) for reliable clustering.

---

## Part D: Interpretation and Application (Q31-40)

### Q31. Given importance %: Brand 40%, Price 30%, Battery 20%, Camera 10%. Interpret.
**Model answer:** Brand is the dominant driver of preference — 40% of total importance. Price is secondary (30%). Battery moderately important (20%). Camera contributes least (10%). Strategic: invest in brand building; second priority is competitive pricing. Battery matters but is less decisive. Camera improvements offer limited payoff.

### Q32. Part-worths for price: £100 = 2.0, £150 = 1.0, £200 = 0.0. Interpret.
**Model answer:** Preference decreases linearly with price. Each £50 increase reduces utility by 1.0 unit. Use this slope to calculate WTP for other attributes. Linear response suggests price sensitivity uniform in this range — no evidence of price-quality signalling.

### Q33. Brand part-worths: Apple = 2.5, Samsung = 1.2, OnePlus = −0.3. Interpret.
**Model answer:** Apple strongly preferred; OnePlus disliked (negative compared to reference). Samsung intermediate. Range = 2.8 — strong discriminator among brands. For market simulation: strong Apple preference suggests durability; Samsung has room to grow; OnePlus faces brand challenge.

### Q34. Market simulator predicts 45% share for proposed product vs 35% current. Recommend.
**Model answer:** 10-point increase is substantial — consistent with product improvement or better positioning. Actions: (1) Verify assumptions — were all key competitors included? (2) Sensitivity analysis — how robust is the gain? (3) Consider competitive response: if you gain 10%, competitors may respond by matching features. (4) Pilot launch in test market for validation. (5) Estimate ROI given development costs.

### Q35. You find significant interaction between Brand and Price. Interpret.
**Model answer:** The effect of price on preference differs by brand. Example: luxury brands may have less price sensitivity. Pure additive model misleading. Add interaction terms: part-worth(brand × price) captures brand-specific price sensitivity. Allows strategic pricing: premium brands can charge more without proportional utility loss.

### Q36. Conjoint reveals consumer strongly prefers a feature costing $50 to develop. WTP = $100. Decide.
**Model answer:** Positive business case: consumers value feature at $100 but development cost is only $50. Adding feature increases willingness to pay by $100. Net benefit: $50 per unit (ignoring scale effects and competitive dynamics). Recommendation: include feature — it strengthens value proposition. Caveats: verify sample representativeness, lab vs market behaviour.

### Q37. How to use conjoint for pricing optimisation?
**Model answer:** (1) Include price as attribute with realistic levels (e.g., $9, $12, $15, $18). (2) Estimate part-worths. (3) Use simulator to compute market share at each price. (4) Plot revenue = share × price vs price — find peak. (5) Consider competitor responses. (6) Validate with actual market test. Identifies revenue-optimising price, not just consumer's max WTP.

### Q38. Conjoint for new product launch forecast.
**Model answer:** (1) Include proposed new product with its attributes, plus realistic competitive offerings. (2) Simulate market with full product assortment. (3) Predicted market share for new product. (4) Adjust for distribution constraints, launch timing, marketing effectiveness. (5) Usually combined with other data (awareness, trial, repeat) for total volume forecast. Caveat: conjoint overstates; apply calibration factor based on validation studies.

### Q39. Share-of-preference gives 30% for your product; first-choice gives 50%. Which to report?
**Model answer:** Neither is "correct" — they model different choice processes. Share-of-preference spreads probability across alternatives (smooth substitution). First-choice concentrates on best (discrete choice). In markets with strong differentiators, first-choice closer. In commodity markets, share-of-preference closer. Report both with caveat; compare to actual market data to calibrate.

### Q40. Respondents' stated preferences via conjoint and actual purchase behaviour differ. How to interpret?
**Model answer:** (1) Stated preferences reflect aspirations; behaviour reflects constraints and context. (2) Conjoint may overstate price sensitivity (people say they want cheap). (3) Socially desirable choices biased upward in surveys. (4) Real market has distribution, availability, timing constraints absent from conjoint. (5) Use conjoint for relative ranking, not absolute shares. Calibrate against transaction data when possible.

---

## Part E: Limitations and Advanced (Q41-45)

### Q41. State key limitations of conjoint analysis.
**Model answer:** (1) Hypothetical choices ≠ actual purchases. (2) Limited attributes — real products have many more factors. (3) Additivity assumption may miss interactions. (4) Respondent fatigue with many tasks. (5) Price level chosen is constrained to survey levels. (6) Assumes respondents are expert on trade-offs. (7) Market simulator based on stated, not revealed, preferences.

### Q42. Compare CBC and HB estimation.
**Model answer:** CBC aggregate MNL: single set of part-worths for all respondents. Fast, simple; doesn't capture heterogeneity. HB (Hierarchical Bayes): individual-level part-worths. Captures heterogeneity; enables segmentation. Computationally intensive; requires more respondents. HB is modern standard.

### Q43. What is adaptive conjoint (ACA)?
**Model answer:** Customises tasks based on prior responses: harder trade-offs when preferences are clear, simpler ones where uncertain. More efficient for large attribute sets. Can handle 10+ attributes (vs 4-8 in traditional). Criticism: task complexity, cognitive load, learning effects.

### Q44. What is maxdiff (best-worst scaling)?
**Model answer:** Alternative to conjoint for measuring preferences among items. Respondents pick best and worst from each set. Estimates relative preference scores. Good for ranking large attribute lists. Limitation: doesn't handle attribute combinations; choose between conjoint (for products) and maxdiff (for individual attributes).

### Q45. How to handle non-linear effects of a continuous attribute?
**Model answer:** (1) Treat as categorical with multiple levels — captures any shape. (2) Include quadratic term: utility = β₁·X + β₂·X². (3) Spline: piecewise linear with breakpoints. (4) Specify functional form (log, sigmoidal). Choice depends on theory and data. Piecewise linear (levels) most flexible but loses information.

---

## Part F: Application (Q46-50)

### Q46. Design a conjoint study for a new smartphone.
**Model answer:** Attributes (5): Brand (Apple, Samsung, OnePlus, Huawei), Price (£300, 500, 700, 900), Screen size (6", 6.5", 7"), Battery (4000 mAh, 5000, 6000), Camera (Standard, Premium). Full factorial: 4×4×3×3×2 = 288 profiles. Use fractional factorial (orthogonal array) to reduce to ~16-24 profiles. Use CBC with 10-12 choice sets per respondent. Include "none" option. n = 300 respondents. Estimate with HB. Simulate launch: compare new phone to iPhone 15 at launch price. Validate with holdout task.

### Q47. Your conjoint shows price sensitivity very high; CEO wants to raise price 15%. Recommend.
**Model answer:** (1) Share simulation at proposed price — likely significant share loss. (2) Decompose elasticity: is whole market price sensitive, or specific segments? (3) Premium segment may be less sensitive — targeted pricing strategy. (4) Consider bundling or added features offsetting price increase. (5) Monitor competitor response — if they match, all lose equally. (6) If volume sensitivity outweighs margin gain, decline. Recommendation: proceed only with offsetting benefits; test via market experiment in one region first.

### Q48. A conjoint identifies 3 segments by preferences. How to use?
**Model answer:** (1) Characterise segments: demographics, behaviours, size. (2) Design products tailored to each (or best-fit subset). (3) Targeted marketing messages per segment. (4) Strategic decisions: focus on largest/most profitable segment or diversify. (5) Pricing: can charge more for features valued by premium segment. (6) Validate: do segments actually differ in purchase outcomes? (7) Monitor segment migration over time.

### Q49. Evaluate a conjoint result: R² = 0.45, importance: Brand 50%, Price 10%, other 40%.
**Model answer:** (1) R² = 0.45 is moderate — explains 45% of preference variance. Half the variance unexplained. (2) Brand dominates (50%) — unusual; price typically important. (3) Low price importance (10%) suggests low price sensitivity, possibly due to limited price range in survey (not enough differentiation). (4) Check: were price levels wide enough to reveal sensitivity? (5) Validation: compare predicted vs actual holdouts; if good, take at face value. (6) Business implication: brand differentiation more valuable than aggressive pricing — focus on brand building.

### Q50. Critique: "Conjoint is the only way to measure preferences."
**Model answer:** Overstates. Conjoint is powerful for stated preferences but: (1) Revealed preferences from transaction data are actual behaviour. (2) Discrete choice experiments (DCE) — similar but in behavioural economics context. (3) Eye-tracking reveals what respondents actually notice. (4) Surveys with stated importance and constant-sum allocation are simpler but less realistic. (5) Qualitative research explores why. (6) Best: triangulate conjoint + actual data + qualitative for comprehensive understanding. Conjoint excels at trade-offs but has blind spots.

---

**Exam tip:** For conjoint questions, always: (1) specify attributes and levels clearly, (2) justify design type (CBC preferred for realism), (3) explain estimation method (MNL, HB), (4) report part-worths with interpretation and attribute importance, (5) use simulator for business recommendations, (6) discuss validation (holdout tasks) and calibration to actual behaviour.
