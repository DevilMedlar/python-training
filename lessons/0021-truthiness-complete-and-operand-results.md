# Record 0021: truthiness complete and operand results

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Phase 1 truthiness assessment, record-style correction, and operand-result lesson |
| Previous record | [0020](0020-grouping-complete-and-truthiness.md) |
| Phase guide | [Root README](../README.md), Phase 1: Beginner (Foundations) |
| Verified repository commit | [48cb1d3](https://github.com/DevilMedlar/python-training/commit/48cb1d3904936cfc8f01b231936e5c0e4015b4af) |
| Verified source | [flirt_check.py at this commit](https://github.com/DevilMedlar/python-training/blob/48cb1d3904936cfc8f01b231936e5c0e4015b4af/flirt_check.py) |
| Source blob | 2dba8decf17800ba18a42d3f7197dc99ea6aa125 |
| Runtime evidence | Three learner-supplied Codespace runs |
| Truthiness assignment | Complete at the assigned scope |
| Corrections pending | None |
| New topics | and/or operand results, fallback values, basic type() inspection |
| New assignment | message_defaults.py; four value/type runs |
| Assignment status | Explained and assigned in chat; awaiting learner work |

**Evidence.** The submitted source matches the repository file at the pinned commit. The learner provided the three requested terminal runs. Source was verified against the commit tree; runtime evidence is the learner's transcript, not a tutor execution in their Codespace.

```python
message = input("Type your message here: ")
available_minutes = int(input("Available minutes: "))

print(bool(message), bool(available_minutes))

if message:
    print("Text entered")
else:
    print("No text entered")

if available_minutes:
    print("Some time available")
else:
    print("No time available")
```

| Message | Available minutes | Observed boolean line | Observed following lines |
| --- | --- | --- | --- |
| Empty | 0 | False False | No text entered; No time available |
| Text 0 | 30 | True True | Text entered; Some time available |
| Text False | 0 | True False | Text entered; No time available |

Semicolons separate distinct output lines. All three cases match the assignment.

**Assessment.** The learner preserves the raw message string, converts only available minutes to an integer, prints both explicit bool results in the requested order, and uses two independent direct if/else decisions. The strings 0 and False are correctly treated as nonempty; numeric zero is falsy. Code organization, variable names, spacing, indentation, and user-facing minute units are clear. No functional or style correction is required. This is successful guided practice of familiar-number and string truthiness; it does not establish mastery of later collection or custom-object behavior.

**Documentation style instruction.** The learner explicitly requested neutral technical writing throughout lessons/*.md, with conversational style confined to chat. Record teaching content, examples, requirements, source citations, evidence, assessments, and next steps without copying conversational performance or personal forms of address. This applies to the lesson index as well as numbered files.

To apply this instruction to existing records, conversational passages in 0019 and 0020 were rewritten as neutral technical prose. The changes preserve the technical content, assignment requirements, source code, outputs, citations, historical status, actual filenames, and record identities. This user-directed prose correction is a narrow exception to the usual append-only treatment of historical records. No exercise source is modified by the tutor.

**New lesson and assignment.** The following is the neutral technical record of the material explained and assigned in chat.

**Lesson: operand results from and/or.**

An operand is a value on which an operator acts. In x or y, x and y are operands. Python's and/or operators select an operand as the result; they do not necessarily create a boolean.

| Expression | Result |
| --- | --- |
| x or y | x when x is truthy; otherwise y |
| x and y | x when x is falsy; otherwise y |

The right operand is evaluated only when needed. not always produces a boolean. Earlier and/or expressions combined comparison results, which were already boolean operands.
Sources: [Python boolean operations](https://docs.python.org/3.14/library/stdtypes.html#boolean-operations-and-or-not) and [Python expression reference](https://docs.python.org/3.14/reference/expressions.html#boolean-operations).

Worked example in a separate scenario:

```python
nickname = ""
visits = 2

display_name = nickname or "Guest"
visit_label = visits and "Returning visitor"

print(display_name)
print(visit_label)
```

Output:

```text
Guest
Returning visitor
```

The empty nickname is falsy, so or selects the fallback string Guest. The nonzero visits value is truthy, so and selects Returning visitor. If visits is changed to 0, visit_label becomes the integer 0. These operators do not alter their input variables.

Using or for a default is appropriate when every falsy left value should select the fallback. In particular, 0 or 30 gives 30; use an explicit condition if zero must be preserved.

**Inspecting basic value types.**

type(value) reports the value's type:

```python
print(type("0"))
print(type(0))
```

Output:

```text
<class 'str'>
<class 'int'>
```

str identifies text and int identifies an integer. These are Python's displayed type labels. Plain print displays both the string "0" and the integer 0 as 0, so type() makes the distinction visible. This is basic data-type inspection; class definitions and advanced introspection are not part of this lesson.
Source: [Python type](https://docs.python.org/3.14/library/functions.html#type).

To inspect a value and its type together, a call such as print(display_name, type(display_name)) prints both on one line.

**Assignment: message_defaults.py.**

This is a focused operator experiment. Reuse the familiar raw-message and integer-minutes inputs:

1. Read message with input().
2. Read available_minutes with int(input(...)). Use nonnegative integers for this exercise.
3. Assign display_message using or: use the entered message when nonempty; otherwise use the exact fallback string "No message supplied".
4. Assign timed_message using and, with available_minutes on its left and display_message on its right.
5. Print display_message and its type together on one line.
6. Print timed_message and its type together on the next line.

Preserve the raw message. Produce these results with the assigned operators rather than replacing them with if/else. No additional validation, loops, or functions are required. The timed_message value intentionally demonstrates the different operand types: integer zero or a string. It is not presented as the preferred way to display fixed user-facing status messages; an ordinary if/else remains clearer for that purpose.

Run:

```bash
python3 message_defaults.py
```

| Message entered | Minutes | display_message value/type | timed_message value/type |
| --- | --- | --- | --- |
| Press Enter without typing | 0 | "No message supplied", str | 0, int |
| Press Enter without typing | 30 | "No message supplied", str | "No message supplied", str |
| 0 | 30 | "0", str | "0", str |
| False | 0 | "False", str | 0, int |

Quotation marks in the table identify strings; do not type them at the prompt. The printed type labels are <class 'str'> and <class 'int'>, as demonstrated above. Submit code and the four actual runs without predictions.


**Review criteria and uncertainty.** Check the precise left/right rules, fallback only on a falsy raw message, numeric zero versus positive integer behavior for the left operand of and, unchanged string values, and both printed types. Do not replace the exercise with bool conversions: the point is to inspect the selected values themselves. The four cases cover both paths of each operator and the text-versus-number zero distinction. Empty-string display and spaces-only normalization are not additional requirements.

type() is introduced before the assignment because it has not appeared in earlier recorded lessons. It is used only in its one-argument form to identify the already familiar str and int types. Do not introduce the three-argument form, class definitions, subclass checks, or other advanced introspection.

**Topics introduced versus demonstrated.** Truthiness practice is now complete at this scope. Operand selection, a string fallback, the numeric-zero default hazard, and basic type() output are explained here; the new learner implementation is pending. Practical short-circuit guards that prevent invalid operations, longer fallback chains, whitespace normalization, and later-type truthiness remain future material. not with grouped conditions and mixed/exclusive bounds remain useful later variations.

**Sources.**

- [Python boolean operations](https://docs.python.org/3.14/library/stdtypes.html#boolean-operations-and-or-not).
- [Python expression reference](https://docs.python.org/3.14/reference/expressions.html#boolean-operations).
- [Python type](https://docs.python.org/3.14/library/functions.html#type).

All were checked in this turn. The last confirmed learner interpreter is Python 3.14.2; sources describe the current 3.14 series.

**Resume state.** Review message_defaults.py and the four actual runs. Once successful, teach practical short-circuit guards through familiar numeric operations, or consult the remaining curriculum for the next appropriate Phase 1 topic. Do not require predictions, repeated old-case runs, or routine Git synchronization. Keep future lesson files neutral while teaching fully in chat.

**Record maintenance.** This record supersedes the pending truthiness-assignment status in 0020. Add 0021 to the Foundation index, replace the current checkpoint, and retain practical short-circuit guards while removing the introduced non-boolean and/or operand-results topic from remaining coverage. Maintain neutral historical records and learner-owned source. The next record is 0022.
