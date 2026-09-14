# Placement and resumption

Placement locates a useful starting task. It is not a certificate, personality
test, or a reason to delay useful teaching. Ask one task at a time. If the learner
declares no experience, start at `P1-01` and guide the first edit, commit, and Actions run in the browser.

## Brief intake

Use already available answers: What would the learner like to build? What have
they built without an exact tutorial? How much time do they have today? Python runs on GitHub Actions; that environment is already decided. Ask about access needs when relevant. Do not collect unrelated personal data.

## Adaptive tasks

| Entry point | Task | Observe | Route if a gap appears |
|---|---|---|---|
| P1 foundations | Trace `x = 3`, `y = x + 2`, `x = 10` | Does `y` remain 5, with a correct explanation? | P1-02 |
| P1 control/data | Count values at least 10 in `[4, 10, 15]`, then `[]` | Loop, condition, initialization, empty case | P1-05 through P1-07 |
| P1 functions | Return an average or `None` for empty input | Contract, return versus print, boundary | P1-08 |
| P1 debugging/files | Explain how to load valid duration JSON without overwriting malformed history | Parse/schema distinction and error handling | P1-10 through P1-12 |
| P2 readiness | Build a CSV topic aggregator with tests | Quoting, validation, duplicates, no partial success, pure calculation | Relevant P2 lessons |
| P3 readiness | Explain and repair a growing task list behind a semaphore | Bounds, ownership, cancellation, actual failure checks | P3-06 and P3-07, or earlier prerequisites |
| P4 readiness | Critique a speed comparison from one dataset and one timing | Units, baseline, uncertainty, scope, reproducibility | P4-01 through P4-04 |
| P5 readiness | Defend a small contribution against existing alternatives | Value, evidence, compatibility, novelty limits | P5-01 through P5-03 |

The first row is a short verbal trace, not a demand to copy three statements into
one line. The advanced rows are only for learners whose previous work supports
trying them. Stop after enough evidence to choose an immediate lesson, usually
two or three tasks rather than this entire table.

## Scoring a task

Sample the GitHub action attached to the same Python task: identify its committed
file and run, inspect its diff, or explain its PR. Teach missing browser controls
within that Python lesson. Do not conduct separate GitHub placement or require
GitHub mastery before the first Python program.

Record `pass` or `retry`, the actual response, and support used. Use `none` for
independent work, `reference` for allowed documentation/accommodations, `hint`
for conceptual assistance, and `solution` when the answer or a modeled decisive
step was supplied. A syntax lookup may be an allowed reference; a generated
implementation is solution assistance. Ask what help was used when it matters.

Do not infer competence in every preceding lesson from a single successful
advanced task. Record the objectives actually demonstrated. Equivalent prior
work can satisfy a prerequisite when its relevant behavior and explanation are
inspected; otherwise label it unconfirmed and sample it during learning.

Use explicit learning goals to tailor the route. A working developer seeking
testing help need not start with arithmetic. A research specialist may need a
targeted gap repair in packaging. Document the tailored prerequisites rather
than inventing a global “expert” score.

## Resume after a gap

Read the latest record and ask one short retrieval question from the current
lesson or a due review. If the record is unavailable, request it or reconstruct
only what the learner reports, with that uncertainty noted. A later failure
changes that skill to `review_needed`; it does not erase unrelated achievements.
