# Chapter 4.2.1.4: Lasso Regression

## From Shrinkage to Selection

Ridge regression solved overfitting by shrinking large weights.

But it kept all weights in the model.

If you have 1000 features but only 100 matter, Ridge still uses all 1000 (most with tiny weights).

What if you want the model to **actually discard irrelevant features**?

That is the problem Lasso solves.

---

## The Problem: Too Many Features

Imagine predicting stock prices using:

- Volume traded
- Previous day return
- Day of week
- Time of day

Plus 500 more features like:

- CEO's favorite color
- Random noise
- Features derived from features
- Interactions you may not need

Which features actually matter?

**Lasso** says: "Let me learn automatically which ones to keep and which ones to ignore."

It does this by forcing **some weights to exactly zero**.

---

## L1 vs L2 Regularization: The Key Difference

Recall Ridge regression used **L2 regularization**:

$$J(w, b) = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \lambda ||w||_2^2$$

Where: $||w||_2^2 = w_1^2 + w_2^2 + ... + w_n^2$

Lasso uses **L1 regularization**:

$$J(w, b) = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \lambda ||w||_1$$

Where: $||w||_1 = |w_1| + |w_2| + ... + |w_n|$

The **L1 norm** is the sum of absolute values, not squares.

This small change has a huge effect: L1 regularization pushes weights toward **exactly zero**.

---

## Why L1 Leads to Sparsity (Feature Selection)

This is a geometric fact about norms. Here is an intuitive explanation:

Imagine you have two features and want to minimize error while keeping weights small.

Graph the constraint regions:

**L2 (Ridge)**: Weights must lie inside a **circle** (smooth constraint)

**L1 (Lasso)**: Weights must lie inside a **diamond/square** (sharp corners)

When the optimization algorithm finds the best point (closest to the ideal weights), it often hits a **corner** of the diamond.

At a corner, one weight is exactly zero.

The sharper geometry of L1 encourages hitting these corners.

---

## Visual Intuition

Consider two features. The constraint region looks like:

```
Ridge (L2):                  Lasso (L1):

    w2                           w2
    |                            |
    |___                          |____
   /   \                         /|   |\
  |     |                        | |   | |
  |     |      (circle)          | |   | |  (diamond)
  |_____|                        | |   | |
        w1                       |_|___|_|
                                     w1
```

The error surface creates peaks and valleys. The solution (best point on the constraint) often aligns with a **corner** for Lasso (axis-aligned), forcing one weight to zero.

For Ridge, the smooth curve makes hitting a corner unlikely.

---

## Real-World Example: Email Feature Selection

Suppose you collect 50 features for spam detection:

- Contains "FREE"
- Contains numbers
- Sender unknown
- All caps message
- Multiple exclamation marks
- Long email address
- ... 44 more

Unregularized linear regression: uses all 50 features  
Ridge regression: uses all 50, but some have tiny weights  
**Lasso regression**: might keep only 8 features, setting 42 weights to exactly zero

Example result after training Lasso:

```
Feature                    Weight
Contains "FREE"            +0.85
All caps                   +0.62
Multiple exclamation marks +0.51
Sender unknown             +0.44
... (8 features kept) ...
Random feature #23         0       (zeroed out)
CEO favorite color         0       (zeroed out)
... (42 features zeroed out) ...
```

Now your model is:

**Spam probability = 0.85 * contains_FREE + 0.62 * all_caps + ... (only 8 terms)**

This is **sparse**: most features contribute nothing.

---

## How Lasso Learns

The gradient for L1 regularization includes the absolute value:

$$\frac{\partial J}{\partial w} = \frac{2}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i) x_i + \lambda \cdot \text{sign}(w)$$

The issue: the absolute value function is not smooth at zero. Its derivative is discontinuous there.

**Standard gradient descent doesn't work directly.**

Instead, specialized algorithms are used:

- **Proximal gradient descent**: Handle the non-smooth term specially
- **Coordinate descent**: Update one weight at a time
- **LARS** (Least Angle Regression Shrinkage): Efficiently compute solutions

All these algorithms achieve the same goal: find weights that balance fit and sparsity.

---

## Strengths of Lasso

- **Automatic feature selection**: Identifies which features truly matter
- **Interpretability**: The sparse model is easier to explain
- **Reduced overfitting**: Fewer features usually means less overfitting
- **Computational efficiency**: Using fewer features speeds up prediction
- **Domain insight**: The selected features reveal what the data really depends on

---

## Limitations of Lasso

### 1. Unstable With Correlated Features
If two features are highly correlated, Lasso often selects only one and zeros out the other.

Example:
- Feature A: "Contains $"
- Feature B: "Mentions money"

These are correlated. Lasso might drop B entirely and keep only A.

This is **arbitrary**—either could be useful, but Lasso picks one.

### 2. Can Be Inconsistent
With noisy data, different samples might select different subsets of features.

### 3. Requires Tuning λ
Like Ridge, the regularization strength $\lambda$ must be tuned via cross-validation.

### 4. Computationally Harder
Lasso requires specialized algorithms (proximal gradient descent, coordinate descent). It is slower than Ridge or regular linear regression.

---

## The Bias-Variance Tradeoff

Ridge and Lasso represent different choices in the **bias-variance tradeoff**:

**High λ (strong regularization)**:
- Higher bias (the model underfits)
- Lower variance (stable predictions)
- Risk of missing real patterns

**Low λ (weak regularization)**:
- Lower bias (fits the data closely)
- Higher variance (predictions are jumpy)
- Risk of overfitting

Lasso's feature selection is another form of choosing this tradeoff:

- Selected features represent high confidence in what matters
- Zeroed features represent a bet that they do not matter

---

## When to Use Lasso vs Ridge

**Use Lasso when**:
- You want to know which features matter most
- You have many features and suspect most are irrelevant
- You want a sparse, interpretable model
- Computational efficiency matters

**Use Ridge when**:
- You believe many features are useful (just need regularization)
- Features are correlated (Lasso would arbitrarily drop some)
- Interpretable feature selection is not critical
- You want a stable, simple solution

---

## Connection to the Lineage

Linear regression: learn weights \
Ridge regression: constrain weights to be small (L2) \
**Lasso regression: force some weights to be zero (L1)**

This progression shows how we solve layer-by-layer problems:

1. First, we learn patterns from data (linear regression)
2. Then, we avoid overfitting by keeping weights small (Ridge)
3. Then, we go further by asking: which features are truly needed? (Lasso)

Feature selection is not optional—it is **central to good machine learning**.

---

## What Comes Next

Lasso and Ridge are different regularization strategies.

The next section introduces:

- **Elastic Net**: Combines L1 and L2 (best of both worlds)
- **Linear SVM**: Another linear model with a different loss function