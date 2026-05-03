# Chapter 3.2.3: Naive Bayes as a Bridge from Symbolic to Statistical AI

Naive Bayes is one of the clearest bridge models in the whole lineage.

Why?

Because it still looks simple and structured like classical AI,
but it reasons with probability instead of hard rules.

Its core idea is:

> combine several pieces of evidence to estimate which class is most likely

The common form is:

`P(H|X1, X2, ..., Xn) proportional to P(H) product over i of P(Xi|H)`

This comes from Bayes' rule plus the **naive conditional independence assumption**:

> once the class `H` is known, the features `X1, X2, ..., Xn` are treated as independent

## 1. Why It Is Called "Naive"

It is called naive because that independence assumption is often not fully true in real life.

Words in a sentence are not fully independent.
Symptoms in a patient are not fully independent.

But the model is still useful because the simplification makes computation easy and often works surprisingly well.

## 2. Spam Illustration

Suppose the class is:

- `Spam = yes`
- `Spam = no`

And the features are words in the message, like:

- `free`
- `win`
- `offer`

A symbolic rule system may say:

`if "free" appears, then maybe spam`

Naive Bayes does something softer:

- it gives each word a probability weight
- it combines those weights
- it chooses the most likely class

So instead of one brittle rule, we get evidence accumulation.

## 3. Why It Matters in the Lineage

Naive Bayes is important because it shows a new style of intelligence:

- less hand-written rule firing
- more belief accumulation from data and probabilities

It still needs chosen features.
It still uses structure designed by humans.
But it has clearly moved away from pure symbolic logic.

That is why it feels like a real bridge chapter between old AI and learning-based AI.

## 4. Common Uses

Historically, Naive Bayes became widely used for tasks like:

- spam filtering
- document classification
- simple diagnosis tasks

It was not powerful because it was perfect.
It was powerful because it was simple, fast, and often good enough.

From here, the next step is to represent many uncertain relationships in a more general structured way.

That leads to **graphical models**.
