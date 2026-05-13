# Chapter 4.2.5.1: Naive Bayes

## The Problem: Classification When You're Not Sure

Imagine you're building spam filter. You get an email with the words "FREE!!!1" and "click here now" - pretty suspicious.

But are you certain it's spam? Not 100%. Maybe it's a legitimate promotion.

**Naive Bayes** doesn't give you a yes or no. It gives you probabilities:
- 92% chance this is spam
- 8% chance it's legitimate

It does this using **Bayes' theorem** from probability theory, which is a mathematically principled way to update beliefs when you see new evidence.

---

## What Is Bayes' Theorem?

Bayes' theorem is about **conditional probability** - the probability of something given that you've observed evidence.

The theorem states:

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

In words:
- $P(A|B)$ = probability of A given B (what we want to know)
- $P(B|A)$ = probability of B given A (how likely the evidence if A is true)
- $P(A)$ = probability of A (before seeing evidence, called the "prior")
- $P(B)$ = probability of B (total probability of seeing this evidence)

Real-world example:

- $A$ = "email is spam"
- $B$ = "email contains $$FREE"
- $P(\text{spam}|\text{FREE})$ = probability it's spam given that it says FREE

Bayes' theorem says:
$$P(\text{spam}|\text{FREE}) = \frac{P(\text{FREE}|\text{spam}) \cdot P(\text{spam})}{P(\text{FREE})}$$

---

## From Bayes' Theorem to Naive Bayes

Bayes' theorem works for one piece of evidence. But emails have many words. How do we combine them?

**Naive Bayes** makes a key assumption:

> All features are conditionally independent given the class

That is: "Given that an email is spam, the probability of seeing 'FREE' is independent of the probability of seeing 'click here'."

This is "naive" because in reality, these words are not independent - spammers use common word combinations. But despite the unrealistic assumption, the method works very well in practice.

With this assumption, the formula becomes:

$$P(\text{class}|features) = \frac{P(\text{class}) \cdot \prod_{i} P(feature_i|\text{class})}{P(\text{features})}$$

In plain terms:

> Probability of spam given these words = (Probability of spam) × (Probability of each word in spam emails) / (Total probability of seeing these words)

The right-hand side is easy to calculate from training data.

---

## How Naive Bayes Works

### Step 1: Precompute from Training Data

Count in spam emails: 50,000 contain "FREE", 40,000 contain "click"
Count in non-spam emails: 2,000 contain "FREE", 15,000 contain "click"
Total spam emails: 100,000
Total non-spam emails: 100,000

From this:
$$P(\text{FREE}|\text{spam}) = \frac{50,000}{100,000} = 0.5$$
$$P(\text{click}|\text{spam}) = \frac{40,000}{100,000} = 0.4$$
$$P(\text{FREE}|\text{not spam}) = \frac{2,000}{100,000} = 0.02$$
$$P(\text{click}|\text{not spam}) = \frac{15,000}{100,000} = 0.15$$
$$P(\text{spam}) = \frac{100,000}{200,000} = 0.5$$

### Step 2: Classify New Example

New email contains: "FREE" and "click"

$$P(\text{spam}|\text{FREE, click}) \propto P(\text{spam}) \cdot P(\text{FREE}|\text{spam}) \cdot P(\text{click}|\text{spam})$$
$$= 0.5 \times 0.5 \times 0.4 = 0.1$$

$$P(\text{not spam}|\text{FREE, click}) \propto P(\text{not spam}) \cdot P(\text{FREE}|\text{not spam}) \cdot P(\text{click}|\text{not spam})$$
$$= 0.5 \times 0.02 \times 0.15 = 0.0015$$

Normalize to probabilities:
- P(spam) = 0.1 / (0.1 + 0.0015) ≈ 0.985
- P(not spam) = 0.0015 / (0.1 + 0.0015) ≈ 0.015

**Prediction: 98.5% chance it's spam.**

---

## Real-World Example: Disease Diagnosis

A patient has a fever. You want to know: "What's the probability they have the flu?"

Known from past data:
- 1% of the population has the flu: $P(\text{flu}) = 0.01$
- 90% of flu patients have fever: $P(\text{fever}|\text{flu}) = 0.9$
- 10% of non-flu people have fever: $P(\text{fever}|\text{not flu}) = 0.1$

Using Bayes:

$$P(\text{flu}|\text{fever}) = \frac{P(\text{fever}|\text{flu}) \cdot P(\text{flu})}{P(\text{fever})}$$

$$P(\text{fever}) = P(\text{fever}|\text{flu}) \cdot P(\text{flu}) + P(\text{fever}|\text{not flu}) \cdot P(\text{not flu})$$
$$= 0.9 \times 0.01 + 0.1 \times 0.99 = 0.009 + 0.099 = 0.108$$

$$P(\text{flu}|\text{fever}) = \frac{0.9 \times 0.01}{0.108} = \frac{0.009}{0.108} \approx 0.083 = 8.3\%$$

Surprising! Even though the person has a fever, they're only 8.3% likely to have the flu (not 90%). Why? Because fever is common overall, and most people with fever don't have the flu.

---

## Variants of Naive Bayes

Naive Bayes can work with different probability distributions:

**Gaussian Naive Bayes**: Assumes features come from a Gaussian (normal) distribution. Good for continuous features like height, weight, temperature.

**Multinomial Naive Bayes**: Assumes features are counts (like word frequencies). Good for text classification.

**Bernoulli Naive Bayes**: Assumes features are binary (present/absent). Good for text with just "word appears" or "doesn't appear".

---

## Strengths

**Very Fast**: Just counts and multiplies. No expensive optimization. Can train and predict on millions of examples quickly.

**Works Well with High Dimensions**: Text classification often has thousands of words (features). Despite the high dimensionality, Naive Bayes doesn't struggle because it just counts.

**Little Data Needed**: Works with relatively small training sets compared to other methods.

**Probabilistic Output**: You get confidence scores, not just "yes" or "no".

**Simple and Interpretable**: You can see which features matter most for each class.

---

## Limitations

**The Independence Assumption is Wrong**: Features are rarely truly independent. In spam emails, certain word combinations are more common than their individual frequencies suggest.

**Struggles with Correlated Features**: If two features are highly correlated, Naive Bayes effectively double-counts their effect.

**Zero Probability Problem**: If a word never appears in spam emails in training data, then P(word|spam) = 0, which makes P(spam|...) = 0 even if other evidence suggests spam. 

(Solution: **smoothing** - add a small count to all words to avoid exact zeros.)

**Assumes Features are Independent**: This is rarely true in real data.

---

## Connection to What Came Before

Chapters 4.1 taught us about data and loss functions.

Linear Regression (4.2.3) finds weights to minimize error.

Naive Bayes takes a different approach: **don't optimize weights, instead estimate class probabilities directly from data using probability theory.**

This is the start of **probabilistic modeling** - learning by estimating probability distributions instead of fitting weighted sums.

---

## What Comes Next

Naive Bayes assumes all features are independent. But in reality, variables are often connected.

**Bayesian Networks** extend this idea: they explicitly model which variables depend on which, creating a graph of dependencies.

Then **Hidden Markov Models** add time: they model sequences where hidden states evolve over time.