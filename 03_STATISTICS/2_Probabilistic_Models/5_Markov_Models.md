# Chapter 3.2.5: Markov Models

Many AI problems unfold over time.

Examples:

- speech arrives as a sequence
- robot states change step by step
- weather changes day by day
- a sentence unfolds word by word

To model such problems, AI needed probability models for sequences.

That is where **Markov models** enter.

## 1. The Markov Idea

The main assumption is simple:

> the next state depends mainly on the current state, not the full past history

In shorthand:

`P(X_{t+1} | X_t, X_{t-1}, ..., X_0) = P(X_{t+1} | X_t)`

This is called the **Markov assumption**.

It is not always perfectly true, but it makes sequence modeling manageable.

## 2. Markov Chain

A **Markov chain** is the simpler case.

- states change over time
- the current state directly influences the next one

Example:

- sunny today
- rainy tomorrow
- cloudy the next day

The weather tomorrow depends a lot on today, even if we ignore the distant past.

## 3. Hidden Markov Model

A **Hidden Markov Model (HMM)** adds another idea:

- the true state is hidden
- we only observe signals produced by that hidden state

Example:

- hidden state: actual weather
- observation: umbrella use

You may not see the weather directly,
but you may see many people carrying umbrellas.
That gives evidence about the hidden state.

## 4. Why Markov Models Mattered

Markov models gave AI a practical way to reason about uncertain sequences.

They became important in areas like:

- speech recognition
- part-of-speech tagging
- time-series modeling

Later methods became stronger, but Markov models were a major step in statistical AI.

They showed that uncertainty was not only about one static fact.
It could also be about **state evolution through time**.

That brings us to another important split:

> once we have a probabilistic model, are we trying to reason with it, or are we trying to learn it?

That is the next section.
