# Python training: append-only course record

Created: 2026-09-09. Repository: DevilMedlar/python-training.

This is the durable course record for tutoring, review, and resuming work. The learner has authorized the tutor to maintain Markdown records under lessons/. The learner writes the exercise programs and practices terminal and Git commands.

**How to maintain this record.**

- Preserve existing records and their text. Add a new numbered Markdown file for each subsequent lesson, review, correction, or checkpoint. Do not rewrite or delete earlier entries.
- Continue numbering after the highest existing numbered record. This README describes the initial system; later records may add refinements without editing it.
- Record corrections in a new entry that identifies the earlier entry and explicitly explains what is superseded. Historical observations remain historical observations.
- Before tutoring, inspect the latest records and any linked unresolved work. Before a repository write, check current files and branch state so concurrent learner work is preserved.
- Every new record should identify its evidence, topics taught, assignment, submission/review status, demonstrated strengths, difficulties or uncertainties, next action, and sources used.
- Separate introduced material, successful guided practice, independent demonstrations, and performance across repeated practice. One successful small exercise does not establish broad mastery.
- Record actual mistakes and remaining uncertainties separately. Do not invent weaknesses or assume an untested skill is a weakness.
- When documentation is committed directly on GitHub, tell the learner how to bring it into the Codespace. A GitHub update does not automatically update an existing Codespace checkout.

**Teaching agreement.**

The goal is deep practical Python fluency and strong command-line, Git, and GitHub skills. Remain in GitHub Codespaces until the learner asks to begin working directly on the PC. Introduce repository settings when they become relevant.

Explain each new concept and command before assigning work. Use small worked examples, then let the learner implement the exercise. Review correctness, names, spacing, control flow, and readability even when output is correct. Distinguish language requirements, style guidance, and optional conventions.

Use consistent practice with variation and later revisits. Move through basic print usage promptly once demonstrated. Increase independence and review depth over time. Commit at meaningful checkpoints, not automatically after every small exercise.

Verify technical guidance against official documentation and the actual Python version. Do not imply that repository access reveals unsaved or unpushed Codespace files or live terminal state. The current confirmed interpreter is Python 3.14.2.

# Records

**Foundation**
| Record | Purpose |
| --- | --- |
| [0001](0001-foundations-and-first-git-checkpoint.md) | Evidence and assessment for setup, first output, and the first Git commit/push |
| [0002](0002-variables-and-assignment.md) | Next lesson and assignment; awaiting learner work at issue time |
| [0003](0003-variables-review.md) |  |
| [0004](0004-spacing-cost-and-readability.md) |  |
| [0005](0005-assignment-complete-and-integer-updates.md) |  |
| [0006](0006-inventory-review-initial-output.md) |  |
| [0007](0007-inventory-complete-and-first-debugging.md) |  |

**Data and reusable logic**
| Record | Purpose |
| --- | --- |

# Course Direction

| Stage | Coverage |
| --- | --- |
| Foundations | Environment, terminal, print, variables, strings, integers, floats, booleans, operators, input, conditions, loops, break/continue, basic exceptions |
| Data and reusable logic | Lists, tuples, sets, dictionaries, mutability/copying, indexing/slicing, comprehensions, functions, parameters, returns, scope, recursion, lambda |
| Programs and dependencies | Files, context managers, paths, encodings, CSV/JSON, modules, packages, virtual environments, pip, exception else/finally, debugging, automated tests |
| Design and advanced language tools | Classes, composition, inheritance, polymorphism, encapsulation, dataclasses, type hints, iterators, generators/yield, closures, decorators, partial functions |
| Deep Python and performance | Data model, descriptors, introspection, metaclasses, method resolution and super(), asyncio, threads, multiprocessing, algorithms, profiling, memory, extension modules |
| Distribution and collaboration | Architecture, documentation, unittest/pytest and TDD practice, packaging and PyPI, APIs/databases, Git branches/reviews/merges/conflicts/recovery, GitHub Actions, releases and relevant repository settings |

Style, debugging, testing, terminal use, and editor/GitHub shortcuts are recurring practices throughout the course. Future numbered records expand the curriculum as prerequisites are learned.
