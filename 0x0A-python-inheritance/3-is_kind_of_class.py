#!/usr/bin/python3
""" Checks if object is an instance of a class
    or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or any subclass of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
