"""Offline curriculum integrity and executable Markdown checks.

Runs repository-authored examples in fresh subprocesses with a timeout. This is
not a sandbox for untrusted learner programs. No network checks are performed.
"""

import ast
from datetime import date
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_URL = "https://supreme-fishstick-5g5gxqwrgjrpcp777.github.dev/"
if __package__ in {None, ""}:
    sys.path.insert(0, str(ROOT))
from tools.progress import validate_state
from tools.render_index import render


class CheckError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise CheckError(message)


def slug(text):
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def without_fences(text):
    lines = []
    inside = False
    for line in text.splitlines():
        if line.startswith("```"):
            inside = not inside
        elif not inside:
            lines.append(line)
    require(not inside, "unclosed Markdown fence")
    return "\n".join(lines)


def anchors(text):
    counts = {}
    content = without_fences(text)
    found = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']\s*>', content))
    for heading in re.findall(r"^#{1,6} (.+)$", content, re.M):
        base = slug(heading)
        number = counts.get(base, 0)
        found.add(base if number == 0 else f"{base}-{number}")
        counts[base] = number + 1
    return found


def validate_catalog(catalog):
    require(catalog.get("catalog_version") == "1.3", "unsupported catalog version")
    require(catalog.get("minimum_python") == "3.12", "review changes to minimum Python explicitly")
    require(catalog.get("workspace_url") == WORKSPACE_URL, "workspace URL must use the learner's Codespace")
    require(catalog.get("compatible_progress_versions") == ["1.0", "1.1", "1.2"],
            "historical progress versions must remain readable")
    require(catalog.get("legacy_reference_ids") == [f"GH-{number:02}" for number in range(1, 17)],
            "historical GitHub reference IDs must remain readable")
    require("github" in catalog.get("legacy_capstones", []), "historical GitHub capstone must remain readable")
    phases = catalog.get("phases")
    lessons = catalog.get("lessons")
    require(isinstance(phases, list) and isinstance(lessons, list), "catalog phases/lessons must be lists")
    require([phase["id"] for phase in phases] == [1, 2, 3, 4, 5], "phase identities or order changed")
    ids = [lesson["id"] for lesson in lessons]
    require(len(set(ids)) == len(ids), "duplicate lesson ID")
    require(ids == sorted(ids), "lesson order must be stable")
    require(not catalog.get("tracks"), "separate curriculum tracks are not supported")
    by_id = {lesson["id"]: lesson for lesson in lessons}
    for lesson in lessons:
        ident = lesson["id"]
        require(type(lesson["core"]) is bool, f"core must be boolean: {ident}")
        require(re.fullmatch(r"P[1-5]-\d{2}", ident), f"Python route contains a non-Python lesson: {ident}")
        require(type(lesson["phase"]) is int and lesson["phase"] == int(ident[1]),
                f"phase mismatch: {ident}")
        require(lesson.get("track") is None, f"Python lesson has a separate track: {ident}")
        require(not {"github_skills", "github_task", "github_evidence"} & lesson.keys(),
                f"obsolete GitHub requirements in Python lesson: {ident}")
        require(isinstance(lesson.get("workspace_shortcut"), str) and lesson["workspace_shortcut"].strip(),
                f"missing workspace shortcut: {ident}")
        validate_metadata(lesson)
        require(len(set(lesson["prerequisites"])) == len(lesson["prerequisites"]), f"duplicate prerequisite: {ident}")
        for prerequisite in lesson["prerequisites"]:
            require(prerequisite in by_id, f"unknown prerequisite {prerequisite} in {ident}")
            require(prerequisite != ident, f"self prerequisite: {ident}")
            if lesson["core"]:
                require(by_id[prerequisite]["core"], f"core lesson depends on optional lab: {ident}")
    visited, visiting = set(), set()

    def visit(ident):
        require(ident not in visiting, f"prerequisite cycle at {ident}")
        if ident in visited:
            return
        visiting.add(ident)
        for prerequisite in by_id[ident]["prerequisites"]:
            visit(prerequisite)
        visiting.remove(ident)
        visited.add(ident)

    for ident in ids:
        visit(ident)
    repository_lessons = catalog.get("repository_lessons", [])
    require(isinstance(repository_lessons, list), "repository_lessons must be a list")
    repository_ids = [lesson["id"] for lesson in repository_lessons]
    require(len(repository_ids) == len(set(repository_ids)), "duplicate repository lesson ID")
    for lesson in repository_lessons:
        ident = lesson["id"]
        require(re.fullmatch(r"REPO-\d{2}", ident), f"invalid repository lesson ID: {ident}")
        require(not lesson.get("prerequisites"), f"repository lesson must have no Python prerequisites: {ident}")
        require(not lesson.get("core"), f"repository lesson cannot join the Python core route: {ident}")
        validate_metadata(lesson)
    return catalog


def validate_metadata(lesson):
    ident = lesson["id"]
    for field in ("objective", "title", "path", "anchor"):
        require(isinstance(lesson.get(field), str) and lesson[field].strip(),
                f"missing {field}: {ident}")
    sources = lesson.get("source_ids")
    require(isinstance(sources, list) and sources and
            all(isinstance(item, str) and item.strip() for item in sources) and
            len(sources) == len(set(sources)), f"missing or duplicate source mapping: {ident}")


def check_catalog_documents(catalog, sources, root):
    """Check Python lesson and optional repository-card metadata against content."""
    for lesson in [*catalog["lessons"], *catalog.get("repository_lessons", [])]:
        path = (root / lesson["path"]).resolve()
        require(path.is_relative_to(root.resolve()), f"lesson path leaves repository: {lesson['id']}")
        content = path.read_text(encoding="utf-8")
        heading = f"## {lesson['id']} {lesson['title']}"
        require(heading + "\n" in content, f"lesson heading mismatch: {lesson['id']}")
        body = content.split(heading + "\n", 1)[1].split("\n## ", 1)[0]
        if lesson["id"].startswith("REPO-"):
            fields = ("Outcome", "Practice", "Sources")
        else:
            fields = ("Prerequisites", "Outcome", "Practice A", "Practice B", "Hints", "Evidence", "Sources")
            require(f"**Workspace shortcut:** {lesson['workspace_shortcut']}" in body,
                    f"workspace shortcut drift: {lesson['id']}")
            require("```python" in body or "**Worked example:**" in body,
                    f"missing example: {lesson['id']}")
            prerequisites = re.search(r"\*\*Prerequisites:\*\* ([^\n]+)", body)
            require(prerequisites is not None, f"missing Prerequisites in {lesson['id']}")
            require(re.findall(r"\b[A-Z][A-Z0-9]*-\d{2}\b", prerequisites.group(1)) == lesson["prerequisites"],
                    f"prerequisite drift: {lesson['id']}")
        for field in fields:
            require(f"**{field}:**" in body, f"missing {field} in {lesson['id']}")
        actual_sources = re.findall(r"\[([A-Z][A-Z0-9-]+)\]\(\.\./audit/SOURCES", body)
        require(actual_sources == lesson["source_ids"], f"source mapping drift: {lesson['id']}")
        require(all(ident in sources for ident in actual_sources), f"unknown source: {lesson['id']}")
        require(lesson["anchor"] == slug(f"{lesson['id']} {lesson['title']}") and
                lesson["anchor"] in anchors(content), f"lesson anchor mismatch: {lesson['id']}")


def check_links(path, root):
    count = 0
    for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", without_fences(path.read_text(encoding="utf-8"))):
        parts = urlsplit(target)
        if parts.scheme or parts.netloc:
            continue
        destination = (path.parent / unquote(parts.path)).resolve() if parts.path else path.resolve()
        require(destination.is_relative_to(root.resolve()), f"link leaves repository: {path}: {target}")
        require(destination.exists(), f"missing link: {path.name}: {target}")
        if parts.fragment:
            require(destination.suffix == ".md", f"unsupported local anchor target: {target}")
            require(unquote(parts.fragment) in anchors(destination.read_text(encoding="utf-8")),
                    f"missing anchor: {path.name}: {target}")
        count += 1
    return count


def check_python_blocks(path):
    content = path.read_text(encoding="utf-8")
    count = 0
    for match in re.finditer(r"^```python\n(.*?)^```[ \t]*$", content, re.M | re.S):
        code = match.group(1)
        line = content[:match.start()].count("\n") + 1
        ast.parse(code, filename=f"{path}:{line}")
        expected = re.match(r"\s*```output\n(.*?)\n```", content[match.end():], re.S)
        require(expected is not None, f"runnable block needs explicit output: {path}:{line}")
        with tempfile.TemporaryDirectory() as temporary:
            result = subprocess.run([sys.executable, "-I", "-c", code], cwd=temporary,
                                    capture_output=True, text=True, encoding="utf-8", timeout=10)
        require(result.returncode == 0, f"example failed: {path}:{line}\n{result.stderr}")
        require(not result.stderr, f"example produced unexpected stderr: {path}:{line}\n{result.stderr}")
        require(result.stdout == expected.group(1) + "\n", f"output mismatch: {path}:{line}\n"
                f"expected {expected.group(1)!r}; got {result.stdout!r}")
        count += 1
    return count


def check_repo(root=ROOT):
    require(sys.version_info >= (3, 12), "Use Python 3.12 or newer for this repository")
    catalog = validate_catalog(json.loads((root / "curriculum/catalog.json").read_text(encoding="utf-8")))
    registry = json.loads((root / "audit/sources.json").read_text(encoding="utf-8"))
    sources = {source["id"]: source for source in registry["sources"]}
    require(len(sources) == len(registry["sources"]), "duplicate source ID")
    for source in sources.values():
        require(source["url"].startswith("https://"), f"invalid source URL: {source['id']}")
        date.fromisoformat(source["reviewed_on"])
        require(source["scope"].strip(), f"missing source scope: {source['id']}")
    check_catalog_documents(catalog, sources, root)
    require((root / "curriculum/INDEX.md").read_text(encoding="utf-8") == render(catalog),
            "index is stale: run python tools/render_index.py")
    for template in ("progress-template.json", "github-progress-template.json", "progress.json"):
        validate_state(json.loads((root / "tutor" / template).read_text(encoding="utf-8")), catalog)
    markdown_files = [path for path in root.rglob("*.md") if not any(
        part in {".git", ".venv", "progress", "__pycache__"} for part in path.relative_to(root).parts)]
    links = sum(check_links(path, root) for path in markdown_files)
    snippets = sum(check_python_blocks(path) for path in markdown_files)
    python_files = [path for folder in ("examples", "tests", "tools") for path in (root / folder).rglob("*.py")]
    for path in python_files:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return {"python_lessons": sum(item["phase"] is not None for item in catalog["lessons"]),
            "repository_lessons": len(catalog.get("repository_lessons", [])),
            "legacy_github_ids": len(catalog.get("legacy_reference_ids", [])),
            "core_lessons": sum(item["core"] for item in catalog["lessons"]),
            "source_records": len(sources), "markdown_files": len(markdown_files),
            "internal_links": links, "executed_markdown_examples": snippets,
            "parsed_python_files": len(python_files)}


def main():
    try:
        print(json.dumps(check_repo(), indent=2))
    except (CheckError, OSError, ValueError, SyntaxError, subprocess.TimeoutExpired) as error:
        print(f"Repository check failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
