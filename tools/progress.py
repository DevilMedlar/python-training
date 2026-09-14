"""Validate an evidence-based progress record and suggest a conservative next task.

This tool validates consistency. It cannot verify whether a claimed attempt
actually happened or judge the learner's code. It never writes learner records.
"""

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
INDEPENDENT = {"none", "reference"}
STATUSES = {"not_started", "learning", "provisional", "secure", "review_needed"}


class ProgressError(ValueError):
    """The record is malformed or claims a status without required evidence."""


def require(condition, message):
    if not condition:
        raise ProgressError(message)


def keys(value, expected, where):
    require(isinstance(value, dict), f"{where} must be an object")
    require(set(value) == set(expected), f"{where} has missing or unknown fields")


def text_list(value, where):
    require(isinstance(value, list) and all(isinstance(item, str) and item.strip()
            for item in value), f"{where} must be a list of nonempty strings")


def iso_date(value, where, *, nullable=False):
    if value is None and nullable:
        return None
    require(isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value),
            f"{where} must be YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise ProgressError(f"{where} is not a valid date") from error


def validate_state(state, catalog, *, today=None):
    today = today or date.today()
    lessons = {lesson["id"]: lesson for lesson in catalog["lessons"]}
    keys(state, {"schema_version", "catalog_version", "updated_on", "environment",
                 "goals", "current_lesson", "lessons", "reviews", "capstones",
                 "next_task", "notes"}, "record")
    require(type(state["schema_version"]) is int and state["schema_version"] == 1,
            "unsupported schema_version")
    compatible = [catalog["catalog_version"], *catalog.get("compatible_progress_versions", [])]
    require(state["catalog_version"] in compatible, "catalog version mismatch")
    updated = iso_date(state["updated_on"], "updated_on", nullable=True)
    require(updated is None or updated <= today, "updated_on cannot be in the future")
    keys(state["environment"], {"os", "python", "command", "execution_available"}, "environment")
    for name in ("os", "python", "command"):
        value = state["environment"][name]
        require(value is None or isinstance(value, str) and value.strip(), f"environment.{name} is invalid")
    require(state["environment"]["execution_available"] is None or
            type(state["environment"]["execution_available"]) is bool,
            "execution_available must be boolean or null")
    text_list(state["goals"], "goals")
    text_list(state["notes"], "notes")
    require(isinstance(state["current_lesson"], str) and state["current_lesson"] in lessons,
            "unknown current lesson")
    require(isinstance(state["next_task"], str) and state["next_task"].strip(), "next_task is required")
    require(isinstance(state["lessons"], dict), "lessons must be an object")
    evidence_dates = []
    for lesson_id, record in state["lessons"].items():
        require(lesson_id in lessons, f"unknown lesson: {lesson_id}")
        keys(record, {"status", "attempts"}, lesson_id)
        require(isinstance(record["status"], str) and record["status"] in STATUSES,
                f"{lesson_id}: invalid status")
        require(isinstance(record["attempts"], list), f"{lesson_id}: attempts must be a list")
        passed = {kind: [] for kind in ("guided", "transfer", "explanation", "delayed")}
        for attempt in record["attempts"]:
            keys(attempt, {"kind", "performed_on", "outcome", "support", "summary"}, "attempt")
            kind = attempt["kind"]
            require(isinstance(kind, str) and kind in passed, "invalid attempt kind")
            require(isinstance(attempt["outcome"], str) and attempt["outcome"] in {"pass", "retry"},
                    "invalid outcome")
            require(isinstance(attempt["support"], str) and
                    attempt["support"] in INDEPENDENT | {"hint", "solution"}, "invalid support")
            require(isinstance(attempt["summary"], str) and attempt["summary"].strip(),
                    "attempt summary is required")
            performed = iso_date(attempt["performed_on"], "performed_on")
            require(performed <= today, "attempt cannot occur in the future")
            evidence_dates.append(performed)
            if attempt["outcome"] == "pass" and attempt["support"] in INDEPENDENT:
                passed[kind].append(performed)
        status = record["status"]
        if status == "not_started":
            require(not record["attempts"], f"{lesson_id}: not_started contradicts recorded attempts")
        elif status in {"learning", "review_needed"}:
            require(bool(record["attempts"]), f"{lesson_id}: record an observed attempt or gap")
        if status in {"provisional", "secure"}:
            require(passed["transfer"] and passed["explanation"],
                    f"{lesson_id}: independent transfer and explanation evidence required")
            checks = [(index, attempt) for index, attempt in enumerate(record["attempts"])
                      if attempt["kind"] in {"transfer", "delayed"}]
            latest_check = max(checks, key=lambda pair: (pair[1]["performed_on"], pair[0]))[1]
            require(latest_check["outcome"] == "pass" and latest_check["support"] in INDEPENDENT,
                    f"{lesson_id}: latest assessment requires repair or new independent evidence")
        if status == "secure":
            require(any(later > earlier for later in passed["delayed"] for earlier in passed["transfer"]),
                    f"{lesson_id}: secure requires an independent review on a later date")
            # A later unsuccessful independent check must not be hidden by an old success.
            reviews = [(index, attempt) for index, attempt in enumerate(record["attempts"])
                       if attempt["kind"] == "delayed"]
            latest_review = max(reviews, key=lambda pair: (pair[1]["performed_on"], pair[0]))[1]
            require(latest_review["outcome"] == "pass" and latest_review["support"] in INDEPENDENT,
                    f"{lesson_id}: latest delayed check does not support secure status")
    require(isinstance(state["reviews"], list), "reviews must be a list")
    seen_reviews = set()
    for review in state["reviews"]:
        keys(review, {"lesson_id", "due_on", "reason"}, "review")
        require(isinstance(review["lesson_id"], str) and review["lesson_id"] in lessons,
                "review references an unknown lesson")
        require(review["lesson_id"] not in seen_reviews, "duplicate scheduled review")
        seen_reviews.add(review["lesson_id"])
        iso_date(review["due_on"], "due_on")
        require(isinstance(review["reason"], str) and review["reason"].strip(), "review reason required")
    require(isinstance(state["capstones"], dict), "capstones must be an object")
    for phase, record in state["capstones"].items():
        capstone_ids = {str(item["id"]) for item in catalog["phases"]} | set(catalog.get("legacy_capstones", []))
        require(phase in capstone_ids, "unknown capstone phase or track")
        keys(record, {"status", "completed_on", "support", "evidence"}, "capstone")
        require(isinstance(record["status"], str) and
                record["status"] in {"not_started", "in_progress", "complete"}, "invalid capstone status")
        require(isinstance(record["support"], str) and
                record["support"] in INDEPENDENT | {"hint", "solution"}, "invalid capstone support")
        text_list(record["evidence"], "capstone evidence")
        completed = iso_date(record["completed_on"], "completed_on", nullable=True)
        require(completed is None or completed <= today, "capstone date cannot be in the future")
        if record["status"] == "complete":
            require(completed is not None and record["evidence"] and record["support"] in INDEPENDENT,
                    "completed capstone requires dated independent evidence")
            evidence_dates.append(completed)
        else:
            require(completed is None, "unfinished capstone cannot have a completion date")
    if evidence_dates:
        require(updated is not None and updated >= max(evidence_dates),
                "updated_on must include the latest recorded evidence")
    return state


def recommend(state, catalog, *, today=None, track=None):
    today = today or date.today()
    validate_state(state, catalog, today=today)
    # Retain compatibility with old callers without preserving a second course.
    require(track in {None, "github"}, "unknown track")
    by_id = {lesson["id"]: lesson for lesson in catalog["lessons"]}
    statuses = {key: value["status"] for key, value in state["lessons"].items()}
    ready = {key for key, value in statuses.items() if value in {"provisional", "secure"}}

    def task(kind, ident, **extra):
        lesson = by_id[ident]
        reference = None
        if lesson.get("kind") == "reference":
            reference = ident
            lesson = by_id[lesson["introduced_with"]]
        result = {"kind": kind, "lesson_id": lesson["id"],
                  "github_skills": list(lesson["github_skills"]),
                  "github_task": lesson["github_task"],
                  "github_evidence": lesson["github_evidence"], **extra}
        if reference:
            result["reference_id"] = reference
        return result

    due = [review for review in state["reviews"]
           if iso_date(review["due_on"], "due_on") <= today]
    if due:
        review = min(due, key=lambda item: (item["due_on"], item["lesson_id"]))
        return task("review", review["lesson_id"], reason=review["reason"])
    for lesson in catalog["lessons"]:
        if statuses.get(lesson["id"]) == "review_needed":
            return task("repair", lesson["id"])
    for phase in catalog["phases"]:
        for lesson in catalog["lessons"]:
            if lesson["phase"] != phase["id"] or not lesson["core"] or lesson["id"] in ready:
                continue
            missing = [item for item in lesson["prerequisites"] if item not in ready]
            if missing:
                return task("prerequisite", missing[0], needed_for=lesson["id"])
            return task("lesson", lesson["id"])
        if state["capstones"].get(str(phase["id"]), {}).get("status") != "complete":
            return {"kind": "capstone", "phase": phase["id"], "path": phase["capstone"],
                    "github_task": "Review the same Python capstone through its branch, PR, and observed Actions results."}
    return {"kind": "maintenance", "reason": "Continue delayed reviews and a chosen Python contribution on GitHub."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    parser.add_argument("--next", action="store_true", dest="show_next")
    parser.add_argument("--track", help="Legacy github value is an alias for the integrated Python route")
    args = parser.parse_args(argv)
    try:
        state = json.loads(args.record.read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
        validate_state(state, catalog)
        if args.track is not None:
            require(args.track == "github", "unknown track")
        print(json.dumps(recommend(state, catalog, track=args.track), indent=2)
              if args.show_next else "Progress record is consistent.")
    except (OSError, ValueError) as error:
        print(f"Invalid progress: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
