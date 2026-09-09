# Record 0006: integer updates and the missing initial output

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Inventory submission review and small correction |
| Assigned lesson | [Record 0005](0005-assignment-complete-and-integer-updates.md) |
| Verified learner commit | [e9e8336](https://github.com/DevilMedlar/python-training/commit/e9e8336cc17fd2cd64b41a7041f830b0d452cfc4) |
| Verified source | [inventory.py at this commit](https://github.com/DevilMedlar/python-training/blob/e9e8336cc17fd2cd64b41a7041f830b0d452cfc4/inventory.py) |
| File blob | 74e35401cbc52f696f3864c6dfe5d1f595c56581 |
| Status | Update operations and style correct; required initial print still missing |

The learner's pasted code exactly matches the seven-line inventory.py fetched from the stated commit. The supplied prediction and terminal output are both 20, 15, 3. The code initializes books to 12, adds 8, prints, subtracts 5, prints, assigns 3, and prints.

**Assessment against the assignment.**

| Requirement | Finding |
| --- | --- |
| Start books at 12 | Correct |
| Print the starting count | Missing: the first print occurs after books += 8 |
| Add 8 using += and print | Correct; prints 20 |
| Subtract 5 using -= and print | Correct; prints 15 |
| Set the recount to 3 using = and print | Correct; prints 3 |
| Predict output | Correct for the submitted program; the task requested four outputs |
| Names and spacing | Correct; spacing around =, +=, and -= is retained in a new exercise |

**Strengths demonstrated.** The learner uses addition updates, subtraction updates, and direct reassignment appropriately, predicts the resulting values of the written program, and carries the spacing correction into fresh code.

**Specific follow-up.** One explicit output requirement was omitted. This is a requirements-completeness issue, not evidence of misunderstanding the arithmetic or augmented assignment. Do not generalize it into a broad judgment about carelessness or understanding.

The first assigned step was to start books at 12 and print the count. The submitted code changes the count before its first print. Add a print of the initial value before the delivery update. The tutor should identify the needed placement and let the learner make the edit, without rewriting the full program for them.

The corrected program should produce:

```text
12
20
15
3
```

A useful checking habit is to walk through the numbered requirements and identify how the code satisfies each one. Correct output prediction for a program does not, on its own, establish that every requested behavior is present.

**Next learner action.** Add the initial print, save, rerun python3 inventory.py, and submit the revised code and output. A formal prose explanation and another Git checkpoint are not required for this correction.

**Resume state.** The earlier assignment/reassignment lesson remains complete. Integer update practice is awaiting this one correction. If the corrected submission shows the initial output in the proper position, record completion in a new entry and proceed to teaching traceback reading and a simple case-sensitive-name debugging exercise. Continue accepting informal explanations when their meaning is clear.

Prior official references remain applicable: [Python augmented assignment](https://docs.python.org/3.14/reference/simple_stmts.html#augmented-assignment-statements), [print](https://docs.python.org/3.14/library/functions.html#print), and [PEP 8 operator spacing](https://peps.python.org/pep-0008/#other-recommendations).

This entry is a new append-only record. Earlier lesson files are preserved; synchronize tutor notes into the Codespace at a suitable later Git checkpoint.
