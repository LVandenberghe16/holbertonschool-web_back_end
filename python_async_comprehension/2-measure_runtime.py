#!/usr/bin/env python3
"""
comment
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    comment
    """

    start = time.time()
    await asyncio.gather(async_comprehension())
    end = time.time()
    return end - start
