#!/usr/bin/python3
import sys
from add_0 import add

a = int(sys.argv[1])
b = int(sys.argv[3])
add = add(a,b)
print(f"{a} + {b} = {add}")

