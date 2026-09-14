"""Observe Git behavior in disposable local repositories; no GitHub/network access.

Requires Git with switch/restore and init -b support (Git 2.28+). Every modified
file, remote, configuration file, and ref lives in this run's temporary directory.
The checks test Git invariants, not platform-specific status wording or commit IDs.
"""

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def run_lab():
    executable = shutil.which("git")
    if executable is None:
        raise RuntimeError("Git is required for this optional GitHub companion lab")
    observations = []
    with tempfile.TemporaryDirectory(prefix="python-tutor-git-") as temporary:
        root = Path(temporary)
        hooks = root / "empty-hooks"
        hooks.mkdir()
        config = root / "empty-gitconfig"
        config.write_text("", encoding="utf-8")
        env = {key: value for key, value in os.environ.items() if not key.upper().startswith("GIT_")}
        env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=str(config),
                   GIT_TERMINAL_PROMPT="0", GIT_EDITOR="true", GIT_MERGE_AUTOEDIT="no")

        def git(where, *args, succeeds=True):
            result = subprocess.run([
                executable, "-c", f"core.hooksPath={hooks.as_posix()}",
                "-c", f"core.excludesFile={config.as_posix()}",
                "-c", "core.autocrlf=false", "-c", "commit.gpgsign=false",
                "-c", f"init.templateDir={hooks.as_posix()}",
                "-c", "user.name=Python Tutor Lab", "-c", "user.email=tutor@example.invalid",
                *args,
            ], cwd=where, env=env, capture_output=True, text=True, encoding="utf-8", timeout=20)
            require((result.returncode == 0) == succeeds,
                    f"Unexpected result from git {' '.join(args)}: {result.stderr}")
            return result.stdout

        def write(where, name, contents):
            (where / name).write_text(contents, encoding="utf-8", newline="")

        remote, work, peer = (root / name for name in ("remote.git", "work", "peer"))
        git(root, "init", "--bare", "-b", "main", str(remote))
        git(root, "clone", str(remote), str(work))
        write(work, "README.md", "one\n")
        write(work, ".gitignore", ".env\n.env.*\n!.env.example\n")
        git(work, "add", "README.md", ".gitignore")
        git(work, "commit", "-m", "Create practice history")
        git(work, "push", "-u", "origin", "main")
        initial = git(work, "rev-parse", "HEAD").strip()
        git(work, "switch", "-c", "practice/change")
        write(work, "README.md", "two\n")
        git(work, "add", "README.md")
        write(work, "README.md", "three\n")
        require(git(work, "show", ":README.md") == "two\n", "Index did not preserve staged content")
        git(work, "commit", "-m", "Record staged version")
        require(git(work, "show", "HEAD:README.md") == "two\n", "Commit included unstaged content")
        require((work / "README.md").read_text() == "three\n", "Working edit was lost")
        require(git(remote, "rev-parse", "main").strip() == initial, "Local commit changed remote main")
        observations.append("A commit records staged content; local work does not move remote main.")

        git(work, "add", "README.md")
        git(work, "restore", "--staged", "--", "README.md")
        require((work / "README.md").read_text() == "three\n", "Unstaging discarded working content")
        require(git(work, "diff", "--staged") == "", "Unstaging left a staged change")
        git(work, "restore", "--", "README.md")
        require((work / "README.md").read_text() == "two\n", "Restore did not use the index")
        observations.append("Unstage preserves working edits; plain restore replaces them from the index.")

        write(work, "README.md", "paused\n")
        write(work, "notes.txt", "untracked practice note\n")
        write(work, ".env", "SYNTHETIC_PLACEHOLDER=only\n")
        write(work, ".env.example", "SETTING=placeholder\n")
        require(git(work, "check-ignore", ".env").strip() == ".env", "Ignore rule missed .env")
        git(work, "check-ignore", ".env.example", succeeds=False)
        git(work, "stash", "push", "-u", "-m", "Pause synthetic practice work")
        require(not (work / "notes.txt").exists() and (work / ".env").exists(), "Stash inclusion was wrong")
        git(work, "stash", "apply", "stash@{0}")
        require((work / "README.md").read_text() == "paused\n" and (work / "notes.txt").exists(),
                "Stash did not restore work")
        require(bool(git(work, "stash", "list").strip()), "Apply incorrectly removed stash")
        git(work, "restore", "--", "README.md")
        (work / "notes.txt").unlink()
        (work / ".env.example").unlink()
        observations.append("Stash -u includes untracked files, excludes ignored files, and apply retains the stash.")

        git(work, "push", "-u", "origin", "practice/change")
        git(root, "clone", str(remote), str(peer))
        write(peer, "README.md", "peer\n")
        git(peer, "add", "README.md")
        git(peer, "commit", "-m", "Change the same goal upstream")
        git(peer, "push", "origin", "main")
        feature = git(work, "rev-parse", "HEAD").strip()
        git(work, "fetch", "origin")
        require(git(work, "rev-parse", "origin/main") == git(peer, "rev-parse", "HEAD"),
                "Fetch did not update the remote-tracking reference")
        require(git(work, "rev-parse", "HEAD").strip() == feature, "Fetch moved the current branch")
        git(work, "merge", "--ff-only", "origin/main", succeeds=False)
        require(git(work, "rev-parse", "HEAD").strip() == feature, "Refusal changed history")
        observations.append("Fetch preserves the current branch; a fast-forward-only merge refuses divergence.")

        git(work, "merge", "--no-edit", "origin/main", succeeds=False)
        require(bool(git(work, "ls-files", "--unmerged")), "Expected an actual merge conflict")
        git(work, "merge", "--abort")
        require((work / "README.md").read_text() == "two\n", "Clean-start abort did not restore the file")
        git(work, "merge", "--no-edit", "origin/main", succeeds=False)
        write(work, "README.md", "two and peer\n")
        git(work, "add", "README.md")
        git(work, "commit", "-m", "Reconcile both learning goals")
        require(len(git(work, "rev-list", "--parents", "-n", "1", "HEAD").split()) == 3,
                "Resolution did not retain two parents")
        observations.append("A clean-start conflict can be aborted, then resolved with both histories retained.")

        write(work, "README.md", "temporary mistake\n")
        git(work, "add", "README.md")
        git(work, "commit", "-m", "Make an ordinary practice mistake")
        mistake = git(work, "rev-parse", "HEAD").strip()
        git(work, "revert", "--no-edit", mistake)
        require((work / "README.md").read_text() == "two and peer\n", "Revert did not restore behavior")
        git(work, "merge-base", "--is-ancestor", mistake, "HEAD")
        git(work, "branch", "rescue", mistake)
        require(git(work, "rev-parse", "rescue").strip() == mistake, "Rescue ref points to wrong commit")
        observations.append("Revert preserves the original commit; a rescue branch names a recorded commit.")

        git(work, "push", "origin", "practice/change")
        mirror = root / "mirror.git"
        git(root, "clone", "--mirror", str(remote), str(mirror))
        git(mirror, "fsck", "--full")
        require(git(mirror, "rev-parse", "practice/change") == git(work, "rev-parse", "HEAD"),
                "Mirror did not retain the pushed feature history")
        restored = root / "restored"
        git(root, "clone", str(mirror), str(restored))
        git(restored, "switch", "--detach", git(work, "rev-parse", "HEAD").strip())
        require((restored / "README.md").read_text() == "two and peer\n",
                "Restoration from the mirror lost the final tracked content")
        observations.append("A fresh clone restores tracked content from a mirror; GitHub metadata is outside this experiment.")
        version = git(root, "--version").strip()
    return {"git": version, "checks": len(observations), "observations": observations,
            "scope": "Disposable local Git repositories only; no authentication, GitHub PR, or service settings tested."}


if __name__ == "__main__":
    print(json.dumps(run_lab(), indent=2))
