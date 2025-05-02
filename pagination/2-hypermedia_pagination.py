#!/usr/bin/env python3
"""
comment
"""


from typing import Tuple, List, Dict
import csv
import math


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, None]:
        """
        comment
        """
        page_data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_page = math.ceil(total_items / page_size) if page_size > 0 else 0
        next_page = page + 1 if page < total_page else None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_page
        }
