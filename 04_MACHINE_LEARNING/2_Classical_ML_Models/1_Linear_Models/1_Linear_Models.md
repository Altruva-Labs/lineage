# Chapter 4.2.2: Introduction to Linear Models

One of the simplest and most important model families in machine learning is the **linear model**.

Its core idea is:

> combine features using weights

A simple form looks like:

`y_hat = w_1x_1 + w_2x_2 + ... + w_nx_n + b`

Where:

- `x_1, x_2, ..., x_n` are features
- `w_1, w_2, ..., w_n` are weights
- `b` is a bias term

## 1. Why Linear Models Matter

Linear models matter because they are:

- simple
- interpretable
- mathematically clean
- historically central

They helped show that useful prediction could come from learned parameters, not only hand-written rules.

## 2. Common Linear Models

This section covers several key linear models:

- Linear Regression (for continuous outputs)
- Logistic Regression (for classification)
- Lasso Regression (with L1 regularization)
- Ridge Regression (with L2 regularization)
- Elastic Net (combines L1 and L2)
- Linear SVM (support vector machine for linear separation)

Each has its own strengths and use cases.

## 3. Strengths of Linear Models

Linear models work well when:

- relationships are simple or roughly linear
- features are informative
- interpretability is important

## 4. Limits of Linear Models

Their main weakness is also clear:

> the real world is often not linear

If the pattern depends on complex interactions, raw linear models may struggle.

This pushed machine learning toward richer models.

## 5. What Comes Next

We begin with the most basic linear model: **linear regression**.
