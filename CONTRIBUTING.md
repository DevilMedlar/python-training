# Improve the Python course

Make course changes through github.dev and review them on github.com. Read
[AGENTS.md](AGENTS.md), [tutor instructions](tutor/INSTRUCTIONS.md), and the
[verification record](audit/VERIFICATION.md) before changing teaching behavior.

1. Create a branch from current `main` using the branch selector on github.com
   or github.dev. Give it a name describing one change.
2. Edit the relevant Python code, tests, lesson, and catalog fields together.
   Explain the behavior being fixed. Preserve stable lesson IDs and existing work.
3. Inspect the diff in Source Control, stage the intended files, and Commit & Push.
4. Open a pull request on github.com. Describe why the change is needed, what now
   happens, and what observed checks support it.
5. Inspect **Verify Python tutor** on that PR. Fix failed checks through github.dev.
   A merge should use the tested head commit and respect repository controls.

Keep GitHub instruction inside the corresponding Python lesson. Every Python
lesson has a concrete GitHub task on its own code. `GH-` IDs identify browser
reference cards, not a separately selected syllabus. The learner's tools are
github.com and github.dev; all Python execution, builds, and checks use hosted
Actions. Do not add a laptop setup, local clone, CLI curriculum, or Codespaces
requirement.

Catalog changes must regenerate `curriculum/INDEX.md`. For browser maintenance,
use **Actions → Render lesson index** and copy the complete generated Markdown
from its log into the index in github.dev, then commit. This workflow does not
write to the repository. The normal verifier rejects a stale index.

Runnable Markdown Python examples need an adjacent expected `output` block.
Use `python-template` for incomplete or input-dependent snippets, and explain how
the learner will run them. Test changed behavior and relevant failures. Preserve
historical audit results as history; append new observations without claiming an
unrun environment passed. Sources belong in `audit/sources.json` and `audit/SOURCES.md`.
