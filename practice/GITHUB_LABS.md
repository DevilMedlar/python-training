# GitHub hands-on labs

Use these with the [GitHub track](../curriculum/github.md). The tutor should ask
for a prediction, wait for your attempt, and record actual results. Reading a
completed demonstration is guided practice, not independent evidence.

Browser work uses a practice repository you own. Local history exercises use
new disposable directories. Choose unused names if an example directory exists.
Use synthetic text and your chosen commit identity; never add real credentials.
The shell commands below work in Git Bash or PowerShell when Git is installed.
Create/edit file content in your editor where instructed.

## Lab A Your first browser PR

1. Create `github-practice` in your GitHub account, choose its visibility, and
   initialize a README. Private is a useful choice for personal practice.
2. From its actual default branch, create `practice/first-edit`.
3. Edit README to add one learning goal and commit to that branch.
4. Open a PR. Name the base and compare/head branches before proceeding.
5. Inspect Files changed and explain exactly which content would reach the base.
6. Add a second small commit to the same branch; find it in the existing PR.
7. When the practice change is complete and permitted, merge through GitHub.
8. Open the default branch and verify the result. Delete the completed remote
   branch only after you have confirmed the work is preserved.

**Transfer:** Repeat with a different change. Explain why creating the branch,
committing, opening the PR, and merging are four distinct state changes. If you
cannot use a GitHub account, rehearse the states and mark execution as pending.

## Lab B See what staging records

Create a new directory outside this course checkout and open a terminal there:

```sh
git init -b main
git config user.name "Your Name"
git config user.email "YOUR-CHOSEN-EMAIL"
```

Replace the identity placeholders with your chosen values. Create `README.md`
containing the single line `one` and a `.gitignore` containing:

```gitignore
.venv/
__pycache__/
.env
.env.*
!.env.example
```

Record the starting snapshot:

```sh
git add README.md .gitignore
git diff --staged
git commit -m "Create practice snapshot"
git switch -c practice/staging
```

Change README to `two`, run `git add README.md`, then change it to `three`.
Predict the following outputs before running the commands:

| Inspection | Content it should reveal |
|---|---|
| `git show HEAD:README.md` | `one` in the current commit |
| `git show :README.md` | `two` in the index |
| Your editor | `three` in the working tree |
| `git diff --staged` | The change from `one` to `two` |
| `git diff` | The change from `two` to `three` |

Commit the staged version, inspect `HEAD:README.md`, then run:

```sh
git add README.md
git restore --staged -- README.md
git status
```

The file still contains `three`. To finish with a clean practice branch, stage
that intended version, inspect it, and commit it. Unstaging itself did not save
or discard the working change.

**Transfer:** Add two new files and commit only one. Show how you verified both
the included content and the remaining untracked file.

## Lab C Synchronize a local remote

This experiment needs no GitHub account or internet. In a new parent directory,
create a bare repository and an ordinary clone:

```sh
git init --bare -b main github-remote.git
git clone github-remote.git work
cd work
git config user.name "Your Name"
git config user.email "YOUR-CHOSEN-EMAIL"
```

Create README with a learning goal, commit it, and push:

```sh
git add README.md
git commit -m "Record first learning goal"
git push -u origin main
cd ..
git clone github-remote.git peer
cd peer
git config user.name "Your Name"
git config user.email "YOUR-CHOSEN-EMAIL"
```

In `peer`, add a second goal to README, commit, and push `main`. Return to `work`:

```sh
cd ../work
git rev-parse HEAD
git fetch origin
git log --oneline HEAD..origin/main
git rev-parse HEAD
git pull --ff-only origin main
```

Fetch discovers the peer's commit without moving your current branch. The final
pull integrates it. This verifies local Git transport, not GitHub authentication,
permissions, branch rules, or PR behavior.

**Transfer:** Before fetching, make a different local commit that changes the
same line as a peer commit. Show that fast-forward-only integration refuses and
explain which two histories now need a deliberate decision.

## Lab D Conflict, abort, and reconcile

In a disposable repo with a committed README and clean status:

1. Create `practice/conflict`, change one existing line to `Learn loops`, and commit.
2. Switch to `main`, change that same original line to `Learn functions`, and commit.
3. Switch back to `practice/conflict`, confirm a clean status, then merge:

```sh
git merge main
git status
git diff
```

Both branches changed the same base line. Inspect the conflict and then run
`git merge --abort`. Confirm your branch's committed text is back. Repeat the
merge and edit the final text to `Learn loops and functions`; remove all markers.

```sh
git add README.md
git diff --staged
git commit -m "Combine both learning goals"
git log --oneline --graph --all
```

**Transfer:** Resolve a different conflict using stated behavior requirements.
Explain why marker-free text can still be wrong. Do not apply a merge-abort
promise to a situation that began with uncommitted work.

## Lab E Recovery and ignore rules

Use a clean disposable repo with at least one committed file. Inspect both diffs
before each experiment and predict what will remain afterward.

| Experiment | Observation to establish |
|---|---|
| Edit, stage, then `git restore --staged -- README.md` | Working edits remain; staged change is removed |
| Then `git restore -- README.md` | The unstaged edit is discarded in favor of the index version |
| Edit README, add an untracked note and an ignored synthetic `.env`, then `git stash push -u` | Tracked/untracked work is stashed; ignored `.env` remains |
| `git stash apply 'stash@{0}'` | Work returns and the stash is retained; conflicts are possible |
| Make a new ordinary mistake commit, then `git revert --no-edit COMMIT-ID` | A new inverse commit appears; the original remains in history |
| Identify a recorded commit, then `git branch rescue COMMIT-ID` | A reference keeps that recorded history reachable |

Verify `.env` is ignored and `.env.example` can be tracked. The example file must
contain placeholders only. `git check-ignore -v -- FILE` identifies a matching
ignore rule; `git ls-files -- FILE` tells you whether a path is tracked.
Adding an ignore rule does not erase old commits.

**Transfer:** Diagnose staged, unstaged, shared-commit, and lost-reference scenarios.
Explain why `revert` and `restore` are not interchangeable and why a reflog is not
a guarantee of recovering edits never recorded by Git.

## Automated offline demonstration

From the course repository root, after inspecting the script, run:

```sh
python -m examples.git_workflow_lab
```

The [script](../examples/git_workflow_lab.py) creates temporary repositories and
a local bare remote. It tests seven groups of Git invariants and removes its
temporary files when finished. It uses isolated configuration and synthetic
commit identity. Git is an additional requirement for this optional lab; the
ordinary Python examples still need only their documented dependencies.
These labs use `git init -b`, requiring [Git 2.28 or later](../audit/SOURCES.md#git-init).

Predict each observation before reading the code. Running this demonstration
does not establish that you independently performed a GitHub PR, account setup,
Codespaces session, or repository setting change.

## Lab F A test that can fail

From a practice copy or branch of this course, inspect
[topic_names.py](../examples/topic_names.py), then run:

```sh
python tools/run_tests.py --pattern test_topic_names.py
```

Expect six passing tests in the maintained version. Remove `.lower()` from the
implementation temporarily and rerun. Inspect the failing lowercase assertion,
then restore only your deliberate experiment and verify a passing run.

To demonstrate empty discovery, use a pattern that matches no test file:

```sh
python tools/run_tests.py --pattern test_does_not_exist_*.py
```

This command must fail with "No tests discovered". It is an intentionally
unsuccessful check, not the normal project validation command. Do not remove
failing tests or change their expected values merely to get a green result.

**Transfer:** Add a useful new requirement, design a test from that requirement,
and show that it distinguishes the old and new behavior. Empty discovery and
passing irrelevant tests are different problems.

## GitHub capstone A reviewable Python contribution

Choose a small documentation or behavior improvement in a practice copy/fork of
the Python course. Use a real need, not an invented error. Deliver:

- A precise starting commit, branch, and acceptance criteria.
- A focused change with a corresponding lesson/example/test update where needed.
- A PR or, if remote access is unavailable, a clearly labeled local proposal.
- Actual checker/test outputs tied to the proposed change, including counts/skips.
- A demonstrated relevant failure and correction, plus reviewed final diff.
- An explanation of one recovery choice and how the work is preserved.
- A short handoff with the merge choice, release/backup considerations, and remaining limits.

For the complete GitHub capstone, demonstrate a real branch push and PR workflow
in a repository where you have permission. A local proposal can meet a partial
milestone; it must not be recorded as a completed remote collaboration task.
Another person's response is not required to show your own review, but do not
invent a human or AI review that did not occur. Merge only when it is in scope.

Use independent/reference support for the final assessment, followed by a new
transfer task such as revising the PR after an actual or clearly simulated
requirement change. Record completion under `capstones.github` using the same
evidence fields as the Python capstones. No paid plan or automatic AI review is
required to complete this project.
