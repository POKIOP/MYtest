import argparse
import csv


def find_numb_of_people(csv_file, region, passs, year, sex='both'):
    """Returns number of people.

    Args:
        csv_file (list): csv file loaded as list
        region (str): region of Poland or whole Poland
        passs (str): pass or not
        year (int): year of exam
        sex (str, optional): sex. Defaults to 'both'.

    Returns:
        int: number of people
    """
    if sex == 'both':
        number_of_women = int(find_numb_of_people(csv_file, region, passs, year, "kobiety"))
        number_of_men = int(find_numb_of_people(csv_file, region, passs, year, "mężczyźni"))
        return number_of_women + number_of_men
        
    else:
        for row in csv_file:
            if row[0]==region and row[1]==passs and row[2]==sex and row[3]==year:
                return row[4]
    

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Show number of persons')
    parser.add_argument('--region', type=str)
    parser.add_argument('--passs', type=str)
    parser.add_argument('--sex', type=str)
    parser.add_argument('--year', type=int)

    args=parser.parse_args()
    print(find_numb_of_people(args.region, args.passs, args.sex, args.year))

