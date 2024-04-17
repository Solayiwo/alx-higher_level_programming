#!/usr/bin/python3
"""This module adds all arguments to a Python list and save them to a file."""

import sys
import json
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args):
    """Adds all arguments to a Python list and saves them to a JSON file."""
    filename = 'add_item.json'

    """Check if the file exists, if not, create it"""
    if not path.exists(filename):
        save_to_json_file([], filename)

    """Load existing data from file"""
    data = load_from_json_file(filename)

    """Add arguments to the list"""
    data.extend(args)

    """Save the updated list to the file"""
    save_to_json_file(data, filename)


if __name__ == "__main__":
    add_item(sys.argv[1:])
