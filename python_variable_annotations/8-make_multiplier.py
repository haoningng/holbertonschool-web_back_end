#!/usr/bin/env python3
"""This module defines the type-annotated make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float(i.e. multiplier) as argument
    and return a function that multiplies a float by multiplier

    Argument
    multipler(float): argument
    """
    def callback(arg: float) -> float:
        """This function takes a float as argument and multiply it
        with the multiplier

        Argument:
        arg(float): argument
        """
        return arg * multiplier
    return callback
