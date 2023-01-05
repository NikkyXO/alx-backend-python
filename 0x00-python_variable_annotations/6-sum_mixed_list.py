#!/usr/bin/env python3
"""
This module contains the "sum_mixed_list" function
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
	"""The sum_mixed_list function """
	sum = 0
	for i in mxd_lst:
		sum += i
	return sum
