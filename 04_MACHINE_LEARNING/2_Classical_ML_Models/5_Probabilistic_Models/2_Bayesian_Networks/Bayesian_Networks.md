# Chapter 4.2.5.2: Bayesian Networks

## The Problem: Modeling Real-World Relationships

In Naive Bayes, we assumed all features are independent given the class. But that's unrealistic.

In real life, variables influence each other in complex ways. Consider a medical diagnosis system:
- **Patient age** affects risk of disease
- **Patient symptoms** are caused by disease
- **Disease** causes certain test results
- **Test results** help diagnose disease

These variables are not independent. They form a network of influences.

A Bayesian Network explicitly models these relationships so you can reason with them.

---

## What Is a Bayesian Network?

A Bayesian Network (also called a **belief network** or **directed graphical model**) represents:

> A probabilistic model as a graph where nodes are variables and edges are causal/dependence relationships

Each node has a form of conditional probability: the probability of that variable given its parents in the graph.

---

## The Structure: Nodes and Edges

**Nodes** = Variables (can be discrete like "disease=yes/no" or continuous like "temperature")

**Edges** = "Depends on" relationships. An arrow from A to B means "A influences B" or "B depends on A."

Example: Medical Diagnosis Network

```
Patient Age ----->
                   |
                   v
                Disease -----> Symptoms
                   |
                   v
                Test Result
```

This says:
- Disease depends on Age (some diseases more common in old age)
- Symptoms depend on Disease (sick people show symptoms)
- Test Result depends on Disease (sick people test positive)
- Symptoms do NOT directly depend on Age (only indirectly through Disease)

---

## Joint Probability via Chain Rule

A Bayesian Network represents a **joint probability distribution** over all variables:

$$P(X_1, X_2, ..., X_n) = \prod_{i=1}^{n} P(X_i | \text{Parents}(X_i))$$

This is much more efficient than storing a huge table of all possible combinations.

Example with the network above:

$$P(\text{Age, Disease, Symptoms, TestResult})$$
$$= P(\text{Age}) \cdot P(\text{Disease}|\text{Age}) \cdot P(\text{Symptoms}|\text{Disease}) \cdot P(\text{TestResult}|\text{Disease})$$

Notice:
- Age has no parents, so $P(\text{Age})$ - just a prior
- Disease depends on Age: $P(\text{Disease}|\text{Age})$
- Symptoms only depends on Disease, not Age: $P(\text{Symptoms}|\text{Disease})$

This factorization is much smaller than the full joint distribution, which would require tables for all combinations.

---

## Real-World Example: Burglar Alarm

A classic example used in AI:

```
Burglar --------\
                 |-----> Alarm <----- Earthquake
                /
```

Variables:
- **Burglary**: Is there a burglar? (true/false)
- **Earthquake**: Is there an earthquake? (true/false)
- **Alarm**: Does the alarm go off? (true/false)

Relationships:
- If there's a burglar, alarm is likely to go off
- If there's an earthquake, alarm is likely to go off  
- These causes are somewhat independent (both cities can have earthquakes and burglaries)

**Given the alarm went off, what's the probability there's a burglar?**

With the network structure, you can use Bayes' theorem properly accounting for both causes.

---

## Inference: Asking Questions

Once you build a network, you can ask questions:

Query: "What is P(Burglary=true | Alarm=true)?"

Answer: Use Bayes' theorem. The alarm went off. Given the network structure, calculate the probability that it was specifically a burglary.

Query: "What is P(Earthquake | Burglary=true, Alarm=true)?"

Answer: What's the probability of an earthquake if we know there was a burglary and the alarm went off?

These inferences use the network structure to avoid conditioning on irrelevant variables.

---

## Learning the Network

There are two parts:
1. **Structure learning**: Determine which edges exist (which variables influence which)
2. **Parameter learning**: Estimate the conditional probability tables

### Parameter Learning (Easier)

If you already know the structure, just count in your training data:

Given data of age and disease status, estimate P(Disease=yes|Age=40s).

### Structure Learning (Harder)

Determining the structure is harder. You can:
- Use domain knowledge (ask an expert)
- Try different structures and score them (model selection)
- Use algorithms that search for good structures

---

## Strengths

**Encodes Domain Knowledge**: You can build in known relationships. If you know "age affects health", the structure makes that explicit.

**Principled Reasoning**: Based on probability theory - not ad-hoc.

**Handles Missing Data**: The network structure lets you reason about unobserved variables.

**Interpretable**: The graph structure shows what influences what.

**Efficient Representation**: The network factorization uses far fewer parameters than a full joint distribution table.

---

## Limitations

**Requires Structure Knowledge**: If the structure is wrong, the model is wrong. Getting structure right is hard.

**Inference Complexity**: If the network is large and highly connected, inference can become computationally expensive (NP-hard in worst case).

**Assumes Directed Acyclic Graph**: The relationships must form a DAG - no cycles. Real relationships sometimes have feedback loops.

**Parameter Estimation**: Even with known structure, you need enough data to estimate the conditional probabilities accurately.

---

## Comparison to Naive Bayes

| Aspect | Naive Bayes | Bayesian Network |
|--------|---|---|
| Dependencies | Assumes all independent | Explicitly models dependencies |
| Structure | Fixed (all features to class) | Can be arbitrary |
| Interpretability | Simple but unrealistic | More realistic but needs specification |
| Computational Cost | Very fast | Can be expensive |
| Data Requirements | Little data | Needs more data |

---

## Connection to What Came Before

Naive Bayes said: "All features are independent - just multiply probabilities."

Bayesian Networks say: "No, some variables depend on others - let's model those dependencies explicitly."

This is a major step:
- Naive Bayes: assumes a simple structure
- Bayesian Networks: flexible structure, but you must specify it

Later, neural networks will learn structure from data (implicitly), rather than having you specify it explicitly.

---

## What Comes Next

Bayesian Networks are good for modeling static relationships: "given these variables, what are the probabilities?"

But what if relationships change over time? What if you have a sequence of observations?

**Hidden Markov Models** extend this: they model sequences where hidden states evolve according to transition probabilities, and each state generates observations.