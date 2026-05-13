# Chapter 4.2.7.3: Stacking (Blending)

## The Question: How Do We Combine Predictions?

You have trained three good models:
- Model A: Decision tree (accuracy 82%)
- Model B: Logistic regression (accuracy 79%)
- Model C: K-NN (accuracy 80%)

How do you combine them?

**Averaging** is one approach: predict the average of the three.

But what if you could learn **when to trust each model**?

- Trust the tree on complex patterns
- Trust logistic regression on simple linear stuff
- Trust K-NN when data is clustered

Stacking learns this automatically.

---

## The Core Idea: Meta-Learning

Stack has two levels:

**Level 0 (Base Models)**:
- Train multiple diverse models on the training data
- Each learns different patterns

**Level 1 (Meta-Model)**:
- Use the *predictions* of base models as features
- Train another model to combine these predictions

It is like having expert consultants (base models) and a manager (meta-model) who decides whose advice to follow.

---

## How Stacking Works: Step-by-Step

### Step 1: Divide Data

Split your training data into two parts:
- **Fit set**: Train base models here (2/3 of data)
- **Meta set**: Generate meta-features here (1/3 of data)

Why? If you use the same data for both levels, the meta-model will just memorize the training data.

### Step 2: Train Base Models

Train each base model on the fit set.

```
Model A (Tree):   Train on fit set
Model B (Log Reg): Train on fit set
Model C (K-NN):    Train on fit set
```

### Step 3: Generate Meta-Features

Use the trained base models to predict on the **meta set** (data they haven't seen).

For each sample in the meta set:
- Get prediction from Model A → Feature 1
- Get prediction from Model B → Feature 2
- Get prediction from Model C → Feature 3
- Original target → Target

Now you have a new dataset:
```
Meta-Feature 1  Meta-Feature 2  Meta-Feature 3  Target
0.8             0.7             0.9             1
0.1             0.2             0.05            0
...
```

### Step 4: Train Meta-Model

Train a typically simple model (like logistic regression) on these meta-features.

This model learns: "When model A predicts 0.8 and model C predicts 0.9 but model B predicts 0.1, trust C and A."

### Step 5: Final Prediction

When predicting on test data:
1. Get predictions from all base models
2. Use these as input to the meta-model
3. Output final prediction

---

## Real-World Example: Disease Diagnosis

Three doctors (models):
- **Dr. A** (Tree): Looks at symptom combinations, finds patterns
  - Good at rare diseases (overfits to symptoms)
- **Dr. B** (Logistic): Uses a simple checklist approach
  - Reliable on common diseases
- **Dr. C** (K-NN): Compares to similar past cases
  - Great when patterns are localized

Each doctor makes a diagnosis (0-1 confidence):
- Dr. A: "90% sure it is disease X"
- Dr. B: "60% sure"
- Dr. C: "95% sure"

The manager (meta-model) learns:
- "When all three agree above 80%, trust them"
- "When Dr. C and A agree but B disagrees, probably Dr. B is wrong"

Result: Better diagnoses than any single doctor.

---

## Variants

### Blending
Simpler version of stacking:
- Split data into train/validation
- Train base models on train set
- Use predictions on validation set as meta-features
- Train meta-model

Less sophisticated than full stacking but simpler to implement.

### Multi-Level Stacking
Stack on top of stack:
- Level 0: 5 base models
- Level 1: 3 meta-models trained on predictions from Level 0
- Level 2: 1 final model trained on predictions from Level 1

More complex but can capture richer interactions.

### Cross-Validation Stacking
Use cross-validation to generate meta-features (more computationally expensive but reduces overfitting).

---

## Key Tuning Parameters

### Diversity of Base Models
- Should be different from each other
- If all base models make the same mistakes, stacking won't help
- Mix: Tree + Linear + KNN + SVM

### Meta-Model Choice
- Usually simple: Logistic regression, Ridge regression, or small tree
- Keep it simple. The base models do the heavy lifting.
- Overly complex meta-model → overfitting

### Data Split for Meta-Training
- Typical: 2/3 fit set, 1/3 meta set
- Depends on dataset size and model complexity

### Cross-Validation
Use proper CV to avoid overfitting:
- Validate on separate test set
- Monitor meta-model generalization

---

## Strengths and Weaknesses

### Strengths
- **Ensemble flexibility**: Combine any types of models
- **Learned integration**: Automatically learns how to weight predictions
- **Often wins competitions**: Many Kaggle winners use stacking
- **Can exceed best base model**: Sometimes significantly

### Weaknesses
- **Complex**: More logic, harder to debug
- **Data hungry**: Need data for meta-training (2-3× training time)
- **Risk of overfitting**: If validation set for meta-training is too small
- **Less interpretable**: Hard to explain why model combination works
- **Slower prediction**: Multiple model predictions needed

---

## Stacking vs. Boosting vs. Bagging

| Method | How It Combines | When to Use | Interpretability |
|--------|-----------------|-------------|------------------|
| Bagging | Average predictions | Reduce variance | High |
| Boosting | Weighted average (sequential) | Reduce bias | Medium |
| Stacking | Learned combination | Max performance | Low |

---

## When to Use Stacking

- **High-stakes prediction**: Accuracy is paramount (medicine, finance)
- **Competition**: Kaggle, ML competitions
- **When you have diverse models**: Different model types give different strengths
- **When you have enough data**: Need data for meta-training
- **Willing to trade interpretability for performance**: Black-box is okay

---

## Real Implementation Tips

1. **Always use separate meta-training data**: Don't leak information
2. **Monitor overfitting**: Validate meta-model on held-out test set
3. **Start simple**: Base meta-model should be simpler than base models
4. **Try different base model combinations**: T try 3, 5, 10 models
5. **Use cross-validation**: Generate meta-features via k-fold CV
6. **Balance model diversity and quality**: All base models must be reasonably good

---

## What Comes Next

Stacking combines multiple classical ML models.

But what if you want to combine **predictions from different paradigms**?

For example:
- Classical ML model (tree, logistic regression)
- Embeddings from a neural network
- Rule-based system output

This moves us toward **deep learning ensembles** and **neural networks** to learn representations directly.

**Next chapters** (Chapter 5) introduce neural networks, which can be combined within a single deep architecture.