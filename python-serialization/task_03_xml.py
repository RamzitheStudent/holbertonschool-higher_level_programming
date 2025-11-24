#!/usr/bin/python3
"""XML Serialization and Deserialization using ElementTree."""

import xml.etree.ElementTree as ET


def _convert_value(value):
    """
    Convert string value back to Python type:
    int, float, bool, or leave as string.
    """
    # Boolean check
    if value == "True":
        return True
    if value == "False":
        return False

    # Integer check
    if value.isdigit():
        return int(value)

    # Float check
    try:
        return float(value)
    except ValueError:
        pass

    # Default: string
    return value


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.
    Return True if successful, otherwise False.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True

    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Read XML file and return a Python dictionary.
    Handles basic type conversion.
    Return None on failure.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for child in root:
            result[child.tag] = _convert_value(child.text)

        return result

    except Exception:
        return None
