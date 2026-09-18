# Progress and assessment records

[progress.json](progress.json) records actual learner work and assessment evidence.
An inactive session has `current_lesson` and `next_task` both null. Maintenance
leaves those fields inactive and creates no learner attempts or assessment results.
[Historical records](history/README.md) preserve earlier evidence without assigning work.

## Lesson evidence

| Status | Meaning |
|---|---|
| not_started | The lesson has not been attempted. |
| learning | The learner is writing the program or still needs teaching/practice. |
| provisional | The learner authored a successful program with conceptual hints or references. |
| secure | The learner demonstrated independent/reference application. |
| review_needed | New evidence identifies a particular gap needing further teaching/practice. |

Record code actually written, observed behavior, explanations where relevant, and
help used. `solution` means a supplied implementation; use a fresh complete task
before treating it as learner-authored success. Preserve historical evidence
honestly rather than relabeling old assistance. Placement is not lesson evidence
and does not mark lessons complete or skip them.

## Assessments

The `assessments` list records placement, occasional quizzes, phase tests, and
reviews. Each entry contains `kind` (`placement`, `quiz`, `phase_test`, or `review`),
`performed_on`, `phase` (1–5 or null for mixed/placement work), `topics` (lesson IDs),
`needs_practice` (the subset needing further work), `support`, and `summary`.
A phase test has a phase number. In the summary, record actual multiple-choice
questions or identifiers, selected options, correct/incorrect or unfamiliar findings,
feedback, and follow-up. All quizzes and tests are multiple choice; do not collect
written explanations or coding answers as assessment responses. Placement samples
all five phases; subsequent assessments use only actually taught topics. Placement
exposure is not teaching. Record coding practice separately as lesson evidence. Empty `needs_practice` means no gap was found
in this sample, not that every related skill is mastered. For phase tests, include
all topic IDs covered by the test; do not substitute an unrelated question for the
phase's objectives. Record new assessments after they happen, never in advance.

Diagnostic placement changes the teaching/practice plan, not lesson order. Quiz,
test, and review findings guide reteaching and extra practice. When practical work
also establishes a lesson attempt, record that separately with the actual help.
A conceptual answer alone does not become completed coding work.

## Planning reviews and tests

`reviews` holds planned topic revisits with a lesson ID, due date, and reason.
Use them to plan spaced practice across topics and phases. Move/remove a due item
after completing or deliberately rescheduling it; keep completed findings in
`assessments`. Reviews are part of teaching and do not require separate permission
on every occasion. Quizzes occur occasionally at varied points, not after every lesson.

The recommender stays idle during maintenance. During an active session it calls
for initial placement when no placement record exists, follows lesson order, and
calls for an end-of-phase test after the phase's required lessons. A test showing
gaps calls for targeted teaching/practice and reassessment. Due reviews accompany
the teaching plan. Optional project suggestions do not substitute for phase tests.
The tutor selects quiz timing and questions from taught topics; this is not an
automatically administered quiz or a fixed lesson-count schedule.

## Other fields and compatibility

`environment` records only observed Codespace facts. `lessons` holds actual attempts;
`capstones` holds optional completed projects. `goals` and `notes` provide useful
context without request-history narratives. Keep public records free of private data.
Use actual dates and do not invent work to populate fields.

The two template files contain empty, inactive records. Schema 1 accepts historical
records without `assessments`; they remain readable. The validator checks consistency,
not whether the evidence really happened, and never writes records. The legacy
`--track github` option remains an alias for the same Python route.
