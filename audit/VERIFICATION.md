# Verification record

The current Codespaces restart is recorded in the final section. Earlier
sections are historical observations, not current setup instructions.

Review date: 2026-09-14. This file records the scope of the four review passes.
The original Python rebuild and subsequent GitHub addition have separate observed
results below. The [GitHub audit](GITHUB_AUDIT.md) records its source-specific checks.
Observed command results are recorded below after the complete repository checks.
No combination of these checks proves universal correctness or educational efficacy.

## Pass 1 Source and factual review

The original seven attachments were inventoried and their content extracted, including
Word tables and links. The five-phase topics and teaching guidance were mapped
into the canonical course. Claims retained in the course were checked against
primary documentation where version-sensitive, subtle, or research-dependent;
the [claim audit](CLAIM_AUDIT.md) records significant decisions. Proposed research
ideas are not represented as established novelty. Original draft passages not
carried into the course are not certified by this audit.

## Pass 2 Executable behavior

Test every runnable Python block in canonical Markdown. Check reference programs
against explicit contracts, hand-computable cases, independent comparisons, and
realistic failures. Include corrupt data, failed saves, strict CSV fields, async
cancellation, transaction rollback, and unsupported progress claims. The optional
scientific lab is checked separately from the dependency-free core.

## Pass 3 Structure and consistency

Check lesson IDs, headings, prerequisites, acyclicity, required lesson sections,
source references, internal file links and anchors, generated index, JSON formats,
and the empty progress template. Compare capstone rules with implementations.
Review version-sensitive statements and separate optional specialty routes from
the default progression.

## Pass 4 Tutor behavior review

Walk through the scenarios in [SCENARIOS.md](../tutor/SCENARIOS.md): new learner,
wrong answer, requested solution, alternate correct code, missing file access,
no execution tools, failed delayed recall, disputed answer key, imported
instructions, version mismatch, research overclaim, and a tailored creator route.
This is a manual protocol/design review, not a controlled learning study or a
claim that every ChatGPT model will follow the prompt perfectly.

## Reproduce the current maintenance checks

In the Codespace terminal run `python tools/check_repo.py` and
`python tools/run_tests.py`. The **Verify Python tutor** workflow also checks
course integrity and examples on GitHub. Learner programs run directly in the
Codespace. Earlier tables below record superseded implementations.

## Original Python rebuild local results

On 2026-09-14, the completed checks ran on Linux x86-64 with CPython 3.12.14,
NumPy 2.3.5, and SciPy 1.17.0. These are observations from that environment,
not assumed results for other interpreters or operating systems.

| Check | Observed result |
|---|---|
| `python tools/check_repo.py` | Passed: 50 lessons, 48 core lessons, 60 source records, 27 Markdown files, 250 internal links, 21 executed Markdown examples, 24 parsed Python files |
| `python -m unittest discover -s tests -q` | Passed: 82 tests, including all five optional scientific tests; no skips |
| `python tools/progress.py tutor/progress-template.json --next` | Returned the initial lesson `P1-01` |
| `python -m examples.research_optional` | Completed the full default experiment and emitted valid JSON with 1,000 raw paired loss rows per scenario |
| `git diff --check` | Passed before publication |

The full experiment used 100 observations per independent dataset and 4,999 BCa
bootstrap resamples. Its observed results, rounded here for readability, were:

| Contamination probability | Mean estimator MSE | Median estimator MSE | Mean minus median MSE | Per-scenario 95% interval for the difference |
|---|---|---|---|---|
| 0.0 | 0.010254378 | 0.016104910 | -0.005850532 | [-0.006984501, -0.004833089] |
| 0.1 | 0.106613159 | 0.019857322 | 0.086755837 | [0.077657393, 0.096714764] |

These intervals describe Monte Carlo uncertainty for the specified simulated
populations. They do not establish a universal ranking of estimators. Raw results
are reproducible with the command above in the recorded environment; generated
experiment files are deliberately excluded from the source repository.

## GitHub verification history

The first published run, `34893339350`, found a test-fixture defect on all three
Windows jobs: the fixture writer translated LF to CRLF, while its assertion
still expected LF inside a quoted CSV field. The application correctly preserved
the file's embedded line break. The test writer now disables translation, and
the test covers LF, CRLF, and CR on every platform. This is a correction to the
new test suite, not a defect attributed to the supplied drafts.

After that correction, [run 34893558086](https://github.com/DevilMedlar/python-training/actions/runs/34893558086)
completed successfully for PR head `7e52d4d87450ea74faf839a58b13f4d3aa93cf89`.
All ten jobs passed. The setup logs reported these exact CPython versions:

| Runner label | Python 3.12 job | Python 3.13 job | Python 3.14 job |
|---|---|---|---|
| `ubuntu-latest` | 3.12.14 — passed | 3.13.15 — passed | 3.14.7 — passed |
| `windows-latest` | 3.12.10 — passed | 3.13.15 — passed | 3.14.7 — passed |
| `macos-latest` | 3.12.10 — passed | 3.13.15 — passed | 3.14.7 — passed |

Each core job passed the repository checker, all 77 core tests, and initial
progress routing. Its unittest report lists 82 tests with five explicit skips
because scientific dependencies are intentionally absent. The separate Ubuntu
research job used CPython 3.12.14, installed the pinned requirements, and passed
all five scientific tests without skips. The full 1,000-dataset experiment above
was a local run; CI's scientific job runs the smaller end-to-end regression case.

Runner labels and installed patch versions can change on future runs. This table
records the observed run, not every possible Python build or future dependency.

## GitHub addition local results

The added reference was reviewed independently as described in
[GITHUB_AUDIT.md](GITHUB_AUDIT.md). On Linux with CPython 3.12.14 and Git 2.51.1:

| Check | Observed result |
|---|---|
| Original supplied Python example | Four tests passed; deliberate lowercase regression failed; restoration passed; empty discovery rejected |
| Maintained unit suite | 100 tests passed, including five scientific tests; no skips in the installed local environment |
| Offline Git lab | Seven invariant groups passed, including a fresh clone from a mirror and restored tracked content |
| Markdown examples | All 22 runnable Python blocks passed |
| Catalog | 66 lessons, 48 Python core lessons, 16 optional GitHub lessons, 115 primary source records |
| Initial routing | Default record starts at P1-01; explicit GitHub route starts at GH-01 |

The runner now rejects zero discovered tests; five intentional scientific skips
in a core environment are distinct from an empty suite.

## GitHub addition hosted results

[Run 34902607844](https://github.com/DevilMedlar/python-training/actions/runs/34902607844)
completed successfully for PR head `237548a0aaa9c7c782a9b6992f893438bc6c9986`.
All ten jobs passed, and all ten job logs were inspected. This is a separate run
of the GitHub addition, not an extrapolation from the earlier Python rebuild.

| Runner label | Python 3.12 job | Python 3.13 job | Python 3.14 job | Git observed in the lab |
|---|---|---|---|---|
| `ubuntu-latest` | 3.12.14 — passed | 3.13.15 — passed | 3.14.7 — passed | 2.55.0 |
| `windows-latest` | 3.12.10 — passed | 3.13.15 — passed | 3.14.7 — passed | 2.55.0.windows.5 |
| `macos-latest` | 3.12.10 — passed | 3.13.15 — passed | 3.14.7 — passed | 2.55.0 |

Each core job passed the repository checker, seven Git invariant groups, and both
initial routing checks. Each test report lists 100 tests with five explicit skips:
95 core tests passed, and the scientific tests were intentionally absent from that
environment. The separate research job used CPython 3.12.14 and passed those five
scientific tests with the pinned dependencies. All 22 runnable Markdown examples
and 393 internal links passed the checker. This table records these observed
environments; future runner images and patch versions may differ.

## Limits of all checks

External URLs were consulted for the cited topics; an automated link check cannot
establish a source's truth. Internal links are checked offline. Optional third-party
workflows not executed are learning directions with primary references, not verified
installation recipes. Local runs do not prove every platform/build configuration.
No learner trial, independent academic review, exhaustive formal proof, or universal
research novelty search was performed. See CI and recorded command outcomes for
the exact verified environments.

## Browser integration correction on 2026-09-14

The learner workflow now uses github.dev for edits and GitHub-hosted Actions for
Python execution. All 50 Python lessons embed GitHub practice; the 16 GH entries
are references. One progress route replaces the earlier independent track.
Historical progress versions 1.0 and 1.1 remain readable without inventing mastery.

Observed in the agent verification environment, Linux x86-64 with CPython 3.12.14:

| Check | Observed result |
|---|---|
| Maintained suite | 106 tests passed, including five installed scientific tests |
| Lesson runner | Starter executed successfully and printed Ready to learn and 5 |
| Runner failure cases | Recorded stdin, imports, result files, missing inputs/files, syntax failure, explicit nonzero exit, timeout, escaped output, and truncated previews checked |
| Progress routing | Starts at P1-01 with its GitHub action; legacy track argument selects the same route; GH history cannot skip Python or add a capstone |
| Repository integrity | 50 Python lessons, 16 GitHub references, 119 sources, 34 Markdown files, 528 internal links, 21 executed Markdown examples, 31 parsed implementation/test files |
| Workflow syntax | Three YAML workflows parsed with their intended triggers and jobs |

These checks happened in the agent environment, not on the learner's laptop.
They do not imply that every GitHub-hosted matrix job already passed. The PR and
Actions runs that introduce this correction provide the hosted check results;
inspect the commit and job conclusions there. The learner's first-run output and
course verification are different workflows, and neither proves learner mastery.

No real learner attempts were fabricated, and the new progress record is empty.
The source attachments were not rewritten. Browser buttons are documented from
GitHub's primary documentation; an automated runner test does not claim that an
interactive browser session or independent learner trial was performed.

### First hosted observations for the browser correction

The [lesson run 34906151900](https://github.com/DevilMedlar/python-training/actions/runs/34906151900)
passed on GitHub's Ubuntu runner with Python 3.14.7 at commit
`fec8a6dd6bb5b5d75445311af84bc3019171583f`. Its log printed Ready to learn and 5,
and explicitly reported that no learner tests had been supplied yet.

The [initial verifier run 34906173227](https://github.com/DevilMedlar/python-training/actions/runs/34906173227)
passed the six Linux/macOS core jobs and the scientific job. The three Windows
jobs exposed a new test expectation that assumed LF for printed output. The
runner correctly preserved Windows CRLF. The fixture now expects the platform's
line separator; this corrects the test without changing program output. The PR
checks for the subsequent commit establish the final hosted outcome.

## Codespaces course restart on 2026-09-18

The learner specified the existing Codespace at
https://cuddly-trout-q767pqw4v79rfpjr.github.dev/. The previous Actions-based learner
workflow did not match that requirement. This revision uses direct Python execution,
live terminal input, and short workspace controls alongside applied Python tasks.
Repository settings, licenses, ignore rules, and collaboration have eight separate
non-Python reference lessons. Prediction and recall gates were removed.

The active progress record was reset at P1-01. The immediately preceding record
is archived byte-for-byte at `tutor/history/progress-before-restart-2026-09-18.json`.
No new learner completion is inferred from these maintenance checks.

Before publication, the agent workspace checks observed:

| Check | Result |
|---|---|
| `python tools/check_repo.py` | Passed: 50 Python lessons, 8 repository lessons, 16 historical GH IDs, 48 core lessons, 124 source records, 35 Markdown files, 294 internal links, 21 executed examples, 29 parsed Python files |
| `python tools/run_tests.py` | Passed: 107 tests, no skips, including the available scientific dependency tests |
| Catalog/progress compatibility | Historical 1.0–1.2 records remain readable; 1.3 uses applied work and optional reviews/projects |
| Preserved learner work | Existing workspace/main.py unchanged; fresh starter created as workspace/lesson_01.py |

These checks verify course content and tools. The browser opened the named Codespace
and observed a clean main branch, Linux, and Python 3.14.2 before synchronization.
Actual post-publication workspace runs and the pull request's CI results establish
their own execution evidence; the earlier observations do not cover this revision.

### Observed publication and Codespace runs

[PR #4](https://github.com/DevilMedlar/python-training/pull/4) merged at
`a57e7cb867263017a4709bb9784739a9795bbf78`. Its
[verification run](https://github.com/DevilMedlar/python-training/actions/runs/35301668265)
passed all ten jobs: the nine OS/Python combinations and the optional research job.

The assistant used the browser to update the learner's existing Codespace from
a clean main branch with a fast-forward pull. It then clicked **Run Python File**
on `workspace/lesson_01.py` and observed both greeting lines. The same button ran
`workspace/input_example.py`; typing `Workspace check` live into the terminal
produced `Hello, Workspace check!`. Linux and Python 3.14.2 were directly observed.
No redirected input file, learner workflow, or laptop runtime was involved.
These are setup checks, not evidence that the learner completed P1-01.
