#!/usr/bin/env python3
"""This module defines index_range function and Server class"""
import csv
import math
from typing import List, Tuple, Any


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert (isinstance(page, int) and isinstance(page_size, int)
                and page > 0 and page_size > 0)
        if self.__dataset is None:
            self.dataset()
        pagination: Tuple[int, int] = index_range(page, page_size)
        return [each_page
                for each_page in self.__dataset[pagination[0]:pagination[1]]]
