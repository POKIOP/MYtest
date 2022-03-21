import argparse
import csv


def find_row(csv_file, region, passs, year, sex="both"):
    found_rows = []
    for row in csv_file:
        if row[0] == region and row[1] == passs and row[2] == sex:
            found_rows.append(row)
        elif sex == "both":
            if row[0] == region and row[1] == passs and row[2] == "mężczyźni":
                found_rows.append(row)
            if row[0] == region and row[1] == passs and row[2] == "kobiety":
                found_rows.append(row)
            if row[1] == passs and row[2] == sex and row[0] == "lubuskie":
                found_rows.append(row)
    return found_rows  ### przerobic, np. podam region lubuskie i pokaze mi wszystkie linijki gdzie jest lubuskie


def proceed_in_year(csv_file, region, passs, year, sex="both"):
    """Returns number of people who proceeded to exam in particular region and year.

    Args:
        csv_file (list): csv file loaded as list
        region (str): region of Poland or whole Poland
        passs (str): pass or not
        year (int): year of exam
        sex (str, optional): sex. Defaults to 'both'.

    Returns:
        int: number of people
    """

    if sex == "both":
        number_of_women = int(proceed_in_year(csv_file, region, passs, year, "kobiety"))
        number_of_men = int(proceed_in_year(csv_file, region, passs, year, "mężczyźni"))
        return number_of_women + number_of_men

    else:
        for row in csv_file:
            if (
                row[0] == region
                and row[1] == passs
                and row[2] == sex
                and row[3] == year
            ):
                return row[4]


def proceed_all_years(csv_file, region, passs, sex, year="all"):
    """Returns number of people who proceeded to exam in all years.

    Args:
        csv_file (list): csv file loaded as list
        region (str): region of Poland or whole Poland
        passs (str): pass or not
        year (int): year of exam
        sex (str, optional): sex. Defaults to 'both'.

    Returns:
        int: number of people
    """

    if year == "all":
        found_rows = find_row(csv_file, region, passs, sex)
        return sum(int(row[4]) for row in found_rows)
    else:
        for row in csv_file:
            if (
                row[0] == region
                and row[1] == passs
                and row[2] == sex
                and row[3] == year
            ):
                return row[4]


def number_of_people_who_passed(csv_file, region, passs, sex, year="all"):
    """Returns number of people who passed exam.

    Args:
        csv_file (list): csv file loaded as list
        region (str): region of Poland or whole Poland
        passs (str): pass or not
        year (int): year of exam
        sex (str, optional): sex. Defaults to 'both'.

    Returns:
        int: number of people
    """
    found_rows = []
    if year == "all" and sex == "both":
        for row in csv_file:
            if row[0] == region and row[1] == passs:
                found_rows.append(row[4])
        return sum(int(x) for x in found_rows)


def percent_of_passed(csv_file, region, sex="both", year="all"):
    """Returns percent of people who passed exam.

    Args:
        csv_file (list): csv file loaded as list
        region (str): region of Poland or whole Poland
        passs (str): passed
        year (int): all years
        sex (str): both.

    Returns:
        float: number of people
    """
    zdalo = number_of_people_who_passed(
        csv_file, region, passs="zdało", sex=sex, year=year
    )
    przystapilo = number_of_people_who_passed(
        csv_file, region, passs="przystąpiło", sex="both", year="all"
    )
    percentage = round(zdalo / przystapilo * 100, 2)
    return f"{percentage}%"


# if __name__ == '__main__':
#     import d_load_csv

#     matura=d_load_csv.load_csv('matura.csv')

#     parser=argparse.ArgumentParser(description='Show number of persons')
#     parser.add_argument('--region', type=str)
#     parser.add_argument('--passs', type=str)
#     parser.add_argument('--sex', type=str)
#     parser.add_argument('--year', type=int)

#     args=parser.parse_args()
#     print(proceed_in_year(matura, args.region, args.passs, args.sex, args.year))
