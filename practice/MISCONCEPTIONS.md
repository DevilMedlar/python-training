# Misconception and debugging guide

Use these as hypotheses to investigate. Do not diagnose a learner from one wrong
answer. Show the correct technique, run a small example, then help the learner
repair their code and rerun it. The source drafts already correctly identified many of these traps.

| Observed assumption | More accurate rule | Diagnostic or repair |
|---|---|---|
| Assignment creates a live formula | The right side is evaluated at assignment time | Rebind an input after computing a result |
| Input is automatically numeric | `input` returns a string | Compare adding before/after conversion |
| `//` truncates toward zero | Built-in numeric floor division floors | Run negative-division examples and inspect Python's results |
| Strings can be changed at an index | Strings are immutable | Compare a new string with the original |
| `range` includes its stop | The stop is excluded | Print `list(range(...))` for zero-length and descending ranges |
| The accumulator belongs inside the loop | Initialization usually precedes accumulation | Move the initialization and compare the actual totals |
| Printing supplies a function result | Printing and returning are different effects | Assign the call's result and inspect it |
| Assigning or slicing deep-copies a list | Assignment aliases; shallow copies share nested objects | Mutate an inner list through a copy |
| A tuple/frozen dataclass deeply freezes its contents | Referenced mutable contents can still change | Store a list and mutate that list |
| Default lists are new for each call | Defaults are evaluated at definition time | Compare two omitted-default calls |
| `is` tests numeric equality | It tests identity | Use separately created equal containers |
| A valid JSON document is valid application data | Shape and domain rules need separate checks | Load an object where a duration list is required |
| `isinstance(True, int)` rejects booleans | `bool` subclasses `int` | Apply an exact integer contract where appropriate |
| An annotation validates input | Ordinary annotations are not runtime guards | Construct an invalid typed record |
| A generator guarantees constant total memory | Downstream buffers and retained results matter | Add a list-collecting stage |
| A connection's context manager closes it | SQLite transaction context and connection lifetime differ | Test explicit close separately |
| The GIL prevents all races | Compound application invariants still need synchronization | Interleave read/modify/write steps |
| Python 3.14 means every build has no GIL | Free-threaded builds are optional; compatibility matters | Record the actual runtime configuration |
| A semaphore bounds every resource | Task creation, queues, and retained results need bounds too | Compare two pipeline architectures |
| A timeout means no remote write occurred | The remote outcome can be uncertain | Model lost acknowledgment after commit |
| A seed makes every environment identical | Algorithm/build/platform details can change results | State a reproducibility criterion |
| A 95% confidence interval gives a posterior probability | Frequentist coverage describes the procedure under assumptions | Identify the parameter and repeated experiment |
| Many rows mean many independent replications | Dependence and unit definitions matter | Identify clusters, datasets, or trajectories |
| An optimization must be better everywhere | Workload and cost boundaries determine benefit | Include a losing case |
| High coverage or passing tests proves perfection | Tests cover particular observations | Construct a plausible surviving defect |
| Finishing a phase grants degree equivalence | These phases are informal skill routes | Request demonstrated work, not a prestige label |
