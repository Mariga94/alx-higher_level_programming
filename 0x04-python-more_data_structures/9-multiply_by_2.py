#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    for key, value in dic.items():
        dic[key] = value * 2

    return dic
