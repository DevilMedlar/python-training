# Python Training on GitHub

Learn Python while using GitHub to save, run, review, and improve the same Python
work. All learner work happens through **github.com** and **github.dev**.
GitHub skills are built into the five Python phases, with one lesson sequence,
one progress record, and one set of projects.

## Start learning

1. Follow [START_HERE.md](START_HERE.md) for your first Python edit and run.
2. Open [the browser editor](https://github.dev/DevilMedlar/python-training).
3. Edit [workspace/main.py](workspace/main.py), then **Commit & Push**.
4. On github.com, open [Actions → Run Python lesson](https://github.com/DevilMedlar/python-training/actions/workflows/learn.yml)
   and open the run for your commit. Read its **Python lesson result** summary.
5. Use [one tutor launch prompt](tutor/START_PROMPT.md) and begin at `P1-01`,
   or resume from [your progress record](tutor/progress.json).

`github.dev` is the editor. **GitHub Actions runs Python on GitHub-hosted machines**;
the result comes back to a page on github.com. github.dev itself has no Python
runtime or terminal. No Python, Git, desktop editor, or command line needs to be
installed on your laptop. [GitHub's editor documentation](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)
and [Python Actions documentation](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)
explain these roles.

## One learning route

| Python phase | What you build and learn | GitHub used in that work |
|---|---|---|
| [1 — Novice](curriculum/phase-1.md) | Values, decisions, loops, functions, debugging, files; a study tracker | Edit and commit Python; inspect output and diffs; introduce a branch and PR with a function change |
| [2 — Practitioner](curriculum/phase-2.md) | Tested modules, data, APIs, SQL, packaging; a report application | Tests in Actions, feature PRs, issue descriptions, simple conflicts, a release draft |
| [3 — Expert](curriculum/phase-3.md) | Architecture, concurrency, profiling, reliable delivery | Review design changes, compare runs, inspect permissions and failure checks |
| [4 — Researcher](curriculum/phase-4.md) | Reproducible computational investigation | Commit protocols and configurations, link runs to code, review evidence and limitations |
| [5 — Creator](curriculum/phase-5.md) | Useful original contribution and maintenance | Contribution review, release notes, compatibility evidence, maintenance and recovery |

The [lesson index](curriculum/INDEX.md) pairs each Python lesson with a specific
GitHub action on its code. `GH-` IDs are lookup references used inside those
lessons; they do not create another course or a second graduation requirement.
These phases are informal learning directions, not academic credentials.

## During a lesson

Predict the result, edit a small program, commit it, inspect its Actions run,
explain what happened, and try a fresh challenge. The tutor introduces only the
GitHub controls needed for that Python task. YAML and automation internals come
later; running the first program only requires browser controls.

Use [workspace/input.txt](workspace/input.txt) for answers to `input()` prompts.
Actions reads them in order; it does not accept live typing during a run.
See [the browser workflow](practice/BROWSER_WORKFLOW.md) for inputs, files,
dependencies, checks, and troubleshooting.

## Course material

- [Tutor instructions](tutor/INSTRUCTIONS.md), [teaching playbook](tutor/TEACHING.md),
  [placement](tutor/PLACEMENT.md), and [progress](tutor/PROGRESS.md).
- [Python capstones](practice/CAPSTONES.md), [beginner drills](practice/BEGINNER_DRILLS.md),
  [assessment](practice/ASSESSMENT.md), and [glossary](curriculum/GLOSSARY.md).
- [GitHub reference](curriculum/github.md) and [browser task cards](practice/GITHUB_LABS.md),
  consulted from the current Python lesson.
- [Reference programs](examples/README.md), tests, and [contribution instructions](CONTRIBUTING.md).
- [Input provenance](audit/INPUTS.md), [primary sources](audit/SOURCES.md),
  [claim audit](audit/CLAIM_AUDIT.md), and [verification history](audit/VERIFICATION.md).

The executable core targets Python 3.12–3.14. Open
[Actions → Verify Python tutor](https://github.com/DevilMedlar/python-training/actions/workflows/verify.yml)
to inspect or manually run course checks on GitHub. Actual run results establish
what passed. The [MIT license](LICENSE) applies to repository content.
