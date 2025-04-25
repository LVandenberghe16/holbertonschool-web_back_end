#!/usr/bin/env python3
"""
comment
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    comment
    """
    list = []
    coroutine = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(coroutine):
        result = await task
        list.append(result)
    return list
