# GitHub task cards inside Python practice

Use the card linked to the Python work you are doing. These are browser steps
for that exercise, not another curriculum. Work on your Python files through
github.dev and inspect results on github.com.

## Lab A Your first browser PR

Use with **P1-08 functions**, then reuse for later Python features.

1. From current main, create a branch named for the function change.
2. Edit the Python function in github.dev. Inspect the diff, stage the intended
   files, and Commit & Push.
3. Open its Run Python lesson result. Explain the output and any boundary cases.
4. On github.com, create a PR with main as base and your branch as compare.
5. Read Files changed and the checks. Describe the Python contract, change, and
   observed result. Merge only after reviewing those facts and the intended scope.

Explain what editing, committing, opening a PR, and merging each changed. Your
function task supplies the learning content; no unrelated README exercise is needed.

## Lab B See what staging records

Use with **P1-02 arithmetic** and **P1-09 mutation**.

1. Change one Python expression and inspect its Source Control diff.
2. Stage the file with +. Make another edit to the same line.
3. Inspect staged and unstaged views, and predict the staged version.
4. Stage the final intended version, Commit & Push, and confirm it on github.com.
5. Match the Actions output to that commit and explain the Python calculation.

Do not discard an edit as part of this exercise. Inspecting and staging are enough
to demonstrate which snapshot is recorded.

## Lab C Keep your Python branch current

Use with **P2-11 packaging**.

Compare your branch with current main on github.com. If an older PR needs a newer
main change, inspect and use Update branch when available, then inspect its new
checks. Otherwise preserve the old branch, make a fresh branch from main, and
reapply the small package change in github.dev. Review the replacement PR diff
and link the old PR before closing it as superseded. Explain which package code
the hosted build actually tested.

## Lab D Resolve a simple Python conflict

Use with **P2-11 packaging and collaboration** on disposable practice branches.

1. Create two branches from the same main version. Give the same Python output
   line a different edit in each branch.
2. Merge the first small PR after checking its output. Open the second PR.
3. When GitHub offers Resolve conflicts, state the required final output, edit
   the competing text, remove conflict markers, and Mark as resolved.
4. Commit merge. This brings the entire base branch into the head branch;
   inspect all resulting changes and run the Python checks.
5. Explain why resolving text alone does not prove the program correct.

If the browser cannot resolve that conflict, keep both branches and use Lab C's
fresh-branch method. Do not switch to a laptop or claim the original conflict was
resolved. [GitHub conflict documentation](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-on-github).

## Lab E Recover a Python regression

Use with **P1-10 debugging** and later Python maintenance.

Find the earlier intended function through file history on github.com. Make a
focused repair in github.dev and add the regression case to the Python tests.
Commit it and inspect the new run. Explain what remains in history.

For an eligible merged PR, inspect GitHub's Revert-created PR before merging it.
If that operation conflicts, use a targeted new fix from main. A revert is not a
general credential-removal method. An ignore rule does not delete committed history.

## Hosted history demonstration

The **Verify Python tutor** workflow runs
[git_workflow_lab.py](../examples/git_workflow_lab.py) in temporary repositories
on its GitHub-hosted runner. Open the corresponding job log to inspect staged
snapshots, conflicts, and restoration invariants. This is an implementation
demonstration, not an instruction to install Git or a substitute for your own
reviewed Python work.

## Lab F A test that can fail

Use with **P1-10** and **P2-07**.

Create workspace/test_*.py for a function you are learning. Commit a deliberately
wrong implementation on a practice branch and inspect the expected test failure.
Repair it and inspect a new run. Confirm the test imports the changed function,
the discovered count is positive, and the failure was about the intended behavior.
The reference normalizer and its tests can be read after your independent attempt.

## Python capstones include the contribution review

Use the [five Python capstones](CAPSTONES.md). Deliver the same Python project
with its contract, source, tests or appropriate acceptance evidence, observed
Actions runs, reviewed PR, and explained next improvement. There is no additional
GitHub graduation project. Record the Python reasoning and GitHub action together.
