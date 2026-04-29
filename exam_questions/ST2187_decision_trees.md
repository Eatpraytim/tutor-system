# ST2187 — Decision Tree Analysis & Decision Under Uncertainty: 50 Exam Questions with Model Answers

---

## Part A: Decision Tree Fundamentals (Q1-10)

### Q1. What is a decision tree?
**Model answer:** A graphical model representing sequential decisions and their possible consequences under uncertainty. Nodes: squares = decision nodes (controlled choices), circles = chance nodes (probabilistic outcomes), triangles = terminal nodes (payoffs). Branches connect alternatives and outcomes.

### Q2. Distinguish the three types of nodes in a decision tree.
**Model answer:** Decision node (square): the decision-maker chooses among alternatives. Chance node (circle): nature randomly selects outcomes based on probabilities. Terminal node (triangle or endpoint): the end of a scenario with an associated payoff.

### Q3. Explain the process of solving a decision tree.
**Model answer:** (1) Draw the tree from left to right showing sequence of decisions and chance events. (2) Assign probabilities to chance branches and payoffs to terminal nodes. (3) Solve by backward induction (roll back): at chance nodes compute expected value; at decision nodes choose the maximum expected value. (4) The root value is the optimal expected payoff.

### Q4. Define Expected Monetary Value (EMV).
**Model answer:** EMV(alternative) = Σ P(outcome_i) × Payoff_i across all possible outcomes. The average payoff if the decision were repeated many times. The decision with highest EMV is optimal under the EMV criterion.

### Q5. Why use decision trees over simple payoff tables?
**Model answer:** Decision trees handle sequential decisions where later choices depend on earlier outcomes (multi-stage problems), whereas payoff tables handle single-stage decisions with exhaustive alternatives and states. Trees also incorporate Bayesian updating from test information.

### Q6. Explain the Expected Value of Perfect Information (EVPI).
**Model answer:** EVPI = (Expected payoff with perfect information) − (Expected payoff under current information). It is the maximum amount a decision-maker should pay for perfect foresight. Computed by finding the best decision for each state, weighting by state probabilities, then subtracting the best EMV.

### Q7. Explain the Expected Value of Sample Information (EVSI).
**Model answer:** EVSI = (Expected payoff using sample information) − (Expected payoff without sample information). The amount a decision-maker should pay for an imperfect study or test. Always EVSI ≤ EVPI. Requires Bayesian revision of probabilities using the sample's likelihood.

### Q8. Define efficiency of sample information.
**Model answer:** Efficiency = EVSI/EVPI × 100%. Measures how much of the maximum possible value perfect information can provide is actually captured by the imperfect sample. Higher = more informative. Efficiency = 100% means the sample is as good as perfect information.

### Q9. What are the limitations of using EMV?
**Model answer:** (1) Ignores risk preferences — a risk-averse decision-maker might choose lower EMV with smaller variance. (2) Assumes repeated decisions; for one-off decisions, expected value can be misleading. (3) Sensitive to probability estimates. (4) Does not account for non-monetary considerations (strategic fit, ethics).

### Q10. What is a decision rule?
**Model answer:** A rule for making a decision based on a criterion: (i) maximin (maximise the worst-case payoff, pessimist), (ii) maximax (maximise the best-case, optimist), (iii) Laplace (assume equal probabilities, average), (iv) EMV (use known probabilities, most common), (v) minimax regret (minimise maximum regret).

---

## Part B: Probability and Bayesian Updating (Q11-20)

### Q11. State Bayes' theorem in decision analysis context.
**Model answer:** P(State | Test result) = P(Test result | State) · P(State) / P(Test result). Used to update prior probabilities P(State) to posterior probabilities given evidence. P(Test result) = Σ P(Test | State) · P(State) by law of total probability.

### Q12. Calculate P(disease | positive test) if P(disease) = 0.01, P(+|disease) = 0.95, P(+|no disease) = 0.05.
**Model answer:** P(+) = 0.95(0.01) + 0.05(0.99) = 0.0095 + 0.0495 = 0.0590. P(disease | +) = 0.0095/0.0590 = 0.161 or 16.1%. Despite test 95% accurate, only 16% of positives actually have disease due to low base rate.

### Q13. What is a prior probability?
**Model answer:** The decision-maker's belief about the probability of a state before observing new information. Based on historical data, expert judgement, or subjective estimates. Bayesian analysis updates priors to posteriors as evidence accumulates.

### Q14. Distinguish subjective, objective, and empirical probabilities.
**Model answer:** Subjective: personal degree of belief. Objective (frequentist): long-run relative frequency from repeated trials. Empirical: estimated from observed sample data. Decision trees often use mixed sources — objective for well-known physical processes, subjective for novel or rare events.

### Q15. Explain risk, uncertainty, and ignorance in decision theory.
**Model answer:** Risk: probabilities of states are known (use EMV). Uncertainty: states known but probabilities unknown (use maximin, Laplace). Ignorance: even states unknown. Clear distinction helps choose appropriate decision rule.

### Q16. Why do we use backward induction to solve a tree?
**Model answer:** Starting from the rightmost payoffs, we compute expected values at chance nodes and optimal choices at decision nodes working backward. This correctly handles sequential decisions by incorporating future optimal play. Forward evaluation would ignore how future decisions depend on earlier outcomes.

### Q17. How do you handle multi-stage decision problems?
**Model answer:** Draw the tree explicitly showing all sequential decisions and outcomes. Solve by backward induction: at the final decision, choose the best option given the state; at the final chance, compute EV; continue rolling back to the initial decision. The method is an application of Bellman's principle of optimality.

### Q18. State the posterior probability formula used when a test returns a result.
**Model answer:** P(State_i | Result) = P(Result | State_i) × P(State_i) / Σⱼ P(Result | State_j) × P(State_j). Numerator: joint probability of state and result. Denominator: marginal probability of the result across all states.

### Q19. Explain sensitivity analysis in decision trees.
**Model answer:** Vary input parameters (probabilities, payoffs) to see how the optimal decision changes. Identify critical thresholds — e.g., if P(state) drops below 0.3, the optimal decision switches. Sensitivity analysis reveals which inputs drive the decision and where to focus further data collection.

### Q20. What is a risk profile?
**Model answer:** The probability distribution of payoffs for each alternative, showing the full range of outcomes rather than just EMV. Used to compare alternatives by variance, worst case, best case — complementing EMV especially when decision-makers are risk-averse.

---

## Part C: Decision Criteria (Q21-30)

### Q21. State maximin and when it's appropriate.
**Model answer:** Maximin: choose the alternative whose worst-case payoff is largest. Appropriate for extreme risk aversion (pessimistic decision-maker) or when consequences of failure are catastrophic. Ignores probabilities.

### Q22. State maximax and when it's appropriate.
**Model answer:** Maximax: choose the alternative with the highest possible payoff. Appropriate for extreme optimism or gamblers focusing on upside. Ignores downside risk and probabilities.

### Q23. State the Laplace (equal likelihood) criterion.
**Model answer:** Treat all states as equally likely and maximise expected payoff: Σ Payoff_i / n. Justified by the principle of insufficient reason — without probability information, assign equal probabilities. Simple but arbitrary.

### Q24. State Hurwicz's criterion.
**Model answer:** Weighted average of maximin and maximax using an optimism coefficient α ∈ [0,1]: H = α·(max payoff) + (1−α)·(min payoff). α = 0 is maximin; α = 1 is maximax. Allows the decision-maker to reflect their level of optimism.

### Q25. State the minimax regret criterion.
**Model answer:** Regret_{ij} = (max payoff in state j) − (payoff_{ij}). Choose the alternative minimising the maximum regret across states. Avoids decisions that could be highly regretted if the opposite state occurs.

### Q26. Compare EMV and minimax regret in principle.
**Model answer:** EMV weighs outcomes by probability — averages over states. Minimax regret considers how much regret one would feel if a suboptimal decision were made, and minimises the worst regret. Regret theory is less sensitive to probability estimates but requires defined payoff structure.

### Q27. What is a dominated alternative?
**Model answer:** An alternative is dominated if another alternative has at least as high a payoff in every state and strictly higher in at least one state. Dominated alternatives can be eliminated without further analysis. They never appear as optimal under any rational criterion.

### Q28. Explain the utility function.
**Model answer:** A function U(payoff) that maps monetary outcomes to subjective utility. Risk-averse: concave (e.g., log). Risk-neutral: linear (U = payoff). Risk-seeking: convex. Decisions should maximise expected utility E[U(payoff)], not EMV, when risk attitudes matter.

### Q29. Define the certainty equivalent.
**Model answer:** The guaranteed payoff that yields the same utility as a risky prospect. CE = U⁻¹(E[U(payoff)]). For a risk-averse decision-maker, CE < EMV; the difference is the risk premium they'd pay to avoid uncertainty.

### Q30. Why is decision analysis under uncertainty important in business?
**Model answer:** Most real decisions (new product launch, investment, M&A) involve uncertain outcomes. Formal decision analysis: (i) forces explicit reasoning, (ii) enables consistent decision-making, (iii) quantifies value of information, (iv) communicates trade-offs to stakeholders, (v) documents reasoning for audit and learning.

---

## Part D: Numerical Problems (Q31-40)

### Q31. Two options: A (payoff 10 with p=0.7, −5 with p=0.3), B (payoff 4 for certain). Find EMV and optimal choice.
**Model answer:** EMV(A) = 0.7(10) + 0.3(−5) = 7 − 1.5 = 5.5. EMV(B) = 4. Choose A with higher EMV. Note: higher variance — risk-averse decision-maker might prefer B despite lower EMV.

### Q32. Compute EVPI given state probabilities 0.6 (good) and 0.4 (bad), max payoff per state: $100 (good), $40 (bad), and best EMV = $60.
**Model answer:** E[max payoff] = 0.6(100) + 0.4(40) = 60 + 16 = $76. EVPI = 76 − 60 = $16. Decision-maker should pay up to $16 for perfect information about which state will occur.

### Q33. Test accuracy: P(+|disease) = 0.9, P(−|no disease) = 0.8. Prior P(disease) = 0.2. Find P(disease|+).
**Model answer:** P(+|no disease) = 0.2. P(+) = 0.9(0.2) + 0.2(0.8) = 0.18 + 0.16 = 0.34. P(disease|+) = 0.18/0.34 = 0.529 or 52.9%.

### Q34. Decision tree: Invest $100K with 40% chance of $300K return, 60% chance of $0. Or don't invest ($100K retained). Optimal?
**Model answer:** EMV(Invest) = 0.4(300K − 100K) + 0.6(0 − 100K) = 0.4(200K) − 60K = 80K − 60K = $20K. EMV(Don't) = $0 (relative to baseline of doing nothing; $100K retained is baseline). Choose Invest for EMV = $20K, but large downside risk of $100K loss with 60% probability.

### Q35. Regret table for decisions A, B: states S1, S2 with payoffs A(50, 20), B(40, 30). Compute max regret.
**Model answer:** Max payoff in S1 = 50, in S2 = 30. Regret A: (0, 10). Regret B: (10, 0). Max regret A = 10; Max regret B = 10. Tied — both equally preferred by minimax regret. EMV with P(S1) = P(S2) = 0.5: A = 35, B = 35; also tied.

### Q36. Laplace criterion for payoff matrix A(30, 60), B(40, 50). Choose.
**Model answer:** Average A = (30+60)/2 = 45. Average B = (40+50)/2 = 45. Tied. Need additional tie-break: look at variance (A has higher), or apply different criterion. In practice, prefer B for lower risk if tied.

### Q37. Hurwicz with α = 0.6: A(max=80, min=20), B(max=60, min=40). Choose.
**Model answer:** H(A) = 0.6(80) + 0.4(20) = 48 + 8 = 56. H(B) = 0.6(60) + 0.4(40) = 36 + 16 = 52. Choose A. With lower α (more pessimistic), B becomes preferred — sensitivity to α matters.

### Q38. A decision-maker has utility U(x) = √x. Prefers 100 for certain or 0/400 coin flip?
**Model answer:** U(100) = 10. E[U(flip)] = 0.5·√0 + 0.5·√400 = 0 + 0.5(20) = 10. Indifferent in utility terms. EMV of flip = 200 > 100, but the concave utility penalises the uncertainty exactly enough.

### Q39. With priors P(S1) = 0.6, P(S2) = 0.4, and likelihoods P(+|S1) = 0.8, P(+|S2) = 0.3. Update after observing +.
**Model answer:** P(+) = 0.8(0.6) + 0.3(0.4) = 0.48 + 0.12 = 0.60. P(S1|+) = 0.48/0.60 = 0.80. P(S2|+) = 0.12/0.60 = 0.20. Posterior shifts from 0.6 to 0.8 probability on S1.

### Q40. EVSI = $50, EVPI = $80. Compute efficiency.
**Model answer:** Efficiency = 50/80 = 0.625 or 62.5%. The sample captures 62.5% of the maximum value perfect information could provide. Decision: is the sample worth its cost? If cost < $50, yes.

---

## Part E: True/False and Interpretation (Q41-45)

### Q41. T/F: A risk-averse decision-maker always chooses the lowest-variance option.
**Model answer:** FALSE. A risk-averse decision-maker maximises expected utility, balancing EMV and variance. If another option has substantially higher EMV with only slightly higher variance, they may still prefer it. Risk aversion penalises variance, not eliminates all preference for it.

### Q42. T/F: EVPI equals the maximum possible gain from improving decisions.
**Model answer:** TRUE. EVPI is the upper bound on what better information can improve the decision's expected value. It equals the difference between optimal decision with perfect information and optimal under current beliefs. Any imperfect info (EVSI) is at most EVPI.

### Q43. T/F: In a decision tree, chance nodes should be solved before decision nodes.
**Model answer:** TRUE. Backward induction computes chance-node expected values first (at terminal chance nodes), then moves leftward to decision nodes where the decision-maker selects the option maximising downstream EV. Solving left-to-right would be incorrect.

### Q44. T/F: Maximin always produces the same decision as EMV.
**Model answer:** FALSE. Maximin ignores probabilities; EMV uses them. They generally disagree when the worst case for the EMV-maximising choice is much worse than alternatives. Example: an investment with high EMV but large downside may lose to a mediocre safe alternative under maximin.

### Q45. T/F: Sensitivity analysis is only useful after the decision has been made.
**Model answer:** FALSE. Sensitivity analysis is most useful BEFORE the decision. It identifies (i) which parameters drive the decision, (ii) robustness of the recommendation, (iii) where to invest in better data. After the decision is made, it becomes a post-mortem, which is still useful but less impactful.

---

## Part F: Application (Q46-50)

### Q46. A company is deciding whether to launch a new product. Market test cost = $50K. Prior: 60% success probability. Test accuracy: 90% correct. Walk through the decision analysis.
**Model answer:** (1) Draw tree: Test or don't; if test, observe +/−; then launch decision. (2) Compute posteriors by Bayes: P(success|+) and P(success|−). (3) Backward induction: optimal launch/no-launch at each branch. (4) Compute EV of testing and EV of not testing. (5) Compute EVSI (test − no test) and compare to test cost. (6) Test is worthwhile iff EVSI > $50K. Sensitivity analysis on test accuracy and prior probability.

### Q47. A firm must choose between two factory designs. Design A: high fixed cost, low variable cost. Design B: lower fixed cost, higher variable cost. Demand uncertain. How to approach?
**Model answer:** Model demand as a probability distribution (low/medium/high). Compute profit for each design under each demand state. Construct decision tree: choose design → observe demand → earn profit. Compute EMV of each design. Apply sensitivity analysis on demand probabilities and cost parameters. Consider break-even demand for each design. If risk-averse, compare variance; use utility-based framework.

### Q48. You have a 0.6 prior on project success. A consultant study costs $10K; they're right 80% of the time. Study says "success". Update the prior and decide whether to proceed.
**Model answer:** P(success|+) = 0.8(0.6)/[0.8(0.6) + 0.2(0.4)] = 0.48/0.56 = 0.857. If expected payoff(success) = $200K, expected payoff(failure) = −$100K, then EMV(proceed|+) = 0.857(200) + 0.143(−100) = 171.4 − 14.3 = $157.1K. Highly favorable. Decision: proceed. The consultant's study raised confidence from 60% to 85.7% — substantial update.

### Q49. Stock investment: Stock A (E = 10%, σ = 20%), Stock B (E = 7%, σ = 10%). Utility U(r) = r − 0.5(σ²). Rank.
**Model answer:** Utility A = 10 − 0.5(400) = 10 − 200 = −190. Utility B = 7 − 0.5(100) = 7 − 50 = −43. B has higher utility; preferred by risk-averse investor with this utility function. Despite A's higher expected return, its higher variance overwhelms it under strong risk aversion. Illustrates the risk-return trade-off and importance of utility framework.

### Q50. A manager faces three strategies under uncertain economic conditions. Payoffs: Growth (100, 60, 20), Stable (70, 80, 50), Defensive (40, 50, 80). Economic states: Boom (30%), Normal (50%), Recession (20%). Recommend with full analysis.
**Model answer:** EMV(Growth) = 0.3(100) + 0.5(60) + 0.2(20) = 30 + 30 + 4 = 64. EMV(Stable) = 0.3(70) + 0.5(80) + 0.2(50) = 21 + 40 + 10 = 71. EMV(Defensive) = 0.3(40) + 0.5(50) + 0.2(80) = 12 + 25 + 16 = 53. Rank: Stable > Growth > Defensive. Recommend Stable strategy: highest EMV (71) and moderate variance. Cross-check with maximin (Defensive = 40 wins here — noting risk aversion). Decision: Stable aligns EMV with moderate variance — no strategy is dominant across all criteria. Report EMV ranking, note Defensive protects downside, and suggest sensitivity analysis on state probabilities before committing.

---

**Exam tip:** For decision analysis questions, always: (1) draw the tree clearly with nodes labelled, (2) compute EMV step by step with backward induction, (3) state the optimal decision explicitly, (4) compute EVPI/EVSI when testing is involved, (5) perform sensitivity analysis on key probabilities, (6) consider risk preferences beyond pure EMV for real-world decisions.
