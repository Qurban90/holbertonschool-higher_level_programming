#!/usr/bin/env python3
"""
Module that converts CSV data to JSON format
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV file to JSON file (data.json)
    Returns True if successful, otherwise False
    """
    try:
        data = []

        with open(filename, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
