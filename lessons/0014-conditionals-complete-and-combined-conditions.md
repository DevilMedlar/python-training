# Record 0014: first conditionals complete and combined conditions

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Conditional exercise review and Phase 1 boolean logic lesson |
| Previous lesson | [Record 0013](0013-comparisons-review-and-conditionals.md) |
| Phase guide | [Root README](../README.md), Phase 1: Beginner (Foundations) |
| Verified learner commit | [69f318c](https://github.com/DevilMedlar/python-training/commit/69f318c30e8aa2021269cd214b93a008fa434062) |
| Verified source | [book_target.py at this commit](https://github.com/DevilMedlar/python-training/blob/69f318c30e8aa2021269cd214b93a008fa434062/book_target.py) |
| File blob | 6484a7304a7af5d95f6fe83dd058e6d2dabdcc45 |
| Runtime evidence | Learner's pasted Codespace runs for 18, 20, and 23 |
| Conditional practice status | Complete at the demonstrated scope; single-line output variation accepted |
| Current lesson | and/or with comparison results; basic short-circuit behavior |
| New assignment | reading_goals.py, with five actual input pairs |
| New assignment status | Taught and issued in chat; awaiting learner work |

**Evidence.** The source fetched at the pinned learner commit exactly matches the submitted code:

```python
target = 20
books = int(input("How many books do you have? "))
if books < target:
    print("Books still needed:", target - books)
elif books == target:
    print("Target reached.")
else:
    print("Extra books:", books - target)
```

| Entered books | Learner's observed output after the prompt | Assessment |
| --- | --- | --- |
| 18 | Books still needed: 2 | Correct below-target branch and subtraction |
| 20 | Target reached. | Correct equality branch |
| 23 | Extra books: 3 | Correct remaining branch and subtraction |

The tutor verified repository source; runtime evidence is the learner's terminal transcript. Do not claim a tutor execution in the learner's Codespace. All three requested runs were supplied. No prediction request or grading is appropriate.

**Demonstrated strengths.** The learner implements the if/elif/else chain with correct colons and four-space branch indentation. They use books on the left of comparisons and correctly connect the comparison direction with the intended question, addressing the operand-order point carried from 0013. The program calculates the missing or extra quantity from variables, uses the equality branch at the target, and supplies all requested branch cases. Integer input, names, operator spacing, and multi-value print syntax are correct.

**Output layout and accepted variation.** Record 0013 requested the message and quantity on separate lines. The learner prints both in one call on one line. The tutor accepts this clear presentation for this exercise; do not call it an exact match to the original output layout or force a rerun just to change the line breaks. Explain that print can take multiple comma-separated values and inserts a space between them by default, so the learner's call displays the label and calculated integer together. Source: [Python print](https://docs.python.org/3.14/library/functions.html#print). Custom sep/end controls are not taught by this brief explanation.

There are no functional errors identified for the requested inputs. Each branch contains one statement, so multiple statements inside a selected branch remain explained but not independently demonstrated. Likewise, this disjoint-condition task does not establish behavior with overlapping conditions. Revisit multiple-statement blocks naturally in a later task with useful state changes or loops; the new combined-condition assignment will reinforce branch order. This is successful first practice, not a claim of comprehensive control-flow mastery.

**New lesson: combine comparisons with and and or.** Remain in Phase 1. Teach the material directly in chat before assigning work. The operands in this lesson are boolean results of numeric comparisons.

- and gives True when both boolean conditions are True.
- or gives True when at least one boolean condition is True, including when both are True.

| First condition | Second condition | and result | or result |
| --- | --- | --- | --- |
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

Source: [Python boolean operations](https://docs.python.org/3.14/library/stdtypes.html#boolean-operations-and-or-not).

Precision for future teaching: and/or return a selected operand. In today's examples those operands are boolean comparison results. Do not make a blanket statement that and/or always return bool for every input type. General truthiness, non-boolean operands, mixed-operator precedence, and not remain to teach. Do not introduce collections, bitwise operators, or exception handling through this lesson.

**Worked example for chat.**

```python
pencils = 6
pens = 2

if pencils >= 5 and pens >= 5:
    print("Both supplies are ready.")
elif pencils >= 5 or pens >= 5:
    print("One supply is ready.")
else:
    print("Neither supply is ready.")
```

The output is:

```text
One supply is ready.
```

The first condition combines True and False, which is False. The next condition is True because there are enough pencils. The elif block prints its message. Explain that if both counts reached at least five, the first branch would handle that case. The or operation itself includes the both-true case; it means exactly one ready supply here only because the earlier branch already handled both.

Each side must express the intended comparison: pencils >= 5 and pens >= 5. Do not abbreviate the second comparison to just a bare number or assume the first comparison operator carries across and/or. Conditions can still be placed directly after if or elif, using the same colons and indentation already practiced.

**Evaluation behavior.** Python evaluates the left operand first and checks the right only if it is needed: and skips the right when the left is False; or skips it when the left is True. This is short-circuiting. In the worked example's elif, the pencils comparison is True, so the pens comparison is skipped. This is an explanation of evaluation, not a new tracing assignment. Source: [Python expression reference](https://docs.python.org/3.14/reference/expressions.html#boolean-operations).

**Learner assignment: reading_goals.py.** Ask for the number of completed books and the number of days spent reading, using two separate int(input(...)) calls. Use descriptive names such as books and reading_days; equivalent clear names are accepted.

For this exercise the goals are at least three completed books and at least five reading days. Use one if/elif/else chain:

1. Check both goals together with and. If both are reached, print "Both goals reached".
2. Otherwise, check whether either goal is reached with or. If so, print "One goal reached".
3. Otherwise, print "Neither goal reached".

Calculate the conditions from the user's inputs. Reaching a goal includes exceeding it. The tutor supplies the behavioral requirements and the separate supplies example, not the finished reading_goals.py code. Use known integer comparisons, input, and conditional blocks; no error-handling or looping requirements are added.

Save and run:

```bash
python3 reading_goals.py
```

Use the same saved program for these input pairs. The expected results are provided for checking, not requested as predictions.

| Completed books | Reading days | Expected result, apart from prompts |
| --- | --- | --- |
| 3 | 5 | Both goals reached |
| 3 | 4 | One goal reached |
| 2 | 5 | One goal reached |
| 2 | 4 | Neither goal reached |
| 4 | 6 | Both goals reached |

The first four cases cover every combination of goal completion; the final case confirms that exceeding the thresholds still qualifies. Ask for code and actual runs only. Keep one result message per run; the input prompts are expected additional text.

**Review criteria and uncertainty.** Look for two real comparisons joined by each operator, correct minimum-threshold comparisons, inclusive or understood within the first-match chain, correct branch order, and the two independent inputs. No combined-condition implementation or run has yet been submitted. Do not label untested boolean logic or shortcuts as a weakness. Do not claim mastery from one small program.

**Resume state.** Initial comparison and conditional practice are complete at the recorded scope. Operand direction now has correct practical evidence. Multi-value printing has been used successfully and its default spacing explained. The current exercise is reading_goals.py. After reviewing it, teach logical not with a named boolean condition and a focused application, then the remaining related Phase 1 topics. Keep truthiness and non-boolean and/or behavior distinct from today's boolean examples. Continue consulting the detailed remaining coverage; Phase 2 try/except/else/finally stays deferred. The learner reads the lesson in chat and need not read or synchronize these tutor notes before practicing.

**Record maintenance.** Preserve 0001-0013 unchanged. Add 0014 to lessons/README.md with a Record/Purpose entry, update its current checkpoint, and replace the broad remaining logical-operators item with its untaught parts. The root README remains the phase skeleton. Do not modify learner Python files. The next new numbered record is 0015. Keep the standing rule: code and actual runs are the default submission; predictions only when essential to a specific lesson.
