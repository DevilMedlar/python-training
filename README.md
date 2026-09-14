# Python Training

A practical Python course and an explicit operating guide for a ChatGPT tutor.
Start from your demonstrated skills, learn through small programs, and progress
toward reliable applications, research, and useful original contributions.

The curriculum adapts seven supplied AI-generated drafts. Their claims are treated
as provisional source material. The [claim audit](audit/CLAIM_AUDIT.md) explains
corrections and qualifications; the [verification report](audit/VERIFICATION.md)
states exactly what was checked and what remains outside those checks.

## Start learning

1. Open [START_HERE.md](START_HERE.md).
2. Give your tutor the [launch prompt](tutor/START_PROMPT.md), with access to the
   repository files. A URL alone does not guarantee the tutor can read them.
3. Begin the short [placement process](tutor/PLACEMENT.md), or request lesson
   `P1-01` if you are new to programming.
4. Keep your [progress record](tutor/PROGRESS.md) between conversations.

## The learning route

| Phase | Focus | Evidence for progressing |
|---|---|---|
| [1 — Novice](curriculum/phase-1.md) | Values, control flow, collections, functions, files, debugging | Build and explain a small program; handle boundary cases |
| [2 — Practitioner](curriculum/phase-2.md) | Interfaces, testing, data, APIs, SQL, packaging, Git | Deliver a useful application with repeatable checks |
| [3 — Expert](curriculum/phase-3.md) | Protocols, architecture, concurrency, performance, reliability | Defend design choices and demonstrate failure handling |
| [4 — Researcher](curriculum/phase-4.md) | Questions, literature, experimental design, numerical validity | Produce a reproducible, appropriately limited investigation |
| [5 — Creator](curriculum/phase-5.md) | Original contribution, evaluation, delivery, maintenance | Create something useful that others can inspect and extend |

These are informal, overlapping routes, not academic credentials or a universal
psychological sequence. Research and creator work are optional directions; you
can build useful software and contribute to projects much earlier.

## What is included

- [Lesson index](curriculum/INDEX.md) and a machine-readable prerequisite catalog.
- A [tutor protocol](tutor/INSTRUCTIONS.md), [teaching playbook](tutor/TEACHING.md),
  placement tasks, hint rules, assessment criteria, and progress handoff.
- Two practice tasks per lesson, [five capstones](practice/CAPSTONES.md),
  [50 additional beginner drills](practice/BEGINNER_DRILLS.md), a
  [working glossary](curriculum/GLOSSARY.md),
  [assessment guidance](practice/ASSESSMENT.md), and a
  [misconception guide](practice/MISCONCEPTIONS.md).
- Runnable [reference programs](examples/README.md), meaningful tests, and
  automated checks for the curriculum, internal links, and Python examples.
- [Primary sources](audit/SOURCES.md), attachment provenance, and a record of
  review limitations. [Input coverage](audit/INPUTS.md) maps all seven attachments.
  No guarantee of perfect correctness is made.

## Run the checks

Use Python 3.12, 3.13, or 3.14. The core examples and checks need only the standard
library. Run these commands from the repository root:

```sh
python tools/check_repo.py
python -m unittest discover -s tests -v
python -m examples.studylog examples/data/sessions.csv
```

On Windows, use `py` in place of `python` if that is your working interpreter
command. On macOS/Linux it may be `python3`; [setup](START_HERE.md) explains this.
Optional scientific and packaging tools are introduced when a lesson needs them.

To improve the course, follow [CONTRIBUTING.md](CONTRIBUTING.md). The existing
[MIT license](LICENSE) applies to repository content; external references retain
their own terms.
