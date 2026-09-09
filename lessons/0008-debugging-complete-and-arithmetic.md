# Record 0008: debugging complete and arithmetic with groups

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Debugging submission review and next arithmetic lesson |
| Previous lesson | [Record 0007](0007-inventory-complete-and-first-debugging.md) |
| Verified learner commit | [3955e0d](https://github.com/DevilMedlar/python-training/commit/3955e0d945cd955736e21df3df8bfe5e7a11890c) |
| Verified source | [debugging.py at this commit](https://github.com/DevilMedlar/python-training/blob/3955e0d945cd955736e21df3df8bfe5e7a11890c/debugging.py) |
| File blob | 93af672ba8a809976f641bc8f37651407b9ff9a6 |
| Debugging exercise status | Complete for the assigned case-sensitive-name error |
| Next exercise | packing.py: multiplication, division, floor division, and remainder |

**Evidence and assessment.** The learner ran the deliberately broken starter, supplied the actual traceback, identified line 3, changed Coins to coins, and reran the corrected script. Their six corrected statements match debugging.py fetched at the pinned commit. The output evidence comes from the learner's terminal transcript; repository access does not establish access to their live terminal.

The first run printed 7 and then reported:

```text
Traceback (most recent call last):
  File "/workspaces/python-training/debugging.py", line 3, in <module>
    Coins += 3
    ^^^^^
NameError: name 'Coins' is not defined. Did you mean: 'coins'?
```

The learner's explanation was "changed Coins to coins on line 3". Accept this concise explanation: it identifies the specific name mismatch and location accurately.

Corrected program:

```python
coins = 7
print(coins)
coins += 3
print(coins)
coins -= 2
print(coins)
```

The supplied corrected prediction and runtime output are both 7, 10, 8. The initial prediction of 7 also matches the output produced before the broken program stopped.

| Skill | Evidence and status |
| --- | --- |
| Locate the reported error | Correctly identifies line 3 |
| Repair a case-sensitive name mismatch | Changes Coins to the previously assigned coins |
| Preserve intended behavior | Initial print and both updates remain; all three corrected values are right |
| Predict execution | Predictions agree with the supplied outputs before and after the repair |
| Naming and operator spacing | Consistent in the corrected statements |
| Go to Line shortcut | Introduced previously; actual use was not reported |
| Broader debugging fluency | Not established by this single guided example |

**Strengths and remaining practice.** The learner supplies useful diagnostic evidence, makes the targeted correction, explains it without unnecessary prose, and confirms the result. No unresolved mistake is demonstrated in this debugging exercise. Continue to revisit errors in varied later tasks; do not mark untested debugging skills as weaknesses. The earlier inventory omission and assignment-spacing correction remain resolved.

**Next lesson: arithmetic choices.** Teach the following meanings and examples before assigning packing.py. These are ordinary integer operands:

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| * | Multiplication | 19 * 2 | 38 |
| / | Division | 19 / 4 | 4.75 |
| // | Floor division | 19 // 4 | 4 |
| % | Division remainder | 19 % 4 | 3 |

For 19 marbles placed in bags of 4, // gives 4 full bags and % gives 3 marbles left over. Multiplication gives the number in those full bags: 4 * 4 is 16. These worked examples are separate from the learner's sticker exercise. See the [Python arithmetic introduction](https://docs.python.org/3.14/tutorial/introduction.html#numbers).

Introduce the type distinction: int represents integers; float can represent fractional values and also values such as 2.0. Dividing two integers with / produces a float, even when the division is exact: 8 / 4 gives 2.0. With two integer operands, // produces an int. Floor means rounding toward negative infinity: -7 // 3 gives -3. Do not teach floor division as simply chopping off fractional digits or as always producing int for every operand type. See [Python numeric operations](https://docs.python.org/3.14/library/stdtypes.html#numeric-types-int-float-complex).

Briefly establish that floats have limited precision and many decimal fractions are approximated. Detailed representation, rounding, and precision exercises remain for later. See [floating-point limitations](https://docs.python.org/3.14/tutorial/floatingpoint.html).

**Learner assignment.** Create packing.py in the repository root. Begin with stickers equal to 26 and pack_size equal to 4. Use variable-based calculations and all four newly taught operators to store these results:

1. full_packs: how many complete packs can be made.
2. leftover_stickers: how many stickers remain outside the full packs.
3. packed_stickers: how many stickers are inside the full packs, calculated by multiplication.
4. division_result: stickers divided by pack_size using ordinary division.

Print those four results in that order, each on its own line. Predict the output, save, and run `python3 packing.py`. Then change only the starting sticker count from 26 to 28, predict again, save, and rerun. Request the code, both predictions, and both actual outputs. The learner writes the solution; the tutor does not create or edit packing.py.

**Review criteria.** Check that results are calculated from the named values rather than written as fixed answers, that the intended operators are selected, and that each output requirement is present. Review meaningful lowercase names, underscores, and spacing around operators. The two cases exercise both leftover stickers and an exact multiple:

| Starting stickers | Expected full_packs | Expected leftover_stickers | Expected packed_stickers | Expected division_result |
| --- | --- | --- | --- | --- |
| 26 | 6 | 2 | 24 | 6.5 |
| 28 | 7 | 0 | 28 | 7.0 |

These are tutor review expectations, not observed learner results. Arithmetic practice is awaiting submission. Do not infer mastery or a weakness before reviewing the learner's work.

**Resume state.** The assignment/reassignment, integer update, and first debugging exercises are complete at their demonstrated scope. Multiplication, division, integer floor division, remainder, and the basic int/float distinction are being taught with this response. Follow successful packing practice with powers and operator precedence, then introduce input and conversions in small steps. Return later to signed remainders, additional numeric edge cases, float precision, and error handling.

**Course and repository continuity.** Add this record to the README Record/Purpose table in the same change. Narrow Stage/Coverage to the parts still to teach while keeping the curriculum open to additional topics. Preserve all older numbered records and the learner's exercise files. Continue accepting clear informal explanations. Synchronize tutor notes into the Codespace at a meaningful Git checkpoint; another commit or pull is not required merely to submit this exercise.
