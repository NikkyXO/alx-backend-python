#!/usr/bin/env python3
"""Async Basics"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays (float values)"""
    values_list = []
    for i in range(n):
        temp = await wait_random(max_delay)
        values_list.append(temp)
    return values_list
