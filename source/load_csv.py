import csv


def load_csv(path_to_csv):
    """Open csv file to list.

    Args:
        path_to_csv (str): file to load

    Returns:
        list: loaded file
    """
    with open(path_to_csv) as file:  # with - opening and closing file
        csv_file = csv.reader(file)
        return list(csv_file)
