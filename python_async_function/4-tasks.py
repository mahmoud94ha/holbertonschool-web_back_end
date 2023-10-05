#!/usr/bin/env python3
"""
task_wait_n function
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that calls n times a defined task.
    """
    corountine_list: List[asyncio.Task] = []
    response_list: List[float] = []
    for _ in range(0, n):
        corountine_list.append(task_wait_random(max_delay))

    for cr in asyncio.as_completed(corountine_list):
        response_list.append(await cr)

    return response_list