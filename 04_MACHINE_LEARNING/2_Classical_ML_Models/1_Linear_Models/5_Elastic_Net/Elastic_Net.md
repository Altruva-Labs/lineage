# Chapter 4.2.1.5: Elastic Net

## The Best of Both Worlds

So far we have seen two regularization strategies:

- **Ridge**: Shrinks weights toward zero (L2), keeps all features
- **Lasso**: Forces some weights to zero (L1), does feature selection

Each has strengths and weaknesses.

Ridge is stable with correlated features. Lasso is interpretable and sparse.

What if you want **both properties**?

That is where Elastic Net comes in.

---

## The Core Idea

Elastic Net combines L1 and L2 regularization in the same objective:

$$J(w, b) = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \lambda \left[ \alpha ||w||_1 + (1 - \alpha) ||w||_2^2 \right]$$

Where:
- $\lambda$ is the overall regularization strength
- $\alpha$ is the **mixing ratio** between L1 and L2

The ratio parameter controls the balance:

- $\alpha = 0$: Pure Ridge (only L2)
- $\alpha = 0.5$: Equal mix of L1 and L2
- $\alpha = 1$: Pure Lasso (only L1)

---

## Why Both Penalties?

**The problem each solves**:

Ridge handles **multicollinearity** well. When features are correlated, Ridge distributes the weight among them gracefully.

Lasso does **feature selection**. It automatically identifies which features matter.

But Lasso struggles with correlated features. It arbitrarily drops some and keeps others.

**Elastic Net's solution**:

The L2 term encourages related features to have similar weights (they work together).  
The L1 term encourages sparsity (some weights become zero).

Together, they often select **groups of correlated features as a unit** rather than arbitrarily picking one.

---

## Real-World Example: Genomics Data

In genomics, you might have:
- Gene 1, Gene 2, Gene 3: highly correlated (they work together in a pathway)
- Gene 4: moderately correlated with genes 1-3
- ... thousands more genes

**Lasso alone**:
Might select only Gene 1 and zero out Gene 2 and 3 (because they're redundant individually).

Problem: You lose the biological insight that this pathway matters.

**Ridge alone**:
Keeps all genes, using tiny weights for the irrelevant ones.

Problem: Hard to identify which genes really matter.

**Elastic Net**:
Selects all three genes (1, 2, 3) together because the L1 term penalizes them, but L2 encourages them to cooperate. You get feature selection (genes are identified as important) plus stability (correlated genes work together).

---

## Hyperparameters: λ and α

Elastic Net has **two hyperparameters** to tune:

### 1. Regularization Strength ($\lambda$)

Controls how much regularization: higher λ = more shrinkage and feature selection.

### 2. Mixing Ratio ($\alpha$ or l1_ratio)

Controls the balance:

- $\alpha = 0.1$: Mostly Ridge (smooth, stable, keeps most features)
- $\alpha = 0.5$: Balanced (moderate sparsity, handles correlation)
- $\alpha = 0.9$: Mostly Lasso (aggressive feature selection, may struggle with correlation)

To find the best values, use **cross-validation**:

1. Try a grid of (λ, α) combinations
2. Train on training data, evaluate on validation data
3. Choose the combination with best validation performance

---

## Strengths of Elastic Net

- **Combines benefits**: Gets both Ridge's stability AND Lasso's interpretability
- **Handles correlated features gracefully**: Groups related features together
- **Automatic feature selection**: Still zeros out irrelevant features
- **Flexible**: Can be tuned to lean toward Ridge or Lasso
- **Robust**: Works well across many problem types
- **Scalable**: Efficient algorithms exist for large datasets

---

## Limitations of Elastic Net

### 1. Two Hyperparameters to Tune
You must choose both $\lambda$ and $\alpha$. More tuning work than Ridge alone.

### 2. Still Linear
Like all linear models, assumes relationships are linear at heart.

### 3. Not Always Best for Sparse Data
If you truly need aggressive sparsity (narrow down to a few features), pure Lasso might be better.

### 4. Computational Cost
Tuning both hyperparameters requires more cross-validation.

---

## When to Use Each

| Situation | Best Choice |
|-----------|-------------|
| Few features, want to regularize | Ridge (simple, one param) |
| Many features, most irrelevant | Lasso (strong selection) |
| Correlated features, need sparsity | Elastic Net (best balance) |
| Unknown correlations | Elastic Net (safe default) |
| Minimal data, many features | Elastic Net (stable selection) |

---

## Progression of Regularized Linear Models

Think of this as a journey:

**Linear Regression**:  
No regularization. High risk of overfitting.

**Ridge Regression**:  
L2 penalty. Shrinks all weights, keeps all features.

**Lasso Regression**:  
L1 penalty. Zeros out some weights, enables feature selection.

**Elastic Net**:  
L1 + L2 penalty. Combines strengths, balances weaknesses.

Each one solves a practical problem the previous one could not fully address.

---

## Connection to the Lineage

Linear regression learned from data.
Regularization improved on that by preventing overfitting.

Now we have a family of regularized linear models:

- Ridge: stable all-features regularization
- Lasso: aggressive feature selection
- Elastic Net: balanced pragmatism

This shows an important pattern in machine learning:

> Adding the right constraint or penalty can solve real problems

This principle extends far beyond linear models:

- Neural networks use regularization (weight decay, dropout)
- Ensemble methods use regularization (diversity, bagging)
- Bayesian methods use prior distributions (implicit regularization)

---

## What Comes Next

Elastic Net is the final member of the **regularized linear models family**.

The next section steps away from adding constraints to linear models.

Instead, we explore a completely different approach:

**Linear Support Vector Machines**

Instead of adding penalties to the loss function, SVM changes **which points matter** during training.

It focuses on the **points closest to the decision boundary**, not all points equally.

This leads to a different philosophy of learning.