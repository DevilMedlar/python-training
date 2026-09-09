# Record 0001: foundations and first Git checkpoint

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Lesson review and progress checkpoint |
| Evidence | Current course conversation, learner's pasted code/terminal output, and GitHub verification |
| Verified learner commit | [92962ab](https://github.com/DevilMedlar/python-training/commit/92962abf52d036dce6c5421c33703cffd313ac98) — Add first Python script |
| Verified submitted file | [hello.py at the learner commit](https://github.com/DevilMedlar/python-training/blob/92962abf52d036dce6c5421c33703cffd313ac98/hello.py) |
| Runtime and workspace | Python 3.14.2; /workspaces/python-training; branch main |

**Coverage and evidence.**

The learner opened a GitHub Codespace, ran python3 --version, used pwd and git status, created and saved hello.py, and executed python3 hello.py. The two-line script printed the chosen text and the result of 7 + 7, which was 14.

The learner corrected the environment distinction using observed shortcut destinations: period opened vscode.dev/github/DevilMedlar/python-training, and comma opened the named expert-couscous Codespace. The browser editor and Codespace use similar VS Code interfaces; the Codespace provides the cloud runtime and terminal used in this course.

The submitted Git sequence showed hello.py as untracked, staged it with git add hello.py, displayed the additions with git diff --cached, committed with a descriptive message, pushed main to origin, and finished with a clean working tree and an up-to-date origin/main message. GitHub verification confirmed the same learner commit and exactly two lines in hello.py.

| Skill | Assessment at this checkpoint |
| --- | --- |
| Open the appropriate development environment | Demonstrated after clarification |
| Run the available interpreter and a saved script | Demonstrated with supplied commands |
| Print a string and an arithmetic result | Correct in the first submitted exercise |
| Basic spacing and capitalization | Correct in both submitted lines; no style fix required |
| Follow stage, review, commit, push workflow | Successfully completed once with guidance |
| Explain Git's different states independently | Not yet assessed |
| Predict expression results and distinguish names from strings | Basic arithmetic output demonstrated; variable behavior not yet assessed |
| Broader Python knowledge | Not assessed by this two-line exercise |

**Strengths observed.**

- Produces code matching the taught requirements and provides the actual runtime output.
- Applies the spacing demonstrated in the lesson.
- Reports real interface behavior and challenges an imprecise explanation.
- Successfully completes the first guided Git checkpoint.

**Difficulties and uncertainties to revisit.**

- The lightweight web editor versus Codespace distinction needed clarification; the learner subsequently demonstrated the correct environment.
- The pasted diff contains many repeated screen views, (END), and tilde filler lines. Revisit pager navigation and how to copy useful output. This is not evidence of duplicated source code or a failed commit.
- No Python bug or style violation was found in the submitted program.
- Further practice is needed before claiming independent Git fluency or mastery of language concepts not yet exercised.

**Tooling follow-up prepared for the next response.**

A pager is a viewer for command output. In the usual less viewer, q exits to the shell. The repeated display in the pasted transcript does not change the two-line program.

To display a staged diff directly in terminal output for future checkpoints:

```bash
git --no-pager diff --cached
```

--no-pager is a Git option placed before the subcommand. --cached selects changes staged for the next commit. After the completed commit, an empty staged diff is expected unless new changes have been staged. See [Git options](https://git-scm.com/docs/git) and [git diff](https://git-scm.com/docs/git-diff).

The tutor is adding lesson records on GitHub. To bring those commits into the existing Codespace, the next response will teach:

```bash
git pull --ff-only
```

This fetches remote updates and updates the current branch only when it can fast-forward; it stops if local and remote history have diverged. A fast-forward moves the branch to an existing newer commit without making a merge commit. See [git pull](https://git-scm.com/docs/git-pull).

**Resume state.**

| Item | Status |
| --- | --- |
| First output exercise | Complete; reviewed with no changes required |
| First Git checkpoint | Complete; learner commit verified on GitHub |
| Download of tutor lesson records into Codespace | Awaiting learner's pull |
| Variables and assignment | Next lesson; see record 0002 |
| Learner's variables.py | Not yet submitted or assessed |

Other references used in this course so far: [Python print](https://docs.python.org/3.14/library/functions.html#print), [PEP 8](https://peps.python.org/pep-0008/), [environment comparison](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor), [opening an existing Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/opening-an-existing-codespace).
