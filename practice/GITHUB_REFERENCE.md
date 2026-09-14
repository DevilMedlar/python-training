# Browser reference for Python work

Look up the action required by your current Python lesson. All edits happen in
github.dev; execution and review happen on github.com.

## Daily workflow

Predict the Python result → edit the file → inspect the diff → Commit & Push →
open the matching Actions run → explain the result → try a fresh case.
From P1-08 onward, use a branch and PR when practicing a feature change.

## Browser action effects

| Action | What changes or appears | What to check |
|---|---|---|
| Save an editor buffer | Browser-held edit | It has not necessarily reached GitHub |
| Stage with + | Selected content for the next commit | Inspect staged and unstaged versions |
| Commit & Push | A new committed version on the selected GitHub branch | Confirm file and commit on github.com |
| Create branch | Another branch based on the selected version | Start from current main for new work |
| Run workflow | A new run for the chosen branch's committed version | Workflow, branch, commit, output |
| Re-run jobs | Another attempt of the existing run's commit | It does not pick up a newer editor change |
| Create PR | A proposal from head branch into base | Python contract, Files changed, checks |
| Merge PR | Incorporates reviewed changes into the base | Final source and observed checks |
| Revert PR | Proposes an inverse change in a new PR when supported | Scope, conflicts, and Python tests |
| New fix commit | Repairs current code while preserving history | Regression case and relevant diff |

## Search by result type

Search code for an implementation, issues for a reported behavior, and repositories
for projects. Use `repo:DevilMedlar/python-training` to narrow a GitHub search.
Use permanent code links for a result that depends on one version. Keep relative
links in the course's own Markdown.

## Python execution

Use [Run Python lesson](https://github.com/DevilMedlar/python-training/actions/workflows/learn.yml)
for workspace/main.py and
[Verify Python tutor](https://github.com/DevilMedlar/python-training/actions/workflows/verify.yml)
for maintained course checks. Record the run URL, commit, relevant output, and
test count. Queued, skipped, cancelled, and passed are different states.

`input()` reads workspace/input.txt. Generated files are temporary runner files
unless deliberately preserved; source commits persist on GitHub. See the complete
[browser workflow](BROWSER_WORKFLOW.md) for file, package, and workflow instructions.

## Troubleshooting

| Problem | Browser check |
|---|---|
| Old output | Confirm commit and branch; start a new run of the correct version |
| Code will not run in github.dev | Open Actions on github.com; the editor has no runtime |
| Missing input | Add one line per input() call, including an exit choice for a menu |
| Failed Python run | Read the exception and line number; fix and commit a new attempt |
| PR conflict | Use the simple web conflict editor when supported, or a preserved replacement branch from main |
| Test badge looks green | Inspect which tests ran, their count, and which code they exercised |
| Package missing | Check the committed lesson requirements and the hosted install step |

For definitions and primary sources, use the [GitHub reference cards](../curriculum/github.md).
