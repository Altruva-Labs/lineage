# Chapter 4.1.3: Loss, Training, and Optimization

Now we have data.
We have features.
We may also have labels.

The next question is:

> how does a model improve?

The short answer is:

> it makes predictions, measures error, and adjusts itself to reduce that error

## 1. Prediction

Suppose a model is written as:

`y_hat = f(x; theta)`

Where:

- `x` = input
- `theta` = model parameters
- `y_hat` = predicted output

The symbol `theta` simply stands for the adjustable parts of the model.

## 2. Loss

A model needs a way to measure how wrong it is.

That measure is called the **loss**.

If the true answer is `y` and the prediction is `y_hat`, then a loss function `l(y_hat, y)` tells us the size of the error.

For example:

- in regression, a common idea is to punish predictions that are far from the true value
- in classification, we punish wrong or overconfident predictions

One general training objective is:

`J(theta) = (1/n) sum_i l(f(x_i; theta), y_i)`

This means:

- make a prediction for each example
- measure the error
- average the errors

The model tries to make `J(theta)` small.

## 3. Optimization

Once the loss is defined, we want the best parameters:

`theta* = argmin_theta J(theta)`

This means:

- search over possible parameter values
- choose the ones that make the loss lowest

This is an optimization problem.

So machine learning depends deeply on mathematics.

Even though the model is learning from data,
under the hood it is still solving a formal optimization task.

## 4. A Real-World Illustration

Imagine a basketball player practicing free throws.

Each shot gives feedback:

- too short
- too far
- too much left
- too much right

The player adjusts based on the error.

Training a model is similar.

Each example says, in effect:

- your prediction was too high
- your prediction was too low
- this case was misclassified

Then the model adjusts.

## 5. Training Loop

A simple learning loop looks like this:

```text
1. Start with initial parameters
2. Make predictions
3. Measure loss
4. Update parameters
5. Repeat
```

In pseudocode:

```python
initialize theta

repeat:
    y_hat = model(X, theta)
    loss = error(y_hat, Y)
    theta = update(theta, loss)
```

The exact update rule depends on the model.

Some classical methods have closed-form solutions.
Others use iterative procedures.
Later, neural networks will rely heavily on gradient-based updates.

## 6. Why This Matters in the Lineage

This is a major shift from classical symbolic AI.

Earlier systems often improved because humans changed the rules.

Now the system itself can adjust internal parameters from data.

That is a deep change.

It means intelligence is moving from:

- manually specified behavior

toward:

- learned behavior

## 7. What Comes Next

But reducing training loss is not enough.

A model can do well on old examples and still fail on new ones.

That brings us to one of the most important ideas in machine learning:

**generalization**.
