# Phase 3 Expert practice

Develop dependable judgment about language behavior, system boundaries, failure,
and measurement. This route is not equivalent to a master's degree. Use a
continuing package or service and produce evidence as you improve it. Each lesson
includes both an investigation and a transfer task; do not turn the course into
memorization of advanced vocabulary.


Work in [your Codespaces workspace](https://supreme-fishstick-5g5gxqwrgjrpcp777.github.dev/).
The tutor explains every objective, concept, syntax rule, and common error in the
lesson before giving program requirements. The learner writes the entire program
from a blank file, or all new code in their own project. Reference snippets illustrate
concepts; they are not prefilled assignment answers. Run learner-authored code and
type `input()` answers in the workspace Terminal.
Placement adjusts teaching depth and practice without skipping lessons. Occasional
quizzes and cumulative reviews revisit taught topics. Complete a phase-end test
using [the assessment plan](../practice/ASSESSMENT.md#tests-at-the-end-of-each-phase).
Each lesson includes one short workspace control; repository administration is
optional material outside this Python sequence. See [workspace controls](../practice/BROWSER_WORKFLOW.md).

## P3-01 Protocols descriptors and object behavior

**Workspace shortcut:** Use Ctrl+P to switch between the protocol implementation and its contract tests.

**Prerequisites:** P2-12.

**Outcome:** Explain attribute lookup and implement a small, lawful Python protocol.

Study special methods for length, iteration, indexing, equality, hashing, and
operators. Equal hashable objects must have equal hashes; key-relevant state must
remain stable during use as a dictionary key. An unsupported operator may return
`NotImplemented` to permit the other operand's handling. It is not the same as
raising `NotImplementedError`, and its truth testing changes in Python 3.14.

Under ordinary instance lookup, a data descriptor on a class precedes the instance
dictionary; the instance dictionary precedes a non-data descriptor. Custom lookup
can alter this. Properties and bound methods become understandable through these
rules. Learn method resolution order and cooperative `super` with tiny examples
before designing a multiple-inheritance hierarchy.

```python
class Label:
    @property
    def name(self):
        return "from property"

item = Label()
item.__dict__["name"] = "from instance"
print(item.name)
```

```output
from property
```

**Practice A:** Run small examples of a data descriptor, a non-data descriptor,
and an instance attribute with the same name. Change each example and inspect
which value Python returns.

**Practice B:** Build a small read-only sequence wrapper and test indexing,
iteration, empty input, and caller expectations. Explain when a built-in is simpler.

**Hints:** Start from the property example above and run each variation. Separate
“cannot reassign this field” from “nothing reachable through this object can mutate.”

**Evidence:** Correct protocol behavior and an explanation of a broken hash or
lookup contract without relying on implementation accidents.

**Sources:** [PY-MODEL](../audit/SOURCES.md#py-model), [PY-DESCRIPTOR](../audit/SOURCES.md#py-descriptor).

## P3-02 Closures decorators and caches

**Workspace shortcut:** Use Ctrl+Shift+F to find every caller of the wrapper or cache you are changing.

**Prerequisites:** P3-01.

**Outcome:** Preserve a callable's contract and justify any retained state.

A wrapper must preserve intended arguments, results, exceptions, metadata, and
lifetime. `functools.wraps` helps introspection but does not automatically make an
arbitrary wrapper semantically equivalent to its target. A synchronous wrapper
around an async function measures coroutine creation unless it awaits the work.

For caching, specify key identity, invalidation, bounded size, retention, and
concurrent misses. A thread-safe cache can still compute the same missing key
more than once. Caching coroutine objects or exhausted generators as reusable
results is usually the wrong abstraction. Closures, callbacks, and caches can
keep large objects alive.

**Worked example:** Inspect [contracts.py](../examples/contracts.py). Its
`timed` decorator uses a caller-supplied sink and `finally`; its tests cover metadata,
keyword arguments, return values, and a target failure. Timing placement is the
lesson, not a claim that one short duration is a trustworthy benchmark.

**Practice A:** Implement a metadata-preserving wrapper that records an event on
both successful and failing calls while preserving the target's exception.

**Practice B:** Design an asynchronous version and a cache policy for a changing
data source. Include a case where caching would return stale or unusable results.

**Hints:** Name every retained reference. Ask when the underlying operation starts
and finishes, especially for generators and coroutines.

**Evidence:** A contract test, a lifetime explanation, and a reason to reject or
bound a cache. Document whether the reporting sink is allowed to fail.

**Sources:** [PY-FUNCTOOLS](../audit/SOURCES.md#py-functools), [PY-ASYNC](../audit/SOURCES.md#py-async).

## P3-03 Advanced typing and API boundaries

**Workspace shortcut:** Use View → Problems for static diagnostics and the Terminal for runtime test results.

**Prerequisites:** P3-02.

**Outcome:** Express meaningful generic relationships without inventing runtime guarantees.

Study protocols, generics, variance, overloads, narrowing, callable signatures,
and gradual typing through real interfaces. `ParamSpec` can preserve a relationship
between a wrapped function's parameters and its wrapper. A narrowing predicate
is a promise to a checker; incorrect promises can conceal errors. Verify the
availability and semantics of newer typing features for the target interpreter
and chosen checker.

Python 3.14 changes default annotation evaluation to deferred evaluation. Tools
that inspect annotations must choose a format and account for evaluation effects.
Evaluating annotations from untrusted code may execute code. Version-aware
introspection is an advanced concern, not a beginner setup requirement.

**Worked example:** A storage protocol exposes `get(code) -> Item | None`.
Two implementations satisfy the interface, but only behavior tests can check
whether they return the correct item, preserve failures, or meet a latency bound.

**Practice A:** Type a wrapper and two interchangeable storage implementations;
introduce one incompatible signature and observe a checker diagnostic.

**Practice B:** Validate an external payload before constructing typed domain
objects. Explain why a cast or `TypedDict` declaration cannot replace validation.

**Hints:** State the relationship between input and output types first. Use the
smallest interface the caller actually needs; avoid hiding everything behind `Any`.

**Evidence:** Actual static-check results when a checker is available, runtime
boundary tests, and a documented limitation of the type system used.

**Sources:** [PY-TYPING](../audit/SOURCES.md#py-typing), [PY-ANNOTATIONS](../audit/SOURCES.md#py-annotations).

## P3-04 Runtime memory and inspection

**Workspace shortcut:** Open Terminal → New Terminal for the runtime inspection commands and keep its version output.

**Prerequisites:** P3-03.

**Outcome:** Separate language guarantees from observations about a particular runtime.

Use `ast` and `dis` to inspect how Python represents source and compiled code.
Bytecode is version-dependent; do not ship a cross-version contract based on an
observed instruction sequence. Reference counting and cyclic collection are
CPython mechanisms, not a language-wide guarantee of immediate cleanup.

Measure retained objects as well as allocation volume. `sys.getsizeof` is shallow;
it is not the total memory of everything reachable from an object. `tracemalloc`
tracks Python allocations and cannot stand in for all process or device memory.
Investigate growing caches, closures, exception tracebacks, and callbacks before
labeling every rise in memory a runtime leak.

**Worked example:** Create a cache retaining a large synthetic value, hold a weak
reference where supported, remove owners, and observe lifetime in your interpreter.
Report which observation is build-specific and why a file still needs explicit cleanup.

**Practice A:** Run `ast.dump` and `dis.dis` on a small expression to inspect
Python's generated representations. Record the interpreter version, change the
expression, and rerun the tools to compare their output.

**Practice B:** Compare repeated allocation with retained allocation and measure
both Python allocation data and a clearly labeled process-memory metric if available.

**Hints:** Add and remove one retained reference at a time and measure the
result. A variable disappearing does not imply the object has no other references.

**Evidence:** A minimal reproducer, version/build metadata, and a bounded claim
about what the measurement tool actually observes.

**Sources:** [PY-MODEL](../audit/SOURCES.md#py-model), [PY-INSPECTION](../audit/SOURCES.md#py-inspection), [PY-MEMORY](../audit/SOURCES.md#py-memory).

## P3-05 Algorithms profiling and fair benchmarks

**Workspace shortcut:** Use Explorer to open the saved benchmark results beside your implementation.

**Prerequisites:** P3-04.

**Outcome:** Identify a limiting cost and evaluate an optimization without changing the contract.

Profile a representative application before timing a convenient helper. Distinguish
latency, throughput, startup, steady state, allocations, and peak retained memory.
Record workload families, sizes, setup costs, interpreter/build, and raw trials.
Compare correctness before speed. A faster result produced by doing less required
work is a contract change, not an optimization of the same task.

Selecting a small number of values with a heap can be useful; sorting may be
preferable when requesting most values. The crossover depends on data and costs.
Use repeated trials and preserve results. For stronger performance evidence,
learn calibrated tooling such as pyperf rather than interpreting one stopwatch run.

**Worked example:** [selection.py](../examples/selection.py) contains a sorting
oracle and a heap candidate. [benchmark_selection.py](../examples/benchmark_selection.py)
records trial order and raw durations, checks agreement outside timing, and makes
no universal speedup claim.

**Practice A:** Compare both methods on empty, sorted, reversed, and duplicate-heavy
inputs across several `k` values before measuring them.

**Practice B:** Investigate two size regimes where a proposed optimization helps
and loses. Include input acquisition when users pay that cost.

**Hints:** State what the timer includes. Separate independent workload variation
from repeatedly timing the same workload.

**Evidence:** A baseline, correctness evidence, raw data, an interpretation, and
specific limits. Do not turn local timing results into a universal ranking.

**Sources:** [PY-HEAPQ](../audit/SOURCES.md#py-heapq), [PYPERF](../audit/SOURCES.md#pyperf).

## P3-06 Threads processes and isolated interpreters

**Workspace shortcut:** Use the Terminal plus button for a separate bounded concurrency run; Ctrl+C interrupts it.

**Prerequisites:** P3-05.

**Outcome:** Choose a concurrency mechanism based on work, ownership, and transfer costs.

Concurrency coordinates overlapping work; parallelism executes work simultaneously.
On conventional GIL-enabled CPython, threads do not generally run CPU-bound Python
bytecode in parallel, although I/O and native code that releases the GIL change
the picture. Processes add startup and serialization costs. Python 3.14's
`InterpreterPoolExecutor` uses separate interpreter state and has its own transfer
and compatibility constraints.

Optional free-threaded CPython is supported in 3.14; this does not mean every
ordinary installation lacks a GIL or every extension supports the build. Imports
can cause the GIL to be enabled. Protect compound invariants explicitly. In 3.14,
`fork` is no longer the default multiprocessing start method on any platform;
use importable workers and a main guard, and verify the platform's actual method.

**Worked example:** A tiny CPU task may run slower in a process pool after worker
startup and data transfer. An I/O-bound task may benefit from overlapping waits.
Neither observation decides every workload.

**Practice A:** Compare sequential execution and one suitable pool using synthetic,
bounded work. Separate setup time from steady-state work.

**Practice B:** Design ownership for a shared counter and its related status field;
test the invariant under concurrency rather than relying on accidental atomicity.

**Hints:** Name what is shared, copied, or serialized. Record the actual build
and GIL state before making a claim about thread parallelism.

**Evidence:** Correctness, startup/transfer accounting, and supported-platform
limits. A 3.14-only investigation is separate from core 3.12 compatibility tests.

**Sources:** [PY-FREE-THREADING](../audit/SOURCES.md#py-free-threading), [PY-EXECUTORS](../audit/SOURCES.md#py-executors), [PY-PROCESSES](../audit/SOURCES.md#py-processes).

## P3-07 Async work bounds and cancellation

**Workspace shortcut:** Keep the running Terminal visible and use Ctrl+C to exercise the program's interruption handling.

**Prerequisites:** P3-06.

**Outcome:** Bound a pipeline's tasks, queue, and retained results and prove cleanup.

`async` does not turn blocking or CPU-intensive code into parallel work. Coroutines
cooperate by yielding control. Use a fixed worker count and a bounded queue when
the input can grow. A semaphore can bound concurrent operations while millions
of pre-created tasks still consume memory. Audit every queue, buffer, task, and
result collection.

`TaskGroup` manages related tasks and propagates failures using defined grouped
exception semantics. An ordinary child failure generally cancels siblings; task
cancellation has special handling. Cleanup belongs in `finally` or context managers.
Do not swallow `CancelledError` casually; it can break structured concurrency.
An application timeout does not establish the outcome of a remote side effect.

**Worked example:** [pipeline.py](../examples/pipeline.py) uses a bounded queue,
fixed consumers, worker subtotals, and a `TaskGroup`. Its arithmetic is deliberately
simple: the example demonstrates lifecycle and memory structure, not CPU speedup.

**Practice A:** Instrument a bounded pipeline to record its largest queue and
owned-task count during a small run. Compare those measurements with a
one-task-per-item implementation using a semaphore, then fix the unbounded design.

**Practice B:** Make one worker fail and cancel another run while production is
blocked. Verify completion under a deadline and no owned unfinished tasks.

**Hints:** Include the producer in the same structured lifetime as consumers.
Consider what unblocks it when a consumer fails.

**Evidence:** Success, empty input, invalid workload, worker failure, cancellation,
and cleanup checks. Do not treat a successful happy-path run as sufficient.

**Sources:** [PY-ASYNC](../audit/SOURCES.md#py-async), [PY-QUEUES](../audit/SOURCES.md#py-queues).

## P3-08 Transactions retries and distributed uncertainty

**Workspace shortcut:** Use the Split Editor button to compare the transaction function with its failure tests.

**Prerequisites:** P3-07.

**Outcome:** Protect an invariant across failures and identify uncertain remote outcomes.

Specify what an operation commits and when a caller can know its result. A
transaction can commit while an acknowledgment is lost. Retrying without a stable
operation identity can repeat an effect. Idempotency means repeating an operation
has the same intended effect; it does not require identical responses every time.

Use constraints, conditional updates, unique operation IDs, and explicit
transaction boundaries where appropriate. A local transaction does not automatically
make a database change and a remote message atomic together. Study an outbox,
deduplication, and recovery only after writing the actual failure model. “Exactly
once” needs a precise scope and assumptions, not a slogan.

**Worked example:** The inventory lab checks and decrements stock in one SQL
statement. It prevents a particular negative-stock race but does not solve duplicate
reservations, lost replies, service authorization, or distributed transactions.

**Practice A:** Add an operation identifier and unique constraint to a synthetic
reservation flow. Define and test the response to the same identifier twice.

**Practice B:** Model commit success followed by a lost acknowledgment. Explain
how a retry queries or deduplicates the previous operation without double-applying it.

**Hints:** Enumerate failure points before coding retries. Separate “no reply”
from “no effect,” and retry only within a finite budget.

**Evidence:** A failure table, an invariant, recovery tests, and an explicit
boundary around what the implementation guarantees.

**Sources:** [PY-SQLITE](../audit/SOURCES.md#py-sqlite), [HTTP-SEMANTICS](../audit/SOURCES.md#http-semantics).

## P3-09 Architecture security and operations

**Workspace shortcut:** Use Ctrl+Shift+F to locate the application boundary named by a diagnostic message.

**Prerequisites:** P3-08.

**Outcome:** Make a system's rules, dependencies, and failure signals understandable.

Separate domain calculations from I/O where it makes behavior easier to inspect.
Use explicit dependencies for time, storage, randomness, and remote calls. Patterns
such as adapters or service layers must justify their extra indirection. A small
public API with clear ownership is often easier to maintain than a broad framework.

Treat loaded code and serialized data as different trust boundaries. Unpickling
untrusted data can execute code; parsing JSON does not make every payload valid or
cheap to process. Bound inputs and review path handling. Use parameterized SQL and
document subprocess argument interpretation instead of assembling untrusted shell
commands. Logs, metrics, and traces answer different operational questions.

**Worked example:** A runbook starts with a symptom, expected signals, a minimal
diagnostic command, and a reversible recovery step. It contains enough context for
another maintainer to investigate without your private recollection.

**Practice A:** Refactor a tightly coupled application boundary and show which
test becomes simpler. Reject an abstraction that adds no useful flexibility.

**Practice B:** Inject a storage failure into a synthetic service. Use its signals
to identify the failure and document graceful shutdown and recovery.

**Hints:** Run a small failing input at each trust boundary and inspect the
available diagnostic. Make the message useful enough to locate the failure.

**Evidence:** A design comparison, failure evidence, useful diagnostics, and a
runbook that identifies limits rather than promising universal security.

**Sources:** [PY-PICKLE](../audit/SOURCES.md#py-pickle), [PY-SUBPROCESS](../audit/SOURCES.md#py-subprocess), [PY-LOGGING](../audit/SOURCES.md#py-logging).

## P3-10 Reliable delivery and specialization

**Workspace shortcut:** Use Terminal → New Terminal for a clean-environment install and run the documented first task there.

**Prerequisites:** P3-09.

**Outcome:** Deliver an expert-level project with independent evidence and a clear specialty route.

Test the artifact you distribute, including package data, command entry points,
and supported versions. Keep platform/build claims narrower than your actual
checks. Record migration behavior and known limitations. A passing test suite,
type checker, or full coverage report supports specific conclusions; none proves
all possible behavior correct.

Choose one specialty: backend services, scientific/numerical computing, runtime
and compiler work, developer tools, or data systems. Native code, GPU programming,
advanced statistics, and distributed execution become requirements only when the
project needs them. They are not universal badges of Python expertise.

**Worked example:** A bounded ingestion system accepts synthetic records, validates
them, processes work under memory limits, and either commits or reports failure
under a documented policy. Its evidence includes a corrupted record, worker
failure, interruption, and clean installation.

**Practice A:** Build your project's wheel in Codespaces, install it into a
fresh virtual environment there, and run its first task from a temporary directory
outside the source checkout.

**Practice B:** Complete [Capstone 3](../practice/CAPSTONES.md#capstone-3-bounded-processing-system),
defend two design choices, and demonstrate a new failure chosen by the tutor.

**Hints:** Identify the shipped artifact before choosing validation commands.
Write the limitations while the experiment's assumptions are still visible.

**Evidence:** Contract, tests, failure behavior, measurements, delivery instructions,
and a teach-back. Choose a research or creator route by interest and prerequisites.

**Sources:** [PY-PACKAGING](../audit/SOURCES.md#py-packaging), [PY-UNITTEST](../audit/SOURCES.md#py-unittest).
