"""Two established implementations under one explicitly validated contract.

Input is a finite sequence of exact integers (no booleans, text, or binary data). k is an exact
nonnegative integer. Return up to k values ascending, preserving duplicates and
leaving input unchanged. Validation cost is part of both public functions.
"""

from collections.abc import Sequence
from heapq import nsmallest


def _validate(values: Sequence[int], k: int) -> None:
    if type(k) is not int:
        raise TypeError("k must be an integer, excluding booleans")
    if k < 0:
        raise ValueError("k must be nonnegative")
    if not isinstance(values, Sequence) or isinstance(values, (str, bytes, bytearray)):
        raise TypeError("values must be a finite sequence of integers, not text or binary data")
    if any(type(value) is not int for value in values):
        raise TypeError("values must contain integers, excluding booleans")


def reference(values: Sequence[int], k: int) -> list[int]:
    _validate(values, k)
    return sorted(values)[:k]


def candidate(values: Sequence[int], k: int) -> list[int]:
    _validate(values, k)
    return nsmallest(k, values)
