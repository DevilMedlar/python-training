"""Bounded async teaching pipeline. Arithmetic here is not a speedup workload."""

import asyncio
from collections.abc import Awaitable, Callable


async def square(value: int) -> int:
    await asyncio.sleep(0)
    return value * value


async def total_squares(
    n: int,
    workers: int = 3,
    *,
    transform: Callable[[int], Awaitable[int]] = square,
) -> int:
    """Sum transformed range(n), owning a fixed worker set and bounded queue.

    n is an exact nonnegative int; workers is an exact positive int. A transform
    must cooperate with cancellation and return an int. The caller is responsible
    for its transform's external resources and side effects. Memory scales with
    workers (plus integer sizes), not with a list of all n results.
    """
    if type(n) is not int or type(workers) is not int:
        raise TypeError("n and workers must be integers, excluding booleans")
    if n < 0 or workers < 1:
        raise ValueError("n must be nonnegative and workers must be positive")
    queue: asyncio.Queue[int | None] = asyncio.Queue(maxsize=workers * 2)

    async def produce() -> None:
        for value in range(n):
            await queue.put(value)
        for _ in range(workers):
            await queue.put(None)

    async def consume() -> int:
        subtotal = 0
        while True:
            value = await queue.get()
            try:
                if value is None:
                    return subtotal
                result = await transform(value)
                if type(result) is not int:
                    raise TypeError("transform must return an integer")
                subtotal += result
            finally:
                queue.task_done()

    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(consume()) for _ in range(workers)]
        group.create_task(produce())
    return sum(task.result() for task in tasks)


if __name__ == "__main__":
    print(asyncio.run(total_squares(10)))
