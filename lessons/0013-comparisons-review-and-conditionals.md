# Record 0013: comparisons review and first conditionals

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Learner preferences, comparison review, and Phase 1 lesson |
| Previous lesson | [Record 0012](0012-input-complete-and-comparisons.md) |
| Phase guide | [Root README](../README.md), Phase 1: Beginner (Foundations) |
| Verified learner commit | [c89b85b](https://github.com/DevilMedlar/python-training/commit/c89b85b399476244c1d0251539a1ac6f5e683a60) |
| Verified source | [comparisons.py at this commit](https://github.com/DevilMedlar/python-training/blob/c89b85b399476244c1d0251539a1ac6f5e683a60/comparisons.py) |
| File blob | 471ecdff88ea8c07df89411d4fe3a04d9e5df352 |
| Submission evidence | Learner's pasted comparisons.py and three Codespace terminal runs |
| Comparison status | Outputs correct for the submitted expressions; initial practice sufficient to progress, with operand direction carried forward |
| New lesson | if/elif/else, first matching branch, and block indentation |
| New assignment | book_target.py; code and actual runs for 18, 20, and 23 |
| New assignment status | Issued in chat; awaiting learner evidence |

**Learner clarifications and teaching agreement.** The root README is a skeleton outline of the course. lessons/README.md tracks more detailed coverage and links to completed teaching and practice. Numbered records retain the detailed history already being recorded. These files are for the tutor to read and maintain, so teaching follows the actual progress and phase order. The learner expects the lesson and work in chat; they only expect to inspect the records when something appears off, such as repetition or premature advanced material. Do not substitute a link to a record for the actual teaching.

The learner explicitly asks to stop requesting predictions on every challenge, especially on multiple line-by-line prints, unless absolutely necessary for the lesson. Default to code and actual runs. Only request a focused prediction when essential to teach or diagnose a specific concept, with a reason. This supersedes the blanket prediction request in 0012 and any older guidance to routinely encourage or grade predictions. Do not rewrite those historical records.

**Evidence and review.** The learner supplied:

```python
target = 20

books = int(input("How many books do you have? "))
print(target == books)
print(target != books)
print(target < books)
print(target <= books)
print(target > books)
print(target >= books)
```

All observed output sequences below match those expressions. The columns follow the operator order in the submitted source; target is on the left and books is on the right.

| Entered books | target == books | target != books | target < books | target <= books | target > books | target >= books |
| --- | --- | --- | --- | --- | --- | --- |
| 19 | False | True | False | False | True | True |
| 20 | True | False | False | True | False | True |
| 21 | False | True | True | True | False | False |

The learner also included matching output blocks outside the terminal transcripts. Their presence is not grounds for another prediction requirement. The learner pushed comparisons.py while the tutor was preparing this review. The source at the pinned learner commit above was fetched and exactly matches the pasted code. Runtime evidence remains the learner's terminal transcripts; do not claim the tutor ran this code in the learner's Codespace. The documentation change is based on that latest learner commit to preserve the new Python file. Pasted code and run evidence can also be accepted before a push at other checkpoints.

**Demonstrated strengths.** Correctly combines input and integer conversion, uses both variables in all six comparisons, uses each operator once in the requested operator order, preserves appropriate spaces and readable names, and supplies valid runs below, at, and above the target. All observed boolean results are correct for the code. The equality boundary is demonstrated in the runs. This is successful initial practice, not evidence of broad mastery.

**Difference from the original task and feedback.** Record 0012 asked for books on the left. The submission puts target on the left. That is valid Python, but the four order comparisons ask a different question. For books equal to 19, target < books asks whether 20 < 19 and is False; books < target asks whether 19 < 20 and is True. For these integers, swapping the operands preserves == and !=; preserving the meaning of an inequality while swapping operands requires reversing its direction, for example target > books and books < target.

Explain this briefly without labeling the correct outputs as runtime mistakes. The learner's reason for choosing this orientation is unknown; do not invent a conceptual weakness. Do not require another three runs of the same six-print program. Carry the intended meaning of each comparison into the next task and assess it there. Source: [Python comparisons](https://docs.python.org/3.14/library/stdtypes.html#comparisons).

**New Phase 1 lesson: selecting a branch.** A condition is an expression used to decide whether a block should run. Comparisons already learned supply boolean conditions. In an if/elif/else chain, Python considers conditions in order and runs the first matching block. Later branches are skipped. The else block has no condition and handles the remaining case when no earlier condition matched.

The worked example for the chat is:

```python
score = 7

if score >= 10:
    print("Goal reached.")
elif score >= 5:
    print("Keep going.")
    print(10 - score)
else:
    print("Getting started.")

print("Check complete.")
```

Output:

```text
Keep going.
3
Check complete.
```

Explain that 7 >= 10 is False, then 7 >= 5 is True, so both lines in that elif block run. The last print is outside the chain and runs afterward. With a score of 12, the first block runs and the elif is skipped even though 12 >= 5 would also be True. This shows why the order of overlapping conditions matters. An if can stand alone, have an else, or have one or more elif clauses; elif and else are optional. Without an else and without a matching condition, no branch body runs.

Sources: [Python tutorial: if statements](https://docs.python.org/3.14/tutorial/controlflow.html#if-statements) and [Python language reference: if](https://docs.python.org/3.14/reference/compound_stmts.html#if).

**Syntax and style.** Put a colon at the end of each if, elif, and else header. Align related headers. Indent the lines belonging to each branch consistently. Python uses indentation to group these multiline blocks; four spaces per level is the PEP 8 convention, not a claim that the language only accepts four. Use spaces consistently. A block can contain multiple statements, as the two print calls above demonstrate. Returning to the header's indentation ends that block. Source: [PEP 8 indentation](https://peps.python.org/pep-0008/#indentation), with block grammar in the language reference above.

**Editor shortcut taught with the block.** In the Windows VS Code editor, with editor focus, Ctrl+] indents the current or selected lines and Ctrl+[ outdents them. These use the editor's configured indentation size. Four spaces is the course's Python indentation convention. If a browser or customized binding intercepts a shortcut, use the Command Palette to find Indent Line or Outdent Line. Shortcut use has been explained, not observed. Sources: [VS Code Windows shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf) and [keyboard shortcuts documentation](https://code.visualstudio.com/docs/configure/keybindings).

**Learner assignment: book_target.py.** Create a new Python file. Set target to 20 and obtain books through the familiar int(input(...)) pattern. Write one if/elif/else chain that checks the book count against the target. Use books on the left of the written comparison conditions to reinforce the wording of the question.

| Case | Required behavior |
| --- | --- |
| Books below target | Print "Books still needed:" and then calculate and print how many more books are needed on the next line |
| Books equal to target | Print "Target reached." |
| Books above target | Print "Extra books:" and then calculate and print how many books exceed the target on the next line |

Keep both print statements for a below/above result in their selected branch. Calculate the differences from the variables rather than using a fixed answer. Existing integer arithmetic and input are prerequisites; conditional execution and indentation are the new work. The tutor gives the worked example and behavioral requirements, not the finished book_target.py source.

Save and run:

```bash
python3 book_target.py
```

Run the same saved program three times, entering 18, 20, and 23. These exercise the three different branches and avoid reliance on a fixed difference of one. Submit the code and actual outputs. Do not request predictions. Do not add an error-handling assignment: formal try/except/else/finally remains Phase 2. Input range validation is still future Phase 1 work.

**Review expectations, not learner results.** Apart from the input prompt, 18 should produce "Books still needed:" and 2; 20 should produce "Target reached."; 23 should produce "Extra books:" and 3. Exactly one branch should supply the result each run. Check comparison meaning, branch choice, correct subtraction direction, use of variables, colons, indentation of both branch statements, and normal style. A finished implementation or successful run has not yet been supplied.

**Resume state.** Earlier work remains complete at its demonstrated scope. Initial six-operator comparison practice is accepted after explaining the task's operand-order difference; observe whether the learner applies comparisons correctly in book_target.py. New conditional syntax is introduced, and its first exercise is pending. After reviewing that submission, continue with related Phase 1 boolean logic and practical conditions before loops, while consulting remaining coverage and expanding it as appropriate. Nested conditionals and independent if statements remain to teach. No advanced phase is completed by a preview.

**Record maintenance.** This new record preserves 0001-0012 unchanged. Update the lessons README with this file's Record/Purpose row, the new learner preferences, and current checkpoint. Remove introduced basic if/elif/else and block indentation from remaining coverage, retaining untaught conditional topics. Keep the root README as the phase skeleton and leave learner Python files to the learner. The next new record number is 0014.
