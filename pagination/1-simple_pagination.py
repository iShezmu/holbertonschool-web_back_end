#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Returns a tuple of size two containing a start index and
        an end index corresponding to the range of indexes to return
        in a list for those particular pagination parameters.
        """
        start = (page - 1) * page_size
        end = page * page_size
        return start, end

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Finds the correct indexes to paginate dataset correctly
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = self.index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
