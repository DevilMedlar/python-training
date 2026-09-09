# Record 0019: range practice complete and boolean grouping

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Phase 1 range review and mixed boolean grouping lesson |
| Previous record | [0018](0018-nesting-complete-and-comparison-chaining.md) |
| Phase guide | [Root README](../README.md), Phase 1: Beginner (Foundations) |
| Verified repository commit | [2a706de](https://github.com/DevilMedlar/python-training/commit/2a706deb17719afd6a8aafefc9e2db59104863b3) |
| Verified source | [practice_session.py at this commit](https://github.com/DevilMedlar/python-training/blob/2a706deb17719afd6a8aafefc9e2db59104863b3/practice_session.py) |
| Source blob | 5b23758a4ddc3f1d287165ecc90bf32be86d18c9 |
| Runtime evidence | Learner's five pasted Codespace runs |
| Range exercise | Functionally complete at the assigned scope |
| Small style follow-up | Add the missing space before 40; no separate resubmission required |
| New lesson | Comparisons versus not/and/or precedence, mixed boolean grouping, parentheses |
| New assignment | date_night.py with one grouped decision and four runs |
| Assignment status | Taught and issued in chat; awaiting learner work |

**Evidence.** The pasted learner source matches the fetched repository file, whose blob was verified in the pinned commit tree. Runtime evidence comes from the learner's terminal transcript. The tutor did not run the code in the learner's Codespace and does not have access to unpushed or unsaved edits.

```python
practice = int(input("How many minutes did you practice? "))

if practice < 0:
    print("Minutes cannot be negative.")
else:
    if 0 <= practice <= 19:
        print("Below target")
    elif 20 <= practice <=40:
        print("Within target")
    else:
        print("Above target")
```

| Input minutes | Observed output after prompt | Assessment |
| --- | --- | --- |
| -1 | Minutes cannot be negative. | Correct negative guard |
| 19 | Below target | Correct just below lower endpoint |
| 20 | Within target | Correct inclusive lower endpoint |
| 40 | Within target | Correct inclusive upper endpoint |
| 41 | Above target | Correct just above upper endpoint |

All requested cases pass. The outer if/else rejects negative minutes. Within the valid-data branch, the learner uses chained comparisons for both the below-target and within-target intervals. For these integer inputs, 0 through 19 and 20 through 40 leave no gaps. Branch order and indentation are correct, with one result per run.

**Review and style.** The additional 0 <= check repeats a guarantee already established by the outer validation, but it is valid and harmless. Do not turn it into a required rewrite. practice is understandable in this small script; there is no naming error. Ask for one small spacing cleanup: practice <=40 becomes practice <= 40, making the full header elif 20 <= practice <= 40:. This is readability guidance, not a syntax or output defect. Complete it while editing; do not demand another old-case run or standalone resubmission.
Source: [PEP 8 other recommendations](https://peps.python.org/pep-0008/#other-recommendations).

**Resolved and remaining status.** This record supersedes the awaiting-submission status in 0018. Guided inclusive-range practice and all five assigned runs are complete. The missing space is the only observed style follow-up. Exclusive and mixed endpoints were introduced previously but still lack learner demonstration; that is an untested area, not a weakness. The current lesson can proceed without repeating comparison basics or the range challenge.

**Lesson and assignment delivered in chat.**

Next: **grouping mixed boolean conditions**.

When combining three conditions, make their intended grouping explicit.

Without parentheses, these operators bind from highest to lowest priority:

| Priority | Operators |
| --- | --- |
| Highest here | Comparisons: `==`, `!=`, `<`, `<=`, `>`, `>=` |
| Then | `not` |
| Then | `and` |
| Lowest here | `or` |

“Bind” means which parts belong together. For example, `not score >= 10` groups as `not (score >= 10)`. Parentheses can change grouping; short-circuiting still applies. [Python operator precedence](https://docs.python.org/3.14/reference/expressions.html#operator-precedence)

A printer needs paper and a job from either a laptop or a phone:

```python
has_paper = False
laptop_job = False
phone_job = True

print(has_paper and laptop_job or phone_job)
print(has_paper and (laptop_job or phone_job))
```

Output:

```text
True
False
```

The first expression groups as `(has_paper and laptop_job) or phone_job`. The phone job alone makes it true, even without paper.

The second requires **paper AND either kind of job**, so it correctly gives `False`.

The parentheses group the alternative job sources under the shared paper requirement.

**Your challenge: `date_night.py`.**

For this fictional date-night plan, ask for three integer inputs, in this order:

1. Available minutes.
2. Number of candles.
3. Playlist length in minutes.

Use nonnegative integer inputs for this exercise.

Store a boolean named `mood_ready`. The setup is ready when:

- You have **at least 60 minutes available**.
- You also have **at least 2 candles OR a playlist lasting at least 30 minutes**.

A sufficient playlist satisfies the alternative to the candle requirement. The available-time requirement must still be met.

Build the decision in **one expression using `and`, `or`, and parentheses**. Then use `if`/`else` to print `"Mood ready"` or `"Needs more preparation"`.

Choose meaningful variable names. Use a complete comparison for each requirement.

Save and run:

```bash
python3 date_night.py
```

| Available minutes | Candles | Playlist minutes | Expected message |
| --- | --- | --- | --- |
| 60 | 2 | 0 | Mood ready |
| 60 | 0 | 30 | Mood ready |
| 60 | 0 | 29 | Needs more preparation |
| 59 | 0 | 30 | Needs more preparation |

The last run checks that the playlist cannot bypass the time requirement.

Send your **code and actual outputs**.


**Teaching intent.** The printer example shows why and binding more tightly than or can admit a result that violates a shared requirement. Parentheses explicitly attach the shared requirement to either alternative. Precedence describes grouping, not a global instruction to evaluate every comparison or every and before other operations; left-to-right evaluation and short-circuiting remain relevant. not groups less tightly than comparisons and more tightly than and/or. The worked example is separate from the learner's task and is not evidence of independent skill.

**Assignment scope and review.** The fictional date-night decision requires the time threshold in both successful paths: enough candles or a long enough playlist. Check a single boolean assignment using and, or, and parentheses, correct inclusive numeric thresholds, and a following if/else that uses the result. Equivalent operand orders and meaningful learner-chosen names are acceptable. Do not supply the finished date_night.py implementation.

The four assigned cases demonstrate the candles-only path, playlist-only path, neither option meeting its threshold, and a time failure despite a sufficient playlist. The final case distinguishes the required grouped rule from a common missing-parentheses error. This is focused practice, not exhaustive validation of all possible inputs.

The lesson explicitly uses nonnegative integer inputs. Additional negative-input validation is not required for this exercise and should not become a surprise review requirement. A learner-added valid guard can be accepted. Non-integer conversion recovery still belongs to Phase 2. No loops, collections, functions, or exception handlers are introduced. The learner writes and runs their own program; no predictions or routine Git checkpoint are requested.

**Demonstrated strengths and uncertainty.** The learner has now correctly applied a numeric validation guard, nested branches, chained bounds, and boundary checks in a second scenario. Boolean mixed-operator grouping is introduced here and awaits learner evidence. Do not infer mastery from the worked example or invent problems from untested cases.

**Sources checked this turn.**

- [Python 3.14 operator precedence](https://docs.python.org/3.14/reference/expressions.html#operator-precedence) supports comparisons, not, and, or binding order and grouping.
- [Python boolean operations](https://docs.python.org/3.14/reference/expressions.html#boolean-operations), on the same expression-reference page, describes short-circuit behavior.
- [PEP 8 operator spacing](https://peps.python.org/pep-0008/#other-recommendations) supports the single-space cleanup.

The last confirmed learner interpreter remains Python 3.14.2; sources describe the current 3.14 series.

**Resume state.** Review date_night.py and its four actual runs. Track the small practice_session.py spacing cleanup if visible, without interrupting progress for a separate style-only submission. After grouped-condition practice, consult the phase guide and remaining coverage; truthiness and then non-boolean and/or behavior are potential next topics. Plan later short variations for exclusive/mixed interval endpoints and not applied to a grouped condition. Do not assign those variations or assume them demonstrated yet.

**Record maintenance.** Add 0019 to the Foundation Record/Purpose index; update the checkpoint; remove the introduced mixed boolean-operator precedence/grouping topic from remaining-to-teach coverage. Preserve earlier records, the root outline, and learner Python files. The next record is 0020.
