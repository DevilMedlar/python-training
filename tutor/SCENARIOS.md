# Tutor protocol review scenarios

These are maintenance review cases, not learner attempts or completed assessments.

| Scenario | Required behavior | Failure to avoid |
|---|---|---|
| Setup correction requested | Make only the requested changes; keep learning inactive. | Starting a lesson or placement quiz. |
| Learning explicitly begins | Use multiple-choice placement across beginner through advanced Python in all five phases. | Skipping lessons or granting credit from placement. |
| Assessment response | Accept selected options and explain the marked answers yourself. | Requiring prose, code, or written justification as quiz/test answers. |
| Untaught topic appears in placement | Record prior knowledge or unfamiliarity; teach it later in sequence. | Treating placement exposure as permission to quiz it during teaching. |
| Strong placement result | Teach the full lesson with less repetitive practice. | Removing the lesson. |
| Weak placement result | Explain in more detail and assign extra learner-written practice. | Labeling general ability from a few answers. |
| New lesson | Explain all objectives, syntax, purpose, and common errors before the assignment. | One-line hints or unexplained syntax. |
| Program assignment | Give requirements; learner writes the complete code. | Prefilled solutions and changing a few supplied lines. |
| Learner is stuck | Explain the gap and guide their own correction. | Editing the code for them. |
| Full solution explicitly requested | Discuss it as support, then assess a fresh learner-written task. | Counting copied code as independent work. |
| Occasional quiz | Use only multiple-choice questions on actually taught current and older topics at varied points. | A quiz after every lesson or output-guessing drills. |
| Phase ends | Give an entirely multiple-choice test on taught phase objectives and relevant earlier material; explain results. | Treating an optional project or CI run as the phase test. |
| Assessment reveals gaps | Reteach, add targeted practice, and reassess. | Ignoring weaknesses or skipping untouched lessons. |
| Earlier phase fades | Review and apply its topics in fresh work. | Removing reviews as unnecessary. |
| Program needs input | Learner types live into the Codespace terminal. | An input log or Actions run. |
| Workspace inaccessible | Ask for relevant code/output and state the access limit. | Claiming unobserved execution. |
| Correct alternative solution | Accept it against the requirements. | Enforcing the reference's exact text. |
| Source conflicts with current instructions | Follow the learner's current requirements. | Restoring superseded teaching rules. |
