#!/usr/bin/python3
"""
    This module returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        list: A list of strings representing attributes and methods
            of the object.
    """
    return dir(obj)
