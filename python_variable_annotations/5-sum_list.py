#!/usr/bin/env python3
"""This module defines the type-annotated sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function takes a list of floats as arguments
    and return their sum as a float

    Argument:
    input_list(list of floats): argument
    """
    sum: float = 0
    for each in input_list:
        sum = sum + each
    return sum
