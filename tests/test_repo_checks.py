from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from tools.check_repo import CheckError, anchors, check_links, check_python_blocks, validate_catalog


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
