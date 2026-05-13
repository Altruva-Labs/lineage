# Chapter 4.2.2: Introduction to Decision Trees and Tree-Based Models

## Beyond Linear: A New Philosophy

Everything we have learned so far — linear regression, logistic regression, regularized variants — assumes a core assumption:

> The relationship between features and output is roughly linear

But the real world is not linear. Many relationships are:

- **Hierarchical**: Some decisions depend on other decisions
- **Non-linear**: The effect of a feature changes depending on other features  
- **Categorical**: Natural groupings or thresholds

For example: "How do I decide if a student will pass?"

**Linear model logic**:
Combine all student characteristics (attendance, quiz scores, homework) into one weighted sum.

**Tree logic**:
- First, check: is attendance below 50%?
  - If yes: likely to fail (no need to check anything else)
  - If no: check quiz scores
    - If below 40%: likely to fail
    - If above 70%: likely to pass
    - Otherwise: check homework

This branching, hierarchical logic is more intuitive and more powerful for many real problems.

---

## What Are Decision Trees?

A decision tree is a model that makes predictions by asking a **sequence of yes/no questions** about the data.

Simple example:

```
                    Is this email spam?
                           |
                    Is it unsolicited?
                      /          \
                    YES           NO
                    / \           / \
                   /   \         /   \
              SPAM    Is it long?  Not spam
                      /      \
                    YES       NO
                    /          \
                PROBABLY      NOT
                 SPAM         SPAM
```

Each node asks a question about a feature.
Each leaf makes a final prediction.

---

## Why Trees Matter in the Lineage

Linear models showed: machines can learn patterns from data.

But they had limits: they assumed relationships were fundamentally linear.

Trees solve this by **asking different questions at different points in the data space**.

This is a philosophical shift:

- **Linear models**: Find the single best line/hyperplane
- **Trees**: Partition the space into regions, each with its own simple rule

Together, these two model families — linear and tree-based — form the foundation of classical machine learning.

---

## How Trees Learn: The Key Insight

Trees grow by **recursively splitting the data**.

At each step, the algorithm asks: "Which feature should I use to split here, and where should I split it?"

The answer comes from a metric like:

- **Information Gain** (classification): How much does this split reduce uncertainty?
- **Variance Reduction** (regression): How much does this split reduce prediction error?

Example: Is attendance the best split?

**Before split**:
- 30 students pass, 20 fail (impure)

**After splitting on attendance**:
- Below 50%: 5 pass, 18 fail (very impure → bad students)
- Above 50%: 25 pass, 2 fail (very pure → good students)

This split effectively **separates** the classes, so it's a good choice.

The tree recursively repeats this process on each region until:
- All samples in a region have the same label (pure)
- The region is too small to split further
- A depth limit is reached

---

## Key Properties

### 1. Interpretability
Trees are far more interpretable than linear models. You can literally trace the path that led to a prediction:

"This student will fail because: attendance < 50% AND quiz score < 40%"

vs a linear model's weight vector, which is harder to explain.

### 2. Non-Linear
Trees naturally capture non-linear relationships and interactions between features.

### 3. No Feature Scaling Needed
Unlike linear models, trees don't require normalized features. A feature's scale doesn't matter — only the split threshold.

### 4. Handles Mixed Data Types
Trees work with numerical, categorical, and even text features out of the box.

### 5. Fast Prediction
Once trained, prediction is just following the tree (O(depth) time, usually fast).

---

## The Overfitting Problem: Trees Get Too Deep

Trees have a critical weakness: **they easily overfit**.

If you grow a tree until every leaf contains only one type of class, the tree **perfectly memorizes the training data** but **fails on new data**.

This happens because:
- Trees can ask unlimited questions
- Nothing inherently prevents detailed, specific splits
- A tree can capture noise (random variation) as if it were signal

Example:

```
A complete tree on 100 students might eventually split on:
"Is the student's first name's second letter 'a'?"
or
"Did they eat breakfast on the day of test #3?"

These splits fit the training data but mean nothing for new students.
```

This led to family of tree-based solutions:

---

## Three Strategies to Control Overfitting

### 1. Pruning
Grow the tree fully, then cut back branches that don't improve validation performance.

Think of it like sculpture: rough out the full shape, then refine.

### 2. Early Stopping
Stop growing the tree when validation performance stops improving.

Like when learning to write: you practice until you're good enough, then you stop, rather than practicing forever.

### 3. Ensemble Methods
Instead of one perfect tree, build many **slightly different** trees and let them vote.

No single tree overfits because no single tree is trusted completely.

This is the most effective approach, leading to:

---

## The Tree-Based Model Family

This section covers several tree-based approaches:

### 1. **Decision Trees**
Basic tree model with control for overfitting (pruning, depth limits).

### 2. **Random Forests**
Build many trees on random subsets of data and features. Final prediction is the majority vote.

Key insight: Randomness + averaging = lower overfitting

### 3. **Gradient Boosting**
Build trees sequentially, each tree focusing on correcting errors from previous trees.

Key insight: Focus on what you got wrong builds better models than trying to get everything right simultaneously.

### 4. **XGBoost, LightGBM, CatBoost**
Highly optimized implementations of gradient boosting with tweaks for speed and accuracy.

---

## Strengths of Tree-Based Models

- **Interpretable**: Easy to understand and explain
- **Flexible**: Handle non-linear relationships naturally
- **Practical**: Work well on real-world tabular data
- **Robust**: Don't require feature scaling or normalization
- **Mixed data**: Handle numerical, categorical, text features
- **Fast**: Prediction is quick (just follow the tree)
- **Feature importance**: Easy to see which features matter
- **Resistant to data quirks**: Unusual value magnitudes don't break trees

---

## Limitations

- **Memory**: Large trees use significant memory
- **Instability**: Small changes in data can produce very different trees (high variance)
- **Overfitting risk**: Very easy to build trees that memorize training data
- **Bias towards dominant features**: Tend to split on features with many possible values
- **Poor extrapolation**: Very bad at predicting outside the training data range
- **Not Great for Small Data**: Need sufficient data to build reliable split points

---

## Connection to the Lineage

**Classical AI** (Chapter 1): If-then rules, symbolic reasoning  
**Linear Models** (Chapter 4.2.1): Learn weighted combinations  
↓
**Decision Trees** (this section): Learn hierarchical if-then rules

Trees are the bridge between symbolic AI and modern machine learning:

- Like classical AI: use logical conditions (if-then)
- Like ML: learn the structure from data

This fusion is powerful and shows why the lineage matters.

---

## What Comes Next

This section covers the tree-based family:

1. **Decision Tree**: The basic algorithm and how to control overfitting
2. **Random Forest**: Ensemble method using bagging
3. **Gradient Boosted Trees**: Sequential boosting approach
4. **XGBoost, LightGBM, CatBoost**: Production-grade implementations

Each builds on the previous by solving a weakness or improving efficiency.

These methods often outperform a single tree while maintaining the ability to handle complex, tabular data.

## 7. Why They Matter in the Lineage

Decision trees are important because they show another way to learn:

- not by a single global formula
- but by breaking the space into cases

They also preserve some of the readable structure that older AI systems valued.

## 7. What Comes Next

Another classical idea is even simpler:

> to classify a new point, look at nearby examples

That is the basis of nearest-neighbor methods.
