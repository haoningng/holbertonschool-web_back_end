#!/usr/bin/env python3
"""This module defines an asynchronous coroutine"""
import asyncio
import random
from typing import Awaitable, Any


async def wait_random(max_delay: int = 10) -> float:
    """This coroutine takes in an int argument (i.e. max_delay)
    and waits for a random delay between 0 and max_delay
    seconds and eventually returns it

    Argument:
    max_delay(int): argument
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
