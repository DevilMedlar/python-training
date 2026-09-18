from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from tools.check_repo import (CheckError, anchors, check_catalog_documents, check_links,
                             check_python_blocks, validate_catalog)


ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))


class RepositoryCheckTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def test_cycle_is_rejected(self):
        catalog = deepcopy(CATALOG)
        catalog["lessons"][0]["prerequisites"] = ["P1-02"]
        with self.assertRaisesRegex(CheckError, "cycle"):
            validate_catalog(catalog)

    def test_non_python_reference_cannot_join_python_route(self):
        catalog = deepcopy(CATALOG)
        catalog["lessons"][0]["id"] = "GH-01"
        with self.assertRaisesRegex(CheckError, "non-Python"):
            validate_catalog(catalog)

    def test_missing_shortcut_or_obsolete_requirements_are_rejected(self):
        catalog = deepcopy(CATALOG)
        catalog["lessons"][0]["workspace_shortcut"] = ""
        with self.assertRaisesRegex(CheckError, "missing workspace shortcut"):
            validate_catalog(catalog)
        catalog = deepcopy(CATALOG)
        catalog["lessons"][0]["github_task"] = "Separate required GitHub exercise"
        with self.assertRaisesRegex(CheckError, "obsolete GitHub requirements"):
            validate_catalog(catalog)

    def test_wrong_workspace_is_rejected(self):
        catalog = deepcopy(CATALOG)
        catalog["workspace_url"] = "https://github.dev/DevilMedlar/python-training"
        with self.assertRaisesRegex(CheckError, "Codespace"):
            validate_catalog(catalog)

    def test_repository_lesson_cannot_require_python_progress(self):
        catalog = deepcopy(CATALOG)
        catalog["repository_lessons"] = [{"id": "REPO-01", "prerequisites": ["P1-01"]}]
        with self.assertRaisesRegex(CheckError, "no Python prerequisites"):
            validate_catalog(catalog)

    def test_historical_ids_are_not_lost(self):
        catalog = deepcopy(CATALOG)
        catalog["legacy_reference_ids"].remove("GH-04")
        with self.assertRaisesRegex(CheckError, "historical GitHub reference IDs"):
            validate_catalog(catalog)

    def test_unknown_and_duplicate_ids_are_rejected(self):
        catalog = deepcopy(CATALOG)
        catalog["lessons"][0]["prerequisites"] = ["P9-99"]
        with self.assertRaisesRegex(CheckError, "unknown prerequisite"):
            validate_catalog(catalog)
        catalog = deepcopy(CATALOG)
        catalog["lessons"].append(catalog["lessons"][0])
        with self.assertRaisesRegex(CheckError, "duplicate"):
            validate_catalog(catalog)

    def test_optional_prerequisite_cannot_silently_become_mandatory(self):
        catalog = deepcopy(CATALOG)
        lesson = next(item for item in catalog["lessons"] if item["id"] == "P5-06")
        lesson["prerequisites"] = ["P5-04"]
        with self.assertRaisesRegex(CheckError, "optional"):
            validate_catalog(catalog)

    def test_repository_card_heading_anchor_and_sources_are_checked(self):
        lesson = {"id": "REPO-01", "title": "A repository task", "path": "card.md",
                  "anchor": "repo-01-a-repository-task", "objective": "Complete a repository task",
                  "source_ids": ["TEST"]}
        catalog = {"lessons": [], "repository_lessons": [lesson]}
        path = self.root / "card.md"
        body = ("## REPO-01 A repository task\n\n**Outcome:** Complete a repository task\n\n"
                "**Practice:** Use the repository settings page.\n\n"
                "**Sources:** [TEST](../audit/SOURCES.md#test)\n")
        path.write_text(body, encoding="utf-8")
        check_catalog_documents(catalog, {"TEST": {}}, self.root)
        for field, value, message in (("title", "Different title", "heading"),
                                      ("anchor", "wrong-anchor", "anchor"),
                                      ("source_ids", ["OTHER"], "source mapping")):
            changed = deepcopy(catalog)
            changed["repository_lessons"][0][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(CheckError, message):
                check_catalog_documents(changed, {"TEST": {}}, self.root)
        with self.assertRaisesRegex(CheckError, "unknown source"):
            check_catalog_documents(catalog, {}, self.root)
        path.write_text(body.replace("**Practice:**", "**Notes:**"), encoding="utf-8")
        with self.assertRaisesRegex(CheckError, "missing Practice"):
            check_catalog_documents(catalog, {"TEST": {}}, self.root)

    def test_python_shortcut_drift_is_checked(self):
        lesson = deepcopy(CATALOG["lessons"][0])
        path = self.root / lesson["path"]
        path.parent.mkdir(parents=True)
        path.write_text((ROOT / lesson["path"]).read_text(encoding="utf-8"), encoding="utf-8")
        catalog = {"lessons": [lesson]}
        sources = {ident: {} for ident in lesson["source_ids"]}
        check_catalog_documents(catalog, sources, self.root)
        lesson["workspace_shortcut"] = "A mismatched control hint"
        with self.assertRaisesRegex(CheckError, "workspace shortcut drift"):
            check_catalog_documents(catalog, sources, self.root)

    def test_file_and_fragment_links(self):
        source = self.root / "source.md"
        destination = self.root / "target.md"
        destination.write_text("# A title\n\n## Second section\n", encoding="utf-8")
        source.write_text("[go](target.md#second-section)\n", encoding="utf-8")
        self.assertEqual(check_links(source, self.root), 1)
        source.write_text("[bad](target.md#missing)\n", encoding="utf-8")
        with self.assertRaisesRegex(CheckError, "missing anchor"):
            check_links(source, self.root)
        source.write_text("[bad](absent.md)\n", encoding="utf-8")
        with self.assertRaisesRegex(CheckError, "missing link"):
            check_links(source, self.root)

    def test_fenced_headings_do_not_create_anchors(self):
        self.assertEqual(anchors("# Real\n```python\n# Fake\n```\n# Real\n"), {"real", "real-1"})

    def test_explicit_legacy_anchors_remain_valid(self):
        content = '<a id="old-heading"></a>\n# New heading\n```html\n<a id="fake"></a>\n```\n'
        self.assertEqual(anchors(content), {"old-heading", "new-heading"})

    def test_unclosed_fence_is_rejected(self):
        with self.assertRaisesRegex(CheckError, "unclosed"):
            anchors("# A\n```python\nprint(1)\n")

    def test_executable_example_output_is_actually_checked(self):
        path = self.root / "lesson.md"
        path.write_text("```python\nprint(2 + 3)\n```\n\n```output\n5\n```\n", encoding="utf-8")
        self.assertEqual(check_python_blocks(path), 1)
        path.write_text("```python\nprint(2 + 3)\n```\n\n```output\n6\n```\n", encoding="utf-8")
        with self.assertRaisesRegex(CheckError, "output mismatch"):
            check_python_blocks(path)

    def test_example_without_output_or_with_failure_is_rejected(self):
        path = self.root / "lesson.md"
        path.write_text("```python\nprint(1)\n```\n", encoding="utf-8")
        with self.assertRaisesRegex(CheckError, "explicit output"):
            check_python_blocks(path)
        path.write_text("```python\nraise ValueError('bad')\n```\n\n```output\nanything\n```\n", encoding="utf-8")
        with self.assertRaisesRegex(CheckError, "example failed"):
            check_python_blocks(path)
