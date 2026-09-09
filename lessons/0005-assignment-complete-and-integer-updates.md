# Record 0005: assignment complete and integer updates

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Completion assessment, preference clarification, and next lesson |
| Previous record | [Record 0004](0004-spacing-cost-and-readability.md) |
| Assignment/reassignment lesson | Complete for this exercise: code, prediction, formatting correction, and explanation accepted |
| New lesson | Integer updates with =, +=, and -=; assigned with the accompanying response |
| New exercise file | inventory.py, to be written by the learner |
| Repository inspected before this entry | main at 8c0f9e36912c6ae62e98070bef5a622161414826 |

**Evidence and completion decision.**

The learner explained that printing item_count uses its most recently assigned value and does not recalculate the total until a later assignment runs. The meaning is sufficiently clear and technically correct in the context of the submitted program. Combined with the correct prediction and corrected code recorded in entries 0003 and 0004, this completes the introductory assignment/reassignment exercise.

Accept the explanation as supplied. Do not require it to be rewritten in textbook language. This checkpoint demonstrates understanding in this small example; it does not establish mastery across all future variable, aliasing, or collection problems.

**Latest learner preference.**

The learner explicitly asks that informal explanations not be nitpicked for professional presentation: their goal is learning Python, not training to teach it. Assess explanations for actual understanding and correct genuine misconceptions when present. Continue reviewing code correctness and the established code style. Do not grade grammar, polish, or casual wording when the concept is clear. Brief informal explanations remain suitable for useful conceptual checks.

**Strengths and follow-up.**

- Correctly predicts the effect of assignment order and reassignment in the completed exercise.
- Applies the requested formatting correction.
- Gives an understandable account of stored results versus a later recalculation.
- Notices the real storage cost of source characters and asks for the purpose of conventions.
- Revisit operator-spacing consistency during new code practice; the last correction is resolved.
- No remaining conceptual error has been demonstrated in this completed exercise.

**Supplemental unit discussion.**

The learner notes that spaces can add up to megabytes over a sufficiently large project. Ordinary ASCII spaces take one byte each in UTF-8, so that possible aggregate source cost is real. The course keeps readable, consistent authored source while treating resource optimization as a question of actual constraints and measurements.

The standard distinction for the two supplied quantities is:

| Unit | Bytes |
| --- | ---: |
| MB (megabyte) | 1,000,000 |
| MiB (mebibyte) | 1,048,576 |

Use the explicit unit names rather than a blanket claim that all operating systems use one convention. Source: [NIST binary prefixes and comparisons](https://physics.nist.gov/cuu/Units/binary.html). This factual distinction does not reopen the accepted variable explanation or require a further written response about style.

**Next lesson: update using the current value.**

Read this worked example:

```python
coins = 5
coins = coins + 3
print(coins)
```

The output is 8. On the second line, Python reads the current coins value, calculates 5 + 3, then assigns the resulting 8 to coins.

For this integer variable, replace the second line with coins += 3 to get the same resulting value. The += form combines addition and assignment. Subtraction uses -, and -= combines subtraction with assignment.

| Statement for an integer variable | Effect |
| --- | --- |
| coins = 3 | Set the current value to 3 |
| coins += 3 | Add 3 to the current value |
| coins -= 3 | Subtract 3 from the current value |

An update such as += or -= requires an existing value for the name. Keep the two operator characters together, with one space on either side of the complete operator, as in coins += 3.

These comparisons are for the plain integer variables in this lesson. When mutable collections and richer assignment targets are introduced, revisit augmented assignment instead of claiming it is universally identical to the longer form.

Sources: [Python augmented assignment](https://docs.python.org/3.14/reference/simple_stmts.html#augmented-assignment-statements), [Python arithmetic introduction](https://docs.python.org/3.14/tutorial/introduction.html#numbers), and [PEP 8 operator spacing](https://peps.python.org/pep-0008/#other-recommendations).

**Learner exercise.**

Create inventory.py in the repository root and write the following behavior yourself:

1. Start books at 12 and print the count.
2. A delivery adds 8 books: update books using += and print the count.
3. Five books are lent out: update books using -= and print the count.
4. A later recount gives an actual total of 3: set books directly with = and print the count.

Predict the four output lines before running. Save and execute:

```bash
python3 inventory.py
```

Submit the code, predicted output, and terminal output. No formal prose explanation is required for this practice. The tutor provides the different worked coins example, not a full solution to inventory.py.

**Resume state.**

| Item | Status |
| --- | --- |
| Initial print and Git checkpoint | Complete with the previously recorded evidence |
| Variables assignment/reassignment exercise | Complete for the demonstrated scope |
| Integer self-updates and += / -= | Introduced and assigned; awaiting learner work |
| inventory.py | Not yet submitted or assessed |
| Next after successful practice | Teach reading a traceback and diagnose a simple case-sensitive-name error, then expand arithmetic and input in small steps |

Review the new code for initialization before updates, the distinction between changing a count and replacing it, correct execution order, four outputs, names, and spacing. If the learner's code or prediction reveals a gap, teach that specific point and assign a small variation. Keep future reviews append-only.

Continue reviewing pasted work between meaningful Git checkpoints. Tutor notes added on GitHub can be brought into the Codespace with the previously taught pull workflow when appropriate; a Git operation is not required for every small exercise.
