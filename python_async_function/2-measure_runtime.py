#!/usr/bin/env python3
"""Create a function with integers as
arguments that measures the total execution time"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Function that measures the total execution """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return (elapsed / n)
