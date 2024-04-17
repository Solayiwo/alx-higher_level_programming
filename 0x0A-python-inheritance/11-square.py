#!/usr/bin/python3
"""Module for rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Function that returns the square description
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
