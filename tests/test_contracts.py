import inspect
import unittest

from examples.contracts import timed


class DecoratorTests(unittest.TestCase):
    def test_signature_metadata_arguments_and_result(self):
        events = []
        ticks = iter([1.0, 1.25])

        @timed(lambda name, elapsed: events.append((name, elapsed)), clock=lambda: next(ticks))
        def total(values: list[int], *, offset: int = 0) -> int:
            """A documented calculation."""
            return sum(values) + offset

        self.assertEqual(total([2, 3], offset=4), 9)
        self.assertEqual(events, [("total", 0.25)])
        self.assertEqual(total.__name__, "total")
        self.assertEqual(total.__doc__, "A documented calculation.")
        self.assertEqual(inspect.signature(total), inspect.signature(total.__wrapped__))
        self.assertEqual(total.__wrapped__([2, 3]), 5)

    def test_target_exception_identity_is_preserved_and_recorded(self):
        events = []
        ticks = iter([2.0, 2.5])
        failure = ValueError("target failed")

        @timed(lambda name, elapsed: events.append((name, elapsed)), clock=lambda: next(ticks))
        def broken():
            raise failure

        with self.assertRaises(ValueError) as caught:
            broken()
        self.assertIs(caught.exception, failure)
        self.assertEqual(events, [("broken", 0.5)])
