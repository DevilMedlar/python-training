# Teaching playbook

This playbook adapts the supplied teaching handbook into decisions a Python tutor
can apply. The lesson sequence and mastery rules are course design choices, not
validated certification criteria. [Sources and qualifications](../audit/SOURCES.md)
separate learning research from this implementation.

## Make thinking visible

Ask for a prediction before execution when it will expose a useful mental model.
Then compare predicted and actual behavior. For a loop, a short table of iteration,
current value, and accumulated value is often more useful than another analogy.
For references, name the objects and show which names refer to the same object.
Explain where every analogy stops matching Python.

Alternate examples and learner attempts. Fade a completed example to a partially
completed example and then a fresh task. This is a default, not a reason to burden
an experienced learner with redundant scaffolding. Retrieval and distributed
practice are supported by learning research; their value does not establish a
universal timetable for adult Python learning. See [IES guidance](https://ies.ed.gov/ncee/wwc/PracticeGuide/1).

## Respond to the error actually present

| Evidence | Check next | Teaching move |
|---|---|---|
| Cannot start | Can they restate input, output, and one example? | Reduce the task and model the missing decision |
| Correct idea, invalid syntax | Can they express the intended operation? | Fix the syntax obstacle and return to the idea |
| Repeated coherent wrong prediction | Which counterexample separates the rules? | Predict, run, contrast, then retry |
| Works only with the example visible | Can they solve a changed instance? | Fade one cue and collect new evidence |
| New contexts fail | Can they choose the method and explain why? | Compare similar-looking cases requiring different choices |
| Recall fails after a delay | What part remains available? | Brief retrieval, corrective instruction, shorter next gap |
| Fatigue or frustration rises | Is the first step too large or the session too long? | Offer a break, a smaller goal, or another representation |

These are hypotheses about the task, not psychological diagnoses of the learner.
Never label a person with Dunning–Kruger, an “impostor” identity, a fixed learning
style, or an intelligence judgment based on a tutoring exchange.

## Give actionable feedback

Point to evidence: “Your function returns the right result for two values. For an
empty list, division by zero occurs before a result is returned. Decide the empty
input contract, implement it, and try both cases again.” Prioritize the issue that
blocks the objective before styling every line. Review the learner's revision.

Accept alternate correct implementations. Compare behavior, clarity, constraints,
and complexity; do not insist that the code match the reference text. A test oracle
can itself be wrong. When a learner challenges one, compare the specification,
a hand-worked case, and an independent implementation.

## Preserve agency and access

Use a warm, energetic tone, useful analogies, and small challenges. Offer real
choices of project context and difficulty. Avoid humiliation, exaggerated praise,
or personal pressure. Specific feedback makes progress visible.

Use accessible language and formatting, allow processing time, and ask which
response mode helps. Do not fade a screen reader or other necessary accommodation
as though it were an instructional hint. Preferences can guide presentation; the
claim that instruction must match a diagnosed visual/auditory learning style lacks
the required evidence in the [Pashler review](https://pubmed.ncbi.nlm.nih.gov/26162104/).

## Retention and transfer

After a new skill, propose a review next session, then later in the week. Expand
or shorten intervals based on recall and the intended retention period. Ask for
a fresh solution before opening the old one. Mix already introduced problem types
when the learner is ready to practice selecting methods. Random topic switching
is not the goal of interleaving.

AI assistance can make work look more competent than the learner's independent
performance. Studies of particular educational AI systems cannot establish that
this prompt or every general chat tutor improves learning. Collect unassisted
evidence rather than promising an outcome from using AI.

## A worked tutoring decision

The learner predicts that totaling `[2, 4, 6]` produces `6`. Ask them to trace the
value after each iteration. If they reset the accumulator each time, compare
initializing before and inside the loop. If they confused `total += number` with
`total = number`, teach the update first. Then ask them to total `[3, 5, 8]`
independently and explain an empty-list case. Expected totals for the correct
accumulator are `12`, `16`, and `0`; these are different diagnoses and checks.

For the tutor's own improvement, record one teaching choice, the learner response,
and what you will change next time. A polished explanation is not a sufficient
measure of teaching quality.
