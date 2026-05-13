# Chapter 4.2.4.2.3: UMAP (Uniform Manifold Approximation and Projection)

## The Problem with t-SNE

t-SNE is fantastic for visualization, but it has a big weakness:

**It is super slow.**

With even 10,000 points, t-SNE can take minutes or hours.  
With 100,000 points? Forget it.

Also, t-SNE loses global structure. Two clusters might appear right next to each other in the plot even though they are far apart in the original space.

UMAP solves these problems by asking:

> Can I preserve both local neighborhoods AND global structure?  
> Can I do it faster than t-SNE?

The answer is yes.

---

## The Core Idea: Graph-Based Approach

Instead of thinking about point-to-point relationships, think about the **shape of the data** itself.

Imagine your high-dimensional data forms a bumpy surface (manifold).

UMAP's approach:
1. Build a graph where each point connects to its k nearest neighbors (local structure)
2. Extend this to capture global connectivity (global structure)
3. "Unfold" this graph into 2D or 3D while preserving the graph's structure

It is like taking a crumpled piece of paper (your data in high dimensions) and carefully unfolding it flat (into 2D) while trying not to tear it (preserving relationships).

---

## Why It is Faster

UMAP uses a mathematical concept called **fuzzy topology** combined with **stochastic gradient descent**.

Instead of:
- t-SNE: Computing all pairwise distances (O(n²))
- UMAP: Building a k-nearest-neighbor graph and optimizing locally

This is like the difference between:
- Checking distances to every person at a stadium (slow)
- Only checking distances to your 30 nearest neighbors and extending from there (fast)

---

## Algorithm: Three Steps

### Step 1: Build K-NN Graph in High Dimensions

For each point, find its k nearest neighbors.

Connect these neighbors with weighted edges. The weight represents how likely they are close in the true manifold.

### Step 2: Create a Fuzzy Topological Representation

Combine all these local neighborhoods into a global graph structure.

This graph captures "local structure" (neighbors are connected) but also "global structure" (how neighborhoods connect to each other).

### Step 3: Optimize Low-Dimensional Embedding

Start with random 2D or 3D coordinates.

Iteratively adjust them to:
- Keep nearby points close (match the graph)
- Push apart points that should be far (maintain separation)

Use stochastic sampling — don't process all edges every iteration, just random samples. This is what makes it fast.

---

## Real-World Example: Gene Expression Data

Biologists have a dataset of 10,000 cells, each measured on 20,000 genes.

- t-SNE: 30 minutes to visualize
- UMAP: 2 minutes to visualize

After running UMAP, they see:
- Red cluster (cell type A)
- Blue cluster (cell type B)
- Green cluster (between them, probably transitional cells)

With t-SNE, the resolution is less clear. Clusters might appear randomly positioned.

With UMAP, the spatial arrangement actually means something: clusters that are closer in the plot are more similar.

---

## Key Parameters

### n_neighbors
- How many nearby points does each point connect to?
- Typical: 5-50
- Effect: Smaller values = more importance on local structure, larger values = global structure
- Example: n_neighbors=5 focuses on tight neighborhoods; n_neighbors=15 sees the broader picture

### min_dist
- How close can two points be in the low-dimensional space before repulsion occurs?
- Typical: 0.001 to 0.1
- Lower values: tighter clusters; higher values: more spread out

### n_epochs
- How many iterations to optimize
- Typical: 100-500
- Fewer epochs = faster but less optimized; more epochs = slower but better results

### metric
- How to measure distance: 'euclidean', 'cosine', 'manhattan', etc.
- Choose based on your data type

---

## Strengths and Weaknesses

### Strengths
- **Fast**: 100× faster than t-SNE on large datasets
- **Scalable**: Works on 1M+ points
- **Global structure**: Preserves overall layout, not just local clusters
- **Flexible**: Works with any distance metric
- **General-purpose**: Not just for visualization; can use embedding as features for downstream tasks

### Weaknesses
- **Hyperparameter-sensitive**: Results vary significantly with n_neighbors
- **Less interpretable**: Like t-SNE, distances in plot don't directly correspond to original space
- **Non-deterministic**: Different runs can give different results (though more stable than t-SNE)
- **Approximation**: Uses k-NN approximation, so it misses some long-range relationships

---

## UMAP vs. t-SNE vs. PCA

| Aspect | PCA | t-SNE | UMAP |
|--------|-----|-------|------|
| Speed | Fast (< 1 sec) | Slow (minutes) | Medium (seconds) |
| Scalability | Excellent | Poor | Excellent |
| Local structure | Misses | Excellent | Excellent |
| Global structure | Excellent | Loses | Good |
| New data | Easy (linear projection) | Hard | Medium |
| Interpretability | High (linear) | Low | Low |
| Use case | Quick baseline | Deep exploration | General-purpose |

---

## When to Use UMAP

- **Quick visualization**: When you need answers in seconds, not minutes
- **Large datasets**: > 10,000 points
- **Both tasks**: Visualization AND using embedding as features
- **Stable results**: When you need reproducible plots
- **Complex data**: Non-linear structure with many classes/groups

---

## Behind the Scenes: Why This Works

UMAP is based on **topological data analysis** and **manifold learning theory**.

The key insight: if you preserve the "shape" (topology) of your data locally, the global shape takes care of itself.

It is similar to how you can describe the shape of a coastline — not by every tiny detail, but by the overall curvy pattern that emerges when you step back.

---

## What Comes Next

UMAP is still fundamentally a **geometry-based** method that assumes your data lives on a lower-dimensional manifold.

But what if your data structure is even more complex? What if you want to learn the representation automatically from data?

**Autoencoders** (Chapter 4.2.4.2.4) are neural networks that learn to compress and decompress data end-to-end, discovering optimal representations for your specific task.