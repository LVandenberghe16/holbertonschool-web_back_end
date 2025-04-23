#!/usr/bin/env python3
"""
comment
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    comment
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
