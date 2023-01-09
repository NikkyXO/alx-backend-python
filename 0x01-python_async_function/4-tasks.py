#!/usr/bin/env python3
""" Async Basics """

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays (float values)"""
    values_list = []
    for i in range(n):
        temp = await task_wait_random(max_delay)
        values_list.append(temp)
    return values_list
