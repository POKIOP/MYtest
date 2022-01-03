# import csv


# with open ('matura.csv') as file:
#     csv_file=csv.reader(file)
#     for row in csv_file:
#         if row[0]=='Lubuskie' and row[3]<='2011':
#             print(row)

import searching
import d_load_csv

# print(searching.find_numb_of_people(region="Lubuskie", passs="przystąpiło", sex="mężczyźni", year="2019" ))
matura=d_load_csv.load_csv('matura.csv')
print(searching.find_numb_of_people(matura,region="Lubuskie", passs="przystąpiło", sex="mężczyźni", year="2019" ))

