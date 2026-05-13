# Chapter 4.2.7.2: Boosting

## The Problem with Weak Models

Bagging trained many models on different data and averaged them.

But what if each model is still making systematic mistakes on the hard examples?

**Boosting** takes a different approach:

> Train models sequentially. Each new model focuses on correcting the mistakes of the previous ones.

The idea: combine weak learners (models that are slightly better than random) into a strong learner (very accurate predictor).

---

## The Core Insight: Focus on Mistakes

Imagine a student taking practice tests:
1. First attempt: gets some wrong
2. Second attempt: focuses on the hard questions missed before
3. Third attempt: focuses on what's still hard
4. By the end: handles most questions

Boosting works the same way:

1. Train model 1 on all data. Some examples are wrong.
2. Train model 2 with **extra weight on the wrong examples** from model 1
3. Train model 3 with extra weight on examples wrong by models 1 and 2
4. Combine all 3 models (with higher weights for better performers)

Each model specializes in fixing the mistakes of the previous ones.

---

## How Boosting Works: AdaBoost Example

**AdaBoost** (Adaptive Boosting) is the canonical boosting algorithm:

### Step 1: Initialize Weights

Give equal weight to all training examples:
$$w_i^{(1)} = \frac{1}{n}$$

### Step 2: Train First Model

Train model $M_1$ on all data (with equal weights).

Measure error on training data:
$$\text{Error}_1 = \sum_{i: M_1 \text{ wrong on } x_i} w_i^{(1)}$$

### Step 3: Reweight Examples

Increase the weight of examples that $M_1$ got wrong. Decrease the weight of examples it got right.

$$w_i^{(2)} = w_i^{(1)} \cdot \exp(-\alpha_1 y_i M_1(x_i))$$

Where $\alpha_1$ is based on how good the model is (better models → lower weights increase less).

Normalize so weights sum to 1 again.

### Step 4: Train Second Model

Train model $M_2$ on the data with the new weights.

Now hard examples (from step 1) have more influence when training $M_2$.

### Step 5: Repeat

Keep training $M_3, M_4, ..., M_T$ focusing on residual mistakes.

### Step 6: Final Prediction

Combine models with weighted voting:
$$\text{Final prediction} = \text{sign}\left( \sum_{t=1}^{T} \alpha_t M_t(x) \right)$$

Better models (lower training error) get higher weight $\alpha_t$.

---

## Real-World Example: Email Classification

You have 1,000 emails, 90% are legitimate and 10% are spam.

**Round 1**: Train a simple spam filter on all emails equally.
- Catches 80% of spam (correct!)
- Misses 20% of spam (these 200 spam emails are now weighted higher)
- Falsely flags 1% of legitimate emails (these are weighted lower)

**Round 2**: Train a second filter with more weight on the 200 missed spam emails.
- Specializes in detecting the tricky spam that round 1 missed
- Uses features that work on those specific emails

**Round 3**: Train a third filter on examples still wrong by rounds 1 and 2.

**Final**: Use voting where better filters get higher weight.

Result: much better spam detection than any single filter.

---

## Gradient Boosting: Boosting for Regression

AdaBoost works for classification. For regression (continuous outputs), **Gradient Boosting** uses a similar idea:

1. Train first model $M_1$ on data
2. Compute **residuals** (errors): $r_i = y_i - M_1(x_i)$
3. Train second model $M_2$ to predict the residuals $r_i$
4. Update predictions: $M_{1+2}(x) = M_1(x) + \lambda M_2(x)$ (where $\lambda$ is a learning rate)
5. Repeat with new residuals

Each model learns to fix what previous models got wrong.

---

## Popular Boosting Implementations

**XGBoost, LightGBM, CatBoost** are modern implementations of Gradient Boosting optimized for speed and accuracy.

They're essentially faster, better-tuned versions of the same core idea:
- Sequentially train weak models
- Each focuses on residual errors
- Combine with weighted voting

XGBoost became famous for winning machine learning competitions - it often beats neural networks on tabular (structured) data.

---

## Intuition: Bias vs. Variance

**Bagging** reduces **variance**: many independent models, averaged.

**Boosting** reduces **bias**: weak learners → strong learner by iterative improvement.

Different problems benefit from different approaches:
- High variance problems (model is complex, overfits): use bagging
- High bias problems (model is too simple): use boosting

---

## Strengths

**Powerful**: Boosted trees often achieve state-of-the-art performance on tabular data.

**Handles Mixed Data**: Works with numerical and categorical features.

**Feature Importance**: Can get feature importance - which features matter most.

**No Scaling Needed**: Decision trees don't care about feature scale (unlike linear models).

**Beats Neural Networks on Tabular Data**: For structured data (not images/text), boosting often wins.

---

## Limitations

**Overfitting Risk**: It's easier to overfit with boosting. Too many iterations on wrong examples can memorize noise.

**Slower Training**: Sequential training (each depends on previous) can't be parallelized like bagging.

**Parameter Tuning**: Many hyperparameters: learning rate, number of rounds, tree depth, etc. Requires careful tuning.

**Sensitive to Noisy Labels**: If many examples have wrong labels, boosting will focus on them, memorizing noise.

---

## Boosting vs. Bagging

| Aspect | Bagging | Boosting |
|--------|---------|----------|
| Diversity | Sample diversity | Error-focused diversity |
| Training | Parallel | Sequential |
| Reduces | Variance | Bias |
| Speed | Medium | Slow |
| Overfitting | Reduces | Can increase (if over-trained) |
| Best for | High variance | High bias |

---

## Connection to What Came Before

Individual models (trees, linear) have limits. Bagging and boosting show ensemble principles:
- Many models > one complex model
- Diversity reduces error (different aspects, or different mistakes)
- Aggregation (averaging or voting) is powerful

This principle shows up throughout modern ML: ensemble of neural networks, mixture of experts, committee machines.

---

## What Comes Next

We've now covered major classical ML model families:
- Linear models
- Tree-based models
- Probabilistic models
- Kernel methods
- Ensemble methods

**Next**: See how these models feed into the three main learning setups:
- Supervised Learning (prediction with labels)
- Unsupervised Learning (finding structure without labels)
- Reinforcement Learning (learning from interaction)