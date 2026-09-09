# Record 0015: reading goals complete, f-strings, and not

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Combined-condition review and Phase 1 extension |
| Previous lesson | [Record 0014](0014-conditionals-complete-and-combined-conditions.md) |
| Phase guide | [Root README](../README.md), Phase 1: Beginner (Foundations) |
| Verified learner commit | [a20ea87](https://github.com/DevilMedlar/python-training/commit/a20ea873151ff6072526e8eeee2529f2c7c7ca75) |
| Verified source | [reading_goals.py at this commit](https://github.com/DevilMedlar/python-training/blob/a20ea873151ff6072526e8eeee2529f2c7c7ca75/reading_goals.py) |
| File blob | d061e56be214523e7e2507dc1fcc86bc464b28f4 |
| Runtime evidence | Learner's five pasted Codespace runs |
| and/or exercise status | Functionally complete at the demonstrated scope |
| Cleanup pending | Rename completeed_books to completed_books |
| Current lesson | Basic f-string explanation; Rename Symbol; not with a named boolean; separate if statement |
| New assignment | Extend reading_goals.py; two actual runs |
| New assignment status | Issued in chat; awaiting code and runs |

**Verified evidence.** The pinned repository file exactly matches the learner's submitted code:

```python
days = int(input("How many days did you spend reading? "))
completeed_books = int(input(f"How many books did you read in {days} day(s)? "))

if completeed_books >= 3 and days >= 5:
    print("Both goals reached")
elif completeed_books >= 3 or days >= 5:
    print("One goal reached")
else:
    print("Neither goal reached")
```

The learner asks for days first, so record the inputs in that order. This is a valid variation on the original task.

| Days entered | Completed books entered | Observed result | Assessment |
| --- | --- | --- | --- |
| 5 | 3 | Both goals reached | Correct at both thresholds |
| 4 | 3 | One goal reached | Correct when only the book goal is met |
| 5 | 2 | One goal reached | Correct when only the days goal is met |
| 4 | 2 | Neither goal reached | Correct when neither goal is met |
| 6 | 4 | Both goals reached | Correct above both thresholds |

The tutor verified source, while runtime evidence is the learner's pasted terminal transcript. Do not claim the tutor ran this code in the learner's Codespace. The five-case and/or assignment is complete; do not require predictions or repeat all five cases merely to mark it complete.

**Strengths.** The learner uses two separate integer inputs, forms complete comparisons on both sides of and/or, uses inclusive minimum thresholds, puts the both-goals branch first, and produces the correct result in all requested cases. Their code demonstrates the intended inclusive-or behavior within the first-match chain. Indentation, colons, and operator spacing are consistent. The second input prompt successfully incorporates the earlier input using an f-string. These are successful practical demonstrations at this scope, not a claim of broad mastery.

**Naming cleanup.** completeed_books has an extra e. It is used consistently in all three occurrences, so the misspelling does not cause a NameError. Request completed_books for readability as part of the next edit, without requiring a separate resubmission of the completed challenge or labeling this isolated typo as a broad weakness.

Teach Rename Symbol: put the cursor in the variable name, press F2, type completed_books, and press Enter. With working Python rename support, the editor updates the variable definition and its references. The command is language-aware; do not describe it as replacing every matching text fragment anywhere. If the key is intercepted, use the already taught Command Palette and find Rename Symbol. If rename support is unavailable, manually correct this small file's definition and uses; no extension installation or repository setting change is assigned. The shortcut has been explained, not observed.
Sources: [VS Code Rename Symbol](https://code.visualstudio.com/docs/editing/refactoring#rename-symbol), [Python editing support](https://code.visualstudio.com/docs/python/editing).

**Review and explain the learner's f-string.** The f prefix makes the string a formatted string literal. In the supplied prompt, Python evaluates days when that line runs and inserts its value at {days}. With days equal to 5, the prompt includes "5 day(s)". This is valid Phase 1 string work introduced by the learner and now explained by the tutor. Do not pretend it was assigned earlier or mark all string formatting complete. Escaped braces, conversion flags, precision/alignment, and other formatting features remain for future instruction.
Source: [Python formatted string literals](https://docs.python.org/3.14/tutorial/inputoutput.html#formatted-string-literals).

**New lesson: not and a named boolean.** For booleans, not True produces False and not False produces True. It produces a result and does not reassign the original variable. Recall that the result of a comparison can be assigned to a descriptive variable. The named boolean can itself be used as an if condition; an extra comparison with True is unnecessary. Today's teaching uses boolean values; broader truthiness remains for later.
Source: [Python boolean operations](https://docs.python.org/3.14/library/stdtypes.html#boolean-operations-and-or-not).

Use this separate worked example in chat:

```python
pencils = 2
supplies_ready = pencils >= 5

if supplies_ready:
    print("Supplies ready.")
else:
    print("Supplies low.")

if not supplies_ready:
    print("Buy more pencils.")
    print(f"Pencils available: {pencils}")
```

Output:

```text
Supplies low.
Buy more pencils.
Pencils available: 2
```

Explain that supplies_ready holds False because 2 >= 5 is False. The first if/else chooses its else block. Python then reaches a separate if statement: not supplies_ready is True, so both of that block's print statements run. The variable supplies_ready remains False.

**Separate decisions and grouping.** Only one branch is selected within a particular if/elif/else chain. A separate if after that chain makes another decision. Align the new if with the earlier if at the outer indentation level, and indent both reminder statements beneath it. This is an independent decision after the chain; nested conditionals have not been taught here. The example also reinforces multiple statements belonging to one block. Do not imply that a true condition in one chain prevents all later independent if statements from executing.
Source: [Python if statement](https://docs.python.org/3.14/reference/compound_stmts.html#if).

**Learner extension in reading_goals.py.** Build on the existing file:

1. Correct the variable name to completed_books everywhere.
2. After the inputs, assign the result of the existing both-goals condition to a descriptive boolean named both_goals_reached.
3. Use that boolean as the first if condition in the existing chain. Retain the three existing result messages and the either-goal check.
4. After the complete chain, add a separate if that uses not with that boolean. Whenever at least one goal is still unfinished, it should contain two print calls: first "Keep working on the remaining goals.", then an f-string showing the current completed_books and days in a progress summary.
5. Keep both prints inside the new conditional block so they appear together only when further work is needed.

The progress summary can use wording such as "Progress: 3 books over 4 day(s)." Equivalent clear wording is fine; it must interpolate the current variables. The tutor supplies the requirements and supplies example, not the finished reading_goals.py implementation. This extends boolean logic, reuses the learner's basic f-string, and gives the first practical check of multiple statements in a branch.

Save and run:

```bash
python3 reading_goals.py
```

Use these two cases, following the learner's days-first prompt order:

| Days | Books | Expected behavior after prompts |
| --- | --- | --- |
| 5 | 3 | Both goals reached; no reminder or progress summary |
| 4 | 3 | One goal reached, then the reminder and a progress summary containing 3 books and 4 days |

Ask for the updated code and actual outputs only. These cases check both outcomes of the new not condition and placement of both reminder statements. The original five-case and/or evidence remains accepted. Do not add predictions, input-validation infrastructure, loops, or exception handlers.

**Review and pending evidence.** Check that both_goals_reached is calculated after reading both inputs, uses the correct existing comparisons, and is tested directly in the first condition. Verify the separate if uses not without overwriting the stored boolean. Check outer indentation of the separate if, grouping of both print calls, variable interpolation in the progress summary, and completion of the spelling correction. Negative-input checks have not been assigned, so do not introduce an imagined existing validation branch. Rename-tool use, not behavior, independent decisions, and multiple-statement blocks are not yet demonstrated by a new submission. Unknown skills are not weaknesses.

**Resume state.** Initial comparisons, if/elif/else, and and/or practice remain complete at their demonstrated scopes. Basic f-string interpolation now has learner evidence and a tutor explanation. The current task is the two-run not/reminder extension plus naming cleanup. After reviewing it, continue Phase 1 with practical input range checks and nested conditionals, teaching both before assigning them. Truthiness, mixed boolean grouping, further formatting, and loops remain in detailed coverage. Formal try/except/else/finally stays in Phase 2.

**Record maintenance.** Preserve 0001-0014. Add 0015 to lessons/README.md with a Record/Purpose row; update the current checkpoint. Remove introduced logical not, basic independent-if behavior, and basic f-string interpolation from remaining coverage, retaining their untaught related topics. The learner receives the complete teaching in chat and need not read or pull these tutor records before practice. The next new record number is 0016.
