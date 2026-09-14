import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools.run_tests import run_suite


ROOT = Path(__file__).resolve().parents[1]


class TestRunnerTests(unittest.TestCase):
    def test_empty_suite_fails_instead_of_claiming_success(self):
        output = io.StringIO()
        self.assertEqual(run_suite(unittest.TestSuite(), stream=output), 2)
        self.assertIn("No tests discovered", output.getvalue())

    def test_a_real_assertion_failure_changes_exit_status(self):
        def broken_behavior():
            raise AssertionError("Synthetic regression")

        passing = unittest.TestSuite([unittest.FunctionTestCase(lambda: None)])
        failing = unittest.TestSuite([unittest.FunctionTestCase(broken_behavior)])
        self.assertEqual(run_suite(passing, stream=io.StringIO()), 0)
        self.assertEqual(run_suite(failing, stream=io.StringIO()), 1)

    def test_command_line_missing_pattern_cannot_pass(self):
        with tempfile.TemporaryDirectory() as temporary:
            result = subprocess.run([sys.executable, str(ROOT / "tools/run_tests.py"),
                                     "--start", temporary, "--pattern", "test_absent*.py"],
                                    capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 2)
        self.assertIn("No tests discovered", result.stderr)
