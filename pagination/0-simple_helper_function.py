#!/usr/bin/env python3
"""This module defines a function"""
from typing import Tuple, Any


def index_range(page: int, page_size: int) -> Tuple[Any, Any]:
    """This function returns a tuple of size two containing
    a start index and an end index corresponding to the
    range of indexes to return in a list for those particular
    pagination parameters.

    Arguments:
    page(int): nth page
    page_size(int): size of each page
    """
    end_index: int = page * page_size
    start_index: int = end_index - page_size
    return (start_index, end_index)
