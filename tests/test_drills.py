import unittest

from examples import drills


class BeginnerDrillTests(unittest.TestCase):
    def test_minutes_boundaries_and_invalid_domain(self):
        for value, expected in [(0, (0, 0)), (59, (0, 59)), (60, (1, 0)), (135, (2, 15))]:
            self.assertEqual(drills.split_minutes(value), expected)
        with self.assertRaises(ValueError):
            drills.split_minutes(-1)
        with self.assertRaises(TypeError):
            drills.split_minutes(True)

    def test_initials_empty_whitespace_and_multiple_parts(self):
        self.assertEqual(drills.initials("  ada   lovelace "), "AL")
        self.assertEqual(drills.initials("   "), "")
        self.assertEqual(drills.initials("mary ann evans"), "MAE")

    def test_score_boundaries(self):
        for value, expected in [(-1, False), (0, True), (100, True), (101, False)]:
            self.assertIs(drills.valid_score(value), expected)

    def test_accumulation_has_closed_form_agreement(self):
        for n in [0, 1, 5, 20]:
            self.assertEqual(drills.total_through(n), n * (n + 1) // 2)
        with self.assertRaises(ValueError):
            drills.total_through(-1)

    def test_collection_operations_preserve_order_and_input(self):
        values = [-2, 0, 3, 5]
        self.assertEqual(drills.positive_values(values), [3, 5])
        self.assertEqual(values, [-2, 0, 3, 5])
        self.assertEqual(drills.positive_values([]), [])
        self.assertEqual(drills.unique_in_order(["b", "a", "b", "c"]), ["b", "a", "c"])
        self.assertEqual(drills.unique_in_order([]), [])

    def test_word_count_contract_is_case_sensitive_whitespace_tokens(self):
        self.assertEqual(drills.word_counts("red\nblue red"), {"red": 2, "blue": 1})
        self.assertEqual(drills.word_counts("Red red."), {"Red": 1, "red.": 1})
        self.assertEqual(drills.word_counts(""), {})

    def test_average_empty_singleton_and_normal(self):
        self.assertIsNone(drills.average([]))
        self.assertEqual(drills.average([5]), 5)
        self.assertEqual(drills.average([2, 4]), 3)

    def test_count_threshold_and_search(self):
        self.assertEqual(drills.count_at_least([4, 5, 6], 5), 2)
        self.assertEqual(drills.count_at_least([], 5), 0)
        self.assertTrue(drills.contains_value([0, 2, 2], 0))
        self.assertFalse(drills.contains_value([0, 2], 1))
        self.assertFalse(drills.contains_value([], 1))
