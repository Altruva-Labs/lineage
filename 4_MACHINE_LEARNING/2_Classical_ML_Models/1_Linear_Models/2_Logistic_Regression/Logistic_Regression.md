# Chapter 4.2.1.2: Logistic Regression

## The Jump From Regression to Classification

Linear regression solves a continuous problem: "What is the output value?"

But many real problems are different: "Does this belong to category A or B?" or "Will this customer churn?"

Such problems are called **classification**.

Logistic regression is our bridge. Despite its name, it is a **classification model**, not a regression model. But it is built directly from linear regression's foundation.

---

## What Problem Does Logistic Regression Solve?

Imagine a credit card company wants to decide: should we approve this loan application?

The answer is binary: YES or NO.

They have historical data:
- Age, income, credit score, employment history
- For each person: was the loan approved AND did they repay it?

The company wants to learn: given someone's features, what is the probability they will repay?

**Why not just use linear regression?**

Linear regression predicts continuous values. It might output: 2.5, -0.3, or 100. These are not probabilities.

We need probabilities: values between 0 and 1 that answer "how confident are we?"

That is exactly what logistic regression provides.

---

## From Linear to Logistic: The Key Insight

Logistic regression takes linear regression's simple formula:

$$z = w_1x_1 + w_2x_2 + ... + w_nx_n + b$$

But instead of returning $z$ directly, it applies the **sigmoid function**:

$$\hat{y} = \sigma(z) = \frac{1}{1 + e^{-z}}$$

What does this do?

- If $z$ is very large (positive), $\sigma(z) \approx 1$ (high probability of class 1)
- If $z$ is very small (negative), $\sigma(z) \approx 0$ (high probability of class 0)
- If $z = 0$, $\sigma(z) = 0.5$ (maximum uncertainty)

The sigmoid function **squashes any input into the range [0, 1]**.

That output can be interpreted as a probability.

---

## How Logistic Regression Learns

Linear regression minimizes squared error (MSE).

Logistic regression uses a different objective: **log loss** (also called cross-entropy):

$$J(w, b) = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)]$$

Where:
- $y_i$ is the true label (0 or 1)
- $\hat{y}_i$ is the predicted probability

This loss function rewards confident correct predictions and penalizes wrong predictions.

We minimize this loss using **gradient descent** (from Chapter 4.5.2):

$$\frac{\partial J}{\partial w} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i) x_i$$

The update rule is the same as linear regression, but the loss function is different.

---

## Real-World Example: Email Spam Detection

Suppose you train a logistic regression model to detect spam emails.

Features:
- Number of exclamation marks
- Contains "FREE"
- Sender is in your contacts
- Email length

The model learns weights and makes predictions like:

- Email A: predicted probability = 0.95 (95% confident it's spam)
- Email B: predicted probability = 0.15 (15% confident it's spam, so likely legitimate)
- Email C: predicted probability = 0.52 (borderline, could go either way)

To make a binary decision, you choose a **decision threshold** (usually 0.5):

- If $\hat{y} >= 0.5$: classify as SPAM
- If $\hat{y} < 0.5$: classify as LEGITIMATE

You can adjust this threshold based on your priorities:
- High threshold (0.8): Mark fewer emails as spam (less false positives)
- Low threshold (0.2): More aggressive spam filtering (fewer false negatives)

---

## Why Logistic Regression Matters in the Lineage

This represents an important shift:

**Linear Regression**: Learn a continuous mapping from features to output  
**Logistic Regression**: Use that same mapping, but convert it to probabilities

This converts a regression problem into a classification problem while keeping the simple linear structure.

The insight is profound: many different tasks can be solved by:

1. Learning a linear combination of features
2. Applying the right transformation

This pattern repeats throughout machine learning.

---

## Strengths

- **Probabilistic interpretation**: Outputs have meaning (confidence levels)
- **Interpretability**: Weights show which features matter most
- **Simplicity**: Still just weighted features, easy to understand and explain
- **Fast**: Quick to train and predict
- **Well-calibrated**: The probabilities are often reliable
- **Works well**: Despite simplicity, often performs surprisingly well

---

## Limitations

### 1. Assumes Linear Separability in Log-Space
Logistic regression assumes a linear relationship in **log-odds space**. If the decision boundary is curved or complex, logistic regression will struggle.

### 2. Doesn't Handle Complex Interactions
If class A is defined by "high income AND high credit score" (an AND relationship), logistic regression may miss this.

### 3. Sensitive to Class Imbalance
If one class is much rarer (e.g., 1% spam, 99% legitimate), the model may over-predict the common class.

### 4. Binary by Default
While extensions exist for multiple classes, the natural form handles only two classes.

### 5. Still Linear Under the Hood
All the weaknesses of linear models apply—inability to capture curved relationships, for example.

---

## Connection to the Lineage

Linear regression showed us: machines can learn weights from data.

Logistic regression shows us: the same technique works for classification if we apply the right transformation.

This prepares us for the next layers:

- **Regularized linear models** (Ridge, Lasso): What if we penalize large weights to avoid overfitting?
- **Decision trees**: What if we relax the linearity assumption?
- **Neural networks**: What if we stack many nonlinear transformations?

---

## What Comes Next

While logistic regression is powerful, it has limits when boundaries are curved or complex.

The next sections explore:

- **Ridge and Lasso Regression**: Adding penalties to prevent overfitting
- **Other linear models**: Support Vector Machines with similar ideas
- **Nonlinear models**: Decision trees and neural networks that don't assume linearity