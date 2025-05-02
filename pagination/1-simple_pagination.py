#!/usr/bin/env python3
"""
comment
"""


from typing import Tuple
import csv
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    comment
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """
    comment
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        comment
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        comment
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()

        if not dataset:
            return []

        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
