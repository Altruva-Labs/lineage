# Chapter 4.2.6.2: Kernel Ridge Regression

## The Problem: Linear Ridge Regression Isn't Enough

Ridge regression is powerful, but it is still linear. It fits straight lines (or planes in high dimensions).

Many real-world relationships are curved:
- Growth rates that accelerate or decelerate
- Physical phenomena that follow polynomial patterns
- Market trends with seasonal variations

One approach: add polynomial features (x², x³, etc.) and use linear regression on those.

But this approach has problems:
- You must choose which polynomial degree (quadratic? cubic? quartic?)
- Too many features → overfitting
- Interpretability suffers

**Kernel ridge regression** solves this elegantly by using the **kernel trick**.

> Apply ridge regression in a high-dimensional space WITHOUT explicitly creating those features.

---

## Recap: The Kernel Trick (from Chapter 4.2.6)

Kernel methods use a mathematical trick to work in high dimensions cheaply.

Instead of computing:
$$\phi(x) \cdot \phi(x')$$

(dot product in transformed space - expensive)

They compute:
$$K(x, x') = \phi(x) \cdot \phi(x')$$

(kernel function - cheap)

The kernel function directly computes the result without ever building the transformed features explicitly.

---

## How Kernel Ridge Regression Works

### Traditional Ridge Regression Recap

Find weights $\alpha$ that minimize:

$$J(\alpha) = \frac{1}{n} ||y - X\alpha||^2 + \lambda ||\alpha||^2$$

Solution (see Chapter 4.2.1.3):

$$\alpha = (X^T X + \lambda I)^{-1} X^T y$$

### Kernel Ridge Regression: The Modification

We do the exact same thing, but replace the design matrix $X$ with a **kernel matrix** $K$.

The kernel matrix has shape $n \times n$ (one row per training sample, one column per training sample):

$$K_{ij} = K(x_i, x_j)$$

The solution becomes:

$$\alpha = (K + \lambda I)^{-1} y$$

Yes, that is it! Instead of $(X^T X + \lambda I)^{-1}$, we use $(K + \lambda I)^{-1}$.

The $\alpha$ we learn are coefficients for each training point (not weights for features).

---

## Prediction on New Data

With standard linear regression:
$$\hat{y}_{new} = w^T x_{new}$$

With kernel ridge regression:
$$\hat{y}_{new} = \sum_{i=1}^{n} \alpha_i K(x_i, x_{new})$$

Use the learned $\alpha$ coefficients and kernel function to predict.

---

## Common Kernel Functions

### 1. Linear Kernel
$$K(x, x') = x \cdot x'$$

No transformation. Kernel ridge regression becomes regular ridge regression.

### 2. Polynomial Kernel
$$K(x, x') = (x \cdot x' + c)^d$$

Implicitly works in polynomial feature space.
- $d = 2$: quadratic features
- $d = 3$: cubic features
- Higher $d$ = more flexibility (but slower, easier to overfit)

### 3. Radial Basis Function (RBF) Kernel
$$K(x, x') = \exp(-\gamma ||x - x'||^2)$$

Works in infinite-dimensional space!
- Measures similarity as distance
- $\gamma$ (gamma) controls how wide the influence is
- Small $\gamma$ = each point influences far neighbors (smooth)
- Large $\gamma$ = points only influence nearby training samples (wiggly)

### 4. Sigmoid Kernel
$$K(x, x') = \tanh(\kappa (x \cdot x') + c)$$

Less common, but inspired by neural networks.

---

## Real-World Example: Stock Price Prediction

Predict next month's stock price from:
- Previous prices
- Trading volume
- Market indicators

**With linear ridge regression**: Predicts a straight line (bad fit).

**With polynomial kernel** (degree 3):
- Implicitly creates cubic features
- Captures accelerating/decelerating trends
- Much better fit

**With RBF kernel**:
- Very flexible, matches many shapes
- Risk: overfitting if $\gamma$ too large
- Needs validation to tune $\gamma$

---

## Key Parameters

### Lambda (Regularization Strength)
- Higher $\lambda$ = stronger penalty on $\alpha$ coefficients = smoother predictions
- Lower $\lambda$ = weaker penalty = fits training data tighter
- Too low: overfitting; too high: underfitting

Choose via cross-validation (Chapter 4.1.4)

### Kernel Choice and Parameters
- **Polynomial**: Degree $d$ (typically 2-4)
- **RBF**: Gamma $\gamma$ (smaller = smoother, larger = wiggly)

No universally best choice. Try different options and validate.

---

## Strengths and Weaknesses

### Strengths
- **Nonlinear without explicit features**: Kernel trick handles complexity
- **Regularized**: Ridge penalty prevents overfitting
- **Solid theory**: Well-understood algorithm with mathematical guarantees
- **One solution**: Closed-form solution, no iterative optimization

### Weaknesses
- **Quadratic memory**: Kernel matrix is $n \times n$, requires O(n²) memory
- **Cubic time**: Matrix inversion is O(n³)
- **Slow on large datasets**: 10,000+ samples becomes slow
- **Need to tune kernel and hyperparameters**: No free lunch
- **Hard to interpret**: What did the model learn? Harder to explain than linear

---

## Kernel Ridge Regression vs. Other Methods

| Method | Linear | Nonlinear | Interpretable | Speed | Memory |
|--------|--------|-----------|---------------|-------|--------|
| Linear Ridge | Yes | No | High | Fast | Low |
| Polynomial Regression | Yes | No | High | Fast | Low |
| Kernel Ridge | No | Yes | Low | Medium | Medium |
| SVM | Flexible | Yes | Low | Medium | Medium |
| Neural Networks | No | Yes | Very Low | Slow (training) | High |

---

## When to Use Kernel Ridge Regression

- **Regression with nonlinear relationships**: When your data has curves, not lines
- **Medium-sized datasets**: 100 to 10,000 samples (larger → too slow)
- **When you care about uncertainty**: Ridge regularization is principled
- **When speed isn't critical**: Closed-form solution is fast for medium data
- **Benchmark/baseline**: Quick way to get a nonlinear fit

---

## What Comes Next

Kernel ridge regression achieves nonlinearity via the kernel trick applied to regression.

**Kernel methods** also apply to classification: **Support Vector Machines (SVMs)** use a similar trick with a different objective function (Chapter 4.2.6.1).

But both have scalability limitations for very large datasets.

**Neural networks** (Chapter 5) avoid the quadratic memory cost by learning features iteratively, making them scalable to millions of samples.