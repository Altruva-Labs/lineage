# Chapter 4.3.2.3: DBSCAN (Density-Based Spatial Clustering)

DBSCAN groups points that are closely packed together and marks points in low-density regions as noise.

## 1. Core Idea

DBSCAN defines clusters as areas of high density separated by areas of low density.
It has two main parameters:

- `eps`: the radius defining a neighborhood
- `min_samples`: the minimum number of points required to form a dense region

## 2. How It Works

- Identify core points (points with at least `min_samples` neighbors within `eps`).
- Expand clusters from core points by adding reachable points.
- Points that are not reachable from any core point are treated as noise.

## 3. Strengths

- Automatically finds the number of clusters.
- Handles arbitrarily shaped clusters.
- Explicitly identifies noise points.

## 4. Limits

- Choosing `eps` can be tricky.
- Struggles with datasets that have varying densities.

## 5. Where to Learn More

For more detail, see the classical model treatment in the Clustering section:
`LINEAGE/04_MACHINE_LEARNING/2_Classical_ML_Models/4_Clustering_and_Dimensionality_Reduction/1_Clustering/2_DBSCAN.md`
