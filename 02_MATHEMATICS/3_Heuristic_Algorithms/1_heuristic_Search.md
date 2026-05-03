# Chapter 2.3.1: Heuristic Search

In Chapter 2.2, we saw something important:

- BFS is systematic, but memory-heavy
- DFS is lighter on memory, but can go deep in the wrong direction
- UCS respects cost, but it can still explore too many states

So a new question appears:

> Can search be guided by a useful guess?

That question leads us to **heuristic search**.

This is one of the clearest moments in classical AI where search starts to look more intelligent.

Not because the machine is learning.
Not because it understands the world deeply.
But because it is no longer exploring blindly.

---

## 1. What a 'Heuristic' Is

A **heuristic** is a rule of thumb.

It is a practical estimate that helps the algorithm decide which states look more promising.

We usually write a heuristic as:

`h(n) ≈ estimated cost from node n to a goal`

Where:

- `n` is the current node or state
- `h(n)` is the estimated remaining cost

The word "estimate" matters.

A heuristic does not need to know the exact answer.
It only needs to give the search a better sense of direction than blind search.

---

## 2. Simple Real-World Illustration

Imagine you are in a city and want to get to a hospital.

Blind search behaves like this:

- "Let me try roads one by one."
- "Let me keep expanding possibilities until I find it."

Heuristic search behaves like this:

- "The hospital is probably closer in the north-east direction."
- "Let me prefer roads that seem to move me closer."

You still do not know the full best route.
But you now have guidance.

That guidance can save a huge amount of time.

---

## 3. Why Heuristics Mattered in Classical AI

This was a big step because many classical AI problems had enormous search spaces:

- route finding
- puzzle solving
- game playing
- planning

Pure search was often too slow.

So researchers began adding domain knowledge into the search process itself.

That is what a heuristic really is:

> human knowledge injected into search as a guiding estimate

This made systems look smarter, faster, and more focused.

But it also introduced a hidden cost that we will return to later:

- heuristics often had to be hand-designed
- good heuristics were problem-specific
- what worked in one domain often failed in another

---

## 4. Two Important Scores: `g(n)` and `h(n)`

To understand heuristic search well, keep these two ideas separate:

`g(n) = cost from the start node to n`

`h(n) = estimated cost from n to the goal`

So:

- `g(n)` looks backward at cost already paid
- `h(n)` looks forward at estimated cost still left

Different search methods combine these in different ways.

---

## 5. Greedy Best-First Search

One simple heuristic method is **Greedy Best-First Search**.

It chooses the node with the smallest:

`f(n) = h(n)`

That means it only asks:

> "Which state looks closest to the goal right now?"

This can be very fast.
But it can also be careless.

Why?

Because it ignores the cost already spent.

So Greedy Best-First Search may rush toward something that looks near, even if the path to get there is expensive or misleading.

---

## 6. A* Search

The most famous heuristic search method is **A\***.

It combines:

- the real cost so far
- the estimated cost remaining

Its evaluation function is:

`f(n) = g(n) + h(n)`

This is the central formula of A\*.

It means:

- `g(n)` keeps the search honest
- `h(n)` keeps the search focused

So A\* does not behave like UCS alone,
and it does not behave like Greedy search alone.

It balances both.

---

## 7. A Small Example

Suppose you want to move from `S` to `G`.

You currently have two frontier nodes:

- Node `A`: `g(A) = 3`, `h(A) = 4`
- Node `B`: `g(B) = 5`, `h(B) = 1`

Then:

`f(A) = g(A) + h(A) = 3 + 4 = 7`

`f(B) = g(B) + h(B) = 5 + 1 = 6`

A\* will prefer `B`, because `f(B)` is smaller.

Even though `B` already cost more to reach, its remaining route appears much shorter.

This is the key idea:

> A\* chooses the node with the best estimated total path cost

---

## 8. A Familiar Illustration: School Trip

Imagine a student is walking from home to school.

There are many roads.

- `g(n)` is how much distance the student has already walked
- `h(n)` is the guessed distance left to school
- `f(n)` is the guessed full trip length

If one road is cheap so far but still far from school, and another road is a bit more costly so far but much closer to school, A\* compares both using:

`f(n) = g(n) + h(n)`

That is why A\* is often more practical than plain UCS.

---

## 9. When A* Is Guaranteed to Work Well

Two ideas matter a lot here:

- **admissibility**
- **consistency**

### Admissibility

A heuristic is **admissible** if it never overestimates the true remaining cost.

If `h^*(n)` means the true minimum cost from `n` to a goal, then:

`h(n) ≤ h^*(n)`

for every node `n`.

In simple words:

> the heuristic may be too low, but it must not be too high

When this holds, A\* is guaranteed to find an optimal solution in tree search.

### Consistency

A heuristic is **consistent** if it obeys a triangle-like rule:

`h(n) ≤ c(n, a, n') + h(n')`

Where:

- `c(n, a, n')` is the step cost from `n` to successor `n'`

This means:

> your estimate at the current node should not be greater than
> one step of real cost plus the estimate from the next node

Consistency implies that the `f(n)` values do not decrease along a path.

In graph search, this is very useful because it avoids needless re-expansion in the standard version of A\*.

---

## 10. What Makes a Good Heuristic

A good heuristic should be:

- easy to compute
- close to the true remaining cost
- safe enough not to break the guarantee you need

There is a tradeoff here:

- a weak heuristic is safe, but not very helpful
- a strong heuristic is very helpful, but harder to design

At one extreme:

`h(n) = 0`

for all `n`.

If we use that in A\*, then:

`f(n) = g(n)`

So A\* becomes Uniform-Cost Search.

That shows something important:

> heuristic search does not replace earlier search methods
> it generalizes them

---

## 11. Where Heuristics Come From

In classical AI, heuristics were often built from:

- geometry
- domain shortcuts
- relaxed versions of the original problem
- expert knowledge

Example:

If you are solving the 8-puzzle, a useful heuristic is:

- number of misplaced tiles

An even better one is:

- Manhattan distance, which adds how far each tile is from where it belongs

These do not solve the puzzle directly.
They simply tell the search which states look more promising.

---

## 12. Simple A* Procedure

1. Put the start node into a priority queue.
2. Give it priority using `f(n) = g(n) + h(n)`.
3. Repeatedly remove the node with the smallest `f(n)`.
4. If it is the goal, return the solution.
5. Otherwise, expand it and compute scores for its successors.
6. Continue until the goal is found or no nodes remain.

In simplified pseudocode:

```text
A*(start, goal):
    frontier = priority queue ordered by f(n)
    put start in frontier with g(start) = 0

    while frontier is not empty:
        n = remove node with smallest f(n)

        if n is goal:
            return solution

        for each successor n' of n:
            compute g(n')
            compute f(n') = g(n') + h(n')
            add or update n' in frontier
```

---

## 13. Why This Felt Like Intelligence

To people building early AI systems, heuristic search looked powerful because it resembled skilled human problem-solving.

Humans rarely search every option.
We use shortcuts like:

- "this road feels closer"
- "that move looks bad"
- "this arrangement seems more promising"

Heuristic search copied that style in algorithmic form.

So this was one of the first strong examples of:

> intelligence as guided search over a structured space

Still, we must be precise:

This was not learning.
The system was not discovering its own heuristic from data.
In most cases, the heuristic was still designed by a human.

---

## 14. The Hidden Cost of Heuristic Search

Heuristics improved search, but they did not remove the deeper weakness of classical AI.

They were often:

- hand-crafted
- brittle
- domain-specific
- hard to transfer

A very good chess heuristic does not suddenly become a good hospital scheduling heuristic.

So heuristic search was a major improvement.
But it was not yet a general answer.

---

## 15. Why This Section Matters in the Lineage

This section is important because it shows the next layer after uninformed search:

- first, AI represented states and actions
- then, AI searched those spaces blindly
- now, AI adds informed guidance

That is a real advance.

But the method is still fully classical:

- explicit states
- explicit costs
- explicit rules
- explicit human guidance

No learning has happened yet.

---

## 16. What Comes Next

Heuristic search still assumes that many problems can be treated as path-finding through states.

But not every problem looks like a path.

Some problems are really about assigning values while obeying rules.

That brings us to the next chapter:

> **Constraint Satisfaction Problems (CSPs)**  
> where the main issue is not "Which path should I follow?"  
> but "Which assignment satisfies all the constraints?"
