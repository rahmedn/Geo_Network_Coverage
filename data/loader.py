import csv


def load_data(file_path):
    """
    Loads data from a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - list: A list of dictionaries representing the data.

    """
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        data = list(csv.DictReader(csvfile))
    return data
