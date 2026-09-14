# Capstones

Use synthetic practice data. Build from the contract before opening the reference
programs. A reference demonstrates selected mechanisms; the capstone also asks
for independent extension, explanation, and failure evidence. Work on a browser
branch under `workspace/`, run through GitHub Actions, and deliver each capstone
as an inspected Python PR. The GitHub work belongs to that capstone.
Each phase's final Practice B points here.

## Capstone 1 Study tracker

Build a tracker using input() that adds positive whole-number study durations,
reports count/total/average, and saves then quits. Store a JSON list at a documented
path. Missing data means a new history; malformed, unreadable, wrongly shaped,
boolean, or nonpositive saved data must be reported without overwriting it.

Acceptance examples: empty history gives count 0, total 0, average 0.0; adding
20 and 40 gives count 2, total 60, average 30.0; saving and reopening preserves
the list. Invalid input prompts a correction. An unsuccessful save does not claim
success. Supply the menu answers through workspace/input.txt, including a final
quit choice. Demonstrate save and reopen within the same run. For a subsequent
fresh run, commit the intended synthetic starting JSON under workspace/data/;
runner files do not automatically persist or become commits. Preview small saved
files under workspace/results/ on the run summary. Explain both persistence boundaries.

Deliver calculation functions, an interface, error checks, and a short README.
Independently add one feature such as longest session or removal of the latest
entry. Explain how its empty case works. Reference:
[study_tracker.py](../examples/study_tracker.py). Its safer file replacement is
an extension beyond the first beginner version; it is not a guarantee against
power loss or simultaneous writers.

## Capstone 2 Study report application

Read UTF-8 CSV with exactly the ordered header `topic,minutes`. Trim topic edges,
preserve case, support quoting, and combine repeated topics. Define nonnegative
minutes as 1–9 ASCII digits after trimming; reject signs, fractions, separators,
empty fields, extra fields, and invalid rows. Zero is allowed in this reporting
format even though Capstone 1 requires positive study sessions.

Preserve line breaks embedded inside quoted topics after trimming their edges.
LF, CRLF, and CR are supported CSV line endings; do not silently normalize the
contents of a topic while parsing. A topic containing a line break also occupies
multiple lines in this simple text report.

Print totals sorted by topic. Header-only input succeeds with empty output;
malformed later input fails with error output and no partial success summary.
Successful execution returns exit status 0; application failures return 1;
command syntax errors may use argparse's status 2. Do not modify the source file.

Deliver tests, help text, setup instructions, and one independent extension
(date filtering, JSON export, or SQLite persistence). Explain validation,
aggregation, I/O, and CLI boundaries. Package/install it for the P2-11 exercise.
Reference: [studylog.py](../examples/studylog.py). The reference materializes
records; document this limit or implement a correctly bounded alternative.

## Capstone 3 Bounded processing system

Process a stream of synthetic records using a fixed number of workers and bounded
pending work. Define the transformation, malformed-record policy, success output,
task ownership, and shutdown behavior. Account for queues, workers, and retained
results; a semaphore alone is insufficient if every task is created in advance.

Acceptance includes empty work, normal work, invalid configuration, a worker
failure while the producer is blocked, external cancellation, and early cleanup.
Use a deadline in failure tests and demonstrate that no owned work remains active.
Choose whether partial results are discarded, reported, or committed; explain the
tradeoff. A separately owned transaction may be added, with its limits explicit.

Deliver a requirements note, tests, resource accounting, a small performance
study, and a runbook. Add one unfamiliar failure requested by the tutor. Reference:
[pipeline.py](../examples/pipeline.py); [inventory.py](../examples/inventory.py)
is a separate transaction mechanism. Combining them is a design exercise, not
an implied claim of distributed atomicity.

## Capstone 4 Reproducible investigation

Use [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md) to define a question, comparison,
units, primary metric, input generation, uncertainty method, exclusions, and
resource budget before the final analysis. Choose a small replication or a
clearly labeled teaching experiment with an analytical or independent check.

Preserve code identity, environment, configuration, raw per-unit measurements,
failures, and scripts producing results. Define agreement as bytes, tolerance,
or a justified qualitative criterion. For the supplied estimator lab, compare
methods on the same dataset and preserve pairing in inference.

Deliver protocol, artifact, tests, a methods/results report, and a discrepancy
log. Change one prespecified factor and compare against the original baseline.
Seek an independent rerun; if unavailable, state that limitation. A local repeat
is not independent external validation. Reference:
[research_optional.py](../examples/research_optional.py), with optional scientific
dependencies described in [examples](../examples/README.md).

## Capstone 5 Useful contribution

Choose a narrow user or research problem and inspect credible existing solutions.
Examples include a validated domain utility, a focused analysis tool, a better
evaluation harness, or a specific upstream reliability improvement. These ideas
are project prompts, not established novel research directions.

Specify a public contract, a baseline, a candidate change, the intended benefit,
compatibility, and failure cases. Evaluate claims against realistic and adverse
conditions. Prepare an installable/reviewable artifact, complete first-use tutorial,
maintainer map, support policy, and limits. Publishing is optional.

Deliver a contribution brief, tests, evaluation, independent feedback where
available, and a maintenance plan. Explain what changed, who benefits, what the
evidence supports, and what remains unknown. Reference:
[selection.py](../examples/selection.py) and its benchmark are a starting point
for fair comparisons of established methods; copying them is not a novel contribution.

## Suggested starting files

Start small: a README with the contract, an implementation module, a tests file,
and disposable sample data. For research, add a protocol and raw-results directory;
for creator work, add a decision record and evaluation report. Do not create a
large empty directory tree before you know which pieces the project needs.
