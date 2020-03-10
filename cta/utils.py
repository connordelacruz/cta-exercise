import csv

def parse_csv(file_string):
    """Parse a CSV file and return python representations of the data.

    This will remove duplicate values and sort the results by their run number.

    :param file_string: Decoded string representation of the CSV file

    :return: (fields, data), where fields is a list of field names and data is
        a list of OrderedDict objects representing each row
    """
    reader = csv.DictReader(file_string.splitlines(), skipinitialspace=True)
    fields = reader.fieldnames
    # Sort items by run number
    data = sorted(
        [row for row in reader],
        key = lambda i: i.get('RUN_NUMBER', '')
    )
    # Remove duplicates
    unique_data = []
    for d in data:
        if d not in unique_data:
            unique_data.append(d)
    return fields, unique_data

