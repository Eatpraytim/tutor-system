# ST2187 — Data Visualisation: 50 Exam Questions with Model Answers

---

## Part A: Chart Selection and Purpose (Q1-10)

### Q1. State the fundamental rule for choosing a chart.
**Model answer:** Chart type must match the question being asked and the data type. Guide: compare (bar chart), distribution (histogram/box plot), relationship (scatter plot), composition (stacked bar, pie), trend over time (line chart). Never use a pie chart when a bar chart would work better.

### Q2. When is a histogram appropriate?
**Model answer:** For showing the distribution of a single continuous variable. Reveals shape (symmetric, skewed, multimodal), centre, spread, outliers. Bin choice matters: too few loses detail; too many obscures shape. Use Sturges' rule (k = log₂n + 1) or Freedman-Diaconis as starting points.

### Q3. When is a box plot preferred over a histogram?
**Model answer:** Box plots efficiently summarise distributions for comparison across groups. Show median, quartiles, IQR, whiskers, outliers. Use when comparing 3+ groups side-by-side. Histograms show more distributional detail for a single variable.

### Q4. When should you NOT use a pie chart?
**Model answer:** (1) When there are more than 5-6 slices (hard to compare). (2) When comparing across multiple groups (use grouped bars). (3) When slices are similar in size (bars show differences better). (4) When showing change over time. Bar charts almost always communicate proportions more effectively.

### Q5. What is the best chart for showing relationships between two continuous variables?
**Model answer:** Scatter plot. Reveals: direction of association (positive/negative), strength, linearity vs non-linearity, outliers, clusters, heteroscedasticity. Add a smoothed line (LOESS) or regression line to highlight the trend. Useful for bivariate exploration and regression diagnostics.

### Q6. Distinguish bar chart and column chart.
**Model answer:** Column chart: vertical bars. Bar chart: horizontal bars (better for long category labels). Function identically otherwise — compare values across categories. Use horizontal for text-heavy labels; vertical when x-axis order matters (e.g., time).

### Q7. When is a line chart appropriate?
**Model answer:** For continuous data over time (time series) or to show trends. X-axis is typically time or another continuous ordered variable. Connect points to emphasise sequence. Not for unordered categories — use bars.

### Q8. What is a heatmap and when to use it?
**Model answer:** A grid where colour intensity encodes values. Ideal for: correlation matrices, two-way contingency tables, large datasets with many categories. Choose colour scales carefully — diverging for bidirectional data (e.g., correlations from −1 to 1); sequential for unidirectional (counts).

### Q9. What is a violin plot?
**Model answer:** Combines a box plot with a kernel density estimate on either side, showing both summary statistics and the full distribution shape. Useful when distributions are multimodal or non-normal — features hidden by a standard box plot are revealed.

### Q10. Define small multiples (trellis/facet plots).
**Model answer:** Multiple small charts, each showing a subset of data, arranged in a grid. Each panel is the same chart type with consistent scales but different data slices. Excellent for: comparing patterns across many groups, time periods, or dimensions without overcrowding a single chart.

---

## Part B: Principles of Visual Design (Q11-20)

### Q11. State Tufte's principle of data-ink ratio.
**Model answer:** Maximise data-ink, minimise non-data-ink. Remove chart junk (3D effects, unnecessary gridlines, heavy borders). Every visual element should communicate data. Ratio = data-ink / total ink — high ratios are better.

### Q12. Explain the lie factor.
**Model answer:** Lie factor = (size of effect shown in graph) / (size of effect in data). Should equal 1. Common violations: truncated y-axis, 3D effects, non-proportional pictograms. Exaggeration by lie factor > 1 is dishonest; factor < 1 understates.

### Q13. When is a truncated y-axis acceptable?
**Model answer:** When the baseline (usually zero) is not meaningful or the chart's purpose is to show small changes. Acceptable in financial charts showing daily fluctuations. Not acceptable when comparing magnitudes of categories — truncating inflates visual differences misleadingly.

### Q14. What is colour vision deficiency and how to design for it?
**Model answer:** ~8% of men have red-green colour deficiency. Design accessible charts: (1) Use colourblind-safe palettes (ColorBrewer, Viridis). (2) Don't rely solely on colour — add patterns, labels, or position. (3) Test with simulators. (4) Use redundant encodings (colour + shape + label).

### Q15. Describe the gestalt principles relevant to visualisation.
**Model answer:** (1) Proximity — group related items visually. (2) Similarity — similar colour/shape signal belongs together. (3) Continuity — lines draw the eye along paths. (4) Closure — viewers complete incomplete shapes. (5) Figure/ground — foreground vs background. These principles guide layout and encoding choices.

### Q16. What does 'aspect ratio' mean for charts?
**Model answer:** Ratio of height to width. For line charts, "banking to 45°" — choose ratio so typical slopes are ~45°. For scatter plots, aspect ratio influences perceived correlation. Rule: don't distort for aesthetics; let data dictate shape.

### Q17. Explain logarithmic scales and when to use them.
**Model answer:** Y-axis displayed in log(Y). Equal distances = equal ratios (e.g., 1, 10, 100, 1000). Use when: data spans orders of magnitude, multiplicative relationships matter (growth rates, half-lives), or distribution is lognormal. A log scale linearises exponential growth.

### Q18. What is a dual-axis chart and its risks?
**Model answer:** A chart with two y-axes showing different variables. Risks: (1) misleading by forcing correlations through axis scaling, (2) reader confusion, (3) overload. Alternative: separate small multiples or indexed values (each series = 100 at start). Use dual axes only when both series are measured in fundamentally different units.

### Q19. What is pre-attentive processing?
**Model answer:** The visual system processes certain properties in ~250ms without conscious attention: colour, size, shape, position, movement. Effective visualisations encode the most important data in pre-attentive channels. Example: colour highlights an outlier; position on a scale shows magnitude.

### Q20. List Stephen Few's four functional dashboards.
**Model answer:** (1) Operational — real-time monitoring (call centres, manufacturing). (2) Tactical — short-term management decisions (weekly KPIs). (3) Strategic — executive overview (quarterly balanced scorecard). (4) Analytical — deep exploration (data science). Match design to purpose and audience.

---

## Part C: Interpretation Questions (Q21-30)

### Q21. A scatter plot shows a funnel shape. What does this suggest?
**Model answer:** Heteroscedasticity — variability of Y increases (or decreases) with X. The relationship may still be linear on average but with non-constant variance. Implications: OLS regression assumptions violated; use robust SE or WLS. Transform Y (log) may stabilise variance.

### Q22. A histogram has two peaks. What might this indicate?
**Model answer:** Bimodal distribution — two subpopulations mixed in the data. Causes: different groups (e.g., male/female heights), regime changes, measurement errors in discrete categories. Investigate by splitting the data on a suspected grouping variable. Summary statistics (mean, SD) poorly represent bimodal data.

### Q23. A box plot shows one group has much longer whiskers. Interpret.
**Model answer:** That group has more variability (wider spread) and/or more extreme values. The median may be similar, but the distribution is more dispersed. Outliers (shown as dots beyond whiskers) deserve individual investigation. Consider whether the group is genuinely more variable or has data quality issues.

### Q24. A time series line chart shows regular spikes every December. Interpret.
**Model answer:** Seasonal pattern — likely due to holiday effects (retail sales, heating costs). Should be accounted for via seasonal adjustment, dummy variables, or SARIMA models. Failing to account for seasonality leads to biased forecasts and misleading growth claims.

### Q25. Correlation plot heatmap shows X3 and X5 are highly correlated. Implications?
**Model answer:** Multicollinearity — problematic if both used as predictors in regression: inflated SEs, unstable coefficients, sign reversals. Implications: (i) consider dropping one, (ii) combine into an index, (iii) use ridge regression. Also suggests redundant information; data collection can be reduced.

### Q26. A bar chart comparing two quarters shows a 5% increase, but the y-axis starts at 95%. How to critique?
**Model answer:** Visually misleading — the truncated y-axis makes a small change (5% relative) look enormous. Ethical practice: start at zero for bar charts, OR annotate clearly and justify the truncation. Show the comparison with a full-range chart alongside or as a second view.

### Q27. Pie chart shows "Other" = 35% of categories. What's wrong?
**Model answer:** The "Other" category is too large to be relegated to grouping — individual details are lost. Solution: regroup meaningfully (e.g., top 5 explicit + small "Other"), switch to a bar chart allowing more categories, or create a hierarchical treemap.

### Q28. Interpret a Q-Q plot where points deviate from the line in the tails.
**Model answer:** Heavy tails in the data relative to the reference distribution (usually normal). If points are above line at right end and below line at left end: heavy-tailed (t-distribution-like). If opposite: thin tails. Q-Q plots diagnose normality assumption violations visually.

### Q29. A scatter plot shows two distinct clusters. How do you proceed?
**Model answer:** Likely presence of subgroups in the data. Possible causes: gender, region, time period, measurement batches. Action: (1) identify the grouping variable, (2) colour-code by group to verify, (3) analyse groups separately or with interaction terms, (4) a single regression across mixed groups would be misleading.

### Q30. A control chart shows a sustained run of points above the mean line. Diagnose.
**Model answer:** Process shift — the mean has changed. Signal: 7+ consecutive points above (or below) the centreline. Investigate: equipment change, new materials, personnel change, measurement drift. Quality control rules (Western Electric, Nelson) formalise these patterns. Do not wait for out-of-control individual points.

---

## Part D: Visualisation Tools and Software (Q31-40)

### Q31. Compare Excel, Tableau, and R/Python for visualisation.
**Model answer:** Excel: ubiquitous, fast for simple charts, limited for complex analysis. Tableau: drag-and-drop, interactive dashboards, expensive licences, limited reproducibility. R/Python (ggplot2, matplotlib, plotly): free, fully reproducible, steep learning curve, powerful for custom graphics. Choice depends on audience, reproducibility needs, and complexity.

### Q32. Briefly describe ggplot2's grammar of graphics.
**Model answer:** Layered grammar: (1) data, (2) aesthetic mapping (x, y, colour, size), (3) geoms (points, lines, bars), (4) statistical transformations (smooths, binning), (5) scales, (6) coordinate systems, (7) facets. Build complex plots by composing layers. The same syntax handles almost any chart type.

### Q33. What is Tableau's "Show Me" feature?
**Model answer:** Automatic chart recommendations based on selected fields and their data types (measures vs dimensions). Suggests appropriate chart forms. Useful starting point, but domain knowledge is needed to refine — automatic choice isn't always optimal.

### Q34. Describe plotly's interactive capabilities.
**Model answer:** Plotly generates web-based interactive charts: hover tooltips, zooming, filtering, legend clicking, exporting. Interactivity suits exploratory analysis and dashboards better than static images. Available in Python, R, and JavaScript (Plotly.js).

### Q35. What is D3.js and when is it appropriate?
**Model answer:** JavaScript library for custom web-based data visualisations. Extremely flexible — any chart type possible. Steep learning curve. Use when: standard chart libraries cannot achieve the desired visual; custom storytelling visualisations (e.g., NYT graphics); high-end web experiences.

### Q36. What is Dash / Shiny and their purpose?
**Model answer:** Dash (Python) and Shiny (R) are web frameworks for building interactive dashboards. Backend data processing + frontend visualisation. Use for: business dashboards, analytical apps, data exploration tools. No JavaScript needed — the framework handles web rendering.

### Q37. Define exploratory vs explanatory visualisation.
**Model answer:** Exploratory: analyst explores data to find patterns (many quick iterations, minimal polish). Explanatory: polished output for communicating findings to an audience (careful labelling, narrative, design). Different purposes require different styles and effort levels.

### Q38. What is a small multiples (faceted) plot?
**Model answer:** A grid of similar small plots, each showing a data subset. Shared axes allow comparison across panels. Example: sales by product line shown as one panel per line. More effective than overlaying many series in one chart.

### Q39. Define data storytelling.
**Model answer:** Using data visualisation within a narrative structure: context, conflict, resolution. Combines analytical rigour with human storytelling. Elements: clear takeaway, annotations guiding attention, progressive reveal, actionable recommendations. Cole Nussbaumer Knaflic's "Storytelling with Data" is the standard reference.

### Q40. What is the role of annotations in charts?
**Model answer:** Annotations explicitly state conclusions, highlight key points, or provide context. Examples: arrow pointing at a peak with explanation; trend line labelled "forecast"; coloured band showing a target range. Without annotations, readers must infer meaning — many won't. Use sparingly but deliberately.

---

## Part E: Ethics and Critique (Q41-45)

### Q41. Name three ways charts mislead viewers.
**Model answer:** (1) Truncated y-axis on bar charts exaggerates differences. (2) Dual axes forcing misleading correlations. (3) 3D effects distorting magnitude perception. (4) Missing context (e.g., a "record high" without historical baseline). (5) Cherry-picked time windows. Always question the design choices before trusting a chart.

### Q42. Critique: A line chart compares 2 series but uses two different y-axis scales.
**Model answer:** Dual axes can artificially imply correlations — moving one axis's scale changes the visual relationship. Critique: are the two series commensurate? Often they should be indexed to 100 at a common baseline, scaled to percentages, or shown in separate panels. Dual axes are rarely the clearest choice.

### Q43. An advertisement shows sales "soaring" with a tiny y-axis range making a 2% increase look like a mountain. Is this ethical?
**Model answer:** Misleading — the magnitude of change is visually exaggerated beyond what the data supports. This violates Tufte's lie-factor principle. Ethically, marketers should show the full picture; truncated axes are acceptable only with clear annotations explaining the view and showing proportional context.

### Q44. A chart shows COVID deaths growing "exponentially" on a linear scale. Why switch to log scale?
**Model answer:** Linear scale makes exponential growth look like a vertical wall — useful for dramatic effect but obscures growth rates. Log scale linearises exponential patterns — constant slope = constant growth rate. Epidemiologists often prefer log scales to compare growth rates across countries or detect deceleration.

### Q45. How do you critique a visualisation?
**Model answer:** Check: (1) Is the chart type appropriate for the question? (2) Are axes labelled correctly with units? (3) Does the scaling mislead? (4) Is data sufficient for the claim? (5) Are colours chosen for clarity and accessibility? (6) Does the title/annotation match the data? (7) Could an alternative chart communicate better? (8) Is there a source citation?

---

## Part F: Application (Q46-50)

### Q46. A retail analyst has sales data across 50 stores, 20 categories, 12 months. Recommend visualisations.
**Model answer:** (1) Heatmap: store × category for a given month — identify stores under/over-performing by category. (2) Line chart with small multiples: sales over time, one panel per category — show seasonality. (3) Bubble map of stores — geographic patterns. (4) Pareto chart of top categories by sales — identify the vital few. (5) Dashboard combining these for exploration. Avoid single charts trying to show all dimensions at once.

### Q47. A quality engineer wants to detect whether a process has gone out of control. What viz?
**Model answer:** (1) Control chart (X̄ chart with control limits at ±3σ from target mean). Plot process measurements over time with upper and lower control limits. Mark points outside limits or patterns (runs, trends). (2) R or S chart alongside to track variability. (3) Pareto of defect types. Control charts transform statistics into a monitoring tool — action triggered when signals appear.

### Q48. A marketing team wants to compare conversion rates across 6 campaigns over 4 quarters. Viz recommendation.
**Model answer:** Grouped bar chart (campaign on x-axis, conversion rate on y-axis, colour = quarter) or line chart with small multiples (one panel per campaign). Line chart better if trends over quarters matter; grouped bars better for comparing campaigns within a quarter. Clearly label highest and lowest to draw the eye.

### Q49. An executive wants a dashboard summarising business health. How to design?
**Model answer:** Top-of-screen: 4-6 KPIs with values and direction (up/down arrows). Middle: trend line charts for revenue, margin, customer count over 12+ months. Right: bar chart of top performers by region or product. Bottom: drill-down filters for dates, regions. Use traffic-light colouring sparingly (red/amber/green) for alerts only. Update frequency: daily/weekly. Executive dashboards prioritise clarity and actionable signals over comprehensiveness.

### Q50. Your regression output suggests a non-linear relationship. Which visualisations help diagnose and model?
**Model answer:** (1) Scatter plot of X vs Y with LOESS/smooth overlay — visual confirmation of non-linearity. (2) Residual vs fitted plot — U-shape suggests quadratic; fan suggests variance transformation. (3) Partial residual plot (X vs residuals after controlling for other predictors) — isolates each predictor's non-linear effect. (4) Compare R² of linear, log-log, and polynomial models. (5) Cross-validation RMSE to avoid overfitting. Visual diagnostics guide model choice.

---

**Exam tip:** For visualisation questions, always: (1) state the chart type and justify it based on data type and purpose, (2) describe axes and scaling choices, (3) address potential misinterpretations, (4) link the visualisation to an analytical conclusion or business decision. For critique questions, be systematic: chart choice, scaling, labelling, accessibility, honesty.
