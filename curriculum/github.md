# Git and GitHub companion track

Learn to understand a repository, share a small change, review evidence, and
recover deliberately. Start with `GH-01` or ask the tutor to check the skills you
already use. The browser lessons require no Python. `GH-09` introduces a Python
project and lists the Python prerequisites explicitly.

This track adapts the supplied GitHub Practical Reference after a separate
[audit](../audit/GITHUB_AUDIT.md). Use the [lesson index](INDEX.md),
[hands-on labs](../practice/GITHUB_LABS.md), and
[command and troubleshooting reference](../practice/GITHUB_REFERENCE.md).
Track progress with `python tools/progress.py progress/progress.json --next --track github`.
The track is optional alongside the five Python phases, not a sixth rank.

Commands assume the intended repository and branch. Replace uppercase
placeholders, read `git status`, and explain a command's target before changing
files or history. `main` is an example default branch; inspect the actual one.

## GH-01 Read a repository and choose the right copy

**Prerequisites:** None.

**Outcome:** Find a project's purpose, license, version, and checks, and distinguish a ZIP, clone, fork, template, and branch.

Git records file history. GitHub hosts Git repositories and collaboration tools.
A commit records a snapshot; a branch names a moving line of work. A pull request
proposes a change between branches. Downloading files neither installs a program
nor grants permission to push changes back to their source.

| Choice | Result | Typical reason |
|---|---|---|
| ZIP | Selected files without a working Git history | Read a snapshot |
| Clone | Local repository and remote configuration | Develop with history |
| Fork | Related repository under another owner | Propose an upstream contribution |
| Template | New project with independent history | Reuse an intended starting structure |
| Branch | Another reference in one repository | Develop a focused change |

Inspect README, license, supported versions, examples, tests, recent PRs, and
release notes. Stars or a green badge alone cannot establish quality. Public
visibility is not an open-source license. For repeatable evidence, use a
commit-specific file link; GitHub's `y` shortcut can create one from a file view.

**Worked example:** A ZIP lets you read this guide. A clone lets you run checks and
commit locally. A fork supplies a destination you can push to when you lack
upstream write access. None of those operations means your change was merged.

**Practice A:** Locate this repository's entry point, license, verification report,
and one lesson's primary source. Explain what each establishes.

**Practice B:** Choose a copy method for reading offline, contributing a fix, and
starting an independent project. Explain one limit of each choice.

**Hints:** Ask whether you need history, write access, or a new independent origin.

**Evidence:** Correct choices and a commit-specific reference, with a distinction
between an observed check and a project's unsupported claim.

**Sources:** [GH-CLONE](../audit/SOURCES.md#gh-clone), [GH-TEMPLATE](../audit/SOURCES.md#gh-template), [GH-LICENSE](../audit/SOURCES.md#gh-license), [GH-PERMALINK](../audit/SOURCES.md#gh-permalink).

## GH-02 Complete a browser pull request

**Prerequisites:** GH-01.

**Outcome:** Make a small browser edit on a branch and explain its path through a pull request into the default branch.

Use a practice repository you own. Create it with a README, then create a branch
such as `practice/first-edit`. Edit one learning goal and commit it to that branch.
Open a PR whose base is the default branch and whose compare/head is your branch.
Review Files changed before merging. Merging requires the appropriate permission
and any configured checks or reviews.

Commit, push, and merge are different events. A browser commit is already stored
on GitHub; a local commit still needs a push to reach a remote. Opening a PR does
not itself change the base branch. An additional commit on its head branch updates
the same open PR.

**Worked example:** `main` says "Learn loops." Your branch adds "Explain the stop
condition." The PR proposes that extra sentence. After a successful merge, the
sentence appears in `main`; verify by opening that branch, not the old edit view.

**Practice A:** Complete [Lab A](../practice/GITHUB_LABS.md#lab-a-your-first-browser-pr)
and describe the change before and after merge.

**Practice B:** Make a second, different edit. Identify the base and head without
copying the first task's answers; add a follow-up commit to the same PR.

**Hints:** Read the branch selector and the PR's base/compare fields.

**Evidence:** Actual branch and PR states plus a correct explanation. If an account
or permission is unavailable, record the workflow as rehearsed, not executed.

**Sources:** [GH-HELLO](../audit/SOURCES.md#gh-hello), [GH-FLOW](../audit/SOURCES.md#gh-flow).

## GH-03 Set up tools and authenticate

**Prerequisites:** GH-02.

**Outcome:** Choose a working GitHub tool and distinguish commit identity, sign-in, repository access, and execution capability.

The website handles reading, small edits, issues, and reviews. Desktop supplies a
visual local workflow on supported Windows/macOS systems. Git CLI manages history;
the separate `gh` CLI manages GitHub features. `github.dev` edits files but has no
terminal or compute runtime. Codespaces supplies compute, with usage limits.

On Windows, install Git through its official installation resources and check
`git --version` in a new PowerShell or Git Bash session. Use your chosen editor.
Set a real author name and chosen email; a GitHub no-reply email is an option.
Repository-local `git config user.name` and `user.email` settings affect that
repository; `--global` affects your user configuration. Neither authenticates you.

For HTTPS, use a supported credential manager or `gh auth login --web`, then
`gh auth setup-git` if Git needs that CLI-managed credential integration. Follow
sign-in yourself. `gh auth status` inspects the connection without printing a token.
SSH uses an authorized key. An ordinary account password is not a Git-over-HTTPS
password. Token permissions, organization policy, and repository rights still apply.

**Worked example:** A commit can show your name while `git push` fails with an
authentication error. The author metadata succeeded; remote authentication did not.

**Practice A:** Record your chosen tool, Git version, and working sign-in method
without including credentials. Explain which actions that connection permits.

**Practice B:** Diagnose "I can read the repo, but cannot push" and "I opened
github.dev, but cannot run Python" as two different capability questions.

**Hints:** Separate identity, access, and compute. Read a token's supported use case
before choosing it; fine-grained tokens still have documented feature gaps.

**Evidence:** A sanitized capability record and an explanation of the actual failure
boundary; no secret, key, recovery code, or token in the progress record.

**Sources:** [GH-SETUP](../audit/SOURCES.md#gh-setup), [GH-AUTH](../audit/SOURCES.md#gh-auth), [GH-TOKENS](../audit/SOURCES.md#gh-tokens), [GH-DEV](../audit/SOURCES.md#gh-dev), [GH-CLI-AUTH](../audit/SOURCES.md#gh-cli-auth), [GH-DESKTOP](../audit/SOURCES.md#gh-desktop).

## GH-04 Understand working files and staged snapshots

**Prerequisites:** GH-03.

**Outcome:** Predict which exact file content a commit will record after editing and staging.

The working tree is the file content you can edit. The index, also called the
staging area, holds the proposed next snapshot. `HEAD` usually refers through
your current branch to its latest commit. Staging copies content at that moment;
later edits do not silently update the staged copy.

Run `git status`, `git diff`, and `git diff --staged`. The first reports state;
the second shows unstaged tracked changes; the third shows staged changes.
Untracked files require separate inspection. Stage named files while learning.
A branch name is a reference, not a second permanent copy of your folder.

**Worked example:** Commit a file containing `one`. Edit it to `two` and stage it.
Edit it again to `three`. A commit now records `two`; `three` remains an unstaged
working-tree change. [Lab B](../practice/GITHUB_LABS.md#lab-b-see-what-staging-records)
makes this visible before any remote operation.

**Practice A:** Perform the three-version experiment, predicting both diffs before
reading them. Unstage the change and verify that the working file survives.

**Practice B:** Create two files but stage only one. Explain the resulting commit
and show how you verified the second file was not included.

**Hints:** Compare working tree to index, then index to `HEAD`.

**Evidence:** Correct predictions, actual command output, and a commit containing
exactly the intended staged content.

**Sources:** [GIT-BOOK](../audit/SOURCES.md#git-book), [GIT-RESTORE](../audit/SOURCES.md#git-restore).

## GH-05 Synchronize remotes without guessing

**Prerequisites:** GH-04.

**Outcome:** Use fetch, an explicit fast-forward update, and a targeted push while naming the affected local and remote branches.

`origin` is a conventional remote name, not a special GitHub permission. Fetch
downloads objects and updates remote-tracking references; it does not automatically
replace your working files. Pull fetches and integrates into the branch currently
checked out. `git pull --ff-only origin main` does not switch you to `main`.

Start clean. To update local `main`, switch to it, then use the explicit fast-forward
pull. Create a feature branch, make and verify a focused commit, then push that
branch with `git push -u origin BRANCH`. The `-u` records its upstream tracking
relationship. If a push is rejected, fetch and inspect the histories.

For an existing local folder without Git history, create an empty GitHub repo,
initialize locally, review and commit named files, add its clone URL as a remote,
then push. If GitHub already contains commits, cloning it and copying your intended
files into that clone is often easier. Preserve any existing local history.

**Worked example:** Your local `main` and `origin/main` point to commit A. A peer
pushes B. Fetch updates `origin/main` to B; local `main` remains A until you
integrate. If you independently made C, a fast-forward-only update refuses.

**Practice A:** Use [Lab C](../practice/GITHUB_LABS.md#lab-c-synchronize-a-local-remote)
or the offline demonstrator to observe the references before and after fetch.

**Practice B:** Explain how you would upload an existing project when the GitHub
repo is empty versus when it already has a README commit.

**Hints:** Inspect `git branch -vv` and the recent graph. A tree-view URL is not a
repository clone URL. Never treat a force push as an authentication repair.

**Evidence:** Correct target branches, actual synchronization results, and an
explanation of why the fast-forward refusal preserves a decision for the learner.

**Sources:** [GIT-PULL](../audit/SOURCES.md#git-pull), [GH-CLONE](../audit/SOURCES.md#gh-clone), [GIT-BOOK](../audit/SOURCES.md#git-book).

## GH-06 Review contributions and choose a merge method

**Prerequisites:** GH-05.

**Outcome:** Prepare a focused PR or fork contribution and explain the resulting merge history.

Review the diff, relevant tests, supported versions, and the problem the change
claims to solve. State what actually ran. A green workflow is evidence about its
commands, not a proof of all behavior. A draft PR is useful for work still in progress.

Without upstream write access, fork and clone your fork. Name the original remote
`upstream`, fetch it, and start a feature branch from its intended base. Push to
your fork. The PR's base repository is upstream; its head is your fork and branch.
Follow the project's contribution instructions before proposing changes.

| Method | Typical result |
|---|---|
| Merge commit | Retains branch commits and records a merge point |
| Squash | Creates one combined base-branch commit |
| Rebase and merge | Replays commits in a linear base-branch history |

Repository settings determine available methods. Squash/rebase changes commit
identity or ancestry; a local `git branch -d` may subsequently refuse. Confirm
content preservation instead of escalating blindly to forced deletion.

**Worked example:** A PR contains an implementation commit and two fixes. A squash
merge puts their combined result in one new base commit. Those original three
commits need not become ancestors of the base branch.

**Practice A:** Write a PR description with problem, change, checks, and limits;
identify its exact head and base. Inspect a follow-up commit in the same PR.

**Practice B:** Explain a fork contribution and choose a merge method for a second
scenario. Predict what happens to the individual commit IDs.

**Hints:** A remote branch with your commits is not evidence that a PR was merged.

**Evidence:** Review notes tied to actual changed lines and a correct account of
ownership, branch direction, and the chosen history.

**Sources:** [GH-FLOW](../audit/SOURCES.md#gh-flow), [GH-FORK](../audit/SOURCES.md#gh-fork), [GH-MERGES](../audit/SOURCES.md#gh-merges).

## GH-07 Resolve a conflict and verify the combined result

**Prerequisites:** GH-06.

**Outcome:** Reproduce a merge conflict, abort it from a clean start, then resolve and test the intended combined content.

A conflict asks you to choose a coherent final result. It does not mean Git lost
the project. Start with committed work before a practice merge. Inspect the named
files, reconcile the content, remove markers, run relevant checks, stage the
resolved files, and finish the merge.

For a merge from that clean start, `git merge --abort` restores the pre-merge
situation. With pre-existing uncommitted changes, reconstruction is not always
possible. A rebase has its own continue/abort commands; "ours" and "theirs" can
be misleading during rebasing. Do not mechanically accept one side.

**Worked example:** One branch changes the same learning-goal line to "loops" and
another to "functions." The intended resolution is "loops and functions," which
requires an explicit content decision. The offline lab checks that both branch
histories are retained in the merge commit.

**Practice A:** Follow [Lab D](../practice/GITHUB_LABS.md#lab-d-conflict-abort-and-reconcile).
Abort once, confirm the original file, then resolve and inspect the result.

**Practice B:** Given different requirements on each branch, write the combined
acceptance criteria before editing conflict markers. Explain a test that could
fail even after all markers are removed.

**Hints:** Git can detect overlapping text; it cannot establish the application's
intended behavior. A clean merge can still introduce a logical defect.

**Evidence:** A clean-start abort, a deliberate resolution, a reviewed merge diff,
and relevant checks on the combined behavior.

**Sources:** [GIT-MERGE](../audit/SOURCES.md#git-merge), [GIT-RESTORE](../audit/SOURCES.md#git-restore).

## GH-08 Recover deliberately and keep private files out

**Prerequisites:** GH-07.

**Outcome:** Select a recovery operation for staged, unstaged, committed, and temporarily saved work without confusing their effects.

`git restore --staged -- FILE` normally restores the index from `HEAD`, leaving
working edits. `git restore -- FILE` normally replaces working content from the
index and discards its unstaged edits. `--source=COMMIT` selects a different source.
Use disposable files while learning these differences.

`git revert COMMIT` records a new inverse commit; it does not erase the original.
Reverting a merge needs a considered mainline parent. `git stash push -u` includes
untracked files but not ignored files; `stash apply` retains the stash and can
conflict. Stashes and reflogs are local, not ordinary pushed backups. Reflogs can
help locate recorded commits but expire and cannot recover arbitrary unsaved work.

Ignore virtual environments, caches, generated output, and private progress.
Ignore rules do not remove tracked files or earlier commits. Review any deliberate
`git rm --cached FILE` change; it stops tracking while keeping the local file.
Credential exposure requires revocation/rotation first, not just deleting a file.

**Worked example:** Staging a private placeholder by accident calls for unstaging
before committing. A real leaked token calls for credential response even if its
file has since disappeared. These are different states and different remedies.

**Practice A:** Use [Lab E](../practice/GITHUB_LABS.md#lab-e-recovery-and-ignore-rules)
with synthetic content to unstage, restore, stash/apply, and revert.

**Practice B:** Diagnose four supplied states and name both the source and destination
of the proposed recovery. Explain what evidence would be lost by the wrong choice.

**Hints:** Inspect both diffs first. `reset --hard`, `clean -fd`, and force pushes
are destructive tools, not routine setup repairs.

**Evidence:** Preserved intended content, correct inverse history, and a clean
distinction between ignored, untracked, staged, and previously committed files.

**Sources:** [GIT-RESTORE](../audit/SOURCES.md#git-restore), [GIT-REVERT](../audit/SOURCES.md#git-revert), [GIT-STASH](../audit/SOURCES.md#git-stash), [GIT-REFLOG](../audit/SOURCES.md#git-reflog), [GH-IGNORE](../audit/SOURCES.md#gh-ignore), [GH-SENSITIVE](../audit/SOURCES.md#gh-sensitive).

## GH-09 Review a small Python change with real tests

**Prerequisites:** GH-08, P1-10, P1-11.

**Outcome:** Connect a Python behavior contract to a focused commit and a test that detects a plausible regression.

Keep the established repository layout: explanations in `curriculum/`, practice
in `practice/`, maintained programs in `examples/`, and tests in `tests/`. Read
the actual test command instead of installing a copied template with nonexistent
folders. Create a virtual environment when dependencies need isolation.

The supplied reference's topic-normalization example is deliberately small:
lowercase text and join whitespace-separated words with hyphens. Punctuation
remains and empty input yields empty output. It is not a URL or filename sanitizer.

```python
def normalize_topic(topic):
    return "-".join(topic.lower().split())

print(normalize_topic("  Python\tBasics  "))
print(repr(normalize_topic("")))
```

```output
python-basics
''
```

The maintained implementation is [topic_names.py](../examples/topic_names.py).
Its tests cover the stated contract. The repository's test runner explicitly
rejects discovering zero tests; successful discovery alone still says nothing
about whether the tests are relevant or sufficient.

**Practice A:** Run the normalizer tests, remove lowercasing in a disposable copy,
observe the failing assertion, and restore the implementation.

**Practice B:** Propose a small new naming requirement. State its effect on punctuation,
Unicode, and empty input before changing code; add a meaningful example and test.

**Hints:** Type hints do not validate inputs. Do not turn an example's convenient
output into a broader security or naming guarantee.

**Evidence:** A focused diff, an observed failing regression, a restored passing
run, and an independent explanation of the contract.

**Sources:** [PY-TEXT](../audit/SOURCES.md#py-text), [PY-UNITTEST](../audit/SOURCES.md#py-unittest), [GH-PYTHON-CI](../audit/SOURCES.md#gh-python-ci).

## GH-10 Understand and inspect GitHub Actions

**Prerequisites:** GH-09.

**Outcome:** Read a workflow's trigger, permissions, jobs, matrix, and logs, and distinguish a passing check from a skipped or absent one.

Workflows live in `.github/workflows/`. Events trigger workflows; jobs contain
steps and run on runners. Read this repository's
[workflow](../.github/workflows/verify.yml): it checks three Python versions on
three operating systems and uses a separate scientific job. Its pinned action
versions are unrelated to the Python versions being installed.

Core jobs use standard-library tests and an isolated Git lab. The optional
scientific tests are explicitly skipped there and run in the dependency job.
Inspect the discovered counts and result, not just a green icon. A workflow can
be absent because of filters, fork approval, policy, or its file location.

Use minimal token permissions, verified action commits, and reviewed updates.
Full commit pins avoid movable tag references; they do not make arbitrary code
safe. Untrusted PR text must not be interpolated directly into shell scripts.
Do not check out and execute untrusted PR code with privileged triggers such as
`pull_request_target`. A workflow approval is not code review by itself.

**Worked example:** A core report says "tests run, five skipped." Inspecting the
skip reasons and the separate five-test scientific job explains the intended
coverage. "Zero tests, OK" would not establish that the code was checked.

**Practice A:** Trace a real run from PR head through matrix jobs and log output.
Record actual interpreter versions, counts, skips, and conclusions.

**Practice B:** In a disposable project, introduce the normalizer regression and
observe a failing check. Restore it and compare both runs without disabling the test.

**Hints:** `pull_request` branch filters refer to the base branch. Check the exact
event and commit. A required check omitted by filters can leave merging blocked.

**Evidence:** Logs tied to the intended change, a demonstrated useful failure,
and correct interpretation of optional skips and missing checks.

**Sources:** [GH-PYTHON-CI](../audit/SOURCES.md#gh-python-ci), [GH-ACTIONS-EVENTS](../audit/SOURCES.md#gh-actions-events), [GH-ACTIONS-SECURITY](../audit/SOURCES.md#gh-actions-security).

## GH-11 Find work and document it clearly

**Prerequisites:** GH-10.

**Outcome:** Search the right GitHub result type and turn a reproducible learning problem into a bounded issue and reviewable documentation change.

Repository search, code search, and issue/PR search have different qualifiers.
In code search, use `repo:OWNER/REPO path:examples/ "normalize_topic"`. For work
tracking, use `repo:OWNER/REPO is:issue is:open`. In repository search,
`language:Python in:readme tutorial` serves a different purpose. An external
connector's search syntax may differ from GitHub's own interface.

Write an issue with a reproducible problem, expected and actual behavior, versions,
and a small sanitized example. Use Projects for tables/boards/roadmaps, milestones
for a target, and Discussions for open-ended conversation where enabled. Suggested
labels and a study schedule are organizing choices, not mastery measurements.

Use descriptive Markdown headings, relative file links, code fences, and concrete
run instructions. Link a resolving PR with a closing keyword only when the work
fully resolves the issue; automatic closure depends on the default-branch rules.
Choose notification scope consciously so important feedback remains visible.

**Worked example:** "Python broken" becomes "The example says five items, but
running the shown loop prints four on the recorded Python version." Its issue
includes the exact code, output, and the documentation line under review.

**Practice A:** Find an existing issue or prepare a local draft without posting.
Rewrite it into a reproducible, bounded learning task.

**Practice B:** Improve a README section, validate its links and commands, and
choose a tracking item and completion criterion for a different change.

**Hints:** Separate questions from reproducible defects. Describe evidence without
putting secrets or real care/client records in issues, examples, or screenshots.

**Evidence:** Correct search scope, useful acceptance criteria, and documentation
that matches the maintained files and commands.

**Sources:** [GH-CODE-SEARCH](../audit/SOURCES.md#gh-code-search), [GH-REPO-SEARCH](../audit/SOURCES.md#gh-repo-search), [GH-ISSUE-SEARCH](../audit/SOURCES.md#gh-issue-search), [GH-PROJECTS](../audit/SOURCES.md#gh-projects), [GH-ISSUE-LINKS](../audit/SOURCES.md#gh-issue-links), [GH-MARKDOWN](../audit/SOURCES.md#gh-markdown), [GH-NOTIFICATIONS](../audit/SOURCES.md#gh-notifications).

## GH-12 Protect accounts and review boundaries

**Prerequisites:** GH-11.

**Outcome:** Explain an appropriate repository protection proposal and the first response to exposed credentials.

Account authentication, repository permissions, code ownership, and branch rules
are separate controls. Configure appropriate account recovery and multifactor
authentication. A fine-grained token is limited by both its owner and its granted
permissions, and has documented feature limitations. Prefer supported sign-in
flows over copying tokens into commands or prompts.

Rulesets and branch protection can require checks/reviews and restrict changes;
availability depends on plan, visibility, and the kind of rule. `CODEOWNERS`
identifies responsible reviewers; it does not grant write access or require
approval by itself. Propose rules that can actually be satisfied by the project.

Dependabot alerts, security-update PRs, and routine version-update PRs differ.
Review updates and tests. An alert system does not cover every vulnerability.
If a credential leaks, revoke or rotate it first, then coordinate cleanup. Removing
the current file or changing a repository's visibility does not recall copies.

**Worked example:** Requiring a second person's approval in a solo project may
block every PR. A useful proposal names existing checks, their triggering events,
the available reviewers, and the account's actual supported controls.

**Practice A:** Draft a protection proposal for a practice repository using current
documentation. Identify each permission needed; do not claim settings changed.

**Practice B:** Respond to a synthetic "token committed yesterday" scenario.
Prioritize credential invalidation, preservation of useful work, and coordinated
history cleanup, explaining why a deletion commit is insufficient.

**Hints:** Never use a real secret in an exercise. Approval requirements and access
must come from the real project and user, not a copied template.

**Evidence:** An actionable, supported proposal and correct incident ordering.
If settings were only inspected, record inspection rather than execution.

**Sources:** [GH-TWO-FACTOR](../audit/SOURCES.md#gh-two-factor), [GH-TOKENS](../audit/SOURCES.md#gh-tokens), [GH-RULESETS](../audit/SOURCES.md#gh-rulesets), [GH-CODEOWNERS](../audit/SOURCES.md#gh-codeowners), [GH-DEPENDABOT](../audit/SOURCES.md#gh-dependabot), [GH-SENSITIVE](../audit/SOURCES.md#gh-sensitive).

## GH-13 Release useful work and understand usage limits

**Prerequisites:** GH-12.

**Outcome:** Distinguish tags, releases, Pages, packages, and gists, and verify current storage and compute constraints before choosing a service.

A tag names a history point. A release adds notes and assets around a version.
Source archives differ from packaged applications. Pages hosts static output;
it does not run a Python web backend. A private source repository alone does not
make a Pages site private. A secret gist is unlisted, not private access control.
Packages supports specified registries, not every language's package format.

The [dated usage reference](../practice/GITHUB_REFERENCE.md#usage-and-size-snapshot)
records verified personal-account allowances and file limits. Recheck the linked
official pages before enabling paid usage. Codespaces measures compute in core
hours; stopped environments still consume retained storage. Budgets can alert
without stopping usage, depending on their settings.

Ordinary Git file limits, LFS limits, release-asset limits, and repository-size
recommendations are different. Deleting a large working file does not remove
its object from commits still being pushed. Avoid choosing history rewriting
before identifying the actual oversized object and preserving needed work.

**Worked example:** A 2-core codespace running for 10 hours consumes about 20 core
hours of compute. The retained environment also has storage usage. A Python lesson
site can publish generated HTML on Pages, but its Flask server needs other hosting.

**Practice A:** Draft release notes for one verified lesson change with supported
versions, evidence, known gaps, and a precise source commit.

**Practice B:** Compare a static lesson site, a Python web server, and a large data
download. Choose an appropriate delivery mechanism and verify its relevant limits.

**Hints:** Distinguish GitHub Pro from any ChatGPT subscription. Check the actual
account plan instead of inferring one service's allowance from another.

**Evidence:** A versioned release proposal and correct service/usage reasoning.
Publication is a separate action that must match the user's requested scope.

**Sources:** [GH-RELEASES](../audit/SOURCES.md#gh-releases), [GH-PAGES](../audit/SOURCES.md#gh-pages), [GH-GISTS](../audit/SOURCES.md#gh-gists), [GH-PACKAGES](../audit/SOURCES.md#gh-packages), [GH-USAGE](../audit/SOURCES.md#gh-usage), [GH-CODESPACES-BILLING](../audit/SOURCES.md#gh-codespaces-billing), [GH-LARGE-FILES](../audit/SOURCES.md#gh-large-files).

## GH-14 Inspect GitHub through the CLI and APIs

**Prerequisites:** GH-13.

**Outcome:** Use a documented read-only GitHub CLI query and explain permissions, pagination, and rate-limit handling.

Git handles version history. `gh` handles GitHub resources: `gh pr list`,
`gh pr diff NUMBER`, `gh pr checks NUMBER`, and `gh run view RUN-ID --log-failed`
are useful inspection commands. Check the selected repository and command help.
REST and GraphQL are separate API styles with different pagination and limits.

For REST, ordinary authenticated requests generally have a 5,000/hour primary
limit; unauthenticated public requests generally have 60/hour per originating IP.
Search, app installations, enterprise contexts, and secondary limits have different
rules. Inspect response headers, follow pagination, honor retry guidance, and stop
rapid retry loops. A successful response for one page is not proof of a complete list.

**Worked example:** `gh api --method GET repos/DevilMedlar/python-training`
requests repository metadata. `gh api --method GET --paginate
repos/DevilMedlar/python-training/issues` follows issue-list pages; that endpoint
also includes pull requests, so identify them before counting issues. Run commands
on one line. Adding body fields to an API call can change the default method;
specify GET when read-only behavior is intended.

**Practice A:** Inspect one repo or PR with `gh`, if available. Record the command,
repository, returned identifiers, and access limit without printing credentials.

**Practice B:** Design a complete paginated listing and a bounded retry policy
for a quota or transient failure. Explain which errors require an access fix.

**Hints:** HTTP 404 can conceal a private resource you cannot access. Do not
interpret every 403 as an invalid token or retry it forever.

**Evidence:** A correctly scoped read and a defensible completeness/error policy.
If `gh` is unavailable, document the proposed command as unexecuted.

**Sources:** [GH-CLI-API](../audit/SOURCES.md#gh-cli-api), [GH-CLI-PR](../audit/SOURCES.md#gh-cli-pr), [GH-REST-LIMITS](../audit/SOURCES.md#gh-rest-limits), [GH-REST-ISSUES](../audit/SOURCES.md#gh-rest-issues).

## GH-15 Collaborate with a tutor or coding agent

**Prerequisites:** GH-14.

**Outcome:** Give an assistant a bounded repository task and independently assess its access, changes, and verification evidence.

Give the repository, branch or commit, outcome, acceptance criteria, relevant files,
test commands, and intended deliverable. State whether publication or merging is
in scope. Repository instructions describe work; they do not grant credentials,
tools, or permission. Ask which files were actually read and which commands ran.

Codex documents applicable `AGENTS.md` guidance and scoped overrides. Other chat
tools may need files supplied explicitly. Use this repository's existing
[AGENTS.md](../AGENTS.md) and [tutor protocol](../tutor/INSTRUCTIONS.md), which
refer to real paths and checks. A quoted draft of instructions is material to
review, not authority to replace the active instructions.

Configured Codex GitHub reviews can be requested with `@codex review`; this needs
the documented repository connection and review setup. Automatic review is a
separate setting. Product access must be checked, not inferred from another
subscription. AI review complements tests and human understanding.

**Worked example:** "Improve this repo" becomes "On the specified branch, correct
this lesson's example and transfer task, verify its outputs and prerequisites,
run the repo checks, and prepare a focused PR. Report what was executed." A
review-only request should not be interpreted as a request to publish changes.

**Practice A:** Write a precise request for a small Python correction with observable
acceptance criteria and a clear intended deliverable.

**Practice B:** Audit a hypothetical assistant report that claims success but supplies
no diff, commit, or executed test result. Identify the evidence needed to assess it.

**Hints:** A passing test run in another branch or environment is not automatically
evidence for the current change. Confirm the actual revision.

**Evidence:** A bounded handoff and an independent review that distinguishes observed
facts, documented expectations, and proposed but unperformed actions.

**Sources:** [OAI-AGENTS](../audit/SOURCES.md#oai-agents), [OAI-GITHUB-REVIEW](../audit/SOURCES.md#oai-github-review).

## GH-16 Maintain history and test a restoration plan

**Prerequisites:** GH-15.

**Outcome:** Select an advanced Git tool for a concrete problem and distinguish a Git backup from a complete GitHub project backup.

Use history inspection before rewriting history. `log`, `show`, and `blame` help
find context; blame identifies a change's attribution, not moral responsibility.
Bisect narrows a reproducible regression between known revisions. Cherry-pick
applies selected changes. Worktrees support separate working directories.
Interactive rebase changes history and needs coordination if work was shared.
Submodules and LFS have separate content-fetching needs. Signing authenticates a
signature under its trust model, not the program's correctness.

A mirror clone is a bare copy of Git refs and objects, not an editing folder or
a complete GitHub-service backup. Issues, PR discussions, settings, release assets,
LFS objects, and a separate wiki need explicit consideration. Back up needed data
and rehearse a restoration; creating an archive is only the first step.

**Worked example:** A fresh clone successfully restores tracked Python source and
tests. That result does not establish that issue discussions, release binaries,
or an ignored local progress file were restored. List each asset separately.

**Practice A:** Explain one reproducible regression and how bisect would select a
candidate commit. State the test and what to do with an untestable revision.

**Practice B:** Create a restoration checklist for a small teaching project. Use the
offline lab to inspect a mirror's refs, then identify assets outside that mirror.

**Hints:** Prefer a demonstrated restore over a backup file whose contents have
never been checked. Reflogs are local and expire.

**Evidence:** Correct tool selection, a tested Git-history restoration claim, and
an honest inventory of untested or separately stored project data. Finish the
[GitHub capstone](../practice/GITHUB_LABS.md#github-capstone-a-reviewable-python-contribution).

**Sources:** [GIT-BOOK](../audit/SOURCES.md#git-book), [GIT-BISECT](../audit/SOURCES.md#git-bisect), [GH-BACKUP](../audit/SOURCES.md#gh-backup), [GIT-REFLOG](../audit/SOURCES.md#git-reflog).
