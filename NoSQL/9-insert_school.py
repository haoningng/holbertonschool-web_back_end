#!/usr/bin/env python3
"""This module defines a function"""
import pymongo
from bson.objectid import ObjectId
from typing import Dict, Any


def insert_school(
                  mongo_collection: pymongo.collection.Collection,
                  **kwargs: Dict[Any, Any]) -> ObjectId:
    """inserts a new document in a collection based on kwargs
    and return _id"""
    new_dict: Dict[Any, Any] = {}
    for key, value in kwargs.items():
        new_dict[key] = value
    return mongo_collection.insert_one(new_dict).inserted_id
