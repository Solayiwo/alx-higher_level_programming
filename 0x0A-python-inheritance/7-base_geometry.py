#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """
    BaseGeometry class represents methods for geometry calculations.
    """

    def area(self):
        """
        method not implemented yet

        Raises:
            Exception: When the method is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
