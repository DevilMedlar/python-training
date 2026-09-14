# Reference programs

Try the corresponding lesson or capstone first. These are inspectable reference
implementations, not hidden answer keys or complete production systems. The
standard-library examples target Python 3.12–3.14. Run module commands from the
repository root; use your environment's `python`, `python3`, or `py` command.

| Program | Lesson purpose | Run or inspect |
|---|---|---|
| [drills.py](drills.py) | Selected beginner solutions with explicit preconditions | Attempt the beginner drills first |
| [study_tracker.py](study_tracker.py) | Beginner functions, validation, JSON, optional safer save | `python -m examples.study_tracker --file progress/sessions.json` |
| [studylog.py](studylog.py) | Strict CSV, records, aggregation, CLI failures | `python -m examples.studylog examples/data/sessions.csv` |
| [contracts.py](contracts.py) | Typed synchronous decorator and reporting contract | Read with `tests/test_contracts.py` |
| [pipeline.py](pipeline.py) | Fixed workers, bounded queue, failure/cancellation cleanup | `python -m examples.pipeline` |
| [inventory.py](inventory.py) | Parameterized SQLite and owned transaction boundaries | Use a temporary database as in `tests/test_inventory.py` |
| [selection.py](selection.py) | Shared contract and independent algorithm oracle | Read with `tests/test_selection.py` |
| [benchmark_selection.py](benchmark_selection.py) | Raw timings and measurement scope | `python -m examples.benchmark_selection --size 1000 --k 10 --repeats 6` |
| [research_optional.py](research_optional.py) | Paired simulation and uncertainty | Optional instructions below |
| [topic_names.py](topic_names.py) | GH-09 behavior contract and regression practice | `python tools/run_tests.py --pattern test_topic_names.py` |
| [git_workflow_lab.py](git_workflow_lab.py) | Git snapshots, synchronization, conflicts, recovery, and mirror history | `python -m examples.git_workflow_lab` with Git 2.28+ |

Create `progress/` before the tracker command. That directory is ignored by Git.
The reporter prints `Python: 60 min` and `Testing: 20 min`, on separate lines.
The pipeline prints `285`. Benchmark durations vary; no fixed speedup is expected.

## Optional numerical experiment

Use a separate virtual environment. The recorded local reproduction used Python
3.12.14, NumPy 2.3.5, and SciPy 1.17.0. The pins identify that experiment; they are
not a claim that those are the newest releases or the only compatible environment.

```sh
python -m pip install -r requirements-research.txt
python -m examples.research_optional > research-result.json
python tools/run_tests.py --pattern test_research_optional.py
```

Keep generated results in private/ignored storage when they contain learner work.
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

The optional Git lab creates temporary local repositories and removes them when
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
