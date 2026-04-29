# ST3188 — MDS & Mixed Methods: 50 Exam Questions with Model Answers

---

## Part A: Multidimensional Scaling (MDS) Fundamentals (Q1-10)

### Q1. What is multidimensional scaling (MDS)?
**Model answer:** A technique for visualising similarities/dissimilarities between objects in a low-dimensional map. Objects represented as points; distances between points reflect their dissimilarity. Used for perceptual mapping in marketing, psychology, and information retrieval.

### Q2. State the main applications of MDS.
**Model answer:** (1) Perceptual mapping — how consumers perceive brands/products. (2) Positioning analysis — identify gaps and opportunities. (3) Competitive analysis — which brands are perceived similarly. (4) Market segmentation. (5) Dimension reduction for visualisation. (6) Network analysis.

### Q3. What are the main types of MDS?
**Model answer:** (1) Metric MDS — dissimilarities are treated as distances; preserves actual distances. (2) Non-metric MDS — dissimilarities are ordinal; preserves rank order. More flexible and common for perceptual data. (3) Individual differences MDS (INDSCAL) — allows individual weighting of dimensions.

### Q4. State typical data inputs for MDS.
**Model answer:** (1) Direct similarity ratings — respondents rate pairs on similarity scale. (2) Dissimilarity matrix — computed from attribute ratings or distances. (3) Correlation matrix (converted to distance). (4) Conjoint-style preference data. (5) Co-occurrence data (how often items appear together).

### Q5. What is a similarity matrix?
**Model answer:** Symmetric matrix where element (i, j) is the similarity between objects i and j. Diagonal = 1 (object most similar to itself). Off-diagonal elements in [0, 1] or other scale. Higher values = more similar. Input to MDS; converted to dissimilarity by 1 − similarity.

### Q6. How does MDS estimate dimensions?
**Model answer:** Starting from dissimilarity matrix: (1) Initial configuration (random or principal coordinates). (2) Iteratively adjust point positions to minimise stress (mismatch between actual and fitted distances). (3) Continues until stress converges. (4) Final configuration represents positions in k-dimensional space.

### Q7. What is stress in MDS?
**Model answer:** A measure of mismatch between input dissimilarities and distances in the MDS configuration. Lower stress = better representation. Kruskal's stress: √(Σ(d_{ij} − δ_{ij})² / Σ d²_{ij}). Rules of thumb: < 0.05 excellent, < 0.10 good, < 0.20 acceptable, > 0.20 poor.

### Q8. How do you choose the number of dimensions?
**Model answer:** (1) Stress plot: stress vs dimensions. Look for elbow — point where additional dimension adds little. (2) Interpretability: prefer fewer dimensions that can be labelled meaningfully. (3) Typically 2-3 dimensions for visualisation and interpretation. (4) Higher dimensions fit better but become hard to interpret.

### Q9. What is a scree plot in MDS?
**Model answer:** Plot of stress value vs number of dimensions. Decreasing curve — more dimensions, less stress. Look for "elbow" indicating diminishing returns. Choose dimension count before elbow where stress is acceptable. Similar interpretation to factor analysis scree.

### Q10. How do you interpret MDS dimensions?
**Model answer:** (1) Examine positions of well-understood objects on each dimension. (2) Group of objects high on a dimension vs low — what do they have in common? (3) Assign dimension labels based on shared attributes (e.g., luxury/economy; performance/comfort). (4) May not always be interpretable — report as "Dimension 1/2" if meaningless.

---

## Part B: MDS Types and Variants (Q11-20)

### Q11. Describe metric MDS.
**Model answer:** Assumes dissimilarities are ratio/interval scale and represented as actual distances. Uses classical eigendecomposition. Also called Torgerson's or principal coordinates analysis. Good for distance matrices from quantitative measurements.

### Q12. Describe non-metric MDS (Kruskal's MDS).
**Model answer:** Assumes dissimilarities are ordinal — preserves rank order of distances, not magnitudes. Uses iterative gradient descent. More flexible for subjective ratings. Most common MDS type in marketing. Also called Kruskal-Shepard MDS.

### Q13. What is INDSCAL?
**Model answer:** Individual Differences Scaling — extends MDS to allow each individual to weight dimensions differently. Useful when respondents differ in how they perceive attributes. Produces: common configuration + individual weights on each dimension. Reveals individual differences in perception.

### Q14. Compare MDS and factor analysis.
**Model answer:** Both reduce dimensionality. MDS: uses distance/dissimilarity matrix between objects; produces configuration in low-dim space. Factor analysis: uses correlation matrix between variables; produces loadings of variables on factors. MDS for mapping similar objects; FA for identifying latent dimensions explaining variable correlations.

### Q15. Compare MDS and correspondence analysis.
**Model answer:** MDS: input is dissimilarity matrix between objects. Correspondence analysis: input is contingency table (counts of categorical co-occurrences). CA produces simultaneous plot of rows and columns showing associations. Both visualise structure; different data types.

### Q16. What is the Shepard diagram?
**Model answer:** Plot of fitted distances (MDS) vs actual dissimilarities. Ideally on a 45° line. Deviations indicate poor fit. In non-metric MDS, monotone transformation between them — plot shows monotonic relationship. Diagnostic tool for evaluating MDS solution quality.

### Q17. What are external analyses in MDS?
**Model answer:** After producing configuration, relate dimensions to external variables via regression. Attribute fitting: for each attribute, regress attribute values on dimensions. Properties align with dimensions reveal interpretation. Technique: PROFIT (Property Fitting) analysis.

### Q18. What is property fitting (PROFIT)?
**Model answer:** Method to interpret MDS dimensions. For each attribute, fit a regression: attribute_value = β₀ + β₁·Dim1 + β₂·Dim2. Vector from origin in direction (β₁, β₂) points toward objects high on that attribute. Overlays attributes on configuration map.

### Q19. Describe biplot.
**Model answer:** Simultaneous display of objects (points) and variables (vectors) in 2D. Object positions = scores. Vector directions = attribute loadings. Projecting object onto vector = predicted value. Used in MDS, PCA, correspondence analysis. Single compact visualisation of both rows and columns.

### Q20. How to interpret a vector's length in a biplot?
**Model answer:** Length represents importance/variance captured. Longer vectors = attribute contributes more to configuration. Short vectors = attribute weakly represented; interpretation less reliable. Angle between vectors: acute = positive correlation; obtuse = negative; 90° = uncorrelated.

---

## Part C: Mixed Methods Research (Q21-30)

### Q21. Define mixed methods research.
**Model answer:** Integration of quantitative and qualitative methods within a single study. Leverages strengths of both: quant for breadth and generalisation; qual for depth and context. Design explicit about how methods integrate and how findings converge or diverge.

### Q22. State the main mixed methods designs.
**Model answer:** (1) Convergent parallel — both simultaneously, compared. (2) Sequential explanatory — quant first, then qual to explain. (3) Sequential exploratory — qual first, then quant to test. (4) Embedded — one method supports the other. (5) Multiphase — iterative combination across phases.

### Q23. When is convergent parallel design appropriate?
**Model answer:** When you want to cross-validate findings: compare quantitative data and qualitative insights on the same topic. Strengths: multiple perspectives. Weakness: reconciling different results. Example: survey on satisfaction (quant) + focus groups (qual) to triangulate.

### Q24. When is sequential explanatory appropriate?
**Model answer:** When quantitative results need qualitative explanation. Flow: (1) Large-scale survey identifies patterns or outliers. (2) Qualitative interviews explore "why" with select participants. Strength: depth on surprising findings. Weakness: sequential = longer project.

### Q25. When is sequential exploratory appropriate?
**Model answer:** When qualitative exploration precedes quantitative testing. Flow: (1) Interviews or focus groups identify key constructs. (2) Develop and test scales/hypotheses quantitatively. Used in scale development and new domain research. Strength: grounded in real experience. Weakness: requires theoretical coherence across phases.

### Q26. What is an embedded mixed methods design?
**Model answer:** One method (e.g., RCT) plus embedded secondary method (e.g., in-depth interviews with subset). Qualitative data enriches quantitative findings but doesn't change the core design. Common in clinical trials with qualitative process evaluation.

### Q27. State challenges of mixed methods.
**Model answer:** (1) Requires expertise in both methodologies. (2) Time and resource intensive. (3) Integrating divergent findings. (4) Presenting both to audiences who prefer one. (5) Paradigm conflicts (positivism vs interpretivism). (6) Reviewer preferences may not match mixed approach. (7) Word limits in publications.

### Q28. What does triangulation mean?
**Model answer:** Using multiple methods or data sources to validate findings. Types: (1) Data triangulation — multiple sources. (2) Investigator triangulation — multiple researchers. (3) Method triangulation — qual + quant. (4) Theoretical triangulation — multiple theoretical perspectives. Increases validity when methods converge.

### Q29. Distinguish pragmatism, dialectical stances in mixed methods.
**Model answer:** Pragmatism: "what works" orientation. Methods chosen for utility; less concerned with paradigm. Dialectical: deliberately uses conflicting paradigms to generate insights from tensions. Both support mixed methods but with different philosophical emphases. Pragmatism most common.

### Q30. How do you integrate mixed methods findings?
**Model answer:** (1) Side-by-side comparison — present quant and qual results in separate sections, compare in discussion. (2) Joint display — table with quant and qual findings integrated for each theme. (3) Merged interpretation — synthesise within discussion. (4) Follow-up — qual explains quant outliers; quant generalises qual themes.

---

## Part D: MDS Applications (Q31-40)

### Q31. Market research firm wants to map brand positioning. Design an MDS study.
**Model answer:** (1) Select 8-12 brands (including competitors and new entrants). (2) Collect similarity ratings: respondents rate all pairs on 9-point scale. (3) Alternatively, derive dissimilarity from attribute ratings. (4) Sample 100-200 respondents from target market. (5) Compute average dissimilarity matrix. (6) Run non-metric MDS. (7) Plot 2D configuration; label dimensions. (8) Overlay attribute vectors via PROFIT. (9) Identify competitive clusters and market gaps.

### Q32. How to interpret a perceptual map?
**Model answer:** (1) Close brands are perceived similarly — direct competitors. (2) Distant brands are perceived differently — may target distinct segments. (3) Empty spaces = potential positioning opportunities. (4) Relate dimensions to key attributes. (5) Brand positioning: how close to target position? (6) Action: reposition by changing attributes or messaging.

### Q33. An MDS shows 3 dimensions explain 95% of variance. Interpret.
**Model answer:** Market perception is complex — not just 2D. 3 dimensions capture main variation. Interpret each dimension by examining high/low brands. Visualisation: 3D plot or 2D projections. Strategic: consider all 3 dimensions when positioning. Note: higher dimensions harder to interpret — may reflect noise.

### Q34. Stress = 0.25 in your MDS. Interpret.
**Model answer:** Poor fit — configuration doesn't represent dissimilarities well. Actions: (1) Add dimensions. (2) Check data quality — respondent errors? (3) Respondents may perceive differences subjectively (non-metric approach). (4) Perhaps no clear structure exists in data. (5) Try different MDS algorithm. Don't interpret stress > 0.20 without improvement.

### Q35. An MDS of 10 car brands shows 2 distinct clusters. Interpret.
**Model answer:** Two perceptual positions: e.g., Cluster A = luxury (BMW, Mercedes, Audi); Cluster B = mainstream (Toyota, Honda, Ford). Within-cluster brands compete directly; between-cluster brands operate in different market spaces. Gap between clusters may represent a market opportunity for brands positioning between.

### Q36. Dimension 1 shows luxury-value; Dimension 2 shows performance-comfort. How to use?
**Model answer:** (1) Map target segment's ideal position. (2) Identify brands closest to that ideal — main competitors. (3) Assess your brand's position relative to target. (4) Design strategic actions: messaging, product features to shift perceptions toward desired position. (5) Re-survey after intervention to measure perception change.

### Q37. Compare MDS and cluster analysis for market segmentation.
**Model answer:** MDS: visualises brand positioning — objects are brands. Cluster analysis: groups customers — objects are individuals. Can combine: cluster customers into segments, then MDS each segment to understand their brand perceptions. Complementary tools for strategic marketing.

### Q38. What if MDS dimensions aren't interpretable?
**Model answer:** (1) Examine extreme objects on each dimension — what do they have in common? (2) Conduct PROFIT analysis — align with attributes. (3) Collect additional attribute ratings to correlate with dimensions. (4) Respondents may use unique cognitive dimensions not measured. (5) Report dimensions as "Dim 1" with caveat. Interpretation is the hardest step.

### Q39. How to validate MDS results?
**Model answer:** (1) Replicate with independent sample. (2) Check stress — should be < 0.15 for reliable interpretation. (3) Compare to alternative methods (PCA, correspondence analysis). (4) Domain expert review — do dimensions and positions make theoretical sense? (5) Predictive validation — if positioning drives choice, should correlate with market share.

### Q40. A new brand wants to position between luxury and value. How does MDS help?
**Model answer:** (1) Conduct MDS of existing brands — identify luxury and value poles. (2) Target position: between these clusters. (3) Design product attributes consistent with target: moderate quality, mid-range price, selective features. (4) Position marketing messages to reinforce this intermediate identity. (5) Post-launch, re-run MDS to verify intended position. (6) Adjust if perception differs from intention.

---

## Part E: True/False and Interpretation (Q41-45)

### Q41. T/F: MDS works only with numerical data.
**Model answer:** FALSE. MDS works with similarity or dissimilarity matrices, which can be derived from subjective ratings, rankings, co-occurrence data, or any measurement that can be converted to distance. Non-metric MDS specifically handles ordinal data.

### Q42. T/F: Low stress always means good model.
**Model answer:** NEARLY TRUE. Low stress (< 0.10) indicates good fit, but: (1) Over-fitting possible with many dimensions. (2) Low stress from small dataset may be artifactual. (3) Interpret stress alongside interpretability. Aim for low stress AND interpretable dimensions.

### Q43. T/F: MDS dimensions have inherent labels.
**Model answer:** FALSE. MDS produces unlabelled dimensions. Labels come from: (1) Examining what objects cluster together on each dimension. (2) Correlating dimensions with measured attributes. (3) Domain expertise. Interpretation is subjective and can be wrong.

### Q44. T/F: Mixed methods requires equal weight to qual and quant.
**Model answer:** FALSE. Designs vary: convergent gives equal weight; embedded gives main method more weight. Sequential weights vary by research question. Choose based on research goals. Report methodology transparently; don't artificially balance if one is primary.

### Q45. T/F: MDS and factor analysis produce the same output.
**Model answer:** FALSE. Different inputs, different outputs. MDS: distance matrix between objects → spatial configuration. FA: correlation matrix between variables → loading structure. They can give complementary views: FA identifies underlying constructs; MDS maps objects on these or other dimensions.

---

## Part F: Application (Q46-50)

### Q46. A retailer wants to understand store positioning vs competitors. Design.
**Model answer:** (1) Define competitive set: 10-12 relevant retailers. (2) Survey 200 shoppers: rate all pairs on similarity (or rate on attributes for computed dissimilarity). (3) Aggregate matrix. (4) Non-metric MDS; examine stress plot; choose 2-3 dimensions. (5) Plot map; label dimensions (e.g., price-value, product variety). (6) Identify competitive clusters. (7) Strategic: assess own position, identify gaps for positioning. (8) Track over time to monitor perception drift.

### Q47. A mixed methods study on remote work impact. Design.
**Model answer:** Sequential explanatory design. (1) Phase 1 (Quant): Survey 1,000 workers on satisfaction, productivity, work-life balance pre- and post-remote shift. Identify significant changes and outliers. (2) Phase 2 (Qual): In-depth interviews with n = 30, selected from extremes (most satisfied, most distressed). Explore "why" findings. (3) Integration: triangulate findings in discussion. Identify themes quant missed; validate themes with survey respondents. (4) Report: quant provides scale and trends; qual provides understanding and recommendations.

### Q48. Critique an MDS solution with 2 dimensions, stress = 0.12, one brand in a corner away from others.
**Model answer:** (1) Stress acceptable (< 0.15). (2) Isolated brand (corner): highly distinctive — either unique positioning or data issue. (3) Investigate: (a) Does the isolated brand genuinely occupy unique perceptual space? (b) Sample error — too few respondents rated that brand? (c) Outlier respondents skewing matrix? (4) Interpret: if genuine, unique positioning may be strength (no direct competitors) or weakness (no perceived similarity to trusted alternatives). (5) Validate with separate data sources.

### Q49. Compare perceptual map vs positioning statement approaches.
**Model answer:** Perceptual map (MDS): data-driven, reveals actual consumer perception. Strengths: objective, identifies gaps. Weaknesses: may miss new positioning not yet attempted. Positioning statement: aspirational, strategic choice. Strengths: enables brand differentiation strategy. Weaknesses: may not match reality. Best practice: develop positioning statement informed by MDS; validate perceived position post-launch with follow-up MDS.

### Q50. Describe a mixed methods study using MDS.
**Model answer:** Research question: "How do consumers perceive brands in the luxury watch market?" Design: (1) Phase 1 (Quant): 300 consumers rate similarities among 10 watch brands; run non-metric MDS. Identify clusters. (2) Phase 2 (Qual): In-depth interviews with 15 participants from different perceptual positions — why do they perceive brands as similar/different? (3) Interpretation: quantitative structure (map) + qualitative understanding (reasons for perception). (4) Deliverables: positioning map (visual) + consumer narratives explaining perceptions. More actionable than either method alone — marketers know where brands are AND why.

---

**Exam tip:** For MDS questions, always: (1) specify metric vs non-metric based on data type, (2) report stress and justify dimension count, (3) interpret dimensions through extreme objects or property fitting, (4) overlay external variables for interpretation, (5) validate with independent data. For mixed methods: (1) justify design type, (2) describe integration clearly, (3) report how findings converge or diverge, (4) use joint displays or triangulation narratives.
