# Working glossary

Use this on demand; do not memorize it before programming. Definitions are scoped
to this course. Relevant primary references appear in each phase and the source map.

| Term | Meaning |
|---|---|
| Argument | A value supplied in a function call |
| Parameter | A name in a function's definition that receives an argument |
| Binding | An association between a name and an object |
| Identity | Which object a reference denotes, compared with `is` |
| Equality | A value comparison defined by the objects' behavior, usually using `==` |
| Mutation | A change to an existing object's state |
| Alias | Another reference to the same object |
| Shallow copy | A new outer object that can retain shared nested references |
| Scope | The context in which a name is resolved |
| Closure | A function with access to bindings from an enclosing scope |
| Iterable | An object from which an iterator can be obtained |
| Iterator | An object that advances through values and signals exhaustion |
| Generator | An iterator whose execution can suspend and resume around yielded values |
| Comprehension | A compact expression that constructs a collection from iteration |
| Exception | A signaled execution condition that transfers control to handling logic |
| Traceback | The recorded call context associated with an exception |
| Context manager | An object/protocol for controlled entry and exit around a block |
| Module | An importable unit of Python code or functionality |
| Package | An organization of importable modules; distribution terminology differs |
| Virtual environment | An isolated interpreter/package environment for a project |
| Contract | Specified inputs, outputs, effects, errors, and other expectations |
| Invariant | A property that must hold across the relevant operations |
| Oracle | A justified basis for deciding the expected result of a test |
| Regression test | A check intended to detect the return of a previous defect |
| Property test | A test of a general relationship across generated or varied inputs |
| Metamorphic relation | A justified relationship between outputs under an input transformation |
| Protocol | Required operations and expectations; typing Protocol models structural interfaces |
| Descriptor | An object that participates in attribute access through descriptor methods |
| Serialization | Encoding structured values for storage or transfer |
| Transaction | A grouping of changes with a specified commit/rollback policy |
| Idempotence | Repetition has the same intended effect as one application |
| Concurrency | Coordinating overlapping work |
| Parallelism | Executing work simultaneously on multiple execution resources |
| Backpressure | Slowing or rejecting production when downstream capacity is limited |
| Cancellation | A request to stop work with defined propagation and cleanup behavior |
| Profiling | Identifying where execution spends time or other resources |
| Benchmarking | Measuring performance under a stated workload and environment |
| Conditioning | A problem's sensitivity to perturbations in its inputs |
| Numerical stability | How an algorithm handles numerical errors under its assumptions |
| Experimental unit | The unit to which an independent treatment or replication applies |
| Data leakage | Information entering model development/evaluation through an invalid boundary |
| Verification | Checking implementation against its specification |
| Validation | Checking whether a model/specification is adequate for an intended use |
| ABI | The binary interface contract between compiled components |
| Transfer | Applying a learned skill in a changed task or context |
| Delayed review | An independent check on a later occasion to examine retention |

## Git and GitHub terms

Use these with the [companion lessons](github.md); the
[command reference](../practice/GITHUB_REFERENCE.md) explains effects and boundaries.

| Term | Working meaning |
|---|---|
| Repository | Project history and associated Git data; a working clone also has editable files |
| Working tree | Files currently checked out for editing |
| Index or staging area | Proposed next snapshot; later edits do not automatically restage themselves |
| Commit | Recorded snapshot, metadata, and parent references |
| HEAD | Reference to the current commit, usually through the checked-out branch |
| Branch | Movable reference naming a line of work |
| Remote | Named configuration identifying another repository |
| Remote-tracking branch | Local reference recording an observed remote branch state |
| Fetch | Receive objects and update references according to the fetch configuration |
| Pull | Fetch and integrate into the current branch according to the selected policy |
| Push | Request updates to references in a remote repository and transfer needed objects |
| Fork | Related repository under another account for independent work/contribution |
| Pull request | Proposal to bring a head branch's changes into a base branch |
| Conflict | Integration that requires an explicit content or structural resolution |
| Revert | New commit reversing changes from a selected earlier commit |
| Reflog | Local record of reference movements, subject to expiration |
| CI | Automated integration checks with a defined trigger, environment, and coverage |
| Release | Published version information and optional assets associated with a tag |
| Ruleset | Configured constraints on repository changes, with scope and availability limits |
