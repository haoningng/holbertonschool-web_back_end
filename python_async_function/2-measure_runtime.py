#!/usr/bin/env python3
"""This module defines an asynchronous coroutine"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    This coroutine measures the total execution time for
    wait_n(n, max_delay) and returns total_time/n

    Arguments:
    n(int): number of times wait_random is called
    max_delay(int): max delay time for wait_random
    """
    s: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.perf_counter() - s
    return total_time / n
