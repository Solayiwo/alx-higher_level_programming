#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return self.__size ** 2
