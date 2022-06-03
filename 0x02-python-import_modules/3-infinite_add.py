#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    for i in argv:
        mysum = int(0)
        arglen = len(argv) - 1
        
        if arglen == 0:
            mysum += 0
        else:
            for i in range(1,len(argv)):
                mysum += int(argv[i])
                        
    print("{}".format(mysum))
