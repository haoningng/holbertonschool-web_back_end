#!/usr/bin/env python3
"""This module defines a function"""
import pymongo
from typing import List, Any


def list_all(
             mongo_collection: pymongo.collection.Collection
            ) -> List[Any]:
    """This function lists all documents in a collection:"""
    doc_cursor: pymongo.cursor.Cursor[Any] = mongo_collection.find()
    doc_list: List[Any] = []
    for doc in doc_cursor:
        doc_list.append(doc)
    return doc_list
