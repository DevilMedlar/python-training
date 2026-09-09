# Record 0018: nesting complete and comparison chaining

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Placement correction accepted and Phase 1 range lesson |
| Previous record | [0017](0017-nested-validation-review.md) |
| Phase guide | [Root README](../README.md), Phase 1: Beginner (Foundations) |
| Verified repository commit | [0187fbf](https://github.com/DevilMedlar/python-training/commit/0187fbfe5a02b8b1b6470b1a3a6de397a6777b6b) |
| Verified source | [reading_goals.py at this commit](https://github.com/DevilMedlar/python-training/blob/0187fbfe5a02b8b1b6470b1a3a6de397a6777b6b/reading_goals.py) |
| Source blob | 536f08211c8afbe4fa45d97c667b6bfba1a4d7da |
| Evidence | Current pasted learner source and matching repository file; prior five runs retained |
| Nested-validation exercise | Complete at the assigned scope |
| New lesson | Bounded numeric ranges, chained comparisons, endpoint inclusion |
| New assignment | practice_session.py with a negative guard and a 20–40 inclusive target |
| Assignment status | Taught and issued in this turn; awaiting code and five boundary runs |

**Evidence and correction review.** The learner supplied revised code only, as requested in 0017. The repository source matches the submission and its blob matches the pinned commit tree. The tutor inspected source rather than executing the learner's Codespace. No new runtime evidence was requested or claimed.

```python
days = int(input("How many days did you spend reading? "))
completed_books = int(input(f"How many books did you read in {days} day(s)? "))

if completed_books < 0 or days < 0:
    print("Counts cannot be negative.")
else:
    both_goals_reached = completed_books >= 3 and days >= 5
    if both_goals_reached:
        print("Both goals reached")
    elif completed_books >= 3 or days >= 5:
        print("One goal reached")
    else:
        print("Neither goal reached")
        
    if not both_goals_reached:
        print("Keep working on the remaining goals.")
        print(f"Progress: {completed_books} books over {days} day(s)")
```

The both_goals_reached assignment is now the first statement inside the outer else, indented four spaces and before its uses. The classification and separate reminder if are at that same level; their print statements are nested one level deeper. Thus the negative-count branch skips the entire goal workflow, including the assignment. The existing and/or/not logic, nonnegative boundary, f-strings, names, operator spacing, and two wording fixes remain correct.

The five runs accepted in 0017 remain evidence for the existing behavior: (-1 days, 3 books) and (5 days, -1 books) produce only the negative message; (0, 0) produces neither plus reminder/progress; (5, 3) produces both only; (4, 3) produces one plus reminder/progress. The current change is verified through source placement and does not require a repeated five-case submission.

**Resolved status.** This supersedes the pending-assignment-placement status in 0017. The nested-validation extension is complete at the assigned scope. No material issue remains. A whitespace-only blank line is not a reason to delay completion or ask for another edit. Successful guided nesting is demonstrated; do not infer universal mastery or invent untested weaknesses.

**Lesson and assignment delivered in chat.**

Next is **comparison chaining and bounded ranges**.

Sometimes a number must meet a lower limit and an upper limit. For example:

```python
12 <= temperature <= 18
```

This is a **chained comparison**. For this numeric variable, it has the same result as:

```python
12 <= temperature and temperature <= 18
```

Both comparisons must be true. Read it as “temperature is at least 12 and at most 18.”

```python
temperature = 15
within_range = 12 <= temperature <= 18
print(within_range)
```

This prints `True`: 15 meets both limits. The middle expression is evaluated once; if the first comparison fails, Python skips the second. [Python comparison chaining](https://docs.python.org/3.14/reference/expressions.html#comparisons)

The operators determine whether the endpoints count:

| Expression | Allowed values |
| --- | --- |
| `12 <= temperature <= 18` | 12 through 18, including both endpoints |
| `12 < temperature < 18` | Greater than 12 and less than 18; both endpoints excluded |
| `12 <= temperature < 18` | Includes 12, excludes 18 |

“Inclusive” means the endpoint is included. You can use variables for the limits too.

To check whether a value is **outside** the inclusive range, either side is enough: `temperature < 12 or temperature > 18`.

**Your work: create `practice_session.py`.**

For this exercise, the target practice duration is **20 through 40 minutes, inclusive**.

1. Ask for an integer number of minutes using `int(input(...))`.
2. Use an outer `if`/`else` to reject negative minutes.
3. Inside the valid-data `else`, use one `if`/`elif`/`else` chain to classify the duration.
4. Use a **chained comparison** for the within-target condition. Choose the branch order yourself.

| Minutes | Required message |
| --- | --- |
| Negative | `Minutes cannot be negative.` |
| 0 through 19 | `Below target` |
| 20 through 40 | `Within target` |
| Above 40 | `Above target` |

Print one result message per run. Use meaningful names and four spaces per indentation level.

Save and run:

```bash
python3 practice_session.py
```

Run it with **-1, 19, 20, 40, and 41**. These check negative input, both endpoints, and just outside each endpoint.

Send your **code and actual outputs**.


**Teaching scope and review criteria.** The new topic builds on comparisons and and/or already taught, and the nested assignment reuses newly demonstrated structure. Check that negative values take only the outer error path, zero is classified below target, the within-target check is chained, both endpoints are included, and the three valid classifications are mutually exclusive. Permit any correct branch order that includes the explicit chained within-target condition. Variable names and literal versus named bounds are learner choices. Only one classification line should appear after the prompt.

Boundary evidence for the new assignment is expected as follows:

| Input minutes | Expected output after prompt |
| --- | --- |
| -1 | Minutes cannot be negative. |
| 19 | Below target |
| 20 | Within target |
| 40 | Within target |
| 41 | Above target |

These five cases exercise the negative guard and each side of both target boundaries. They do not establish all possible runtime behavior. No predictions, extra old-case reruns, or Git synchronization step are assigned. No loops, functions, collections, or exception handlers are needed. The duration limits are fictional exercise rules, not a recommendation for study duration. Non-integer conversion recovery remains Phase 2.

**Topics introduced versus demonstrated.** Chained numeric comparisons, lower and upper range limits, inclusive/exclusive endpoints, a mixed endpoint example, evaluation-once/short-circuit semantics, and an outside-range or condition are explained in this lesson. The new chained-comparison exercise awaits learner evidence; exclusive and mixed bounds have examples but no independent learner demonstration. The completed reading-goals source demonstrates the placement correction and retains earlier behavior; do not confuse it with evidence for chained comparisons.

**Sources.** [Python 3.14 expression reference: comparisons](https://docs.python.org/3.14/reference/expressions.html#comparisons), checked in this turn. The learner's last confirmed interpreter is 3.14.2; the documentation currently describes the 3.14 series. Indentation conventions and compound-statement semantics are carried forward from 0016/0017 rather than taught as new syntax.

**Resume state.** Review practice_session.py and the five runs. Resolve any observed errors, preserving prior accepted work. After successful practice, consult the current coverage; mixed boolean-operator grouping/precedence is a possible next Phase 1 topic, with a focused later variation on mixed or exclusive interval endpoints. Truthiness, non-boolean and/or behavior, strings/further formatting, numeric details, loops and repeated prompts remain. No further topic is assigned by this note.

**Record maintenance.** Add 0018 to the Foundation Record/Purpose index and update the current checkpoint. Remove comparison chaining and upper/combined input bounds from remaining-to-teach coverage because they are introduced here; preserve pending exercise status and untested endpoint variants in this record. Preserve all earlier numbered records, the root README, and learner Python files. The next record is 0019.
