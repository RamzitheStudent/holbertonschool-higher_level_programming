#!/usr/bin/python3
"""Defines a lookup function."""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: List of attribute and method names.
    """
    return dir(obj)
