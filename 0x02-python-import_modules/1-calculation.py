#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

a = int(sys.argv[1])
b = int(sys.argv[3])
op = sys.argv[2]

if op == '+':
    add = add(a, b)
    print(f"{a} + {b} = {add}")
elif op == '-':
    sub = sub(a, b)
    print(f"{a} - {b} = {sub}")
elif op == "*":
    mul = mul(a, b)
    print(f"{a} * {b} = {mul}")
elif op == '/':
    div = div(a, b)
    print(f"{a} / {b} = {div}")
