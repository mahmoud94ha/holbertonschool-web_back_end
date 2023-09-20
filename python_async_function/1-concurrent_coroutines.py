#!/usr/bin/env python3
"""
Asynchronous routine
"""
import asyncio
from types import coroutine
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that takes in n and max_delay.
    The function spawn wait_random n times with the specified max_delay.
    Returns the list of all the sorted delays.
    """
    corountine_list: List[coroutine] = []
    response_list: List[float] = []
    for _ in range(0, n):
        corountine_list.append(wait_random(max_delay))

    for cr in asyncio.as_completed(corountine_list):
        response_list.append(await cr)

    return response_list
