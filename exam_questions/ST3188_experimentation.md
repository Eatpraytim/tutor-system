# ST3188 — Experimentation & Causal Design: 50 Exam Questions with Model Answers

---

## Part A: Experimental Fundamentals (Q1-10)

### Q1. What are the three key conditions for establishing causality?
**Model answer:** (1) Association — X and Y are statistically related. (2) Temporal precedence — X precedes Y in time. (3) Non-spuriousness — the relationship is not explained by a third variable (confounder). Experiments achieve all three by design; observational studies struggle with (3).

### Q2. Define independent and dependent variables.
**Model answer:** Independent variable (IV): the manipulated factor — the hypothesised cause. Dependent variable (DV): the measured outcome — the hypothesised effect. Extraneous variables: other factors that may affect the DV; control through randomisation or design.

### Q3. What is manipulation in experimental research?
**Model answer:** Actively varying the independent variable across conditions rather than just measuring it. Distinguishes experiments from correlational studies. Manipulation ensures temporal precedence and isolates the effect of the IV. Example: randomly assigning advertising budgets across regions.

### Q4. Distinguish true experiments, quasi-experiments, and pre-experiments.
**Model answer:** True experiment: random assignment + control group + manipulation. Quasi-experiment: manipulation without random assignment (natural groupings). Pre-experiment: no random assignment AND no true control (one-shot case studies, one-group pre-post). Descending order of internal validity.

### Q5. State Campbell and Stanley's threats to internal validity.
**Model answer:** (1) History — external events. (2) Maturation — natural change over time. (3) Testing — pre-test affects post-test. (4) Instrumentation — measurement changes. (5) Statistical regression — extreme scorers regress to mean. (6) Selection — non-equivalent groups. (7) Mortality — differential attrition. (8) Selection-maturation interaction — groups mature differently.

### Q6. State Campbell and Stanley's threats to external validity.
**Model answer:** (1) Interaction of testing and treatment — pre-test sensitises. (2) Interaction of selection and treatment — sample not representative. (3) Reactive effects of experimental arrangements — artificial setting. (4) Multiple-treatment interference — prior treatments confound. Trade-off: increasing internal validity (control) often reduces external validity (realism).

### Q7. What is Hawthorne effect?
**Model answer:** Participants alter behaviour because they know they're being observed, regardless of actual treatment. Named after Hawthorne Works studies in 1920s. Threatens internal validity — observed effect may be attention rather than intervention. Mitigate with blinding, placebo controls, naturalistic observation.

### Q8. Define placebo effect and how it's controlled.
**Model answer:** Improvement in outcomes from expectation of treatment rather than the treatment itself. Control: (1) Placebo condition — inert treatment. (2) Double-blinding — neither participant nor researcher knows allocation. (3) Active control — compare to standard treatment. Essential in clinical trials.

### Q9. Define demand characteristics.
**Model answer:** Subtle cues in an experiment that suggest to participants how they should behave. Participants may comply with or resist perceived expectations. Mitigate: cover stories, unobtrusive observation, measures of participant awareness, debriefing. Strong demand characteristics invalidate experimental conclusions.

### Q10. What is experimenter bias and how to reduce it?
**Model answer:** Researcher's expectations subtly influence procedure, measurement, or analysis. Reduction: (1) Double-blinding. (2) Standardised protocols. (3) Automated data collection. (4) Pre-registered hypotheses and analyses. (5) Data collection by naive assistants. (6) Analyst blinding — analyse before knowing condition labels.

---

## Part B: Experimental Designs (Q11-20)

### Q11. State the classical true experimental design notation.
**Model answer:** R O₁ X O₂ vs R O₃ O₄. R = random assignment; O = observation/measurement; X = treatment. Subscripts denote sequence. Pre-test/post-test control group design. Compare O₂ − O₁ (treatment change) to O₄ − O₃ (control change). Classic design for causal inference.

### Q12. Describe the post-test only control group design.
**Model answer:** R X O₁ vs R O₂. Eliminates pre-test sensitisation. Valid if random assignment creates equivalent groups. Simpler than pre-post design. Disadvantage: cannot verify randomisation's equivalence pre-treatment.

### Q13. Describe the Solomon Four-Group Design.
**Model answer:** Four groups: (1) R O₁ X O₂, (2) R O₃ O₄, (3) R X O₅, (4) R O₆. Combines pre-post with post-only. Allows testing for pre-test effects separately from treatment. Most rigorous but expensive — requires 4x sample size.

### Q14. Describe a 2×2 factorial design.
**Model answer:** Two factors, each at two levels → four conditions. Tests: (1) Main effect of A. (2) Main effect of B. (3) Interaction A×B. Example: (Price: low/high) × (Advertising: yes/no) = 4 cells. Efficient — tests two factors with same n as one-factor design.

### Q15. Describe a Latin Square design.
**Model answer:** Balances order effects in within-subjects designs. For k conditions, create k×k matrix where each condition appears once in each row and column. Example: 3 conditions A, B, C with 3 participant groups: Row 1: ABC, Row 2: BCA, Row 3: CAB. Controls for order and carryover.

### Q16. What is a crossover design?
**Model answer:** Each participant receives multiple treatments in counterbalanced order. E.g., Group 1: A then B; Group 2: B then A. Advantages: fewer participants, within-subject precision. Risks: carryover (effect of first treatment lingers), period effects (learning, fatigue). Washout periods between treatments.

### Q17. Distinguish within-subjects vs between-subjects designs.
**Model answer:** Within-subjects: same participants in all conditions. Pros: smaller N, controls individual differences. Cons: order effects, fatigue. Between-subjects: different participants. Pros: no carryover. Cons: larger N, individual differences add noise. Mixed designs combine both.

### Q18. Describe a repeated measures design.
**Model answer:** Multiple observations on the same subjects over time or conditions. Within-subjects. Examples: longitudinal studies, A/B testing with sequential conditions. Analysed with repeated-measures ANOVA or mixed models. Handles individual variability through within-subject comparisons.

### Q19. Describe blocking in experimental design.
**Model answer:** Group similar units into blocks before randomisation. Randomise within blocks. Reduces variability by controlling known sources. Example: age-block randomisation in clinical trial. Blocking improves precision when blocks differ meaningfully on the outcome.

### Q20. Describe stratified random assignment.
**Model answer:** Subjects grouped by a categorical variable (age, gender), then randomly assigned to conditions within each stratum. Ensures balance on that variable across conditions. More reliable than simple random assignment for key baseline variables. Improves internal validity.

---

## Part C: Field Experiments and A/B Testing (Q21-30)

### Q21. What is a field experiment?
**Model answer:** Experiment in a natural setting (store, workplace, community) rather than a lab. Manipulates treatment and measures outcomes in context. Strengths: external validity, realism. Weaknesses: reduced control, field contamination, ethical complexity.

### Q22. Describe A/B testing.
**Model answer:** Online field experiment comparing two versions (A = control, B = treatment). Random assignment of users to version, measure outcome (click, conversion). Ubiquitous in digital marketing. Strengths: fast, cheap, high N. Weaknesses: short-horizon metrics may not capture long-term effects.

### Q23. When is A/B testing inappropriate?
**Model answer:** (1) Sensitive or safety-critical contexts. (2) Small samples (n < 100/group). (3) When interactions between users distort outcomes (network effects). (4) Long-term outcomes requiring long observation. (5) When treatment effects are heterogeneous and aggregated estimates mislead. (6) Ethical concerns (e.g., harmful variants).

### Q24. What is the SUTVA assumption?
**Model answer:** Stable Unit Treatment Value Assumption: each unit's outcome depends only on its own treatment assignment, not others'. Violated by: interference (A's treatment affects B's outcome), hidden variations of treatment. Especially problematic in social network experiments. Cluster randomisation helps mitigate.

### Q25. Describe Multi-Armed Bandit (MAB) testing.
**Model answer:** Dynamic allocation: as evidence accumulates, shift more traffic to the better-performing variant. Contrasts with fixed-split A/B. Strengths: minimises regret (lost conversions during testing). Weaknesses: biased estimation if not corrected; more complex analysis; assumes stationarity.

### Q26. Describe cluster randomised trials.
**Model answer:** Groups (schools, hospitals, neighbourhoods) randomly assigned to treatment, rather than individuals. Used when individual randomisation is impractical or contaminating. Analysis accounts for intraclass correlation (ICC). Sample size larger than individual randomisation.

### Q27. Describe difference-in-differences (DiD).
**Model answer:** Effect = (Treated_after − Treated_before) − (Control_after − Control_before). Controls for time-invariant differences between groups AND common time trends. Assumes parallel trends without treatment. Used in natural and quasi-experiments (policy analysis).

### Q28. Describe regression discontinuity design (RDD).
**Model answer:** Treatment assigned based on a cutoff in a running variable (e.g., test score ≥ 60 = scholarship). Compare outcomes just above vs just below. Strong causal inference under smoothness of potential outcomes at cutoff. Examples: age-based eligibility, minimum wage thresholds.

### Q29. Describe instrumental variables (IV).
**Model answer:** A variable Z that affects treatment X but is otherwise uncorrelated with outcome Y (exclusion restriction). Use Z to identify causal effect of X on Y. Example: distance to college as IV for education. 2SLS is standard estimator. Critical: valid instrument, strong first stage (F > 10).

### Q30. Describe propensity score matching.
**Model answer:** Estimate probability of receiving treatment (propensity) given observed covariates. Match treated units to control units with similar propensity. Creates balance on observables. Used in observational studies. Limitations: matches only on observed variables; unmeasured confounders remain.

---

## Part D: Statistical Analysis of Experiments (Q31-40)

### Q31. How to analyse a randomised between-subjects experiment with one IV (3 levels)?
**Model answer:** One-way ANOVA. H₀: μ₁ = μ₂ = μ₃. F-test for overall differences. If significant, post-hoc tests (Tukey) for pairwise comparisons. Check homogeneity of variance (Levene's). Effect size: η². Report: F(df1, df2) = value, p, η².

### Q32. How to analyse a 2×2 between-subjects factorial experiment?
**Model answer:** Two-way ANOVA. Three tests: main effect of A, main effect of B, A×B interaction. If interaction significant, interpret simple main effects (effect of A at each level of B). Partial η² for each effect. Plot interaction. Report all three F-tests and effect sizes.

### Q33. How to analyse a repeated-measures experiment?
**Model answer:** Repeated-measures ANOVA. Sphericity assumption: variances of differences between all pairs of conditions are equal. Test with Mauchly's test; if violated, apply Greenhouse-Geisser or Huynh-Feldt correction. Alternatively, use mixed-effects models (linear mixed models) that don't require sphericity.

### Q34. What is ANCOVA in experimental contexts?
**Model answer:** Analysis of Covariance. Adds continuous covariate (e.g., pre-test score, age) to ANOVA model. Adjusts group means for covariate and reduces error variance. Increases statistical power. Key assumption: homogeneity of regression slopes (covariate's effect same across groups).

### Q35. How to handle dropouts in longitudinal experiments?
**Model answer:** (1) Intent-to-treat (ITT) analysis: include all randomised participants in original groups regardless of dropout. Preserves randomisation, conservative. (2) Per-protocol analysis: analyse only completers. Biased if dropouts differ systematically. (3) Sensitivity analyses — multiple imputation, pattern-mixture models. Report both ITT and per-protocol.

### Q36. What is intent-to-treat (ITT) analysis?
**Model answer:** Analyse participants according to the group they were randomised to, regardless of whether they received the treatment. Preserves randomisation and provides unbiased estimate of the effect of assignment to treatment. Standard in clinical trials. Contrasts with per-protocol (only compliers).

### Q37. Describe the risk of multiple comparisons and how to control it.
**Model answer:** Conducting many tests inflates family-wise error rate. Solutions: (1) Bonferroni: α/m. (2) Holm-Bonferroni: sequential. (3) Benjamini-Hochberg: controls false discovery rate (FDR). Pre-register primary hypotheses; label secondary/exploratory tests. Report all tests conducted, not just significant ones.

### Q38. What is effect size reporting and why does it matter?
**Model answer:** Standardised measure of magnitude: Cohen's d (mean difference/SD), η² (ANOVA), r or R². Context for interpreting p-values. Small, medium, large conventions (Cohen): d = 0.2, 0.5, 0.8. Essential because large n can make trivial effects "significant". Effect size communicates practical importance.

### Q39. What is a power analysis?
**Model answer:** Computes required n given desired power (1−β), effect size, α. Equivalent: computes achievable power given fixed n. Conducted before data collection to avoid underpowered studies. Tools: G*Power, R pwr package. Essential for ethical research and grant applications.

### Q40. Explain the intent of pre-registration.
**Model answer:** Register hypotheses, methods, and analysis plan before data collection. Distinguishes confirmatory from exploratory analyses. Reduces publication bias and p-hacking. Platforms: OSF, AsPredicted, ClinicalTrials.gov. Increases credibility and reproducibility. Post-hoc modifications must be transparent.

---

## Part E: Validity and Ethics (Q41-45)

### Q41. Define construct validity.
**Model answer:** Extent to which manipulations and measures capture the intended theoretical constructs. Manipulation construct: does the manipulation really change the theoretical variable? Measurement construct: does the DV measure what's intended? Assessed through convergent/discriminant validity, pilot testing, manipulation checks.

### Q42. What is a manipulation check?
**Model answer:** Verification that the experimental manipulation had the intended effect. Example: in a stress study, measure subjective stress ratings to confirm the stress manipulation worked. If failed (no difference), interpretation is ambiguous — effect may be due to other factors. Essential for construct validity.

### Q43. Describe ethical concerns in behavioural experiments.
**Model answer:** (1) Informed consent — voluntary participation, full information. (2) Deception only if necessary and debriefed. (3) Risk minimisation. (4) Participant welfare monitoring. (5) Right to withdraw. (6) Confidentiality. (7) Debriefing — explain true purpose, correct misunderstandings. (8) IRB approval required.

### Q44. When is deception in research ethical?
**Model answer:** Deception is acceptable when: (1) Full disclosure would invalidate research. (2) Risk to participants is minimal. (3) Participants cannot be harmed by the deception. (4) Thorough debriefing explains rationale. (5) No reasonable alternative exists. IRB approval required. Common in social psychology but minimise use.

### Q45. What is debriefing?
**Model answer:** Post-experiment conversation where researchers explain the true purpose, correct any deception, address participant concerns. Required by ethics. Especially important if deception was used. Includes: research purpose, how data will be used, opportunity to withdraw data, offer of results summary.

---

## Part F: Application (Q46-50)

### Q46. Design an experiment to test whether a new restaurant menu layout increases spending.
**Model answer:** (1) Between-subjects RCT: randomly assign restaurant branches to new or old menu (Cluster randomised). (2) Sample size: power analysis based on expected lift (say 5%). (3) Outcomes: average check size, dessert/drink attach rate, customer satisfaction. (4) Duration: 4-8 weeks to average seasonal variation. (5) Controls: matched on size, location type. (6) Analysis: two-group t-test or regression with control variables. (7) Limitations: cannot separate novelty from sustained effect; repeat after 3 months.

### Q47. You want to test whether framing of charitable appeals (gain vs loss) affects donation. Design.
**Model answer:** 2 conditions × online A/B test. (1) Random assignment of visitors to appeal. (2) Framing: Gain condition — "Donate to save X lives." Loss condition — "X lives lost without your donation." (3) Outcome: donation rate, amount, click-through. (4) Sample: thousands per condition. (5) Duration: 2-4 weeks, balanced across days. (6) Analysis: logistic regression for conversion, linear regression for amount. (7) Measure: average treatment effect, variation by donor segment. (8) Check: pre-treatment demographics balance.

### Q48. Design a within-subjects experiment on UI design preference.
**Model answer:** Counterbalanced presentation of 3 designs. (1) Each participant sees all 3 in random order. (2) Latin Square (3x3) to balance order effects across participants. (3) After each design, rate preferences, task completion time, error rate. (4) Analysis: repeated-measures ANOVA; if sphericity violated, use Greenhouse-Geisser correction. (5) Washout/attention check between designs. (6) Sample size: smaller than between-subjects due to within-subject comparisons. (7) Control for design-specific learning effects.

### Q49. Your A/B test shows 5% lift, but 90% power required 10,000 users and you only ran 1,000. What do you do?
**Model answer:** Underpowered — high Type II error risk. Options: (1) Continue test to reach required n. (2) Decide on effect size meaningful to business (maybe 5% is enough to act on). (3) Run Bayesian analysis — report posterior probability of positive effect. (4) Use sequential testing methods (Mills-Bonferroni adjustments) if stopping early is planned. (5) Replicate in next A/B cycle. Avoid: declaring victory on the observed 5% as statistically significant when it may not be.

### Q50. A new drug trial shows statistically significant reduction in blood pressure (p = 0.04, n = 400). How to critique and interpret?
**Model answer:** Critique: (1) Effect size — how much reduction? Cohen's d or absolute reduction in mmHg? (2) Clinical significance — is the reduction meaningful to patient outcomes or simply statistically detectable? (3) CI width indicates precision. (4) Pre-specified primary endpoint or exploratory (multiple testing risk)? (5) ITT analysis done? (6) Adverse events? (7) Duration of follow-up — is effect sustained? (8) Subgroup heterogeneity — does it work for all demographics? (9) Dosage — was this the right dose? Full critique requires reading the trial report; p = 0.04 alone is insufficient basis for recommendation.

---

**Exam tip:** For experimental design questions, always: (1) state IV and DV clearly, (2) justify between-vs within-subjects and specific design type, (3) address threats to internal and external validity specifically, (4) describe random assignment procedure, (5) include sample size justification (power analysis), (6) specify analysis plan BEFORE data collection, (7) outline ethical considerations.
