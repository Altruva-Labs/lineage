# Chapter 4.2.7: Ensemble Methods

Ensemble methods build stronger models by combining multiple weaker ones.
The core idea is that a group of models can correct each other's mistakes.

## 1. Core Idea

Instead of training one model, ensembles train many and then combine their outputs.
The combination can be as simple as averaging or voting, or more complex.

This often improves accuracy and robustness.

## 2. Major Forms of Ensembles

### Bagging (Bootstrap Aggregating)

Bagging trains each model on a different random subset of the data (with replacement).
This reduces variance.

**Random Forest** is the most famous bagging method.
It builds many decision trees and averages their predictions.

### Boosting

Boosting trains models sequentially.
Each new model focuses on examples that previous models got wrong.
This reduces bias and can produce very strong predictors.

Popular boosting implementations include:

- **Gradient Boosting Machines** (GBMs)
- **XGBoost**
- **LightGBM**
- **CatBoost**

### Stacking (Blending)

Stacking trains multiple base models and then trains a second-level model to combine their outputs.
This lets the ensemble learn how to best mix the individual model predictions.

## 3. Strengths

Ensembles are powerful because they:

- reduce overfitting compared to a single model
- often improve performance with little extra feature engineering
- can combine different model families (trees, linear models, neural nets)

## 4. Limits

They can also be:

- harder to interpret (many models instead of one)
- more expensive to train and run
- sensitive to how the ensemble is constructed

## 5. Why This Matters in the Lineage

Ensemble methods became a dominant practical approach in classical machine learning.
They show how combining simple models can outperform complex single models.

The ideas behind ensembles continue to appear in modern architectures and model-soup approaches.

## 6. What Comes Next

We have now expanded our model toolbox with:
- probabilistic models
- kernel methods
- ensembles

The next section of this chapter will show how these model families are used in the three main learning setups: supervised, unsupervised, and reinforcement learning.
