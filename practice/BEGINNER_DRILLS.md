# Fifty beginner drills

Adapted from the supplied Phase 1 guide. Use these for extra practice and delayed
review after the listed prerequisite. The original numbering is retained; the
order is not a second syllabus. Tasks involving retry loops wait until exception
handling, and initials wait until iteration has been taught.

State input rules, attempt the task, check a normal and boundary case, and explain
one change to the input. These examples are acceptance checks, not full solutions.
For drills that use functions, return results unless the task explicitly asks
for display or interaction. Use disposable data for file exercises.

| Drill | Earliest lesson | Task | Check or requirement |
|---|---|---|---|
| D01 | P1-01 | Print a two-line introduction to your practice program | Exactly two output lines |
| D02 | P1-03 | Store a topic and a minutes value; print a labeled sentence | `loops`, `25` → `Practiced loops for 25 minutes.` |
| D03 | P1-02 | Reassign a counter twice and trace its values | Begin at 2, add 3, double it → 10 |
| D04 | P1-04 | Convert a numeric string and add 7 | `"18"` → 25 |
| D05 | P1-02 | Display the types of five different values | Include `"False"`, `False`, and `None` |
| D06 | P1-02 | Calculate a rectangle's area and perimeter | Width 4, height 7 → area 28, perimeter 22 |
| D07 | P1-02 | Convert nonnegative whole minutes to hours and remaining minutes | 135 → 2 hours, 15 minutes; 0 → 0 and 0 |
| D08 | P1-02 | Convert Celsius to Fahrenheit | 0 → 32; 100 → 212 |
| D09 | P1-02 | Compute the mean of three supplied numbers | 3, 6, 9 → 6 |
| D10 | P1-03 | Format a number to two decimal places | `2.5` → text `2.50` |
| D11 | P1-03 | Strip outside whitespace and lowercase a topic | `"  LoOps  "` → `"loops"` |
| D12 | P1-07 | Produce uppercase initials from a nonempty name | `"ada lovelace"` → `"AL"`; ignore repeated spaces |
| D13 | P1-03 | Count whitespace-separated tokens | `"one  two\nthree"` → 3; empty text → 0 |
| D14 | P1-03 | Replace every exact `"cat"` substring with `"dog"` | `"cat cat"` → `"dog dog"`; case-sensitive |
| D15 | P1-03 | Check for a `.py` suffix | `"lesson.py"` → true; `"lesson.txt"` → false |
| D16 | P1-05 | Identify an integer as even or odd | 0 is even; -3 is odd |
| D17 | P1-05 | Label a score as passing at 70 or above | 69 fails; 70 passes |
| D18 | P1-05 | Check that a number lies from 0 through 100 inclusive | -1 false, 0 true, 100 true, 101 false |
| D19 | P1-05 | Accept `yes` or `y` after stripping and lowercasing | `" Y "` true; `"no"` false |
| D20 | P1-05 | Find the largest of three numbers using conditions | Include ties and negative numbers |
| D21 | P1-06 | Print integers from 1 through 10 | Include both endpoints |
| D22 | P1-06 | Print even integers from 2 through 20 | Ten output values |
| D23 | P1-06 | Sum integers from 1 through a nonnegative integer `n` using a loop | 5 → 15; 0 → 0 |
| D24 | P1-07 | Read words until the user enters `quit` | Do not add the sentinel to the result list |
| D25 | P1-10 | Keep asking until the user supplies a whole number | `hello`, `2.5`, `8` → accept 8 |
| D26 | P1-07 | Filter a list to its positive values | `[-2, 0, 3, 5]` → `[3, 5]` |
| D27 | P1-07 | Demonstrate `.append()` versus `.extend()` | Explain the shape of each resulting list |
| D28 | P1-07 | Remove all zero values by constructing a new list | `[0, 1, 0, 2]` → `[1, 2]` |
| D29 | P1-07 | Unpack a coordinate tuple and describe each value | `(4, 9)` → `x=4`, `y=9` |
| D30 | P1-07 | Remove duplicate strings while keeping first-appearance order | `['a', 'b', 'a', 'c']` → `['a', 'b', 'c']` |
| D31 | P1-07 | Look up a topic score with a default of zero | A missing topic returns 0 |
| D32 | P1-07 | Count exact whitespace-separated words | `"red blue red"` → `{'red': 2, 'blue': 1}` |
| D33 | P1-07 | Increase an inventory count in a dictionary | Existing 3 plus 2 → 5; missing item plus 2 → 2 |
| D34 | P1-07 | Invert a dictionary whose values are unique strings | `{'a': 'red', 'b': 'blue'}` → `{'red': 'a', 'blue': 'b'}` |
| D35 | P1-07 | Total `minutes` across a list of record dictionaries | 20 and 35 → 55; empty list → 0 |
| D36 | P1-08 | Write `celsius_to_fahrenheit(celsius)` that returns its result | No input or printing inside the function |
| D37 | P1-08 | Write `average(values)` returning `None` for an empty list | `[2, 4]` → 3.0; `[]` → `None` |
| D38 | P1-08 | Write `count_at_least(values, target)` | `[3, 5, 7]`, target 5 → 2 |
| D39 | P1-08 | Write a greeting function with a default punctuation argument | Demonstrate default and explicit keyword use |
| D40 | P1-08 | Write `contains_value(values, target)` with a loop | Return `True` or `False`; handle an empty list |
| D41 | P1-10 | Repair a missing-colon error and a misspelled-variable error | Explain why their exception categories differ |
| D42 | P1-10 | Read two whole numbers and divide them | Handle invalid integer text and a zero denominator |
| D43 | P1-10 | Write `read_positive_integer()` | Reject zero, negatives, empty text, and nonintegers |
| D44 | P1-06 | Trace an accumulator over `[3, 1, 4]` | Show the total after each iteration: 3, 4, 8 |
| D45 | P1-10 | Test your function from exercise 38 | Normal, exact threshold, empty, all below, all above |
| D46 | P1-12 | Write and then read a short UTF-8 practice note | Use a named practice file and verify the text |
| D47 | P1-12 | Save and reload a dictionary using JSON | Compare the loaded values with the original |
| D48 | P1-12 | Write a CSV with topic and minutes columns; read its total | 15, 25, 40 → 80 |
| D49 | P1-12 | Specify a terminal task manager before writing it | State inputs, outputs, five rules, and five checks |
| D50 | P1-12 | Add CSV export to the study tracker | Export columns `session` and `minutes`, preserving order |

For D12, define initials using whitespace-separated nonempty parts; an empty
string returns an empty string in the supplied reference. This simple rule is
not a general model of personal names. For D47, choose JSON-compatible data
with string keys; arbitrary Python objects do not all round-trip unchanged.
For D50, use the column order `session,minutes`, number rows from 1, and preserve
duration order. A header-only export is valid for no sessions.

Selected checked implementations: [drills.py](../examples/drills.py). Open them
after an attempt, then use different inputs for a fresh check. Relevant sources
are linked from [Phase 1](../curriculum/phase-1.md).
