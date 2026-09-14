"""Small teaching harness, not a universal ranking or calibrated performance study.

Run as a module. Correctness is checked outside timing. Each trial times both
public functions (including their validation), alternating which runs first.
Raw durations and order are retained. Use pyperf for stronger timing experiments.
"""

import argparse
import json
import platform
from random import Random
from time import perf_counter_ns

from examples.selection import candidate, reference


def run(size: int = 1000, k: int = 10, repeats: int = 6) -> dict:
    if any(type(value) is not int for value in (size, k, repeats)):
        raise TypeError("size, k, and repeats must be integers")
    if size < 0 or k < 0 or repeats < 1:
        raise ValueError("size/k must be nonnegative and repeats must be positive")
    seed = 20260914
    rng = Random(seed)
    values = [rng.randrange(-1000, 1001) for _ in range(size)]
    expected = sorted(values)[:k]
    functions = {"sort": reference, "heap": candidate}
    for function in functions.values():
        if function(values, k) != expected:
            raise RuntimeError("contract disagreement before benchmarking")
    rows = []
    for trial in range(repeats):
        order = ["sort", "heap"] if trial % 2 == 0 else ["heap", "sort"]
        for position, name in enumerate(order):
            start = perf_counter_ns()
            result = functions[name](values, k)
            elapsed = perf_counter_ns() - start
            if result != expected:
                raise RuntimeError("contract disagreement during benchmarking")
            rows.append({"trial": trial, "position": position, "method": name,
                         "duration_ns": elapsed})
    return {
        "python": platform.python_version(), "implementation": platform.python_implementation(),
        "platform": platform.platform(), "seed": seed, "size": size, "k": k,
        "repeats": repeats, "scope": "public function including validation; excludes input generation",
        "limitations": "one machine, one input family, no calibrated workers or memory measurement",
        "trials": rows,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=1000)
    parser.add_argument("--k", type=int, default=10)
    parser.add_argument("--repeats", type=int, default=6)
    args = parser.parse_args(argv)
    try:
        result = run(args.size, args.k, args.repeats)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
