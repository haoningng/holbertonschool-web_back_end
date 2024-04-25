#!/usr/bin/env python3
"""This module defines a function"""
import pymongo
from typing import List, Any


def schools_by_topic(
                  mongo_collection: pymongo.collection.Collection,
                  topic: str) -> List[Any]:
    """
    This function returns the list of school having a specific topic
    """
    return list(mongo_collection.find({"topics": {"$in": [topic]}}))
