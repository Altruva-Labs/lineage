# Chapter 3.2.6: Inference vs Learning

By now, we have probabilistic models.

But two different tasks appear around them:

- **inference**
- **learning**

These are related, but they are not the same.

## 1. Inference

Inference means:

> given a model and some observations, compute what is likely

Examples:

- compute `P(Disease|Symptoms)`
- compute the most likely hidden state in an HMM
- update belief after new evidence

So inference is about **reasoning inside a model**.

## 2. Learning

Learning means:

> use data to estimate the model itself

Examples:

- estimate `P(Word|Spam)` from labeled emails
- estimate transition probabilities from observed sequences
- estimate parameters in a Bayesian network

So learning is about **building or adjusting the model from data**.

## 3. Why This Distinction Matters

This is a very important lineage point.

In the earlier Classical AI sections, humans mostly built the structure and rules.

In probabilistic AI, that still often happens.
But now data begins to play a larger role.

That means AI is moving from:

- reasoning with fixed knowledge - inference

toward:

- estimating knowledge from experience - learning

This is one of the clearest signs that machine learning is getting close.

## 4. Simple Illustration

Suppose a clinic model already knows:

- symptom probabilities
- disease priors

Then asking:

`P(Disease|Symptoms)`

is inference.

But using past patient records to estimate those probabilities in the first place is learning.

Both matter.

AI must both:

- reason with uncertainty
- improve models from data

That sounds powerful, but there is still a limitation.

Many probabilistic models still depend on humans to choose the variables and structure in advance.

That is the next pressure point.
