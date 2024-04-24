#!/usr/bin/env python3
"""This module defines an asynchronous coroutine"""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This coroutine will execute async_comprehension
    four times in parallel using asyncio.gather
    """
    total_time: float = 0
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(10)))
    end_time = time.time()
    total_time += (end_time - start_time)
    return total_time
