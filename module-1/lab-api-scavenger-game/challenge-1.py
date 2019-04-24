# enter your code below
import requests
import json

url = 'https://api.github.com/'

with open('key.env') as kf:
  key=kf.read()

response = requests.get(url+'repos/ironhack-datalabs/datamad0419/forks', auth=('Mihlos', key))
results = response.json()

# with open('json.txt', 'w') as jf:
#   jf.write(response.text)
lang_array=[]

for i in range(len(results)):
  lang_array.append(results[i]['language'])

lang_set= set(lang_array)
#print(lang_array)
print(lang_set)