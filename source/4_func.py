import argparse
import d_load_csv

def find_numb_of_people(csv_file, region, year):
    for row in csv_file:
        if row[0]==region and row[3]==year:
            return row[4]

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Show number of persons')
    parser.add_argument('--region', type=str)
    parser.add_argument('--year', type=int)

    args=parser.parse_args()
    #print(find_numb_of_people(args.region, args.year))            
    matura=d_load_csv.load_csv('matura.csv')
    print(find_numb_of_people(matura,region="Lubuskie", year="2010"))
    
