#!/usr/bin/env python3
"""This module defines a function"""
import asyncio
import random
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This coroutine takes 2 int arguments n and max_delay
    and spawn wait_random n times with the specified
    max_delay, return the list of all the delays (float)

    Arguments:
    n(int): spawn wait_random n times
    max_delay(int): time delay for each wait_random
    """
    new_list: List[float] = []
    new_list = await wait_n(n, max_delay)
    return new_list
