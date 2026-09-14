# Start here with Python and GitHub

Your first task is to change a Python program and see its result, entirely in
your browser. You need your signed-in GitHub account and access to this repository.

## Your first edit and run

1. Open [python-training in github.dev](https://github.dev/DevilMedlar/python-training).
   You can also press `.` while viewing the repository on github.com.
2. In the file explorer, open `workspace/main.py`. It starts with:

```python
print("Ready to learn")
print(2 + 3)
```

```output
Ready to learn
5
```

3. Predict what changing `2 + 3` to `8 + 4` will print. Make that change.
4. Open **Source Control** in the left sidebar. Click the changed file to inspect
   its diff: the old and new lines. Stage that file with **+**, enter a message
   such as `Change my first Python calculation`, and choose **Commit & Push**.
   For this first exercise, use the current `main` branch. Branches are introduced
   when you change a function in `P1-08`; there is no GitHub course to finish first.
5. Open [Run Python lesson](https://github.com/DevilMedlar/python-training/actions/workflows/learn.yml)
   on github.com. A workspace commit starts it automatically. Open the run whose
   branch and commit match your change. Queued or running means it is still working.
6. Read **Python lesson result** on the run's summary page. You should see
   `Ready to learn` and `12`. The **Run program** step also contains the output.
7. Explain which Python expression changed and why the answer changed. Your commit
   saved the source; Actions executed that saved version on a GitHub-hosted machine.

To run again without another edit, choose **Run workflow**, select the branch
containing your work, then **Run workflow** again. That runs the branch's latest
committed code. **Re-run jobs** on an older run repeats that older commit.

Saving an editor tab alone does not commit it to GitHub. Confirm your edited file
on github.com before closing the editor; uncommitted edits remain in browser
storage. [Editor help](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor).

## What each page does

| Where | Your task |
|---|---|
| github.dev | Write Python, edit sample inputs, inspect and commit changes |
| github.com → Actions | Run Python on GitHub's machines and read output, errors, and tests |
| github.com → Code, commits, pull requests | Read lessons and review the history of your Python work |

There is no terminal or Python runtime in github.dev. This course uses GitHub
Actions for execution throughout. It does not require laptop installations,
repository downloads, GitHub Desktop, or Codespaces.

## When your code asks for input

At `P1-04`, put one answer per line in `workspace/input.txt` and commit it with
your program. Each `input()` consumes the next line. If the answers run out,
Python raises `EOFError`; add the missing answer and make a new commit. You cannot
type responses into an Actions log. See [the worked input example](practice/BROWSER_WORKFLOW.md#inputs-for-input).

## Start the tutor

Use [the launch prompt](tutor/START_PROMPT.md). A complete beginner starts at
`P1-01`; otherwise the tutor checks a small sample and starts where it is useful.
Every lesson combines a Python objective with a GitHub action on that same work.
Say `hint`, `explain`, `show solution`, `harder`, `slower`, `review`, or `save progress`.

The tutor gives a manageable task, waits for your attempt, and responds to what
you actually did. Use [tutor/progress.json](tutor/progress.json) for the same
Python-and-GitHub session history. Keep it focused on code and learning evidence;
this repository is public.

For a 2–3 hour session, use shorter periods with breaks, a fresh independent task,
and a saved next step. Pace follows your understanding and energy, not a timer.
