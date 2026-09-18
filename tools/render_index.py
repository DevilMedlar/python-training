"""Render Python lessons with small Codespaces controls and optional repo cards."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def render(catalog):
    lines = ["# Python lesson index", "",
             "Generated from [catalog.json](catalog.json). Follow one Python sequence.",
             f"Write and run Python in [your Codespace]({catalog['workspace_url']}).",
             "Use the small workspace control hint when you need it.", "",
             "[Workspace guide](../START_HERE.md). Lessons begin only when learning is requested.", ""]
    for phase in catalog["phases"]:
        lines += [f"## Phase {phase['id']} {phase['title']}", "",
                  "| Lesson | Python focus | Workspace control | Route |",
                  "|---|---|---|---|"]
        for lesson in catalog["lessons"]:
            if lesson["phase"] != phase["id"]:
                continue
            path = Path(lesson["path"]).name
            shortcut = lesson["workspace_shortcut"].replace("|", "\\|").replace("\n", " ")
            lines.append(f"| [{lesson['id']}]({path}#{lesson['anchor']}) | {lesson['title']} | "
                         f"{shortcut} | {'Core' if lesson['core'] else 'Optional specialty'} |")
        lines += ["", f"Optional phase project: [build with what you learned](../{phase['capstone']}).", ""]
    lines += ["## Repository lessons", "",
              "[Optional repository lessons](github.md) cover settings, licenses, `.gitignore`,",
              "and other repository tasks on github.com. They are independent of Python progress.", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    catalog = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
    (ROOT / "curriculum/INDEX.md").write_text(render(catalog), encoding="utf-8")
    print("Rendered curriculum/INDEX.md")
