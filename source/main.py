# import csv


# with open ('matura.csv') as file:
#     csv_file=csv.reader(file)
#     for row in csv_file:
#         if row[0]=='Lubuskie' and row[3]<='2011':
#             print(row)
# https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5488/15/1/1/liczba_osob_ktore_przystapily_lub_zdaly_egzamin_maturalny.csv



# print(searching.find_numb_of_people(region="Lubuskie", passs="przystąpiło", sex="mężczyźni", year="2019" ))


# years - 4 defined




#task 1 , result: 15750
# import searching
# import d_load_csv

# matura=d_load_csv.load_csv('matura.csv')
# print(searching.find_numb_of_people_0(matura,region="Lubuskie",passs="przystąpiło", year="2018" ))


#task 2, result: 77879
# import search1
# import d_load_csv

# matura=d_load_csv.load_csv('matura.csv')
# print(search1.find_numb_of_people_3(matura,region="Lubuskie", passs="przystąpiło", sex="both"))


#task 3, result: 61883
import search1
import d_load_csv

matura=d_load_csv.load_csv('matura.csv')
print(search1.find_numb_of_people_3(matura,region="Lubuskie", passs="zdało", sex="both"))


#task 4, result: 79.46%
import search1
import d_load_csv

matura=d_load_csv.load_csv('matura.csv')
print(search1.find_numb_of_people_3(matura,region="Lubuskie", passs="zdało", sex="both"))