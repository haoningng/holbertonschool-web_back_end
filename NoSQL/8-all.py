#!/usr/bin/env python3
"""This module defines a function"""


def list_all(mongo_collection):
    return list(mongo_collection.find())
