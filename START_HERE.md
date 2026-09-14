# Start here

You do not need prior programming experience. You need a place to run Python,
time for a small attempt, and a way to share your code or error message.

## Get a working interpreter

Use a supported stable Python release compatible with your tools. This course's
executable core targets **Python 3.12–3.14**. Python 3.14 is the stable feature
series at the 2026-09-14 review; do not install a prerelease merely because its
number is larger. Use the [official download page](https://www.python.org/downloads/)
and check your actual version, not a screenshot in an old tutorial.

Choose one editor you already have, or Python's included IDLE when your
installation supplies it. A browser-based interpreter is enough for early
lessons; file persistence, networking, package installation, and processes may
be restricted there. Record those limits instead of treating them as Python bugs.

In a **terminal**, try the appropriate command:

| Platform | First command | If it is unavailable |
|---|---|---|
| Windows | `py --version` | Try `python --version`; check the installed interpreter |
| macOS or Linux | `python3 --version` | Check your installation instructions; do not replace system Python |

Do not type terminal commands at Python's `>>>` prompt. `exit()` leaves that
prompt. The rest of the course writes `python` for your chosen interpreter
command; substitute `py` or `python3` consistently.

Save the following as `hello.py` in a practice directory:

```python
name = "Python learner"
print(f"Hello, {name}!")
```

```output
Hello, Python learner!
```

Run `python hello.py` in the terminal **from that directory**. Expected output:
`Hello, Python learner!`. If the file is missing, check the directory and that
the editor did not save it as `hello.py.txt`. Keep the exact error message.

## Use the repository locally

Download the repository through GitHub's Code menu, or, when Git is installed:

```sh
git clone https://github.com/DevilMedlar/python-training.git
cd python-training
```

Early lessons do not require installing packages. When you reach isolated
environments, create `.venv` in the repository. Activation is optional:

| Platform | Create | Use its Python directly |
|---|---|---|
| Windows | `py -m venv .venv` | `.venv\Scripts\python.exe --version` |
| macOS/Linux | `python3 -m venv .venv` | `.venv/bin/python --version` |

Use that interpreter's `-m pip` when a lesson explicitly needs a package.
Do not change security policy just to activate an environment. See
[venv documentation](https://docs.python.org/3.14/library/venv.html).

## Start the tutor

Use [the launch prompt](tutor/START_PROMPT.md). Tell the tutor your current goal,
available time, and what can run Python. If you do not know your level, the tutor
should check a small sample and start teaching, not administer a long exam.

The tutor should give one manageable task, wait for your attempt, and respond to
what you actually did. Say `hint`, `explain`, `show solution`, `harder`, `slower`,
`review`, or `save progress` in ordinary language. These are convenience phrases,
not special product commands.

## Pick a sustainable session

For 25 minutes: retrieve an earlier idea, study one example, attempt one task,
and record the next step. For 60 minutes: add a second independent task and a
short project improvement. For a 2–3 hour block: use two or three shorter working
periods with breaks, ending with a fresh task and a handoff. These are adaptable
planning suggestions, not scientifically optimal intervals.

Progress comes from what you can explain, build, debug, and later use again.
Using documentation is normal. If the tutor supplies a solution, study it and
then try a different task before claiming independent success.
