# Chapter 4.5.1: Objective Functions and Search

By now, one thing should be clear:

> machine learning is not only about data, it is also about search

A model has parameters.
Those parameters can take many possible values.

The learning problem is:

> which parameter values make the model perform best?

That question takes us into optimization foundations.

## 1. Why Optimization Matters

Earlier in this chapter, we already saw loss and training.

But now we slow down and look at the deeper structure.

If a model is written as:

`y_hat = f(x; theta)`

then learning usually means choosing `theta` so that prediction error becomes small.

That is why we define an objective such as:

`J(theta) = (1/n) sum_i l(f(x_i; theta), y_i)`

The model then tries to find:

`theta* = argmin_theta J(theta)`

This means:

> search for the parameter setting that makes the total error as small as possible

## 2. Objective Function

An **objective function** is the quantity we want to minimize or maximize.

In machine learning, it is often a loss or cost.

Examples:

- squared error in regression
- logistic loss in classification
- clustering objective in k-means

Different models use different objectives.
But the core pattern is the same:

> define what "good" means, then search for it

## 3. Search Space

The parameters live in a search space.

If a model has two parameters, we can imagine a 2D surface.
If it has many parameters, the space becomes high-dimensional.

Each point in that space is one possible model.

So learning is not only:

- seeing data

It is also:

- moving through parameter space

This is one of the deepest links between machine learning and mathematics.

## 4. Real-World Illustration

Imagine you are trying to make the perfect cup of tea.

You can change:

- water temperature
- tea quantity
- steeping time

Each combination gives a different result.

Your goal is to find the combination that gives the best taste.

That is an optimization problem.

Machine learning works in a similar way, except the parameters are often numbers inside a model.

## 5. Why Different Models Learn Differently

Not all models search the same way.

Some models have neat mathematical solutions.

For example, some forms of linear regression can be solved directly.

Other models use iterative search:

- try parameters
- measure error
- update parameters
- repeat

As models become more complex, iterative optimization becomes more important.

## 6. Loss Surface Intuition

It helps to picture the objective as a landscape.

- high points = large error
- low points = small error

The learner wants to move downhill toward better settings.

This picture is not perfect, but it is very useful.

It explains why training can be:

- easy in some cases
- unstable in some cases
- slow in some cases

## 7. Local and Global Optima

A **global minimum** is the best possible point on the whole landscape.

A **local minimum** is a point that is better than nearby points, even if a better one exists elsewhere.

In simple landscapes, this difference may not matter much.
In more complex ones, it matters a lot.

This becomes especially important later in neural networks.

## 8. Why This Section Matters in the Lineage

Classical AI often focused on:

- symbolic rules
- logical structure
- explicit search in state spaces

Machine learning introduces another kind of search:

> search through parameter values to fit a model from data

That is a major shift.

It means the system is no longer only searching for an external solution.
It is also searching for an internal configuration.

## 9. What Comes Next

Once we understand learning as optimization, the next question is:

> how does the model actually move through this error landscape?

That leads to gradient descent, learning rates, and training dynamics.
