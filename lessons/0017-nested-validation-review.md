# Record 0017: nested validation review

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Phase 1 submission review and one placement correction |
| Previous lesson | [Record 0016](0016-not-complete-and-nested-validation.md) |
| Phase guide | [Root README](../README.md), Phase 1: Beginner (Foundations) |
| Verified repository commit | [bd0e565](https://github.com/DevilMedlar/python-training/commit/bd0e5651b7e63c1e34a2114916e3a8b70c94b68d) |
| Verified source | [reading_goals.py](https://github.com/DevilMedlar/python-training/blob/bd0e5651b7e63c1e34a2114916e3a8b70c94b68d/reading_goals.py) |
| File blob | eb4fd0a692e2fabf772d3cf9f3c1a1c0bf319681 |
| Runtime evidence | Learner's five pasted Codespace runs |
| Functional behavior | All five requested cases correct |
| Display cleanup | Both fixes complete |
| Remaining requirement | Move the boolean assignment into the outer else |
| Next submission | Revised code only; existing runs remain accepted |

**Evidence.** The learner's pasted source matches the fetched repository source. Repository inspection does not reveal unsaved or unpushed edits or the live Codespace terminal. Execution evidence below comes from the learner's transcript; the tutor did not run the program in that Codespace.

```python
days = int(input("How many days did you spend reading? "))
completed_books = int(input(f"How many books did you read in {days} day(s)? "))
both_goals_reached = completed_books >= 3 and days >= 5

if completed_books < 0 or days < 0:
    print("Counts cannot be negative.")
else:
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

| Days | Books | Observed output after prompts | Assessment |
| --- | --- | --- | --- |
| -1 | 3 | Counts cannot be negative. | Correct; no goal or reminder output |
| 5 | -1 | Counts cannot be negative. | Correct; no goal or reminder output |
| 0 | 0 | Neither goal reached; Keep working on the remaining goals.; Progress: 0 books over 0 day(s) | Correct; zero is accepted |
| 5 | 3 | Both goals reached | Correct; reminder skipped |
| 4 | 3 | One goal reached; Keep working on the remaining goals.; Progress: 3 books over 4 day(s) | Correct; both reminder lines run |

Semicolons separate distinct output lines in this table.

**Demonstrated strengths.** The learner uses or to reject either negative count and prints the error once. The classification chain and separate reminder condition are both nested correctly inside the valid-data else. Their headers align at four spaces, with their print statements at eight. Both reminder statements belong to their condition. Goal thresholds, branch order, the named boolean, not, and f-string interpolation remain correct. The workning typo is fixed and the progress line now labels books. Names and operator spacing are clear. These are successful guided demonstrations at the assigned scope, not a claim of broad mastery.

**One requirement remains.** Record 0016 explicitly required the full goal workflow, including the both_goals_reached assignment, inside the outer else. The submitted assignment is still above the outer validation condition. For these integer comparisons that is safe and does not change the requested output. It nevertheless computes goal status for negative counts before the program rejects them.

The correction is to move the existing assignment so it is the first statement inside the outer else, with four leading spaces, immediately before and aligned with if both_goals_reached. Move the line rather than duplicating it. This makes validation control the calculation as well as the decisions and printed results.

**Teaching reinforced.** An outer conditional controls execution of every statement in its selected block, including assignments. Python skips the outer else when its if condition is true. This review reinforces nesting and execution order; it introduces no new syntax.
Source checked: [Python 3.14 conditional statements](https://docs.python.org/3.14/reference/compound_stmts.html#if). The documentation is for the learner's Python 3.14 series; the last confirmed interpreter remains 3.14.2.

**Follow-up assignment in chat.** Affirm the five correct runs and the two wording fixes. Explain the single placement difference without calling the program's output incorrect. Ask the learner to make the move, save, and send the revised code. Do not provide the finished solution, request predictions, repeat all five runs, or require a Git synchronization step. The corrected placement can be verified from the next pasted source.

**Status and uncertainty.** This record supersedes the awaiting-submission and pending-display-cleanup status in 0016. The five runtime cases and display fixes are now accepted; complete containment of the goal workflow awaits the one-line move. No other mistake is observed. Both inputs preceding validation follows the assignment even when a negative day count appears in the second prompt. Recovery from non-integer text was not assigned and remains Phase 2. Do not invent a relationship constraint between books and days.

**Resume state.** Review the next source for assignment placement and use within the valid branch. Once confirmed, close this extension and consult the current tracker/root phase outline before teaching bounded numeric ranges and comparison chaining, the next direction recorded in 0016. Those topics have not been taught by this review and stay in remaining coverage. Do not repeat the successful and/or/not lessons. Preserve the learner's practice of receiving teaching here in chat and writing their own exercise files.

**Record maintenance.** Add this record and its purpose to lessons/README.md and replace its current checkpoint. No remaining-coverage item is removed because no new topic was taught. Preserve prior numbered records, the root outline, and learner Python files. The next record number is 0018.
