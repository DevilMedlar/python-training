"""CSV reporting reference; see practice/CAPSTONES.md for the exact contract.

This teaching application materializes rows. It is suitable for modest local
files, not unbounded input. No partial success summary is printed on parse failure.
"""

import argparse
from collections.abc import Iterable
import csv
from dataclasses import dataclass
from pathlib import Path
import re
import sys


MAX_MINUTES = 999_999_999


@dataclass(frozen=True, slots=True)
class Session:
    topic: str
    minutes: int

    def __post_init__(self) -> None:
        if not isinstance(self.topic, str):
            raise TypeError("topic must be text")
        if not self.topic.strip() or self.topic != self.topic.strip():
            raise ValueError("topic must be nonblank with trimmed edges")
        if type(self.minutes) is not int:
            raise TypeError("minutes must be an integer, excluding booleans")
        if not 0 <= self.minutes <= MAX_MINUTES:
            raise ValueError(f"minutes must be between 0 and {MAX_MINUTES}")


def parse_minutes(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("minutes input must be text")
    cleaned = text.strip()
    if re.fullmatch(r"[0-9]{1,9}", cleaned) is None:
        raise ValueError("minutes must contain 1 to 9 ASCII digits")
    return int(cleaned)


def read_sessions(path: Path) -> list[Session]:
    sessions = []
    with Path(path).open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source, strict=True)
        if reader.fieldnames != ["topic", "minutes"]:
            raise ValueError("CSV header must be exactly: topic,minutes")
        for row in reader:
            location = f"near line {reader.line_num}"
            if None in row or row.get("topic") is None or row.get("minutes") is None:
                raise ValueError(f"{location}: expected exactly two fields")
            try:
                sessions.append(Session(row["topic"].strip(), parse_minutes(row["minutes"])))
            except (TypeError, ValueError) as error:
                raise ValueError(f"{location}: {error}") from error
    return sessions


def summarize(sessions: Iterable[Session]) -> dict[str, int]:
    totals: dict[str, int] = {}
    for session in sessions:
        totals[session.topic] = totals.get(session.topic, 0) + session.minutes
    return totals


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Summarize study minutes by topic.")
    parser.add_argument("input", type=Path, help="UTF-8 CSV with topic,minutes header")
    args = parser.parse_args(argv)
    try:
        totals = summarize(read_sessions(args.input))
    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    for topic, minutes in sorted(totals.items()):
        print(f"{topic}: {minutes} min")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
