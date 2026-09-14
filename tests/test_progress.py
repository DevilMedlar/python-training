from copy import deepcopy
from datetime import date
import json
from pathlib import Path
import unittest

from tools.progress import ProgressError, recommend, validate_state


ROOT = Path(__file__).resolve().parents[1]
TODAY = date(2026, 9, 14)
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))


def attempt(kind, day="2026-09-10", support="none", outcome="pass"):
    return {"kind": kind, "performed_on": day, "outcome": outcome, "support": support,
            "summary": "Synthetic fixture: completed the stated task and explained the result."}


def provisional():
    return {"status": "provisional", "attempts": [attempt("transfer"), attempt("explanation")]}


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.state = json.loads((ROOT / "tutor/progress-template.json").read_text(encoding="utf-8"))

    def check(self):
        return validate_state(self.state, CATALOG, today=TODAY)

    def add_record(self, record):
        self.state["updated_on"] = "2026-09-14"
        self.state["lessons"]["P1-01"] = record

    def test_empty_record_starts_at_first_lesson(self):
        self.check()
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY), {"kind": "lesson", "lesson_id": "P1-01"})

    def test_legacy_progress_remains_readable_but_unknown_version_is_rejected(self):
        self.state["catalog_version"] = "1.0"
        self.check()
        self.state["catalog_version"] = "2.0"
        with self.assertRaisesRegex(ProgressError, "catalog version mismatch"):
            self.check()

    def test_github_starts_without_python_and_advances_with_evidence(self):
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY, track="github"),
                         {"kind": "lesson", "lesson_id": "GH-01"})
        self.state["updated_on"] = "2026-09-14"
        self.state["lessons"]["GH-01"] = provisional()
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY, track="github")["lesson_id"], "GH-02")
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["lesson_id"], "P1-01")

    def test_github_python_work_waits_for_actual_prerequisites(self):
        self.state["updated_on"] = "2026-09-14"
        for number in range(1, 9):
            self.state["lessons"][f"GH-{number:02}"] = provisional()
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY, track="github"),
                         {"kind": "prerequisite", "lesson_id": "P1-01", "needed_for": "GH-09"})
        for number in range(1, 12):
            self.state["lessons"][f"P1-{number:02}"] = provisional()
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY, track="github")["lesson_id"], "GH-09")

    def test_reviews_follow_selected_route_and_its_current_dependencies(self):
        self.state["updated_on"] = "2026-09-14"
        for ident in ("P1-01", "GH-01"):
            self.state["lessons"][ident] = provisional()
        self.state["reviews"] = [{"lesson_id": "P1-01", "due_on": "2026-09-13", "reason": "Recall"},
                                 {"lesson_id": "GH-01", "due_on": "2026-09-14", "reason": "Recall"}]
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["lesson_id"], "P1-01")
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY, track="github")["lesson_id"], "GH-01")
        self.state["reviews"].pop()
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY, track="github")["lesson_id"], "GH-02")
        for number in range(2, 10):
            self.state["lessons"][f"GH-{number:02}"] = provisional()
        result = recommend(self.state, CATALOG, today=TODAY, track="github")
        self.assertEqual((result["kind"], result["lesson_id"]), ("review", "P1-01"))

    def test_github_capstone_is_separate_from_python_capstones(self):
        self.state["updated_on"] = "2026-09-14"
        for lesson in CATALOG["lessons"]:
            if lesson.get("track") == "github" or lesson["phase"] == 1:
                self.state["lessons"][lesson["id"]] = provisional()
        result = recommend(self.state, CATALOG, today=TODAY, track="github")
        self.assertEqual((result["kind"], result["track"]), ("capstone", "github"))
        self.state["capstones"]["github"] = {"status": "complete", "completed_on": "2026-09-14",
                                              "support": "reference", "evidence": ["Synthetic reviewed PR."]}
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY, track="github")["kind"], "maintenance")
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["phase"], 1)

    def test_unknown_track_is_rejected(self):
        with self.assertRaisesRegex(ProgressError, "unknown track"):
            recommend(self.state, CATALOG, today=TODAY, track="unknown")

    def test_provisional_requires_transfer_and_explanation(self):
        self.add_record({"status": "provisional", "attempts": [attempt("guided")]})
        with self.assertRaisesRegex(ProgressError, "independent transfer"):
            self.check()

    def test_hint_and_solution_cannot_establish_independent_mastery(self):
        for support in ("hint", "solution"):
            self.add_record({"status": "provisional", "attempts":
                             [attempt("transfer", support=support), attempt("explanation")]})
            with self.subTest(support=support), self.assertRaises(ProgressError):
                self.check()

    def test_allowed_references_count_as_independent(self):
        self.add_record({"status": "provisional", "attempts":
                         [attempt("transfer", support="reference"), attempt("explanation", support="reference")]})
        self.check()
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["lesson_id"], "P1-02")

    def test_secure_requires_later_review(self):
        record = provisional()
        record["status"] = "secure"
        record["attempts"].append(attempt("delayed"))
        self.add_record(record)
        with self.assertRaisesRegex(ProgressError, "later date"):
            self.check()
        record["attempts"][-1]["performed_on"] = "2026-09-12"
        self.check()

    def test_later_failure_cannot_hide_behind_an_old_success(self):
        for kind in ("transfer", "delayed"):
            record = provisional()
            record["status"] = "secure"
            record["attempts"] += [attempt("delayed", "2026-09-12"),
                                   attempt(kind, "2026-09-13", outcome="retry")]
            self.add_record(record)
            with self.subTest(kind=kind), self.assertRaises(ProgressError):
                self.check()
            record["status"] = "review_needed"
            self.check()
            self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["kind"], "repair")

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

    def test_due_review_takes_priority(self):
        self.add_record(provisional())
        self.state["reviews"] = [{"lesson_id": "P1-01", "due_on": "2026-09-14", "reason": "Recall check"}]
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["kind"], "review")
        self.state["reviews"][0]["due_on"] = "2026-09-15"
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["lesson_id"], "P1-02")

    def test_duplicate_review_is_rejected(self):
        review = {"lesson_id": "P1-01", "due_on": "2026-09-15", "reason": "Recall"}
        self.state["reviews"] = [review, dict(review)]
        with self.assertRaisesRegex(ProgressError, "duplicate"):
            self.check()

    def test_capstone_required_before_next_phase(self):
        self.state["updated_on"] = "2026-09-14"
        for lesson in CATALOG["lessons"]:
            if lesson["phase"] == 1:
                self.state["lessons"][lesson["id"]] = provisional()
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["kind"], "capstone")
        self.state["capstones"]["1"] = {"status": "complete", "completed_on": "2026-09-14",
                                            "support": "reference", "evidence": ["Synthetic capstone review."]}
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["lesson_id"], "P2-01")

    def test_completed_capstone_cannot_be_based_only_on_a_solution(self):
        self.state["capstones"]["1"] = {"status": "complete", "completed_on": "2026-09-14",
                                            "support": "solution", "evidence": ["Copied solution."]}
        with self.assertRaisesRegex(ProgressError, "independent evidence"):
            self.check()

    def test_optional_specialties_are_not_forced_into_core_route(self):
        self.state["updated_on"] = "2026-09-14"
        for lesson in CATALOG["lessons"]:
            if lesson["phase"] in {1, 2, 3, 4} or lesson["id"] in {"P5-01", "P5-02", "P5-03"}:
                self.state["lessons"][lesson["id"]] = provisional()
        for phase in range(1, 5):
            self.state["capstones"][str(phase)] = {"status": "complete", "completed_on": "2026-09-14",
                                                  "support": "none", "evidence": ["Synthetic reviewed capstone."]}
        self.assertEqual(recommend(self.state, CATALOG, today=TODAY)["lesson_id"], "P5-06")
