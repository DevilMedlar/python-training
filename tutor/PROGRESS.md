# Progress records

Copy [progress-template.json](progress-template.json) to ignored
`progress/progress.json`, or keep the JSON in a private note. Never commit real
learner records to this public repository. The template contains no learner history.
For the companion track, start from [github-progress-template.json](github-progress-template.json).
Both templates use the same schema and can hold Python and GitHub evidence together.

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
The current catalog is `1.1`. Existing `1.0` records remain readable because
Python IDs and evidence fields are preserved; save new handoffs as `1.1`.
Unknown versions require an explicit migration, not silently relabeled evidence.
Each attempt has `kind`, `performed_on`, `outcome`, `support`, and `summary`.
Kinds are `guided`, `transfer`, `explanation`, and `delayed`; outcomes are `pass`
or `retry`. Dates use `YYYY-MM-DD`. Do not fabricate a date for unknown history;
describe it in `notes` and obtain new evidence before a status requiring dates.

`reviews` contains `lesson_id`, `due_on`, and `reason`. `capstones` maps phase
numbers as strings, or the companion key `github`, to `status`, `completed_on`,
`support`, and `evidence`.
Capstone statuses are `not_started`, `in_progress`, and `complete`. Completion
requires an actual date, independent/reference support, and a nonempty evidence list.
`current_lesson` and `next_task` preserve the immediate context. Use `notes` for
uncertainty and tailored route decisions.

## Validate and route

From the repository root, run:

```sh
python tools/progress.py tutor/progress-template.json
python tools/progress.py progress/progress.json --next
python tools/progress.py tutor/github-progress-template.json --next --track github
```

The recommendation is a conservative default: due reviews first, then repairs,
then the first incomplete core lesson whose prerequisites are available. It
requires a capstone before entering a later phase. Optional specialist lessons
are chosen by the learner/tutor; the default route does not force them. The tool
does not schedule reminders, judge code, or write progress automatically.

Use `--track github` for GitHub recommendations. The default remains Python even
if `current_lesson` names a GitHub lesson; the flag makes the selected route explicit.
GitHub routing checks due reviews and repairs in that track and the next lesson's
transitive prerequisites. It starts at `GH-01` without Python, requests missing
Python prerequisites when reaching `GH-09`, and ends at the separate GitHub capstone.
Unrelated Python reviews do not block early browser tasks. After all track lessons
are ready, keep any further Python review schedule through the Python route.

Record the chosen route, Git version, repository/branch context, and tool access in
`notes`. Do not add undocumented fields or store tokens. A simulated PR, copied
solution, or automated lab run must not be recorded as an independent real contribution.

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
