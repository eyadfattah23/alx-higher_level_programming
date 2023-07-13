#!/usr/bin/python3
"""define a script that adds all arguments to a Python list,
and then save them to a file"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file = "add_item.json"
plist = load_from_json_file(file)
with open(file, 'w') as f:
    for i in range(1, len(sys.argv)):
        plist.append(sys.argv[i])
save_to_json_file(plist, file)
