# Chapter 4.3.2.6: t-SNE (t-Distributed Stochastic Neighbor Embedding)

t-SNE is a nonlinear embedding technique designed for visualizing high-dimensional data.

## 1. Core Idea

t-SNE maps high-dimensional points into a low-dimensional space (usually 2D or 3D) such that similar points stay close together.
It focuses on preserving local structure rather than global distances.

## 2. How It Works

- Convert high-dimensional distances into pairwise similarities (probabilities).
- Define a similar probability distribution in low-dimensional space.
- Minimize the divergence between the two distributions using gradient descent.

## 3. Strengths

- Often reveals cluster structure in complex datasets.
- Great for visualization and exploratory data analysis.

## 4. Limits

- Can be slow for large datasets.
- Results can vary depending on hyperparameters (perplexity, learning rate).
- Not designed for out-of-sample generalization.

## 5. Learn More

See the classical models treatment:
`LINEAGE/04_MACHINE_LEARNING/2_Classical_ML_Models/4_Clustering_and_Dimensionality_Reduction/2_Dimensionality_Reduction/2_t_SNE.md`
