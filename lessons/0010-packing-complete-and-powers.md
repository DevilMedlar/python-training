# Record 0010: packing complete and powers with parentheses

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Corrected packing review and next lesson |
| Previous review | [Record 0009](0009-packing-review.md) |
| Verified learner commit | [ff72606](https://github.com/DevilMedlar/python-training/commit/ff726063dffc58cb38d16747bad87d14cb09ec31) |
| Verified source | [packing.py at this commit](https://github.com/DevilMedlar/python-training/blob/ff726063dffc58cb38d16747bad87d14cb09ec31/packing.py) |
| File blob | 9419373f9bb2da0efd25b14bdf8397f401313101 |
| Packing status | Complete: both corrections and both required runs are demonstrated |
| Next exercise | garden.py: positive integer powers and arithmetic grouping |

**Evidence.** The learner submitted corrected code for 26 stickers and for 28 stickers, with predictions and terminal output for both. The two pasted programs differ only in the initial sticker count. The 28-sticker version matches the repository file fetched at the pinned commit. Evidence for the 26-sticker version is the learner's pasted code and transcript; this review does not claim that both versions were fetched from GitHub or executed by the tutor.

The submitted code uses `packed_stickers = pack_size * full_packs`, then prints full_packs, leftover_stickers, packed_stickers, and division_result in the requested order. This order of the integer multiplication operands is correct; no reversal is needed.

| Starting stickers | full_packs | leftover_stickers | packed_stickers | division_result | Prediction and actual output |
| --- | --- | --- | --- | --- | --- |
| 26 | 6 | 2 | 24 | 6.5 | Match |
| 28 | 7 | 0 | 28 | 7.0 | Match |

**Assessment and strengths.** All assigned requirements are satisfied. The learner uses //, %, *, and / for the requested calculations, calculates from named values, corrects the output sequence, predicts both runs accurately, and keeps descriptive names and consistent operator spacing. The exact-multiple case correctly produces zero leftovers and a floating-point division result of 7.0.

**Resolved follow-ups.** The requested multiplication, output-order correction, and second run from record 0009 are all complete. Do not retain them as unresolved weaknesses or require another equivalent correction. This demonstrates the assigned arithmetic in two cases; advanced numeric behavior and broader programming independence still require later evidence. Confirm completion warmly and move on.

**Next teaching scope.** Introduce positive integer powers with **: 3 ** 2 is 3 multiplied by itself, giving 9. For the positive-number arithmetic used in this lesson, parentheses specify groups; ** binds before multiplication/division/floor division/remainder, which bind before addition/subtraction. The multiplication/division group and the addition/subtraction group each associate left to right. Power chains, negative signs, and negative/fractional exponents remain later topics. Source: [Python power and precedence rules](https://docs.python.org/3.14/reference/expressions.html#operator-precedence).

Use these worked expressions before assigning the garden program:

| Expression | Explanation | Result |
| --- | --- | --- |
| 3 ** 2 | Square 3 | 9 |
| 4 + 2*3 | Multiply 2 by 3, then add 4 | 10 |
| (4+2) * 3 | Add 4 and 2, then multiply by 3 | 18 |

Explain the style refinement alongside these examples: PEP 8 permits spacing to reflect operator priorities. The compact groups above do not change the arithmetic; parentheses do affect grouping. Keep assignment spacing consistent. Do not present an optional mixed-expression spacing convention as a new required correction to the completed packing code. Source: [PEP 8 operator spacing](https://peps.python.org/pep-0008/#other-recommendations).

**Learner assignment: garden.py.** Explain that a square's area is its side length squared. Start with side_length equal to 5 metres and extension equal to 2 metres. The side length increases by extension; this is a change in total side length, not a border width added on every edge.

Ask the learner to calculate and store:

1. original_area: the original square's area, using **.
2. expanded_area: the area after the side length increases by extension. To practise grouping, use one expression with parentheses and ** so the side-length addition happens before squaring.
3. added_area: the expanded area minus the original area.

Print these three results in that order, each on its own line. Predict the output, save, and run `python3 garden.py`. Request code, prediction, and actual output. Supply the different worked expressions above, not the learner's complete solution.

**Next review criteria.** Check variable-based calculations, ** for the two areas, the explicit parenthesized addition for expanded_area, subtraction for added_area, and the three outputs in order. Expected values are 25, 49, 24, in square metres. These are tutor review expectations; no garden submission has yet been received. The single assigned case is sufficient for the next review; do not add unannounced requirements.

**Editor shortcut introduced.** With the code editor focused and the cursor on a line, Alt+Up or Alt+Down moves that line in VS Code on Windows/Linux. This is useful for rearranging statements. The shortcut is being taught, not claimed as already demonstrated. Source: [VS Code default keybindings](https://code.visualstudio.com/docs/reference/default-keybindings).

**Resume state.** Packing is complete at its assigned scope. Positive integer powers, basic arithmetic precedence, and grouping are introduced with this response; garden.py is awaiting learner evidence. After successful garden practice, move to input and conversions. Retain negative/fractional powers, power chains, precedence involving signs and later operators, and further numeric details for later focused practice.

**README and workflow.** Add record 0010 with its purpose and narrow the remaining powers/precedence coverage in the same commit. Keep the curriculum non-exhaustive and preserve older records and learner programs. Continue accepting clear informal explanations and choosing meaningful Git checkpoints instead of requiring a commit or pull for each small exercise.
