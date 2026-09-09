# Record 0012: input complete and handling conversion errors

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Interactive inventory review and next lesson |
| Assigned input lesson | [Record 0011](0011-garden-complete-and-input.md) |
| Verified learner commit | [905088f](https://github.com/DevilMedlar/python-training/commit/905088fa74e22400faada2feb31b5de08881d379) |
| Verified source | [inventory.py at this commit](https://github.com/DevilMedlar/python-training/blob/905088fa74e22400faada2feb31b5de08881d379/inventory.py) |
| File blob | 9a27abf08c84b8206a30c476acf386d2fe36c155 |
| Input exercise status | Implementation and all three requested runs complete |
| Next practice | Handle ValueError with try/except/else and correctly indented blocks |

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

Earlier exercises and their resolved corrections remain complete at the demonstrated scope. Error handling and indentation are new teaching targets, not established weaknesses.

**Next lesson: a specific handler and success-only work.** Teach this worked example before assigning the learner's revision:

```python
try:
    apples = int(input("How many apples? "))
except ValueError:
    print("Please run again and enter a whole number.")
else:
    print(apples + 2)
```

try contains the input/conversion operation. except ValueError handles that exception from the try block. else runs when the try block finishes normally. Here, entering 7 produces 9; entering seven produces the message and the script finishes. An exception from else is not caught by this try's preceding handler. Keep the conversion scope narrow and place the arithmetic in else. Source: [Python exception handling](https://docs.python.org/3.14/tutorial/errors.html#handling-exceptions).

Explain that the earlier failed conversion did not assign books in that fresh run. The success-only calculation block prevents using a value that conversion never produced. This else belongs to try; if/else will be taught separately.

**First indented blocks.** A block is a group of statements belonging together. Python uses indentation to mark these groups. In this pattern, try:, except ValueError:, and else: are aligned; each header ends with a colon. Indent each body by four spaces, following the course's PEP 8 style. Keep related body statements at the same level. Source: [PEP 8 indentation](https://peps.python.org/pep-0008/#indentation).

**Editor shortcut.** In the focused VS Code editor on Windows/Linux, Ctrl+] indents the current or selected lines and Ctrl+[ outdents them. Use the editor's indentation commands to help move the existing calculation lines into the else block, checking that the body uses four spaces. The shortcut is introduced, not claimed as demonstrated. Source: [VS Code default keybindings](https://code.visualstudio.com/docs/reference/default-keybindings).

**Learner assignment: revise inventory.py.**

1. Put the input and integer conversion in try.
2. Add except ValueError with one clear message asking the person to rerun the program and enter a whole number. Exact wording is the learner's choice.
3. Put the initial count print, +8 update and print, and -5 update and print inside else. Preserve that order and the existing += and -= operations.
4. Use aligned colon-ended headers and four spaces for each body.

Ask the learner to save and run `python3 inventory.py` separately for 12, twelve, and 7.5. Request revised code and the complete output for all three runs. Explain the expected behavior before these tests:

| Entered response | Expected behavior after the revision |
| --- | --- |
| 12 | Three numeric outputs: 12, 20, 15 |
| twelve | One clear error message; no numeric count outputs or traceback |
| 7.5 | One clear error message; no numeric count outputs or traceback |

The prompt remains expected terminal text in every case. These are future review expectations, not observed learner results. Each run ends after its result or message; repeat prompting will be taught with loops. Do not require a loop, negative-value check, a full-program rewrite, or an additional Git operation for this assignment.

**Review criteria and next decision.** Verify that only input/conversion is protected by the specific ValueError handler, that all five existing calculation/print statements are in else, and that both invalid inputs finish without attempting to use books. Evaluate syntax and indentation as well as output. If a gap appears, explain that specific point with a small example before assigning a correction.

**Resume state.** Basic input and integer-text conversion are complete for the assigned cases. try/except ValueError/else, colon-ended headers, four-space blocks, and indentation shortcuts are introduced with this response; the revised handler is awaiting learner evidence. After successful practice, teach comparisons and if/else for domain checks such as rejecting negative book counts. Repeated prompting follows when loops are taught. Additional exception types, raising, finally, and cleanup remain later topics.

**README and workflow.** Add this record with its purpose. Narrow the remaining input validation and exception coverage, and remove the newly taught exception else clause from Programs and dependencies while retaining finally/cleanup. Keep the coverage outline non-exhaustive, earlier numbered records unchanged, and learner programs under the learner's control. Bring tutor notes into the Codespace at a meaningful later Git checkpoint.
