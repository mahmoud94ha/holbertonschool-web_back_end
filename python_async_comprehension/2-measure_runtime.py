#!/usr/bin/env python3
"""
measure_runtime coroutine
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension
    four times in parallel using asyncio.gather.
    """
    before_time: float = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    after_time: float = time.time() - before_time
    return after_time
