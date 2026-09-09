# Python training: append-only course record

Created: 2026-09-09. Repository: DevilMedlar/python-training.

This is the durable course record for tutoring, review, and resuming work. The learner has authorized the tutor to maintain Markdown records under lessons/. The learner writes the exercise programs and practices terminal and Git commands.

**Audience and file roles.** These Markdown files are the tutor's working records. Read them before teaching to track what has been introduced, what has been demonstrated, what needs practice, and what comes next. Deliver the complete lesson, explanations, worked examples, review, and assignment in the chat. The learner is not expected to read these files for ordinary lessons; they may inspect them when checking a suspected repeat or a topic introduced too early.

- The [root README](../README.md) is the growing skeleton outline and guide to phase order.
- This lessons/README.md is the detailed course tracker: the Record/Purpose index points to teaching and review history, the current checkpoint identifies active work, and Stage/Coverage lists material still to teach.
- Numbered records retain detailed evidence, teaching, assignments, assessments, preferences, and next actions. Read later records for updates that supersede historical status.

**How to maintain this record.**

- Preserve existing numbered lesson records and their text. Add a new numbered Markdown file for each subsequent lesson, review, correction, or checkpoint. Do not rewrite or delete earlier lesson entries. This README is the maintained index and remaining curriculum; update it in place.
- Continue numbering after the highest existing numbered record. Whenever a lesson Markdown file is added, update the appropriate Record/Purpose table in this README with its link and a concise, non-empty purpose as part of the same change.
- Treat Stage/Coverage as a growing, non-exhaustive outline of material still to teach. Add relevant topics within each stage as they are identified. Remove each covered topic as the lesson records document it. For a partly covered topic, retain only its untaught portions. Keep a stage while any listed coverage remains; remove the stage row when its final listed coverage item is removed. Restore a stage if additional topics in that area need teaching.
- Record corrections in a new entry that identifies the earlier entry and explicitly explains what is superseded. Historical observations remain historical observations.
- Before tutoring, inspect the latest records and any linked unresolved work. Before a repository write, check current files and branch state so concurrent learner work is preserved.
- Every new record should identify its evidence, topics taught, assignment, submission/review status, demonstrated strengths, difficulties or uncertainties, next action, and sources used.
- Separate introduced material, successful guided practice, independent demonstrations, and performance across repeated practice. One successful small exercise does not establish broad mastery.
- Record actual mistakes and remaining uncertainties separately. Do not invent weaknesses or assume an untested skill is a weakness.
- Documentation committed directly on GitHub does not automatically update an existing Codespace checkout. The learner need not pull tutor records before each exercise. Explain synchronization at a requested or meaningful Git checkpoint; do not make commit/push/pull a routine prerequisite for each lesson.

**Teaching agreement.**

The goal is deep practical Python fluency and strong command-line, Git, and GitHub skills. Remain in GitHub Codespaces until the learner asks to begin working directly on the PC. Introduce repository settings when they become relevant.

Follow the learner's phase order in the [repository README](../README.md), checking it before issuing a lesson. The current phase is Phase 1, Foundations: data types, basic operators, boolean logic, if/elif/else, and loops with break/continue. Formal exception handling with try/except/else/finally belongs to Phase 2, Data and reusable logic. Complete the foundation prerequisites before assigning that material. An early preview does not complete a later-phase topic.

Explain each new concept and command before assigning work. Use small worked examples, then let the learner implement the exercise. Review correctness, names, spacing, control flow, and readability even when output is correct. Distinguish language requirements, style guidance, and optional conventions.

Use consistent practice with variation and later revisits. Move through basic print usage promptly once demonstrated. Increase independence and review depth over time. Commit at meaningful checkpoints, not automatically after every small exercise.

Do not routinely request output predictions, especially for exercises containing multiple line-by-line prints. Ask for a prediction only when it is essential to a specific lesson or diagnosis, explain why, and keep it focused. The default submission is the learner's code and actual runs. This learner clarification supersedes routine prediction requirements in older records, including 0012.

Verify technical guidance against official documentation and the actual Python version. Do not imply that repository access reveals unsaved or unpushed Codespace files or live terminal state. The current confirmed interpreter is Python 3.14.2.

**Current checkpoint.** [Record 0015](0015-reading-goals-complete-and-not.md) completes the initial and/or reading-goals exercise: all five requested outcomes are correct, and the learner successfully uses a basic f-string in the second prompt. The spelling cleanup from completeed_books to completed_books is pending. The current Phase 1 lesson explains that f-string use, teaches Rename Symbol, and introduces not with a named boolean plus a separate if statement. An extension to reading_goals.py awaits learner code and two runs (days/books: 5/3 and 4/3). That extension will also check two statements grouped in one conditional block; this has been taught but not yet demonstrated.

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
| [0009](0009-packing-review.md) | Review correct packing values; request multiplication and output-order corrections, with the second run pending |
| [0010](0010-packing-complete-and-powers.md) | Complete packing practice; introduce positive integer powers, arithmetic grouping, and moving editor lines |
| [0011](0011-garden-complete-and-input.md) | Complete garden practice; introduce input(), integer-text conversion, and recognizing invalid input |
| [0012](0012-input-complete-and-comparisons.md) | Complete input practice; teach Phase 1 boolean values and numeric comparisons |
| [0013](0013-comparisons-review-and-conditionals.md) | Review comparisons and operand order; record tracking and prediction preferences; teach if/elif/else and indentation |
| [0014](0014-conditionals-complete-and-combined-conditions.md) | Complete first conditionals; explain printing multiple values; introduce and/or and the reading-goals exercise |
| [0015](0015-reading-goals-complete-and-not.md) | Complete and/or practice; review basic f-strings and naming; teach not, Rename Symbol, and a separate reminder condition |

**Data and reusable logic**

| Record | Purpose |
| --- | --- |

# Course Direction

This table is a growing, non-exhaustive outline of material still to teach. Each stage can include additional topics beyond those currently listed; expand it as the course develops. Remove a listed topic after it has been taught, while keeping exercise status, evidence, and further practice in the numbered records. Remove a stage when its listed coverage is empty, and add it back if further topics in that area are identified. Covered skills continue to be used and revisited.

| Stage | Coverage |
| --- | --- |
| Foundations (Phase 1) | String operations and further formatting beyond basic f-string interpolation, further integer conversions and representations, further float operations and precision/rounding, negative/fractional and chained powers, precedence involving signs and later operators, signed remainders and further numeric edge cases, comparison chaining, truthiness, mixed boolean-operator precedence/grouping, and/or with non-boolean operands and practical short-circuit guards, input range checks and repeated prompts, nested conditionals, for/while loops, break/continue |
| Data and reusable logic (Phase 2) | Lists, tuples, sets, dictionaries, mutability/copying, indexing/slicing, functions, parameters, returns, scope, recursion, lambda, error handling with try/except/else/finally, exception types and raising exceptions, end-of-input handling |
| Programs and dependencies (Phase 2) | Files, context managers, paths, encodings, CSV/JSON, modules, packages, virtual environments, pip, debugger use and breakpoints |
| Design and advanced language tools (Phase 3) | Classes, composition, inheritance, polymorphism, encapsulation, dataclasses, type hints, advanced comprehensions, iterators, generators/yield, closures, decorators, partial functions, asyncio, threads, multiprocessing |
| Deep Python and performance (Phase 4) | Data model, descriptors, introspection, metaclasses, method resolution and super(), algorithms, profiling, memory, extension modules |
| Distribution and collaboration (Phase 4) | Architecture, documentation, unittest/pytest and TDD practice, packaging and PyPI, APIs/databases, Git branches/reviews/merges/conflicts/recovery, GitHub Actions, releases and relevant repository settings |

Style, debugging, testing, terminal use, and editor/GitHub shortcuts are recurring practices throughout the course. Future numbered records expand the curriculum as prerequisites are learned.
