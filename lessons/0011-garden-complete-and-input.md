# Record 0011: garden complete and reading numeric input

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Garden submission review and next lesson |
| Assigned garden lesson | [Record 0010](0010-packing-complete-and-powers.md) |
| Verified learner commit | [012b76c](https://github.com/DevilMedlar/python-training/commit/012b76cbc107b116008b2882c646a048ee7178d5) |
| Verified garden source | [garden.py at this commit](https://github.com/DevilMedlar/python-training/blob/012b76cbc107b116008b2882c646a048ee7178d5/garden.py) |
| Garden file blob | 4181bb0629778fd5b763bf58a4f479b72ca714f5 |
| Garden status | Complete for the assigned powers and grouping exercise |
| Next exercise | Update inventory.py to read the starting count with input() and int() |

**Evidence.** The learner's submitted garden.py matches the file fetched at the pinned repository commit. Their prediction and supplied terminal output are both 25, 49, 24. Execution evidence is from the learner's transcript; this review does not claim that the tutor ran the learner's Codespace.

```python
side_length = 5
extension = 2

original_area = side_length ** 2
expanded_area = (side_length + extension) ** 2
added_area = expanded_area - original_area
print(original_area)
print(expanded_area)
print(added_area)
```

| Requirement | Finding |
| --- | --- |
| Use side_length = 5 and extension = 2 | Correct |
| Square the original side length using ** | Correct: 25 |
| Add the extension before squaring, using one expression with parentheses and ** | Correct: 49 |
| Calculate the difference in areas | Correct: 24 |
| Print original_area, expanded_area, added_area in that order | Correct |
| Predict the three outputs | Matches the actual output |
| Naming, assignment spacing, and grouping | Clear and consistent; no correction required |

**Strengths and resolved state.** The learner applies the new power syntax, uses parentheses at the required place, calculates from variables, meets the requested sequence on the first garden submission, and supplies matching predictions and runtime evidence. No unresolved error is demonstrated in this exercise. Earlier packing corrections remain resolved.

The spacing inside the parenthesized addition is readable and consistent with the course's earlier examples. Record 0010's discussion of compact spacing was an optional refinement, not a requirement to rewrite this correct program. Completion is scoped to this exercise; signed and chained powers and broader precedence rules remain later material.

**Next lesson: input and conversion.** Teach that input(prompt) displays a question and reads a line, returning text of type str. Entering 7 produces the string "7". int() converts suitable integer text to an integer for arithmetic. Use this worked example:

```python
apples_text = input("How many apples? ")
apples = int(apples_text)
print(apples + 2)
```

After running the example, entering 7 without quotes and pressing Enter makes it print 9. Explain each line before assigning the learner's work. The first two lines can also be written as:

```python
apples = int(input("How many apples? "))
```

In this expression, input returns the text, int converts it, and the resulting integer is assigned. Accept either the separate or combined form in the learner's exercise. Sources: [input](https://docs.python.org/3.14/library/functions.html#input) and [int](https://docs.python.org/3.14/library/functions.html#int).

**Invalid input, introduced before the observation task.** Strings such as "seven" and "7.5" are not accepted directly by int() as integer text and cause ValueError. Explain that the latter example concerns a string, rather than int() applied to a numeric float. An unhandled exception stops the script, as previously learned. This lesson observes that failure; catching it is the next lesson. Source: [Python's conversion-error example](https://docs.python.org/3.14/tutorial/errors.html#handling-exceptions).

Do not teach a digits-only parsing rule: int() supports additional valid integer-text forms. Detailed parsing, other conversions, validation, and end-of-input behavior remain later topics.

**Learner assignment: update inventory.py.** The existing [inventory.py at the checked commit](https://github.com/DevilMedlar/python-training/blob/012b76cbc107b116008b2882c646a048ee7178d5/inventory.py) still has the fixed starting count, the +8 and -5 updates, and the final recount to 3. Its blob is aacb893f6aea18bd4e1211360b8609e3494f62a8. Ask the learner to revise it so it:

1. Prompts for a starting book count, reads it with input(), and converts it with int() into books.
2. Prints the starting count.
3. Adds 8 with += and prints the updated count.
4. Subtracts 5 with -= and prints the updated count.

Explicitly ask them to remove the old final books = 3 recount and its print; this version ends after the subtraction. Require a clear prompt, but do not impose exact wording or require a particular intermediate text-variable name.

Save and run `python3 inventory.py`. At the running program's question, enter the response without quotation marks and press Enter. Run once with 12 and again with 7, using the same saved code. Ask for predictions before each valid run. Run once more with twelve to observe the expected ValueError and capture the traceback. Request the revised code, both valid predictions and outputs, and the invalid-input traceback. Do not assign try/except before teaching it.

**Review expectations.**

| Entered response | Expected result |
| --- | --- |
| 12 | Numeric outputs 12, 20, 15 |
| 7 | Numeric outputs 7, 15, 10 |
| twelve | ValueError during int conversion; no numeric count outputs |

These are expected future results, not observed learner results. The input prompt itself is additional expected terminal text. The traceback line number depends on the learner's accepted code structure and should not be prescribed. Check that the same program handles both valid entries, that conversion precedes arithmetic, that += and -= are used as requested, and that the old recount is removed. The intentional invalid-input failure is not itself a learner mistake.

**Resume state.** Garden practice is complete. input(), str-to-int conversion, and recognizing ValueError from unsuitable integer text are introduced with this response; the interactive inventory assignment awaits submission. After successful practice, teach a specific try/except ValueError handler and the required indentation before assigning error handling. Then teach comparisons and conditions for meaningful input ranges, with repeat prompting after loops are introduced.

**README and workflow.** Add record 0011 and its purpose, remove the newly taught basic input coverage, and retain the remaining conversions, validation, and end-of-input topics. The curriculum remains open to other topics. Preserve older numbered records and learner programs; the learner performs the inventory edit. Keep Git checkpoints deliberate and let the learner bring tutor notes into the Codespace at a suitable later pull.
