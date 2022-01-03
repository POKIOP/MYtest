import argparse
import csv



def find_numb_of_people(csv_file, region, passs, sex, year):
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

