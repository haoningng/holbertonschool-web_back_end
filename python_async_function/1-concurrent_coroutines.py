#!/usr/bin/env python3
"""This module defines an asynchronous coroutine"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This coroutine takes 2 int arguments n and max_delay
    and spawn wait_random n times with the specified
    max_delay, return the list of all the delays (float)

    Arguments:
    n(int): spawn wait_random n times
    max_delay(int): time delay for each wait_random
    """
    new_list: List[float] = []
    for _ in range(n):
        new_list.append(await wait_random(max_delay))
    return sorted(new_list)
