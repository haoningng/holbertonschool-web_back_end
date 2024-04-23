#!/usr/bin/env python3
"""This module defines the element_length function"""
from typing import Iterable, List, Any, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function return a list

    Argument
    lst(list): list argument"""
    return [(i, len(i)) for i in lst]
