# Chapter 4.3.2.4: Hierarchical Clustering

Hierarchical clustering builds a tree (dendrogram) of nested clusters.

## 1. Core Idea

There are two main approaches:

- **Agglomerative** (bottom-up): start with each point in its own cluster, then merge the closest pairs.
- **Divisive** (top-down): start with all points in one cluster, then recursively split.

## 2. How It Works (Agglomerative)

- Compute distances between points.
- Merge the two closest clusters.
- Update distances using a linkage criterion (single, complete, average).
- Repeat until all points are in one cluster.

## 3. Strengths

- No need to choose a fixed number of clusters upfront.
- Provides a visual summary (dendrogram).

## 4. Limits

- Can be computationally expensive (O(n^3) in naive implementations).
- Sensitive to noise and outliers.

## 5. Where to Learn More

For a deeper explanation, see the classical model chapter:
`LINEAGE/04_MACHINE_LEARNING/2_Classical_ML_Models/4_Clustering_and_Dimensionality_Reduction/1_Clustering/3_Hierarchical_Clustering.md`
