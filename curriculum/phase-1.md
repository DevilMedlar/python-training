# Phase 1 Novice

Learn to write and run useful Python, starting with no programming experience.
Work through one lesson at a time. The tutor explains each new tool, shows working
code, and helps you apply it. Practice A is guided; Practice B gives you another
small program to make. Ask for a complete example whenever it helps.
There are no output-prediction drills, hand-tracing gates, or fixed hour quotas.


Work in [your Codespaces workspace](https://cuddly-trout-q767pqw4v79rfpjr.github.dev/).
Open a Python file, save, run it in the workspace Terminal, and use the result to
make the next change. Type answers to `input()` directly in that Terminal.
The tutor shows the technique and a working example before asking you to apply it.
Each lesson includes one short workspace control; repository administration is
optional material outside this Python sequence. See [workspace controls](../practice/BROWSER_WORKFLOW.md).

## P1-01 Run and inspect a program

**Workspace shortcut:** Open workspace/lesson_01.py in Explorer, save with Ctrl+S, then use Run Python File in Terminal (the triangle or editor right-click menu when available). The terminal fallback is in START_HERE.md.

**Prerequisites:** none.

**Outcome:** Write, save, and run a Python file in your Codespaces workspace.

A program is a file containing instructions for Python. Open
`workspace/lesson_01.py` in [your workspace](https://cuddly-trout-q767pqw4v79rfpjr.github.dev/).
Type or change the code, save with **Ctrl+S**, and use **Run Python File in Terminal**
from the triangle button or editor right-click menu when the Python extension is
available. If that control is missing, open **Terminal → New Terminal** and run
`python workspace/lesson_01.py` from the repository folder. All of this happens in
the browser workspace. [START_HERE.md](../START_HERE.md) shows the first run.

`print(...)` displays text in the Terminal. Put the text between quotes inside
the parentheses. Python runs one line and then the next. Start with this program:

```python
print("Hello, Python!")
print("I am learning in my workspace.")
```

```output
Hello, Python!
I am learning in my workspace.
```

**Practice A:** Change only the sentence inside the second pair of quotes to
something you want to say. Save with **Ctrl+S**, run the file, and see your sentence
in the Terminal.

**Practice B:** Optional variation: add a third `print(...)` with another sentence,
save, and run again.

**Hints:** Save `workspace/lesson_01.py` before running. If you see an old result,
check the file name in the Terminal command and run the current file again.

**Evidence:** Your saved file runs and displays your changed sentence. That is
enough to finish this first lesson.

**Sources:** [PY-INTRO](../audit/SOURCES.md#py-intro).

## P1-02 Values names and arithmetic

**Workspace shortcut:** Use Ctrl+S to save, then run the current Python file again to see the calculation.

**Prerequisites:** P1-01.

**Outcome:** Use assignments, integers, floats, strings, booleans, and
`None` for appropriate purposes.

A name refers to an object. Assignment evaluates the right side and binds the
name on the left; it is not an algebraic equation that remains active. `int`
represents integers; `float` represents finite-precision floating-point numbers.
Text is a `str`. `bool` represents truth values, and `None` often represents the
absence of a result. Objects have types; a name can later refer to another type.

For built-in integers, `/` returns a float, `//` floors the quotient, `%` gives a
remainder, and `**` means exponentiation. Negative floor division rounds down,
not toward zero. Parentheses make intended grouping clear. Binary floats cannot
represent every decimal fraction exactly; learn tolerances before comparing
results of approximate calculations.

```python
minutes = 135
hours = minutes // 60
remaining = minutes % 60
print(hours, "hours", remaining, "minutes")
```

```output
2 hours 15 minutes
```

**Practice A:** Convert 185 whole minutes into hours and leftover minutes.

**Practice B:** Make a seconds-to-minutes converter with `//` and `%`. Run it
with 59, 60, and 61 seconds and check that it displays both parts correctly.
Then print `/`, `//`, and `%` results for a negative integer to inspect the rules.

**Hints:** Use `//` for complete groups and `%` for what remains. If an input
changes, run the calculation again to update the stored result.

**Evidence:** Working duration converters, including a boundary at 60, with
clear variable names and the correct arithmetic operations.

**Sources:** [PY-INTRO](../audit/SOURCES.md#py-intro), [PY-FLOAT](../audit/SOURCES.md#py-float).

## P1-03 Strings and text transformations

**Workspace shortcut:** Use Ctrl+F to find a string in the open file; save and run after changing it.

**Prerequisites:** P1-02.

**Outcome:** Index, slice, normalize, combine, and format simple text.

Strings are immutable: transformations produce strings rather than changing
individual characters in place. Indexing starts at zero; a slice excludes its
stop position. An out-of-range single index raises `IndexError`, while slicing
can safely stop at the available end. A Python string models Unicode text;
one indexed code point is not necessarily one user-perceived character.

Use `strip` for surrounding whitespace, `split` for tokenization under a stated
rule, and `join` to combine parts. A whitespace split is not a complete natural
language tokenizer. An f-string evaluates expressions when the f-string is
created; it does not update itself after a variable changes.

```python
raw = "  Learn Python  "
clean = raw.strip()
print(clean[:5])
print("-".join(clean.lower().split()))
print(f"Length: {len(clean)}")
```

```output
Learn
learn-python
Length: 12
```

**Practice A:** Normalize a topic by trimming outside whitespace and lowercasing
it. Keep internal spaces unchanged and specify what empty input produces.

**Practice B:** Build a title cleaner using `strip`, `split`, and `" ".join(...)`.
Run it on a two-word title, repeated spaces, and whitespace-only text. Print the
cleaned title and its `len` so Python shows you the result.

**Hints:** Separate cleaning from splitting. Inspect the pieces returned by
`split` before joining them. This task does not require a loop or condition.

**Evidence:** Explain unchanged original text, slicing endpoints, and at least
one empty-input case. A tutor can use two fixed parts before loops are available.

**Sources:** [PY-TEXT](../audit/SOURCES.md#py-text).

## P1-04 Input conversion and explicit contracts

**Workspace shortcut:** Run the file, click its Terminal panel, type each answer at its prompt, and press Enter.

**Prerequisites:** P1-03.

**Outcome:** Distinguish text input, conversion, and a program's validity rules.

`input` returns text. Converting text with `int` is a separate operation that can
fail. Successful conversion does not mean the value is allowed by your program:
`-5` is an integer but may be invalid for a study duration. Never parse a number
by evaluating arbitrary Python code.

For now, use valid sample inputs, inspect conversion errors, and state the
contract. Branching and exception handling will make the program robust in later
lessons. `int(2.9)` truncates a number; it does not validate that it was originally
a whole number. `int("2.9")` fails. Accepted forms for `int` include more than
ASCII digits; a strict file format needs its own rule.

```python
# Fixed text stands in for input("Minutes: ") in this reproducible example.
raw = " 25 "
minutes = int(raw)
print(minutes + 5)
```

```output
30
```

**Practice A:** In a Python file under `workspace/`, ask for a name and a whole
number using `input()`, then display the number plus one. Run it, click the
Terminal, and type an answer at each prompt followed by Enter. Convert the numeric
answer with `int(...)` before adding.

**Practice B:** Make a minutes-to-seconds converter that asks for minutes using
`input()` and prints the result. Rerun it with `"0"`, `"-3"`, `"2.5"`, `" 7 "`,
and `"hello"`; inspect the conversion results or errors. The next lessons teach
how to reject unwanted values and retry.

**Hints:** Use `raw = input("Minutes: ")`, then `minutes = int(raw)` on the next
line. Keep prompts and answers in the running Terminal. If conversion fails,
read the exception and rerun with a whole number.

**Evidence:** A correct distinction between parsing and domain validation;
the learner can interpret the observed exception without needing to catch it yet.

**Sources:** [PY-BUILTINS](../audit/SOURCES.md#py-builtins).

## P1-05 Booleans decisions and boundaries

**Workspace shortcut:** Use Ctrl+S and Run Python File in Terminal after changing a boundary input.

**Prerequisites:** P1-04.

**Outcome:** Express a decision with comparisons and test all its boundaries.

`if`, `elif`, and `else` choose a suite of statements. Use `==` for value equality
and `=` for assignment. Comparisons can be chained, as in `0 <= score <= 100`.
`and` and `or` short-circuit and return operands, which are not necessarily
booleans; avoid assuming they always manufacture `True` or `False`.

An empty container, zero, and `None` are false in a condition, but may mean
different things in a data contract. Do not discard a valid zero merely because
it is false. Use `is None` to check the sentinel; use equality for numeric/text
values rather than relying on identity caching.

```python
score = 100
if 0 <= score <= 100:
    print("valid")
else:
    print("outside range")
print(0 or 7)
```

```output
valid
7
```

**Practice A:** Classify a supplied integer as negative, zero, or positive.

**Practice B:** Define three nonoverlapping study-duration bands, then implement
them. Include the value immediately below, at, and above each cutoff.

**Hints:** Write a tiny table of inputs and intended outputs before code.
Check that an earlier branch does not consume a later branch's cases.

**Evidence:** Explain one boundary, the difference between equality and
assignment, and why `if value` is not the same as `if value is not None`.

**Sources:** [PY-TRUTH](../audit/SOURCES.md#py-truth), [PY-FUNCTIONS](../audit/SOURCES.md#py-functions).

## P1-06 Loops accumulation and termination

**Workspace shortcut:** Click the running Terminal and press Ctrl+C to stop a loop; save the repair and run again.

**Prerequisites:** P1-05.

**Outcome:** Write and run finite repetition, including an empty input.

A `for` loop consumes an iterable. `range(start, stop, step)` describes integer
steps and excludes `stop`; a negative step reverses the direction when endpoints
permit it. A `while` loop repeats while its condition is true, so its state must
eventually change or another exit must occur. Know your environment's stop button
or keyboard interrupt before experimenting with open-ended loops.

An accumulator carries information between iterations. Initialize it before the
loop. `break` exits the innermost loop; `continue` starts its next iteration.
Run the loop to see its result; add a temporary `print` when you need to inspect a value.

```python
total = 0
for value in [2, 4, 6]:
    total += value
print(total)
print(list(range(5, 0, -2)))
```

```output
12
[5, 3, 1]
```

**Practice A:** Count the positive values in `[-2, 0, 5, 7]`, using an explicit
loop. Run it and compare the final count with the two positive entries.

**Practice B:** Sum integers from 1 through a supplied nonnegative integer `n`.
Test `n = 0`, `1`, and `5`. Then explain a loop that incorrectly resets its total.

**Hints:** Initialize a running total before the loop and update it inside the
loop. Run an empty list as a second case. Click the Terminal and press **Ctrl+C**
if a loop does not stop.

**Evidence:** A working counter and sum, correct empty input, and a program that
stops. Print the final total after the loop when you want one result.

**Sources:** [PY-FUNCTIONS](../audit/SOURCES.md#py-functions).

## P1-07 Collections and choosing a representation

**Workspace shortcut:** Use Explorer → New File to keep this collections exercise in its own .py file.

**Prerequisites:** P1-06.

**Outcome:** Choose and use a list, tuple, dictionary, or set for a small task.

A list is a mutable sequence. A tuple is an immutable sequence of references;
it can contain a mutable object. A dictionary maps hashable keys to values and
preserves insertion order. A set models unique hashable values; its iteration
order is not a sorting contract. An empty `{}` is a dictionary; use `set()` for
an empty set.

Choose the structure for the operations you need. A dictionary makes lookup by
topic natural; a list retains duplicate sessions in order. Many mutating methods,
including `list.append` and `list.sort`, return `None`. Use `sorted` to produce a
new sorted list. Do not structurally modify a collection while iterating over it
without a carefully defined strategy.

```python
totals = {}
for topic in ["loops", "files", "loops"]:
    totals[topic] = totals.get(topic, 0) + 1
print(totals)
print(sorted(set([3, 1, 3])))
```

```output
{'loops': 2, 'files': 1}
[1, 3]
```

**Practice A:** Count whitespace-separated words under a case-sensitive contract.
The empty string should produce an empty mapping.

**Practice B:** Remove repeated strings while preserving first appearances.
Explain why simply converting to a set does not express the required order.

**Hints:** Decide whether duplicates matter. For counting, look up the previous
count with a default of zero; for order, maintain an explicit output sequence.

**Evidence:** Correct normal and empty cases, plus a justified representation.

**Sources:** [PY-COLLECTIONS](../audit/SOURCES.md#py-collections).

## P1-08 Functions parameters and return values

**Workspace shortcut:** Use Ctrl+P to reopen your function file quickly, then run its example calls.

**Prerequisites:** P1-07.

**Outcome:** Turn a computation into a reusable function with an explicit contract.

A function groups behavior behind a name and parameters. Calling it binds
arguments to those parameters. `return` supplies a result to the caller and ends
that call. `print` writes output; it does not substitute for returning a useful
value. Reaching the end without a return value produces `None`.

Keep calculations separate from input and display so you can test them without
typing into a menu. Specify accepted input, output, empty behavior, mutation, and
failures. These choices need not be elaborate, but they must be clear. Reusing a
function should not unexpectedly ask for input or change unrelated global state.

```python
def average(values):
    if not values:
        return None
    return sum(values) / len(values)

print(average([20, 40]))
print(average([]))
```

```output
30.0
None
```

**Practice A:** Write a function returning the count of values greater than or
equal to a threshold. Do not print inside it.

**Practice B:** Write a search function returning the first matching index or
`None` when missing. Cover a match at index zero, duplicates, and an empty list.

**Hints:** Write an example call and expected result before the definition.
For a search, return immediately on a match and decide what happens after the loop.

**Evidence:** Explain parameters versus arguments and why a missing value must
not be confused with a legitimate zero. Test the same function with new inputs.

**Sources:** [PY-FUNCTIONS](../audit/SOURCES.md#py-functions).

## P1-09 References mutation and scope

**Workspace shortcut:** Use the Split Editor button to compare two small examples side by side.

**Prerequisites:** P1-08.

**Outcome:** Explain aliasing, a shallow copy, a mutable default, and local rebinding.

Assignment does not copy an object. Two names can refer to one list, so mutation
through either name affects that list. A shallow copy creates a new outer
container while retaining references to nested objects. A parameter is another
local name for the argument object; rebinding the parameter differs from mutating
the shared object. Avoid describing this as automatic deep copying.

Default argument expressions are evaluated when the function is defined. A
mutable default can therefore be shared across calls. Use a `None` default and
create a fresh list inside when that is the intended behavior. Learn local and
enclosing scopes through small examples before using `global` or `nonlocal`.

```python
original = [["loops"]]
copy = original.copy()
copy[0].append("files")
copy.append(["testing"])
print(original)
print(len(copy))
```

```output
[['loops', 'files']]
2
```

**Practice A:** Run the shallow-copy example, then use two separate outer lists
and compare the results. Print both lists after each change. Repair a version
that accidentally shares a list between two records.

**Practice B:** Write `add_topic(topic, topics=None)` that makes a fresh list when
omitted and appends to a supplied list when provided. Explain that mutation policy.

**Hints:** Count objects separately from names. For the default, ask when the
list is created and which future calls can still reach it.

**Evidence:** Two actual calls keep separate default lists, while a supplied list follows the documented mutation policy.

**Sources:** [PY-CLASSES](../audit/SOURCES.md#py-classes), [PY-MODEL](../audit/SOURCES.md#py-model).

## P1-10 Errors debugging and tests

**Workspace shortcut:** Ctrl+click a file-and-line link in a Terminal traceback to open the failing line.

**Prerequisites:** P1-09.

**Outcome:** Reproduce a failure, read a traceback, repair its cause, and test the repair.

A syntax error prevents valid parsing; an exception occurs during execution.
Read the exception type and message, then open the linked failing line. Reduce the
input until the failure is understandable. State expected and observed behavior,
change one suspected cause, and rerun a case that failed before the fix.

Catch an expected exception near the operation that can raise it. Conversion and
domain validation remain separate. A broad catch that ignores every error hides
information. Assertions are useful learning checks; optimized execution can
remove them, so required input validation needs ordinary checks and exceptions.

```python
def positive_minutes(raw):
    value = int(raw)
    if value <= 0:
        raise ValueError("minutes must be positive")
    return value

try:
    positive_minutes("0")
except ValueError as error:
    print(error)
```

```output
minutes must be positive
```

**Practice A:** Add checks to the averaging function for its documented normal,
single-value, and empty inputs. Introduce and then repair an off-by-one bug.

**Practice B:** Write an interactive positive-integer reader with retries for
invalid text and nonpositive values. Explain why unrelated programming errors
should remain visible. Type invalid answers and then a valid answer directly into
the Terminal prompts; confirm that the program keeps asking until it accepts one.

**Hints:** First reproduce a failure without the menu. Read the final exception
line before scanning every line of the program.

**Evidence:** A small bug report, a repaired function, and a regression case.

**Sources:** [PY-ERRORS](../audit/SOURCES.md#py-errors), [PY-ASSERT](../audit/SOURCES.md#py-assert).

## P1-11 Modules environments and standard tools

**Workspace shortcut:** Open the Command Palette (Ctrl+Shift+P) and choose Python: Select Interpreter when the Python extension is available.

**Prerequisites:** P1-10.

**Outcome:** Import a helper without starting its interactive interface and identify
which interpreter owns an installed package.

A module is an importable unit of Python code. A package organizes importable
modules. Importing a module can execute its top-level statements; use an
`if __name__ == "__main__"` guard for an entry point that should run only when
the module is launched as the main program. Do not name your own file `json.py`
or another imported module's name without understanding the resulting shadowing.

Explore useful standard modules one at a time: `pathlib`, `json`, `csv`, `math`,
`statistics`, and `random`. A virtual environment isolates a project's Python
packages from other environments. It does not make code a security sandbox or
automatically freeze every dependency. Use the interpreter's `-m pip` to make the
installation target explicit.

```python
from math import isclose
from statistics import mean

print(mean([20, 40]))
print(isclose(0.1 + 0.2, 0.3))
```

```output
30
True
```

**Practice A:** Move a calculation into a helper module, import it, and verify that
importing does not ask for input or print a menu.

**Practice B:** In the workspace Terminal, run `python --version` and
`python -m pip --version` to inspect the interpreter and its package installer.
Use the [environment exercise](../practice/BROWSER_WORKFLOW.md#environment-exercise-for-p1-11)
when you need a separate project environment. These commands run in Codespaces.

**Hints:** For a script launched as `python workspace/lesson_11.py`, keep
`helpers.py` beside it and use `import helpers`. For a module launched from the
repository root as `python -m workspace.lesson_11`, use
`from workspace import helpers`. Match the import to how you run the file.

**Evidence:** An importable helper and an explanation of the main guard and
environment boundary. Package installation is not needed to complete this phase.

**Sources:** [PY-MODULES](../audit/SOURCES.md#py-modules), [PY-VENV](../audit/SOURCES.md#py-venv).

## P1-12 Files serialization and the first project

**Workspace shortcut:** Use Explorer to open the JSON file your program saved, then rerun the program in the same workspace.

**Prerequisites:** P1-11.

**Outcome:** Save and load validated practice data without silently discarding a
damaged existing file.

A relative path is interpreted from the working directory, which may differ
from the script's directory. Use an explicit path policy, `with` for file
lifetime, and an encoding such as UTF-8 for text. JSON syntax validation is not
application schema validation. Check the loaded shape and value rules separately.
Booleans are a subclass of integers in Python; reject them explicitly when a
whole-number record contract excludes them.

A missing file can mean “new history.” Malformed or unreadable data needs a
visible error, not an empty replacement. A direct write can truncate existing
content; use disposable practice data. Later lessons introduce safer replacement
and transaction policies. A file is not automatically saved whenever memory changes.

```python
import json

sessions = [20, 40]
text = json.dumps(sessions)
loaded = json.loads(text)
print(loaded == sessions)
print(sum(loaded))
```

```output
True
60
```

**Practice A:** Round-trip a list of positive integer durations through a temporary
JSON file. Try a missing file, invalid JSON, and a valid JSON object of the wrong shape.

**Practice B:** Build [Capstone 1](../practice/CAPSTONES.md#capstone-1-study-tracker)
from its requirements before opening the reference implementation. Explain the
calculation, validation, load, and save boundaries.

**Hints:** Test the calculation separately. Then classify each load failure and
decide whether continuing could overwrite valuable information.

**Evidence:** A tracker you can run, use, save, close, and reopen, with the
acceptance cases and one useful feature change. See [assessment](../practice/ASSESSMENT.md)
for a short practical check.

**Sources:** [PY-FILES](../audit/SOURCES.md#py-files), [PY-JSON](../audit/SOURCES.md#py-json).
