# Chapter 4.3.2.7: UMAP (Uniform Manifold Approximation and Projection)

UMAP is a nonlinear dimensionality reduction technique that preserves both local and global structure.
It is commonly used for visualization and embedding data for downstream tasks.

## 1. Core Idea

UMAP builds a graphical representation of the data’s manifold structure and optimizes a low-dimensional embedding that preserves that structure.

## 2. How It Works

- Construct a fuzzy simplicial complex in high-dimensional space.
- Optimize a low-dimensional equivalent using stochastic gradient descent.

## 3. Strengths

- Often faster than t-SNE on large datasets.
- Better at preserving global structure.

## 4. Limits

- Hyperparameters can be unintuitive.
- The embedding can still be unstable across runs.

## 5. Learn More

See the classical models chapter:
`LINEAGE/04_MACHINE_LEARNING/2_Classical_ML_Models/4_Clustering_and_Dimensionality_Reduction/2_Dimensionality_Reduction/3_UMAP.md`
