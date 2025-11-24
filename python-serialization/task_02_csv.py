#!/usr/bin/python3
"""Convert CSV data to JSON and save into data.json."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file into JSON format and save as data.json.
    Returns True if successful, otherwise False.
    """
    try:
        data_list = []

        # Read CSV file
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data_list.append(row)

        # Serialize and write to JSON file
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file)

        return True

    except Exception:
        return False
