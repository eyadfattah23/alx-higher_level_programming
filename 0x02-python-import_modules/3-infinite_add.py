#!/usr/bin/python3
import sys

sum = 0
if (len(sys.argv)) == 1:
    print("0")
else:
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
    print("{}".format(sum))
    
