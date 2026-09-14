"""A synchronous, typed decorator with explicit reporting behavior."""

from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import ParamSpec, TypeVar


P = ParamSpec("P")
R = TypeVar("R")


def timed(
    sink: Callable[[str, float], None],
    *,
    clock: Callable[[], float] = perf_counter,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Record one duration after a synchronous call, including a failed call.

    Contract: sink and clock do not raise. If they violate that precondition,
    their exception can replace a target exception. This is explicitly not an
    async/generator lifecycle decorator or a calibrated benchmark harness.
    """
    def decorate(function: Callable[P, R]) -> Callable[P, R]:
        @wraps(function)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            start = clock()
            try:
                return function(*args, **kwargs)
            finally:
                sink(function.__name__, clock() - start)
        return wrapped
    return decorate
