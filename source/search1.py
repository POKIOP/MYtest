import argparse
import searching


def find_numb_of_people_0(csv_file, region, passs, year, sex='both'):
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
        number_of_women = int(find_numb_of_people_0(csv_file, region, passs, year, "kobiety"))
        number_of_men = int(find_numb_of_people_0(csv_file, region, passs, year, "mężczyźni"))
        return number_of_women + number_of_men


def find_numb_of_people(csv_file, region, passs, sex, year ='all'):
    
    if year == 'all':
        number_year0 = int(find_numb_of_people(csv_file, region, passs, sex, "2010"))
        number_year1 = int(find_numb_of_people(csv_file, region, passs, sex, "2011"))
        number_year2 = int(find_numb_of_people(csv_file, region, passs, sex, "2012"))
        number_year3 = int(find_numb_of_people(csv_file, region, passs, sex, "2013"))
        number_year4 = int(find_numb_of_people(csv_file, region, passs, sex, "2014"))
        number_year5 = int(find_numb_of_people(csv_file, region, passs, sex, "2015"))
        number_year6 = int(find_numb_of_people(csv_file, region, passs, sex, "2016"))
        number_year7 = int(find_numb_of_people(csv_file, region, passs, sex, "2017"))
        number_year8 = int(find_numb_of_people(csv_file, region, passs, sex, "2018"))
        number_year9 = int(find_numb_of_people(csv_file, region, passs, sex, "2019"))

        return number_year0 + number_year1 + number_year2 + number_year3 + number_year4 + number_year5 + number_year6 + number_year7 + number_year8 + number_year9
    else:
        for row in csv_file:
            if row[0]==region and row[1]==passs and row[2]==sex and row[3]==year:
                return row[4]
    

def find_numb_of_people2(csv_file, region, passs, sex, year ='all'):
    
    found_rows = []
    if year == 'all':
        for row in csv_file:
            if row[0]==region and row[1]==passs and row[2]==sex:
                found_rows.append(row[4])
                a=list(map(int, found_rows)) 
        return sum(a)    

        
    else:
        for row in csv_file:
            if row[0]==region and row[1]==passs and row[2]==sex and row[3]==year:
                return row[4]

# results for task 2 i 3
def find_numb_of_people_3(csv_file, region, passs, sex, year ='all'):
    found_rows = []
    if year == 'all' and sex == 'both':
        for row in csv_file:
            if row[0]==region and row[1]==passs:
                found_rows.append(row[4])
                a=list(map(int, found_rows)) 
        return sum(a)   

# pass='both'

def pass_or_not(csv_file, region, passs, sex, year ='all'):
    if passs == 'both':
        number_of_przystapilo = int(pass_or_not(csv_file, region, sex, year, "przystąpiło"))
        number_of_zdalo = int(pass_or_not(csv_file, region, passs, year, "zdało"))
        return number_of_zdalo/number_of_przystapilo*100




if __name__ == '__main__':
    import d_load_csv

    matura=d_load_csv.load_csv('matura.csv')

    parser=argparse.ArgumentParser(description='Show number of persons')
    parser.add_argument('--region', type=str)
    parser.add_argument('--passs', type=str)
    #parser.add_argument('--sex', type=str)
    # parser.add_argument('--year', type=int)

    args=parser.parse_args()
    print(find_numb_of_people_3(matura, args.region, args.passs))