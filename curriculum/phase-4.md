# Phase 4 Researcher

Use Python to investigate a question whose answer is uncertain. This is a research
training route, not a PhD qualification. Research **with** Python and research
**on** Python require different specialist knowledge. Strengthen mathematical and
domain prerequisites alongside a narrow project rather than collecting tools.


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

## P4-01 Questions literature and scope

**Workspace shortcut:** Use Explorer → New File to save a short research protocol beside the experiment.

**Prerequisites:** P3-10.

**Outcome:** Form a tractable question and distinguish evidence gaps from unfamiliarity.

Specify the method, comparison, conditions, outcome, and intended population or
workload. “Learn a library” is an activity; “when does method A reduce time at the
same error tolerance?” is an investigable question. Separate descriptive,
predictive, causal, theoretical, and engineering-feasibility claims.

Read prior work for the actual claim, assumptions, method, data, baseline, metric,
limitations, and available artifact. Keep search dates and queries. An idea being
new to you does not establish novelty. Trace citations backward and look for later
replications or challenges; do not cite a generated summary as if you read its source.

**Worked example:** Compare mean and median squared error under two explicitly
defined symmetric distributions. The question is about performance under those
simulators, not whether either estimator is universally better.

**Practice A:** Write a one-page proposal with three relevant sources, a smallest
useful experiment, a primary outcome, costs, and evidence that would change your mind.

**Practice B:** Critique a claim that a method is “best” using its comparison and
scope. Rewrite it so a concrete experiment could support or refute it.

**Hints:** Name a counterexample you would accept. If none is possible, the claim
may be too vague to investigate.

**Evidence:** [The protocol template](../practice/RESEARCH_PROTOCOL.md), a literature
matrix, and a clear distinction between established knowledge and a proposed test.

**Sources:** [RESEARCH-PRACTICE](../audit/SOURCES.md#research-practice).

## P4-02 Mathematical and numerical validity

**Workspace shortcut:** Use the Split Editor button to keep the numerical method and its check visible together.

**Prerequisites:** P4-01.

**Outcome:** Identify the mathematical assumptions and numerical errors relevant to a result.

Learn linear algebra, probability, statistics, calculus, optimization, and numerical
analysis as required by the question. Distinguish a problem's conditioning
(sensitivity to input changes) from an algorithm's numerical stability. Separate
measurement, model, approximation, sampling, and floating-point errors.

For array work, state dimensions and axis meanings. A NumPy view can share data;
reshaping is not a guarantee of a view. Define dtype and handling of NaNs,
infinities, empty arrays, singular systems, and invalid inputs. Prefer solving a
linear system with an appropriate solver rather than explicitly forming an inverse
merely to multiply by its right-hand side.

**Worked example:** For a symmetric zero-centered mixture with probability `p`
of standard deviation 10 and otherwise standard deviation 1, variance is
`(1-p) * 1 + p * 100`. For `n` independent observations, the sample mean's MSE
for the true mean zero is that variance divided by `n`. This gives an analytical
check of a simulation, under its stated independence assumptions.

**Practice A:** Put the supplied formula in a Python function. Run it for
`p = 0` and `p = 0.1`, with `n = 100`, then use the computed values as checks on
a simulation. Document the formula's independence and distribution assumptions.

**Practice B:** Use a known-answer numerical problem, vary difficulty and precision,
and report residual and actual error separately. Choose meaningful tolerances.

**Hints:** Write the target quantity before choosing the estimator. A small
residual does not always imply a small solution error in a sensitive problem.

**Evidence:** A numerical implementation, a primary mathematical reference or
supplied analytical rule, observed checks, and a tolerance justified by the task.

**Sources:** [PY-FLOAT](../audit/SOURCES.md#py-float), [NUMPY-VIEWS](../audit/SOURCES.md#numpy-views), [SCIPY-LINALG](../audit/SOURCES.md#scipy-linalg).

## P4-03 Experimental units baselines and uncertainty

**Workspace shortcut:** Open the experiment configuration and analysis script in separate editor tabs.

**Prerequisites:** P4-02.

**Outcome:** Design a comparison whose uncertainty analysis matches its sampling units.

Declare the experimental unit: dataset, participant, independent trajectory,
machine, or another justified unit. Repeated observations from one unit may be
dependent. Repeated seeds on a single fixed dataset do not establish performance
across a population of datasets. Match tuning budgets, preprocessing, precision,
and stopping criteria when comparing methods; explain unavoidable differences.

Preserve pairing when two methods use the same units. Choose an uncertainty method
that respects dependence. A frequentist 95% interval refers to a procedure's
repeated-sampling coverage under assumptions; it is not generally a 95% posterior
probability that a fixed parameter is inside one observed interval. Bootstrap
methods can fail or be misleading for degenerate, dependent, or unsuitable samples.

**Worked example:** Compute each estimator's loss on the same simulated dataset,
subtract those losses, then estimate the mean of the paired differences. Resample
datasets or their paired differences, not independent pools of the two methods' losses.

**Practice A:** Identify units, pairing, baseline, primary metric, and exclusions
for a proposed benchmark before running it.

**Practice B:** Repair an evaluation that fits preprocessing to all data before
splitting. Use group-aware or time-aware splits if the domain requires them.

**Hints:** Ask what a newly sampled unit would mean. Do not treat a large row
count as proof of a large independent sample.

**Evidence:** An analysis plan, uncertainty assumptions, and an explanation of
what the design cannot establish, including causal or population-level claims.

**Sources:** [NIST-CI](../audit/SOURCES.md#nist-ci), [SCIPY-BOOTSTRAP](../audit/SOURCES.md#scipy-bootstrap), [SKLEARN-LEAKAGE](../audit/SOURCES.md#sklearn-leakage).

## P4-04 Reproducibility provenance and randomness

**Workspace shortcut:** Use Explorer to open the saved configuration and raw results from the same experiment run.

**Prerequisites:** P4-03.

**Outcome:** Regenerate a result from recorded inputs, code, configuration, and environment.

Keep raw inputs or authoritative retrieval instructions, transformations, resolved
parameters, code commit/dirty state, software versions, and raw measurements.
Specify whether agreement means identical bytes, numeric agreement within a
tolerance, or a consistent scientific conclusion. A lock file helps specify
dependencies but cannot record every hardware, external-data, or runtime effect.

Give stochastic tasks stable identities and explicit generators. NumPy's
`SeedSequence` supports well-separated streams with very high probability; it is
not a proof of every desired independence property. A seed alone cannot promise
bitwise agreement across all builds, devices, algorithms, or library versions.
Restart notebooks and execute in order to test whether current cells reproduce
displayed results.

**Worked example:** The optional [research lab](../examples/research_optional.py)
maps scenario and replication IDs to random streams. It preserves per-replication
losses and software/configuration metadata. Its manifest is deliberately incomplete
until you also capture code identity and the external execution environment.

**Practice A:** Rerun a small experiment and compare outputs under a declared
agreement criterion. Then change task order and verify stable task results.

**Practice B:** Reproduce one result in a fresh virtual environment inside
Codespaces using only the written procedure. Record missing assumptions and repair
the instructions. External independent reproduction is an optional stronger check.

**Hints:** Keep each reported number linked to its raw measurement and input.
Record task-to-stream assignment as well as the root seed.

**Evidence:** A fresh rerun, provenance record, discrepancy log, and explicit
cross-platform limits. Do not claim independent reproduction from one local rerun.

**Sources:** [NUMPY-RANDOM](../audit/SOURCES.md#numpy-random), [RESEARCH-PRACTICE](../audit/SOURCES.md#research-practice).

## P4-05 Verification validation and scientific tests

**Workspace shortcut:** Ctrl+click the Terminal failure location to open the scientific test that needs repair.

**Prerequisites:** P4-04.

**Outcome:** Test whether the implementation follows its specification and whether
the specification supports the intended investigation.

Verification asks whether the implementation meets its stated rules. Validation
asks whether the model and rules are suitable for their intended use. A correct
implementation of an unsuitable model can still produce a misleading conclusion.

Use supplied known-answer cases, independent oracles, invariants, metamorphic relations,
convergence checks, and fault injection when justified. Shared dependencies can
give two implementations the same bug. A property test is only as meaningful as
its property and input domain. Do not require every random realization to look
typical; that creates false failures instead of a sound stochastic test.

**Worked example:** Translation of all observations by a constant should translate
a location estimate by the same constant, under the estimator's defined contract.
That relation may detect a normalization bug without knowing every exact answer.

**Practice A:** Add known-answer and metamorphic checks to a small numerical method.
Document tolerances and behavior for invalid or degenerate input.

**Practice B:** Introduce a swapped axis, state-sharing error, or leakage bug and
determine which checks detect it. Improve the missing check before celebrating coverage.

**Hints:** Choose a plausible wrong implementation and ask whether your tests
would accept it. A saved output can preserve an old mistake.

**Evidence:** Detected scientific defects, defensible oracles, and the remaining
distance between implementation correctness and domain validity.

**Sources:** [HYPOTHESIS](../audit/SOURCES.md#hypothesis), [NUMPY-VIEWS](../audit/SOURCES.md#numpy-views).

## P4-06 Performance scaling and computational budgets

**Workspace shortcut:** Use the Terminal plus button for a bounded performance run and Explorer for its saved measurements.

**Prerequisites:** P4-05.

**Outcome:** Evaluate computational cost under equivalent accuracy and workload conditions.

Report what is timed: initialization, data loading, compilation, host/device
transfer, kernel execution, synchronization, and postprocessing. GPU or JIT
execution can be asynchronous, so timing dispatch alone can miss the actual work.
Separate cold and warmed execution when they answer different user questions.

Vectorization can remove Python overhead while creating expensive temporary
arrays. Native loops, GPUs, task schedulers, or distributed execution add setup,
communication, and maintenance costs. Use them only when the workload and measured
bottleneck justify them. Include memory, failures, and cases where scaling loses.

**Worked example:** Compare a repeated numerical kernel and the complete workflow
that moves data to it. A kernel speedup may disappear once transfer or compilation
costs are included. Consult the chosen framework's synchronization documentation.

**Practice A:** Profile one workload and compare a clear baseline against one
change across several sizes at the same correctness or accuracy target.

**Practice B:** Define a limited scaling study with explicit hardware, worker
counts, per-worker work, and communication accounting. Explain the unit of replication.

**Hints:** Keep accuracy and cost on the same comparison table. Do not silently
give the new method looser tolerances or better hardware.

**Evidence:** Raw trials, scope, environment, correctness checks, and a bounded
conclusion. The curriculum does not require buying accelerator hardware.

**Sources:** [JAX-BENCHMARK](../audit/SOURCES.md#jax-benchmark), [PYPERF](../audit/SOURCES.md#pyperf).

## P4-07 Scientific communication and critique

**Workspace shortcut:** Use the Markdown preview button to inspect your report alongside the source text.

**Prerequisites:** P4-06.

**Outcome:** Write a report in which claims, methods, results, and limits can be inspected.

Explain the question and why the comparison answers it. Describe data provenance,
methods, units, preprocessing, metrics, uncertainty, failures, and deviations from
the original plan. Distinguish observations from interpretations and exploratory
findings from planned tests. A negative or inconclusive result can still be useful.

Make figures and tables traceable to scripts and raw records. Label axes, units,
sample sizes, and uncertainty meaning. Preserve exclusions and failed runs with
reasons. Do not choose only favorable seeds or workloads. Cite the actual primary
sources you inspected and state when an artifact was inaccessible.

**Worked example:** “The median had lower estimated MSE in this particular
zero-centered contaminated simulation” is narrower and more defensible than
“the median is better for real data.” An interval about Monte Carlo uncertainty
does not include every uncertainty about the real world.

**Practice A:** Write a short methods-and-results report for the research lab,
including the sign of the paired difference and the analytical check.

**Practice B:** Critique a peer-style report by identifying its strongest claim,
the evidence supporting it, one alternative explanation, and a follow-up test.

**Hints:** Replace vague adjectives such as “robust” with the tested failure
conditions. Keep results that challenge your preferred explanation.

**Evidence:** A report another learner can reproduce and challenge without
private instructions. Teach back a limitation without overstating certainty.

**Sources:** [RESEARCH-PRACTICE](../audit/SOURCES.md#research-practice), [NIST-CI](../audit/SOURCES.md#nist-ci).

## P4-08 Replication and the research capstone

**Workspace shortcut:** Use Ctrl+P to open the reproduction instructions, then run their commands in the workspace Terminal.

**Prerequisites:** P4-07.

**Outcome:** Complete one bounded investigation with reproducible evidence and an honest conclusion.

Choose a published result with accessible artifacts and affordable computation,
or a clearly labeled teaching experiment. Reproduce a small part before adding a
new method. Record discrepancies in configuration, environment, data, and results.
Do not convert unsuccessful setup into a claim that the paper is false.

An extension should change one meaningful factor and retain a credible baseline.
State what would count as agreement, disagreement, or insufficient evidence.
Research novelty requires more than implementing an established algorithm in Python.
For domain-sensitive conclusions, seek appropriate domain review rather than
treating programming competence as expertise in every subject.

**Worked example:** Extend the paired estimator experiment with a prespecified
third distribution. Retain individual losses, choose the inference plan before
seeing final results, and distinguish a teaching extension from an original finding.

**Practice A:** Reproduce the supplied lab and its analytical mean-MSE expectation.
Explain numeric discrepancies and why two reruns need not prove universal portability.

**Practice B:** Complete [Capstone 4](../practice/CAPSTONES.md#capstone-4-reproducible-investigation),
including an independent rerun or an explicitly uncompleted rerun request.

**Hints:** Shrink the research claim before expanding the tool stack. A complete
small study is easier to assess than an unfinished broad research agenda.

**Evidence:** Protocol, code, environment, raw records, tests, report, and a
defensible response to critique. Admission, publication, and degrees are separate matters.

**Sources:** [RESEARCH-PRACTICE](../audit/SOURCES.md#research-practice).
