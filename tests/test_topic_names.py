import unittest

from examples.topic_names import normalize_topic


class TopicNameTests(unittest.TestCase):
    def test_lowercases_words(self):
        self.assertEqual(normalize_topic("Python Basics"), "python-basics")

    def test_collapses_spaces(self):
        self.assertEqual(normalize_topic("  for   loops  "), "for-loops")

    def test_handles_tabs_and_newlines(self):
        self.assertEqual(normalize_topic("list\tand\nset"), "list-and-set")

    def test_empty_and_whitespace_only(self):
        self.assertEqual(normalize_topic(""), "")
        self.assertEqual(normalize_topic(" \t\n"), "")

    def test_punctuation_and_unicode_are_not_sanitized(self):
        self.assertEqual(normalize_topic("Café / Python?"), "café-/-python?")

    def test_normalizing_an_already_normalized_result_is_stable(self):
        for text in (" A B ", "", "Café / Python?", "snake_case"):
            once = normalize_topic(text)
            self.assertEqual(normalize_topic(once), once)
