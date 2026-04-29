# ST3188 — Cluster Analysis: 50 Exam Questions with Model Answers

---

## Part A: Fundamentals (Q1-10)

### Q1. What is cluster analysis?
**Model answer:** An unsupervised multivariate technique that groups objects (customers, products, cases) into clusters so that members within a cluster are similar and members of different clusters are dissimilar. Unlike discriminant analysis, there are no pre-defined groups — they emerge from the data.

### Q2. Distinguish cluster analysis from discriminant analysis.
**Model answer:** Discriminant analysis: supervised — groups are known in advance; classifies new cases into them. Cluster analysis: unsupervised — groups are discovered from data. Output of cluster analysis is often input to discriminant analysis: first find segments, then build classifier.

### Q3. State the main applications of cluster analysis.
**Model answer:** (1) Market segmentation — grouping customers by behaviour or demographics. (2) Product positioning. (3) Pattern recognition. (4) Test selection. (5) Document clustering. (6) Biomedical grouping. (7) Pre-processing for other analyses (sub-group regression). (8) Anomaly detection.

### Q4. State the two main families of clustering methods.
**Model answer:** (1) Hierarchical: builds a tree (dendrogram) of nested clusters. Agglomerative (bottom-up) or divisive (top-down). (2) Non-hierarchical (partitioning): k-means, k-medoids. Requires pre-specified number of clusters; iteratively assigns observations. Different strengths: hierarchical for visualisation; partitioning for large datasets.

### Q5. Define similarity and dissimilarity measures.
**Model answer:** Quantify how alike/different two observations are. For continuous variables: Euclidean distance (default), squared Euclidean, Manhattan, Mahalonobis. For categorical: simple matching, Jaccard. For mixed: Gower coefficient. Choice affects clusters.

### Q6. Describe Euclidean distance.
**Model answer:** d(x, y) = √(Σ(xᵢ − yᵢ)²). Straight-line distance between points in k-dimensional space. Sensitive to scale of variables. Standardise variables first (unless measurement units are comparable). Most common distance metric.

### Q7. Describe Mahalonobis distance.
**Model answer:** Multivariate distance accounting for correlations between variables: d² = (x−y)ᵀ Σ⁻¹ (x−y). Scales differences by covariance. Invariant to linear transformations. Useful when variables are correlated; removes this as a source of spurious distance.

### Q8. Why standardise variables before clustering?
**Model answer:** Variables in different units have different ranges. A variable measured in pounds (0-500) vs metres (0-2) will dominate distance calculations. Standardising (z-scores or min-max) gives each variable equal weight. Skipping standardisation allows scale to drive clustering — usually undesirable.

### Q9. State the assumptions and requirements of cluster analysis.
**Model answer:** (1) Meaningful similarity metric. (2) Representative sample. (3) Distinct cluster structure exists in the data. (4) Variables measure relevant characteristics. (5) No severe outliers (distort centroids). (6) Appropriate sample size — enough for each cluster to be meaningful.

### Q10. What is the curse of dimensionality in clustering?
**Model answer:** In high-dimensional space, distances between points become similar, making clusters hard to distinguish. Variables with little discriminative power add noise. Remedies: (1) Feature selection — use only meaningful variables. (2) Dimensionality reduction (PCA, factor analysis). (3) Specialised high-dim clustering algorithms.

---

## Part B: Hierarchical Clustering (Q11-20)

### Q11. Describe agglomerative hierarchical clustering.
**Model answer:** Bottom-up approach: start with each observation as its own cluster. At each step, merge the two most similar clusters. Continue until one big cluster. Produces a dendrogram. Popular due to transparency. Single-pass: once merged, clusters cannot split.

### Q12. Describe divisive hierarchical clustering.
**Model answer:** Top-down approach: start with one large cluster, split into sub-clusters iteratively. Computationally expensive; less common than agglomerative. Advantage: early splits are key decisions (opposite of agglomerative's early merges).

### Q13. State the main linkage methods.
**Model answer:** (1) Single linkage — minimum distance between cluster members. (2) Complete linkage — maximum distance. (3) Average linkage — average pairwise distance. (4) Ward's method — minimise within-cluster variance. Each produces different cluster shapes. Ward's most popular; complete next.

### Q14. Compare single and complete linkage.
**Model answer:** Single: tends to create "chained" elongated clusters — nearest pair joins tightly. Sensitive to noise. Complete: compact, spherical clusters — farthest pair must be close for merger. More robust. Single detects patterns; complete detects clear groups.

### Q15. Describe Ward's method.
**Model answer:** Merges clusters minimising the increase in total within-cluster sum of squares (variance). Produces compact, roughly spherical clusters of similar sizes. Most commonly used hierarchical method. Assumes continuous variables and Euclidean distance.

### Q16. Describe a dendrogram.
**Model answer:** Tree diagram showing hierarchical merging: x-axis = observations, y-axis = distance at merger. Height of horizontal line = distance between merged clusters. Cut the tree at a chosen height to define number of clusters. Visual tool for choosing cluster number.

### Q17. How do you decide cluster count from a dendrogram?
**Model answer:** (1) Visual inspection — look for large vertical jumps indicating natural cluster boundaries. (2) Knee/elbow in cluster merger distance. (3) Cut at a distance threshold based on theory. (4) Silhouette analysis on resulting partition. Subjective decision guided by multiple criteria.

### Q18. State the computational complexity of hierarchical clustering.
**Model answer:** O(n³) for standard agglomerative — cannot scale beyond ~10,000 observations. Distance matrix is n×n = O(n²) memory. For large datasets, use k-means or approximate methods. Alternative: subset clustering or parallelised algorithms.

### Q19. Can hierarchical clustering handle outliers well?
**Model answer:** No. Single-linkage especially sensitive — one outlier connects distant clusters via chaining. Complete linkage and Ward's more robust. Remedies: (1) Detect and remove outliers first. (2) Use robust distance measures. (3) Try multiple linkages and compare. (4) Consider density-based clustering (DBSCAN) for outlier detection.

### Q20. What's the practical advantage of hierarchical clustering?
**Model answer:** (1) Does not require pre-specifying number of clusters — examine dendrogram. (2) Reveals cluster structure at multiple scales (sub-clusters within clusters). (3) Deterministic — same input yields same result. (4) Well-established interpretation via dendrogram. (5) Works with any dissimilarity matrix.

---

## Part C: K-Means and Partitioning Methods (Q21-30)

### Q21. Describe the k-means algorithm.
**Model answer:** (1) Choose k (number of clusters). (2) Randomly initialise k centroids. (3) Assign each observation to nearest centroid. (4) Recompute centroids as the mean of assigned observations. (5) Repeat 3-4 until centroids stabilise. Converges to local minimum of within-cluster sum of squares.

### Q22. State the objective function of k-means.
**Model answer:** Minimise total within-cluster sum of squares: SSW = ΣΣ ||x_ij − μ_i||² summed over clusters i and their members j. μ_i is the centroid of cluster i. k-means finds clusters that minimise SSW — equivalent to maximising between-cluster separation.

### Q23. What are the limitations of k-means?
**Model answer:** (1) Must pre-specify k. (2) Assumes spherical clusters of equal size. (3) Sensitive to initial centroid placement — may find local minima. (4) Sensitive to outliers — centroids distorted. (5) Assumes Euclidean distance. (6) Cannot handle categorical variables directly. (7) Stochastic due to random initialisation.

### Q24. How to choose k in k-means?
**Model answer:** (1) Elbow method: plot SSW vs k; look for knee. (2) Silhouette score: measure cohesion vs separation; choose k maximising average silhouette. (3) Gap statistic: compare SSW to null reference distribution. (4) BIC/AIC for probabilistic clustering (Gaussian mixture). (5) Theory/business knowledge. Combine multiple criteria.

### Q25. Describe the elbow method.
**Model answer:** Plot within-cluster SS (or %) vs number of clusters. As k increases, SS decreases. Look for "elbow" — point where marginal decrease drops sharply. Choose k at the elbow. Subjective but commonly used. Combine with silhouette analysis for robustness.

### Q26. Describe silhouette analysis.
**Model answer:** For each point, silhouette width s(i) = (b − a)/max(a, b), where a = mean distance to own cluster, b = mean distance to nearest other cluster. Range [-1, 1]. High values = well-clustered. Average across points; choose k maximising average silhouette. Interpretable and widely used.

### Q27. What is k-means++ initialisation?
**Model answer:** Smarter initialisation than random: pick first centroid randomly; subsequent centroids chosen with probability proportional to squared distance from nearest existing centroid. Tends to spread initial centroids, improving convergence quality and reducing need for multiple runs.

### Q28. Compare k-means and hierarchical clustering.
**Model answer:** K-means: fast, scalable, partition-based, requires k. Hierarchical: shows nested structure, dendrogram for visualisation, slower, small-to-medium datasets. K-means for exploratory segmentation with known k; hierarchical for structure exploration and when k is unknown.

### Q29. Describe k-medoids (PAM).
**Model answer:** Partitioning Around Medoids. Similar to k-means but uses actual observations as cluster centres (medoids) rather than means. More robust to outliers; supports any distance metric (not just Euclidean). Slower than k-means. Good for interpretable cluster centres.

### Q30. What is a cluster profile?
**Model answer:** Description of each cluster by its characteristics on key variables. Summarised by means (for continuous) and frequencies (for categorical) per cluster. Used to interpret and label clusters: "Cluster 1 = young, high-income urban professionals." Essential for making clusters actionable.

---

## Part D: Evaluating and Interpreting Clusters (Q31-40)

### Q31. How to evaluate cluster quality?
**Model answer:** Internal metrics (no external truth): (1) Within-cluster sum of squares. (2) Silhouette score. (3) Calinski-Harabasz index. (4) Davies-Bouldin index. External metrics (if true labels known): (1) Adjusted Rand Index. (2) Mutual information. Typically use multiple metrics; visualise clusters when possible.

### Q32. Describe the Calinski-Harabasz index.
**Model answer:** Ratio of between-cluster variance to within-cluster variance, adjusted for df. Higher = better separation. Well-defined for any k. Good for comparing clustering solutions. Complements silhouette as alternative internal validation.

### Q33. Describe the Davies-Bouldin index.
**Model answer:** Average similarity between each cluster and its most similar neighbour. Lower = better (clusters are tight and well-separated). Commonly reported alongside other validation metrics.

### Q34. What is cluster stability?
**Model answer:** Whether repeated clustering on similar data yields similar clusters. Tests: (1) Bootstrapping — resample, re-cluster, measure agreement. (2) Cross-validation — split data, cluster subsets, compare to full solution. (3) Noise injection — add small random noise, re-cluster. Unstable solutions suggest noisy or over-extracted clusters.

### Q35. How to validate market segmentation clusters?
**Model answer:** (1) Internal validation — silhouette, within-cluster distances. (2) External validation — do clusters differ meaningfully on outcome variables (e.g., purchase behaviour)? (3) Theoretical coherence — do clusters match reasonable segmentations? (4) Managerial utility — are clusters actionable and reachable? (5) Stability over time — do segments persist? (6) Replication on independent sample.

### Q36. When are clusters "statistically significant"?
**Model answer:** Statistical significance in clustering is contested. Standard tests don't apply since clustering doesn't have a formal null hypothesis of "no clusters". Use: (1) Gap statistic (compare to null uniform data). (2) Bootstrap cluster stability. (3) Formal tests like GAP or silhouette bootstrap. (4) Ultimately, substantive interpretation matters more than statistical significance.

### Q37. What is a silhouette score of 0.3?
**Model answer:** Marginal clustering — points have some but weak separation from other clusters. Benchmarks: > 0.5 reasonable, > 0.7 strong, < 0.25 artificial clusters. 0.3 suggests further refinement: try different k, different variables, or different algorithm. Clusters may exist but are not sharply distinct.

### Q38. Describe the gap statistic.
**Model answer:** Compare log(SSW) for observed data to expected log(SSW) under uniform null distribution at each k. Gap(k) = E[log(SSW_null)] − log(SSW_observed). Larger gap = stronger cluster structure. Optimal k at first local maximum where gap exceeds next k's gap minus SE. Formalised selection; common in academic clustering.

### Q39. How should you interpret and label clusters?
**Model answer:** (1) Compute cluster means/frequencies on key variables. (2) Identify distinctive variables — variables with largest between-cluster differences. (3) Label with descriptive name capturing essence (e.g., "Price-Sensitive Families"). (4) Characterise on demographic and behavioural dimensions. (5) Compare across clusters in tabular form. (6) Validate interpretation with domain experts.

### Q40. What if k-means produces clusters that don't make business sense?
**Model answer:** (1) Review input variables — are they relevant? Remove irrelevant. (2) Check scaling — dominant variables skew results. (3) Try different k. (4) Try different algorithm (Ward's, PAM). (5) Outliers — remove and re-cluster. (6) Investigate: maybe the data genuinely lacks meaningful clusters. (7) Bring domain expert judgement — "useful" clusters align with business constructs.

---

## Part E: Applications and Considerations (Q41-45)

### Q41. When is cluster analysis NOT appropriate?
**Model answer:** (1) Small samples (< 50). (2) Too few clusters discernible in data. (3) Unclear what variables to cluster on. (4) Strong temporal structure (need time-series methods). (5) When pre-defined groups are known (use discriminant analysis). (6) When seeking causal relationships (clustering describes, doesn't explain).

### Q42. Describe pre-processing steps before clustering.
**Model answer:** (1) Handle missing data — impute or remove. (2) Standardise continuous variables. (3) Encode categorical variables if using k-means — or use Gower's distance. (4) Remove extreme outliers. (5) Reduce dimensionality if many variables (PCA first). (6) Check variable correlations — highly correlated variables may dominate.

### Q43. What is Gower's coefficient?
**Model answer:** Dissimilarity metric for mixed-type data (continuous, binary, ordinal). For each variable, calculates a contribution based on type; averages across variables. Widely used with datasets combining demographic, behavioural, and categorical variables. Range [0, 1].

### Q44. How many clusters are too many?
**Model answer:** Rule of thumb: k ≤ √(n/2) or k selected where clusters remain interpretable and actionable. Over-clustering produces tiny, unstable groups. In marketing, 3-7 segments often optimal — enough differentiation, few enough to address strategically. Hierarchical allows sub-clustering if needed.

### Q45. Describe DBSCAN (density-based clustering).
**Model answer:** Groups points that are densely packed together; marks outliers as noise. Parameters: ε (neighborhood radius), minPts (minimum points in ε-neighborhood to form a core point). Advantages: (1) Finds arbitrarily shaped clusters. (2) Doesn't require pre-specifying k. (3) Identifies outliers. Weaknesses: (1) Sensitive to ε. (2) Struggles with varying density.

---

## Part F: Application (Q46-50)

### Q46. Design a customer segmentation for a bank.
**Model answer:** (1) Variables: demographics (age, income, location), product holdings, transaction patterns, channel usage, customer lifetime value. (2) Standardise all variables. (3) Pre-process: handle missing, remove outliers. (4) Test k = 3-7 via elbow, silhouette. (5) Primary method: Ward's hierarchical or k-means; compare solutions. (6) Profile clusters: e.g., "Mass Affluent Young", "Multi-Product Families". (7) Validate: check cluster stability via bootstrapping. (8) Implement: tailor marketing, service, pricing by segment. (9) Monitor: segment composition changes over time.

### Q47. A retail store has 500 products. How to group similar products?
**Model answer:** (1) Variables: sales volume, price, margin, category, seasonality, customer demographics of purchasers. (2) Standardise. (3) Hierarchical clustering with Ward's for moderate dataset size. (4) Choose k by dendrogram inspection and silhouette. (5) Label clusters: "High-velocity impulse buys", "High-margin specialty", etc. (6) Use for: assortment planning, promotion targeting, supplier negotiations, shelf layout. (7) Validate: subjective check with category managers.

### Q48. Your k-means has silhouette = 0.45 and clusters sizes 50, 45, 3, 2. Evaluate.
**Model answer:** Moderate silhouette is adequate but small clusters (3, 2) are concerning — often represent outliers or noise, not meaningful segments. Options: (1) Remove outliers first; re-cluster. (2) Reduce k to 2 (natural large split). (3) Merge small clusters if they are near larger ones. (4) Investigate small clusters' characteristics — may reveal anomalies of business interest. Tiny clusters are rarely actionable as segments.

### Q49. A cluster analysis of 1 million customer transactions. Approach?
**Model answer:** (1) Hierarchical infeasible; use k-means with k-means++ initialisation. (2) Pre-process: feature engineering to create meaningful variables (RFM — Recency, Frequency, Monetary). (3) Scale appropriately. (4) Iterate k from 3 to 10; evaluate silhouette, Calinski-Harabasz. (5) Multiple runs with different seeds; select consistent solution. (6) Consider parallel implementations or sampling-based methods. (7) Profile clusters on meaningful business metrics. (8) Validate via business outcome (e.g., cluster predicts churn, lifetime value).

### Q50. Compare cluster analysis and factor analysis.
**Model answer:** Both unsupervised, but different goals. Factor analysis: identifies underlying latent dimensions that explain variable correlations — reduces variables. Cluster analysis: identifies homogeneous groups of observations — reduces observations. Often complementary: (1) FA first to identify key constructs. (2) Compute factor scores. (3) Cluster customers based on factor scores. Produces meaningful, interpretable segments based on latent constructs.

---

**Exam tip:** For cluster analysis questions, always: (1) justify variable selection and scaling, (2) justify algorithm choice (hierarchical for small data/visualisation, k-means for scale), (3) determine k via multiple criteria (elbow, silhouette, theory), (4) evaluate cluster quality (silhouette, CH index), (5) interpret clusters substantively with labels, (6) validate stability and practical utility.
