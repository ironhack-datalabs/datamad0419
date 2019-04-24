# enter your code below
import requests
import json

url = 'https://api.github.com/'

with open('api_key.env') as kf:
  key=kf.read()

response = requests.get(url+'repos/ironhack-datalabs/datamad0419/commits?since=2019-01-15T00:00:00Z&until=2019-01-22T00:00:00Z', auth=('Mihlos', key))
# Para abril no me da resultados, lista vacía. En enero si da resultados.
if response.status_code == 200:
  results = response.json()
  print(len(results))
else: print('Error en datos')