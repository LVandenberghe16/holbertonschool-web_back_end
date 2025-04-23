#!/usr/bin/env python3

from typing import Tuple, Iterable, Sequence, List

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
