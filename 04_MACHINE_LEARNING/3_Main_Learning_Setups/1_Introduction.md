# Chapter 4.3: Introduction to the Main Learning Setups

Machine learning is one broad idea:

> improve from data or experience

But that can happen in different ways.

The most common division is into three setups:

1. **Supervised learning**
   Learn from examples that already have correct answers.

2. **Unsupervised learning**
   Learn structure from data without given answers.

3. **Reinforcement learning**
   Learn behavior through action, feedback, and reward over time.

These are not the only categories in all of machine learning,
but they are the main foundation.

They differ mostly in one question:

> what kind of feedback does the learner receive?

That question changes everything.

But it is helpful to remember: this is only one way to classify machine learning methods.
Another useful classification is by the **type of model** we use (linear, tree-based, kernel, neural, etc.).

### Two useful classification systems

1. **Task (learning setup)** – regression, classification, clustering, reinforcement
2. **Model family** – linear models, tree-based models, kernel methods, probabilistic models, neural networks

Both views are important.
A real project almost always uses both:

- choose the task you need to solve (the setup)
- choose a model family that works well for the data and the task

A quick mapping of a few common algorithms:

| Algorithm           | Task                      | Model Family |
| ------------------- | ------------------------- | ------------ |
| Linear Regression   | Regression                | Linear       |
| Logistic Regression | Classification            | Linear       |
| Random Forest       | Classification/Regression | Tree         |
| SVM                 | Classification/Regression | Kernel       |
| K-Means             | Clustering                | Clustering   |
| Neural Networks     | Many tasks                | Neural       |

If the learner receives exact answers, it can train one way.
If it receives no labels, it must search for structure.
If it receives only reward signals over time, it must learn from interaction.

So this section is not just a list.
It is about three different relationships between:

- data
- feedback
- learning

We start with the most common one:

**supervised learning**.
