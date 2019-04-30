import pandas as pd
import numpy as np
import requests
import unicodedata
import matplotlib.pyplot as plt

# acquisition

def acquisition():
  data_original = pd.read_csv('earthquake.csv')
  data = pd.read_csv('datacities.csv')
  return data

# wrangling

def wrangling(df):
  # eliminar duplicados    
  def del_duplicates(df):
    res = df.drop_duplicates()
    return res
  
  data = del_duplicates(df)      
  
  # vemos número de nulls en las columnas
  # null_cols = df.isnull().sum()
  # vemos que hay muchos nulls en las ciudades
  # vamos a usar una api para obtener las ciudades a partir de las coordenadas

  def get_year(date):
    return(int(date[:4]))

  data['year'] = data['date'].map(get_year)
  # eliminamos registros anteriores a 2014
  # eliminamos registros de terremotos con índice 0 en la Escala de Richter
  data = data.query('year >= 2004 & richter != 0')

  # nos quedamos con las columnas que nos interesan
  data = data[['id', 'date', 'time', 'lat', 'long', 'city', 'area', 'richter', 'year']]
  
  # añadimos la columna 'coords', como una tupla de 'lat' y 'long'
  data['coords'] = list(zip(data.lat, data.long))

  # obtener ciudades según coordenadas
  def get_city(location):
    key = open(".env", "r").read()
    response = requests.get("https://geocodeapi.p.rapidapi.com/GetNearestCities?latitude={}&longitude={}&range=0".format(lat, lng),
      headers={
      "X-RapidAPI-Host": "geocodeapi.p.rapidapi.com",
      "X-RapidAPI-Key": key
      }
    )
    res = response.json()
    return unicodedata.normalize('NFKD',res[0]['City']).encode('ASCII', 'ignore').decode('utf-8').lower()
    
  # creamos la columna con las ciudades creadas a partir de la api
  '''
  res = []
  for row in data.index: 
    res.append(get_city(data.loc[row, 'coords']))  
  data['city2'] = res
  '''
    
  filtered = data
  return filtered
  
    
if __name__ == '__main__':
    data = acquisition()
    filtered = wrangling(data)