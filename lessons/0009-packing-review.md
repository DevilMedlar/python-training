# Record 0009: packing review and required follow-ups

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | First packing submission review |
| Assigned lesson | [Record 0008](0008-debugging-complete-and-arithmetic.md) |
| Verified learner commit | [1022a78](https://github.com/DevilMedlar/python-training/commit/1022a78f0a64b5ced8c4b67e08bc1148b278f43c) |
| Verified source | [packing.py at this commit](https://github.com/DevilMedlar/python-training/blob/1022a78f0a64b5ced8c4b67e08bc1148b278f43c/packing.py) |
| File blob | 9cb3130e36cdeeccd61a70d17f51633649184b9e |
| Current status | First case calculates correct values; required multiplication, output order, and second run remain pending |

**Evidence.** The learner submitted the following program, a prediction of 2, 24, 6, 6.5, and a terminal transcript with those same outputs. The repository file fetched at the pinned commit matches the submitted statements. Runtime evidence is supplied by the learner; the tutor has not run commands in their Codespace.

```python
stickers = 26
pack_size = 4
full_packs = stickers // pack_size
leftover_stickers = stickers % pack_size
packed_stickers = stickers - leftover_stickers
division_result = stickers / pack_size
print(leftover_stickers)
print(packed_stickers)
print(full_packs)
print(division_result)
```

**Assessment against the assigned behavior.**

| Requirement | Finding |
| --- | --- |
| Start with 26 stickers and pack size 4 | Correct |
| Calculate full_packs using floor division | Correct: 6 |
| Calculate leftover_stickers using remainder | Correct: 2 |
| Calculate packed_stickers using multiplication | Value 24 is correct, but subtraction was used instead of the required multiplication |
| Calculate division_result using ordinary division | Correct: 6.5 |
| Print full_packs, leftover_stickers, packed_stickers, division_result in that order | Submitted order is leftover_stickers, packed_stickers, full_packs, division_result; revision needed |
| Predict the first run's output | Correct for the submitted program's actual print order |
| Repeat after changing only the starting count to 28 | Not yet submitted; keep pending |
| Names and spacing | Descriptive lowercase names, underscores, and operator spacing are correct |

**Strengths.** The learner chooses //, %, and / appropriately, calculates from variables rather than fixed answers, predicts the written program accurately, and supplies actual output. Subtracting the leftovers from the total is mathematically valid for this packing calculation and returns the correct number of packed stickers. Do not label that alternative as a Python error or bad mathematical reasoning.

**Specific practice target.** The assignment explicitly required using all four newly taught operators, including multiplication for packed_stickers, and an exact output order. Checking the requested method and output sequence remains a useful practice target. Record 0006 also had an output-requirement follow-up, which was resolved in record 0007; do not reopen that completed correction or infer a broad trait from these observations. Multiplication in this exercise is not yet demonstrated, which is different from demonstrated misunderstanding.

**Explanation and learner revision.**

1. Explain that the total in full packs can be calculated by multiplying the number of full packs by the number of stickers in each pack. Ask the learner to use those two variables with * for packed_stickers. Their subtraction gives the correct value, but multiplication is the specific practice requirement here.
2. Ask the learner to arrange the four print calls as full_packs, leftover_stickers, packed_stickers, division_result.
3. Have the learner predict and rerun the corrected 26-sticker case, then change only the starting sticker count to 28, predict again, save, and rerun. Request corrected code and predictions/actual outputs for both cases.

The arithmetic concepts were taught in record 0008. This response reinforces the relevant reasoning before requesting the changes; it should not provide a rewritten full solution or require a formal prose explanation.

**Expected results for the next review.** These are review expectations, not observed outputs from a corrected submission:

| Starting stickers | full_packs | leftover_stickers | packed_stickers | division_result |
| --- | --- | --- | --- | --- |
| 26 | 6 | 2 | 24 | 6.5 |
| 28 | 7 | 0 | 28 | 7.0 |

Check both code and output: the values alone cannot establish that multiplication was used. Confirm the output sequence and the second case without adding new requirements. Do not require a commit or pull for this small correction.

**Resume state.** Packing practice remains in progress. Previous assignment, inventory, and first debugging exercises remain complete at their demonstrated scope. After the required revisions and both cases are satisfactory, record completion in a new numbered entry and proceed to powers and operator precedence as planned. Keep any further practice proportional to specific evidence.

**README maintenance.** Add this record and its purpose to the index in the same commit. Stage/Coverage already excludes the arithmetic introduced in record 0008; this review introduces no new coverage item to remove. Keep the remaining coverage and its non-exhaustive policy intact. Preserve all older numbered records and the learner's programs.

References carried forward from the verified lesson: [Python arithmetic introduction](https://docs.python.org/3.14/tutorial/introduction.html#numbers) and [numeric operations](https://docs.python.org/3.14/library/stdtypes.html#numeric-types-int-float-complex).
