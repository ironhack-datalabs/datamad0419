import os
from config import URL_API
import time
import requests
import json

def devuelve_continente(area):
    #Devuelve el continente al que pertenece el area
    try: 
        url_iso = URL_API
        peticion = url_iso + area
        res_continente = requests.get(peticion)
        results = res_continente.json()
        return results['region']

    except Exception as e:
        return 'Error: ' + str(e)


def continentes(areas):
    area_continente = {}
    
    if os.path.exists('continentes.json'):
        with open('continentes.json') as json_file:  
            area_continente = json.load(json_file)
    else:
        print('Buscando Continentes, espere....')
        for area in areas:
            area_continente[area] = devuelve_continente(area)
            time.sleep(2 / 1000) 
        
        #guardamos el archivo json con los continentes
        archivo_json = json.dumps(area_continente)
        archivo = open('continentes.json','w')
        archivo.write(archivo_json)
        archivo.close()
        
    return area_continente  