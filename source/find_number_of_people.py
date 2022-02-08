import argparse


def proceed_in_year(csv_file, region, passs, year, sex='both'):
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
        number_of_women = int(proceed_in_year(csv_file, region, passs, year, "kobiety"))
        number_of_men = int(proceed_in_year(csv_file, region, passs, year, "mężczyźni"))
        return number_of_women + number_of_men

  

def proceed_all_years(csv_file, region, passs, sex, year ='all'):
    
    found_rows = []
    if year == 'all':
        for row in csv_file:
            if row[0]==region and row[1]==passs and row[2]==sex:
                found_rows.append(row[4])
                a=list(map(int, found_rows))  # zmienic na list comprehension, zrobic w return
        return sum(a)    

        
    else:
        for row in csv_file:
            if row[0]==region and row[1]==passs and row[2]==sex and row[3]==year:
                return row[4]


def pass_all_years(csv_file, region, passs, sex, year ='all'):
    found_rows = []
    if year == 'all' and sex == 'both':
        for row in csv_file:
            if row[0]==region and row[1]==passs:
                found_rows.append(row[4])
                a=list(map(int, found_rows)) # zmienic na list comprehension, zrobic w return
        return sum(a)

def proceed_vs_pass(csv_file, region, sex='both', year ='all'):
    zdalo = pass_all_years(csv_file, region, passs='zdało', sex='both', year ='all')
    przystapilo = pass_all_years(csv_file, region, passs='przystąpiło', sex='both', year ='all')
    return zdalo / przystapilo * 100 # 2 liczby po przecinku, znak % lub docs.
    




# if __name__ == '__main__':
#     import d_load_csv

#     matura=d_load_csv.load_csv('matura.csv')

#     parser=argparse.ArgumentParser(description='Show number of persons')
#     parser.add_argument('--region', type=str)
#     parser.add_argument('--passs', type=str)
#     parser.add_argument('--sex', type=str)
#     parser.add_argument('--year', type=int)

#     args=parser.parse_args()
#     print(find_numb_of_people_0(matura, args.region, args.passs, args.sex, args.year))