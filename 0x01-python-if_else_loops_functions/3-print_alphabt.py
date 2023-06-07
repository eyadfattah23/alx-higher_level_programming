#!/usr/bin/python3
for c in range(97, 97 + 26):
    if chr(c) == 'q' or chr(c) == 'e':
        continue
    print("{}".format(chr(c)), end='')
