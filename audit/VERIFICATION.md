# Verification record

Review date: 2026-09-14. This file records the scope of the four review passes.
Observed command results are recorded below after the complete repository checks.
No combination of these checks proves universal correctness or educational efficacy.

## Pass 1 Source and factual review

All seven attachments were inventoried and their content extracted, including
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

## Reproduce the checks

```sh
python tools/check_repo.py
python -m unittest discover -s tests -v
python tools/progress.py tutor/progress-template.json --next
```

Install `requirements-research.txt` in a separate environment to include the
optional NumPy/SciPy tests. Without those packages, those tests are explicitly
skipped. GitHub CI tests the core on Python 3.12–3.14 and several operating
systems, plus a separate pinned scientific job; configured jobs are not counted
as successful until their actual results are observed.

## Observed local results

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

Final matrix results are recorded once observed; the configuration alone does
not establish that those checks passed.

## Limits

External URLs were consulted for the cited topics; an automated link check cannot
establish a source's truth. Internal links are checked offline. Optional third-party
workflows not executed are learning directions with primary references, not verified
installation recipes. Local runs do not prove every platform/build configuration.
No learner trial, independent academic review, exhaustive formal proof, or universal
research novelty search was performed. See CI and recorded command outcomes for
the exact verified environments.
