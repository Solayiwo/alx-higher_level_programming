#!/usr/bin/python3
"""This module defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file"""

    with open(filename, "r") as file_object:
        json_data = json.load(file_object)
    return json_data
