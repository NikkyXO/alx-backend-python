#!/usr/bin/env python3
"""
This module contains the "Base" class
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
	"""The to_kv function"""
	return (k, v**2)
