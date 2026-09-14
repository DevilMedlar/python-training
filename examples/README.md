# Reference programs

Try the corresponding lesson or capstone first. These are inspectable reference
implementations, not hidden answer keys or complete production systems. The
standard-library examples target Python 3.12–3.14. Read them on github.com or
github.dev. Commands in the table are **GitHub-hosted workflow steps**, introduced
when the corresponding Python lesson needs them. Edit a workflow's `run:` step
in github.dev and inspect its Actions output; do not run commands on your laptop.
The ordinary learner entry point remains workspace/main.py.

| Program | Lesson purpose | Run or inspect |
|---|---|---|
| [drills.py](drills.py) | Selected beginner solutions with explicit preconditions | Attempt the beginner drills first |
| [study_tracker.py](study_tracker.py) | Beginner functions, validation, JSON, optional safer save | `python -m examples.study_tracker --file workspace/results/sessions.json < workspace/input.txt` |
| [studylog.py](studylog.py) | Strict CSV, records, aggregation, CLI failures | `python -m examples.studylog examples/data/sessions.csv` |
| [contracts.py](contracts.py) | Typed synchronous decorator and reporting contract | Read with `tests/test_contracts.py` |
| [pipeline.py](pipeline.py) | Fixed workers, bounded queue, failure/cancellation cleanup | `python -m examples.pipeline` |
| [inventory.py](inventory.py) | Parameterized SQLite and owned transaction boundaries | Use a temporary database as in `tests/test_inventory.py` |
| [selection.py](selection.py) | Shared contract and independent algorithm oracle | Read with `tests/test_selection.py` |
| [benchmark_selection.py](benchmark_selection.py) | Raw timings and measurement scope | `python -m examples.benchmark_selection --size 1000 --k 10 --repeats 6` |
| [research_optional.py](research_optional.py) | Paired simulation and uncertainty | Optional instructions below |
| [topic_names.py](topic_names.py) | Python string contract and regression review | `python tools/run_tests.py --pattern test_topic_names.py` |
| [git_workflow_lab.py](git_workflow_lab.py) | Git snapshots, synchronization, conflicts, recovery, and mirror history | `python -m examples.git_workflow_lab` in the existing verifier job |

For the tracker, use workspace/input.txt with the required menu choices and a
quit choice. In a hosted workflow step, create workspace/results first and redirect
that input file into the module command. Results are temporary until deliberately
preserved. The ordinary lesson runner already creates that results directory.
The reporter prints `Python: 60 min` and `Testing: 20 min`, on separate lines.
The pipeline prints `285`. Benchmark durations vary; no fixed speedup is expected.

## Optional numerical experiment

Use a GitHub-hosted workflow job. The earlier recorded reproduction used Python
3.12.14, NumPy 2.3.5, and SciPy 1.17.0. The pins identify that experiment; they are
not a claim that those are the newest releases or the only compatible environment.

These commands belong in hosted `run:` steps (see the [browser workflow](../practice/BROWSER_WORKFLOW.md#advanced-commands-run-in-workflows)):

```sh
python -m pip install -r requirements-research.txt
python -m examples.research_optional
python tools/run_tests.py --pattern test_research_optional.py
```

Use synthetic data and plan how required research results will be retained on GitHub.
The lab outputs raw per-replication losses, version/configuration information, and
per-scenario BCa intervals for the mean paired loss difference. Positive difference
favors the median; negative favors the mean. Both estimates target zero in the
specified symmetric populations.

The sample mean's analytical MSE is `variance / observations`; with 100 observations
it is 0.010 for clean data and 0.109 for the contaminated mixture. Monte Carlo
estimates vary. The intervals quantify Monte Carlo uncertainty for the simulator,
not the validity of every real contamination model. Degenerate intervals are
reported as an error, not silently replaced by a favorable result.

## Important boundaries

The optional Git lab creates temporary repositories on the hosted runner and removes them when
finished. It uses synthetic identity/data and isolated Git configuration, with no
network or GitHub authentication. Its observations do not complete a learner's
independent tasks or prove a real GitHub PR, policy, deployment, or account setting.
See [the hands-on labs](../practice/GITHUB_LABS.md) for learner-controlled practice.

The tracker is a single-writer teaching app and does not guarantee crash durability.
The reporter loads its records in memory and limits minutes text to nine ASCII
digits. The async transform must cooperate with cancellation; a blocked CPU loop
cannot be forcibly stopped by a normal async timeout. The inventory lab does not
deduplicate remote operations. The timing harness is intentionally modest; it
does not control CPU frequency, process isolation, or input-family generalization.
