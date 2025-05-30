#!/usr/bin/env python3
"""
comment
"""
from pymongo import MongoClient


def print_nginx_stats(nginx_collection):
    """
    comment
    """

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_stats(client.logs.nginx)
