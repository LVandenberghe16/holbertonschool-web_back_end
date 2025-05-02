#!/usr/bin/env python3
"""
comment
"""

import csv
from typing import List, Dict


class Server:
    """
    comment
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        comment
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        comment
        """
        if index is None:
            index = 0
        indexed_data = self.indexed_dataset()
        assert index >= 0 and index < len(self.dataset()), "Index out of range"
        data = []
        current_index = index
        count = 0
        while count < page_size and current_index < len(self.dataset()):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                count += 1
            current_index += 1
        next_index = current_index
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
