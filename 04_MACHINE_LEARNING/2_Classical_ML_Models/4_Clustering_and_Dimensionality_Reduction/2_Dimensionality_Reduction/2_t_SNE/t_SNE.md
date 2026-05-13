# Chapter 4.2.4.2.2: t-Distributed Stochastic Neighbor Embedding (t-SNE)

## The Problem with PCA

PCA finds global structure—it preserves distances between far-apart points.

But what if you care about **local structure**?

Imagine a dataset of handwritten digits (0, 1, 2, ..., 9). Each image is 28×28 pixels = 784 features.

PCA might tell you that pixel brightness varies a lot, so the first principal component is brightness.  
But you actually care more that **"similar-looking 3s cluster together"** and **"3s and 8s are nearby"**.

This is local structure: relationships between neighbors.

t-SNE solves this by saying:

> If two points are neighbors in my original high-dimensional space, they should stay neighbors in my low-dimensional visualization.

---

## Intuition: Crowding Problem

When you project high-dimensional data to 2D or 3D, something bad happens: **the crowding problem**.

Imagine 100 points evenly distributed in a sphere of radius 10 (high dimensions).  
They are all roughly equidistant from each other.

Now project them to a 2D circle of radius 1 (low dimensions).  
You can't fit 100 points without them overlapping!

So you are forced to put some distant points close together.

t-SNE manages this by thinking probabilistically:

> In high dimensions, what is the probability that point A is a neighbor of point B?

> In low dimensions, enforce the same probability.

This automatically "pushes apart" clusters if there is room, while "squeezing together" necessarily overlapping regions.

---

## How t-SNE Works

### Step 1: Compute Distances in High Dimensions

For each pair of points, calculate how far apart they are.

Convert distances to **probabilities**: points that are close have high probability of being neighbors, far points have low probability.

### Step 2: Initialize Low-Dimensional Representation

Start with random 2D or 3D coordinates for each point.

### Step 3: Iterative Optimization

Repeat many times:

1. Compute distances in the low-dimensional space
2. Convert to probabilities
3. Measure the difference between high-D and low-D probabilities
4. Move points to make low-D probabilities match high-D probabilities better
5. Gradually decrease "temperature" (learning rate)

This is like **gravity and repulsion**: similar points attract, dissimilar points repel.

---

## Real-World Example: MNIST Digits

Here is what happens when you run t-SNE on 5,000 handwritten digit images:

Before (784-dimensional):
- All 10,000 images are scattered in a high-dimensional space
- You can't see their structure

After t-SNE (2D):
```
        1  2
       /|||||\
      /  0  3\\
      |   4   |
      \ 5 6 7/
       \|||||/ 
        9  8
```

Each digit (0-9) forms its own cluster!

Digits that look similar (like 3 and 8, or 4 and 9) are **near** each other.

All this is automatically discovered from the pixel patterns alone.

---

## Key Parameters

### Perplexity
- Controls how many neighbors a point "sees" immediately
- Typical range: 5-50
- Higher perplexity = more global structure, lower perplexity = more local structure
- For 5,000 samples, try perplexity = 30

### Learning Rate
- Controls how fast points move
- Too high = chaotic jumps, too low = slow convergence
- Usually auto-tuned

### Number of Iterations
- t-SNE is slow (roughly O(n²))
- Needs hundreds to thousands of iterations to converge
- You can often stop when clusters stop changing

---

## Strengths and Weaknesses

### Strengths
- **Fantastic for visualization**: Produces beautiful, interpretable 2D/3D plots
- **Preserves local structure**: Neighbors stay neighbors
- **Automatic cluster discovery**: Often reveals clusters you didn't know existed
- **Works with any distance metric**: Not limited to Euclidean

### Weaknesses
- **Slow**: O(n²) complexity, impractical for > 100,000 points
- **Non-deterministic**: Different random initializations → different results
- **Hard to interpret distances**: Distances in the plot are not meaningful; only "clusters" matter
- **Not suitable for new data**: Can't easily project new test points (unlike PCA)
- **Loses global structure**: Far-apart clusters might appear close

---

## When to Use t-SNE

- **Exploratory data analysis**: "What clusters are naturally in my data?"
- **Visualization of embeddings**: After training a neural network, visualize what it learned
- **Sanity checking**: "Does my model group similar images together?"
- **Diagnosis**: "Why are these two classes overlapping?"

---

## Important Notes

### Why "t-distributed"?
In the low-dimensional space, t-SNE uses a "heavy-tailed" Student's t-distribution instead of Gaussian.  
This helps push apart clusters that would otherwise overlap.

### Comparison to PCA
| Aspect | PCA | t-SNE |
|--------|-----|-------|
| Speed | Fast | Slow |
| Global structure | Good | Loses detail |
| Local structure | Misses | Excellent |
| Interpretability | Linear directions | Group proximity |
| New data | Easy to project | Difficult |

---

## What Comes Next

t-SNE is powerful but slow.

**UMAP** (Chapter 4.2.4.2.3) is a newer alternative that is faster and preserves local structure reasonably well.  
**Autoencoders** (Chapter 4.2.4.2.4) are neural networks that learn nonlinear dimensionality reduction end-to-end from data.