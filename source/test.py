#url='https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5488/15/1/1/liczba_osob_ktore_przystapily_lub_zdaly_egzamin_maturalny.csv'

import searching
import d_load_csv

# print(searching.find_numb_of_people(region="Lubuskie", passs="przystąpiło", sex="mężczyźni", year="2019" ))
matura=d_load_csv.load_csv('matura.csv')
res1=int(searching.find_numb_of_people(matura,"Lubuskie", "przystąpiło","kobiety", "2010"))
res2=int(searching.find_numb_of_people(matura,"Lubuskie", "przystąpiło","mężczyźni", "2010"))
print(res1+res2)
