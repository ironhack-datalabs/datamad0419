# enter your code below
import requests
import json
import base64

# def base64ToString(c):
#     return base64.b64decode(c).decode('utf-8')

url = 'https://api.github.com/'
main = 'repos/ironhack-datalabs/scavenger/contents'
with open('api_key.env') as kf:
  key=kf.read()

def api_get(path=''):
  response = requests.get(url+main+path, auth=('Mihlos', key))
  return response

def get_dirs(results):
  dirs_arr= []
  for i in range(len(results)):
    dirs_arr.append(results[i]['name'])
  return dirs_arr

response = api_get()
if response.status_code == 200:
  results = response.json()
  d_arr= get_dirs(results)
  print(d_arr)
  #response = api_get(main)
else: print('Error en datos')