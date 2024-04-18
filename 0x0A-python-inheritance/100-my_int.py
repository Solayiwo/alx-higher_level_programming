#!/usr/bin/python3
"""Module for class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Invert == operator"""
        return not super().__eq__(value)

    def __ne__(self, value):
        """Invert != operator"""
        return not super().__ne__(value)
