"""Phase 1 reference with an optional safer-save extension.

One process owns one local JSON file. Replacement avoids truncating an old file
on a failed pre-replacement write; it does not guarantee crash durability or
coordinate simultaneous writers. Calculation functions do no terminal I/O.
"""

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile


def validate_sessions(sessions):
    if not isinstance(sessions, list):
        raise ValueError("saved data must be a list")
    if any(type(minutes) is not int or minutes <= 0 for minutes in sessions):
        raise ValueError("sessions must contain positive integers, excluding booleans")


def load_sessions(path):
    try:
        text = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return []
    sessions = json.loads(text)
    validate_sessions(sessions)
    return sessions


def save_sessions(path, sessions):
    """Validate, write a sibling temporary file, then replace the destination.

    The caller supplies an existing parent directory. A failed save propagates
    the error. This function does not merge histories or create backups.
    """
    validate_sessions(sessions)
    path = Path(path)
    text = json.dumps(sessions, indent=2) + "\n"
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent,
            prefix=f".{path.name}.", suffix=".tmp", delete=False,
        ) as stream:
            temporary_path = Path(stream.name)
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def summarize_sessions(sessions):
    validate_sessions(sessions)
    total = sum(sessions)
    return {
        "count": len(sessions),
        "total": total,
        "average": total / len(sessions) if sessions else 0.0,
    }


def read_minutes():
    while True:
        try:
            minutes = int(input("Minutes studied: "))
        except ValueError:
            print("Enter a whole number, such as 25.")
            continue
        if minutes <= 0:
            print("Minutes must be positive.")
            continue
        return minutes


def main(argv=None):
    parser = argparse.ArgumentParser(description="Track positive study durations.")
    parser.add_argument("--file", type=Path, default=Path("study_sessions.json"))
    args = parser.parse_args(argv)
    try:
        sessions = load_sessions(args.file)
    except (OSError, ValueError) as error:
        print(f"Could not load: {error}. Existing data was not overwritten.", file=sys.stderr)
        return 1
    try:
        while True:
            print("\n1. Add session\n2. Show summary\n3. Save and quit")
            choice = input("Choose 1, 2, or 3: ").strip()
            if choice == "1":
                sessions.append(read_minutes())
            elif choice == "2":
                summary = summarize_sessions(sessions)
                print(f"Sessions: {summary['count']}; total: {summary['total']} min; "
                      f"average: {summary['average']:.1f} min")
            elif choice == "3":
                try:
                    save_sessions(args.file, sessions)
                except OSError as error:
                    print(f"Could not save: {error}. You can retry.", file=sys.stderr)
                    continue
                print(f"Saved to {args.file.resolve()}")
                return 0
            else:
                print("Choose 1, 2, or 3.")
    except (EOFError, KeyboardInterrupt):
        print("\nStopped. Changes since the last save were not saved.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
