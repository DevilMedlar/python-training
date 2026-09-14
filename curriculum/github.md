# GitHub reference for Python lessons

Use these cards when the current Python lesson links to them. They explain the
GitHub action you are performing on that same Python code. There is no separate
GH lesson sequence, track choice, or GitHub capstone. Follow the [Python index](INDEX.md).

The learner works through github.com and github.dev. Python execution and any
advanced commands run in hosted workflows. See the [browser workflow](../practice/BROWSER_WORKFLOW.md).

## GH-01 Read your Python repository

**Used within Python:** First introduced with P1-01; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Locate the current Python lesson, practice file, branch, history, and run on GitHub.

The Code page holds committed files. The branch selector determines which version
you see. Open README, the current phase guide, and workspace/main.py. Commit history
records changes; Actions records executions. A permanent file link identifies a
specific commit, while a branch link follows later changes.

A fork is a repository under another owner and is useful when you cannot write to
an upstream project. This learning repository is already your destination; you do
not need to download or clone it. Read a project's license before reusing its code.

**Worked example:** Find workspace/main.py in the Code page, then open its latest commit and the matching Actions run.

**Practice A:** Open the current Python lesson and its practice file in github.dev.

**Practice B:** Explain which page contains source text and which contains the observed program output.

**Hints:** Check the repository name and branch before interpreting a result.

**Evidence:** A source link, a run link, and an explanation of their different roles.

**Sources:** [GH-DEV](../audit/SOURCES.md#gh-dev), [GH-PERMALINK](../audit/SOURCES.md#gh-permalink), [GH-LICENSE](../audit/SOURCES.md#gh-license).

## GH-02 Complete a browser pull request

**Used within Python:** First introduced with P1-08; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Use a branch and pull request to review a change to your current Python function.

A branch lets you change the function while keeping main available as a baseline.
Use the branch selector in github.dev to create a named branch from main. Edit the
function, inspect the diff, and Commit & Push. On github.com, open Pull requests →
New pull request, select main as base and your branch as compare, and inspect the
Python diff before creating the PR. The PR proposes incorporating that change.

Read the Actions checks and the PR's Files changed view. Explain the function's
contract and results before merging. Creating a PR does not merge it. These controls
are introduced with P1-08's function change, after ordinary edit/commit/run practice.

**Worked example:** A branch changes a repeated calculation into a function; its PR shows that refactor and its run.

**Practice A:** Complete the branch and PR steps for the function you are writing in P1-08.

**Practice B:** Make a fresh function improvement on another branch and explain base versus head.

**Hints:** The base receives changes; the head contains the proposed work.

**Evidence:** A reviewed Python diff, observed run, and explanation of the PR state.

**Sources:** [GH-HELLO](../audit/SOURCES.md#gh-hello), [GH-FLOW](../audit/SOURCES.md#gh-flow), [GH-DEV](../audit/SOURCES.md#gh-dev).

## GH-03 Use github.dev and hosted Python execution

**Used within Python:** First introduced with P1-01; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Distinguish browser editing, GitHub sign-in, repository access, and hosted execution.

Open github.dev while signed in to the GitHub account that can edit this repository.
Use Source Control to commit. The editor has no terminal or compute runtime;
GitHub Actions supplies Python on a hosted runner. A saved editor buffer is not
yet a GitHub commit, and a successful commit is not yet a successful Python run.

In the modules lesson, inspect the workflow's Python setup and the hosted virtual
environment exercise. Interpreter and dependency ownership remain Python concepts,
but their installation and execution happen on GitHub's machines. Do not create
a Codespace or install local tools for this course.

**Worked example:** main.py is edited in github.dev; its committed code runs in the Run program step on github.com.

**Practice A:** Identify the current branch, edit a Python expression, and confirm it appears on github.com after committing.

**Practice B:** At P1-11, inspect the hosted interpreter and pip version and explain their environment boundary.

**Hints:** An access failure, a commit failure, and a Python exception need different repairs.

**Evidence:** The relevant committed file and runner observation, with unknown settings left unclaimed.

**Sources:** [GH-DEV](../audit/SOURCES.md#gh-dev), [GH-AUTH](../audit/SOURCES.md#gh-auth), [GH-PYTHON-CI](../audit/SOURCES.md#gh-python-ci).

## GH-04 Review and commit Python snapshots

**Used within Python:** First introduced with P1-02; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Explain which Python edits are included in a commit by inspecting the browser diff.

Open Source Control in github.dev. Select a changed file to compare its old and
new contents. Stage intended files with +, write a message about the behavior,
and use Commit & Push. Confirm the committed source on github.com.

Staging selects a snapshot; a later edit can leave a file with both staged and
unstaged changes. Inspect both views before committing, or deliberately stage the
latest intended content again. A commit can contain the Python implementation,
its sample input, and its test when they belong to one change.

**Worked example:** Changing 2 + 3 to 8 + 4 changes one expression; the diff explains the result in the next Actions run.

**Practice A:** Inspect and commit the arithmetic or string change from the current Python lesson.

**Practice B:** After staging a change, edit it again and predict which version is staged; inspect before committing.

**Hints:** Read the diff rather than assuming every visible editor change is included.

**Evidence:** A correct prediction about the committed Python and a link to that snapshot.

**Sources:** [GH-DEV](../audit/SOURCES.md#gh-dev), [GIT-BOOK](../audit/SOURCES.md#git-book).

## GH-05 Keep browser branches current

**Used within Python:** First introduced with P2-11; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Identify the branch versions used by a Python change and prepare a current browser branch.

Start new work from current main. Existing feature branches can fall behind main
when another PR is merged. Inspect the PR comparison and, if GitHub offers Update
branch, read its effect and check the resulting tests. The main branch does not
change merely because you view or edit a feature branch.

When you cannot update a complex branch through the available browser controls,
preserve it, make a new branch from current main, and reapply the small intended
Python edit in github.dev. Review the complete replacement diff and link the older
PR. Close the superseded PR after confirming the replacement; do not erase history.

**Worked example:** An old package branch lacks a newer parser fix. A fresh branch from main includes that fix before the package change is reapplied.

**Practice A:** Before the P2-11 package change, inspect main and the branch used for its hosted build.

**Practice B:** Explain how a run on the wrong branch could test the wrong package version.

**Hints:** Match the branch, commit, PR comparison, and run before diagnosing the Python code.

**Evidence:** A current branch and an observed hosted run for its exact Python change.

**Sources:** [GH-FLOW](../audit/SOURCES.md#gh-flow), [GH-DEV](../audit/SOURCES.md#gh-dev), [GH-MERGES](../audit/SOURCES.md#gh-merges).

## GH-06 Review contributions and choose a merge method

**Used within Python:** First introduced with P1-09; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Review the Python contract, diff, and observed checks before incorporating a contribution.

A useful PR describes the problem, changed behavior, and relevant test evidence.
Review Files changed and each required check. A green badge only describes checks
that actually ran; inspect failures, skips, and the code version they tested.

Merge commit, squash, and rebase can produce different histories even when their
final files match. Use the repository's available method and inspect the result.
After merging, main must contain the intended Python behavior. For an upstream
project without write access, use a browser fork and target the upstream base;
follow that project's contribution guidance.

**Worked example:** The tracker PR includes a longest-session function, its empty case, and a run showing both.

**Practice A:** Review the current Python PR against its stated contract and tests.

**Practice B:** Find an omission or explain why a different correct implementation still meets the contract.

**Hints:** Review behavior and evidence rather than requiring source text identical to the tutor answer.

**Evidence:** An explained Python review and accurate observed PR/merge state.

**Sources:** [GH-FLOW](../audit/SOURCES.md#gh-flow), [GH-FORK](../audit/SOURCES.md#gh-fork), [GH-MERGES](../audit/SOURCES.md#gh-merges).

## GH-07 Resolve a conflict and verify the combined result

**Used within Python:** First introduced with P2-11; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Resolve a simple competing-line Python conflict through GitHub and test the intended result.

Use a disposable pair of practice branches. Make competing edits to the same
Python line. After one change reaches main, open the other PR. When GitHub offers
Resolve conflicts, decide the intended Python behavior, edit the conflicting text,
remove markers, mark it resolved, and commit the merge. GitHub merges the entire
base branch into the head branch during this resolution, so inspect all changes.

The web conflict editor supports simple competing-line conflicts. If it is unavailable
for your case, preserve the old branch and use a fresh branch from main to reapply
the intended small change in github.dev. This is a replacement contribution, not
a claim that GitHub resolved the original conflict. Run tests before merging.

**Worked example:** Two branches change the report title. Choose the specified final title and verify the Python output after resolution.

**Practice A:** Use the conflict task card with a disposable Python display line during P2-11.

**Practice B:** Explain why syntactically resolved text could still calculate the wrong result.

**Hints:** Write the expected final behavior before choosing either side.

**Evidence:** The combined diff, correct output, and an honest description of the resolution method.

**Sources:** [GH-WEB-CONFLICTS](../audit/SOURCES.md#gh-web-conflicts), [GH-FLOW](../audit/SOURCES.md#gh-flow).

## GH-08 Recover a Python change in the browser

**Used within Python:** First introduced with P1-10; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Restore intended Python behavior with a reviewable new change and preserve useful history.

For a recent mistake, inspect the previous version of the file on github.com.
Copy the needed small correction into a new browser edit, commit it, and rerun
the failing Python case. This adds a fix without rewriting published history.

For an eligible merged PR, GitHub's Revert action creates a new PR with the inverse
change. Inspect its scope and tests before merging it. If reverting conflicts or
the control is unavailable, use a targeted fix PR from current main. A file ignore
rule does not remove already committed data. Exposed credentials require revocation
or rotation; changing a file alone does not remove the exposure.

**Worked example:** A string transformation regression is repaired in a new commit; the previous failure remains inspectable.

**Practice A:** Restore the intended Python behavior and rerun the regression case from P1-10.

**Practice B:** Explain what a new fix commit preserves and what a PR revert would change.

**Hints:** Inspect the old function and current requirements before restoring text blindly.

**Evidence:** A failing case, a focused recovery diff, and the succeeding run.

**Sources:** [GH-WEB-REVERT](../audit/SOURCES.md#gh-web-revert), [GH-IGNORE](../audit/SOURCES.md#gh-ignore), [GH-SENSITIVE](../audit/SOURCES.md#gh-sensitive).

## GH-09 Review a small Python change with real tests

**Used within Python:** First introduced with P1-10; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Connect a Python behavior contract to a regression test that actually executes.

Keep tests under workspace/test_*.py when testing learner code. The lesson
workflow runs these files after the program and rejects empty discovery when test
files exist. Standard course tests under tests/ check maintained reference code.
Read the count and assertions instead of treating an unrelated green check as proof.

For string normalization, define exactly what to trim, lowercase, preserve, and
reject. The reference examples/topic_names.py and tests/test_topic_names.py provide
one contract to inspect after your attempt. It is not a general security sanitizer.

**Worked example:** A test expects learn-python; removing lowercasing makes the relevant test fail, and repairing it passes.

**Practice A:** Write a regression test for the current Python bug and observe failure before the repair.

**Practice B:** Add an unfamiliar boundary case and explain which requirement it covers.

**Hints:** Make sure the test imports the function you changed and runs on the same commit.

**Evidence:** Actual failure and success logs, discovery count, and a requirement-based explanation.

**Sources:** [PY-TEXT](../audit/SOURCES.md#py-text), [PY-UNITTEST](../audit/SOURCES.md#py-unittest), [GH-PYTHON-CI](../audit/SOURCES.md#gh-python-ci).

## GH-10 Understand and inspect GitHub Actions

**Used within Python:** First introduced with P1-01; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Read the output and status of a hosted run for the current Python commit.

At P1-01, use Actions only to run and read output. Choose Run Python lesson and
open your commit. The result summary distinguishes stdout, stderr, and exit status.
Inputs come from the committed input.txt file. Re-run jobs uses the old run's
commit; Run workflow uses the chosen branch's latest committed version.

At later lessons, inspect YAML triggers, steps, Python setup, dependencies, tests,
permissions, and timeout. The course verifier checks Python 3.12–3.14 on multiple
hosted systems; its optional scientific job has its own dependencies. Queued,
skipped, failed, and successful jobs are different outcomes. Inspect actual results.

**Worked example:** The first Python file prints two lines; a missing quote produces a failed Run program step with SyntaxError.

**Practice A:** Inspect the matching output or error for your current Python edit.

**Practice B:** When learning tests, explain which tests ran and why a skipped job provides no passing evidence.

**Hints:** Read workflow name, branch, commit, step, and output in that order.

**Evidence:** An observed run and an explanation appropriate to the current Python objective.

**Sources:** [GH-PYTHON-CI](../audit/SOURCES.md#gh-python-ci), [GH-ACTIONS-MANUAL](../audit/SOURCES.md#gh-actions-manual), [GH-ACTIONS-EVENTS](../audit/SOURCES.md#gh-actions-events), [GH-ACTIONS-SECURITY](../audit/SOURCES.md#gh-actions-security).

## GH-11 Find work and document it clearly

**Used within Python:** First introduced with P1-12; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Use GitHub search and Markdown to make a Python task or result understandable.

Search the relevant result type: code for an implementation, issues for a
reported behavior, repositories for a project. Use relative Markdown links inside
the course and permanent code links when a report depends on an exact version.

A small Python bug report states the input, expected result, actual result, and
the failing run. A project README describes its contract and browser run steps.
For research, commit the protocol before the final analysis and connect conclusions
to code and results. Draft content in the repository; posting to another project's
discussion is a separate collaboration action.

**Worked example:** A CSV parser note links a quoted-field fixture, its failing test, and the repaired implementation.

**Practice A:** Document one assumption or failure from the current Python lesson beside its code.

**Practice B:** Use GitHub search to locate the relevant implementation or existing report and explain the match.

**Hints:** A useful report lets somebody reproduce the behavior from the stated input.

**Evidence:** A bounded, source-linked Python task or result note.

**Sources:** [GH-CODE-SEARCH](../audit/SOURCES.md#gh-code-search), [GH-ISSUE-SEARCH](../audit/SOURCES.md#gh-issue-search), [GH-MARKDOWN](../audit/SOURCES.md#gh-markdown), [GH-PERMALINK](../audit/SOURCES.md#gh-permalink).

## GH-12 Protect accounts and review boundaries

**Used within Python:** First introduced with P3-09; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Relate repository access and workflow permissions to the Python code being executed.

Inspect the actual repository settings and workflow permissions before describing
them. Account authentication, collaborator roles, branch controls, code ownership,
and Actions permissions govern different things. Do not infer configured controls
from a template or a public repository badge.

The lesson workflow needs read access to source and has no repository write step.
Use synthetic data and no credentials in public practice files or logs. For a
future Python integration, explain the minimal access needed before adding it.
Do not treat an agent-authored PR as automatically trusted.

**Worked example:** An architecture review distinguishes the parser validation boundary from the workflow token permission.

**Practice A:** Inspect permissions alongside the P3-09 Python trust-boundary review.

**Practice B:** Explain the effect and limits of one proposed protection without claiming it is already enabled.

**Hints:** Name the resource and operation each permission governs.

**Evidence:** A documented boundary and accurate observation of the relevant configuration.

**Sources:** [GH-TWO-FACTOR](../audit/SOURCES.md#gh-two-factor), [GH-TOKENS](../audit/SOURCES.md#gh-tokens), [GH-RULESETS](../audit/SOURCES.md#gh-rulesets), [GH-CODEOWNERS](../audit/SOURCES.md#gh-codeowners), [GH-SENSITIVE](../audit/SOURCES.md#gh-sensitive).

## GH-13 Release useful work and understand usage limits

**Used within Python:** First introduced with P2-12; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Tie a release candidate to tested Python behavior and a bounded hosted workflow.

A tag identifies a code version. A GitHub release adds release information and
optional assets. Prepare a draft on github.com with usage, compatibility, changes,
checks, and limits. Publishing a release is a later explicit action; creating a
draft or a passing workflow does not publish one.

Package installation and builds happen in hosted workflow steps. Keep experiments
finite and inspect current Actions usage rules if the workload changes. Ordinary
hosted runners, larger runners, and different repository plans can have different
conditions. Do not promise unlimited compute or configure paid resources as a
hidden lesson prerequisite.

**Worked example:** The report application draft points to the reviewed commit and hosted command-interface checks.

**Practice A:** Prepare release notes for the current Python deliverable with its actual evidence.

**Practice B:** Identify the code version and one compatibility or workload limit a user needs to know.

**Hints:** A draft, a tag, a package build, and a public release are distinct states.

**Evidence:** An inspectable release candidate and correctly described publication state.

**Sources:** [GH-RELEASES](../audit/SOURCES.md#gh-releases), [GH-PACKAGES](../audit/SOURCES.md#gh-packages), [GH-USAGE](../audit/SOURCES.md#gh-usage), [GH-ACTIONS-BILLING](../audit/SOURCES.md#gh-actions-billing).

## GH-14 Read GitHub APIs from Python

**Used within Python:** First introduced with P2-09; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Apply Python HTTP and JSON skills to a bounded read-only GitHub API example.

In P2-09, start with a small recorded response and a fake transport so failure
tests are deterministic. Then, if the exercise needs a live observation, run a
bounded GET request in GitHub Actions. Parse JSON, validate the expected fields,
and handle HTTP errors and timeouts.

Repository issue endpoints can include pull requests; identify the documented
pull_request marker when the task wants only issues. Pagination means one response
may not contain all results. Rate limits differ by authentication and endpoint.
No GitHub CLI installation is required, and practice code should not make write
requests or embed credentials to demonstrate an HTTP lesson.

**Worked example:** The Python adapter reads the full_name field of this repository from a recorded metadata response, then compares a documented live read if needed.

**Practice A:** Test valid, malformed, timed-out, and failed responses through the adapter you are building.

**Practice B:** Explain pagination and the difference between an issue-only count and an issues-endpoint count.

**Hints:** Separate request transport, JSON decoding, validation, and the calculation.

**Evidence:** Deterministic Python tests and separately labeled live observations.

**Sources:** [PY-URLLIB](../audit/SOURCES.md#py-urllib), [GH-REST-ISSUES](../audit/SOURCES.md#gh-rest-issues), [GH-REST-LIMITS](../audit/SOURCES.md#gh-rest-limits).

## GH-15 Collaborate with a tutor or coding agent

**Used within Python:** First introduced with P3-09; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Give an assistant a bounded Python task and inspect its actual repository work.

State the Python behavior, files in scope, browser-only learning environment,
and evidence needed. An assistant must report actual file access, changed code,
and observed runs. A repository URL or instruction file does not grant access.

Ask the tutor to explain a code change and give you a fresh task to perform.
Review generated code against the contract; record solution assistance honestly.
Use the one progress record. Do not route to a separate GitHub tutor or accept a
claim of learning based only on code the assistant wrote.

**Worked example:** Ask for an explanation of a failing parser case and a small repair, then independently handle a different case.

**Practice A:** Scope assistance for the current Python problem and inspect the returned diff and tests.

**Practice B:** Explain the revised code and complete a fresh task without copying the solution.

**Hints:** Tool access, code correctness, and learner understanding are different evidence questions.

**Evidence:** A bounded request, inspected result, and honestly attributed learner work.

**Sources:** [OAI-AGENTS](../audit/SOURCES.md#oai-agents), [OAI-GITHUB-REVIEW](../audit/SOURCES.md#oai-github-review).

## GH-16 Maintain history and test a restoration plan

**Used within Python:** First introduced with P4-04; return here only for the action linked by your current lesson.

**Prerequisites:** none. Consult the current Python lesson for its Python prerequisites.

**Outcome:** Use GitHub history and hosted reproduction to preserve an inspectable Python result.

Record the code commit, inputs, configuration, dependencies, and observed run.
Git history preserves tracked files; it does not automatically preserve all Actions
outputs, issue discussions, settings, or external data. Retention and permissions
must be part of a research or maintenance plan.

Practice a small restoration by opening an earlier committed Python file and
reapplying the intended content on a new browser branch, then running its checks.
The verifier also runs an isolated Git-history demonstration on GitHub's runner.
Inspecting that demonstration teaches boundaries; it does not prove a complete
project backup or replace your own Python reproduction evidence.

**Worked example:** A protocol and script can be retrieved at a known commit, but a temporary uncommitted result requires a separate preservation method.

**Practice A:** Reproduce a small result from the recorded Python commit and committed inputs in Actions.

**Practice B:** List the project assets that this reproduction did not restore or verify.

**Hints:** Specify what must survive and test its retrieval instead of assuming history stores everything.

**Evidence:** A demonstrated hosted reproduction and an explicit inventory of remaining gaps.

**Sources:** [GH-PERMALINK](../audit/SOURCES.md#gh-permalink), [GH-BACKUP](../audit/SOURCES.md#gh-backup), [GH-ACTIONS-MANUAL](../audit/SOURCES.md#gh-actions-manual).
