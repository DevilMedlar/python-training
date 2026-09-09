# Record 0004: spacing, source size, and readability

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Revision review and explanation of a style tradeoff |
| Previous review | [Record 0003](0003-variables-review.md) |
| Current code status | Behavior and formatting accepted |
| Remaining lesson item | Learner's explanation of the stored total |
| Verified learner commit | [68eef4c](https://github.com/DevilMedlar/python-training/commit/68eef4c1367c1bde2c77c66eb466041850a09d68) |
| Verified source | [variables.py at this commit](https://github.com/DevilMedlar/python-training/blob/68eef4c1367c1bde2c77c66eb466041850a09d68/variables.py) |
| Verified file blob | 5a3d0d77f2df4c52051db986c28d985d7230cc45 |

This new record updates the current assessment while preserving earlier entries. The corrected variables.py now exists on GitHub and exactly matches the learner's latest pasted code. The learner's rerun produced 10, 9, 10, 13, as required. No additional Git command transcript was provided, so this record verifies the repository result without claiming how the learner performed those Git operations.

**Changes since the previous review.**

| Item | Assessment now |
| --- | --- |
| Spacing around assignment = | Corrected in all five assignments |
| Variable names and spacing around + | Remain correct |
| Assignment/reassignment order and output | Remain correct |
| Explanation in the learner's own words | Still not supplied; keep pending |
| Source-size observation | Correct: adding ordinary spaces adds bytes to the source text |

The learner questioned the benefit of the spacing because each added space increases file size. Address that engineering question directly. Do not dismiss the observation or infer unwillingness to learn: the correction was completed, and the storage observation is accurate.

**Checked byte difference.**

The two pasted code versions were compared as ASCII-only text encoded in UTF-8, each with LF line endings and one final newline. The comparison is of the supplied text; it is not a measurement of an earlier unsaved editor buffer or of filesystem allocation.

| Version | UTF-8 source bytes under those conditions |
| --- | ---: |
| Original submission in record 0003 | 148 |
| Revised submission | 158 |
| Increase from inserted spaces | 10 |

There are five assignments and two inserted spaces per assignment. Each ordinary ASCII space occupies one byte in UTF-8, giving ten added bytes.

**Explanation prepared for the accompanying response.**

The spaces around these assignment operators are optional for Python syntax. They leave this program's calculation and output unchanged. Their purpose is readable, consistent source. PEP 8 explicitly motivates its conventions through readability and consistency and recommends one space on each side of assignment operators.

Source length, startup/parsing work, execution time, and runtime memory are separate measurements. A ten-byte reduction in this script's source is not evidence of a useful runtime optimization. The tutor should explain the tradeoff without claiming that added source bytes cost literally nothing or that all whitespace is irrelevant. Python whitespace can carry meaning in other contexts, including indentation and string literals.

Readability and project conventions are the priorities for these authored course files. When actual resource constraints arise, teach measurement and choose changes that address the observed constraint.

Sources checked: [PEP 8 readability rationale](https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds), [PEP 8 operator spacing](https://peps.python.org/pep-0008/#other-recommendations), and [Python whitespace between tokens](https://docs.python.org/3.14/reference/lexical_analysis.html#whitespace-between-tokens).

**Teaching adjustment and strengths.**

The learner applies a correction and asks about its practical justification. Pair future style guidance with its purpose, and distinguish language requirements from course conventions. Keep assessing continued spacing consistency in later work; do not claim a permanent habit is established from this revision alone.

**Next action and resume state.**

The revised code needs no further change for this exercise. Ask one short conceptual check: when pencils becomes 9, why does item_count remain 10 until its later assignment runs? This is a request for the previously assigned explanation, not a new programming exercise.

After a satisfactory explanation, record completion in a new numbered entry and continue with variable updates, naming, and basic debugging as planned in record 0002. If the answer reveals a specific misunderstanding, address it with a small different example. No misunderstanding has been demonstrated merely by the explanation being absent.

Preserve all earlier records. Sync new tutor notes into the Codespace at a suitable Git checkpoint using the previously taught workflow; this review does not require the learner to perform another commit or pull.
