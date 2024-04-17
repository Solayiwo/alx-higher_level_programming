#!/usr/bin/python3
""" Checks if object is an instance of a class that
    inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited (directly
    or indirectly) from the specified class a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
