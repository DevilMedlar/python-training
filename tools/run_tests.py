"""Run repository tests and fail explicitly if discovery finds none."""

import argparse
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def run_suite(suite, *, stream=None):
    stream = stream if stream is not None else sys.stderr
    if suite.countTestCases() == 0:
        print("No tests discovered; check the start directory and pattern.", file=stream)
        return 2
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=Path, default=ROOT / "tests")
    parser.add_argument("--pattern", default="test*.py")
    args = parser.parse_args(argv)
    if not args.start.is_dir():
        parser.error("test start directory does not exist")
    suite = unittest.defaultTestLoader.discover(str(args.start.resolve()), pattern=args.pattern)
    return run_suite(suite)


if __name__ == "__main__":
    raise SystemExit(main())
