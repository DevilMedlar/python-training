from pathlib import Path
import tempfile
import unittest

from tools.run_lesson import LessonResult, read_preview, render_summary, run_program


class BrowserLessonTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.workspace = self.root / "workspace"
        self.workspace.mkdir()
        (self.workspace / "__init__.py").write_text("", encoding="utf-8")
        (self.workspace / "input.txt").write_text("", encoding="utf-8")

    def program(self, code, inputs=""):
        (self.workspace / "main.py").write_text(code, encoding="utf-8")
        (self.workspace / "input.txt").write_text(inputs, encoding="utf-8")

    def test_recorded_inputs_imports_and_file_result(self):
        (self.workspace / "helper.py").write_text("def double(n): return n * 2\n", encoding="utf-8")
        self.program(
            "from workspace.helper import double\n"
            "from pathlib import Path\n"
            "name = input()\n"
            "value = double(int(input()))\n"
            "print(f'{name}: {value}')\n"
            "Path('workspace/results/output.json').write_text(str(value))\n",
            "learner\n21\n",
        )
        result = run_program(self.root)
        self.assertEqual((result.exit_code, result.stdout, result.stderr), (0, "learner: 42\n", ""))
        self.assertIn("output.json", render_summary(result, self.root))
        self.assertEqual((self.workspace / "results/output.json").read_text(), "42")

    def test_missing_answer_fails_and_explains_batch_input(self):
        self.program("input()\ninput()\n", "only one\n")
        result = run_program(self.root)
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("EOFError", result.stderr)
        self.assertIn("workspace/input.txt", result.stderr)

    def test_syntax_error_and_explicit_failure_are_not_reported_as_success(self):
        for code in ("print('broken)\n", "raise SystemExit(7)\n"):
            with self.subTest(code=code):
                self.program(code)
                result = run_program(self.root)
                self.assertNotEqual(result.exit_code, 0)
                self.assertIn("**failed**", render_summary(result, self.root))

    def test_nonterminating_program_is_stopped(self):
        self.program("while True: pass\n")
        result = run_program(self.root, timeout=0.3)
        self.assertEqual(result.exit_code, 124)
        self.assertTrue(result.timed_out)
        self.assertIn("Stopped after", result.stderr)

    def test_missing_workspace_files_are_actionable_failures(self):
        self.assertIn("main.py", run_program(self.root).stderr)
        self.program("print(1)\n")
        (self.workspace / "input.txt").unlink()
        self.assertIn("input.txt", run_program(self.root).stderr)

    def test_preview_limits_are_explicit_and_summary_escapes_program_text(self):
        path = self.workspace / "large.txt"
        path.write_text("abcdefghij", encoding="utf-8")
        preview = read_preview(path, 4)
        self.assertTrue(preview.startswith("abcd\n"))
        self.assertIn("truncated", preview)
        summary = render_summary(LessonResult(0, "</pre><script>bad()</script>", ""), self.root)
        self.assertNotIn("<script>", summary)
        self.assertIn("&lt;script&gt;", summary)
