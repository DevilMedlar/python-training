# Record 0003: variables exercise review

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Submission review and correction assignment |
| Previous lesson | [Record 0002](0002-variables-and-assignment.md) |
| Evidence | Learner's pasted variables.py, predicted output, and terminal output |
| Repository state inspected | main at 8ae8bf3a23aa366b5b4b3c963ca3c2648d6068f6 before this record was added |
| Overall status | Behavior and prediction correct; assignment spacing and learner explanation pending |

This entry updates the current assessment without changing record 0002. The source for this review is the learner's pasted work. variables.py was not present on GitHub main when checked; no claim is made to have read the live Codespace file.

**Submitted code, preserved as received.**

```python
pencils=6
pens=4
item_count=pencils + pens
print(item_count)
pencils=9
print(pencils)
print(item_count)
item_count=pencils + pens
print(item_count)
```

The learner supplied the prediction 10, 9, 10, 13. Running python3 variables.py produced the same four lines:

```text
10
9
10
13
```

**Assessment.**

| Skill or requirement | Finding |
| --- | --- |
| Assignment before use | Correct |
| Reassignment and execution order | Correct in the submitted program |
| Calculating with variable names | Correct; item_count uses pencils and pens |
| Four output lines | Correct order and values |
| Prediction | Matches the actual result |
| Naming | Meaningful lowercase names and correct item_count spelling |
| Spacing around + | Correct in both additions |
| Spacing around assignment = | Missing in all five assignment statements; correction required by the course style standard |
| Explanation in the learner's own words | Not supplied; understanding has not yet been assessed through explanation |

**Demonstrated strengths.** The learner follows the sequence of assignments, uses meaningful names, calculates from variables, and predicts the output correctly in this exercise. There is no runtime or logic error in the submitted code.

**Specific follow-up.** The taught assignment-spacing convention was not applied. Treat this as a concrete style issue to correct and revisit in later exercises. The missing explanation is an outstanding submission item, not evidence of a conceptual misunderstanding. Do not infer broader weaknesses from this one exercise.

For the simple assignments in this lesson, PEP 8 calls for one space on either side of the assignment operator. Examples of the intended formatting are:

```python
pencils = 6
item_count = pencils + pens
```

The existing compact assignments are valid Python. The correction makes them follow the course's readability convention and does not change their values. This rule concerns assignment statements; other uses of an equals sign, such as keyword arguments and some parameter defaults, are covered in later lessons. Source: [PEP 8 operator spacing](https://peps.python.org/pep-0008/#other-recommendations).

**Next learner action.**

1. Add the appropriate spaces around = in all five assignment statements in variables.py.
2. Save and rerun the script to check the corrected version; the expected behavior remains the same.
3. Submit the corrected code and a short explanation answering: why is the third printed value still 10 after pencils is reassigned to 9, and what makes the final printed value 13?

Do not supply a rewritten full solution on the learner's behalf. The small formatting examples and earlier worked example provide the needed teaching.

**Resume state and next decision.**

The variables lesson is awaiting this revision and explanation. If both are satisfactory, continue with variable updates, naming, and basic debugging, returning to spacing during later practice. If the explanation reveals a misunderstanding, use a small different example to teach the specific gap. Add the next review in a new numbered record.

The learner has not shown a pull of the earlier lesson records in this submission. That does not prevent reviewing the pasted program. Keep Git checkpoints deliberate: the learner can pull notes when needed, and at the next code checkpoint the tutor should inspect branch state and account for documentation commits on GitHub before guiding the learner's new commit/push sequence.

The new record is committed on GitHub; an existing Codespace checkout will receive it through the previously taught git pull --ff-only command when a fast-forward is possible. Do not require a new pull or commit just to submit this small code correction.
