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

    """Get the classes that obj is an instance of"""
    object_classes = type(obj).__mro__

    """Check if any of these classes are equal to or derived from a_class"""
    for cls in object_classes:
        if cls is a_class or issubclass(cls, a_class):
            return True
    return False
