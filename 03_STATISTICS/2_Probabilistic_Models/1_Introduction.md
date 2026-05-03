# Chapter 3.2.1: Introduction to Probabilistic Models

In Section 3.1, probability entered AI as a new way to reason.

Now the next question is:

> how do we build full models of uncertain worlds?

That is the role of **probabilistic models**.

A probabilistic model does not only store one probability.
It describes how many uncertain variables relate to one another.

This is important because AI rarely faces one uncertain event in isolation.

It usually faces many connected uncertainties:

- symptoms and diseases
- words and document classes
- states over time
- observations and hidden causes

So the job of a probabilistic model is to represent those relationships in a structured way.

In this section, we move through a connected sequence:

1. Bayes' rule
2. Naive Bayes
3. Graphical models
4. Markov models
5. Inference vs learning
6. The limitations of hand-built probabilistic structure

This section matters because it sits in the middle of the lineage.

It is richer than pure logic,
but it still often depends on human-designed variables and structure.

That is why it is powerful, but not yet the final answer.

We start with the most famous updating rule in probability:

**Bayes' rule**.
