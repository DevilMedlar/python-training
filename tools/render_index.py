"""Render one Python lesson route with its embedded GitHub practice."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def render(catalog):
    by_id = {lesson["id"]: lesson for lesson in catalog["lessons"]}
    lines = ["# Python and GitHub lesson index", "",
             "Generated from [catalog.json](catalog.json). Follow one Python sequence.",
             "Each lesson uses GitHub on that same Python exercise. Open its GitHub",
             "references only when needed; they are not another curriculum.", "",
             "Edit in github.dev and inspect execution on github.com through GitHub Actions.",
             "Start with [your first edit and run](../START_HERE.md).", ""]
    for phase in catalog["phases"]:
        lines += [f"## Phase {phase['id']} {phase['title']}", "",
                  "| Lesson | Python focus | GitHub practiced in that lesson | Prerequisites | Route |",
                  "|---|---|---|---|---|"]
        for lesson in catalog["lessons"]:
            if lesson["phase"] != phase["id"]:
                continue
            path = Path(lesson["path"]).name
            prerequisites = ", ".join(lesson["prerequisites"]) or "None"
            skills = ", ".join(f"[{by_id[ident]['title']}](github.md#{by_id[ident]['anchor']})" for ident in lesson["github_skills"])
            lines.append(f"| [{lesson['id']}]({path}#{lesson['anchor']}) | {lesson['title']} | "
                         f"{skills} | {prerequisites} | {'Core' if lesson['core'] else 'Optional specialty'} |")
        lines += ["", f"Phase checkpoint: [Python capstone with GitHub review evidence](../{phase['capstone']}).", ""]
    lines += ["Use the [GitHub reference](github.md) and [browser task cards](../practice/GITHUB_LABS.md)",
              "within the linked Python task. There is one progress record and five phase capstones.", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    catalog = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
    (ROOT / "curriculum/INDEX.md").write_text(render(catalog), encoding="utf-8")
    print("Rendered curriculum/INDEX.md")
