# Record 0012: input complete, booleans, and comparisons

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Interactive inventory review and corrected Phase 1 lesson |
| Assigned input lesson | [Record 0011](0011-garden-complete-and-input.md) |
| Verified learner commit | [905088f](https://github.com/DevilMedlar/python-training/commit/905088fa74e22400faada2feb31b5de08881d379) |
| Verified source | [inventory.py at this commit](https://github.com/DevilMedlar/python-training/blob/905088fa74e22400faada2feb31b5de08881d379/inventory.py) |
| File blob | 9a27abf08c84b8206a30c476acf386d2fe36c155 |
| Input exercise status | Implementation and all three requested runs complete |
| Course phase | Phase 1: Beginner (Foundations) |
| Next practice | Boolean values and numeric comparisons in comparisons.py |
| Lesson status | Replacement lesson issued; comparison practice awaiting learner evidence |

**Evidence.** The learner's six-line inventory.py matches the file fetched from the pinned commit. They supplied two valid-input terminal runs and the requested invalid-input traceback. The tutor verified repository content; the runtime evidence is the learner's transcript, not a claimed tutor execution in the Codespace.

```python
books = int(input("How many books do you have? "))
print(books)
books += 8
print(books)
books -= 5
print(books)
```

| Entered response | Observed result | Assessment |
| --- | --- | --- |
| 12 | 12, 20, 15 | Correct |
| 7 | 7, 15, 10 | Correct |
| twelve | ValueError on line 1 during int conversion; no numeric outputs | Expected for the assigned observation |

The supplied error was:

```text
ValueError: invalid literal for int() with base 10: 'twelve'
```

**Strengths and completion.** The learner correctly combines input() and int(), provides a clear prompt, uses the entered integer in the existing updates, removes the old recount, preserves the requested output order, and demonstrates behavior for valid and invalid text. Names and operator spacing are consistent. The deliberately observed ValueError is not a learner mistake.

No separate pre-run predictions were included in this submission. Do not describe the terminal outputs as evidence that predictions were supplied. Accept the correct implementation and complete runtime evidence as sufficient to progress; encourage prediction in later practice without requiring a retrospective rewrite of this successful submission.


**Current lesson and phase order.** At the learner's explicit request, record 0012 is renamed and rewritten as a Phase 1 lesson. This replacement and the README supersede the previous error-handling assignment and the next-step plan in record 0011. Formal try/except/else/finally instruction and practice belong to Phase 2, Data and reusable logic. Check the learner's [phase guide](../README.md) before planning later lessons. The earlier preview does not complete that Phase 2 topic.

Earlier exercises and their resolved corrections remain complete at the demonstrated scope. Continue with the lesson below; the current practice file is comparisons.py.

**Boolean values.** Python's bool type has two values: True and False. Use those exact capitalizations without quotation marks. A value such as "True" is text of type str. Booleans express whether a statement is true or false. For example:

```python
is_ready = True
print(is_ready)
```

This prints True. A comparison can calculate a boolean instead of assigning one directly. Source: [Python boolean type](https://docs.python.org/3.14/library/stdtypes.html#boolean-type-bool).

**Six numeric comparison operators.** The following comparisons use ordinary integers and produce boolean results:

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| == | Equal to | 8 == 10 | False |
| != | Not equal to | 8 != 10 | True |
| < | Less than | 8 < 10 | True |
| <= | Less than or equal to | 8 <= 10 | True |
| > | Greater than | 8 > 10 | False |
| >= | Greater than or equal to | 8 >= 10 | False |

The equality boundary matters: 10 < 10 is False, while 10 <= 10 is True. Likewise, 10 > 10 is False and 10 >= 10 is True. Source: [Python comparisons](https://docs.python.org/3.14/library/stdtypes.html#comparisons).

**Assignment and equality have different jobs.** A single = assigns a value to a name. The == operator compares values. In `apples = 8`, apples is assigned 8. The expression `apples == 10` checks equality and leaves apples unchanged. Keep comparison operators together and use spaces on either side, as in `apples >= target`.

**Worked example.**

```python
apples = 8
target = 10
has_enough = apples >= target
print(has_enough)
```

The comparison 8 >= 10 is False, so has_enough refers to False and the print displays False. The assignment stores the calculated result, just as the earlier arithmetic assignments stored numeric results. Printing a comparison reports its boolean result; making a decision with if is the next lesson.

**Learner assignment: comparisons.py.** Create a new file with target equal to 20. Ask for a book count with input() and convert it to an integer named books using the input pattern already learned.

Use each of the six numeric comparison operators once to answer the following questions, comparing books on the left with target on the right. Print the six boolean results in this order:

1. Is books equal to target?
2. Is books different from target?
3. Is books less than target?
4. Is books less than or equal to target?
5. Is books greater than target?
6. Is books greater than or equal to target?

Either print each comparison directly or store its result in a descriptive variable first. Calculate from books and target rather than writing fixed True/False answers. No particular intermediate variable names are required.

Save and run `python3 comparisons.py`. Use the same saved program for the three entered counts 19, 20, and 21. Predict each set of six boolean outputs before running. Send the code, predictions, and actual outputs. These cases compare values below, equal to, and above the target.

**Review expectations.** The table below is an answer key for the tutor; these are not observed learner results.

| Entered books | == | != | < | <= | > | >= |
| --- | --- | --- | --- | --- | --- | --- |
| 19 | False | True | True | True | False | False |
| 20 | True | False | False | True | False | True |
| 21 | False | True | False | False | True | True |

Review operator selection, the equality boundary, boolean output, variable use, and the requested order. The prompt is expected extra terminal text. The learner's comparison skills are not yet assessed; do not invent a weakness or claim mastery before the submission.

**Resume state.** Basic input practice remains complete. This written replacement introduces boolean values and six numeric comparisons; the new exercise awaits learner work. After successful practice, teach if/elif/else and its indentation, then boolean logic and the remaining Phase 1 material, including loops and break/continue. Comparison chaining and truthiness can be added as related foundation topics. Keep formal exception handling for Phase 2.

**Record maintenance.** This rename and rewrite is the learner-authorized exception for record 0012. Continue the append-only record policy for subsequent work unless the learner explicitly directs another replacement. The next new record number remains 0013. Update the README index and coverage to match this file. Preserve the learner's Python files and choose meaningful Git checkpoints.
