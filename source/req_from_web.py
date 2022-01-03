import requests
from requests.api import request
import json

a=requests.get('https://api.dane.gov.pl/1.4/datasets/1946,liczba-osob-ktore-przystapilyzdaly-egzamin-matural?lang=pl')
response = requests.get('https://api.dane.gov.pl/1.4/datasets/1946,liczba-osob-ktore-przystapilyzdaly-egzamin-matural?lang=pl')

#print(a)
response.encoding = 'utf-8'

d=response.text
b=response.headers
c=json.loads(d)

print(c)

#if response.status_code == 200:
#    print('Success')
#elif response.status_code == 404:
#    print('Not found')

