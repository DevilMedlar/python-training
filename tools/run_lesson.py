"""Run the committed browser workspace and summarize its observed result.

This executes repository code on the current runner. It is not a sandbox for
untrusted programs. GitHub supplies the disposable machine and job deadline.
"""

from dataclasses import dataclass
from html import escape
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_LIMIT = 64 * 1024
RESULT_LIMIT = 8 * 1024


@dataclass
class LessonResult:
    exit_code: int
    stdout: str
    stderr: str
    timed_out: bool = False


def read_preview(path, limit):
    with path.open("rb") as stream:
        raw = stream.read(limit + 1)
    text = raw[:limit].decode("utf-8", errors="replace")
    if len(raw) > limit:
        text += f"\n[Preview truncated at {limit} bytes; do not use as a complete file.]\n"
    return text


def run_program(root=ROOT, *, timeout=30):
    root = Path(root).resolve()
    workspace = root / "workspace"
    if not (workspace / "main.py").is_file():
        return LessonResult(2, "", "Missing workspace/main.py. Create and commit it in github.dev.\n")
    if not (workspace / "input.txt").is_file():
        return LessonResult(2, "", "Missing workspace/input.txt. Commit an empty file when no input is needed.\n")
    (workspace / "results").mkdir(exist_ok=True)
    env = dict(os.environ, PYTHONUNBUFFERED="1", PYTHONIOENCODING="utf-8")
    # Program text is displayed by this runner; it should not append its own
    # output directly to GitHub's summary or workflow command files.
    for key in ("GITHUB_STEP_SUMMARY", "GITHUB_ENV", "GITHUB_OUTPUT", "GITHUB_PATH"):
        env.pop(key, None)
    with tempfile.TemporaryDirectory() as temporary:
        output = Path(temporary) / "stdout.txt"
        errors = Path(temporary) / "stderr.txt"
        timed_out = False
        with (workspace / "input.txt").open("rb") as input_stream, \
                output.open("wb") as output_stream, errors.open("wb") as error_stream:
            try:
                result = subprocess.run(
                    [sys.executable, "-m", "workspace.main"], cwd=root, env=env,
                    stdin=input_stream, stdout=output_stream, stderr=error_stream,
                    timeout=timeout, check=False,
                )
                exit_code = result.returncode
            except subprocess.TimeoutExpired:
                timed_out = True
                exit_code = 124
        stdout = read_preview(output, OUTPUT_LIMIT)
        stderr = read_preview(errors, OUTPUT_LIMIT)
    if timed_out:
        stderr += f"\nStopped after {timeout:g} seconds. Check loop termination and workload size.\n"
    if "EOFError" in stderr:
        stderr += "\nAdd enough answers to workspace/input.txt; Actions cannot accept live typing.\n"
    return LessonResult(exit_code, stdout, stderr, timed_out)


def render_summary(result, root=ROOT):
    status = "timed out" if result.timed_out else "completed" if result.exit_code == 0 else "failed"
    lines = ["## Python lesson result", "",
             f"Program **{status}** with exit code `{result.exit_code}`.", "",
             f"Interpreter: Python {sys.version.split()[0]}. Source: `workspace/main.py`.", ""]
    for label, content in (("Program output", result.stdout), ("Program errors", result.stderr)):
        lines += [f"### {label}", "", f"<pre>{escape(content or '(none)')}</pre>", ""]
    results = Path(root) / "workspace" / "results"
    if results.is_dir():
        files = [p for p in sorted(results.rglob("*"))
                 if p.is_file() and not p.is_symlink()
                 and p.resolve().is_relative_to(results.resolve())
                 and p.suffix.lower() in {".txt", ".json", ".csv", ".md"}]
        if files:
            lines += ["### Generated file previews", "",
                      "These files exist on this runner only. They have not been committed to GitHub.", ""]
            for path in files[:10]:
                label = escape(path.relative_to(Path(root)).as_posix())
                lines += [f"<p>{label}</p>", f"<pre>{escape(read_preview(path, RESULT_LIMIT))}</pre>", ""]
            if len(files) > 10:
                lines += ["Only the first 10 matching result files are previewed.", ""]
    lines += ["A successful run shows execution completed; compare its behavior with your prediction.", ""]
    return "\n".join(lines)


def main():
    result = run_program()
    print(f"Python {sys.version.split()[0]} — workspace/main.py — exit code {result.exit_code}")
    # Prefix each line so printed Python strings cannot be interpreted as GitHub
    # workflow commands such as ::error::. The summary retains the exact text.
    for label, content in (("OUTPUT", result.stdout), ("ERROR", result.stderr)):
        for line in content.splitlines():
            print(f"{label}: {line}")
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with Path(summary_path).open("a", encoding="utf-8") as stream:
            stream.write(render_summary(result))
    return result.exit_code if result.exit_code >= 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
