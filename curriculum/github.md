# Short GitHub repository lessons

These lessons use **github.com** for repository management. Choose one when you
need it. They have no Python prerequisites and no required completion order.
For buttons used while writing Python, use [workspace controls](../practice/BROWSER_WORKFLOW.md).

## REPO-01 Repository pages and visibility

**Outcome:** Find the repository pages and identify its current visibility.

Open the repository on **github.com**. **Code** contains files and history;
**Issues** holds tasks; **Pull requests** holds proposed changes; **Settings**
contains repository configuration when your role allows it. The Public/Private
label describes who can see the repository. Your Codespace is the place to edit
and run Python; these pages manage the repository.

**Practice:** Open Code, Issues, and Pull requests. Find the repository's visibility
label. Look at the available Settings sections without changing visibility.

**Sources:** [GH-HELLO](../audit/SOURCES.md#gh-hello).

## REPO-02 README files and Markdown

**Outcome:** Format a short repository description using Markdown.

A README introduces a project. Markdown formats plain text with headings, lists,
and links. On github.com open a Markdown file, click the pencil to edit, and use
**Preview** before committing. A useful README says what the project is for and
where to start.

**Practice:** On a practice branch, create `notes/repository-practice.md` using
**Add file → Create new file**. Write a heading, a two-item list, and a link back
to the repository. Preview and commit the documentation change.

**Sources:** [GH-MARKDOWN](../audit/SOURCES.md#gh-markdown).

## REPO-03 Licenses and reuse

**Outcome:** Find a license and understand what information to check before reuse.

Open [LICENSE](../LICENSE). This repository uses the MIT license, which includes
permission terms and a requirement to preserve its copyright and permission notice
in copies or substantial portions. Read the complete text when reusing it.
Public visibility alone does not supply a license. A project's code, bundled
assets, and third-party material may have different terms.

**Practice:** Locate this repository's license and copyright notice. For another
project you want to reuse, find its license and notice files. If starting your
own new repository, GitHub's license template picker can help add the license
you have chosen. This exercise does not ask you to change this repository's license.

**Sources:** [GH-LICENSE](../audit/SOURCES.md#gh-license).

## REPO-04 Ignore rules with gitignore

**Outcome:** Use a .gitignore rule for generated or personal files.

The filename is **`.gitignore`**. Its patterns tell Git which untracked files to
leave out of normal staging. `scratch-notes/` can exclude a folder; `*.tmp` can
exclude temporary files. Open [.gitignore](../.gitignore) on github.com to inspect
real patterns. Rules affect matching paths according to their scope.

Adding an ignore rule does not remove an already tracked file or erase repository
history. Use normal file review before committing.

**Practice:** In a practice branch on github.com, edit `.gitignore` to add
`scratch-notes/`, preview the change, and commit it. Read the rule as “ignore this
folder when it is untracked.” No Python program is needed for this lesson.

**Sources:** [GH-IGNORE](../audit/SOURCES.md#gh-ignore).

## REPO-05 Branches and pull requests

**Outcome:** Propose and review a documentation change.

A branch keeps a line of changes separate while you work. A pull request compares
a proposed branch with a target branch and provides a place to review the diff.
On github.com use the branch selector to create a branch. After editing a file,
choose **Pull requests → New pull request**, check the base and compare branches,
and inspect **Files changed**.

**Practice:** Propose a small change to `notes/repository-practice.md` on a practice
branch. Open its pull request, inspect the diff, and merge only if you want the
change included in the target branch and its checks and repository rules allow it.

**Sources:** [GH-FLOW](../audit/SOURCES.md#gh-flow).

## REPO-06 Issues and planning

**Outcome:** Write a clear repository task and track its status.

An issue can track a concrete task such as improving a README or replacing a broken
link. Include what needs changing and how you will know it is finished. Labels
and Projects help organize tasks when needed. A pull request can refer to an issue;
supported closing keywords can close it when merged into the default branch.

**Practice:** Use **Issues → New issue** to describe one documentation improvement
you actually want. Complete it through a documentation change, then close it with
a brief result. A Project board is optional; one useful issue is enough.

**Sources:** [GH-PROJECTS](../audit/SOURCES.md#gh-projects), [GH-ISSUE-LINKS](../audit/SOURCES.md#gh-issue-links).

## REPO-07 Repository settings and access

**Outcome:** Locate settings and understand access roles.

Open **Settings** on github.com if your role allows it. The available controls
depend on your access, account, and repository. Repository access determines what
people can do; rulesets can add requirements to selected branches and tags.
Changing visibility or granting access changes who can see or modify your work.

**Practice:** Locate the access-management and ruleset pages. Read the roles or
rules currently shown. If a page is unavailable, note the permission needed.
Inspection completes this lesson; changing access is a separate deliberate decision.

**Sources:** [GH-ACCESS](../audit/SOURCES.md#gh-access), [GH-RULESETS](../audit/SOURCES.md#gh-rulesets).

## REPO-08 Releases and repository maintenance

**Outcome:** Understand a release and draft useful documentation notes.

A release describes a tagged version and can include attached files. GitHub's
release page offers **Draft a new release** when you have the needed access.
Choose the intended tag/commit and write what changed. A draft stays unpublished
until you publish it. Repository files, issues, release assets, and other metadata
are different items to consider when preserving a project.

**Practice:** Draft release notes for a documentation revision: a title, the changes,
and any limitations. Save a draft only if you want one; publishing a release is
optional. Identify the files and repository information you would preserve.

**Sources:** [GH-RELEASES](../audit/SOURCES.md#gh-releases), [GH-BACKUP](../audit/SOURCES.md#gh-backup).

