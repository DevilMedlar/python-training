# Workspace buttons for Python

[**Open your Codespace**](https://supreme-fishstick-5g5gxqwrgjrpcp777.github.dev/)

Use the controls here as you need them during Python lessons.

| What you want | Control in this workspace |
|---|---|
| Open a file | **Explorer** → file; or **Go → Go to File** and type its name |
| Create a Python file | Explorer's **New File** button → a name ending in `.py` |
| Save an edit | **File → Save** (`Ctrl+S`, or `Cmd+S` on Mac) |
| Run the open Python file | **▶ Run Python File**; or right-click → **Run Python → Run Python File in Terminal** |
| Run without the Python extension button | **Terminal → Run Task → Run current Python file**, with the `.py` tab active |
| Open the terminal | **Terminal → New Terminal** |
| Answer a running program | Click its terminal → type your answer → **Enter** |
| Stop a running program | Click its terminal → **Ctrl+C** |
| Debug when introduced | **Run and Debug** → **Python: current file in terminal** → **Start Debugging** |
| Save progress to GitHub | **Source Control** → review file → **+** → message → **Commit** → **Push** |

Menu wording can vary slightly with the editor and installed extensions. Use
**View → Command Palette** to find commands by name. The Python extension provides
the Python Run button. Install Microsoft's recommended Python extension **in this
Codespace** if requested; the supplied task and terminal command also run Python.

## Run a program

Save the active `.py` file, then click its Run button. Read the **Terminal** panel.
If you get a Python error, read the final error line and the file/line above it,
fix that line, save, and run again. A changed file can run immediately.

Fallback in **Terminal → New Terminal**, from the repository root:

```sh
python workspace/lesson_01.py
```

For the supplied task, keep your `.py` file active; it runs whichever file is open.
The task uses `python` from the Codespace terminal. The extension's Run button uses
its selected interpreter. If they differ, choose **Python: Select Interpreter**
in the Command Palette and use the interpreter your lesson needs.

## Live input

At P1-04, open `workspace/input_example.py`, save, and run. When the question
appears, type directly into the terminal and press **Enter**. Python waits for you.
If you already see the shell prompt, the program has ended; run it again before answering.

For a menu program, answer each menu prompt the same way and use its quit option
when finished. **Ctrl+C** interrupts a program that is still running.

## Files and packages

Run commands from the repository root, shown as `python-training` in the terminal
path. The provided task and debug configuration use that folder. A relative path
such as `workspace/data/sessions.json` is interpreted from the running program's
working directory. When file paths are introduced, the tutor will show how to use
`pathlib` and create any required output directory.

At the packages lesson, use the Codespace terminal:

```sh
python -m pip install -r workspace/requirements.txt
```

Only add dependencies when needed. For tests introduced later:

```sh
python tools/run_tests.py --pattern test_study_tracker.py
```

Advanced module, packaging, research, and test commands in this course also run
in this same terminal. The tutor explains the command when it becomes useful.

## Environment exercise for P1-11

When a project needs its own packages, open **View → Command Palette** and use
**Python: Create Environment → Venv**. Select an available Python interpreter in
this Codespace. Then use **Python: Select Interpreter** to choose the new environment,
and open a new terminal so the extension can activate it. Run `python --version`
and `python -m pip --version` there to inspect the interpreter and package target.
All environment files and commands stay in the Codespace.

## Save your work to GitHub

**File → Save** writes in the Codespace. To preserve a useful version in the repository:

1. Open **Source Control** and select your changed file to review it.
2. Select **+** beside the files you want to include.
3. Enter a short message, such as `Add my greeting`, then **Commit**.
4. Use **… → Push**. If the branch is new, choose **Publish Branch**.

**Sync Changes** can pull and push together. Use **… → Pull** when you only want
to bring repository updates into the current branch. Preserve pending work and
resolve any reported conflict before continuing. Saving, running, and committing
are different actions; use each when you need it.

## Repository management

For licenses, ignore rules, settings, and collaboration pages, use the short
[repository lessons](../curriculum/github.md). They use documentation and repository
metadata as their exercises. They are available independently of your Python progress.

Sources: [Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/developing-in-a-codespace),
[Python controls](https://code.visualstudio.com/docs/python/python-tutorial),
[tasks](https://code.visualstudio.com/docs/debugtest/tasks),
[source control](https://code.visualstudio.com/docs/sourcecontrol/overview).
