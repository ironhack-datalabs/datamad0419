# pipeline steps: acquisition, wrangling, analysis, reporting

'''
comentarios e ideas:

idea principal: ver si en las zonas donde hay más terremotos hay más o menos densidad de población

el propio dataset nos da la información de la cantidad de terremotos

la densidad de población nos la dará una API

me gustaría llegar a representar el mapa de Turquía por colores según la cantidad de terremotos en las regiones

además, haré histogramas, el primero que se me ocurre es según la escala de richter, con bins

estaría bien poner un input de los años/ciudades/zonas que se quieran ver y que el resultado sea de esos años

usar filter, map, reduce

'''

import pandas as pd
import pandas_profiling
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import unicodedata


# acquisition

def acquisition():
    data = pd.read_csv('earthquake.csv')
    return data

# wrangling

def wrangling(df):
    # Primero veremos la cantidad de filas y columnas que tiene
    print(df.shape)
    # vemos número de nulls en las columnas
    null_cols = df.isnull().sum()
    print(null_cols)
    # vemos que hay muchos nulls en las ciudades
    # vamos a usar una api para obtener las ciudades a partir de las coordenadas

    # eliminar duplicados
    
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print('Number of duplicate records dropped: ', str(before - after))
    
    def get_year(date):
      return(int(date[:4]))

    df['year'] = df['date'].map(get_year)
    
    # eliminamos registros anteriores a 1964
    # eliminamos registros de terremotos con índice 0 en la Escala de Richter
    df = df.loc[data['year'] >= 1964]
    df = df.loc[data['richter'] != 0]
    # nos quedamos con las columnas que nos interesan
    df = df[['id', 'date', 'time', 'lat', 'long', 'city', 'area', 'richter', 'year']]
    
    # obtener ciudades según coordenadas
    def get_city(lat, lng):
      key = open(".env", "r").read()
      response = requests.get("https://geocodeapi.p.rapidapi.com/GetNearestCities?latitude={}&longitude={}&range=0".format(lat, lng),
        headers={
        "X-RapidAPI-Host": "geocodeapi.p.rapidapi.com",
        "X-RapidAPI-Key": key
        }
      )
      res = response.json()
      return unicodedata.normalize('NFKD',res[0]['City']).encode('ASCII', 'ignore').decode('utf-8').lower()
    
    
    
    
    filtered = df
    return filtered
    
    
if __name__ == '__main__':
    data = acquisition()
    filtered = wrangling(data)