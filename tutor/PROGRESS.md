# Progress without extra homework

[progress.json](progress.json) records the Python work actually completed, help
used, and an agreed next task. No lesson is active until the learner asks to
begin. [Historical records](history/README.md) do not assign current work.

[progress-template.json](progress-template.json) and
[github-progress-template.json](github-progress-template.json) are identical
empty progress templates. The compatibility filename does not create a second track.
The schema remains `1`; the current catalog is `1.3`. Earlier compatible records
remain readable without inventing evidence.

## What statuses mean

| Status | Meaning |
|---|---|
| not_started | No attempt has been recorded. |
| learning | The learner is working on the task with help or still fixing it. |
| provisional | The learner successfully applied the technique; guided help counts when recorded. |
| secure | Successful application used no assistance beyond allowed references. |
| review_needed | An observed gap needs a specific repair. |

Both `provisional` and `secure` permit forward progress. A copied solution is not
independent work; record `solution` support. An explanation alone does not prove a
working program. Predictions, recitations, delayed reviews, and hours studied are
not advancement requirements. Optional reviews must not take over the next lesson.

## What to record

Use one attempt for one observed application: its date, outcome, help used, and
a short description of what the program did. Include a file or commit link when
available. Describe terminal output accurately; distinguish tutor-observed work
from the learner's report. Repository checks do not count as learner attempts.
Python work does not require a GitHub administration action to count as successful.

- `environment` describes the Codespace. Keep OS, Python version, and execution
  availability `null` until observed. `command` names the intended Run control.
- `current_lesson` and `next_task` are both `null` when no lesson is active.
  Set them for an explicitly requested learning session, not for setup maintenance.
- `lessons` stores statuses and attempts. Use `applied` for a practical task.
  Existing `guided`, `transfer`, `explanation`, and `delayed` kinds remain readable;
  explanations and later reviews are optional evidence.
- Each attempt uses `pass` or `retry`, and support `none`, `reference`, `hint`, or
  `solution`. A fresh application can use `transfer`; a worked exercise can use
  `guided`. Record assistance based on what happened, not the chosen label.
- `reviews` stores only optional reviews agreed with the learner; it may stay empty.
- `capstones` holds optional phase projects actually completed, with help recorded.
  A project suggestion does not block the next phase. Historical GitHub capstones
  remain readable but add no requirement to the Python course.

Use actual `YYYY-MM-DD` dates. Put uncertain or undated reports in `notes` rather
than inventing dates. Keep public records free of private data and credentials.

The tutor updates the record through authorized repository tools or the Codespace.
The progress validator checks consistency and suggests Python tasks; it cannot
judge the quality or truth of evidence, and it does not save progress. Its legacy
`--track github` option remains an alias for the Python route.

End each learning session with what worked, help used, any remaining issue, and
an agreed next task. Maintenance requests get a correction report without a
lesson assignment. Say whether the record was saved when relevant.
