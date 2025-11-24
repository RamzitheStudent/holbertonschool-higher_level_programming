#!/usr/bin/python3
"""Module for class_to_json function."""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization."""
    result = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value

    return result

