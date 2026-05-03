# Chapter 3.1.3: Random Variables, Distributions, and Expectation

To reason with probability, AI needs a way to describe uncertain quantities clearly.

That is where three ideas enter:

- random variables
- probability distributions
- expectation

## 1. Random Variable

A **random variable** is a variable whose value is uncertain.

Examples:

- `Weather` may be `{sunny, rainy, cloudy}`
- `DieRoll` may be `{1, 2, 3, 4, 5, 6}`
- `Spam` may be `{yes, no}`

The point is not that the variable is random in a magical way.
The point is that **we do not know its value with certainty in advance**.

## 2. Probability Distribution

A **probability distribution** tells us how likely each possible value is.

Example:

`P(Weather = rainy) = 0.4`

`P(Weather = sunny) = 0.35`

`P(Weather = cloudy) = 0.25`

These numbers must add up to `1`.

So a distribution is a formal way to describe uncertainty.

## 3. Expectation

Sometimes we want one summary number that tells us the average result we should expect.

That is **expectation**.

For a discrete random variable `X`, the expectation is:

`E[X] = sum over x of x P(X = x)`

### Simple Example

For a fair die:

`E[X] = 1(1/6) + 2(1/6) + 3(1/6) + 4(1/6) + 5(1/6) + 6(1/6) = 3.5`

You never roll a `3.5`, but `3.5` is the average value over many rolls.

## 4. Why This Matters for AI

These ideas gave AI something logic could not give easily:

- a way to represent uncertain states
- a way to compare possible outcomes numerically
- a way to reason about averages, risk, and likely behavior

### Small AI Illustration

Suppose a delivery robot estimates the travel time for a route.

The time is uncertain because of traffic.

If:

- 20 minutes with probability `0.5`
- 30 minutes with probability `0.3`
- 40 minutes with probability `0.2`

then:

`E[Time] = 20(0.5) + 30(0.3) + 40(0.2) = 27`

So the expected travel time is 27 minutes.

That kind of reasoning becomes very useful once AI has to choose between actions.

Before that, we still need one more key idea:

> how does one piece of knowledge change another?

That leads us to **conditional probability**.
