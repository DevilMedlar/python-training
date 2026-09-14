import asyncio
import unittest

from examples.pipeline import total_squares


class PipelineTests(unittest.IsolatedAsyncioTestCase):
    async def test_success_and_empty_work(self):
        for n, workers in [(0, 1), (1, 5), (10, 3), (1000, 7)]:
            with self.subTest(n=n, workers=workers):
                result = await asyncio.wait_for(total_squares(n, workers), timeout=3)
                self.assertEqual(result, n * (n - 1) * (2 * n - 1) // 6)

    async def test_invalid_workload_rejected_before_task_creation(self):
        before = asyncio.all_tasks()
        for n, workers, error in [(-1, 1, ValueError), (1, 0, ValueError),
                                  (True, 1, TypeError), (1, False, TypeError), (1.5, 1, TypeError)]:
            with self.subTest(n=n, workers=workers), self.assertRaises(error):
                await total_squares(n, workers)
        self.assertEqual(asyncio.all_tasks(), before)

    async def test_worker_failure_cancels_blocked_producer_and_peers(self):
        started = asyncio.Event()
        release_failure = asyncio.Event()
        active = set()
        seen = []

        async def transform(value):
            active.add(value)
            seen.append(value)
            started.set()
            try:
                await release_failure.wait()
                if value == 0:
                    raise RuntimeError("injected worker failure")
                await asyncio.Event().wait()
            finally:
                active.remove(value)

        before = asyncio.all_tasks()
        task = asyncio.create_task(total_squares(10000, workers=2, transform=transform))
        await asyncio.wait_for(started.wait(), 2)
        # Both workers stop inside transform; the large producer cannot complete.
        await asyncio.sleep(0)
        self.assertLessEqual(len(seen), 2)
        release_failure.set()
        with self.assertRaises(ExceptionGroup) as caught:
            await asyncio.wait_for(task, 2)
        self.assertTrue(any(isinstance(error, RuntimeError) for error in caught.exception.exceptions))
        self.assertEqual(active, set())
        self.assertEqual(asyncio.all_tasks(), before)

    async def test_external_cancellation_cleans_owned_work(self):
        started = asyncio.Event()
        active = set()

        async def transform(value):
            active.add(value)
            started.set()
            try:
                await asyncio.Event().wait()
            finally:
                active.remove(value)

        before = asyncio.all_tasks()
        task = asyncio.create_task(total_squares(10000, workers=2, transform=transform))
        await asyncio.wait_for(started.wait(), 2)
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await asyncio.wait_for(task, 2)
        self.assertEqual(active, set())
        self.assertEqual(asyncio.all_tasks(), before)

    async def test_transform_contract_failure_is_visible(self):
        async def wrong(value):
            return True

        with self.assertRaises(ExceptionGroup) as caught:
            await asyncio.wait_for(total_squares(3, transform=wrong), 2)
        self.assertTrue(any(isinstance(error, TypeError) for error in caught.exception.exceptions))
