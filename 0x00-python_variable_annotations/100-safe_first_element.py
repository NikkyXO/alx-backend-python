#!/usr/bin/env python3
"""
This module contains the "safe_first_element" function
"""


from typing import List, Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:

    """A safe_first_elemen function """
    if lst:
        return lst[0]
    else:
        return None
