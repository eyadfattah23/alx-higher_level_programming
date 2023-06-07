#!/usr/bin/python3
for c in range(ord('z'), ord('a')-1, -1):
    if c % 2 == 0:
        print(chr(c).lower(), end='')
    else:
        print(chr(c).upper(), end='')
