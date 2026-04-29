# ST3188 — Research Design & Types: 50 Exam Questions with Model Answers

---

## Part A: Research Design Fundamentals (Q1-10)

### Q1. Define research design.
**Model answer:** A blueprint for conducting a study: specifies what data to collect, from whom, how, and how to analyse it. Links research question to empirical evidence. Good design ensures results are valid, reliable, and answer the question efficiently.

### Q2. Distinguish exploratory, descriptive, and causal research.
**Model answer:** Exploratory: gains initial insight into a problem, flexible methods, qualitative often (interviews, focus groups). Descriptive: describes market/population characteristics, structured, quantitative (surveys). Causal: establishes cause-effect relationships, requires experimental designs with manipulation.

### Q3. When is exploratory research appropriate?
**Model answer:** (1) When the problem is poorly defined. (2) Before designing detailed research — to identify variables. (3) When existing literature is scarce. (4) For hypothesis generation. (5) To understand consumer motivations or unexpected phenomena. Output: hypotheses, research questions, insights.

### Q4. When is descriptive research appropriate?
**Model answer:** When the goal is to document the market: size, segments, customer profiles, market share, attitudes. Used for (i) forming business decisions based on market profile, (ii) segmentation, (iii) tracking over time. Requires clear a priori hypotheses and structured methods (surveys, panels).

### Q5. Compare cross-sectional vs longitudinal designs.
**Model answer:** Cross-sectional: data collected at one point in time. Faster, cheaper; cannot detect change. Longitudinal: repeated measurements over time — same subjects (panel) or different (repeated cross-section). Reveals change, trends, cause-effect. Expensive; panel attrition is a concern.

### Q6. Define primary vs secondary data.
**Model answer:** Primary: data collected specifically for the current study (surveys, experiments, interviews). Tailored but expensive. Secondary: data already collected for other purposes (government statistics, industry reports, scanner data). Cheap but may not fit the research question exactly.

### Q7. What are the advantages of secondary data?
**Model answer:** (1) Faster — already exists. (2) Cheaper — collection costs already borne. (3) Useful for benchmarking and context. (4) Can cover long time periods. (5) May be the only source (e.g., historical). Evaluate: purpose of original collection, currency, accuracy, granularity.

### Q8. What are the limitations of secondary data?
**Model answer:** (1) May not match research question exactly. (2) Outdated or inappropriate categories. (3) Sampling, measurement, or definitional differences. (4) Quality unknown. (5) Limited control over the variables collected. Evaluate relevance, accuracy, currency, specificity, bias before use.

### Q9. Describe panel data (longitudinal design).
**Model answer:** Same units observed repeatedly over time. Tracks change within units; can estimate causal effects by differencing out time-invariant confounders (fixed effects). Issues: attrition, panel conditioning (responses affected by prior participation), costs. Gold standard for many longitudinal research questions.

### Q10. What is a research question vs hypothesis?
**Model answer:** Research question: what you want to know, phrased as question ("Does X affect Y?"). Hypothesis: testable statement or prediction ("X is positively related to Y"). Research questions drive exploratory work; hypotheses drive confirmatory work. Exploratory studies produce hypotheses; confirmatory studies test them.

---

## Part B: Experimental Design (Q11-20)

### Q11. Define an experiment.
**Model answer:** A research method where the researcher manipulates an independent variable (treatment) and measures its effect on a dependent variable, holding other factors constant via design (random assignment). Establishes cause-effect relationships.

### Q12. What is random assignment and why does it matter?
**Model answer:** Randomly allocating subjects to treatment conditions. Creates statistical equivalence of groups on all characteristics (observable and unobservable) on expectation. Removes selection bias and confounding. Essential for valid causal inference in experiments.

### Q13. Distinguish field and laboratory experiments.
**Model answer:** Laboratory: controlled environment, high internal validity, low external validity (artificial setting). Field: real-world setting, lower internal validity (confounders), higher external validity (generalisable). Choose based on research question — causal mechanism (lab) vs real-world effect (field).

### Q14. Define a quasi-experiment.
**Model answer:** Compares treatment and control groups but without random assignment. Examples: policy changes affecting certain regions, natural disasters. Provides causal inference under weaker conditions than RCT. Common methods: difference-in-differences, regression discontinuity, instrumental variables.

### Q15. State the four threats to internal validity.
**Model answer:** (1) History — external events during the study. (2) Maturation — natural changes in participants over time. (3) Selection — groups differ before treatment. (4) Regression to the mean — extreme scorers shift toward the mean. (5) Testing — pre-test affects post-test. (6) Instrumentation — measurement changes. (7) Mortality — differential attrition.

### Q16. What is a between-subjects vs within-subjects design?
**Model answer:** Between-subjects: different participants in each condition. Larger N needed; no carryover effects. Within-subjects: same participants in all conditions. Smaller N; controls for individual differences; risks carryover (order effects, fatigue). Counterbalance order to mitigate.

### Q17. Describe factorial design.
**Model answer:** Experiment with multiple factors tested simultaneously. 2×2 factorial: two factors, each with two levels. Provides information on main effects AND interactions. More efficient than multiple separate experiments. Example: studying pricing × packaging simultaneously.

### Q18. What is a control group and its purpose?
**Model answer:** A group not receiving treatment, otherwise identical to the treatment group. Serves as counterfactual: "what would have happened without treatment?" Essential for causal inference. Types: pure control (no treatment), placebo (sham treatment), active control (current standard).

### Q19. Describe a randomised controlled trial (RCT).
**Model answer:** Gold standard for causal inference. Steps: (1) Recruit eligible participants. (2) Randomly assign to treatment or control. (3) Administer intervention. (4) Measure outcomes. (5) Compare groups via appropriate statistical test. Strengths: unbiased causal estimates. Challenges: cost, ethics, external validity.

### Q20. State the four threats to external validity.
**Model answer:** (1) Interaction with selection — sample not representative. (2) Setting — artificial experimental context. (3) History — temporal context affects generalisation. (4) Testing — pre-testing influences responsiveness. Generalisability (external validity) often trades off against control (internal validity).

---

## Part C: Observational Designs (Q21-30)

### Q21. Distinguish cohort, case-control, and cross-sectional studies.
**Model answer:** Cohort: follow a group over time, observing who develops the outcome. Prospective. Strong for rare exposures. Case-control: identify cases and controls, look back at exposures. Retrospective. Strong for rare outcomes. Cross-sectional: snapshot at one point. Descriptive; cannot establish temporality.

### Q22. What is selection bias?
**Model answer:** Systematic error when the sample is not representative of the target population. Forms: (1) self-selection (volunteers), (2) survivorship (only survivors observed), (3) sampling frame error (eligible people missing). Biases estimates and threatens external validity.

### Q23. Define confounding.
**Model answer:** A variable correlated with both the exposure and outcome, causing a spurious association. Example: "ice cream causes drowning" — confounded by summer temperature. Handle by: randomisation (experiments), matching, regression adjustment, stratification, instrumental variables.

### Q24. What is reverse causality?
**Model answer:** When the outcome actually causes the predictor, not the other way around. Example: "police presence causes crime" — areas with more crime get more police, not the reverse. Causes spurious relationships in cross-sectional analysis. Remedies: longitudinal data, natural experiments, instrumental variables.

### Q25. Describe propensity score matching.
**Model answer:** Statistical technique for quasi-experiments. Estimate each unit's probability of being treated (propensity) based on covariates. Match treated to control with similar propensity. Creates pseudo-experimental balance. Limitations: matches only on observable covariates; unobserved confounders remain.

### Q26. Define natural experiment.
**Model answer:** A situation where assignment to treatment is effectively random but not controlled by researchers. Examples: lottery-based school admission, policy changes, natural disasters. Provides quasi-experimental evidence when true experiments are infeasible.

### Q27. Describe difference-in-differences (DiD).
**Model answer:** Compares change over time in a treated group vs a control group. Effect = (Treated_after − Treated_before) − (Control_after − Control_before). Controls for time-invariant group differences AND common time trends. Assumes parallel trends in absence of treatment — testable and crucial.

### Q28. What is regression discontinuity design (RDD)?
**Model answer:** Exploits a threshold-based treatment assignment: units above the cutoff receive treatment, those below don't. Compare outcomes just above/below. Strong causal inference under smoothness of potential outcomes at the cutoff. Examples: test-score cutoffs for scholarships, age-based eligibility.

### Q29. Explain instrumental variables (IV).
**Model answer:** An instrument Z must: (i) affect X (relevance), (ii) not directly affect Y (exclusion). Used to identify causal effect of endogenous X on Y. Examples: distance to college as instrument for education. Two-stage least squares (2SLS) is standard estimator. Weak instruments cause bias.

### Q30. Define a natural experiment vs quasi-experiment.
**Model answer:** Natural experiment: "as if random" allocation due to external event (policy, lottery). Stronger identification. Quasi-experiment: non-random groups studied with statistical adjustment (DiD, RDD, IV, propensity scores). Weaker than true random experiments but stronger than purely observational.

---

## Part D: Measurement and Operationalisation (Q31-40)

### Q31. What are the four levels of measurement?
**Model answer:** (1) Nominal — categories without order (gender). (2) Ordinal — ordered categories without equal intervals (ranking). (3) Interval — equal intervals, no true zero (temperature). (4) Ratio — equal intervals and true zero (weight, income). Determines which statistics apply.

### Q32. Define construct validity.
**Model answer:** Extent to which an operationalised measure captures the intended theoretical construct. Subtypes: (1) Convergent — measure correlates with other measures of the same construct. (2) Discriminant — doesn't correlate with different constructs. (3) Content — covers all aspects. Assessed through correlations with related measures.

### Q33. Define internal consistency reliability and how to measure.
**Model answer:** Degree to which items in a multi-item scale measure the same construct. Measured by Cronbach's α: α = (k/(k−1))[1 − Σσ²_i/σ²_total]. Range [0, 1]. Rule of thumb: α > 0.7 acceptable; > 0.8 good; > 0.9 excellent. Low α suggests items measure different things.

### Q34. What is test-retest reliability?
**Model answer:** Correlation between measurements of the same construct at two time points. High reliability = consistent scores. Requires stable constructs and sufficient time gap to avoid memory effects. Low values may reflect true change or unreliable measurement.

### Q35. Define face validity.
**Model answer:** Extent to which a measure appears (on its face) to measure what it intends. Subjective judgement by experts or participants. Weakest form of validity; necessary but not sufficient. Example: a questionnaire labelled "job satisfaction" that asks about job-related items has face validity.

### Q36. Distinguish random error and systematic error.
**Model answer:** Random error: unpredictable, averages to zero over many observations. Reduces reliability. Systematic error (bias): consistent directional error. Reduces validity. Example: scale giving random readings vs scale consistently reading 2 lbs too high.

### Q37. Describe a Likert scale.
**Model answer:** A psychometric scale where respondents rate agreement on an ordinal scale (e.g., 5- or 7-point from strongly disagree to strongly agree). Widely used in attitude measurement. Often treated as interval for analysis, though technically ordinal. Sum or average across multiple items to form a construct score.

### Q38. Distinguish formative and reflective indicators.
**Model answer:** Reflective: indicators "reflect" the construct (caused by it). Items should correlate. E.g., depression symptoms reflect depression. Formative: indicators "form" the construct (cause it). Items need not correlate. E.g., job dissatisfaction = sum of pay, workload, environment. Different analytic approaches apply.

### Q39. What is concurrent validity?
**Model answer:** Extent to which a measure correlates with an established criterion measured at the same time. Compare new scale with existing benchmark; high correlation supports validity. Example: a new depression scale against a validated one. Doesn't address whether the construct is real, only that measures agree.

### Q40. Compare reliability and validity.
**Model answer:** Reliability: consistency of measurement (low random error). Validity: accuracy, measuring what you intend (low systematic error). Can be reliable but not valid (consistent but wrong). Cannot be valid without reliability. Aim for both: multiple items, clear conceptualisation, pilot testing.

---

## Part E: Ethics and Quality (Q41-45)

### Q41. State the key ethical principles in research.
**Model answer:** (1) Informed consent — voluntary participation with full understanding. (2) Confidentiality — protect participant identities. (3) Harm minimisation — risks must not exceed benefits. (4) Right to withdraw. (5) Deception only when justified. (6) Institutional Review Board (IRB) approval for human subject research.

### Q42. What are the requirements for informed consent?
**Model answer:** (1) Purpose of research explained. (2) Procedures described. (3) Risks and benefits disclosed. (4) Confidentiality protections outlined. (5) Voluntary participation emphasised. (6) Right to withdraw stated. (7) Contact for questions. (8) Signature or documented consent.

### Q43. What is data triangulation?
**Model answer:** Using multiple data sources, methods, or investigators to cross-validate findings. Types: (1) Data triangulation — multiple data sources. (2) Investigator triangulation — multiple researchers. (3) Methodological triangulation — quantitative + qualitative. Increases validity and depth.

### Q44. Define mixed methods research.
**Model answer:** Combines qualitative and quantitative methods in a single study. Designs: (1) Convergent parallel — both simultaneously, compared. (2) Sequential explanatory — quant then qual to explain. (3) Sequential exploratory — qual then quant to test. (4) Embedded — one method supports the other.

### Q45. Distinguish probability and non-probability sampling.
**Model answer:** Probability: each unit has known, non-zero probability of selection. Enables statistical inference. Examples: simple random, stratified, cluster. Non-probability: selection based on convenience or judgement. Cannot generalise to population with known error. Examples: convenience, quota, snowball.

---

## Part F: Application (Q46-50)

### Q46. You're designing a study on smartphone use and sleep quality. Recommend a design.
**Model answer:** Cross-sectional quickly establishes association. However, causality is uncertain — do phones reduce sleep, or do poor sleepers use phones more? Better: (1) Longitudinal/panel study — track same individuals over time. (2) Natural experiment — use a policy change banning phones. (3) Randomised experiment: randomise app-use restrictions; measure sleep objectively (actigraphy). Ethically feasible for brief interventions. Report both objective (actigraphy) and subjective (questionnaire) sleep measures.

### Q47. A retailer wants to test price sensitivity. Design an experiment.
**Model answer:** Field experiment: randomly assign stores (or customer cohorts) to different price levels (e.g., £9.99, £12.99, £14.99). Measure: units sold, revenue, customer satisfaction. Control: pre-existing trends. Potential confounds: location demographics, promotion timing. Use randomisation over many stores; stratify by region/size; run for sufficient duration (e.g., 8 weeks) to average out weekly fluctuations. Analyse via ANOVA or regression.

### Q48. You want to study the effect of a new education policy across UK schools. What design?
**Model answer:** RCT impractical politically. Use quasi-experimental design: (1) Difference-in-differences: compare outcomes in schools that adopted vs didn't, before vs after. Check parallel trends assumption. (2) Regression discontinuity if eligibility threshold exists (e.g., school size). (3) Instrumental variable if an exogenous factor predicts adoption. Report multiple approaches for robustness; interpret cautiously given non-random policy adoption.

### Q49. A pharmaceutical firm is testing a new drug vs placebo. Walk through the design.
**Model answer:** RCT: (1) Enrol patients meeting inclusion/exclusion criteria. (2) Random assignment to drug or placebo (double-blind). (3) Measure outcomes at pre-defined intervals. (4) Intent-to-treat analysis (include all randomised, regardless of compliance) for primary endpoint. (5) Per-protocol analysis as sensitivity check. (6) Report safety, efficacy, adverse events. (7) Ethics: informed consent, IRB approval, data monitoring board. (8) Analyse with appropriate tests (t-test, survival analysis).

### Q50. You have an online survey of 1,000 customers but suspect non-response bias. How to assess and address?
**Model answer:** (1) Compare respondent demographics to target population (e.g., census or customer database). Any systematic differences suggest bias. (2) Use wave analysis: compare early responders (who reply quickly) to late/pushed responders. Differences suggest bias in those who don't respond at all. (3) Weight responses to match population characteristics. (4) Sensitivity analysis: what would conclusions be if non-respondents had extreme opinions? (5) Follow-up a random sub-sample of non-respondents to characterise them. (6) Report: response rate, demographic comparison, potential directions of bias in conclusions.

---

**Exam tip:** For research design questions, always: (1) identify the research question (exploratory, descriptive, causal), (2) justify method selection given the question, (3) address threats to validity (internal and external), (4) discuss sampling and ethical considerations, (5) evaluate practical feasibility and limitations, (6) link design to the type of inference possible.
