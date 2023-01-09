#!/usr/bin/env python3
"""Async Basics"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the total runtime"""
    total_time = time.perf_counter()
    # temp = await wait_n(n, max_delay)
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - total_time
    return elapsed
