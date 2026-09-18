from copy import deepcopy
from datetime import date
import json
from pathlib import Path
import unittest

from tools.progress import ProgressError, recommend, validate_state


ROOT = Path(__file__).resolve().parents[1]
TODAY = date(2026, 9, 18)
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))


def attempt(kind="applied", day="2026-09-18", support="none", outcome="pass"):
    return {"kind": kind, "performed_on": day, "outcome": outcome, "support": support,
            "summary": "Synthetic fixture: wrote and ran the requested program."}


def provisional(support="hint"):
    return {"status": "provisional", "attempts": [attempt(support=support)]}


def historical_provisional():
    return {"status": "provisional", "attempts": [attempt("transfer"), attempt("explanation")]}


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.state = json.loads((ROOT / "tutor/progress-template.json").read_text(encoding="utf-8"))

    def check(self):
        return validate_state(self.state, CATALOG, today=TODAY)

    def add_record(self, record):
        self.state["updated_on"] = "2026-09-18"
        self.state["lessons"]["P1-01"] = record

    def test_empty_record_starts_at_first_lesson_in_the_codespace(self):
        self.check()
        result = recommend(self.state, CATALOG, today=TODAY)
        self.assertEqual((result["kind"], result["lesson_id"]), ("lesson", "P1-01"))
        self.assertEqual(result["workspace_url"], CATALOG["workspace_url"])
        self.assertEqual(result["workspace_shortcut"], CATALOG["lessons"][0]["workspace_shortcut"])

    def test_legacy_progress_remains_readable_but_unknown_version_is_rejected(self):
        for version in ("1.0", "1.1", "1.2"):
            self.state["catalog_version"] = version
            self.add_record(historical_provisional())
            with self.subTest(version=version):
                self.check()
                self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["lesson_id"], "P1-02")
        self.state["catalog_version"] = "2.0"
        with self.assertRaisesRegex(ProgressError, "catalog version mismatch"):
            self.check()

    def test_old_track_parameter_uses_the_same_python_route(self):
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY, track="github"),
                         recommend(self.state, CATALOG, today=TODAY))
        self.add_record(provisional())
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY, track="github")["lesson_id"], "P1-02")

    def test_historical_github_evidence_cannot_skip_python_learning(self):
        self.state["catalog_version"] = "1.1"
        self.state["current_lesson"] = "GH-04"
        self.state["updated_on"] = "2026-09-18"
        for ident in CATALOG["legacy_reference_ids"]:
            self.state["lessons"][ident] = historical_provisional()
        self.state["capstones"]["github"] = {"status": "complete", "completed_on": "2026-09-18",
                                              "support": "reference", "evidence": ["Historical synthetic review."]}
        for track in (None, "github"):
            self.assertEqual(recommend(self.state, CATALOG, today=TODAY, track=track)["lesson_id"], "P1-01")

    def test_old_github_review_does_not_create_a_compulsory_route(self):
        self.state["catalog_version"] = "1.2"
        self.state["updated_on"] = "2026-09-18"
        self.state["lessons"]["GH-04"] = historical_provisional()
        self.state["reviews"] = [{"lesson_id": "GH-04", "due_on": "2026-09-13", "reason": "Old review"}]
        result = recommend(self.state, CATALOG, today=TODAY)
        self.assertEqual((result["kind"], result["lesson_id"]), ("lesson", "P1-01"))
        self.assertNotIn("optional_reviews", result)

    def test_python_completion_does_not_add_a_github_capstone(self):
        self.state["updated_on"] = "2026-09-18"
        for lesson in CATALOG["lessons"]:
            if lesson["core"]:
                self.state["lessons"][lesson["id"]] = provisional()
        result = recommend(self.state, CATALOG, today=TODAY)
        self.assertEqual(result["kind"], "maintenance")
        self.assertEqual([item["phase"] for item in result["suggested_capstones"]], [1, 2, 3, 4, 5])

    def test_unknown_track_is_rejected(self):
        with self.assertRaisesRegex(ProgressError, "unknown track"):
            recommend(self.state, CATALOG, today=TODAY, track="unknown")

    def test_applied_success_advances_without_prediction_explanation_or_delayed_review(self):
        for kind in ("applied", "guided", "transfer"):
            for support in ("none", "reference", "hint", "solution"):
                self.add_record({"status": "provisional", "attempts": [attempt(kind, support=support)]})
                with self.subTest(kind=kind, support=support):
                    self.check()
                    self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["lesson_id"], "P1-02")

    def test_pure_explanation_is_not_an_applied_attempt(self):
        self.add_record({"status": "provisional", "attempts": [attempt("explanation")]})
        with self.assertRaisesRegex(ProgressError, "applied work"):
            self.check()

    def test_learning_status_preserves_an_unfinished_attempt(self):
        self.add_record({"status": "learning", "attempts": [attempt(outcome="retry", support="solution")]})
        self.check()
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["lesson_id"], "P1-01")

    def test_secure_requires_work_without_hint_or_solution_support(self):
        for support in ("hint", "solution"):
            self.add_record({"status": "secure", "attempts": [attempt(support=support)]})
            with self.subTest(support=support), self.assertRaisesRegex(ProgressError, "none/reference"):
                self.check()
        for support in ("none", "reference"):
            self.add_record({"status": "secure", "attempts": [attempt(support=support)]})
            with self.subTest(support=support):
                self.check()

    def test_historical_secure_semantics_are_not_rewritten(self):
        self.state["catalog_version"] = "1.2"
        record = historical_provisional()
        record["status"] = "secure"
        self.add_record(record)
        with self.assertRaisesRegex(ProgressError, "later date"):
            self.check()
        record["attempts"] = [attempt("transfer", "2026-09-16"), attempt("explanation", "2026-09-16"),
                              attempt("delayed", "2026-09-18")]
        self.check()

    def test_later_failure_cannot_hide_behind_an_old_success(self):
        for kind in ("applied", "guided", "transfer", "delayed"):
            for status in ("provisional", "secure"):
                record = {"status": status, "attempts": [attempt(day="2026-09-17"),
                                                         attempt(kind, outcome="retry")]}
                self.add_record(record)
                with self.subTest(kind=kind, status=status), self.assertRaisesRegex(ProgressError, "repair"):
                    self.check()
                record["status"] = "review_needed"
                self.check()
                self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["kind"], "repair")

    def test_failure_order_uses_date_then_record_order(self):
        self.add_record({"status": "secure", "attempts": [attempt(outcome="retry"), attempt()]})
        self.check()
        self.state["lessons"]["P1-01"]["attempts"].reverse()
        with self.assertRaises(ProgressError):
            self.check()

    def test_unknown_lesson_and_status_are_rejected(self):
        self.state["current_lesson"] = "P9-01"
        with self.assertRaises(ProgressError):
            self.check()
        self.state["current_lesson"] = "P1-01"
        self.add_record({"status": "mastered", "attempts": []})
        with self.assertRaises(ProgressError):
            self.check()

    def test_future_and_impossible_dates_rejected(self):
        self.add_record(provisional())
        for value in ("2027-01-01", "2026-02-30", "20260910"):
            self.state["lessons"]["P1-01"]["attempts"][0]["performed_on"] = value
            with self.subTest(value=value), self.assertRaises(ProgressError):
                self.check()

    def test_update_date_must_cover_evidence(self):
        self.add_record(provisional())
        self.state["updated_on"] = None
        with self.assertRaisesRegex(ProgressError, "latest recorded evidence"):
            self.check()

    def test_bad_container_types_are_diagnosed(self):
        for field, value in [("lessons", []), ("reviews", {}), ("goals", "learn"),
                             ("schema_version", True), ("current_lesson", []), ("environment", None)]:
            state = deepcopy(self.state)
            state[field] = value
            with self.subTest(field=field), self.assertRaises(ProgressError):
                validate_state(state, CATALOG, today=TODAY)

    def test_unknown_fields_are_not_silently_lost(self):
        self.state["fake_memory"] = "claimed"
        with self.assertRaisesRegex(ProgressError, "unknown fields"):
            self.check()

    def test_due_review_is_optional_and_does_not_block_next_lesson(self):
        self.add_record(provisional())
        self.state["reviews"] = [{"lesson_id": "P1-01", "due_on": "2026-09-18", "reason": "Requested practice"}]
        result = recommend(self.state, CATALOG, today=TODAY)
        self.assertEqual((result["kind"], result["lesson_id"]), ("lesson", "P1-02"))
        self.assertEqual(result["optional_reviews"][0]["lesson_id"], "P1-01")
        self.state["reviews"][0]["due_on"] = "2026-09-19"
        self.assertNotIn("optional_reviews", recommend(self.state, CATALOG, today=TODAY))

    def test_duplicate_review_is_rejected(self):
        review = {"lesson_id": "P1-01", "due_on": "2026-09-19", "reason": "Requested practice"}
        self.state["reviews"] = [review, dict(review)]
        with self.assertRaisesRegex(ProgressError, "duplicate"):
            self.check()

    def test_phase_project_is_suggested_without_blocking_next_phase(self):
        self.state["updated_on"] = "2026-09-18"
        for lesson in CATALOG["lessons"]:
            if lesson["phase"] == 1:
                self.state["lessons"][lesson["id"]] = provisional()
        result = recommend(self.state, CATALOG, today=TODAY)
        self.assertEqual(result["lesson_id"], "P2-01")
        self.assertEqual(result["suggested_capstones"][0]["phase"], 1)
        self.state["capstones"]["1"] = {"status": "complete", "completed_on": "2026-09-18",
                                        "support": "hint", "evidence": ["Synthetic completed project with help."]}
        self.assertNotIn("suggested_capstones", recommend(self.state, CATALOG, today=TODAY))

    def test_completed_project_still_requires_dated_evidence(self):
        self.state["capstones"]["1"] = {"status": "complete", "completed_on": None,
                                        "support": "solution", "evidence": []}
        with self.assertRaisesRegex(ProgressError, "dated evidence"):
            self.check()

    def test_optional_specialties_are_not_forced_into_core_route(self):
        self.state["updated_on"] = "2026-09-18"
        for lesson in CATALOG["lessons"]:
            if lesson["phase"] in {1, 2, 3, 4} or lesson["id"] in {"P5-01", "P5-02", "P5-03"}:
                self.state["lessons"][lesson["id"]] = provisional()
        self.state["lessons"]["P5-04"] = {"status": "review_needed", "attempts": [attempt(outcome="retry")]}
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["lesson_id"], "P5-06")
