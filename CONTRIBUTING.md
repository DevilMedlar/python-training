# Contributing

Keep the course accurate, usable, and easy for a tutor to navigate. Read
[AGENTS.md](AGENTS.md), [tutor instructions](tutor/INSTRUCTIONS.md), and
[verification scope](audit/VERIFICATION.md) before changing teaching behavior.

For a lesson change, identify the learner problem, prerequisites, objective,
worked example, two practice tasks, hints, evidence, and sources. Preserve stable
lesson IDs. Update `curriculum/catalog.json` and the phase or companion guide together, then
regenerate the index with `python tools/render_index.py`.

For technical changes, state the contract and the relevant failure case. Add
tests that can detect a plausible defect, not tests that merely repeat the code.
Consult primary documentation for the supported version. Record consequential
source corrections in the audit, including whether a behavior was documented,
executed, or remains an untested extension.

Run `python tools/check_repo.py` and `python tools/run_tests.py`; zero discovered
tests must fail. For Git changes, run `python -m examples.git_workflow_lab` with
Git 2.28 or later. Run the optional scientific suite
when changing that lab. Do not label an unrun environment supported by evidence
merely because a CI matrix contains it. Do not promise that a prompt is flawless
or that the course confers a degree.

Keep real progress records, private data, virtual environments, and generated
experiments out of commits. Use synthetic fixtures. Check the diff and preserve
the existing license. A useful review description explains the problem, change,
resulting behavior, validation, and material limits.
