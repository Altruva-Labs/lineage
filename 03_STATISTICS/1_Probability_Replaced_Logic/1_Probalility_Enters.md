# Chapter 3.1.1: Probability Enters: Reasoning Under Uncertainty

The last part of the mathematics chapter ended at a hard limit:

> rules and logic were useful, but the real world was too noisy and incomplete for all-or-nothing reasoning alone

That is the doorway into statistics.

Classical logic works well when statements are crisp:

- true
- false

Example:

- "The light is on."
- "The door is closed."

But many AI problems are not that clean.

Examples:

- A sensor may misread an object
- A patient may have a symptom that suggests many diseases
- A robot action may work most of the time, not all the time
- A message may look like spam, but not with certainty

In cases like these, AI needs more than truth.
It needs **degrees of belief**.

That is what probability provides.

Instead of saying:

> "This is definitely true."

AI can now say:

> "This is likely true."

or

> "I believe this with 80% confidence."

This was a major shift.

Logic asks:

> what follows if the facts are exact?

Probability asks:

> what should I believe when the facts are incomplete or noisy?

### Small Illustration

Suppose a room sensor says there is smoke.

Pure logic may try to use a rule like:

`SmokeSensorOn -> Fire`

But that rule is brittle.
The sensor may be faulty.
Steam may trigger it.

Probability allows a softer statement:

`P(Fire | SmokeSensorOn) = 0.7`

Now the system can reason more carefully.

This is why probability did not just add a new tool.
It changed the style of reasoning itself.

AI was moving from:

- certainty

to:

- uncertainty
- belief
- evidence

That change makes the rest of this chapter possible.

Next, we make that shift more precise through the **Bayesian view of intelligence**.
