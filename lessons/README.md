# Python training: append-only course record

Created: 2026-09-09. Repository: DevilMedlar/python-training.

This is the durable course record for tutoring, review, and resuming work. The learner has authorized the tutor to maintain Markdown records under lessons/. The learner writes the exercise programs and practices terminal and Git commands.

**How to maintain this record.**

- Preserve existing numbered lesson records and their text. Add a new numbered Markdown file for each subsequent lesson, review, correction, or checkpoint. Do not rewrite or delete earlier lesson entries. This README is the maintained index and remaining curriculum; update it in place.
- Continue numbering after the highest existing numbered record. Whenever a lesson Markdown file is added, update the appropriate Record/Purpose table in this README with its link and a concise, non-empty purpose as part of the same change.
- Treat Stage/Coverage as a growing, non-exhaustive outline of material still to teach. Add relevant topics within each stage as they are identified. Remove each covered topic as the lesson records document it. For a partly covered topic, retain only its untaught portions. Keep a stage while any listed coverage remains; remove the stage row when its final listed coverage item is removed. Restore a stage if additional topics in that area need teaching.
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
| [0002](0002-variables-and-assignment.md) | Variable assignment, reassignment, naming, and the stored-total exercise |
| [0003](0003-variables-review.md) | Review variable behavior and predictions; identify spacing and explanation follow-ups |
| [0004](0004-spacing-cost-and-readability.md) | Accept the spacing correction and explain source size versus readability |
| [0005](0005-assignment-complete-and-integer-updates.md) | Complete assignment practice; introduce integer updates with `=`, `+=`, and `-=` |
| [0006](0006-inventory-review-initial-output.md) | Review integer updates and identify the missing starting output |
| [0007](0007-inventory-complete-and-first-debugging.md) | Complete inventory practice; introduce tracebacks, `NameError`, and Go to Line |
| [0008](0008-debugging-complete-and-arithmetic.md) | Complete the first debugging exercise; introduce multiplication, division, floor division, remainders, and basic numeric types |

**Data and reusable logic**

| Record | Purpose |
| --- | --- |

# Course Direction

This table is a growing, non-exhaustive outline of material still to teach. Each stage can include additional topics beyond those currently listed; expand it as the course develops. Remove a listed topic after it has been taught, while keeping exercise status, evidence, and further practice in the numbered records. Remove a stage when its listed coverage is empty, and add it back if further topics in that area are identified. Covered skills continue to be used and revisited.

| Stage | Coverage |
| --- | --- |
| Foundations | String operations and formatting, integer conversions and representations, further float operations and precision/rounding, booleans, powers and operator precedence, signed remainders and further numeric edge cases, comparison and logical operators, input, conditions, loops, break/continue, exception handling |
| Data and reusable logic | Lists, tuples, sets, dictionaries, mutability/copying, indexing/slicing, comprehensions, functions, parameters, returns, scope, recursion, lambda |
| Programs and dependencies | Files, context managers, paths, encodings, CSV/JSON, modules, packages, virtual environments, pip, exception else/finally, debugger use and breakpoints, automated tests |
| Design and advanced language tools | Classes, composition, inheritance, polymorphism, encapsulation, dataclasses, type hints, iterators, generators/yield, closures, decorators, partial functions |
| Deep Python and performance | Data model, descriptors, introspection, metaclasses, method resolution and super(), asyncio, threads, multiprocessing, algorithms, profiling, memory, extension modules |
| Distribution and collaboration | Architecture, documentation, unittest/pytest and TDD practice, packaging and PyPI, APIs/databases, Git branches/reviews/merges/conflicts/recovery, GitHub Actions, releases and relevant repository settings |

Style, debugging, testing, terminal use, and editor/GitHub shortcuts are recurring practices throughout the course. Future numbered records expand the curriculum as prerequisites are learned.
