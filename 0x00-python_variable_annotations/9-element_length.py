#!/usr/bin/env python3
"""
This module contains the "element_length" class
"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    """The element_length function"""
    return [(i, len(i)) for i in lst]
