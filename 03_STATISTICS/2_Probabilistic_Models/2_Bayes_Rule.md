# Chapter 3.2.2: Bayes' Rule

Bayes' rule is one of the central formulas of statistical AI.

It tells us how to reverse a probability question:

- from `P(E|H)` to `P(H|E)`

The formula is:

`P(H|E) = P(E|H) P(H) / P(E)`

Where:

- `H` = hypothesis
- `E` = evidence
- `P(H)` = prior
- `P(E|H)` = likelihood
- `P(H|E)` = posterior

## 1. What It Means

Bayes' rule helps answer this kind of question:

> after seeing evidence, how should I update my belief in a hypothesis?

This is why it became so important in diagnosis, classification, filtering, and many other AI tasks.

## 2. Medical Illustration

Suppose:

- `P(Disease) = 0.01`
- `P(Positive|Disease) = 0.90`
- `P(Positive|NoDisease) = 0.05`

Then:

`P(Positive) = 0.90(0.01) + 0.05(0.99) = 0.0585`

So:

`P(Disease|Positive) = 0.90(0.01) / 0.0585 approx 0.154`

That is about `15.4%`.

This surprises many people.
The test is positive, yet the disease is still not highly likely.

Why?

Because the disease was rare to begin with.

That is the importance of the **prior**.

## 3. Why Bayes' Rule Matters in AI

Bayes' rule teaches a deep lesson:

> evidence should not be judged alone
> it should be judged together with prior belief

This helped AI move away from brittle shortcuts like:

- "positive test means disease"
- "dark cloud means rain"
- "this word means spam"

Instead, AI could reason with:

- how common the event is
- how strong the evidence is
- how uncertain the observation may be

## 4. Why This Is a Bridge

Bayes' rule is still a formula.
But it already behaves like a model of learning from evidence.

That is why it sits at the center of the statistical shift.

From here, AI starts building systems that combine many pieces of evidence at once.

One famous early example of that is **Naive Bayes**.
