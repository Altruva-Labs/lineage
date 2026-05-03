# Chapter 2.3.2: Constraint Satisfaction Problems (CSPs)


In the last section, we improved search by guiding it with heuristics.

But that still leaves another kind of problem:

> some problems are not mainly about finding a path  
> they are mainly about finding a valid assignment

This is where **Constraint Satisfaction Problems (CSPs)** come in.

---

## 1. The Main Idea

In a CSP, we want to assign values to variables in a way that obeys all the rules.

So instead of asking:

> "How do I move from start to goal?"

we ask:

> "How do I fill in all required choices without breaking any constraint?"

---

## 2. The Basic Form of a CSP

A CSP usually has three parts:

- **Variables**: the things we need to decide
- **Domains**: the possible values for each variable
- **Constraints**: the rules that limit which combinations are allowed

We can write this simply as:

`CSP = (X, D, C)`

Where:

- `X = {X_1, X_2, ..., X_n}` is the set of variables
- `D = {D_1, D_2, ..., D_n}` gives the domain of each variable
- `C` is the set of constraints

The goal is to find an assignment:

`X₁ = v₁, X₂ = v₂, ..., Xₙ = vₙ`

such that **all constraints are satisfied**.

---

## 3. A Simple Example: School Timetable

Suppose a school wants to create a timetable.

Variables:

- `Math_Time`
- `English_Time`
- `Physics_Time`

Domains:

- Monday 9am
- Monday 11am
- Tuesday 9am

Constraints:

- Math and Physics cannot be at the same time
- A teacher cannot teach two classes at once
- A classroom cannot hold two classes at the same time

Now the task is not really a path search.
It is an assignment problem.

We must fill in the slots so that the final arrangement is valid.

That is the spirit of a CSP.

---

## 4. Other Common Examples

Classical AI used CSPs for many structured problems, such as:

- map coloring
- Sudoku
- timetabling
- scheduling
- resource allocation
- circuit design

The pattern is always similar:

- choose values
- obey rules
- reject illegal combinations

---

## 5. Map Coloring Example

Imagine we want to color regions on a map.

Variables:

`{WA, NT, SA, Q, NSW, V, T}`

Domains:

`{red, green, blue}`

Constraint example:

`WA ≠ NT, WA ≠ SA, NT ≠ SA`

This means neighboring regions must not share the same color.

The goal is to assign a color to each region so that every neighboring pair has different colors.

This is one of the standard examples because it makes the idea very easy to see.

---

## 6. Why CSPs Matter

CSPs showed that many intelligence problems are really about **structured choice under rules**.

That matters because it expands the classical AI view:

- not all reasoning is theorem proving
- not all problem solving is shortest-path search
- some problems are about satisfying many interacting conditions at once

This was a big deal in planning, scheduling, robotics, and operations research.

---

## 7. Solving a CSP with Backtracking

The most common classical method is **backtracking search**.

The idea is simple:

1. Pick a variable.
2. Try one value from its domain.
3. Check whether any constraint is already broken.
4. If not, continue.
5. If a contradiction appears, go back and try another value.

This is called backtracking because the search moves backward after a bad choice.

### Tiny Illustration

Suppose:

- `A` can be `1` or `2`
- `B` can be `1` or `2`
- constraint: `A != B`

Try:

- `A = 1`
- `B = 1`

This fails, because `A != B` is broken.

So we backtrack and try:

- `B = 2`

Now the assignment works.

---

## 8. Why Plain Backtracking Can Be Slow

Backtracking is correct, but it can still waste a lot of time.

Why?

Because it may go far into a bad partial assignment before discovering failure.

So classical AI added smarter techniques.

This is where heuristics appear again, but in a new form.

---

## 9. Useful CSP Heuristics

Two famous heuristics are:

### Minimum Remaining Values (MRV)

Choose the variable with the fewest legal values left.

Why?

Because if a variable is likely to cause trouble, it is better to face that trouble early.

### Least Constraining Value (LCV)

Choose the value that rules out the fewest options for the remaining variables.

Why?

Because that gives the rest of the search more freedom.

So even inside CSPs, the idea of heuristic guidance comes back.

---

## 10. Constraint Propagation

Another major idea is **constraint propagation**.

Instead of waiting until the end to discover contradictions, we use the constraints early to shrink the domains.

For example:

- if `WA = red`
- and `WA` touches `NT`

then `NT` can no longer be `red`

This removes bad choices early.

That can save a lot of search.

---

## 11. Arc Consistency

One important propagation idea is **arc consistency**.

For a binary constraint between variables `X` and `Y`, the arc `X -> Y` is consistent if:

> for every value in the domain of `X`, there is at least one allowed value in the domain of `Y`

If not, the unsupported value can be removed.

In simple form:

`∀x ∈ D_X, ∃y ∈ D_Y such that (x, y) satisfies the constraint`

If a value of `X` has no supporting value in `Y`, delete it.

This does not solve every CSP by itself.
But it often detects failure much earlier.

---

## 12. Path View vs Assignment View

This is the main difference from earlier chapters:

- search problems care a lot about the path
- CSPs care mainly about the final assignment

In many CSP formulations, every complete assignment has the same depth:

- assign variable 1
- assign variable 2
- assign variable 3
- ...

So the structure of the problem is different.

This is why CSPs deserve their own treatment inside classical AI.

---

## 13. Why CSPs Felt Powerful

CSPs gave classical AI a clean language for expressing many real-world tasks.

Instead of writing one special solver for every problem, you could describe:

- the variables
- the domains
- the constraints

Then use a general CSP solver.

That is the same dream we saw earlier in search:

> define the problem formally once, then solve it with a reusable algorithmic framework

---

## 14. But the Limits Remain

CSPs are powerful, but they are still classical AI.

They still depend on:

- explicit variables
- explicit domains
- explicit rules
- human-made formulations

They do not learn the constraints from data.
They do not generalize by experience.
They do not naturally handle messy uncertainty.

So they extend classical AI, but they do not escape its core limitations.

---

## 15. Why This Section Matters in the Lineage

This section is important because it shows a broader view of problem solving:

- heuristic search taught us guided navigation through state spaces
- CSPs teach us structured assignment under constraints

Both are still forms of symbolic problem solving.

Both are still rooted in explicit knowledge.

Both prepare us for the next step:

> planning, where an agent must choose an action sequence that changes the world from its current state to a desired goal state

That is where we go next.
