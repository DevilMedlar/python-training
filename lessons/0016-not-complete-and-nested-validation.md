# Record 0016: not complete and nested validation

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Reminder extension review and Phase 1 nested conditions |
| Previous lesson | [Record 0015](0015-reading-goals-complete-and-not.md) |
| Phase guide | [Root README](../README.md), Phase 1: Beginner (Foundations) |
| Verified learner commit | [69a8d71](https://github.com/DevilMedlar/python-training/commit/69a8d713dfa2a39a13a42c08ebb2a8e68d7719e1) |
| Verified source | [reading_goals.py at this commit](https://github.com/DevilMedlar/python-training/blob/69a8d713dfa2a39a13a42c08ebb2a8e68d7719e1/reading_goals.py) |
| File blob | 4640dd378eb8ef9143213d6de857256137828de6 |
| Runtime evidence | Learner's two pasted Codespace runs |
| not/reminder exercise | Functionally complete at the demonstrated scope |
| Previous naming correction | completed_books verified |
| Display cleanup pending | workning to working; add books to the progress label |
| New lesson | Nested conditionals and nonnegative integer-count validation |
| New assignment | Extend reading_goals.py with an outer validation decision; five runs |
| New assignment status | Taught and issued in chat; awaiting learner work |

**Evidence.** The learner's pasted source exactly matches the file at the pinned commit:

```python
days = int(input("How many days did you spend reading? "))
completed_books = int(input(f"How many books did you read in {days} day(s)? "))
both_goals_reached = completed_books >= 3 and days >= 5

if both_goals_reached:
    print("Both goals reached")
elif completed_books >= 3 or days >= 5:
    print("One goal reached")
else:
    print("Neither goal reached")

if not both_goals_reached:
    print("Keep workning on the remaining goals.")
    print(f"Progress: {completed_books} over {days} day(s)")
```

| Days | Books | Learner's observed output after prompts | Assessment |
| --- | --- | --- | --- |
| 5 | 3 | Both goals reached | Correct; reminder block skipped |
| 4 | 3 | One goal reached; Keep workning on the remaining goals.; Progress: 3 over 4 day(s) | Correct conditional behavior; both reminder lines ran, with display cleanup noted |

Semicolons in the table separate the three distinct output lines from the second run. The tutor verified repository source; execution evidence is the learner's terminal transcript. Do not claim the tutor ran the code in the learner's Codespace. The previous five-case and/or evidence remains accepted.

**Demonstrated strengths and resolved follow-ups.** The learner calculates both_goals_reached after both inputs, stores a boolean from the correct comparisons, and uses that variable directly in the first if. The independent not condition follows the entire classification chain and does not overwrite the boolean. Both reminder prints are correctly grouped under the same condition, providing the practical multiple-statement block demonstration that had remained pending since 0013/0014. Both outcomes of the reminder condition are demonstrated. The variable name is now completed_books throughout; do not keep requesting that correction. Use of the F2 shortcut itself was not reported and must not be inferred from the renamed source.

**Display feedback.** Request two small edits during the next extension: change workning to working and identify the book count in the progress line, for example "Progress: 3 books over 4 day(s)". These do not invalidate the demonstrated boolean or indentation logic. Do not require a separate resubmission or additional old-case runs merely for wording. No functional errors were observed in the requested cases. Basic f-string interpolation is reinforced by correct use of both inputs. One successful extension is evidence at this scope, not universal mastery.

**New lesson: validate a number's allowed range.** int can convert a signed integer string such as "-1"; successful conversion does not enforce this program's nonnegative-count rule. For this exercise, both days and completed_books must be at least zero. Zero is valid. Check the converted numbers using familiar comparisons and or. Text-conversion recovery is still Phase 2; do not claim the new range check handles input such as "five".
Source: [Python int](https://docs.python.org/3.14/library/functions.html#int).

**Nested conditions.** A conditional can be inside the block of another conditional. The outer decision controls whether Python reaches that inner decision. Teach the concept in chat before assigning the edit, using this different-domain example:

```python
tickets = 3

if tickets < 0:
    print("Ticket count cannot be negative.")
else:
    if tickets >= 5:
        print("Group booking.")
    else:
        print("Standard booking.")
    print(f"Tickets requested: {tickets}")
```

For tickets equal to 3, the output is:

```text
Standard booking.
Tickets requested: 3
```

For tickets equal to -1, only the negative-count message prints; the whole outer else is skipped. Explain that the nested booking decision is reached only for a nonnegative count, and that the final ticket summary is inside the outer else but outside the inner if/else chain. The booking thresholds are illustrative rules for the example.
Source: [Python compound statements and if](https://docs.python.org/3.14/reference/compound_stmts.html#if).

**Indentation and editor practice.** Related if/elif/else headers align at their own level. In this example, the outer headers have zero leading spaces, the inner headers have four, and the inner branch bodies have eight. The final ticket-summary print has four spaces, so it belongs to the outer else. The language uses indentation to define these blocks; four spaces per level is the course's PEP 8 convention, not the only width Python can parse.
Source: [PEP 8 indentation](https://peps.python.org/pep-0008/#indentation).

Revisit the already introduced Windows VS Code shortcuts for this practical block move. With editor focus, select the existing goal workflow from its both_goals_reached assignment through its last print, then use Ctrl+] to indent the selected lines one level. Ctrl+[ outdents. The commands use the configured indentation width; preserve relative indentation and check that the resulting levels are four and eight spaces. Indent Line and Outdent Line are also available through the Command Palette if a browser intercepts a shortcut. Usage is not yet observed.
Source: [VS Code default shortcuts](https://code.visualstudio.com/docs/reference/default-keybindings).

**Learner assignment: extend reading_goals.py.**

1. Apply the two display cleanups while editing.
2. Keep both integer input statements first. For this version, collect both fields before the range check.
3. Add one outer if/else after the inputs. If either count is negative, print "Counts cannot be negative." once.
4. Put the full existing goal workflow inside the outer else: the boolean assignment, the classification chain, and the independent reminder condition with both of its print statements.
5. Preserve the previous goal thresholds and reminder behavior for valid counts. Keep zero valid for each count; no relationship between the two counts is imposed.

Use or for the two possible negative fields so either invalid value is enough to select the error path. The validation else must contain the reminder condition as well as the classification. Inside that else, the classification if and the separate reminder if align at four spaces; their print statements are at eight spaces.

No goal classification, reminder, or progress line should appear for a negative count. The input prompts are expected extra terminal text. End the script naturally after the selected path; no exit helper, loop, function, or exception handler is required. This is the learner's code to write; the tutor gives the separate ticket example and requirements, not the finished reading-goals implementation.

Save and run:

```bash
python3 reading_goals.py
```

Submit the updated code and actual runs for these input pairs, in the learner's days-first order:

| Days | Books | Expected behavior after prompts |
| --- | --- | --- |
| -1 | 3 | Counts cannot be negative. only |
| 5 | -1 | Counts cannot be negative. only |
| 0 | 0 | Neither goal reached, then reminder and progress showing 0 books and 0 days |
| 5 | 3 | Both goals reached only |
| 4 | 3 | One goal reached, then reminder and progress showing 3 books and 4 days |

These cases test each negative field independently, the valid zero boundary, and correct placement of the three possible classifications and reminder after moving the workflow. Do not request predictions. Five focused cases are sufficient for this assigned behavior; do not repeat all previous challenges.

**Review criteria and uncertainty.** Verify the comparison boundary, or rather than and for negative inputs, single error output, complete containment of processing in the valid-data block, unchanged valid goal decisions, and both display edits. Check that both_goals_reached is assigned before it is used and that its uses are inside the same valid-data branch. Nested indentation and negative-count validation are introduced here but await new learner evidence. Unknown skills are not weaknesses. Do not claim handling of non-integer text or completion of all input validation.

**Resume state.** The not extension, named-boolean use, independent decisions, grouped statements, and completed_books naming fix are complete at the demonstrated scope. Current work is nested validation plus two display cleanups. After reviewing the new submission, continue Phase 1 with bounded numeric ranges and comparison chaining as related practice; consult the remaining coverage before planning. Further formatting, truthiness, mixed boolean grouping, loops, and repeated prompts remain. Formal try/except/else/finally remains Phase 2.

**Record maintenance.** Preserve 0001-0015 and the learner's Python source. Add 0016 to the lessons README index with its purpose; update the current checkpoint. Remove the introduced basic nesting and nonnegative-count check from remaining coverage, retaining upper/combined range checks and repeated prompts. Keep the root README as the phase skeleton. Teach the complete lesson in chat; the learner need not read or pull these tutor notes before practicing. The next new record is 0017.
