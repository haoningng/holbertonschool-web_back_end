#!/usr/bin/env python3
"""This module defines the type-annotated to_kv function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function takes a string and int/float and return a tuple.
    First element of tuple being string k
    Second element of tuple being square of the int/float v

    Arguments:
    k(str): first argument
    v(int or float): second argument
    """
    return (k, float(v * v))
