# Chapter 2.3.3: Planning as Search (STRIPS, PDDL)


We have now seen two major ideas:

- search through a state space
- assign values under constraints

Planning brings these ideas together in a very practical way.

In planning, the question is:

> given the current world and a desired goal,  
> what sequence of actions will get us there?

This is one of the most important ideas in classical AI.

---

## 1. What Planning Means

A **plan** is an ordered sequence of actions meant to achieve a goal.

If the current state is `s_0`, and the goal is some target condition, then planning asks us to find:

`a₁, a₂, a₃, ..., a_k`

such that applying those actions transforms the world from the start state into a goal state.

In short:

`s₀ --a₁→ s₁ --a₂→ s₂ --a₃→ ... --a_k→ s_k`

where `s_k` satisfies the goal.

So planning is deeply connected to search.

The planner is searching over possible action sequences.

---

## 2. Real-World Illustration: Getting Ready for School

Suppose the goal is:

> "Be ready and arrive at school."

The actions may include:

- wake up
- bathe
- wear uniform
- eat breakfast
- leave home
- enter school

Some actions depend on others:

- you cannot wear your uniform before finding them
- you cannot leave home before getting ready
- you cannot enter school before traveling there

That means planning is not just about listing actions.
It is about respecting the logic of the world.

---

## 3. Why Planning Was Important in Classical AI

Planning mattered because early AI did not want machines to only react.

It wanted them to:

- reason ahead
- choose action sequences
- achieve explicit goals

This made planning central in:

- robotics
- logistics
- manufacturing
- scheduling
- automated control

Planning gave classical AI a way to connect reasoning to action.

---

## 4. The Basic Planning Structure

A planning problem usually contains:

- an **initial state**
- a **goal description**
- a set of **actions**

Each action changes the state of the world.

So, just like earlier search chapters, planning uses:

- states
- transitions
- goals

But now the transitions are described more carefully in terms of what actions require and what they change.

---

## 5. STRIPS

One of the most influential early planning formalisms was **STRIPS**.

The original STRIPS system appeared in the early 1970s and became a major reference point in classical planning.

In STRIPS-style planning, each action is usually described with:

- **preconditions**
- **add effects**
- **delete effects**

### Meaning

- **Preconditions**: what must already be true before the action can happen
- **Add effects**: what becomes true after the action
- **Delete effects**: what stops being true after the action

This gave AI a very clean way to represent actions.

---

## 6. Simple STRIPS Example

Suppose a robot wants to pick up a book from a table.

Action:

`PickUp(Book)`

Preconditions:

- `OnTable(Book)`
- `HandEmpty`

Add effects:

- `Holding(Book)`

Delete effects:

- `OnTable(Book)`
- `HandEmpty`

So the action can only happen if the book is on the table and the robot's hand is free.

After the action:

- the robot is holding the book
- the book is no longer on the table
- the hand is no longer empty

This is a very simple idea, but it was powerful because it made action change explicit.

---

## 7. Planning as Search

Once actions are formally defined, planning becomes a search problem.

We can think of it like this:

- nodes = world states
- edges = actions
- goal = desired world condition

So the planner searches for a path through the state space:

`state → action → new state`

This is why the title says **Planning as Search**.

The planner is not doing magic.
It is searching through possible futures.

---

## 8. State-Space Search and Plan-Space Search

There are different ways to think about planning.

Two common ones are:

### State-Space Search

Search directly through world states.

Example:

- start with the current state
- apply possible actions
- keep going until the goal condition is true

### Plan-Space Search

Search through partial plans.

Instead of expanding only states, the system reasons about unfinished action sequences and their requirements.

For this chapter, the main point is simple:

> planning can be formulated and solved as search

---

## 9. PDDL

As planning research grew, there was a need for a common language for describing planning problems.

That led to **PDDL**, the **Planning Domain Definition Language**.

PDDL was introduced in the late 1990s to help standardize how researchers described:

- domains
- actions
- objects
- goals
- problem instances

This was important because it allowed planners to be compared on shared benchmark problems.

So PDDL did for planning what a standard file format does for software tools:

it made reuse and comparison easier.

---

## 10. Tiny PDDL-Style Intuition

A planning domain usually says things like:

- what kinds of objects exist
- what actions are available
- what each action needs
- what each action changes

A planning problem then says:

- what objects are present in this case
- what the initial state is
- what goal we want

So we can think of it as:

- **domain file** = general world rules
- **problem file** = one specific task in that world

That separation was very useful in robotics and automated planning research.

---

## 11. Example: Delivering a Package

Imagine a delivery robot.

Initial state:

- robot is in Room A
- package is in Room A
- Room B is the destination

Goal:

- package is in Room B

Possible actions:

- `PickUp(package)`
- `Move(RoomA, RoomB)`
- `Drop(package)`

A valid plan could be:

1. `PickUp(package)`
2. `Move(RoomA, RoomB)`
3. `Drop(package)`

This example looks simple, but it captures the main planning idea:

> represent actions formally, then search for a sequence that reaches the goal

---

## 12. Why Planning Looked So Powerful

Planning was one of the strongest expressions of the classical AI dream.

Why?

Because it suggested that if we:

- describe the world clearly enough
- define actions correctly enough
- specify the goal precisely enough

then a machine can reason out what to do.

That is a bold and beautiful idea.

And in structured environments, it works surprisingly well.

---

## 13. But Planning Also Exposed the Limits

Planning systems usually assumed things like:

- the world is known
- actions are clearly defined
- effects are mostly predictable
- goals are explicitly stated

Those assumptions are acceptable in tidy settings.

But real life is often messier:

- information is incomplete
- the world changes unexpectedly
- action outcomes may be uncertain
- humans do not always state goals in formal logic

So planning was powerful, but fragile outside well-structured worlds.

---

## 14. Why This Section Matters in the Lineage

Planning matters because it pushed classical AI toward real action.

We started with:

- representing states
- searching through states
- guiding search with heuristics
- solving assignments with constraints

Planning now turns all that into:

> goal-directed action over time

This is one of the clearest ancestors of modern agents.

But classical planning still depends on hand-built world models and hand-written action rules.

That becomes a serious problem at scale.

---

## 15. What Comes Next

At this point, the pressure is becoming impossible to ignore.

Classical systems can:

- search
- use heuristics
- satisfy constraints
- build plans

But they still struggle with:

- scale
- uncertainty
- brittleness
- hand-crafted intelligence

That breaking point is the subject of the next chapter.
