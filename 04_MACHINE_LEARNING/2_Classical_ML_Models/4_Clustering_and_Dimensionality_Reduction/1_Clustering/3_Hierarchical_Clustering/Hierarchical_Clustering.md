# Chapter 4.2.4.1.3: Hierarchical Clustering

## The Problem: Choosing a Single Granularity

Imagine you're studying animals. You might group them:
- At one level: mammals, reptiles, birds, fish (broad categories)
- At a finer level: dogs, cats, bears, primates (more specific)
- At an even finer level: Labrador, Golden Retriever, Poodle (very specific)

The "right" level depends on what you're doing. If you're writing an encyclopedia of life, you might want 5 categories. If you're managing a zoo, you might want 50.

K-Means and DBSCAN both give you a single clustering - one answer.

**Hierarchical clustering** says: "give me the whole tree of nestings so I can choose my own level."

---

## What Is Hierarchical Clustering?

Hierarchical clustering builds a **tree structure** of clusters:

> Start with each point as its own cluster, then iteratively merge the closest pairs until everything is one big cluster. Then let the user choose where to "cut" the tree.

This is called **agglomerative clustering** (bottom-up - start small, merge upward).

There's also **divisive clustering** (top-down - start with everything, split downward), but agglomerative is much more common.

---

## The Core Idea: Dendrograms

The result is visualized as a **dendrogram** - a tree diagram:

```
           Cluster 1
          /         \
      Sub1          Sub2
     /   \         /   \
    A     B       C     D
```

At the bottom, A, B, C, D are individual points.

Moving up the tree:
- A and B are most similar, so they merge first
- Then C and D merge
- Then the two groups merge

You can "cut" the tree at different heights to get different numbers of clusters:
- Cut high up = few clusters
- Cut lower down = more clusters

---

## How Hierarchical Clustering Works

### Step 1: Start with Every Point as Its Own Cluster

Initially: A, B, C, D, E are 5 separate clusters.

### Step 2: Find the Two Closest Clusters

Calculate distances between all pairs of clusters.

The two closest merge into one cluster.

Distance between clusters can be measured in several ways:

**Single Linkage**: Distance between the two closest points in the clusters.
$$d(C_i, C_j) = \min_{x \in C_i, y \in C_j} d(x, y)$$

**Complete Linkage**: Distance between the two farthest points.
$$d(C_i, C_j) = \max_{x \in C_i, y \in C_j} d(x, y)$$

**Average Linkage**: Average distance between all pairs.
$$d(C_i, C_j) = \frac{1}{|C_i| \cdot |C_j|} \sum_{x \in C_i} \sum_{y \in C_j} d(x, y)$$

### Step 3: Repeat

Now you have 4 clusters. Find the two closest among them and merge.

Repeat until you have 1 cluster (everything merged).

### Step 4: Build the Dendrogram

Record the distance at which each merge happened. This gives you the tree diagram.

---

## Linkage Methods Matter

Different linkage methods produce different results:

**Single Linkage** tends to create long chains (one point close to the next, which is close to the next). Good for finding elongated clusters.

**Complete Linkage** tends to create compact clusters. Points in a cluster are all relatively close to each other. More robust to outliers.

**Average Linkage** is a compromise - balanced between the two.

For most applications, **average linkage** is a good default choice.

---

## Real-World Example: Customer Segmentation

Suppose you have 5 customers and their purchase data:

| Customer | Spending | Frequency |
|----------|----------|-----------|
| A        | $50      | 2x/month  |
| B        | $55      | 2x/month  |
| C        | $500     | 15x/month |
| D        | $600     | 18x/month |
| E        | $200     | 5x/month  |

Hierarchical clustering might produce:

1. **First merge**: A and B (very similar)
2. **Second merge**: C and D (high-value customers)
3. **Third merge**: E joins with something (intermediate value)
4. **Final merge**: All combined

The dendrogram shows this:

```
            All
          /    \
        AB      CDE
       / \      /  \
      A   B    CD   E
             / \
            C   D
```

If you want 3 segments, cut the tree at height 3 (you get AB, CD, E).

If you want 5 segments, cut at the bottom (A, B, C, D, E - everyone separate).

---

## Strengths

**Dendrogram Visualization**: The tree structure is intuitive and gives you a full picture of relationships at multiple scales.

**Flexible Granularity**: You don't choose K in advance. Examine the dendrogram and pick the level that makes sense for your problem.

**No Parameter Sensitivity**: Unlike K-Means (choose K) or DBSCAN (choose eps and min_samples), you just observe the tree and decide.

**Deterministic**: Same data always produces the same dendrogram (unlike K-Means, which is random).

---

## Limitations

**Computational Cost**: For n points, the algorithm is O(n³) complexity in worst case. For 10,000 points, it becomes very slow.

**Greedy Decisions**: Once you merge two clusters, you can't undo it. If early merges are wrong, the final result is affected. Unlike K-Means, which can be re-optimized globally, hierarchical clustering can't go back.

**Hard to Interpret at Scale**: With millions of points, the dendrogram is too large to visualize or interpret.

**Sensitive to Distance Metric**: Changing how you calculate distances (Euclidean vs. Manhattan, etc.) can dramatically change results.

---

## Comparison of Clustering Methods

| Aspect | K-Means | DBSCAN | Hierarchical |
|--------|---------|--------|--------------|
| Choose what? | K | eps, min_samples | Nothing (choose level after) |
| Cluster shapes | Spherical | Any | Any |
| Outline handling | Force all | Mark as noise | Include all |
| Visualization | Centers | Core/border/noise | Dendrogram |
| Speed | Fast | Moderate | Slow (O(n³)) |
| Scalability | Excellent | Good | Poor |

---

## Connection to What Came Before

All three clustering methods (K-Means, DBSCAN, Hierarchical) make different assumptions about what "natural groups" mean:

- K-Means: minimize distance from points to centroids
- DBSCAN: find dense regions
- Hierarchical: build a multi-scale tree of nested groups

---

## What Comes Next

So far, all three methods are **hard clustering** - each point belongs to exactly one cluster (or is noise).

**Gaussian Mixture Models** introduce **soft clustering** - each point has a probability of belonging to each cluster, not a hard assignment.

This is often more realistic: a customer might be 70% like segment A and 30% like segment B.