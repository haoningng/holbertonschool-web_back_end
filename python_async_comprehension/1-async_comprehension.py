#!/usr/bin/env python3
"""This module defines an asynchronous coroutine"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This coroutine collect 10 random numbers
    using an async comprehensing over async_generator
    then return the 10 random numbers
    """
    result: List[float] = []
    result = [i async for i in async_generator()]
    return result
