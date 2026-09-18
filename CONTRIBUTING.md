# Improve this course

Edit and test in [the Codespace](https://supreme-fishstick-5g5gxqwrgjrpcp777.github.dev/).
Read [AGENTS.md](AGENTS.md) and [tutor instructions](tutor/INSTRUCTIONS.md) before
changing teaching behavior. Preserve the learner's work and stable lesson IDs.

Python lessons teach a concrete Python skill through example, edit, run, and repair.
Each has a short workspace control. Repository management has separate brief,
non-Python lessons in [curriculum/github.md](curriculum/github.md).

For a maintenance change:

1. Create a branch using the branch selector. Edit the relevant code and documents.
2. When catalog metadata changes, run `python tools/render_index.py` in the Codespace terminal.
3. Run `python tools/check_repo.py` and `python tools/run_tests.py` in that terminal.
4. Review and stage the intended files in Source Control, commit, and push.
5. Open a pull request. Describe the problem, resulting behavior, and observed checks.
   Inspect **Verify Python tutor** and merge the tested head while respecting repository controls.

These are course-maintenance checks. A beginner starts by running one Python file.
Runnable Markdown examples need an adjacent `output` block. Use `python-template`
for incomplete or interactive snippets, with direct running instructions. Keep
historical audit results clearly historical and append new observations honestly.
Sources belong in `audit/sources.json` and `audit/SOURCES.md`.
