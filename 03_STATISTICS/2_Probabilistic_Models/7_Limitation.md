# Chapter 3.2.7: Limitation: Representation Rigidity

Probabilistic models were a major advance over pure symbolic logic.

They allowed AI to:

- reason under uncertainty
- combine evidence
- model hidden causes
- work with sequences and changing states

That is real progress.

But they still had an important limitation.

## 1. The Main Problem

Many probabilistic systems still needed humans to decide:

- which variables matter
- what the model structure should be
- which dependencies to include
- which assumptions are acceptable

That means the human designer was still carrying a lot of the burden.

This is similar to the old knowledge engineering problem, even though the framework is now probabilistic instead of logical.

## 2. Why This Becomes Hard

As domains grow, the number of possible variables and relationships can explode.

Examples:

- language has too many possible patterns
- images have too many raw features
- real-world events are often messy and unstructured

So even if the math is good, model design can become rigid and difficult.

## 3. The Deeper Limitation

Probabilistic models often work best when:

- the important variables are known
- the structure is not too large
- the assumptions are reasonable

But modern problems often break these conditions.

The system needs more flexibility.
It needs ways to discover useful structure from data rather than depending so heavily on human design.

## 4. Why This Forces the Next Shift

This is the key lineage lesson:

> probability solved uncertainty, but it did not fully solve representation

AI still needed a stronger way to learn patterns automatically.

That is why the story cannot stop at probabilistic models.

The next stage is not random.
It is forced again by limitation.

We now move from modeling uncertain structure by hand toward **learning structure from data**.

That brings us to decision-making first, and soon after that, to **Machine Learning**.
