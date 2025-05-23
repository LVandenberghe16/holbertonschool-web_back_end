#!/usr/bin/env python3
"""
comment
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    comment
    """
    list = []
    coroutine = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(coroutine):
        resultat = await task
        list.append(resultat)
    return list
