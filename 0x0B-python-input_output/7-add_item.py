#!/usr/bin/python3
"""define a script that adds all arguments to a Python list,
and then save them to a file"""


import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file = "add_item.json"
if os.path.exists(file):
    plist = load_from_json_file(file)
else:
    plist = []
with open(file, 'a') as f:
    for i in range(1, len(sys.argv)):
        plist.append(sys.argv[i])
save_to_json_file(plist, file)
