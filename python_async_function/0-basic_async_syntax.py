#!/usr/bin/env python3
"""
Asynchronous coroutine
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument (max_delay) and
    waits for a random delay between 0 and max_delay seconds and returns it.
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
