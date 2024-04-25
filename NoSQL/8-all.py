#!/usr/bin/env python3
"""This module defines a function"""
import pymongo
from typing import Any


def list_all(
             mongo_collection: pymongo.collection.Collection
            ) -> pymongo.cursor.Cursor[Any]:
    """This function lists all documents in a collection:"""
    return mongo_collection.find()
