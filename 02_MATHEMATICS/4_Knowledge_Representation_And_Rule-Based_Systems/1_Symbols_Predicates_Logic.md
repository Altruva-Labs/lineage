# Chapter 2.4.1: Symbols, Predicates, and Logic

In the last chapter, we saw AI search through states, use heuristics, satisfy constraints, and build plans.

But a deeper question now appears:

> before a machine can reason well, how do we describe the world in a form the machine can work with?

That question leads us into **knowledge representation**.

This was a major move in classical AI.

The idea was simple:

> if we can represent knowledge clearly, then maybe the machine can reason over that knowledge clearly too

So instead of only exploring a search tree, AI also began to ask:

- What objects exist in the world?
- What properties do they have?
- How are they related?
- What rules connect one fact to another?

That is where **symbols**, **predicates**, and **logic** enter.

---

## 1. What a Symbol Is

A **symbol** is a name used to stand for something.

It may stand for:

- an object
- an action
- a place
- a property
- a relation

Examples:

- `Cat`
- `Mat`
- `Rain`
- `John`
- `Classroom_A`

The symbol itself is not the real thing.
It is a formal label for talking about the thing.

In simple words:

> symbols are the words of the machine's internal language

---

## 2. Why Symbols Mattered in Classical AI

Earlier search methods were good at exploring possibilities.
But they still needed the world to be described somehow.

If an AI system wants to reason about a room, a patient, a legal case, or a factory, it needs parts it can manipulate.

Symbols gave classical AI those parts.

This was important because it made knowledge:

- explicit
- reusable
- inspectable
- rule-friendly

So knowledge was no longer hidden only inside a search path.
It could be written down.

---

## 3. From Symbols to Statements

A single symbol is usually not enough.

Real reasoning needs statements like:

- "The cat is on the mat."
- "John is a student."
- "The light is on."

This is where **predicates** help.

A **predicate** expresses a property or a relation.

Examples:

- `Cat(Tom)` means Tom is a cat
- `Student(John)` means John is a student
- `On(Cat, Mat)` means the cat is on the mat

Here:

- `Cat` is a predicate of one argument
- `On` is a predicate of two arguments

So a predicate works like a structured sentence pattern.

---

## 4. Property vs Relation

This distinction is useful.

### Property

A property says something about one object.

Example:

`Red(Apple_1)`

This means `Apple_1` has the property "red".

### Relation

A relation connects two or more objects.

Example:

`OlderThan(Amina, Musa)`

This means Amina is older than Musa.

So:

- one-argument predicate -> property
- two-or-more-argument predicate -> relation

---

## 5. A Small Real-World Illustration

Imagine a school attendance register.

You may want to represent facts like:

- `Student(Ada)`
- `Class(SS2A)`
- `InClass(Ada, SS2A)`
- `Present(Ada, Monday)`

Now the machine can reason over school facts in a clean way.

For example, if we also have a rule:

`Present(x, Monday) -> Marked(x)`

then from:

`Present(Ada, Monday)`

the system may infer:

`Marked(Ada)`

That is the core dream of symbolic AI:

> represent the world as formal statements, then derive new statements by reasoning

---

## 6. What Logic Adds

Symbols and predicates give us pieces.
**Logic** gives us rules for combining those pieces correctly.

Logic helps us talk about:

- what is true
- what follows from what
- when a conclusion is valid

For example:

- `P -> Q` means "if P is true, then Q is true"
- `P ∧ Q` means "P and Q are both true"
- `¬P` means "P is not true"

So if:

- `Rain`
- `Rain -> WetGround`

then we can conclude:

- `WetGround`

This pattern is one of the simplest forms of reasoning in logic.

---

## 7. Knowledge Base View

A symbolic AI system often stores knowledge in a **knowledge base**.

You can think of it as:

`Knowledge Base = Facts + Rules`

Where:

- **facts** say what is currently known
- **rules** say what can be concluded when some facts are true

Example:

Facts:

- `Human(Sade)`
- `Human(Tunde)`

Rule:

- `Human(x) -> Mortal(x)`

Then the system can infer:

- `Mortal(Sade)`
- `Mortal(Tunde)`

---

## 8. Why This Felt Powerful

This approach was attractive for a very good reason.

It looked close to how careful human reasoning sometimes works:

- name the important things
- describe their relations
- apply rules
- derive conclusions

That made symbolic AI feel explainable.

You could often inspect:

- the symbols
- the rules
- the reasoning steps

That is very different from later systems where knowledge is often distributed inside learned parameters.

---

## 9. But Representation Is Not the Same as Reality

This is an important warning.

A symbolic representation is only a model of the world.
It is not the world itself.

If the symbols are poor, incomplete, or too rigid, the reasoning built on top of them will also be weak.

So knowledge representation gave AI power, but it also created a burden:

> humans had to decide what should be represented, and how

That pressure will become more serious later in this chapter.

---

## 10. Key Insight

Search asked:

> which path should we explore?

Knowledge representation asks:

> what exactly are we exploring and how should it be described?

That is why this chapter matters.

Before a machine can reason, it needs a language for the world.

Symbols and predicates were among the first strong answers classical AI gave to that problem.

---

## 11. Forward Link

Now that we can write structured statements like:

- `Cat(Tom)`
- `On(Tom, Mat)`
- `Human(x) -> Mortal(x)`

the next question becomes:

> how expressive should this logic be?

That takes us to the next section:

**Propositional Logic vs First-Order Logic**.
