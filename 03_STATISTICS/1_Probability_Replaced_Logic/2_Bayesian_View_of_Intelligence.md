# Chapter 3.1.2: Bayesian View of Intelligence

Once probability enters AI, a new picture of intelligence appears.

It says:

> intelligence is not only rule application
> it is also belief updating when new evidence arrives

This is the Bayesian view.

The core formula is:

`P(H|E) = P(E|H) P(H) / P(E)`

Where:

- `H` = hypothesis
- `E` = evidence
- `P(H)` = prior belief before seeing the evidence
- `P(E|H)` = how likely the evidence is if the hypothesis is true
- `P(H|E)` = posterior belief after seeing the evidence

In simple words:

- start with a belief
- observe new evidence
- update the belief

### Small Illustration

Suppose:

- `H = "It will rain today"`
- `E = "The sky is very dark"`

Before looking outside, you may already believe rain is possible.
That is the prior.

After seeing a very dark sky, your belief should change.
That new belief is the posterior.

This is important because it gives AI a principled way to learn from evidence even before we get to machine learning.

The system does not need to say:

> "Dark sky means rain with absolute certainty."

It can say:

> "Dark sky makes rain more likely."

That is a much better fit for real life.

### Why This Matters in the Lineage

In symbolic AI, the machine often asked:

> what conclusion follows from these rules?

In Bayesian reasoning, the machine asks:

> how should my belief change after seeing this evidence?

That is a deep change.

It moves AI toward:

- uncertainty-aware reasoning
- evidence combination
- gradual belief revision

This will soon become the basis for diagnosis, prediction, filtering, and probabilistic models.

But to use probability well, we first need some building blocks:

- random variables
- distributions
- expectations

That is the next step.
