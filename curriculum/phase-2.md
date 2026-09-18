# Phase 2 Competent practitioner

Build applications that remain understandable when requirements and inputs change.
Enter after the Phase 1 capstone, or use [placement](../tutor/PLACEMENT.md) to
demonstrate equivalent skills. Improve one continuing project while studying these
lessons. Reference tools are allowed; generated solutions do not prove independence.


Work in [your Codespaces workspace](https://cuddly-trout-q767pqw4v79rfpjr.github.dev/).
Open a Python file, save, run it in the workspace Terminal, and use the result to
make the next change. Type answers to `input()` directly in that Terminal.
The tutor shows the technique and a working example before asking you to apply it.
Each lesson includes one short workspace control; repository administration is
optional material outside this Python sequence. See [workspace controls](../practice/BROWSER_WORKFLOW.md).

## P2-01 Collection patterns and complexity

**Workspace shortcut:** Use Ctrl+F to find the collection operation you are replacing; save and rerun its checks.

**Prerequisites:** P1-12.

**Outcome:** Choose clear collection operations and explain their main time and
space tradeoffs.

Practice comprehensions, `enumerate`, `zip`, unpacking, `Counter`, `defaultdict`,
and `deque` when they express the task. Do not turn several dependent actions
into an unreadable comprehension. `zip` normally stops at the shortest input;
use `strict=True` when unequal lengths indicate an error. Dictionary and set
membership are usually average constant-time operations under ordinary hashing
assumptions, not guaranteed constant cost for arbitrary keys or collisions.

```python
from collections import Counter

counts = Counter(["loops", "tests", "loops"])
print(counts["loops"], counts["missing"])
print([f"{i}: {topic}" for i, topic in enumerate(["loops", "tests"], start=1)])
```

```output
2 0
['1: loops', '2: tests']
```

**Practice A:** Group topic-duration records and compute each topic's count and
total. State whether missing topics are an error or a zero result.

**Practice B:** Join two aligned sequences while detecting unequal lengths, and
remove duplicates with stable order. Explain the extra memory used by your method.

**Hints:** Write the output shape first. Separate a counting problem from a queue
problem before choosing a container.

**Evidence:** Normal, empty, duplicate, and mismatched-length cases; a complexity
argument naming what `n` counts and what assumptions it requires.

**Sources:** [PY-COLLECTIONS](../audit/SOURCES.md#py-collections), [PY-BUILTINS](../audit/SOURCES.md#py-builtins).

## P2-02 Iterators generators and streaming

**Workspace shortcut:** Use Terminal → New Terminal for a fresh run of your streaming example.

**Prerequisites:** P2-01.

**Outcome:** Consume a stream once and account for its lifetime and storage.

An iterable can provide an iterator; an iterator supplies successive values and
eventually raises `StopIteration`. Calling a generator function creates a generator
object; its body advances during iteration. A one-pass iterator cannot be reused
as though it were the original collection. Materializing `list(stream)` consumes
the stream and stores its values.

Laziness delays work; it does not prove bounded memory. A downstream list, grouping
stage, cache, or lagging `itertools.tee` consumer can retain growing data. Handle
external resources explicitly, especially when consumers stop early.

```python
def nonblank(lines):
    for line in lines:
        if line.strip():
            yield line.strip()

stream = nonblank([" loops ", "", "tests"])
print(next(stream))
print(list(stream))
print(list(stream))
```

```output
loops
['tests']
[]
```

**Practice A:** Turn a list-producing transformation into a generator. Show what
work happens before and after the first `next` call.

**Practice B:** Aggregate an iterator of records in one pass. Use a test iterator
that fails if iterated twice, then describe memory growth with unique keys.

**Hints:** Follow each consumer. Ask which stage retains every previous result.

**Evidence:** Correct exhaustion behavior and a justified memory claim that
includes the aggregation map, not only the input reader.

**Sources:** [PY-ITERTOOLS](../audit/SOURCES.md#py-itertools), [PY-CLASSES](../audit/SOURCES.md#py-classes).

## P2-03 Function interfaces scope and wrappers

**Workspace shortcut:** Use Find All References on a function when Python language support is available, or Ctrl+Shift+F to find its callers.

**Prerequisites:** P2-02.

**Outcome:** Design an interface with explicit inputs, defaults, outputs, and mutation.

Use positional-only and keyword-only parameters when they clarify how callers
should use an API. A closure accesses an enclosing binding; it does not generally
snapshot a value when created. Keep the distinction between default evaluation
and closure lookup visible. Prefer explicit dependency parameters over hidden
global configuration when tests or different callers need control.

A decorator takes a callable and usually returns a callable. Introduce wrapping
only for a specific repeated concern. Metadata, exceptions, and asynchronous
behavior are part of the calling contract, not decorative details.

```python
def scaled_total(values, *, multiplier=1):
    return sum(values) * multiplier

callbacks = [lambda value=value: value for value in range(3)]
print(scaled_total([2, 3], multiplier=4))
print([callback() for callback in callbacks])
```

```output
20
[0, 1, 2]
```

**Practice A:** Refactor an interactive calculation into a pure function and a
small interface. Make an optional formatting choice keyword-only.

**Practice B:** Compare loop-created closures with and without the default above.
Explain why the default changes the example, and preserve errors in a small wrapper.

**Hints:** Record when each binding is read. Avoid claiming a default creates a
deep copy; it stores a reference to the evaluated object.

**Evidence:** Two independent callers, default isolation where required, and an
explanation of one rejected interface design.

**Sources:** [PY-FUNCTIONS](../audit/SOURCES.md#py-functions), [PY-FUNCTOOLS](../audit/SOURCES.md#py-functools).

## P2-04 Classes dataclasses and composition

**Workspace shortcut:** Use the Split Editor button to view the class and its tests together.

**Prerequisites:** P2-03.

**Outcome:** Model useful state without accidental sharing or unnecessary inheritance.

A class is useful when it protects related state or supplies a coherent interface.
Use a function when no enduring state or protocol is needed. Prefer composition
when one object uses another's behavior without satisfying a meaningful subtype
relationship. Class attributes and per-instance attributes have different sharing
behavior.

Dataclasses generate methods from declared fields. `default_factory` creates
per-instance defaults; `frozen=True` prevents ordinary field assignment, but does
not recursively freeze nested mutable objects or validate annotations. A domain
invariant needs explicit enforcement at its intended boundary.

```python
from dataclasses import dataclass, field

@dataclass
class StudyPlan:
    topics: list[str] = field(default_factory=list)

first, second = StudyPlan(), StudyPlan()
first.topics.append("testing")
print(first.topics, second.topics)
```

```output
['testing'] []
```

**Practice A:** Model a topic and a duration, stating which operations may mutate
the record and where invalid values are rejected.

**Practice B:** Build a report object that receives a separate storage object.
Replace storage with an in-memory version without changing report calculations.

**Hints:** Identify the state before introducing a class. Create two instances
and mutate one to expose unintended sharing.

**Evidence:** An invariant test, independent instances, and a justified choice
among a plain function, dataclass, and custom class.

**Sources:** [PY-DATACLASSES](../audit/SOURCES.md#py-dataclasses), [PY-CLASSES](../audit/SOURCES.md#py-classes).

## P2-05 Exceptions and resource ownership

**Workspace shortcut:** Ctrl+click a Terminal traceback location to inspect the resource acquisition that failed.

**Prerequisites:** P2-04.

**Outcome:** Preserve useful error context and release resources on failure.

Separate expected user errors, operational failures, and programming defects.
Catch narrowly enough that a new bug remains visible. When translating an error,
`raise NewError(...) from error` records its cause. `finally` expresses cleanup;
a context manager packages entry and exit behavior. A context manager can suppress
exceptions deliberately, so inspect its contract.

The component that acquires a resource should have an explicit ownership policy.
Do not close a stream supplied by a caller unless the API says ownership transfers.
Use `ExitStack` when a variable number of acquired resources needs coordinated
cleanup. Avoid opening every file at once when sequential access suffices.

```python
from contextlib import ExitStack
from io import StringIO

with ExitStack() as stack:
    stream = stack.enter_context(StringIO("one\ntwo\n"))
    print(sum(1 for _ in stream))
print(stream.closed)
```

```output
2
True
```

**Practice A:** Wrap an expected conversion failure in a domain-specific message
while retaining the original exception as its cause.

**Practice B:** Acquire two resources, make a third acquisition fail, and prove
that the first two close. Then test successful completion and early exit.

**Hints:** Write “who closes this?” beside every acquisition. Register cleanup
immediately after successful acquisition rather than only at the end.

**Evidence:** Observed cleanup on success and failure, with an explanation of
which exceptions propagate or are transformed.

**Sources:** [PY-CONTEXT](../audit/SOURCES.md#py-context), [PY-ERRORS](../audit/SOURCES.md#py-errors).

## P2-06 Type hints and runtime validation

**Workspace shortcut:** Open View → Problems to inspect editor diagnostics when a type checker is configured.

**Prerequisites:** P2-05.

**Outcome:** Use annotations to communicate interfaces without mistaking them for checks.

Python does not enforce ordinary type annotations at runtime. Static checking,
runtime validation, and serialization schemas are distinct activities. Annotate
public inputs and returns, express optional results precisely, and prefer a
useful interface such as `Iterable[int]` when any iterable is acceptable.

`Any` relaxes checking; it is not a statement that all operations are safe.
`TypedDict` describes dictionary shapes to a checker, but does not validate loaded
JSON. A `Protocol` can describe required operations without nominal inheritance.
Choose one optional static checker later and record its version and configuration.

```python
from collections.abc import Iterable

def total(values: Iterable[int]) -> int:
    return sum(values)

print(total(number for number in [5, 15]))
```

```output
20
```

**Practice A:** Annotate a function that returns a found record or `None`.
Show how a caller handles both outcomes.

**Practice B:** Validate external topic-duration JSON, then pass the validated
records to a typed calculation. Include wrong shapes, booleans, and negative values.

**Hints:** Locate the trust boundary. An annotation on a dataclass field does
not make its constructor reject an invalid argument.

**Evidence:** Explain one problem a static checker can flag and another that
still requires a runtime check. Report actual checker execution separately.

**Sources:** [PY-TYPING](../audit/SOURCES.md#py-typing).

## P2-07 Testing debugging and logging

**Workspace shortcut:** In the workspace Terminal, run python -m unittest discover -s workspace -p "test_*.py" -v; read the result there.

**Prerequisites:** P2-06.

**Outcome:** Connect requirements to tests and diagnose failures with controlled evidence.

Test observable behavior: normal input, boundaries, invalid input, and meaningful
failures. Use temporary files and local databases when they expose a real boundary
cheaply. Substitute external services or time sources at narrow interfaces rather
than mocking every internal function. A regression test must detect the bug it
is intended to prevent.

Logs explain events during execution; they are not a replacement for assertions
about expected behavior. Avoid logging secrets or real private records. Coverage
reports show executed code, not the adequacy of assertions or absence of defects.
The included suite uses `unittest` to keep the core dependency-free; pytest is an
optional later tool, not a prerequisite for learning to test.

**Worked example:** In the Codespaces Terminal, run
`python -m unittest discover -s workspace -p "test_*.py" -v` to run your tests.
Read the discovered count and any failure output directly there.
Read one test in [test_studylog.py](../tests/test_studylog.py). Identify its
requirement, setup, action, and observation before reading the implementation.

**Practice A:** Add a regression test for a duplicate-record aggregation bug.
Temporarily restore the bug and confirm the test fails for the expected reason.

**Practice B:** Test a command's success and failure exit statuses, standard output,
and error output. A bad later record must not produce a partial success report.

**Hints:** Start with a small case whose correct result is supplied by the task. Make the failure explanation useful
enough that someone else can identify the broken requirement.

**Evidence:** A detected defect and a repaired behavior. Do not reward test count
or a coverage percentage as a substitute for these observations.

**Sources:** [PY-UNITTEST](../audit/SOURCES.md#py-unittest), [PY-LOGGING](../audit/SOURCES.md#py-logging).

## P2-08 Structured text numbers and dates

**Workspace shortcut:** Use Explorer → New File to add a small CSV fixture beside the parser exercise.

**Prerequisites:** P2-07.

**Outcome:** Preserve a data format's meaning through parsing, validation, and output.

Use a CSV parser for CSV rather than splitting every line on a comma: quoted
fields can contain commas and newlines. Specify encoding, headers, field counts,
whitespace policy, and malformed-record behavior. Open CSV files with `newline=""`
as documented. Loading all rows uses memory proportional to the input.

Use `Decimal` constructed from decimal text when the task needs decimal
arithmetic; choose a rounding policy explicitly. A decimal representation alone
does not settle a domain's precision rules. Distinguish dates, naive datetimes,
aware datetimes, and time zones. Define your data's zone before comparing event
times. Use regular expressions for a well-scoped text grammar, not arbitrary nesting.

```python
from decimal import Decimal
from datetime import date

print(Decimal("0.1") + Decimal("0.2"))
print((date(2026, 9, 15) - date(2026, 9, 14)).days)
```

```output
0.3
1
```

**Practice A:** Parse the sample CSV, including a quoted topic with a comma.
Test missing/extra fields and an invalid header.

**Practice B:** Design a date-stamped export with an explicit schema and rounding
rule. Test a leap-day date and round-trip non-ASCII text.

**Hints:** Preserve data in its structured form until presentation. Do not use
display formatting as a substitute for numeric validation.

**Evidence:** A written format contract and boundary tests tied to that contract.

**Sources:** [PY-CSV](../audit/SOURCES.md#py-csv), [PY-DECIMAL](../audit/SOURCES.md#py-decimal), [PY-DATETIME](../audit/SOURCES.md#py-datetime).

## P2-09 HTTP APIs and external failures

**Workspace shortcut:** Use the Terminal plus button to keep a separate terminal for optional API experiments.

**Prerequisites:** P2-08.

**Outcome:** Design a small external-service adapter with bounded failure behavior.

An HTTP response involves a status, headers, and body; a transport failure may
produce no usable response. JSON syntax success does not validate a service's
schema. Define timeouts, maximum response/work sizes, pagination limits, and what
the application does when the remote service is unavailable. Check the chosen
client's current documentation: a timeout argument is not necessarily a total
deadline for the complete operation.

Retries can repeat effects. A timeout does not prove that a remote write never
happened. Start with read-only requests and a stubbed service. Introduce retry
classification, a finite budget, and idempotency only when their meaning is clear.
Keep tokens out of source files and logs.

**Worked example:** A stub returns a status and a decoded mapping for a study
catalog. The adapter validates required fields and converts known failures into
a useful application error. The core calculation receives only validated records.
No live service or credentials are required for this design exercise.

**Practice A:** Write the adapter against a supplied fake response. Test success,
missing fields, an unsuccessful status, and a transport exception.

**Practice B:** Design pagination with a maximum page count and a test for a
repeated cursor. Explain how the application avoids running forever.

**Hints:** Separate sending, decoding, validating, and calculating. Write the
failure contract before adding automatic retries.

**Evidence:** Deterministic local tests and a clear statement of what remains
unverified about a real service. Live integration is an optional extension.

**Sources:** [PY-URLLIB](../audit/SOURCES.md#py-urllib), [HTTP-SEMANTICS](../audit/SOURCES.md#http-semantics).

## P2-10 SQLite queries and transactions

**Workspace shortcut:** Use Explorer to locate the disposable database file, and Terminal → New Terminal for its checks.

**Prerequisites:** P2-09.

**Outcome:** Store records with parameterized queries and demonstrate transaction behavior.

Tables, keys, constraints, joins, and aggregation express relationships in
structured data. Parameterize SQL values; do not insert user values with string
formatting. A transaction groups changes under a chosen policy. Explicitly
document transaction ownership so a helper does not unexpectedly commit another
caller's pending work.

In Python 3.12+, SQLite's `autocommit` setting offers explicit transaction control.
Do not rely on a changing default. A connection's `with` block manages a
transaction under appropriate settings; it does not close the connection.
Use a separate closing policy. SQLite type affinity is not identical to Python
type validation, so validate a strict integer domain before storage.

**Worked example:** Inspect [inventory.py](../examples/inventory.py), which owns
its connections. Its conditional update combines a stock check and decrement,
and a constraint protects nonnegative quantities. A failed reservation rolls back.
This is a local teaching example, not a complete reservation service.

**Practice A:** Insert and aggregate synthetic sessions, including a topic with
an apostrophe. Confirm the query handles it as a value.

**Practice B:** Make a multi-statement transaction fail after its first write and
verify rollback from a separate connection to a temporary file database.

**Hints:** Mark begin/commit/rollback and close separately. Specify whether a
function owns the connection or merely borrows it.

**Evidence:** Constraints, rollback, parameterization, and connection cleanup
demonstrated with concrete tests.

**Sources:** [PY-SQLITE](../audit/SOURCES.md#py-sqlite).

<a id="p2-11-git-packaging-and-reproducible-setup"></a>

## P2-11 Packaging and reproducible setup

**Workspace shortcut:** Open the Command Palette (Ctrl+Shift+P) and choose Python: Create Environment when available, or use the terminal steps in the workspace guide.

**Prerequisites:** P2-10.

**Outcome:** Build a Python package and run it from a clean environment in Codespaces.

Packaging makes your Python application installable with its required files and
command entry points. Start with the smallest package that serves your project.
Use a fresh virtual environment inside this Codespace to check installation
without relying on packages already present in your working environment.

For a distributable Python project, learn `pyproject.toml`, build systems, source
distributions, wheels, and entry points. A distribution name and import name may
differ. A successful import from the checkout does not prove the built wheel
contains the required files. Compatibility ranges and an exact experiment
environment solve different problems; neither guarantees every platform works.

**Worked example:** Follow the [PyPA packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
using a disposable package in the Codespaces Terminal. Build its wheel, install
that wheel in a fresh virtual environment in the workspace, and run from a
separate temporary directory outside the source checkout. Publishing is optional.

**Practice A:** Refactor the study reporter into a package with a command entry
point and documented installation. Inspect the resulting artifact's contents.

**Practice B:** Create a fresh virtual environment in the Codespace and follow
your README to install the built wheel. Run the documented command from outside
the source directory. Repair any missing file, dependency, or entry point.

**Hints:** Separate runtime dependencies, developer tools, and build requirements.
When a clean install fails, inspect the wheel rather than adding random path hacks.

**Evidence:** A clean installation of the wheel and a working documented command in Codespaces.

**Sources:** [PY-PACKAGING](../audit/SOURCES.md#py-packaging).

## P2-12 Algorithms command lines and application delivery

**Workspace shortcut:** Use the workspace Terminal to run your command with --help and then with a sample file.

**Prerequisites:** P2-11.

**Outcome:** Deliver a complete small application with a justified algorithm and usable failures.

Learn linear search, sorting, binary-search preconditions, stacks/queues, and
basic recursion through small examples. State time and space costs in terms of
the actual input. Big-O ignores constants and lower-order effects; it is not a
measurement of a particular program's runtime. Prefer a correct clear baseline
before optimizing. Recursion has a finite practical depth in Python.

Command-line interfaces need useful help, validation, standard output for results,
error output for failures, and meaningful exit codes. `argparse` handles command
syntax; application validation still belongs in the application. Keep import-time
behavior predictable and document the working directory and file contract.

**Worked example:** [studylog.py](../examples/studylog.py) combines CSV parsing,
validated records, a pure aggregator, sorting, and a CLI. Read its tests and contract
before the implementation. It retains records in memory; a streaming extension
still needs a policy against partial success output on later failure.

**Practice A:** Compare repeated linear membership checks with building a set
once. Explain when building the set costs more than it saves.

**Practice B:** Build [Capstone 2](../practice/CAPSTONES.md#capstone-2-study-report-application)
with a documented command and a new feature. Demonstrate a malformed later row.

**Hints:** State the observable contract before picking an algorithm. Run the
installed or launched program, not only isolated helper tests.

**Evidence:** Independent construction, failure handling, tests, setup, and a
short design explanation. Use the common phase rubric rather than a time quota.

**Sources:** [PY-ARGPARSE](../audit/SOURCES.md#py-argparse), [PY-HEAPQ](../audit/SOURCES.md#py-heapq).
