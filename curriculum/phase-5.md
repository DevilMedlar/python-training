# Phase 5 Creator

Create and sustain a useful contribution. “Creator” is an informal route, not a
credential. You can contribute documentation, tests, accessibility improvements,
or small fixes much earlier. The full route below assumes an expert foundation
and research evaluation skills; a narrow engineering project can use a tailored
route with its prerequisites checked explicitly.


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

## P5-01 Contribution value and novelty

**Workspace shortcut:** Use Explorer → New File to keep the contribution brief beside the prototype.

**Prerequisites:** P4-08.

**Outcome:** Define a worthwhile contribution without confusing novelty, complexity, and usefulness.

Personal rediscovery is excellent practice. An engineering contribution can add
value through reliability, integration, usability, portability, or cost even when
its algorithms are established. A research contribution needs an appropriately
original and supported result relative to prior knowledge. Creating a package
does not establish that its underlying idea is new.

Identify who benefits, what changes in their workflow, the credible alternatives,
and how the benefit could be evaluated. Prefer a small problem whose constraints
you understand over a broad framework with no clear user. A proposed project is
a hypothesis about value until evidence supports it.

**Worked example:** A data-validation tool may use known algorithms but prevent
one recurring, costly schema error. Its contribution can be evaluated by detected
failures, false alarms, integration effort, and a real user's ability to recover.

**Practice A:** Write a contribution brief with a target user, existing workflow,
failure, alternatives, proposed change, and measurable success criteria.

**Practice B:** Classify three candidate ideas as personal discovery, engineering,
or research contributions, explaining what additional evidence each needs.

**Hints:** Ask what becomes possible or easier after the change. Avoid using a
degree title or a package's size as the measure of quality.

**Evidence:** A scoped value claim, prior-work comparison, and a concrete way
for evidence to change the project direction.

**Sources:** [RESEARCH-PRACTICE](../audit/SOURCES.md#research-practice), [PEP-PROCESS](../audit/SOURCES.md#pep-process).

## P5-02 Public APIs and compatibility

**Workspace shortcut:** Use Ctrl+Shift+F to find callers affected by an interface change.

**Prerequisites:** P5-01.

**Outcome:** Design an interface other people can use and evolve without hidden assumptions.

Specify accepted inputs, output shape, errors, mutation, ownership, ordering,
resource use, and compatibility. Choose the smallest useful public surface. Two
independent implementations expose which requirements are essential and which
are accidental properties of your first implementation.

Plan deprecation and migration for behavior people may depend on. A type annotation
does not define all semantics. Avoid exposing every internal function as a permanent
promise. Decide what is stable and what remains experimental, and make the distinction
visible in user documentation.

**Worked example:** The selection lab specifies ordering, duplicate preservation,
integer inputs, invalid `k`, and nonmutation. Sorting and heap implementations
share that contract; speed is evaluated separately.

**Practice A:** Write a small public API and two implementations with shared
behavioral tests. Test empty input and one realistic failure.

**Practice B:** Propose a breaking change, then write a migration path and explain
how existing callers would discover and adopt it.

**Hints:** Write an example from a caller's perspective before designing internal
classes. Ask which behavior a user can reasonably rely on.

**Evidence:** Contract tests, an external-use example, and a compatibility decision
that states its cost. Do not promise support for untested builds or platforms.

**Sources:** [PY-TYPING](../audit/SOURCES.md#py-typing), [PY-PACKAGING](../audit/SOURCES.md#py-packaging).

## P5-03 Prototypes baselines and decision records

**Workspace shortcut:** Use the Split Editor button to compare baseline and candidate code while their tests run in Terminal.

**Prerequisites:** P5-02.

**Outcome:** Use a small prototype to compare alternatives and decide whether to continue.

Begin with a transparent reference implementation. Choose one candidate change
and a testable claim. Keep correctness checks outside benchmark timing, and account
for decision overhead if an adaptive strategy chooses between algorithms. Include
workloads that disadvantage the candidate, not only its demonstration case.

Record the decision's context, alternatives, evidence, costs, chosen action, and
revisit condition. A prototype is allowed to fail. Its value is the uncertainty
it resolves, including evidence that a simpler existing approach is sufficient.

**Worked example:** Compare sorting with heap selection across input families and
fractions of selected values. Before proposing an adaptive chooser, test whether
its rule generalizes to held-out families and whether choosing costs enough to matter.

**Practice A:** Add a new candidate to the benchmark harness without changing the
contract or favoring it with different inputs.

**Practice B:** Write a decision record that rejects your preferred implementation
when a documented constraint makes it unsuitable.

**Hints:** Name the strongest competing explanation of your observed improvement.
Measure the complete path users would run.

**Evidence:** Baseline, raw data, shared checks, an explicit decision, and known
limits. A benchmark harness does not establish novelty by itself.

**Sources:** [PY-HEAPQ](../audit/SOURCES.md#py-heapq), [PYPERF](../audit/SOURCES.md#pyperf).

## P5-04 Language runtime and tool creation

**Workspace shortcut:** Use Explorer to keep supported and unsupported syntax samples beside the tool you are building.

**Prerequisites:** P5-03.

**Route:** Optional specialist lab. The default core continues at P5-06.

**Outcome:** Investigate one language/tooling problem with a defined supported subset.

For a language tool, understand parsing, representations, name resolution, control
flow, diagnostics, and semantics. A detector for a pattern is not automatically
a sound analyzer of arbitrary Python. State supported constructs and the intended
balance between missed cases and false alarms. Build reviewed development and
evaluation cases, including ambiguous examples.

For runtime work, record the exact CPython revision and build. Learn the relevant
C, operating-system, memory, and concurrency behavior. Optional JIT, free-threaded,
and experimental builds have distinct constraints. Do not describe a proposal or
draft PEP as a feature already delivered to ordinary Python installations.

**Worked example:** A tiny expression representation supports ordinary evaluation
and operation counting. Its restricted language makes transformations inspectable.
Extending it to arbitrary Python introduces side effects and overloaded operations.

**Practice A:** Build the small representation and two evaluators, or a detector
for one precisely defined defect pattern. State excluded constructs.

**Practice B:** Find a plausible false positive or semantics-changing transformation
and make the tool expose its uncertainty or refuse unsupported input.

**Hints:** Compare with a simple reference before optimizing. A “safe rewrite”
must preserve the contract even when operations have user-defined behavior.

**Evidence:** A supported-subset specification, labeled cases, limitations, and
a mechanism-level explanation. This specialty is optional for other creator paths.

**Sources:** [PY-INSPECTION](../audit/SOURCES.md#py-inspection), [PY-314](../audit/SOURCES.md#py-314), [CPYTHON-CONTRIBUTING](../audit/SOURCES.md#cpython-contributing).

## P5-05 Scientific native and systems contributions

**Workspace shortcut:** Open the compatibility matrix and boundary tests side by side with Split Editor.

**Prerequisites:** P5-03.

**Route:** Optional specialist lab. Choose the investigation relevant to your project.

**Outcome:** Define the extra domain and interoperability evidence needed by a chosen specialty.

Choose one main path: scientific/numerical methods, native acceleration, machine
learning systems, distributed/data infrastructure, or developer tools. Specialization
creates prerequisites; it does not make all of them universal. Learn another language
or hardware model when the project needs it, not to satisfy an imagined mastery checklist.

At native boundaries, specify ownership, accepted layouts/dtypes, error propagation,
thread safety, and build/ABI compatibility. Include conversion and transfer costs.
For scientific methods, justify numerical tolerances, assumptions, convergence, and
domain validity. For distributed systems, define failures, duplicate handling,
recovery, and resource bounds.

**Worked example:** Accelerate one measured numerical kernel while retaining a
Python reference. Test tiny inputs, supported memory layouts, invalid values,
accuracy, and end-to-end cost. A fast kernel that corrupts a boundary case fails
the shared contract.

**Practice A:** Write a specialty prerequisite map and the smallest contribution
that can be evaluated without buying new infrastructure.

**Practice B:** Design a compatibility/validation matrix for a native, scientific,
or distributed component and identify a realistic case where it should be rejected.

**Hints:** Keep the boundary small enough to specify. Consider an upstream
improvement before starting another independently maintained package.

**Evidence:** Domain assumptions, an honest support matrix, boundary tests, and
measured value. Optional features remain unverified until their checks actually run.

**Sources:** [PY-EXTENSIONS](../audit/SOURCES.md#py-extensions), [JAX-BENCHMARK](../audit/SOURCES.md#jax-benchmark), [SCIPY-LINALG](../audit/SOURCES.md#scipy-linalg).

## P5-06 Independent evaluation and adversarial review

**Workspace shortcut:** Use Terminal → New Terminal to follow the first-use instructions and record actual failures.

**Prerequisites:** P5-03.

**Outcome:** Evaluate a contribution under conditions that can reveal its weaknesses.

Use credible baselines, matched constraints, unseen evaluation cases where relevant,
and failure tests. Ask an independent person to install or reproduce the work,
recording the help they needed. A second run by you in Codespaces is a self-directed
repeatability check, not independent external validation.

Separate implementation success, usability, engineering value, and research novelty.
Evidence supporting one does not automatically establish the others. Report
uncertainty, exclusions, failures, and conditions where the contribution loses.
Tests must challenge the advertised behavior rather than merely mirror the code.

**Worked example:** Evaluate a static analyzer on reviewed cases outside its
development set. Report both false positives and false negatives and clarify
ambiguous labels. Faster execution alone does not demonstrate better analysis.

**Practice A:** Have a reviewer propose one plausible counterexample to your
main claim. Test it or explain why it is outside a clearly justified scope.

**Practice B:** Reevaluate after replacing a weak baseline with a credible one.
Revise the claim if its apparent advantage disappears.

**Hints:** Ask what evidence would embarrass your preferred design, then include
an appropriate test of it. Do not quietly discard inconvenient runs.

**Evidence:** Reproducible evaluation, independent feedback or its explicit absence,
and a revised contribution claim with precise limits.

**Sources:** [RESEARCH-PRACTICE](../audit/SOURCES.md#research-practice), [HYPOTHESIS](../audit/SOURCES.md#hypothesis).

<a id="p5-07-releases-community-and-governance"></a>

## P5-07 Compatibility releases and maintenance

**Workspace shortcut:** Use Ctrl+P to open your compatibility tests, then rerun them in the workspace Terminal.

**Prerequisites:** P5-06.

**Outcome:** Prepare a Python package update with compatibility checks and clear migration guidance.

A useful update keeps existing callers working or clearly documents the change
they need. Keep representative old calls as tests. Check arguments, return values,
exceptions, saved-data formats, command options, and supported Python versions.
Make a focused change and rerun those checks in the workspace Terminal.

For a CPython contribution, use the current contributor documentation to understand
the required technical checks. A Python Enhancement Proposal records relevant
language changes; an ordinary package fix does not need one. For your package,
write concise migration notes and test the built wheel outside the source checkout.
Repository settings, licenses, and publishing controls are optional separate
[repository lessons](github.md).

**Worked example:** A review description states the observed bug, the input that
reproduces it, the corrected behavior, the regression check, and compatibility
effects. It does not declare a patch correct solely because an AI produced it.

**Practice A:** Prepare a release candidate with installation, first task,
troubleshooting, known limitations, and tested version/build information.

**Practice B:** Change one public function or saved-data format. Keep an old
caller or fixture as a regression check. Either preserve its behavior or provide
a tested migration path and a clear error for unsupported input.

**Hints:** Start with actual callers and data files. Run them against the updated
package instead of assuming a version number guarantees compatibility.

**Evidence:** A usable package update, compatibility results, and a working
migration example when the interface changes. Publishing is optional.

**Sources:** [CPYTHON-CONTRIBUTING](../audit/SOURCES.md#cpython-contributing), [PEP-PROCESS](../audit/SOURCES.md#pep-process), [PY-PACKAGING](../audit/SOURCES.md#py-packaging).

## P5-08 Maintenance mentoring and the creator capstone

**Workspace shortcut:** Use the Markdown preview button to review the first-use tutorial with its implementation beside it.

**Prerequisites:** P5-07.

**Outcome:** Make a useful contribution understandable and maintainable beyond its creator.

Write for three audiences: a user trying a first task, a maintainer changing a
component, and a reviewer evaluating a claim. Preserve design decisions and
known limitations. Keep supported scope realistic and define how bugs and
deprecations will be handled. Choose sustainable maintenance commitments.

When mentoring, let the learner make meaningful decisions. Ask them to state the
contract, reproduce a failure, propose a check, and explain the change. A handoff
that only works while you narrate every step reveals documentation or design gaps.
Teaching skill itself improves through evidence and revision.

**Worked example:** Another contributor installs a release, reproduces one result,
and makes a small tested modification using only the written materials. Record
where they needed help and revise that part of the project.

**Practice A:** Create a maintainer map and a short tutorial, then review them
against an unfamiliar reader's actual attempt.

**Practice B:** Complete [Capstone 5](../practice/CAPSTONES.md#capstone-5-useful-contribution).
Defend the contribution, demonstrate a failure case, and provide a maintenance plan.

**Hints:** Reduce scope until the whole lifecycle is credible. One well-supported
capability is more assessable than a long list of unfinished features.

**Evidence:** A usable contribution, evaluation, independent feedback where
available, handoff documentation, and honest limitations. Continued learning and
contribution do not depend on being assigned a final prestige label.

**Sources:** [CPYTHON-CONTRIBUTING](../audit/SOURCES.md#cpython-contributing), [RESEARCH-PRACTICE](../audit/SOURCES.md#research-practice).
