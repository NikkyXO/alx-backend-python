#!/usr/bin/env python3
from typing import List
"""
This module contains the "sum_list" function
"""

def sum_list(input_list: List[float]) -> float:
	"""The sum_list function"""
	sum = 0
	for i in input_list:
		sum += i
	return sum
