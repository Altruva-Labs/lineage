# Chapter 4.2.2.1: Decision Tree - The Basic Algorithm

## The Core Algorithm

A decision tree grows by recursively asking: "Which feature should I split on, and where?"

The answer depends on a **splitting criterion**: a metric that measures how good a split is.

---

## Splitting Criteria

### For Classification: Gini Impurity

**Gini impurity** measures how "mixed" a region is.

A region with all one class has Gini = 0 (pure).  
A region with equal mix of classes has Gini = 0.5 (most impure).

Formula:
$$\text{Gini} = 1 - \sum_{i} p_i^2$$

Where $p_i$ is the proportion of class $i$.

Example:
- Region with 100% class A: Gini = 1 - (1.0)² = 0 (pure!)
- Region with 50% class A, 50% class B: Gini = 1 - (0.5² + 0.5²) = 0.5 (impure)
- Region with 33% each of 3 classes: Gini = 1 - (0.33² + 0.33² + 0.33²) = 0.67 (very impure)

A good split **reduces Gini**.

Information gain is:

$$\text{IG} = \text{Gini}_{parent} - \sum_{child} \frac{n_{child}}{n_{parent}} \cdot \text{Gini}_{child}$$

Choose the split that maximizes information gain.

### For Regression: Variance Reduction

In regression, instead of purity, we measure prediction error.

A good split **reduces the variance** of predictions in each child region.

---

## The Greedy Splitting Algorithm

1. **Start** with all training data at the root
2. **For each feature**:
   - **For each possible split value**:
     - Calculate the information gain or variance reduction
     - Track the best split
3. **Execute the best split**: Divide data into two regions
4. **Recursively repeat** steps 1-3 on each region until:
   - Region is pure (all one class)
   - Region has too few samples
   - Tree has reached max depth
   - Information gain is below threshold

This is **greedy**: we make locally optimal choices at each step, without re-evaluating earlier decisions.

---

## Real-World Example: Classifying Iris Flowers

Suppose we want to classify flowers as "Setosa", "Versicolor", or "Virginica" using:
- Sepal length
- Sepal width

**Step 1**: Root node has 150 flowers (50 of each class)
- Gini = 1 - (0.33² + 0.33² + 0.33²) ≈ 0.67

Try all splits:
- Sepal length > 5.5?
- Sepal width > 3.0?
- ... many others

The algorithm finds: **"Sepal length > 5.5?"** gives the best information gain.

Split result:
- **Left** (≤ 5.5): Mostly Setosa (48 Setosa, 5 others) → Gini ≈ 0.13
- **Right** (> 5.5): Mixed (2 Setosa, 95 others) → Gini ≈ 0.95

Information gain = 0.67 - (47/150 × 0.13 + 103/150 × 0.95) ≈ 0.25

**Step 2**: On the left region (nearly all Setosa):
- Nearly pure, so create leaf predicting "Setosa"

**Step 3**: On the right region (mixed):
- Try again: "Sepal width > 3.2?"
- Left: Mostly Versicolor  
- Right: Mostly Virginica

Continue until regions are pure or rules are satisfied.

**Final tree**:
```
          Sepal length > 5.5?
           /          \
        YES           NO
       /  \           / \
  Pure   Sepal width  Setosa
 Setosa  > 3.2?
         /     \
       YES      NO
      /  \      / \
Versi. Virginica
```

---

## Controlling Overfitting

Unchecked, trees grow until they memorize training data.

Three main controls:

### 1. **Max Depth**
Limit tree height. Usually the most important control.

Example: max_depth=3 means at most 3 levels of questions.

Deeper = more specific = more overfitting risk.

### 2. **Min Samples Split**
Don't split a region with fewer than N samples.

If a region has 5 samples, creating a split is probably overfitting.

Example: min_samples_split=10 means only split regions with 10+ samples.

### 3. **Min Samples Per Leaf**
Require at least N samples in each leaf (final decision region).

Prevents creating tiny regions that memorize individual examples.

Example: min_samples_leaf=5 means each leaf must contain at least 5 samples.

---

## Decision Tree Strengths

- **Interpretable**: You can trace the path to any prediction
- **Fast**: O(depth) prediction time, very quick once trained
- **Flexible**: Capture non-linear, hierarchical relationships
- **No preprocessing**: Don't need feature scaling
- **Mixed data types**: Handle numerical and categorical
- **Feature importance**: Identify which splits matter most
- **Explainable**: Can show decision rules to non-technical users

---

## Decision Tree Limitations

### 1. Unstable (High Variance)
Small changes in training data → completely different tree structure.

Example:
- Remove one row from the iris data
- The tree might split differently at every node

This instability is solved by ensemble methods (Random Forest).

### 2. Greedy Algorithm
The greedy approach misses globally optimal trees.

At each step, we make the locally best choice, but this might prevent better choices later.

More sophisticated tree-growing algorithms exist but are less common.

### 3. Biased Towards High-Cardinality Features
If a feature has many possible values, it's more likely to look good for splitting.

Example: "Student ID" has 1000 possible values, so it creates thousands of potential splits. By random chance, some will look good for the specific training data.

### 4. Extrapolation Is Poor
Trees can't extrapolate beyond the training data range.

Example: A tree trained on temperatures 0-100°F can't reliably predict 200°F (outside its experience).

### 5. Requires Careful Tuning
The hyperparameters (max_depth, min_samples_split, etc.) significantly affect performance.

Finding the best values requires cross-validation.

---

## Decision Trees vs Linear Models

| Aspect           | Linear Model              | Decision Tree                 |
|------------------|---------------------------|-------------------------------|
| Relationship     | Assumes linear            | Captures curved, hierarchical |
| Interpretability | Weights are meanings      | Paths are meanings            |
| Feature scaling  | Needed                    | Not needed                    |
| Mixed data       | Needs encoding            | Natural handling              |
| Overfitting      | Risk with high dimensions | Risk with deep trees          |
| Speed            | Very fast                 | Fast                          |
| Extrapolation    | Works beyond range        | Fails beyond range            |
| Human intuition  | Less aligned              | Highly aligned                |

---

## Tree-Based Ensemble Methods

A single decision tree is unstable. But **many trees together** are powerful.

### Random Forest
Build N trees on random subsets of data and features.  
Prediction = majority vote (classification) or average (regression).

Why it works: Randomness + averaging reduces overfitting.

### Gradient Boosting
Build trees sequentially.  
Each tree learns to correct errors from all previous trees.

Why it works: Focusing on mistakes improves faster than averaging random models.

Both approaches take the basic decision tree algorithm and make it:
- More accurate
- More robust  
- Less prone to overfitting

---

## Connection to the Lineage

Linear models learned weighted combinations: a single global rule.

Decision trees learn local rules: different rules in different parts of the feature space.

This is a fundamental shift:

- **Linear**: One equation for all inputs
- **Tree**: Different rules (splits) at different points

Trees show that even without neural networks or complex math, you can build models that capture rich, non-linear patterns.

This made tree-based methods extremely popular in practice, especially on **tabular data** (spreadsheets, databases).

---

## Why Impurity Metrics Matter

The choice of splitting criterion (Gini vs Information Gain vs others) affects:

- Which splits are selected
- Tree depth and shape
- Generalization performance

Different criteria are mathematically equivalent for some purposes, but lead to different tree shapes in practice.

Research shows that for most datasets, the choice of criterion matters less than controlling overfitting depth.

---

## What Comes Next

A single decision tree is useful but unstable.

The next sections introduce the **tree ensemble methods**:

1. **Random Forests**: Stability through randomness and voting
2. **Gradient Boosting**: Stability through sequential correction  
3. **XGBoost/LightGBM/CatBoost**: Production implementations with optimizations

These models often outperform individual trees while being more robust.