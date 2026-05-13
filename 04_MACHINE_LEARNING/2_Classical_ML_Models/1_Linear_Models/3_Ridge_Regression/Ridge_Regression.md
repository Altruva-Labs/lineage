# Chapter 4.2.1.3: Ridge Regression

## When Linear Regression Breaks: The Overfitting Problem

We have learned two linear models so far:

- **Linear Regression**: Predicts continuous values
- **Logistic Regression**: Predicts probabilities for classification

Both work well when the relationship is truly linear or nearly linear.

But what happens when you have data with **many features**? Or **highly correlated features**? Or **more parameters than training examples**?

In those cases, unregularized linear regression often overfits: it learns the noise in the training data rather than the true pattern, and fails on new data.

Ridge regression introduces our first **regularization** strategy to solve this.

---

## The Overfitting Problem: A Real Example

Imagine predicting house prices with many features:

- Square footage
- Number of bedrooms
- Age of house
- Proximity to subway
- School district rating
- Number of nearby restaurants
- Days since last inspection
- Whether the house number is even or odd
- Color of the front door
- ... and 100 more features

If you have only 50 houses in your training data, vanilla linear regression might:

1. Use the door color to predict price (it's useless, but fits the training data)
2. Use the exact age in days (overfitting to random variations)
3. Find exact weights that perfectly fit training data (100% accuracy!)

But on new houses?

4. The model fails miserably because it learned noise, not real patterns

This is **overfitting**: perfect fit to training data, poor performance on test data.

---

## Regularization: The Core Idea

Regularization adds a penalty for having large weights in the loss function.

The intuition: 

> Simple models with small weights generalize better than complex models with large weights

Ridge regression uses **L2 regularization** (also called Tikhonov regularization).

The new objective becomes:

$$J(w, b) = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \lambda ||w||^2$$

Where:
- First term: prediction error (same as linear regression)
- Second term: penalty for large weights
- $\lambda$ : regularization strength (hyperparameter you choose)

The second term is the **L2 norm**: $||w||^2 = w_1^2 + w_2^2 + ... + w_n^2$

This penalizes weights for being large.

---

## How It Works: The Tradeoff

The loss function now has two competing goals:

1. **Fit the data well** (minimize prediction error)
2. **Keep weights small** (minimize the regularization term)

The hyperparameter $\lambda$ controls the tradeoff:

- **$\lambda = 0$**: No regularization (vanilla linear regression)
- **$\lambda$ small (e.g., 0.001)**: Slight penalty for large weights
- **$\lambda$ large (e.g., 100)**: Heavy penalty, forces weights to be small

With high regularization, some weights might shrink toward zero, but Ridge never forces them exactly to zero.

---

## The Update Rule With Regularization

Using gradient descent, the gradient now includes the regularization penalty:

$$\frac{\partial J}{\partial w} = \frac{2}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i) x_i + 2\lambda w$$

The extra $2\lambda w$ term pushes weights toward zero.

The weight update becomes:

$$w_{new} = w_{old} - \eta \left( \frac{2}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i) x_i + 2\lambda w_{old} \right)$$

This is sometimes written as:

$$w_{new} = (1 - 2\eta\lambda) w_{old} - \eta \frac{2}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i) x_i$$

The factor $(1 - 2\eta\lambda) < 1$ means weights are slightly shrunk at each step.

---

## Real-World Example: Predicting Test Scores

Imagine predicting student test scores from 50 features:

- Hours studied
- Sleep the night before
- Class attendance  
- Previous test scores
- ... many more

With 100 students and no regularization:

| Model | Training Accuracy | Test Accuracy |
|-------|-------------------|---------------|
| Linear Regression | 95% | 42% |
| Ridge (small λ) | 88% | 80% |
| Ridge (medium λ) | 82% | 82% |
| Ridge (large λ) | 75% | 76% |

The vanilla linear regression perfectly fits the training data but fails on test data (overfitting).

Ridge regression trades off some training accuracy for better test accuracy.

---

## Strengths of Ridge Regression

- **Handles multicollinearity**: Works well when features are highly correlated
- **Reduces overfitting**: Forces weights to be reasonable rather than extreme
- **Smoother predictions**: Weights don't swing wildly based on noise
- **Always has a solution**: Even if X has more columns than rows
- **Simple to implement**: Just an added penalty term
- **All features are kept**: Unlike some other methods, it doesn't remove features

---

## Limitations of Ridge Regression

### 1. Doesn't Do Feature Selection
Ridge shrinks weights toward zero but never exactly to zero.

If you have 100 features, Ridge still uses all 100 (though some may have tiny weights).

If you want to select which features matter most, you need a different approach (like Lasso).

### 2. Requires Tuning λ
Choosing the right regularization strength is an art. Too little and it doesn't help. Too much and it underfits.

This usually requires cross-validation (testing different values).

### 3. Still Assumes Linearity
Regularization helps with overfitting, but doesn't change the fundamental linear structure.

If the true relationship is curved, Ridge won't capture it.

### 4. Interpretability is Harder
With regularization, the weights change, so you can't interpret them as simply as before.

---

## Multicollinearity Problem (Why Ridge Helps)

**Multicollinearity**: When two features are highly correlated.

Example: predicting house price from:
- Square feet
- Number of rooms

These are correlated (more rooms usually means more square feet).

Unregularized linear regression might assign:
- Weight to square feet: +300
- Weight to rooms: -200 (negative!)

These large opposite weights cancel out, making the model unstable. Small changes in data lead to huge weight changes.

Ridge regularization prevents this by penalizing large weights. It forces the model to distribute weights more evenly:
- Weight to square feet: +100
- Weight to rooms: +50

This is still predictive but more stable.

---

## Choosing λ Through Cross-Validation

In practice, you don't hardcode $\lambda$. Instead:

1. **Try different values**: λ = 0.001, 0.01, 0.1, 1, 10, 100
2. **For each value**, train the model on a subset of data
3. **Evaluate on held-out data** to see which λ generalized best
4. **Use that λ** for your final model

This process is called **cross-validation**.

---

## Connection to the Lineage

Linear regression learned weights from data.

But it had a weakness: large weights led to overfitting.

Ridge regression solves this by **constraining the weights to be small**.

This introduces a fundamental concept that appears throughout machine learning:

> Adding a constraint or penalty during training can prevent overfitting

This pattern appears in:

- **Lasso Regression** (different penalty)
- **Neural Networks** (weight decay)
- **Ensemble Methods** (diversification)

Regularization is not just a technical fix—it is a principle for building models that generalize.

---

## What Comes Next

Ridge uses L2 regularization (squared weights). 

The next section explores:

- **Lasso Regression**: Uses L1 regularization (absolute value of weights) for feature selection
- **Elastic Net**: Combines both L1 and L2