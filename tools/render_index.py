"""Render the lesson navigation table from the authoritative routing catalog."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def render(catalog):
    lines = ["# Lesson index", "", "Generated from [catalog.json](catalog.json). Stable IDs identify lessons across",
             "conversations. Read only the current phase and necessary prerequisites.",
             "The default route uses core lessons; specialist labs are optional.",
             "Each lesson has an objective, two practice tasks, hints, evidence, and sources.", ""]
    for phase in catalog["phases"]:
        lines += [f"## Phase {phase['id']} {phase['title']}", "",
                  "| Lesson | Focus | Prerequisites | Route |",
                  "|---|---|---|---|"]
        for lesson in catalog["lessons"]:
            if lesson["phase"] != phase["id"]:
                continue
            path = Path(lesson["path"]).name
            prerequisites = ", ".join(lesson["prerequisites"]) or "None"
            lines.append(f"| [{lesson['id']}]({path}#{lesson['anchor']}) | {lesson['title']} | "
                         f"{prerequisites} | {'Core' if lesson['core'] else 'Optional specialty'} |")
        lines += ["", f"Phase checkpoint: [capstone](../{phase['capstone']}).", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    catalog = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
    (ROOT / "curriculum/INDEX.md").write_text(render(catalog), encoding="utf-8")
    print("Rendered curriculum/INDEX.md")
