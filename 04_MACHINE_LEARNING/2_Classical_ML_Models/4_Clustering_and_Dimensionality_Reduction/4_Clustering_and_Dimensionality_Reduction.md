# Chapter 4.2.4: Introduction to Clustering and Dimensionality Reduction

Not all machine learning is about predicting a label.

Sometimes the goal is:

- find natural groups
- simplify data
- uncover hidden structure

Two major ideas here are:

- clustering (see `1_Clustering/`)
- dimensionality reduction (see `2_Dimensionality_Reduction/`)

This chapter is split into two subdirectories for clarity. They are connected because both aim to reveal structure in data without labels:

- clustering groups examples into coherent sets
- dimensionality reduction finds compact representations of the same data

## 1. Clustering

Clustering tries to group similar examples together.

Example:

- customers with similar spending behavior
- documents on similar topics
- songs with similar listening patterns

The key point is:

> the groups are not given in advance

The system tries to discover them from the data.

## 2. Dimensionality Reduction

Dimensionality reduction tries to represent data using fewer dimensions.

Why is this useful?

Because high-dimensional data can be:

- noisy
- redundant
- hard to visualize
- hard to learn from

## 3. Common Methods

This section covers:

- Clustering: K-Means, DBSCAN, Hierarchical Clustering, Gaussian Mixture Models
- Dimensionality Reduction: PCA, t-SNE, UMAP, Autoencoders

## 4. Why These Methods Matter

These methods matter because they show that learning is not only about output prediction.

It can also be about:

- organization
- compression
- representation

These two families are also often used together: for example, a low-dimensional representation can make clustering more robust, and clustering can help evaluate whether a representation captures meaningful structure.

This idea will become very important later when neural networks start learning their own internal representations.

## 5. What Comes Next

We start with clustering methods.

By now, we have seen the major forms of classical machine learning.

But a problem is becoming clearer:

> many of these methods depend heavily on human-designed features

The next step is to see how these model families are woven into the main learning setups:

- supervised learning
- unsupervised learning
- reinforcement learning
