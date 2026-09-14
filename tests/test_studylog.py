import csv
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from examples.studylog import Session, parse_minutes, read_sessions, summarize


ROOT = Path(__file__).resolve().parents[1]


class StudyLogTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.path = Path(temporary.name) / "sessions.csv"

    def write(self, contents):
        self.path.write_text(contents, encoding="utf-8")
        return self.path

    def cli(self, path=None):
        return subprocess.run([sys.executable, "-m", "examples.studylog", str(path or self.path)],
                              cwd=ROOT, capture_output=True, text=True, timeout=10)

    def test_valid_minutes(self):
        for raw, expected in [("0", 0), (" 25 ", 25), ("007", 7), ("999999999", 999999999)]:
            with self.subTest(raw=raw):
                self.assertEqual(parse_minutes(raw), expected)

    def test_invalid_minutes(self):
        for raw in ["", " ", "-1", "+2", "2.5", "1_000", "１２", "1e3", "1234567890"]:
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                parse_minutes(raw)

    def test_minutes_requires_text(self):
        for raw in [None, 25, True]:
            with self.subTest(raw=raw), self.assertRaises(TypeError):
                parse_minutes(raw)

    def test_direct_records_enforce_contract(self):
        for topic, minutes in [("", 2), (" x ", 2), ("x", -1), ("x", 10**9)]:
            with self.subTest(topic=topic, minutes=minutes), self.assertRaises(ValueError):
                Session(topic, minutes)
        for topic, minutes in [(None, 2), ("x", True), ("x", 2.0)]:
            with self.subTest(topic=topic, minutes=minutes), self.assertRaises(TypeError):
                Session(topic, minutes)

    def test_iterator_aggregation_duplicates_and_case(self):
        records = iter([Session("Python", 25), Session("Python", 35), Session("python", 0)])
        self.assertEqual(summarize(records), {"Python": 60, "python": 0})

    def test_quoted_commas_newlines_and_unicode(self):
        self.write('topic,minutes\n" Café, notes ",15\n"line one\nline two",3\n')
        self.assertEqual(read_sessions(self.path), [Session("Café, notes", 15), Session("line one\nline two", 3)])

    def test_header_only_and_blank_lines(self):
        self.write("topic,minutes\n\n")
        self.assertEqual(read_sessions(self.path), [])
        result = self.cli()
        self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "", ""))

    def test_invalid_headers(self):
        for contents in ["", "minutes,topic\n", "topic,minutes,extra\n", "topic,topic\n"]:
            with self.subTest(contents=contents), self.assertRaisesRegex(ValueError, "header"):
                read_sessions(self.write(contents))

    def test_invalid_rows_report_location(self):
        for row in ["Python\n", "Python,2,extra\n", " ,5\n", "Python,-1\n", "Python,\n"]:
            with self.subTest(row=row), self.assertRaisesRegex(ValueError, "line 2"):
                read_sessions(self.write("topic,minutes\n" + row))

    def test_malformed_csv(self):
        with self.assertRaises(csv.Error):
            read_sessions(self.write('topic,minutes\n"unterminated,20\n'))

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            read_sessions(self.path)
        result = self.cli()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")

    def test_cli_sorted_summary_and_input_preserved(self):
        self.write("topic,minutes\nTesting,20\nPython,25\nPython,35\n")
        before = self.path.read_bytes()
        result = self.cli()
        self.assertEqual((result.returncode, result.stdout, result.stderr),
                         (0, "Python: 60 min\nTesting: 20 min\n", ""))
        self.assertEqual(self.path.read_bytes(), before)

    def test_cli_bad_later_record_has_no_partial_summary(self):
        self.write("topic,minutes\nPython,25\nTesting,-1\n")
        result = self.cli()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertIn("Error:", result.stderr)

    def test_cli_invalid_encoding(self):
        self.path.write_bytes(b"topic,minutes\n\xff,1\n")
        result = self.cli()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertNotIn("Traceback", result.stderr)
