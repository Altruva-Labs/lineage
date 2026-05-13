# Chapter 4.2.1.6: Linear Support Vector Machines (SVM)

## A Different Philosophy of Learning

So far, every model we have seen treats all training data points equally:

- Linear regression: fit a line to minimize average error across all points
- Logistic regression: match probabilities for all points
- Ridge/Lasso: regularize all weights equally

But what if some data points are more important than others?

**Support Vector Machines** (SVMs) ask a different question:

> What if we focus our effort on the hardest points to classify—the ones closest to the decision boundary?

This changes everything about how the model learns.

---

## The Problem: Where Does The Boundary Go?

Imagine two groups of points in 2D space: red points and blue points.

You need to draw a line that separates them.

Many possible lines work:

```
Line A:          Line B:          Line C:
    B|              B|              B|
    B|            B B|            B B|
 __B|__R        __|__R        __|__R
 R R R|       R RR |      R RR |
```

All three separate the classes correctly on training data.

But which one will generalize best to new data?

**Intuition**: The line that is **furthest from all points** is safest. It has the most "breathing room."

If new points are slightly noisy or shifted, the safest line is less likely to misclassify them.

That is the core idea of SVM: maximize the **margin** (the distance from the boundary to the nearest points).

---

## The Margin

The **margin** is the distance from the decision boundary to the nearest data points.

More precisely:
- Find the closest points on each side of the boundary
- Measure the distance between these points
- Maximize this distance

Data points on the margin are called **support vectors** (hence the name).

Only these points matter for the decision boundary. Points far from the boundary contribute nothing.

This is profoundly different from linear regression, which treats all points equally.

---

## Mathematical Formulation

For a linear binary classification problem, the decision boundary is a hyperplane:

$$w \cdot x + b = 0$$

For each point, we want:

- If $y_i = +1$ (positive class): $w \cdot x_i + b \geq +1$
- If $y_i = -1$ (negative class): $w \cdot x_i + b \leq -1$

The margin is proportional to $\frac{1}{||w||}$. To maximize the margin, we minimize $||w||$.

So the optimization problem is:

$$\text{minimize} \quad ||w||^2$$

$$\text{subject to} \quad y_i(w \cdot x_i + b) \geq 1 \quad \text{for all } i$$

This is a **constrained optimization** problem.

---

## The Hinge Loss

In practice, not all points can be separated perfectly (this is called **soft margin** SVM).

We allow some misclassifications, but penalize them. The loss function becomes:

$$J(w, b) = \frac{1}{n} \sum_{i=1}^{n} \text{hinge\_loss}(y_i, \hat{y}_i) + \lambda ||w||^2$$

The **hinge loss** is:

$$\text{hinge\_loss} = \max(0, 1 - y_i \hat{y}_i)$$

This says:
- If the classification is correct AND confident ($y_i \hat{y}_i > 1$): no loss
- If the classification is wrong or uncertain: loss proportional to how wrong you are

The hinge loss is clever: it only penalizes misclassifications or boundary points. Points far from the boundary contribute zero loss.

Compare this to logistic regression, which penalizes all points based on their margin.

---

## Real-World Example: Detecting Fraud

Suppose you want to flag suspicious credit card transactions.

You have historical data:
- Fraud: unusual location, time, amount
- Legitimate: common patterns

A transaction is either fraud (class +1) or not (class -1).

**SVM approach**:

1. Train on historical transactions
2. SVM finds the decision boundary that maximizes margin
3. **Only the suspicious legitimate transactions and the least-obvious fraud cases matter** (the support vectors)
4. Regular transactions far from the boundary do not influence the decision

Benefits:
- Focuses on the hard decisions
- Robust to noise in clear-cut cases
- Efficient (only support vectors matter)

vs Logistic Regression:
- Every transaction influences the boundary
- Equal attention to everything
- More sensitive to noise overall

---

## Key Properties of Linear SVM

### 1. Only Support Vectors Matter

The final model depends only on the points near the boundary:

$$\hat{y} = \text{sign}(w \cdot x + b)$$

Where $w$ is determined by only the support vectors.

This means:
- Changes to distant points do not affect the model
- Efficient storage: only support vectors are stored
- Fast computation for sparse datasets

### 2. Maximizes Margin

SVM explicitly optimizes for the separation distance, which improves generalization. This is theoretically well-motivated: larger margin = lower capacity = better generalization.

### 3. Handles Linear Separability Well

When classes are linearly separable (or nearly), SVM works very well.

### 4. High-Dimensional Problems

SVM is especially effective in high dimensions (many features). Margin-based learning works better than minimum-error learning in high-dimensional spaces.

---

## The C Parameter

Linear SVM has one key hyperparameter: **C** (not to be confused with λ in regularization, though they are related).

$C$ controls the tradeoff between:
- **Margin size** (maximizing distance from boundary)
- **Misclassification tolerance** (allowing some errors)

$$J(w, b) = C \cdot \sum_{i=1}^{n} \text{hinge\_loss} + ||w||^2$$

- **C small** (e.g., 0.01): Larger margin, more tolerance for errors, simpler decision boundary
- **C large** (e.g., 100): Smaller margin, stricter on errors, more complex boundary

like λ in Ridge/Lasso, C must be tuned via cross-validation.

---

## Strengths of Linear SVM

- **Margin-based reasoning**: Theoretically motivated, explicit generalization goal
- **Efficient**: Only support vectors affect the model
- **Works in high dimensions**: Doesn't suffer as much from curse of dimensionality
- **Interpretable** (somewhat): Support vectors show which points matter
- **Robust**: Ignores distant points, robust to outliers
- **Proven theory**: Extensive theoretical foundation for generalization

---

## Limitations of Linear SVM

### 1. Assumes Linear Separability
If classes are interleaved or curved, linear SVM struggles.

### 2. Requires Balanced Data
If one class is much rarer, SVM may default to always predicting the common class (even with carefully chosen C).

### 3. Slow With Large Datasets
While only support vectors matter, finding them requires solving a quadratic programming problem. This is slow for very large n.

(Stochastic methods now exist, but vanilla SVM can be slow.)

### 4. Sensitive to Feature Scaling
SVM distances depend on feature magnitudes. Unscaled features give unreliable results.

All values should be normalized before training.

### 5. Focus on Boundary Points Can Be Bad
For imbalanced data or with outliers, focusing only on boundary points might miss important patterns in the majority class.

---

## Linear SVM vs Logistic Regression

| Aspect | Logistic Regression | Linear SVM |
|--------|---------------------|-----------|
| Loss function | Logistic loss | Hinge loss |
| Focus | All points equally | Points near boundary |
| Margin | No explicit margin | Maximizes margin |
| Probabilistic | Yes (outputs probabilities) | No (outputs only labels) |
| Interpretation | Confidence scores | Decision boundary + margin |
| Noise robustness | Less robust | More robust |
| Computation | Faster | Slower |
| High dimensions | Struggles more | Handles better |

---

## The SVM Philosophy in the Lineage

All the linear models we have seen (regression, logistic, ridge, lasso) use the same basic learning principle:

> Find parameters that minimize prediction error

SVM introduces a different principle:

> Find parameters that maximize margin (maximize safety, not just minimize error)

This shift appears throughout machine learning:

- **Ensemble methods**: Diversity (different from average) reduces error
- **Boosting**: Focus on hard examples
- **Neural networks**: Implicit regularization from network structure

SVM shows that how you weight the learning examples changes everything.

---

## Connection to Kernels

For now, we have only seen **linear SVM** (linear decision boundary).

But SVM has a powerful extension: **kernel SVM** (Chapter 4.2.6).

Kernels make SVM work in high-dimensional spaces implicitly, allowing non-linear decision boundaries while still using the margin-based principle.

This is one of SVM's greatest strengths.

---

## What Comes Next

We have finished the **regularized linear models** family:

- Linear Regression: baseline learner
- Logistic Regression: for classification
- Ridge: stabilize with L2
- Lasso: select features with L1
- Elastic Net: balance both
- Linear SVM: margin-based

These models all assume linear relationships. The next family steps away from linearity.

**Decision Trees** use a completely different approach: recursive feature-based splitting instead of weighted combinations.

This opens the door to capturing non-linear, complex relationships.