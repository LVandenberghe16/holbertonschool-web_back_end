#!/usr/bin/env python3
"""
comment
"""


from typing import Tuple


def index_range (page: int, page_size: int) -> Tuple[int, int]:
    """
    comment
    """

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
