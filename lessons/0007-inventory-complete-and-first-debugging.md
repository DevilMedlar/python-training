# Record 0007: inventory complete and first debugging practice

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Corrected inventory review and next lesson |
| Previous review | [Record 0006](0006-inventory-review-initial-output.md) |
| Verified repository commit | [43d257c](https://github.com/DevilMedlar/python-training/commit/43d257c29a65ffae03545415c8b69fbd562618ad) |
| Verified source | [inventory.py at this commit](https://github.com/DevilMedlar/python-training/blob/43d257c29a65ffae03545415c8b69fbd562618ad/inventory.py) |
| File blob | aacb893f6aea18bd4e1211360b8609e3494f62a8 |
| Inventory status | Complete: all four required outputs are present |
| Next practice | Read a traceback and fix an inconsistent variable name |

**Evidence and review.** The learner submitted the corrected program below. It matches the inventory.py fetched from the pinned repository commit. The learner's supplied terminal transcript shows 12, 20, 15, 3; these values agree with the program. This review does not claim a separate tutor execution in the learner's Codespace.

```python
books = 12
print(books)
books += 8
print(books)
books -= 5
print(books)
books = 3
print(books)
```

| Requirement | Result |
| --- | --- |
| Assign 12 and print the starting count | Correct: 12 |
| Add 8 with += and print | Correct: 20 |
| Subtract 5 with -= and print | Correct: 15 |
| Replace the count with 3 using = and print | Correct: 3 |
| Use consistent names and spaces around assignment operators | Correct |

**Strengths demonstrated.** The learner distinguishes integer updates from direct reassignment, follows the sequence of changing values, retains the spacing correction across exercises, and successfully applies feedback about the initial output.

**Resolved follow-up.** The omitted starting print in record 0006 is fixed. Do not carry it forward as an unresolved weakness or infer a broad problem from that single omission. This completes the assigned integer update exercise; it does not establish mastery of every augmented-assignment behavior or of debugging, which has not yet been demonstrated.

**Teaching preferences carried forward.** Explain a new concept before assigning work. The learner writes and repairs the exercise files; the tutor maintains the Markdown records. Assess the meaning of informal explanations without correcting their prose for professionalism. Continue teaching accurate code style and introducing useful editor shortcuts. Reuse earlier skills in later work instead of requiring repeated elementary print-only tasks.

**Next lesson: names and tracebacks.** A NameError occurs when Python cannot find a referenced local or global name. Names are case-sensitive, so lives and Lives are different names. A case mismatch is one possible cause of NameError, not its only cause. See the official [NameError reference](https://docs.python.org/3.14/library/exceptions.html#NameError) and [identifier rules](https://docs.python.org/3.14/reference/lexical_analysis.html#names).

Use this worked example before the learner's task:

```python
lives = 3
print(Lives)
```

The relevant error message is `NameError: name 'Lives' is not defined`. An actual traceback may also include source markers or a suggested correction. The first line assigns lives; the second tries to use the different name Lives. Changing the print to `print(lives)` fixes this example. Similarly, an update such as `coins += 3` needs a current value already assigned to that exact name.

Teach the learner to read the final error line for the exception type and message, then the filename and line number immediately above it, then inspect the indicated code and its assignments. In these simple scripts an unhandled exception stops execution: earlier output remains, and later statements do not run. See the [Python 3.14 errors tutorial](https://docs.python.org/3.14/tutorial/errors.html).

**Editor shortcut.** With the code editor focused, Ctrl+G opens Go to Line on Windows/Linux. Enter the line number and press Enter. The [VS Code keybinding reference](https://code.visualstudio.com/docs/reference/default-keybindings) documents the binding. The tutor should identify the platform scope rather than imply every shortcut is universal.

**Assigned practice: debugging.py.** Ask the learner to create this intentionally broken starter and run it unchanged once:

```python
coins = 7
print(coins)
Coins += 3
print(coins)
coins -= 2
print(coins)
```

Run command: `python3 debugging.py`.

The intended program prints the starting count, the count after receiving 3 more coins, and the count after spending 2. Ask the learner to use the actual traceback to find the inconsistent name, repair it, predict the three corrected outputs, save, and rerun. Request the original error message plus the corrected code and output; no formal explanation is required.

**Review criteria for the next submission.** The original starter prints 7 and then raises NameError at line 3 because Coins has no assigned value. A correct repair uses the same intended name consistently and produces 7, 10, 8. Check the learner's actual traceback and code rather than requiring identical diagnostic formatting. Keep the initial output and both updates. Determine from their submission whether traceback location and name consistency are understood; do not pre-label debugging as a weakness.

**Resume state.** Assignment/reassignment and this integer-update exercise are complete at the practiced level. Traceback reading, NameError, and Go to Line are being introduced with this review; the debugging exercise is awaiting learner evidence. After successful debugging practice, expand arithmetic and then input in small, taught steps, continuing to reuse variables and updates. A new commit/push/pull exercise is not required for each small submission.

**Repository continuity.** The observed main commit 43d257c has two parents and is titled "Merge remote-tracking branch 'refs/remotes/origin/main'". No failure is inferred from that merge. At the next Git checkpoint, inspect the actual local/remote state and account for tutor-note commits before guiding synchronization.

This is a new append-only lesson record. Preserve all earlier lesson files. Future corrections, assessments, and new lessons belong in additional numbered records.
