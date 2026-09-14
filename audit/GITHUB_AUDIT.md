# GitHub reference audit and integration

Reviewed 2026-09-14. Input: `GitHub_Practical_Reference(1).md`, identified by
[the input manifest](input-manifest.json). Read all 29 numbered sections, including
the Python example, workflow, instruction-file template, command tables, and
author's verification notes. The draft already contains many careful qualifications;
they are retained where supported. We do not label a correct passage an error to
make this review sound more consequential.

The result is [16 companion lessons](../curriculum/github.md), two tasks per lesson,
[six hands-on labs and a capstone](../practice/GITHUB_LABS.md), and a
[compact reference](../practice/GITHUB_REFERENCE.md). The five Python phases remain
the default route. GitHub is a separately selected practical track, not a sixth
degree or mastery rank.

## Pass 1 Primary facts and scope

Consulted 55 additional primary references in [SOURCES.md](SOURCES.md) and
[sources.json](sources.json), covering GitHub, Git, GitHub CLI, and official OpenAI
documentation. Existing Python/Git references also support the integration.
Consequential checks and integration decisions follow.

| Claim or draft pattern | Finding and treatment | Evidence |
|---|---|---|
| ZIP, clone, fork, template, branch | Retained distinctions; no assumption that reading or copying grants write access | GH-CLONE, GH-TEMPLATE, GH-LICENSE |
| Commit identity versus authentication | Retained; author metadata is not sign-in; ordinary account passwords are not Git-over-HTTPS credentials | GH-SETUP, GH-AUTH |
| Fine-grained tokens | Retained documented feature-gap caveat; do not claim they support every classic-token workflow | GH-TOKENS |
| github.dev versus Codespaces/Desktop | Retained editing/compute and supported-system boundaries | GH-DEV, GH-DESKTOP |
| Working tree, index, HEAD | Retained staged-snapshot model and made it an observable three-version experiment | GIT-BOOK; executable Git lab |
| Pull into the current branch | Retained explicit current-branch warning and fast-forward policy; never prescribe force-push for an auth error | GIT-PULL |
| Squash/rebase and branch cleanup | Retained content-versus-ancestry distinction; deletion refusal is not proof work is absent | GH-MERGES |
| Restore, revert, stash, reflog | Retained different targets and limits; ignored files excluded by stash -u; reflog is local and expires | GIT-RESTORE, GIT-REVERT, GIT-STASH, GIT-REFLOG; Git lab |
| Merge abort | Retained clean-start condition; uncommitted pre-merge work can prevent full reconstruction | GIT-MERGE; conflict/abort lab |
| Ignore rules and exposed credentials | Retained tracked-history limitation and revoke/rotate-first guidance | GH-IGNORE, GH-SENSITIVE |
| Python normalizer | Retained contract and sanitizer caveat; adapted to real paths and expanded boundary coverage | PY-TEXT; original and maintained tests |
| Empty test discovery | Preserved the draft's zero-test guard and applied it to this repository's CI runner | PY-UNITTEST; positive/failure/empty-suite tests |
| Actions pins and event filters | Confirmed both existing full pins against official v7 refs; explain base-branch PR filters and actual logs | GH-ACTIONS-EVENTS, GH-ACTIONS-SECURITY; refs below |
| Generic layout and workflow templates | Adapted to the existing examples/tests/tools layout and ten-job matrix; no duplicate incompatible project skeleton | Inspected repository paths and workflow |
| Search and issue closure | Retained result-type distinctions and default-branch closure qualification | GH-CODE-SEARCH, GH-REPO-SEARCH, GH-ISSUE-SEARCH, GH-ISSUE-LINKS |
| Rulesets and CODEOWNERS | Retained plan/visibility caveats; ownership does not independently require approval or grant write access | GH-RULESETS, GH-CODEOWNERS |
| Pages, gists, packages | Retained static-hosting and privacy distinctions; link explicit Pages private-publication conditions | GH-PAGES, GH-PAGES-ACCESS, GH-GISTS, GH-PACKAGES |
| Usage and size numbers | Rechecked personal Free/Pro allowances, core-hour arithmetic, retained storage, and MiB thresholds; date the snapshot | GH-USAGE, GH-ACTIONS-BILLING, GH-CODESPACES-BILLING, GH-LARGE-FILES |
| CLI and API reads | Added explicit GET, pagination, and issue-list inclusion of PRs to prevent unintended mutation or incomplete counts | GH-CLI-API, GH-REST-ISSUES, GH-REST-LIMITS |
| AGENTS.md and Codex review | Kept instructions subordinate to actual access and host rules; verified review setup/invocation and distinguish quoted templates from active guidance | OAI-AGENTS, OAI-GITHUB-REVIEW |
| Backups and advanced tools | Retained Git-history versus service-data boundary; added a fresh restoration from the tested mirror | GH-BACKUP, GIT-BISECT; Git lab |
| Draft verification notes | Reproduced the Python checks and specific Git invariants; do not inherit all of the author's claimed checks | Results below |

The unchanged workflow action pins were re-read from the official
[checkout v7 ref](https://api.github.com/repos/actions/checkout/git/ref/tags/v7)
(`3d3c42e5aac5ba805825da76410c181273ba90b1`) and
[setup-python v7 ref](https://api.github.com/repos/actions/setup-python/git/ref/tags/v7)
(`5fda3b95a4ea91299a34e894583c3862153e4b97`). This is a dated observation;
future tag movement does not update the pinned workflow automatically.

## Coverage of the supplied reference

| Source section | Canonical destination or treatment |
|---|---|
| 1 First session | GH-02; Lab A |
| 2 Vocabulary | GH-01, GH-04–GH-06; command effect table |
| 3 Ways to use GitHub | GH-03 |
| 4 Evaluate a repository | GH-01 |
| 5 Search | GH-11; reference search examples |
| 6 Download, clone, fork, template | GH-01, GH-06 |
| 7 Accounts and permissions | GH-03, GH-12 |
| 8 Local setup | GH-03; Lab B |
| 9 Everyday workflow | GH-04–GH-06; Labs B/C |
| 10 Existing project upload | GH-05 |
| 11 PRs and merge choices | GH-06 |
| 12 Fork contributions | GH-06 |
| 13 Conflicts | GH-07; Lab D |
| 14 Undo/recovery | GH-08; Lab E |
| 15 Markdown | GH-11; maintained relative links and examples |
| 16 Python repository organization | GH-09; existing layout preserved |
| 17 Python example | GH-09; topic_names.py; Lab F |
| 18 Actions | GH-10; existing verify.yml extended; update proposals taught, no new Dependabot configuration |
| 19 Issues, Projects, notifications | GH-11 |
| 20 Protection | GH-12; proposal exercises rather than assumed setting changes |
| 21 Publishing | GH-13 |
| 22 Usage/limits | GH-13; dated reference table |
| 23 CLI/APIs | GH-14 |
| 24 ChatGPT/Codex | GH-15; launch prompt and existing AGENTS.md adapted |
| 25 Backups/advanced Git | GH-16; specialist commands remain problem-driven extensions |
| 26 Troubleshooting | Reference diagnostic table |
| 27 Practice schedule | Catalog order, placement, tasks, and evidence rules; schedule is a suggestion |
| 28 Commands | Reference with source/destination effects |
| 29 Verification | This audit's independent observations and explicit unexecuted scope |

## Pass 2 Executable checks

Local observations use Linux, CPython 3.12.14, and Git 2.51.1. Optional scientific
dependencies already installed here are NumPy 2.3.5 and SciPy 1.17.0.

- Extracted the draft's three Python files to a disposable directory: all four
  original tests passed. Removing lowercasing failed the expected assertion;
  restoring it passed. Removing the test file caused unsuccessful empty discovery.
- The maintained normalizer has six contract tests, including whitespace-only
  input, punctuation/Unicode, and idempotence. It remains a teaching function.
- The test runner checks positive, failing, and empty suites, including an actual
  subprocess with a discovery pattern that finds no tests.
- The offline Git lab checks seven invariant groups in temporary repositories:
  snapshots; unstage/restore; stash/ignore; fetch/fast-forward refusal; conflict/
  abort/resolution; revert/rescue; mirror and fresh content restoration. It uses
  synthetic identity, isolated configuration/hooks/ignore defaults, and no network.
- The full local suite passed **100 tests**, including all five scientific tests,
  without skips. The seven Git invariant groups passed. See
  [verification history](VERIFICATION.md) for subsequent CI observations.

These results do not claim every optional command in the draft was executed.
Manual browser account setup, `gh` authentication, paid services, ruleset changes,
publication/deployment, LFS restoration, and complete GitHub metadata backup are
documented exercises, not live operations performed for this audit.

## Pass 3 Integration and consistency

The catalog now contains 66 lessons: 50 Python lessons, including 48 default core
lessons, and 16 optional GitHub companion lessons. Every lesson has a worked
example, two tasks, hints, evidence, explicit prerequisites, and source mappings.
There are 182 lesson/drill tasks (132 in lessons and 50 extra beginner drills),
plus six capstone briefs. Lab exercises are additional practice, not added again
to that task count.

Catalog `1.1` preserves schema version 1 and accepts existing `1.0` progress records.
Tests cover independent route selection, current transitive prerequisites, due
review isolation, distinct capstones, invalid tracks, and cross-track cycles.
The checker validates both starter records, generated navigation, local anchors,
and every runnable Python Markdown example. Passing structural validation cannot
establish whether a learner's reported evidence is true.

## Pass 4 Tutor behavior review

Extended the [scenario review](../tutor/SCENARIOS.md) for browser-only beginners,
rehearsed PRs, Python prerequisites, quoted instruction templates, unknown repository
state, legacy progress, and empty CI discovery. The launch prompt requires actual
file-access reporting, one task at a time, evidence-aware progress, and explicit
GitHub routing. An assistant's generated solution does not become independent
learner work merely because its tests pass.

This is a manual design review, not a measured evaluation of ChatGPT compliance
or a guarantee of flawless teaching. External services and docs can change;
account-specific rights and real learner outcomes require their own evidence.
