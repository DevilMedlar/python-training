# Claim and design audit

Review date: 2026-09-14. The supplied materials were AI-generated drafts, not
authorities. This record distinguishes corrections, confirmed claims, and added
engineering controls. It does not imply that every sentence of every external
reference or omitted draft passage was exhaustively verified.

## Corrections and qualifications

| Source or issue | Finding | Action in this repository | Evidence |
|---|---|---|---|
| `learning Phases.txt`, opening and phase labels | A predictable universal psychological/academic trajectory is asserted without support | Replace with informal, overlapping skill routes; no degree equivalence | Course design explicitly identified in README and assessment |
| Same file, Dunning–Kruger/impostor/transcendence claims | These are not sound placement requirements or diagnoses of an individual learner | Remove from placement and progression criteria | Placement uses observed tasks; no psychological diagnosis |
| Different Phase 4/5 labels across files | The short file combines researcher/creator differently from the five Python guides | Adopt Novice, Practitioner, Expert, Researcher, Creator consistently | Catalog and all phase headings checked together |
| Length and duplicated guidance | Long documents do not specify one reliable next tutor action | Separate operating instructions, catalog, lesson content, evidence, and references | Tutoring scenario review and prerequisite checks |
| Mastery schedules and scores | Proposed hours/thresholds are planning suggestions, not measured universal requirements | Remove time-to-mastery promises; use explicit, locally defined evidence rules | Assessment and teaching documents label design choices |
| AI tutoring study generalization | Results from particular systems/settings cannot validate this repository's prompt | Keep unassisted assessment; make no empirical efficacy claim for this tutor | Source handbook's caveats retained; no numerical effect claims imported |
| Beginner tracker | Original explicitly uses direct single-writer saves and returns normally on load failure | Add failure exit status, validated save, temporary sibling write/replacement, interruption behavior | Regression tests preserve old data on validation/fsync/replace failure |
| CSV integer contract | Original accepts arbitrarily long digit strings subject to interpreter limits | State a deliberate 1–9 ASCII-digit input limit; test both boundaries | Application contract and parser tests; this is a changed design, not a Python rule |
| New CSV test fixture on Windows | The first CI run exposed platform newline translation in the test writer; its expected LF value no longer matched the bytes written | Disable newline translation in fixtures and test LF, CRLF, and CR explicitly; preserve embedded topic line breaks | `test_studylog.py`; Python CSV newline guidance in PY-CSV |
| Dataclass boundary | Original explicitly permits unvalidated direct `Session` construction | Add constructor validation so direct internal construction follows the same record rules | Wrong types, booleans, blank topics, and range tests |
| Async lab extensions | Source proposes but does not execute every failure/cancellation extension | Implement dependency injection and tests for blocked production, worker failure, external cancellation, cleanup | `test_pipeline.py` |
| SQLite lab | Source correctly says the helper owns a transaction and warns against committing unrelated work | New helpers own and close their own file-database connections; validate integer domain | Cross-connection rollback and overspend tests |
| Research experiment | Source prints summaries but identifies missing raw evidence as a limitation | Preserve raw paired losses and richer configuration; separate inference entropy from task entropy | Research tests and full rerun; code identity still recorded separately |
| Progress across chats | Uploaded material does not define a validated portable state format | Add explicit records and rejection of unsupported secure/provisional states | `test_progress.py`; validator cannot establish truth of reported history |
| Optional specialty overload | Advanced tool inventories can be mistaken for mandatory prerequisites | Mark two creator specialist labs optional; choose tools by the actual project | Catalog routing and common assessment policy |

## Confirmed technical claims

| Claim | Result and boundary | Primary source |
|---|---|---|
| Python 3.14 stable and 3.15 prerelease at review | Confirmed on the official release page; patch freshness is date-specific | [PY-RELEASES](SOURCES.md#py-releases) |
| Free-threaded CPython is optional and supported in 3.14 | Confirmed; conventional builds, extension compatibility, and actual GIL state still matter | [PY-FREE-THREADING](SOURCES.md#py-free-threading) |
| 3.14 annotation evaluation is deferred by default | Confirmed; introspection/evaluation can have effects | [PY-ANNOTATIONS](SOURCES.md#py-annotations) |
| 3.14 includes interpreter-pool facilities | Confirmed; isolation/serialization costs are part of the model | [PY-EXECUTORS](SOURCES.md#py-executors) |
| `fork` is no longer a default start method in 3.14 | Confirmed; actual platform and selected method still matter | [PY-PROCESSES](SOURCES.md#py-processes) |
| GIL safety, semaphore memory bounds, and timeout effects | The drafts' important caveats are retained, not corrected into false simplifications | [PY-ASYNC](SOURCES.md#py-async), [HTTP-SEMANTICS](SOURCES.md#http-semantics) |
| Type hints and frozen dataclasses do not validate or deeply freeze arbitrary data | Confirmed; new runtime checks are explicit application rules | [PY-TYPING](SOURCES.md#py-typing), [PY-DATACLASSES](SOURCES.md#py-dataclasses) |
| SQLite connection context does not close its connection | Confirmed and covered by explicit ownership in the new example | [PY-SQLITE](SOURCES.md#py-sqlite) |
| Seed alone does not guarantee universal reproducibility | Retained; task identities and exact environment are recorded | [NUMPY-RANDOM](SOURCES.md#numpy-random) |
| Paired estimator comparison and theoretical mean MSE | Original displayed values reproduced; analytical targets 0.010 and 0.109 follow the stated mixture | Source rerun, explicit derivation in P4-02, [SCIPY-BOOTSTRAP](SOURCES.md#scipy-bootstrap) |

## Source execution review

All **61 fenced Python blocks** in the Markdown drafts compiled under Python
3.12.14. This is a syntax check, not a claim that every interactive or context-dependent
fragment ran as a standalone program. All **six Phase 3 Word code labs** executed
after extracting code separately from adjacent explanatory prose. A first extraction
accidentally included prose after lab 2; correcting extraction resolved that error.
It was not a defect in the Python lab itself.

The original Phase 2 study reporter passed its **12 test methods**. The original
Phase 5 selection contract checks passed. The original Phase 4 experiment executed
with NumPy 2.3.5 and SciPy 1.17.0 and reproduced its displayed rounded estimates
and intervals. The new experiment retains those data-generation rules but uses
separate inference entropy and preserves raw results; its bootstrap endpoints
need not equal the original summary table.

The final repository has its own checks and evidence in
[VERIFICATION.md](VERIFICATION.md). Confirmed source material is retained where
useful; no errors were invented merely to make this audit look more critical.
