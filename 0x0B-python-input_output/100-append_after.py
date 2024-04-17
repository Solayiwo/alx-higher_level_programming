#!/usr/bin/python3
"""This module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file"""

    if not all((filename, search_string, new_string)):
        return None

    with open(filename, 'r') as file_object:
        lines = file_object.readlines()

    with open(filename, 'w') as file_object:
        for line in lines:
            file_object.write(line)
            if search_string in line:
                file_object.write(new_string)
