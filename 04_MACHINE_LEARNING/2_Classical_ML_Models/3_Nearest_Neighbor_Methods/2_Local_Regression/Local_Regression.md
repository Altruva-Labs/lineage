# Chapter 4.2.3.2: Local Regression (LOESS)

## The Problem With Global Models

Linear regression fits a single straight line through all your data.

But what if your data doesn't follow one straight line? What if different parts of the data have different patterns?

For example, imagine a coffee shop tracking how temperature affects sales:
- In summer (60-80°F): higher temps increase cold drink sales slightly
- In winter (20-40°F): higher temps decrease hot drink sales

One global line cannot capture both patterns well.

**Local regression** solves this by asking: instead of fitting one line to all data, what if we fit multiple simple lines - one for each region?

---

## The Core Idea

Local regression (LOESS = LOcal Estimated Scatterplot Smoothing) uses the principle we learned from k-NN:

> similar inputs often have similar patterns

Instead of just averaging the k nearest neighbors, we fit a simple model (like linear regression) **locally** to those neighbors.

The prediction at a new point comes from the local model around that point, not a global model.

---

## How It Works: Step by Step

Suppose you want to predict the output at a new point $x_{new}$.

**Step 1: Find Nearby Points**

Identify the k nearest training points to $x_{new}$ using distance (usually Euclidean).

**Step 2: Weight by Distance**

Not all neighbors have equal influence. Closer points matter more.

Use a **weight function** that decreases with distance. A common choice is:

$$w_i = \left(1 - \left(\frac{d_i}{d_{max}}\right)^3\right)^3$$

Where:
- $d_i$ is the distance from $x_{new}$ to neighbor $i$
- $d_{max}$ is the distance to the k-th neighbor
- This gives nearby points high weight and distant points low weight

**Step 3: Fit a Local Model**

Fit a simple model (usually linear regression) to the k neighbors, using the distance weights.

This is a **weighted least squares** problem:

$$\min_{w,b} \sum_{i=1}^{k} w_i (y_i - (wx_i + b))^2$$

Minimize the weighted squared errors, not all errors equally.

**Step 4: Make a Prediction**

Use the local fitted model to predict at $x_{new}$:

$$\hat{y}_{new} = w \cdot x_{new} + b$$

---

## Real-World Example: Temperature vs. Coffee Sales

Imagine historical data:

| Temperature (°F) | Daily Sales ($) |
|---------|----------|
| 25      | 800      |
| 28      | 820      |
| 32      | 850      |
| 45      | 900      |
| 55      | 950      |
| 65      | 980      |
| 72      | 1000     |
| 75      | 990      |
| 80      | 960      |

A global linear regression would fit one line through all points. But local regression works differently.

**To predict at 35°F:**
1. Find k=3 nearest neighbors: (25, 800), (28, 820), (32, 850)
2. Weight them by distance (closest gets highest weight)
3. Fit a local line to those three points with distance weights
4. Use that local line to predict

**To predict at 70°F:**
1. Find 3 nearest: (65, 980), (72, 1000), (75, 990)
2. Weight by distance
3. Fit a local line
4. Use it for prediction

Notice: the local line fitted near 35°F may have a different slope than the local line near 70°F. This flexibility is the power of local regression.

---

## Why Local Regression Works

### 1. Captures Non-Linear Patterns

When global linear regression fails because observations or patterns are complicated, local regression adapts by fitting different simple lines to different regions.

### 2. Smooth Predictions

By using weighted neighbors and fitting locally, predictions change smoothly rather than jumping abruptly.

### 3. Intuitive

The idea builds on nearest neighbors (simple concept) but adds fitting (more flexible than just averaging).

### 4. Flexible

Works well for regression when relationships are smooth but non-linear.

---

## Strengths

- **Flexibility**: Captures non-linear patterns without assuming a global form
- **Smoothness**: Predictions are smooth curves, not jagged
- **Simplicity**: Uses only local, simple models
- **Interpretability**: Each local region has a clear fitted model
- **No strong assumptions**: Does not assume a specific global formula

---

## Limitations

### 1. Computationally More Expensive

For each prediction, we must:
- Find k nearest neighbors
- Fit a local model
- Make a prediction

This is slower than evaluating a single global formula.

### 2. Requires Tuning

You must choose:
- $k$: How many neighbors to use?
- The weight function: Which weighting scheme?
- Whether to use linear or polynomial fits locally

### 3. Less Interpretable Than Global Models

With linear regression, you have one set of weights explaining the whole relationship.
With local regression, you have many local models.

### 4. Struggles in High Dimensions

When features are numerous, distance becomes less meaningful (curse of dimensionality).
Finding "nearby" points becomes harder.

### 5. Extrapolation

Outside the range of training data, local regression cannot extrapolate well.
There are no neighbors beyond the boundary.

---

## Connection to the Lineage

**Chapter 4.2.1.1** (Linear Regression) showed us how to fit a single line to minimize error.

**Chapter 4.2.3.1** (k-Nearest Neighbors) showed us how to use local similarity for predictions.

**Local Regression** merges these ideas:
- Use local neighborhoods (like k-NN)
- Fit a simple model in each neighborhood (like linear regression)

It shows that not all learning happens with a single global model.

Some learning happens locally - fitting different simple models to different regions of the data.

This prepares us for the next big idea: **clustering** and **dimensionality reduction**.

If we can divide data into local regions, we can:
- Group similar examples (clustering)
- Find lower-dimensional patterns (dimensionality reduction)

---

## What Comes Next

Local regression is more flexible than linear regression but also more complex.

When data has clear groups or clusters, we do not need to fit regression models at all.

Instead, we use **clustering** methods to discover those groups without labeled examples.

This is the bridge to unsupervised learning.