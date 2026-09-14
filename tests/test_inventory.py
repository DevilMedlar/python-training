from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sqlite3
import tempfile
import unittest

from examples.inventory import initialize, remaining, reserve


class InventoryTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.path = Path(temporary.name) / "inventory.sqlite"
        initialize(self.path, 5)

    def test_success_and_failure_leave_correct_stock(self):
        reserve(self.path, 3)
        self.assertEqual(remaining(self.path), 2)
        with self.assertRaises(ValueError):
            reserve(self.path, 3)
        self.assertEqual(remaining(self.path), 2)

    def test_invalid_types_and_values(self):
        for value, error in [(True, TypeError), (1.5, TypeError), (0, ValueError),
                             (-1, ValueError), (2**63, ValueError)]:
            with self.subTest(value=value), self.assertRaises(error):
                reserve(self.path, value)
        self.assertEqual(remaining(self.path), 5)

    def test_existing_database_is_not_reset(self):
        with self.assertRaises(sqlite3.OperationalError):
            initialize(self.path, 999)
        self.assertEqual(remaining(self.path), 5)

    def test_separate_connections_cannot_both_overspend(self):
        def attempt():
            try:
                reserve(self.path, 4)
                return "reserved"
            except ValueError:
                return "insufficient"

        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: attempt(), range(2)))
        self.assertCountEqual(results, ["reserved", "insufficient"])
        self.assertEqual(remaining(self.path), 1)

    def test_database_constraint_and_rollback(self):
        connection = sqlite3.connect(self.path, autocommit=False)
        try:
            with self.assertRaises(sqlite3.IntegrityError):
                with connection:
                    connection.execute("UPDATE stock SET quantity = 4")
                    connection.execute("UPDATE stock SET quantity = -1")
            self.assertEqual(remaining(self.path), 5)
        finally:
            connection.close()
