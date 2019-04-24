import json
import requests
import pandas as pd

with open (".env/configuration.lab", "r") as myfile:
    acceso = myfile.readlines()

key = acceso[0].rstrip('\n')
user = acceso[1]

repo = 'ironhack-datalabs/madrid-oct-2018'
get_forks = 'http://api.github.com/repos/'+ repo +'/forks'

res_fork = requests.get(get_forks, auth=(user, key))
results_fork = res_fork.json()

languages = set()

for i in range(len(results_fork)):
    languages.add(results_fork[i]['language'])

print(languages)


