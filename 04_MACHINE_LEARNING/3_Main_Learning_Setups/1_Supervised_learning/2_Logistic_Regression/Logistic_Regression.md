# Chapter 4.3.1.2: Logistic Regression in Supervised Learning

Logistic regression is used for binary or multiclass classification in supervised learning.

## 1. Core Idea

Models the probability of a class using the logistic function.

## 2. How It Works

Uses maximum likelihood to fit the sigmoid: `p(y=1|x) = 1 / (1 + exp(-w·x))`

## 3. Strengths

- Outputs probabilities
- Interpretable weights
- Efficient for linear boundaries

## 4. Limits

- Assumes linear decision boundary
- Not great for complex patterns

## 5. What Comes Next

SVM for better margins.