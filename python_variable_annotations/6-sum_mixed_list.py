#!/usr/bin/env python3
"""This module defines the type-annotated sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function takes a list of int and floats
    and return the sum as float

    Argument:
    mxd_lst(list of int and floats): argument
    """
    sum: float = 0
    for each in mxd_lst:
        sum = sum + each
    return sum
