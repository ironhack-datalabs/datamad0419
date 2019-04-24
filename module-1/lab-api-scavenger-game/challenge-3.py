# enter your code below
import requests
import json
import base64

def base64ToString(c):
  print(c)
  c= base64.b64decode(c).decode('utf-8')
  print(c)
  return c

url = 'https://api.github.com/'
main = 'repos/ironhack-datalabs/scavenger/contents'
with open('api_key.env') as kf:
  key=kf.read()

def api_get(path=''):
  url_total= url+main+'/'+path
  print(url_total)
  response = requests.get(url_total, auth=('Mihlos', key))
  return response

def get_dirs(results):
  dirs_arr= []
  for i in range(len(results)):
    dirs_arr.append(results[i]['name'])
  return dirs_arr

def get_scavs(results):
  files_arr= []
  for i in range(len(results)):
    if len(results[i]['name'])>2: files_arr.append(results[i]['path'])
  return files_arr

def get_content(results):
  content = results['content']
  return content

response = api_get()
if response.status_code == 200:
  results = response.json()
  
  directories_arr= get_dirs(results)
  #borrar el gitignore
  del directories_arr[0]
  
  files_path = []
  
  for dir in directories_arr:
    response2 = api_get(path=dir)
    results2 = response2.json()
    scavs = get_scavs(results2)
    #añadir el path de los scavs en una lista, sin arrays.
    if len(scavs)> 0: 
      if len(scavs)==1: files_path.append(scavs[0])
      else:
        for s in scavs: files_path.append(s)
  #print(files_path)
  def sort_array(e):
    return e[7:]
  
  files_path_ordered= sorted(files_path,reverse=False, key=sort_array)
  
  joke=""
  for scav in files_path_ordered:
    response3= api_get(path=scav)
    results3= response3.json()
    joke_part = get_content(results3)
    joke+= joke_part

  joke= joke.replace("\n", "")
  joke= joke.replace("=", "")
  solucion= base64ToString(joke)

else: print('Error en datos')