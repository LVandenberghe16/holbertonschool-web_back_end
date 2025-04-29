#!/usr/bin/env python3
"""
comment
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    comment
    """

    for _ in range(10):
        i = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield i
