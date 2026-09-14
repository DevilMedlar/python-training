# Phase 1 Novice

Learn to express, trace, test, and explain a small computation. Start without
programming experience. Work through one lesson at a time; a lesson may take
several sessions. The tutor follows [the teaching protocol](../tutor/INSTRUCTIONS.md).
Practice A is guided work; Practice B is a separate transfer check. A tutor should
not reveal a transfer solution before the learner attempts it, unless asked.

## P1-01 Run and inspect a program

**Prerequisites:** none.

**Outcome:** Save a Python file, run it, and distinguish source code, terminal
commands, interpreter prompts, and program output.

A program is a set of instructions expressed as source text. The interpreter
executes that program; an editor changes its text. A terminal can launch the
interpreter. These are different jobs, even when an application puts them in
neighboring panels. Use [setup](../START_HERE.md) and record the working command.

Run a saved file after each change. Python's interactive prompt displays the
value of many expressions, but a script needs an explicit operation such as
`print` to display a result. Indentation groups statements; it is meaningful.

```python
print("Ready to learn")
print(2 + 3)
```

```output
Ready to learn
5
```

**Practice A:** Save and run a two-line program displaying a chosen project name
and the result of adding two whole numbers. Show the command and output.

**Practice B:** Make a different three-line program. Deliberately remove a quote,
observe the error, restore it, and explain which file you actually ran.

**Hints:** Find the saved file's directory first. Then compare the terminal's
working directory and filename with the editor's tab.

**Evidence:** A successful run plus an explanation of why `python hello.py`
belongs in a terminal rather than inside a Python source file. Do not assess
memory of an editor's buttons as knowledge of Python.

**Sources:** [PY-INTRO](../audit/SOURCES.md#py-intro).

## P1-02 Values names and arithmetic

**Prerequisites:** P1-01.

**Outcome:** Trace assignments and use integers, floats, strings, booleans, and
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
minutes = 10
print(hours, remaining, minutes)
print(-7 // 3)
```

```output
2 15 10
-3
```

**Practice A:** Convert 185 whole minutes into hours and leftover minutes.

**Practice B:** For an initial integer `x`, bind `y = x + 4`, then rebind `x`.
Predict both values. Also compare `/`, `//`, and `%` on a negative integer.

**Hints:** Evaluate each right side using values at that moment. For division,
locate the quotient on a number line before choosing its floor.

**Evidence:** Correct traces, a boundary at 60 minutes, and an explanation of
why rebinding `minutes` did not recalculate `hours`.

**Sources:** [PY-INTRO](../audit/SOURCES.md#py-intro), [PY-FLOAT](../audit/SOURCES.md#py-float).

## P1-03 Strings and text transformations

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

**Practice B:** Predict `strip`, `split`, and `len` results for a two-word title,
the same title with repeated spaces, and whitespace-only text. Rebuild a normalized
title with `" ".join(...)`. Explain which original whitespace is lost.

**Hints:** Separate cleaning from splitting. Inspect the pieces returned by
`split` before joining them. This task does not require a loop or condition.

**Evidence:** Explain unchanged original text, slicing endpoints, and at least
one empty-input case. A tutor can use two fixed parts before loops are available.

**Sources:** [PY-TEXT](../audit/SOURCES.md#py-text).

## P1-04 Input conversion and explicit contracts

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

**Practice A:** In your own interactive file, ask for a name and a whole number,
then display the number plus one. Explain why adding to the raw text fails.

**Practice B:** Classify `"0"`, `"-3"`, `"2.5"`, `" 7 "`, and `"hello"`:
which can `int` convert, and which would satisfy a positive-duration rule?

**Hints:** First write each value's current type. Then separate “can convert”
from “allowed after conversion.” Do not add a retry loop before learning loops.

**Evidence:** A correct distinction between parsing and domain validation;
the learner can interpret the observed exception without needing to catch it yet.

**Sources:** [PY-BUILTINS](../audit/SOURCES.md#py-builtins).

## P1-05 Booleans decisions and boundaries

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

**Prerequisites:** P1-05.

**Outcome:** Trace and write finite repetition, including an empty input.

A `for` loop consumes an iterable. `range(start, stop, step)` describes integer
steps and excludes `stop`; a negative step reverses the direction when endpoints
permit it. A `while` loop repeats while its condition is true, so its state must
eventually change or another exit must occur. Know your environment's stop button
or keyboard interrupt before experimenting with open-ended loops.

An accumulator carries information between iterations. Initialize it before the
loop. `break` exits the innermost loop; `continue` starts its next iteration.
Before executing, trace an iteration, the current item, and the accumulated value.

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
loop. Predict how the count changes at each iteration.

**Practice B:** Sum integers from 1 through a supplied nonnegative integer `n`.
Test `n = 0`, `1`, and `5`. Then explain a loop that incorrectly resets its total.

**Hints:** Ask what must remain true after each processed item. Trace an empty
input before adding special branches that may be unnecessary.

**Evidence:** A correct trace and a terminating program. Distinguish printing
inside the loop from printing the final result outside it.

**Sources:** [PY-FUNCTIONS](../audit/SOURCES.md#py-functions).

## P1-07 Collections and choosing a representation

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

**Practice A:** Compare aliasing, a shallow copy, and appending to the outer copy.
Draw which lists are shared before you run the program.

**Practice B:** Write `add_topic(topic, topics=None)` that makes a fresh list when
omitted and appends to a supplied list when provided. Explain that mutation policy.

**Hints:** Count objects separately from names. For the default, ask when the
list is created and which future calls can still reach it.

**Evidence:** Predict two successive calls and distinguish equality from identity.

**Sources:** [PY-CLASSES](../audit/SOURCES.md#py-classes), [PY-MODEL](../audit/SOURCES.md#py-model).

## P1-10 Errors debugging and tests

**Prerequisites:** P1-09.

**Outcome:** Reproduce a failure, read a traceback, repair its cause, and test the repair.

A syntax error prevents valid parsing; an exception occurs during execution.
Read the exception type and message, then trace the relevant calls. Reduce the
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
should remain visible. Use a clean way to stop an unfinished interaction.

**Hints:** First reproduce a failure without the menu. Read the final exception
line before scanning every line of the program.

**Evidence:** A small bug report, a repaired function, and a regression case.

**Sources:** [PY-ERRORS](../audit/SOURCES.md#py-errors), [PY-ASSERT](../audit/SOURCES.md#py-assert).

## P1-11 Modules environments and standard tools

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

**Practice B:** Create a virtual environment using [setup](../START_HERE.md).
Show its interpreter version and `-m pip --version`, without installing anything.

**Hints:** Keep both modules in the initial practice directory. When an import
fails, check the interpreter and module location before changing application code.

**Evidence:** An importable helper and an explanation of the main guard and
environment boundary. Package installation is not needed to complete this phase.

**Sources:** [PY-MODULES](../audit/SOURCES.md#py-modules), [PY-VENV](../audit/SOURCES.md#py-venv).

## P1-12 Files serialization and the first project

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

**Evidence:** The capstone acceptance cases, an independent feature change, and
a later recall task. See [assessment](../practice/ASSESSMENT.md) before advancing.

**Sources:** [PY-FILES](../audit/SOURCES.md#py-files), [PY-JSON](../audit/SOURCES.md#py-json).
