#!/usr/bin/python3
"""This module defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object to its JSON representation.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: The JSON representation of a string object"""

    return json.dumps(my_obj)
