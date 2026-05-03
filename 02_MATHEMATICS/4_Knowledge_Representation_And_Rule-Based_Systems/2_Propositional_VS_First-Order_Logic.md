# Chapter 2.4.2: Propositional Logic vs First-Order Logic

In the last section, we introduced symbols, predicates, and logic as the language of classical AI.

But not every logic can say the same kind of thing.

Some logics are simple and limited.
Some are richer and more expressive.

This distinction mattered a lot in AI because:

> the more complex the world you want to describe, the more expressive your representation may need to be

So in this section, we compare two important forms:

- **Propositional Logic**
- **First-Order Logic (FOL)**

---

## 1. Propositional Logic

Propositional logic is a fundamental component of artificial intelligence that allows systems to represent knowledge using simple statements that can be true or false. It enables AI to reason, infer, and make decisions based on structured information, forming the basis for more complex logical frameworks in AI.

Propositional logic works with whole statements that are either:

- true
- false

Each statement is treated like one unit.

Examples:

- `P`: "It is raining"
- `Q`: "The ground is wet"

You can connect them with logical operators:

- `¬P` : not `P`
- `P ∧ Q` : `P` and `Q`
- `P ∨ Q` : `P` or `Q`
- `P -> Q` : if `P`, then `Q`

Example rule:

`P → Q`

If:

`P = "It is raining"`

and

`Q = "The ground is wet"`

then the rule says:

> if it is raining, then the ground is wet

---

## 2. Why Propositional Logic Is Useful

It is simple.
It is clean.
It is easy to reason with.

For small domains, that simplicity is a strength.

Example:

- `PowerOn`
- `DoorClosed`
- `AlarmActive`

Rules over statements like these can be very useful in small control systems.

---

## 3. The Main Limitation of Propositional Logic

Propositional logic cannot naturally talk about:

- individual objects
- variables
- general patterns over many objects
- relations between objects

For example, it cannot naturally express:

> every cat is a mammal

Why?

Because propositional logic treats each full statement as one block.
It does not break the sentence into objects and relations in a general way.

So you may end up writing many separate facts:

- `Cat(Tom) -> Mammal(Tom)`
- `Cat(Luna) -> Mammal(Luna)`
- `Cat(Milo) -> Mammal(Milo)`

That becomes repetitive very quickly.

---

## 4. First-Order Logic (FOL)

First-order logic (FOL) in artificial intelligence is a formal system that extends propositional logic by allowing the use of quantifiers and predicates, enabling the representation of complex statements about objects and their relationships. It is essential for knowledge representation, reasoning, and making informed decisions in AI systems.

First-Order Logic extends the idea by allowing us to talk about:

- objects
- predicates
- variables
- quantifiers

This makes it much more expressive than propositional logic.

In FOL, we can write:

`∀x (Cat(x) → Mammal(x))`

This means:

> for every object `x`, if `x` is a cat, then `x` is a mammal

Now one rule covers all cats.

That is much closer to how people usually state general knowledge.

---

## 5. The Two Main Quantifiers

### Universal Quantifier

`∀x`

This means:

> for all `x`

Example:

`∀x (Human(x) → Mortal(x))`

Meaning:

> every human is mortal

### Existential Quantifier

`∃x`

This means:

> there exists at least one `x`

Example:

`∃x Student(x)`

Meaning:

> there is at least one student

---

## 6. A Small School Illustration

Suppose a school wants to represent this knowledge:

- Every student in SS3 must wear an ID card.

In propositional logic, you may need many separate rules:

- `Student_Ada_SS3 -> WearsID_Ada`
- `Student_Tayo_SS3 -> WearsID_Tayo`
- `Student_Zainab_SS3 -> WearsID_Zainab`

In FOL, one rule can express the pattern:

`∀x (Student(x) ∧ InClass(x, SS3) → WearsID(x))`

This is more compact, more reusable, and easier to maintain.

---

## 7. Why FOL Mattered So Much in AI

FOL gave classical AI a way to encode general knowledge instead of only isolated facts.

That was important for:

- theorem proving
- expert systems
- planning
- knowledge bases
- language understanding research

Without this richer structure, many symbolic AI goals would have been too awkward to express.

This is one reason logic became so central in early AI thinking.

---

## 8. A Clear Comparison

### Propositional Logic

Best for:

- simple true/false facts
- small rule systems
- cases where object structure does not matter much

Weakness:

- poor at representing general rules about many objects

### First-Order Logic

Best for:

- properties of objects
- relations between objects
- reusable general statements
- richer world descriptions

Weakness:

- reasoning becomes more complex

So the tradeoff is:

> more expressive logic gives more representational power, but also brings more reasoning difficulty

---

## 9. A Note on Meaning

It is easy to write symbols.
It is harder to make sure they match the world well.

For example:

`∀x (Bird(x) → Fly(x))`

This looks neat, but it is not always true.
Penguins and ostriches are counterexamples.

So logic can be precise in form while still being wrong in content if the rule itself is too broad.

That is another lesson classical AI had to learn:

> good reasoning still depends on good knowledge

---

## 10. Key Insight

Propositional logic says:

> here are some true or false statements

First-order logic says:

> here are objects, relations, and general rules about them

That extra expressive power helped symbolic AI move from simple statements to richer world models.

---

## 11. Forward Link

But writing facts and rules is still not enough.

The next question is:

> once the knowledge is stored, how does the machine actually use it to derive conclusions?

That leads us to the next section:

**Inference Engines**.
