#!/usr/bin/env python3
"""
comment
"""


def insert_school(mongo_collection, **kwargs):
    """
    comment
    """
    resultat = mongo_collection.insert_one(kwargs)
    return resultat.inserted_id
