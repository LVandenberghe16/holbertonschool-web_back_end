#!/usr/bin/env python3
"""
comment
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    comment
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    sum = end - start
    return sum / n
