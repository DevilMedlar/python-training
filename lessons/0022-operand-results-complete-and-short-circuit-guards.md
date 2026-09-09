# Record 0022: operand results complete and short-circuit guards

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Phase 1 operand-result assessment and practical short-circuit lesson |
| Previous record | [0021](0021-truthiness-complete-and-operand-results.md) |
| Phase guide | [Root README](../README.md), Phase 1: Beginner (Foundations) |
| Verified repository commit | [cd29393](https://github.com/DevilMedlar/python-training/commit/cd29393efe5cd8688723f3a5491b4aac4fc6ea8a) |
| Verified source | [message_defaults.py at this commit](https://github.com/DevilMedlar/python-training/blob/cd29393efe5cd8688723f3a5491b4aac4fc6ea8a/message_defaults.py) |
| Source blob | 53d3e25616db09b6010a94135e2c43ab82e85957 |
| Runtime evidence | Four learner-supplied Codespace runs |
| Operand-result assignment | Complete at the assigned scope |
| Corrections pending | No functional correction; optional prompt spelling cleanup |
| New topic | Using an ordered condition to guard division or remainder |
| New assignment | equal_shares.py; three focused runs |
| Assignment status | Explained and assigned in chat; awaiting learner work |

**Evidence and assessment.** The submitted code matches the repository file at the pinned commit. The file blob also matches the commit tree. Runtime evidence is the learner's transcript; the tutor did not execute the program in the learner's Codespace.

```python
message = input("Type messaga: ")
available_minutes = int(input("Minutes: "))

display_message = message or "No message supplied"
timed_message = available_minutes and display_message

print(display_message, type(display_message))
print(timed_message, type(timed_message))
```

| Message entered | Minutes | Observed display_message value/type | Observed timed_message value/type |
| --- | --- | --- | --- |
| Empty | 0 | "No message supplied", str | 0, int |
| Empty | 30 | "No message supplied", str | "No message supplied", str |
| Text 0 | 30 | "0", str | "0", str |
| Text False | 0 | "False", str | 0, int |

All four runs match the requirements. The learner uses the requested operators, preserves the raw message, converts only the minutes input to an integer, and prints each selected value with its original type. Nonempty strings remain strings, even when their contents are 0 or False. The zero-minutes cases correctly produce integer zero for timed_message. Variable names, spacing, and statement organization are clear.

Optional prompt cleanup: change "Type messaga: " to "Type message: ". This is a spelling issue in displayed text and does not affect the program logic. No resubmission or repeated run is required solely for that edit.

**Demonstrated scope and uncertainty.** Operand selection, the empty-string fallback, and basic type() inspection are successfully demonstrated in this guided exercise. No actual conceptual error is evident. Practical guard construction has not yet been demonstrated; it is the new application below. Longer fallback chains and whitespace normalization remain untaught.

**Lesson: using short-circuiting as a guard.**

A guard is a condition placed before an operation to check whether that operation may safely run. Python evaluates the left operand of and first. If it is falsy, Python returns that operand and does not evaluate the right operand. This previously introduced behavior can prevent an invalid calculation.

Worked example:

```python
total_minutes = 60
sessions = 0

enough_time = sessions > 0 and total_minutes / sessions >= 20
print(enough_time)
```

Output:

```text
False
```

The first comparison, sessions > 0, is False. Python therefore skips the division and comparison on the right. With sessions changed to 3, the guard succeeds, the division produces 20.0, and the second comparison is True. enough_time is then True. Both operands here are comparison results, so the selected result is a boolean.

Source: [Python boolean expression evaluation](https://docs.python.org/3.14/reference/expressions.html#boolean-operations).

Division by zero and remainder with a zero divisor raise ZeroDivisionError. In the example, the invalid division never runs. Moving the division before the guard, either to the left of and or into an earlier assignment, would lose that protection. The check must be evaluated before the operation it guards.

Source: [Python ZeroDivisionError](https://docs.python.org/3.14/library/exceptions.html#ZeroDivisionError).

This lesson applies Phase 1 boolean control flow. Formal exception handling with try/except/else/finally remains in Phase 2. Learners are not asked to deliberately produce an exception or implement handlers.

**Assignment: equal_shares.py.**

Determine whether chocolates can be distributed equally among guests with no remainder.

1. Read chocolates with int(input(...)), then read guests the same way.
2. For this exercise, enter a positive integer chocolate count and a nonnegative integer guest count. Additional input validation is not part of this task.
3. Assign can_share_evenly using one and expression. Its left condition must check that at least one guest exists. Its right condition must use % to check that equal distribution leaves zero remainder. Keep the remainder operation in this guarded right-hand condition.
4. Use can_share_evenly in an if/else to print "Equal shares possible" when true or "Equal shares unavailable" otherwise.

Recall that % calculates the remainder: 13 % 3 is 1. Zero remainder means there are no leftovers.

Run:

```bash
python3 equal_shares.py
```

| Chocolates | Guests | Required output after prompts |
| ---: | ---: | --- |
| 12 | 0 | Equal shares unavailable |
| 12 | 3 | Equal shares possible |
| 13 | 3 | Equal shares unavailable |

Submit code and these three actual runs. No predictions are requested.

**Review criteria.** The zero-guest case must finish normally because the remainder calculation is skipped. The other cases distinguish zero and nonzero remainders. Inspect source order as well as the messages: the guard must precede the remainder calculation, and the calculation must not be precomputed before the guard. Check meaningful names, operator spacing, and branch indentation. This focused set tests the new guard behavior without repeating earlier exercises.

**Next action.** Review equal_shares.py and these runs. After successful practice, consult the remaining Phase 1 curriculum; an introductory while loop is an appropriate next step toward repeated prompts. Explain repetition, rechecking the condition, updating the controlling value, and termination before assigning a loop. Do not introduce Phase 2 exception handling. Preserve neutral technical lesson records and teach the complete material in chat.

**Sources and version.** The Python expression reference and ZeroDivisionError documentation linked above were checked during this review. The last confirmed learner interpreter is Python 3.14.2; sources describe the 3.14 series.

**Record maintenance.** This entry supersedes the pending message_defaults.py assignment status in 0021. Add 0022 to the Foundation index, update the current checkpoint, and remove practical short-circuit guards from remaining-to-teach coverage while retaining this assignment's pending demonstration status here. Keep longer fallback chains in remaining coverage. Preserve earlier records and learner-owned Python files. The next record is 0023.
