import csv
import pathlib

# import requests

# M_URL='https://dane.gov.pl/pl/dataset/1946,liczba-osob-ktore-przystapilyzdaly-egzamin-matural/resource/35560?page=1&per_page=20&q=&sort='

# with requests.Session() as s:
#     download=s.get(M_URL)
#     decoded_content=download.content.decode('utf-8')

#     cr=csv.reader(decoded_content.splitlines(), delimiter=',')
#     my_list=list(cr)
#     for row in my_list:
#         print(row)

def load_csv(path_to_csv):
    # with open (path_to_csv) as file:
    file=pathlib.Path(path_to_csv).read_text()
    csv_file=csv.reader(file)
    return csv_file
