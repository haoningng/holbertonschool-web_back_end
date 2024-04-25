#!/usr/bin/env python3
"""This module defines a function"""
import pymongo
from typing import List, Any


def update_topics(
                  mongo_collection: pymongo.collection.Collection,
                  name: str,
                  topics: List[str]) -> None:
    """
    This function changes all topics of a
    school document based on the name
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
