# Progress records

Copy [progress-template.json](progress-template.json) to ignored
`progress/progress.json`, or keep the JSON in a private note. Never commit real
learner records to this public repository. The template contains no learner history.

The tutor may update a record only using observed work or explicitly attributed
learner reports. Validation checks its structure and consistency, not whether
the evidence is truthful or sufficient in the real world.

## Status meanings

| Status | Meaning | Required evidence |
|---|---|---|
| `not_started` | No recorded work | No fabricated attempts |
| `learning` | Introduced or practiced | Record support honestly |
| `provisional` | Independent transfer and explanation succeeded | Passing `transfer` and `explanation` attempts with `none` or `reference` support |
| `secure` | The skill was also retained later | Provisional evidence plus a passing independent `delayed` check on a later date than a passing transfer |
| `review_needed` | A previously introduced skill needs repair | Describe the observed gap and next repair |

These thresholds are course design rules, not standardized psychometrics. Multiple
observations strengthen a decision. A date field cannot establish learning by itself.
For ordinary forward progress, provisional prerequisites can be used while their
reviews remain scheduled. A phase capstone is an additional transition requirement.

## Record shape

`schema_version` and `catalog_version` identify formats. `environment` records
known execution facts. `lessons` maps stable lesson IDs to a status and attempts.
Each attempt has `kind`, `performed_on`, `outcome`, `support`, and `summary`.
Kinds are `guided`, `transfer`, `explanation`, and `delayed`; outcomes are `pass`
or `retry`. Dates use `YYYY-MM-DD`. Do not fabricate a date for unknown history;
describe it in `notes` and obtain new evidence before a status requiring dates.

`reviews` contains `lesson_id`, `due_on`, and `reason`. `capstones` maps phase
numbers as strings to `status`, `completed_on`, `support`, and `evidence`.
Capstone statuses are `not_started`, `in_progress`, and `complete`. Completion
requires an actual date, independent/reference support, and a nonempty evidence list.
`current_lesson` and `next_task` preserve the immediate context. Use `notes` for
uncertainty and tailored route decisions.

## Validate and route

From the repository root, run:

```sh
python tools/progress.py tutor/progress-template.json
python tools/progress.py progress/progress.json --next
```

The recommendation is a conservative default: due reviews first, then repairs,
then the first incomplete core lesson whose prerequisites are available. It
requires a capstone before entering a later phase. Optional specialist lessons
are chosen by the learner/tutor; the default route does not force them. The tool
does not schedule reminders, judge code, or write progress automatically.

For a deliberately tailored route, record the decision and use the catalog to
check the needed prerequisites. The default recommendation may differ from that
tailored plan; do not invent completion records merely to change its output.

## Session handoff

Provide a short human-readable summary alongside the updated record:

- Current goal, environment, and lesson.
- What the learner actually demonstrated, including assistance.
- One misconception or uncertainty still to address.
- The next concrete task and the next review date.
- Files the next tutor needs to load.

Say whether the record was actually saved or only printed for the learner to save.
Keep credentials, employer/client records, and unrelated personal details out of it.
