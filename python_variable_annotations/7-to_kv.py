#!/usr/bin/env python3
"""
comment
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    comment
    """
    return (k, v * v)
