#!/usr/bin/env python3
"""This module defines index_range function and Server class"""
import csv
import math
from typing import List, Tuple, Any, Dict


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
        """Find the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset
        (i.e. the correct list of rows)

        Arguments:
        page(int): page number
        page_size(int): number of row per page
        """
        assert (isinstance(page, int) and isinstance(page_size, int)
                and page > 0 and page_size > 0)
        if self.__dataset is None:
            self.dataset()
        pagination: Tuple[int, int] = index_range(page, page_size)
        return [each_page
                for each_page in self.__dataset[pagination[0]:pagination[1]]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[Any, Any]:
        """returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer

        Arguments:
        page(int): page number
        page_size(int): number of row per page
        """
        new_dict: Dict[Any, Any] = {}
        new_dict["page_size"] = page_size
        new_dict["page"] = page
        new_dict["data"] = self.get_page(page, page_size)
        total_rows: int = len(self.__dataset)
        total_pages: int = math.ceil(total_rows / page_size)
        if page >= total_pages:
            new_dict["next_page"] = None
        else:
            new_dict["next_page"] = page + 1
        if page = 1:
            new_dict["prev_page"] = None
        else:
            new_dict["prev_page"] = page - 1
        new_dict["total_pages"] = total_pages
        return new_dict
