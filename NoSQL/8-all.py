#!/usr/bin/env python3
"""
comment
"""


def list_all(mongo_collection):
    """
    comment
    """
    if mongo_collection is None:
        return []
    documents = list(mongo_collection.find())
    return documents
