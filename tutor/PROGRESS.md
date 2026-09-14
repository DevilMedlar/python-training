# One progress record

Use [tutor/progress.json](progress.json) on GitHub for the Python course and the
GitHub skills practiced within it. The tutor can update it through authorized
repository tools; you can edit and commit it in github.dev. Keep only learning
evidence and code/run links suitable for this public repository.

The [empty template](progress-template.json) uses the same format. The old
`github-progress-template.json` filename is retained as an identical compatibility
copy, not a second route. The current catalog is `1.2`; `1.0` and `1.1` records
remain readable. Retain old evidence and dates rather than inventing a migration.

## Evidence and status

| Status | Evidence required |
|---|---|
| not_started | No observed work or fabricated attempts |
| learning | An observed attempt with the actual support recorded |
| provisional | Independent transfer and explanation, with none or reference support |
| secure | Provisional evidence plus an independent passing review on a later date |
| review_needed | The observed gap and next repair |

These are course rules, not standardized psychological measurements. A green
Actions run proves only its checked behavior. It does not show that you understand
the program or independently performed a GitHub action.

Each Python attempt's `summary` records what the code demonstrated and the linked
GitHub action: for example, the function's empty case, the inspected diff, and the
run URL. The tutor checks both parts before marking that combined task successful.
Old `GH-` records are preserved as historical evidence; they cannot grant Python
mastery. Their due reviews are attached to the corresponding Python lesson.

## Record fields

`environment` describes the observed GitHub runner, not your laptop. Leave its
Python patch version unknown until a run reports it. `current_lesson` identifies
the Python task. `lessons` holds statuses and attempts; each attempt has `kind`,
`performed_on`, `outcome`, `support`, and `summary`. Kinds are `guided`, `transfer`,
`explanation`, and `delayed`; outcomes are `pass` or `retry`; support is `none`,
`reference`, `hint`, or `solution`.

Use actual `YYYY-MM-DD` dates. Put undated or unconfirmed history in `notes`.
`reviews` stores a lesson, due date, and reason. `capstones` uses phase keys `1`
through `5`; each capstone includes the Python deliverable and its GitHub review
evidence. A historical `github` capstone record remains readable but creates no
extra completion requirement. `next_task` says exactly where to continue.

## Browser validation and routing

After committing the record, open **Actions → Verify Python tutor → Run workflow**
on the appropriate branch. The progress step validates it and prints the next
Python task with its GitHub skills. Recommendations prioritize due reviews,
repairs, core lessons, and each phase's capstone. Optional specialties stay optional.
The tool cannot judge evidence quality or save progress automatically.

For older integrations, the `--track github` parameter is accepted only as a
compatibility alias for this same integrated route. It never starts a GH sequence.

At session end, summarize the demonstrated skill, help used, remaining gap, next
task, due review, and needed files. State whether the record was actually committed
to GitHub or whether the supplied text still needs to be saved there.
