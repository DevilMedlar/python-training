# Record 0020: grouping complete and truthiness

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Phase 1 grouping assessment and truthiness lesson |
| Previous record | [0019](0019-ranges-complete-and-boolean-grouping.md) |
| Phase guide | [Root README](../README.md), Phase 1: Beginner (Foundations) |
| Verified repository commit | [b5556da](https://github.com/DevilMedlar/python-training/commit/b5556daeb5fb7af85c39238d589f9bd7abcd403a) |
| Verified source | [date_night.py at this commit](https://github.com/DevilMedlar/python-training/blob/b5556daeb5fb7af85c39238d589f9bd7abcd403a/date_night.py) |
| Source blob | 08951db479148e687682e2b000472813df5a9411 |
| Runtime evidence | Four learner-supplied Codespace runs |
| Grouping exercise | Complete at the assigned scope |
| Prior spacing cleanup | Verified in practice_session.py |
| New lesson | Truthiness of familiar numbers and strings, bool(), direct conditions |
| New assignment | flirt_check.py; three inputs-and-output runs |
| New assignment status | Taught and assigned in chat; awaiting learner work |

**Evidence.** The learner's pasted source and repository source have the same executable statements; the repository file includes trailing whitespace after its final statement. The source blob was checked against the pinned commit tree. Runtime evidence is the learner's pasted transcript; the tutor did not run the learner's Codespace or inspect unpushed/unsaved content.

```python
available = int(input("How long is the date? "))
num_candles = int(input("How many candles? "))
playlist_length = int(input("How long is the playlist? "))

mood_ready = 60 <= available and (2 <= num_candles or 30 <= playlist_length)

if mood_ready:
    print("Mood ready")
else:
    print("Needs more preparation")
```

| Available minutes | Candles | Playlist minutes | Observed output | Assessment |
| --- | --- | --- | --- | --- |
| 60 | 2 | 0 | Mood ready | Correct candles-only route |
| 60 | 0 | 30 | Mood ready | Correct playlist-only route |
| 60 | 0 | 29 | Needs more preparation | Correct failure of both atmosphere options |
| 59 | 0 | 30 | Needs more preparation | Correct time failure despite sufficient playlist |

The parentheses keep the candle-or-playlist group subordinate to the required time threshold. The boolean assignment uses a full comparison for every requirement, and the if/else uses the stored boolean correctly. All four assigned runs pass.

**Operand order and clarity.** The learner puts numeric thresholds on the left: 60 <= available is equivalent to available >= 60, and the other comparisons are likewise valid. Do not request reversal of correct expressions. Names are understandable in this small program; an optional user-facing polish is to include minutes in both duration prompts. available_minutes could communicate the unit more explicitly, but this is not a required rewrite or unresolved defect. No additional validation was assigned; do not add surprise negative-input or conversion-error requirements.

**Prior follow-up resolved.** The fetched [practice_session.py at the pinned commit](https://github.com/DevilMedlar/python-training/blob/b5556daeb5fb7af85c39238d589f9bd7abcd403a/practice_session.py) has the header elif 20 <= practice <= 40:, including the missing space. Its verified blob is edab47fe1b2b1d633edeefa0256b8f14506d3768. This closes the spacing follow-up from 0019 without requiring another learner run or submission.

**Assessment status.** Mixed and/or grouping, inclusive threshold use, and the named-boolean decision are successfully demonstrated in the assigned scenario. The grouping exercise is complete. No functional correction is pending. One successful scenario is guided evidence, not universal mastery. Mixed/exclusive range endpoints and not applied to a grouped condition remain useful later practice; do not label these untested areas as mistakes.

**New lesson and assignment delivered in chat.**

Next: **truthiness—using values directly as conditions**.

You already use `if mood_ready:` with a boolean. Python can also test a string or number directly:

- **Truthy:** treated as true in a condition.
- **Falsy:** treated as false in a condition.

`bool(value)` gives that truth-test result as `True` or `False`; it leaves the original value unchanged. [Python bool](https://docs.python.org/3.14/library/functions.html#bool)

| Value | Truth-test result | Reason |
| --- | --- | --- |
| `0`, `0.0` | `False` | Numeric zero |
| `5`, `-5` | `True` | Nonzero numbers |
| `""` | `False` | Empty string |
| `"hello"`, `"0"`, `"False"` | `True` | Nonempty strings |
| `" "` | `True` | One space is still a character |

An empty string contains no characters, including no spaces.

Python checks whether text is present, not whether its words mean “true.” And a negative number being truthy does **not** make it a valid count. [Python truth-value testing](https://docs.python.org/3.14/library/stdtypes.html#truth-value-testing)

```python
message = ""
lights = 2

print(bool(message))
print(bool(lights))

if message:
    print("Message supplied.")
else:
    print("Message missing.")
```

Output:

```text
False
True
Message missing.
```

`if message:` performs the truth test itself. You don't need to wrap its condition in `bool()`. The message remains a string.

Remember: `input()` returns text. Pressing **Enter without typing** gives `""`; typing **0** gives `"0"`. Using `int()` on that text produces the number `0`. [Python input](https://docs.python.org/3.14/library/functions.html#input)

**Your challenge: `flirt_check.py`.**

Check whether a message contains text and whether any time is available.

1. Ask for a message using `input()`, storing it as `message`.
2. Ask for available minutes using `int(input(...))`, storing them as `available_minutes`. Use nonnegative integers for this exercise.
3. Print `bool(message)` and `bool(available_minutes)` together on one line, in that order. You can pass both values to one `print()` call.
4. Use `if message:` with an `else` to print `"Text entered"` or `"No text entered"`.
5. Use a **separate** `if available_minutes:` with an `else` to print `"Some time available"` or `"No time available"`.

Keep the message exactly as entered.

Save and run:

```bash
python3 flirt_check.py
```

| Message entered | Minutes | Boolean line | Following messages |
| --- | --- | --- | --- |
| Press Enter without typing | 0 | `False False` | No text entered; No time available |
| `0` | 30 | `True True` | Text entered; Some time available |
| `False` | 0 | `True False` | Text entered; No time available |

The semicolons separate two output lines. Type `0` and `False` **without quotation marks**.

Send your **code and these three actual runs**.


**Concept scope.** The lesson applies truth testing to familiar booleans, integers, ordinary floats, and strings. Numeric zero and empty strings are falsy; nonzero familiar numbers and nonempty strings are truthy. Negative integer truthiness is explicitly distinguished from valid nonnegative-count input. The lesson does not teach collection truthiness, None, NaN edge cases, custom truth-testing methods, or exceptions; attach those details to their appropriate later topics rather than claiming they were covered here.

bool(value) returns a boolean and does not modify the original value. A direct if condition performs truth testing without an explicit bool() call. Truthiness is not equality with True, text parsing, semantic agreement, or validation. In particular, the literal text False and 0 is nonempty and truthy. The example's bool(message) output does not convert the stored message into a bool.

The input explanation covers an empty submitted line, the text 0, and conversion with the already learned int(). A spaces-only message remains nonempty. No stripping or normalizing is requested. Non-boolean and/or operand-return behavior has not been taught by this lesson and remains in the Foundation coverage.

**Assignment review criteria.** The learner must preserve raw input text, convert only available minutes to an integer, print the two bool results in the specified order, and use two separate direct conditions. Each if/else should produce its own line. Check empty text versus the nonempty strings 0 and False, integer 0 versus positive minutes, and independence of the decisions. A direct if is required for this practice rather than comparisons with True or an empty string. bool() is used for the explanatory output line, not required in the if headers.

The three cases are: empty message / 0 minutes gives False False and both absence messages; text 0 / 30 minutes gives True True and both presence messages; text False / 0 minutes gives True False, text entered and no time available. These exercise the new semantics without routine predictions or rerunning completed exercises. The displayed table is an assignment artifact, not a Python collection literal.

Nonnegative integer minutes are an explicit exercise assumption. Additional input validation is not required. If the learner adds a correct guard, accept it without inventing extra submissions. No function definitions, loops, collections, exception handlers, .strip(), or messaging tools are needed. The program only prints local feedback; nothing is sent to another person.

**Sources checked this turn.**

- [Python 3.14 truth-value testing](https://docs.python.org/3.14/library/stdtypes.html#truth-value-testing).
- [Python bool](https://docs.python.org/3.14/library/functions.html#bool).
- [Python input](https://docs.python.org/3.14/library/functions.html#input).

The last confirmed interpreter is Python 3.14.2; the references describe the current 3.14 series.

**Resume state.** Review flirt_check.py and the three actual runs. Reuse the correct grouping and range skills in later scenarios without repeating their introductory lessons. After successful direct truth testing, consult the remaining coverage and introduce non-boolean and/or return behavior, such as a default text value, through a separate example and practical task. Whitespace normalization belongs to upcoming string methods, with careful distinction between raw and normalized input. Collection truthiness and custom object truth testing belong with those later-phase types. No additional topic is assigned by this note.

**Record maintenance.** This record supersedes the pending date-night assignment and spacing-cleanup status in 0019. Add 0020 to the Foundation Record/Purpose index and update the current checkpoint. Remove the introduced truthiness topic from Foundation remaining coverage while keeping the narrower demonstration status and later-type exclusions in this record. Preserve prior numbered records, the root README, and learner exercise source. The next record is 0021.
