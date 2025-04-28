#!/usr/bin/env python3
"""
comment
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    comment
    """

    result = [x async for x in async_generator() if x < 11]
    return result
