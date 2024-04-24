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
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
