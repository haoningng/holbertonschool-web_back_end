#!/usr/bin/env python3
"""This module defines an asynchronous coroutine"""
import asyncio
import random
from typing import List, Generator


async def async_generator() -> Generator[float, None, None]:
    """This coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        i += 1
