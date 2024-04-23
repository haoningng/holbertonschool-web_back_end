#!/usr/bin/env python3
"""This module defines an regular function"""
import asyncio
import time
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[int]:
    """
    This function takes an integer max_delay and return a
    asyncio.Task

    Argument:
    max_delay(int): argument
    """
    return asyncio.Task(wait_random(max_delay))
