# Chapter 4.2.7.1: Bagging (Bootstrap Aggregating)

## The Wisdom of Crowds

Imagine you're guessing the weight of a cow at a fair. You could ask one expert. Or you could ask 100 random people and average their guesses.

The crowd's average is usually better than any individual guess - even the experts.

This is the core idea of **Bagging**.

---

## What Is Bagging?

Bagging stands for **Bootstrap Aggregating**.

> Train many models on different random subsets of data, then average their predictions

The "bootstrap" part comes from statistics. You create new datasets by:
1. Taking your original data
2. Randomly sampling with replacement (you can pick the same point multiple times)
3. Creating a new dataset of the same size

Each sample might look slightly different from the original - some points appear multiple times, some don't appear.

Train a model on each sample. Then, for prediction, average all their outputs.

---

## Example: Building Decision Trees

Suppose you have 1,000 customer records and want to predict spending using decision trees.

**Without bagging**: Train one big tree on all 1,000 records. It might overfit to noise.

**With bagging (B=100 trees)**:
1. Create 100 bootstrap samples, each with 1,000 random points (picked with replacement)
2. Train a full decision tree on each sample
3. For a new customer, get predictions from all 100 trees
4. Average the 100 predictions

Each tree sees slightly different data, so they make slightly different mistakes. Averaging cancels out the individual mistakes.

---

## Bootstrap Samples More Formally

Given data $\{x_1, x_2, ..., x_n\}$:

For $b = 1$ to $B$:
- Create bootstrap sample: randomly pick $n$ points with replacement
- Train model $M_b$ on this sample

For prediction on new example $x$:
$$\hat{y} = \frac{1}{B} \sum_{b=1}^{B} M_b(x)$$

(For classification, use voting instead of averaging)

---

## Why Does This Work?

The original dataset has some noise - random quirks that don't reflect true patterns.

When you train one model on the exact same training data, it learns the patterns *and* the noise.

By training on slightly different subsets, each model:
- Learns the common patterns (which appear in most subsets)
- Learns slightly different noise (noise doesn't appear consistently)

When you average, the pattern signal reinforces, but the noise cancels out.

**Mathematically**: Bagging reduces **variance** without increasing **bias**.

---

## Real-World Example: Sales Prediction

You have 5 years of sales data and want to predict next month's sales.

One decision tree trained on all 5 years might develop rules like:
- "If holiday month → sales x3"
- "If competitor just entered market → sales ÷ 2"
- "If 3rd Friday is rainy → boost by 5%" (noise!)

The rainy Friday rule is an artifact of your specific data, not a real pattern.

Bagging trains 50 trees on different year-combinations. Most learn the holiday and competitor rules (real patterns). But only 2 trees happen to see that rare Friday-rain-sales correlation, so it doesn't affect the average.

---

## Random Forests: Bagging + Trees

The most famous bagging method is **Random Forest**.

It's bagging with decision trees *plus* an extra randomness: at each split in each tree, you consider only a random subset of features.

This adds even more diversity among trees, which further reduces overfitting.

Random Forests are one of the most practical ML methods - they work well across many domains without extensive tuning.

---

## Strengths

**Reduces Overfitting**: Averaging independent models is a proven way to reduce overfitting.

**Handles Many Data Types**: Works with raw features (no preprocessing needed) since decision trees are flexible.

**Interpretability (somewhat)**: You can look at which features are important across the forest.

**Parallelizable**: Train each tree independently - great for distributed computing.

**Defaults Work Well**: Random Forests with default parameters often beat carefully tuned single models.

---

## Limitations

**Computational Cost**: Slower than a single model (must train B models).

**Doesn't Help Biased Models**: If your base model structure is wrong, bagging won't fix it. Bagging reduces variance, not bias.

Example: If you use shallow decision trees that can never capture complex patterns, bagging just averages bad predictions.

**Less Control Over Individual Models**: With one model, you can interpret why a prediction was made. With 100 models, it's harder.

**Large Memory Use**: Must store B models instead of 1.

---

## Out-Of-Bag (OOB) Error

A nice property: in each bootstrap sample, roughly 37% of the original data points don't appear ("out-of-bag").

You can use these to estimate error without a separate test set:
- Train model $M_b$ on bootstrap sample $b$
- Test $M_b$ on the points not in sample $b$
- Average these test errors across all models

This gives a free estimate of generalization error!

---

## Bagging vs. Single Model

| Aspect | Single Model | Bagging |
|--------|---|---|
| Training time | Fast | Slow (×B) |
| Accuracy | Medium | Often higher |
| Overfitting | Possible | Reduced |
| Interpretability | Good | Reduced |
| Computational cost | Low | Higher |

---

## Connection to What Came Before

All the models we've seen (linear, trees, SVM, clustering) can overfit.

Bagging shows a general principle:
> Many slightly different models, averaged reasonably beats one complex model

This is a different approach than regularization (adding penalties to complexity). Instead, diversify and aggregate.

---

## What Comes Next

Bagging works by creating diversity through different data samples.

**Boosting** works differently: it creates diversity by focusing on hard examples - training each new model to fix mistakes of the previous ones.