#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="utf-8") as file_object:
        print(file_object.read(), end="")
