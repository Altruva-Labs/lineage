# Chapter 4.2.7: Kernel Methods

Kernel methods are a class of algorithms that use similarity functions to project data into higher-dimensional spaces.
They let simple linear models act like powerful nonlinear ones without explicitly computing the higher-dimensional coordinates.

## 1. Core Idea

A **kernel** is a function that measures similarity between two examples.
Instead of working with raw features, kernel methods work with pairwise similarities.

A common trick is the **kernel trick**:

- express the algorithm only in terms of dot products
- replace the dot product with a kernel function
- compute similarities directly without ever forming the high-dimensional representation

This lets the model implicitly work in a high (or infinite) dimensional space while keeping computation manageable.

## 2. Main Example: Support Vector Machines (SVM)

The canonical kernel method is the **Support Vector Machine**.
SVMs find a decision boundary that maximizes the margin between classes.
When used with a kernel, SVMs can separate data that is not linearly separable.

Common kernels:

- linear kernel (standard dot product)
- polynomial kernel
- radial basis function (RBF) / Gaussian kernel
- sigmoid kernel

## 3. Related Methods

### Kernel Ridge Regression

This is a version of ridge regression that uses kernels.
It combines regularization with the flexibility of nonlinear kernels.

### Kernel PCA

Kernel Principal Component Analysis extends PCA to nonlinear structure by applying PCA in a kernel-induced feature space.

## 4. Strengths

Kernel methods are powerful when:

- you have limited data
- you need flexible decision boundaries
- you want a principled way to control complexity (via regularization)

They can often compete with neural networks on smaller datasets.

## 5. Limits

However, kernel methods can struggle when:

- datasets are very large (they often require storing a similarity matrix)
- feature engineering is difficult and there is no good kernel choice

## 6. Why This Matters in the Lineage

Kernel methods show another way to get nonlinearity without deep networks.
They form a bridge between classical ML and modern ideas about feature spaces and embeddings.

Our next stop is on methods that combine multiple models into a stronger whole: ensembles.
