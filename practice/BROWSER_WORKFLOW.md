# Run Python through GitHub

Edit on github.dev, commit to GitHub, and read results on github.com. The provided
[Run Python lesson workflow](../.github/workflows/learn.yml) executes
`workspace/main.py` with Python 3.14 on a GitHub-hosted Ubuntu runner.

## Edit commit and inspect

1. Open [github.dev](https://github.dev/DevilMedlar/python-training) and the desired branch.
2. Edit `workspace/main.py` and any inputs or helper files needed by the lesson.
3. Inspect each change in Source Control, stage the intended files, and **Commit & Push**.
4. Open [Actions](https://github.com/DevilMedlar/python-training/actions/workflows/learn.yml).
   Workspace changes automatically run the lesson. Select your branch and commit.
5. Read the result summary and the **Run program** step. Inspect **Learner tests**
   when tests have been added. A successful script is not proof its logic is correct.

**Run workflow** starts the latest committed version of the branch you select.
**Re-run jobs** repeats the commit of that existing run. Unsaved or uncommitted
editor changes are absent from either run. Use the run URL and commit as evidence.
The manual button requires the workflow to be on the repository's default branch.
[Manual run documentation](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow).

## Inputs for input

For this program in `workspace/main.py`:

```python-template
name = input("Name: ")
minutes = int(input("Minutes: "))
print(f"{name}: {minutes + 5} minutes")
```

Put these lines in `workspace/input.txt`, with a line break after each answer:

```text
Python learner
25
```

Commit both files. The supplied answers are read in order; the final message is
`Python learner: 30 minutes`. Prompts may appear together because redirected input
is not echoed as if somebody typed it. Invalid text still produces a real Python
exception. To test a retry loop, supply invalid answers followed by a valid one.
For a menu, include the final quit choice. End of input raises `EOFError` if the
program requests another answer. Actions is a batch runner, not a live terminal.

The runner stops an ordinary lesson program after 30 seconds and records a failed
run. Use **Cancel workflow** for a queued or running job you no longer need.
Larger experiments need a deliberate, bounded workflow change with the tutor.

## Files and persistence

Execution starts in the repository root. Read committed synthetic input data
from `workspace/data/`. Write disposable outputs to `workspace/results/`, which
the runner creates. Small UTF-8 text, JSON, and CSV results are previewed on the
run summary, with limits clearly marked. A generated file is not a Git commit.

Every run starts from a fresh checkout. To use a small generated JSON result in
a later run, copy its complete preview into a file under `workspace/data/` in
github.dev and commit it. Do not copy a truncated preview. Test save-and-reopen
behavior within one run first; then demonstrate a new run with committed input.
For larger research outputs, design a workflow that preserves the required
artifacts on GitHub and presents inspectable summaries before relying on it.

Use made-up practice data. Code, committed data, and Actions logs in this repository
are public. An ignore rule does not remove an already committed file or its history.

## Modules tests and dependencies

The runner launches the module `workspace.main` from the repository root. Put
helpers beside it and import them as `from workspace.helpers import ...`. Avoid
filenames that shadow standard modules, such as `json.py`.

At `P1-10` and `P2-07`, add `workspace/test_*.py` files using `unittest`.
The **Learner tests** step runs them after a successful program run, rejects empty
test discovery when such files exist, and reports a real failure as a failed job.
Before tests are introduced, it explicitly reports that none were supplied.

The beginner code uses the standard library. When a later lesson needs a package,
edit `workspace/requirements.txt` in the browser and commit its specified versions.
The workflow installs them on the GitHub runner. Keep dependency choices tied to
the current Python task. Inspect the **Set up Python** and **Install lesson dependencies**
steps for environment information.

### Environment exercise for P1-11

In your practice branch, use github.dev to add this step to `learn.yml` before
**Run program**. These are workflow instructions executed by GitHub's Ubuntu
runner; you enter them in the YAML file, not in a laptop terminal:

```yaml
- name: Inspect a fresh Python environment
  run: |
    python -m venv /tmp/python-training-environment
    /tmp/python-training-environment/bin/python --version
    /tmp/python-training-environment/bin/python -m pip --version
```

Inspect the log and explain which interpreter owns that pip. This demonstration
does not switch the later program step into that environment. Remove the teaching
step after reviewing it, or retain it only if the lesson needs it.

### Advanced commands run in workflows

Later Python lessons include package builds, command-line interfaces, profilers,
and scientific runs. Put their commands in a named `run:` step of a lesson
workflow through github.dev; GitHub executes them. Run a short, finite workload
and read its log. No command in a lesson requires a laptop shell.

For the supplied scientific example, the tutor can add these runner steps on
the lesson branch. The recorded pins are in `requirements-research.txt`:

```yaml
- name: Install recorded scientific dependencies
  run: python -m pip install -r requirements-research.txt
- name: Run the teaching experiment
  run: python -m examples.research_optional
```

The existing **Verify Python tutor** research job tests a smaller experiment;
it does not claim to have run the full default investigation.

## Read the course checks

Open [Verify Python tutor](https://github.com/DevilMedlar/python-training/actions/workflows/verify.yml)
and choose **Run workflow**, or inspect its PR checks. It checks the curriculum,
reference programs, and progress records. **Run Python lesson** executes your
workspace. Keep their purposes clear when explaining a green or red result.

## If something goes wrong

| What you see | Next browser action |
|---|---|
| Output still shows the old code | Confirm Commit & Push completed; open the run for that commit and branch |
| Workflow is queued | Wait for a runner; queued does not mean failed |
| No automatic run after a docs-only change | Use Run workflow; automatic lesson runs watch workspace and runner files |
| Actions disabled or a permission message | Read the repository's Actions notice and use your account's allowed controls; do not switch to laptop setup |
| `SyntaxError` | Read the file and line in the log, repair the syntax in github.dev, and commit |
| `EOFError` | Supply enough lines in input.txt, including a menu exit choice |
| `ModuleNotFoundError` | Check the workspace import path or the lesson's requirements file |
| Timeout | Inspect loop termination and input size, then commit a bounded attempt |
| A result file is missing on a later run | Commit required sample input; a previous runner's files are temporary |

Sources: [github.dev](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor),
[Python in Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python),
[job summaries](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#adding-a-job-summary).
