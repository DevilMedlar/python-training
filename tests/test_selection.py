from collections import Counter
from random import Random
import unittest

from examples.benchmark_selection import run
from examples.selection import candidate, reference


class SelectionTests(unittest.TestCase):
    def test_hand_computable_contract(self):
        for function in (reference, candidate):
            self.assertEqual(function([3, -1, 3, 2], 3), [-1, 2, 3])
            self.assertEqual(function([], 2), [])
            self.assertEqual(function([3], 0), [])
            self.assertEqual(function((2, 1), 5), [1, 2])

    def test_differential_cases_and_nonmutation(self):
        rng = Random(42)
        cases = [[], [4], list(range(30)), list(range(30, 0, -1)), [7] * 40]
        cases += [[rng.randrange(-20, 21) for _ in range(size)] for size in range(40)]
        for values in cases:
            original = values.copy()
            for k in range(len(values) + 2):
                with self.subTest(size=len(values), k=k):
                    self.assertEqual(candidate(values, k), reference(values, k))
                    self.assertEqual(values, original)

    def test_properties_beyond_oracle(self):
        values = [5, -2, 5, 1, 9, -2]
        for function in (reference, candidate):
            selected = function(values, 4)
            self.assertEqual(len(selected), 4)
            self.assertEqual(selected, sorted(selected))
            self.assertFalse(Counter(selected) - Counter(values))
            self.assertEqual(function([value + 10 for value in values], 4),
                             [value + 10 for value in selected])
            self.assertEqual(function(list(reversed(values)), 4), selected)

    def test_invalid_contract(self):
        for function in (reference, candidate):
            for values, k, error in [([1], -1, ValueError), ([1], True, TypeError),
                                     ([1], 1.2, TypeError), ([True], 1, TypeError),
                                     ([1.0], 1, TypeError), (iter([1]), 1, TypeError),
                                     ("", 0, TypeError), (b"12", 1, TypeError)]:
                with self.subTest(function=function.__name__, values=values, k=k), self.assertRaises(error):
                    function(values, k)

    def test_benchmark_records_scope_and_all_raw_trials(self):
        result = run(size=50, k=5, repeats=4)
        self.assertEqual(len(result["trials"]), 8)
        self.assertIn("excludes input generation", result["scope"])
        for trial in range(4):
            rows = [row for row in result["trials"] if row["trial"] == trial]
            self.assertEqual([row["method"] for row in rows],
                             ["sort", "heap"] if trial % 2 == 0 else ["heap", "sort"])
            self.assertTrue(all(row["duration_ns"] >= 0 for row in rows))

    def test_benchmark_invalid_configuration(self):
        for config in [(-1, 1, 1), (1, -1, 1), (1, 1, 0)]:
            with self.subTest(config=config), self.assertRaises(ValueError):
                run(*config)
