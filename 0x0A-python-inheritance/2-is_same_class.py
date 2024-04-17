#!/usr/bin/python3
"""This module checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
