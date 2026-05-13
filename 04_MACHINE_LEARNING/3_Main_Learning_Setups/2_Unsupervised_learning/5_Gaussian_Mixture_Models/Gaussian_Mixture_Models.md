# Chapter 4.3.2.5: Gaussian Mixture Models (GMM)

Gaussian Mixture Models offer a probabilistic approach to clustering.
They model the data as a weighted mixture of Gaussian distributions.

## 1. Core Idea

Each data point is assumed to be generated from one of several Gaussian components.
GMMs compute a soft membership probability for each component.

## 2. How It Works

- Initialize component means, covariances, and mixture weights.
- Run Expectation-Maximization (EM):
  - **E-step:** compute the probability each point belongs to each component.
  - **M-step:** update component parameters to maximize expected likelihood.

## 3. Strengths

- Soft cluster assignments allow uncertainty estimation.
- Can model elliptical clusters with different shapes.

## 4. Limits

- Requires specifying the number of components.
- Sensitive to initialization and can converge to local optima.

## 5. Learn More

See the classical models chapter for a deeper dive:
`LINEAGE/04_MACHINE_LEARNING/2_Classical_ML_Models/4_Clustering_and_Dimensionality_Reduction/1_Clustering/4_Gaussian_Mixture_Models.md`
