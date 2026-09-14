import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from examples import study_tracker as tracker


class TrackerTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.path = self.root / "sessions.json"

    def test_empty_and_known_summary(self):
        self.assertEqual(tracker.summarize_sessions([]), {"count": 0, "total": 0, "average": 0.0})
        self.assertEqual(tracker.summarize_sessions([20, 40]), {"count": 2, "total": 60, "average": 30.0})

    def test_missing_file_is_new_history(self):
        self.assertEqual(tracker.load_sessions(self.path), [])
        self.assertFalse(self.path.exists())

    def test_round_trip_and_no_temporary_leftovers(self):
        tracker.save_sessions(self.path, [20, 40])
        self.assertEqual(tracker.load_sessions(self.path), [20, 40])
        self.assertEqual(list(self.root.iterdir()), [self.path])

    def test_invalid_saved_shapes_and_values(self):
        for value in ({}, None, "text", [True], [0], [-1], [1.5], ["25"]):
            with self.subTest(value=value):
                self.path.write_text(json.dumps(value), encoding="utf-8")
                before = self.path.read_bytes()
                with self.assertRaises(ValueError):
                    tracker.load_sessions(self.path)
                self.assertEqual(self.path.read_bytes(), before)

    def test_invalid_json_and_encoding_are_visible(self):
        for contents in (b"[bad json", b"\xff"):
            with self.subTest(contents=contents):
                self.path.write_bytes(contents)
                with self.assertRaises(ValueError):
                    tracker.load_sessions(self.path)

    def test_validation_failure_preserves_previous_file(self):
        tracker.save_sessions(self.path, [10])
        before = self.path.read_bytes()
        with self.assertRaises(ValueError):
            tracker.save_sessions(self.path, [True])
        self.assertEqual(self.path.read_bytes(), before)

    def test_sync_failure_preserves_previous_file_and_cleans_temporary(self):
        tracker.save_sessions(self.path, [10])
        with patch.object(tracker.os, "fsync", side_effect=OSError("disk failure")):
            with self.assertRaises(OSError):
                tracker.save_sessions(self.path, [20])
        self.assertEqual(tracker.load_sessions(self.path), [10])
        self.assertEqual(list(self.root.iterdir()), [self.path])

    def test_replace_failure_preserves_previous_file_and_cleans_temporary(self):
        tracker.save_sessions(self.path, [10])
        with patch.object(tracker.os, "replace", side_effect=OSError("replace failure")):
            with self.assertRaises(OSError):
                tracker.save_sessions(self.path, [20])
        self.assertEqual(tracker.load_sessions(self.path), [10])
        self.assertEqual(list(self.root.iterdir()), [self.path])

    def test_nonexistent_parent_is_not_silently_created(self):
        with self.assertRaises(OSError):
            tracker.save_sessions(self.root / "missing" / "data.json", [10])

    def test_interactive_validation(self):
        with patch("builtins.input", side_effect=["bad", "0", "-1", "25"]), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(tracker.read_minutes(), 25)

    def test_load_failure_reports_failure_without_starting_menu(self):
        self.path.write_text("corrupt", encoding="utf-8")
        with patch("builtins.input") as input_mock, contextlib.redirect_stderr(io.StringIO()) as errors:
            self.assertEqual(tracker.main(["--file", str(self.path)]), 1)
        input_mock.assert_not_called()
        self.assertIn("not overwritten", errors.getvalue())
        self.assertEqual(self.path.read_text(), "corrupt")

    def test_menu_add_summary_save(self):
        with patch("builtins.input", side_effect=["1", "20", "1", "40", "2", "3"]), contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(tracker.main(["--file", str(self.path)]), 0)
        self.assertIn("total: 60", output.getvalue())
        self.assertEqual(tracker.load_sessions(self.path), [20, 40])

    def test_interruption_does_not_claim_save(self):
        with patch("builtins.input", side_effect=EOFError), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()) as errors:
            self.assertEqual(tracker.main(["--file", str(self.path)]), 2)
        self.assertIn("not saved", errors.getvalue())
        self.assertFalse(self.path.exists())
