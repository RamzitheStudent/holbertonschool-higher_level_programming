#!/usr/bin/python3
"""
Module that converts a JSON string to a Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): JSON formatted string.

    Returns:
        object: Python object represented by the JSON string.
    """
    return json.loads(my_str)
