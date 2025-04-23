#!/usr/bin/env python3
"""
comment
"""


from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    comment
    """
    return [(i, len(i)) for i in lst]
