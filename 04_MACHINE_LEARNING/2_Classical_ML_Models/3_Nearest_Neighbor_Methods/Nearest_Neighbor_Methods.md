# Chapter 4.2.3: Introduction to Nearest Neighbor Methods

## A Different Philosophy: Learning by Memory

Everything we have learned so far has followed a pattern:

- **Linear models**: Learn parameters (weights) to define a line or hyperplane
- **Decision trees**: Learn rules by splitting the data into regions

Both approaches build an explicit model during training. Then during prediction, they use that model.

Nearest neighbor methods take a completely different approach:

> Store the training data itself as the model, then predict by looking at what nearby examples say

This is a shift from **learning a structure** to **remembering examples**.

---

## Why This Matters in the Lineage

Linear and tree-based models showed that machines can learn from data. But they require choosing a model structure upfront:

- Linear model: commit to a line
- Tree: commit to hierarchical splits

What if the problem does not fit these shapes?

Nearest neighbor methods say: don't commit to a shape at all. Just remember the training data and let it speak for itself.

This is historically important because:

1. It shows that **lazy learning** (deferring computation to prediction time) is valid
2. It reveals the power of **similarity**: if your example resembles mine, you probably belong to the same class
3. It works with any feature space, not just linearly separable data

---

## The Core Idea: K-Nearest Neighbors (KNN)

The simplest nearest neighbor algorithm is **K-Nearest Neighbors (KNN)**.

The idea is almost comically simple:

1. To predict for a new point, find the K closest points in your training data
2. Look at what those K neighbors predict
3. Use majority vote (for classification) or average (for regression)

Example: Predicting if a student will pass

**Training data**: 
- Student A: 150 hours studied, passed ✓
- Student B: 160 hours studied, passed ✓  
- Student C: 20 hours studied, failed ✗
- Student D: 30 hours studied, failed ✗

**New student**: 140 hours studied (unknown if they'll pass)

With K=3:
- Find 3 closest: A (150 hours), B (160 hours), C (20 hours)
- A and B passed, C failed
- Majority vote: **Pass** (2 out of 3)

That is the entire algorithm.

---

## The Implementation Insight

To find nearest neighbors, we need a **distance metric**. The most common is **Euclidean distance**:

$$d(x, x') = \sqrt{(x_1 - x'_1)^2 + (x_2 - x'_2)^2 + ... + (x_n - x'_n)^2}$$

This says: measure the straight-line distance between two points in feature space.

Other metrics exist:
- **Manhattan distance**: $d = |x_1 - x'_1| + |x_2 - x'_2| + ...$
- **Cosine similarity**: measure angle between vectors
- **Hamming distance**: count differences in categorical features

The choice of metric matters for how the algorithm performs.

---

## Why KNN is Both Powerful and Problematic

### Strengths

1. **No model training needed** - Just store the data
2. **Works with any data shape** - No assumptions about linear separability
3. **Flexible decision boundaries** - Can adapt to complex patterns
4. **Interpretable** - You can point to exactly which examples made the prediction

### Problems

1. **Curse of dimensionality**: In high-dimensional spaces, points become equally distant from each other, making the notion of "nearest" meaningless

2. **Expensive predictions**: Every prediction requires calculating distances to all training points. For a dataset with 1 million examples, predicting on 10,000 new points means 10 billion distance calculations

3. **Sensitive to scale**: If one feature ranges from 0-1 (e.g., proportion of attendance) and another ranges from 0-100 (e.g., test score), the larger-scale feature dominates distance calculations

4. **All features matter equally**: Unlike linear models, you cannot easily tell which features are actually important

5. **Need to choose K**: How many neighbors? Too few (K=1) and you overfit to individual examples. Too many and you lose local information.

---

## From KNN to Refinements

Because of these issues, the nearest neighbor family grew to address specific weaknesses:

- **Weighted KNN**: Give closer neighbors more influence (weight varies by distance)
- **Local regression**: Instead of majority vote, fit a local linear model on neighbors
- **Approximate nearest neighbor**: Use indices to speed up finding neighbors
- **Metric learning**: Learn which features matter most for distance

---

## What Comes Next

The next section explores **local regression**, which takes the nearest neighbor idea and enhances it with local models rather than just voting.

This begins to bridge the gap between the memory-based approach of KNN and the explicit modeling approach of linear and tree models.
