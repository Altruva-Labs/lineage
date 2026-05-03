# Chapter 2.4.3: Inference Engines

We now have facts, predicates, and logical rules.

But a knowledge base on its own is passive.
It just sits there.

So classical AI needed another piece:

> a mechanism that can apply the rules and produce conclusions

That mechanism is the **inference engine**.

In simple words:

> the knowledge base stores what is known; the inference engine works out what follows

---

## 1. Basic Idea

You can think of an inference engine as the reasoning machine inside a rule-based system.

It takes:

- known facts
- stored rules

and tries to derive:

- new facts
- answers to questions
- decisions

In compact form:

`Facts + Rules --Inference Engine → Conclusions`

---

## 2. A Tiny Example

Suppose the system knows:

- `Fever(Amaka)`
- `Cough(Amaka)`

And it has a rule:

`Fever(x) ∧ Cough(x) → NeedsCheckup(x)`

Then the inference engine can derive:

- `NeedsCheckup(Amaka)`

Notice what happened:

The new statement was not typed directly by a human.
It was derived from existing knowledge.

That is the power of inference.

---

## 3. Why Inference Was Important

This mattered because classical AI was not trying to build systems that only store information.

It wanted systems that could:

- reason from known facts
- explain conclusions
- solve domain problems using explicit knowledge

This made symbolic AI look intelligent in a very visible way.

The system could often say not only **what** it concluded, but also **why**.

---

## 4. Two Main Styles of Inference

The two most famous styles in rule-based AI are:

- **forward chaining**
- **backward chaining**

They use the same knowledge in different directions.

---

## 5. Forward Chaining

Forward chaining is **data-driven**.

It starts from the facts already known and keeps applying rules to produce new facts.

The pattern looks like this:

`Known Facts → Apply Rules → New Facts → ...`

### Small Illustration

Facts:

- `Rain`
- `Cold`

Rule:

`Rain ∧ Cold → StayInside`

The engine sees that the facts satisfy the rule, so it concludes:

- `StayInside`

This style is useful when new data keeps arriving and the system should keep updating what it knows.

---

## 6. Backward Chaining

Backward chaining is **goal-driven**.

It starts from a goal or question, then asks:

> what must be true for this goal to hold?

It works backward through the rules.

### Small Illustration

Suppose the goal is:

- `PassCourse(Tola)`

And the system has a rule:

`AssignmentDone(x) ∧ ExamPassed(x) → PassCourse(x)`

Now the engine asks:

- Is `AssignmentDone(Tola)` true?
- Is `ExamPassed(Tola)` true?

If it can prove both, then it proves:

- `PassCourse(Tola)`

This is the basic spirit behind logic programming systems such as Prolog.

---

## 7. Everyday Analogy

Think of a detective.

### Forward chaining

The detective keeps collecting clues and then says:

> "Since I know A and B, I can now conclude C."

### Backward chaining

The detective starts with a suspicion and says:

> "If C is true, what evidence would I need to prove it?"

Both styles reason.
They just move in different directions.

---

## 8. Match This with Search

Inference may look different from search, but the family resemblance is still there.

In search, the system explores states.
In inference, the system explores possible conclusions and rule applications.

So this chapter is not leaving the earlier lineage behind.
It is extending it.

Instead of searching over moves in a map, the machine may now search over:

- rules
- facts
- proof steps

That is still a form of controlled problem solving.

---

## 9. Soundness and Completeness

When people discuss logical inference, two classic ideas matter:

### Soundness

If a system derives a conclusion, that conclusion should really follow from the knowledge base.

In short:

> the engine should not invent false conclusions from the rules

### Completeness

If a conclusion truly follows from the knowledge base, a complete inference procedure should be able to derive it.

In short:

> the engine should not miss conclusions that are logically available

These ideas mattered because AI researchers wanted reasoning systems that were not only useful, but also formally trustworthy.

---

## 10. Why This Became Practical

Inference engines made rule-based AI useful in areas where people wanted:

- clear domain knowledge
- explainable reasoning
- repeatable decisions

That included:

- medical decision support
- configuration systems
- diagnosis
- planning support
- logic programming

But this also introduced a pressure point:

the more knowledge you want the engine to use, the more knowledge someone must encode first.

We will soon see how serious that problem became.

---

## 11. Key Insight

Representation gives AI a language.
Inference gives AI a reasoning procedure over that language.

Without representation, there is little to reason about.
Without inference, stored knowledge cannot do much work.

Classical AI needed both.

---

## 12. Forward Link

Once inference engines became workable, researchers tried to build real systems around them.

That gave rise to one of the most famous products of symbolic AI:

**Expert Systems**.
