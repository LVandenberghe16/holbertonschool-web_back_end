#!/usr/bin/env python3
"""
comment
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    comment
    """
    for i in range(10):
        i = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield i
