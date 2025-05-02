#!/usr/bin/env python3
"""
comment
"""


def schools_by_topic(mongo_collection, topic):
    """
    comment
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
