#!/usr/bin/python3
"""
Adds all arguments to a Python list
and saves them to add_item.json
"""

import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# If file exists, load it. If not, use an empty list
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add all command-line arguments (except script name)
my_list.extend(sys.argv[1:])

# Save updated list
save_to_json_file(my_list, filename)
