# Chapter 4.2.4.1.1: K-Means Clustering

## The Problem: Finding Natural Groups

Imagine you're a music streaming company with data about millions of users - their listening habits, song preferences, time spent on the platform. You want to understand: are there natural groups of users with similar behaviors?

Or imagine you run an online store and have customer purchase data. You want to find groups of customers with similar buying patterns so you can tailor marketing to each group differently.

In both cases, the key difference from what we've learned before is: **there are no pre-defined labels**.

In linear regression or classification, we have examples paired with answers. Here, we just have examples - and we want the algorithm to discover the meaningful groups on its own.

---

## What Is Clustering?

Clustering is **unsupervised learning** - learning without labels.

The goal is simple:

> Group similar data points together and separate different ones apart

The challenge: what does "similar" mean? How do we know when we've found good groups?

K-Means is the simplest and most commonly used answer. The "K" means you have to decide in advance how many groups (clusters) you want to find.

---

## The Core Idea: Centroids and Distances

K-Means works with a simple concept:

> Each cluster is represented by its center point, called a **centroid**

Imagine 100 students scattered across a city. K-Means with K=3 would try to:
1. Find 3 center points
2. Assign each student to the closest center
3. Move the centers to better represent their students
4. Repeat until the centers stop moving

The "closeness" is measured by **distance**. The most common is Euclidean distance:

$$d(p_1, p_2) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2 + ... + (z_1 - z_2)^2}$$

This is the straight-line distance between two points in space.

---

## How K-Means Works: The Algorithm

K-Means is an **iterative algorithm**. It repeats the same steps over and over until nothing changes:

### Step 1: Initialize Centroids

Randomly pick K data points to be the starting centroids.

(There are smarter initialization strategies like k-means++, which pick points that are far apart from each other, but random works as a starting point.)

### Step 2: Assign Points to Nearest Centroid

For every data point, calculate its distance to each of the K centroids. Assign it to the centroid it is closest to.

This creates K clusters.

### Step 3: Update Centroids

For each cluster, calculate the mean (average) of all points in that cluster. This becomes the new centroid.

### Step 4: Repeat

Go back to Step 2. Keep repeating until:
- The centroids stop moving, OR
- You've done a maximum number of iterations (to avoid infinite loops)

When the centroids stop changing, we say the algorithm has **converged**.

---

## Mathematical Notation

The objective function K-Means tries to minimize is called the **within-cluster sum of squares**:

$$J = \sum_{i=1}^{K} \sum_{x \in C_i} ||x - \mu_i||^2$$

Where:
- $K$ is the number of clusters
- $C_i$ is cluster $i$
- $\mu_i$ is the centroid of cluster $i$
- $||x - \mu_i||^2$ is the squared distance from point $x$ to the centroid

In words: **sum up how far every point is from its assigned centroid. Try to minimize this total distance.**

---

## Real-World Example: Customer Segmentation

Suppose you have an online store and want to segment customers into K=3 groups based on:
- How much they spend per month
- How many times they buy per month

You collect data on 50 customers:

| Customer | Spending ($) | Frequency |
|----------|-------------|-----------|
| 1        | 50          | 2         |
| 2        | 45          | 3         |
| 3        | 500         | 15        |
| 4        | 600         | 18        |
| ... | ... | ... |

K-Means finds 3 centroids:
- Cluster 1 (Budget Buyers): low spending, low frequency
- Cluster 2 (Regular Customers): medium spending, medium frequency
- Cluster 3 (VIP Customers): high spending, high frequency

Then it can predict: a new customer spending $520/month with 16 purchases would be classified as VIP.

---

## Strengths

**Speed**: K-Means is very fast, even on large datasets. The algorithm is simple and has low computational cost.

**Simplicity**: Easy to understand and implement. The idea is intuitive: group by distance to centers.

**Interpretability**: Each centroid is a real point in the data space, so you can understand what each cluster "looks like."

**Scalability**: Works well with thousands or millions of points.

---

## Limitations

**Requires Choosing K**: You must decide how many clusters in advance. If you pick the wrong K, results will be poor. How do you know the right K? This is an unsolved problem in some domains - you often have to try different values.

**Sensitive to Initialization**: Different random starts can lead to different final clusters. Sometimes K-Means gets stuck in a "local optimum" - a solution that is good locally but not globally best.

**Assumes Spherical Clusters**: K-Means works best when clusters are roughly round. If clusters have different shapes or sizes, it struggles.

Example: Imagine customers in a city where high-spending customers form a crescent shape, not a circle. K-Means might split the crescent into multiple clusters because of their shape.

**Assumes Clusters of Similar Size**: If one cluster has 1,000 points and another has 10, K-Means tends to split the large cluster unnecessarily.

**Outliers Matter**: A few extreme data points can pull centroids in weird directions.

---

## Connection to What Came Before

Chapters 4.1 talked about **data and Optimization**. From Linear regression in 4.2.1 to Nearest Neighbor in Chapter 4.2.3 showed supervised learning - learning when we have labels.

K-Means shows **unsupervised learning** - learning structure without labels. But it still uses the same core idea from Chapter 4.1:

> Learning = finding parameters that minimize an objective function

Here, the parameters are the centroid positions. The objective is within-cluster distance.

---

## What Comes Next

K-Means assumes you know K in advance, and it assumes spherical clusters.

The next clustering methods remove these limitations:

- **DBSCAN**: Finds clusters of any shape, discovers the right number of clusters automatically
- **Hierarchical Clustering**: Creates a tree of nested clusters, lets you choose the granularity
- **Gaussian Mixture Models**: Probabilistic approach - points have probabilities of belonging to each cluster

Each solves a different problem that K-Means cannot handle.