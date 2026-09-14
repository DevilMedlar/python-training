# GitHub command and troubleshooting reference

Use with the [lessons](../curriculum/github.md) and [labs](GITHUB_LABS.md).
Commands below assume the intended repository. Uppercase values are placeholders.
Read a mutation's target and effect before running it. Keep tokens out of remote
URLs, commands, logs, and prompts; redact any existing credential-bearing output.

## Daily workflow

Start from clean, committed or intentionally stashed work:

```sh
git status
git switch main
git pull --ff-only origin main
git switch -c docs/clarify-lesson
```

Edit the intended files, then review and publish the selected branch:

```sh
git diff
git add README.md
git diff --staged
git commit -m "Clarify lesson setup"
git push -u origin docs/clarify-lesson
```

The named README is an example; stage the files you actually intend. Inspect
untracked files separately. Open a PR with the correct base/head and run the
relevant checks. After its successful merge, update local `main`, inspect the
result, and prune stale remote-tracking references with `git fetch --prune origin`.
Local branch deletion is a separate operation and may be refused after squash.
See [GitHub flow](../audit/SOURCES.md#gh-flow) and
[Git pull](../audit/SOURCES.md#git-pull).

## Command effects

| Task | Command | Boundary |
|---|---|---|
| Inspect state | `git status` | Does not show all file contents |
| Inspect unstaged tracked edits | `git diff` | Does not display every untracked file |
| Inspect proposed commit | `git diff --staged` | Compares index with `HEAD` |
| Inspect history | `git log --oneline --decorate -10` | Selected reachable history, not every saved object |
| Inspect branch tracking | `git branch -vv` | Tracking is not permission to push |
| Fetch | `git fetch origin` | Does not integrate into the current branch |
| Integrate by fast-forward | `git pull --ff-only origin main` | Operates on the currently checked-out branch |
| Push named branch | `git push -u origin BRANCH` | Does not merge its PR |
| Unstage | `git restore --staged -- FILE` | Keeps working content; requires an appropriate source commit |
| Discard unstaged edits | `git restore -- FILE` | Replaces working content from the index |
| Inspect earlier content | `git show COMMIT:PATH` | Read-only inspection of recorded data |
| Undo ordinary committed change | `git revert COMMIT` | Adds an inverse commit; can conflict |
| Temporarily save work | `git stash push -u -m "Pause practice"` | Includes untracked, excludes ignored files |
| Reapply retained stash | `git stash apply 'stash@{0}'` | May conflict; keeps the stash entry |
| Find recent local ref movement | `git reflog` | Local and expiring |
| Name a known commit | `git branch rescue COMMIT` | Does not recover never-recorded edits |
| Explain an ignore match | `git check-ignore -v -- FILE` | Check tracked state separately |

See the version-appropriate [Git command manuals](https://git-scm.com/docs).
Use the isolated labs for recovery commands; do not use broad deletion or
history rewriting as a generic fix for an error you have not diagnosed.

## Search by result type

| Result type | Query example |
|---|---|
| Repositories | `python tutorial in:name,description,readme language:Python` |
| Repositories | `user:DevilMedlar archived:false` |
| Code | `repo:DevilMedlar/python-training path:examples/ "normalize_topic"` |
| Code | `repo:OWNER/REPO ("pytest" OR "unittest")` |
| Issues | `repo:OWNER/REPO is:issue is:open label:"good first issue"` |
| PRs | `repo:OWNER/REPO is:pr is:merged` |

Quotes, qualifiers, and regex rules depend on the search surface. Check
[code search](../audit/SOURCES.md#gh-code-search),
[repository search](../audit/SOURCES.md#gh-repo-search), and
[issue/PR search](../audit/SOURCES.md#gh-issue-search). App connector query
languages may differ. A search result is a lead to inspect, not a quality verdict.

## CLI inspection

Install/configure GitHub CLI separately if needed. `gh auth login --web` uses a
sign-in flow; `gh auth status` checks it. A credential-store fallback can be a
local config file, so use the CLI documentation and your environment's policy.

| Command | Inspect |
|---|---|
| `gh repo view --web` | The selected repository in the browser |
| `gh issue list` | Issues visible to the connection |
| `gh pr list` | PRs in the selected repository |
| `gh pr view NUMBER` | PR metadata |
| `gh pr diff NUMBER` | Proposed file changes |
| `gh pr checks NUMBER` | Check status |
| `gh run list` | Workflow runs |
| `gh run view RUN-ID --log-failed` | Failed-job logs |
| `gh api --method GET rate_limit` | API quota information |

To create a PR after deliberately committing and pushing its branch, first write
the exact description into an external temporary text file. Then use
`gh pr create --draft --base main --head BRANCH --title "Describe the change" --body-file PATH`.
This is a real publication action. `--body-file` preserves multiline text without
fragile shell quoting. See [CLI PR creation](../audit/SOURCES.md#gh-cli-pr-create).

## Usage and size snapshot

Checked 2026-09-14 against official documentation. These personal-account numbers
can change; verify current account type, plan, pooling, rates, and stopping-budget
settings before enabling paid usage. A ChatGPT subscription does not determine
a GitHub plan.

| Included usage | GitHub Free | GitHub Pro |
|---|---|---|
| Actions minutes per month | 2,000 | 3,000 |
| Actions storage | 500 MB | 1 GB |
| Codespaces core hours per month | 120 | 180 |
| Codespaces storage per month | 15 GB | 20 GB |

These are allowances, not a promise every workload is free. Standard hosted
Actions runners for public repositories have a separate free-use rule; larger
runners are billed. At two cores, 120 core hours corresponds to about 60 running
hours if nothing else consumes compute. Stopping a codespace stops compute usage,
but retained storage remains metered. See [included usage](../audit/SOURCES.md#gh-usage),
[Actions billing](../audit/SOURCES.md#gh-actions-billing), and
[Codespaces billing](../audit/SOURCES.md#gh-codespaces-billing).

| Ordinary Git upload boundary | Documented value |
|---|---|
| Browser file upload | At most 25 MiB |
| Large-file warning | Above 50 MiB |
| Blocked ordinary Git file | Above 100 MiB |
| Repository size recommendation | Ideally below 1 GB; below 5 GB strongly recommended |

The repository recommendation is not a universal fixed 5 GB cap. LFS objects,
release assets, and package registries have separate rules. History can still
contain an oversized object after its working file is deleted. See
[large files](../audit/SOURCES.md#gh-large-files). A private source repository does
not alone make a Pages site private; check [Pages access](../audit/SOURCES.md#gh-pages-access).

## Troubleshooting

These are diagnostic starting points, not definitive causes. Share the exact
sanitized command, error, branch, operating system, and Git/Python versions.

| Symptom | Inspect next |
|---|---|
| `git` not recognized | Installation, PATH, and a newly opened terminal |
| Not a Git repository | Current directory; whether this is a ZIP rather than a clone |
| Repository not found / 404 | Owner/name, visibility, account, and authorized app access |
| Authentication / 403 error | Credential method, permissions, organization policy, and rate-limit headers |
| SSH public-key failure | Selected key, agent, account authorization, and remote URL |
| Origin already exists | Existing remote before attempting to add another |
| Non-fast-forward refusal | Fetch and inspect both histories before integrating |
| Changes missing online | Commit, push result, branch view, and actual repo |
| Unexpected PR files | Base/head selection, commits, and staged content |
| Ignore rule seems ineffective | Whether the path is already tracked |
| Branch deletion refused | Ancestry and preserved content, especially after squash |
| Workflow absent | File location, event/base-branch filters, policy, and fork approval |
| Green run with no useful tests | Discovery count and the behavior actually asserted |
| Required check missing | Exact check name and skipped/absent workflow triggers |
| File too large | Objects in commits being pushed, not only present files |
| Codespace unavailable | Usage, budget, policy, and startup logs |

Do not change permissions, discard files, or rewrite shared history solely because
an error message resembles one row. See the corresponding lesson and official
source for the context-specific next step.
