#!/usr/bin/python3
a = 89
b = 10


def switch_value(a, b):
    temp = b
    b = a
    a = temp
    print("a={:d} - b={:d}".format(a, b))


switch_value(a, b)
