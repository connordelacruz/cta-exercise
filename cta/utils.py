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
    # TODO remove duplicates
    data = sorted(
        [row for row in reader],
        key = lambda i: i.get('RUN_NUMBER', '')
    )
    return fields, data

