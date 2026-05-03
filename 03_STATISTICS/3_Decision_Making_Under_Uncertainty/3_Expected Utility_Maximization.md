# Chapter 3.3.3: Expected Utility Maximization

Now we combine the two main ingredients of decision-making:

- probability
- utility

The core principle is:

> choose the action with the highest expected utility

A simple form is:

`a* = argmax over 'a' of sum over 's' of P(s|a) U(s)`

Where:

- `a*` = best action
- `s` = possible outcome
- `P(s|a)` = probability of outcome `s` if action `a` is taken
- `U(s)` = utility of outcome `s`

## 1. What This Means

For each possible action:

1. list possible outcomes
2. weight each outcome by its probability
3. multiply by how valuable it is
4. add the results

Then choose the action with the biggest total.

## 2. Small Illustration

Suppose a student has two travel choices before an exam.

### Option A

- arrives on time with probability `0.9`, utility `10`
- arrives late with probability `0.1`, utility `2`

Expected utility:

`EU(A) = 0.9(10) + 0.1(2) = 9.2`

### Option B

- arrives on time with probability `0.6`, utility `14`
- arrives late with probability `0.4`, utility `0`

Expected utility:

`EU(B) = 0.6(14) + 0.4(0) = 8.4`

So Option A is better under expected utility.

## 3. Why This Was Important in AI

This idea gave AI a clean mathematical answer to a very old question:

> how should a rational agent act under uncertainty?

It connected:

- probability from statistics
- preference from decision theory
- action from AI

That is a major convergence point in the lineage.

But many real tasks are not one-step decisions.
They are sequences of decisions over time.

That leads us to **Markov Decision Processes**.
