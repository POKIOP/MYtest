import csv
import pathlib

import requests

M_URL='https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5488/15/1/1/liczba_osob_ktore_przystapily_lub_zdaly_egzamin_maturalny.csv'

with requests.Session() as s:
    download=s.get(M_URL)
    decoded_content=download.content.decode('utf-8')

    cr=csv.reader(decoded_content.splitlines(), delimiter=';')
    my_list=list(cr)
    for row in my_list:
        print((row)[3])
        