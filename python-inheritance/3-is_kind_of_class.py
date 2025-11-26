#!/usr/bin/python3
"""Defines a function that checks class inheritance."""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or if obj is an
    instance of a class that inherited from a_class; otherwise
    return False.
    """
    return isinstance(obj, a_class)
