#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multiplied_dic = {}
    for key, value in a_dictionary.items():
        multiplied_dic[key] = value * 2
    return multiplied_dic
