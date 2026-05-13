# Chapter 4.2.3.1: k-Nearest Neighbors (k-NN)

k-Nearest Neighbors (k-NN) is a simple, direct way to make predictions from examples. It does not build a global formula ahead of time. Instead, it remembers the training examples and uses the closest ones to predict for a new input.

**Why this matters in the lineage.** k-NN uses two ideas we already met: a distance measure (how similar two examples are) and the idea that similar inputs often have similar outputs. It shows a local, example-driven style of learning that sits between pure rules and full models.

## 1. Core idea (plain)

For a new point:
- Find the k training points closest to it using a distance metric.
- For classification: pick the most common label among those neighbors.
- For regression: average (or weight) their target values to estimate the output.

Real-world picture: To guess whether you'll like a restaurant, look at your k most similar past restaurants (price, food type, location, rating) and see what you thought of them. If most were good, this new one likely is too.

## 2. The math (clean formulas)

Distance (Euclidean) between two points $x$ and $x'$ in $n$ dimensions:
$$
d(x, x') = \sqrt{\sum_{i=1}^n (x_i - x'_i)^2}
$$

Regression prediction (simple average of k neighbors):
$$
\hat{y} = \frac{1}{k} \sum_{j=1}^k y_{(j)}
$$

Weighted regression (inverse-distance weights):
$$
w_j = \frac{1}{d_j + \epsilon}, \quad
\hat{y} = \frac{\sum_{j=1}^k w_j y_{(j)}}{\sum_{j=1}^k w_j}
$$

Classification (majority vote): pick label $\hat{y}$ that maximizes the neighbor count (or the summed weights for weighted voting).

## 3. How to build k-NN from scratch (step-by-step)

1. Choose a distance function ($L_2$ / Euclidean is common; $L_1$/Manhattan is another).
2. Store the training inputs $X$ and targets $y$ — training is just remembering data.
3. For each query point:
	 - Compute distances to every training point.
	 - Find the k smallest distances (partial sort or heap for speed).
	 - For classification: majority vote among the k labels.
	 - For regression: average or weighted-average the k target values.

Notes:
- Normalize features before computing distances (scale matters: meters vs. dollars).
- Choose $k$ by validation: small $k$ is noisy, large $k$ can be biased.

## 4. Efficiency and improvements (practical)

- Brute force is $O(N)$ distance computations per query. For many queries or large $N$, this is slow.
- Use spatial data structures (KD-tree, ball tree) to speed nearest-neighbor search when dimension is moderate.
- Use approximate nearest neighbors for very large datasets (faster, slightly less exact).
- Feature selection and scaling are crucial. Irrelevant features break distance-based methods.

## 5. Strengths and limits (clear)

- Strengths:
	- Very simple to implement.
	- No explicit training; adapts to complex shapes in data.
	- Works well with enough data and a sensible distance.
- Limits:
	- Slow at prediction time for large datasets.
	- Curse of dimensionality: distances lose meaning with many features.
	- Sensitive to feature scaling and irrelevant features.

## 6. Variants and what comes next

- Weighted k-NN: weight neighbors by inverse distance.
- Local regression / locally weighted regression: fit a small model to the neighborhood to get smoother predictions (see next section on local regression).

## 7. From theory to code

This chapter has a compact, readable implementation you can run and study in the repository: see `code.py` in the parent `Nearest_Neighbor_Methods` folder for a from-scratch KNN, weighted KNN, and a local regression example.

If you want to build your own version, follow the simple steps above: implement a distance function, compute distances, pick the k smallest, and vote or average.

---

Small exercises:
- Try different values of $k$ on a toy dataset and plot how accuracy changes.
- Compare Euclidean vs. Manhattan distance on the same features.

References and historical note: k-NN dates back to early pattern recognition and non-parametric statistics; it is one of the oldest, most direct learning methods and helped shape thinking about local vs. global models in the lineage.