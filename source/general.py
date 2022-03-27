import csv
from typing import Optional


def load_csv(path_to_csv: str):
    with open(path_to_csv, encoding="utf-8") as file:
        csv_file = csv.reader(file)
        return list(csv_file)


def find_rows(
    csv_file: list,
    region: Optional[str] = None,
    pass_: Optional[str] = None,
    year: Optional[str] = None,
    sex: Optional[str] = None,
) -> list:
    found_rows: list[list[str]] = []
    for row in csv_file:
        if (
            region in (row[0], None)
            and pass_ in (row[1], None)
            and sex in (row[2], None)
            and year in (row[3], None)
        ):
            found_rows.append(row)
    return found_rows
