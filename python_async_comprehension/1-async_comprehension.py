#!/usr/bin/env python3
"""
comment
"""


import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    comment
    """
    result = [x async for x in async_generator()]
    return result
