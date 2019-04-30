import pandas as pd
import numpy as np
import requests
import unicodedata
import matplotlib.pyplot as plt

# acquisition

def acquisition():
  data_original = pd.read_csv('earthquake.csv')
  data = pd.read_csv('data_cities.csv')
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
  data = data[['id', 'date', 'time', 'lat', 'long', 'city', 'city2', 'area', 'richter', 'year']]
  
  # añadimos la columna 'coords', como una tupla de 'lat' y 'long'
  data['coords'] = list(zip(data.lat, data.long))

  # obtener ciudades según coordenadas
  def get_city(location):
    key = open(".env", "r").read()
    response = requests.get("https://geocodeapi.p.rapidapi.com/GetNearestCities?latitude={}&longitude={}&range=0".format(location[0], location[1]),
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
  # hacemos bins según la Escala de Richter
  bins = [0, 4, 5, 7]
  data['richter_bins'] = pd.cut(data['richter'], bins)
  
  cleaned = data
  return cleaned

def analysis(df):
  # creamos pivot table para la cantidad de terremotos según año y potencia
  data = df
  date_richter = pd.pivot_table(
    data,
    values = 'date',
    index = 'year',
    columns = 'richter_bins',
    aggfunc = len,
    fill_value = 0
    )
  
  # creamos dataframe con el top 15 de ciudades según cantidad de terremotos
  top15cities = data['city2'].value_counts()[:15]
  dfs = (date_richter, top15cities)

  return dfs

def report(df1, df2):
    N = len(df1)
    x = list(df1.iloc[:, 2])
    y = list(df1.iloc[:, 1])
    z = list(df1.iloc[:, 0])
    ind = np.arange(N)

    p1 = plt.bar(ind, z, color = '#87cefa')
    p2 = plt.bar(ind, y, bottom = z, color = '#1e90ff')
    p3 = plt.bar(ind, x, bottom = ([sum(x) for x in zip(y, z)]), color = ('#0000cd'))

    plt.ylabel('Earthquakes')
    plt.xlabel('Years')
    plt.title('Earthquakes by year and Richter Scale')
    plt.xticks(ind, ['\'' + (str(x)[2:]) for x in list(df1.index)])
    plt.legend((p3[0], p2[0], p1[0]), ('(5, 7]', '(4, 5]', '(0, 4]'))
    
    plt.savefig('earthquake_year.png')
    plt.show()

    plt.figure
    height = list(df2)[::-1]
    bars = list(df2.index)[::-1]
    y_pos = np.arange(len(bars))
    
    # Create horizontal bars
    plt.barh(y_pos, height, color = '#87cefa')
    
    # Create names on the y-axis
    plt.yticks(y_pos, bars)

    plt.xlabel('Earthquakes')
    plt.title('Top 15 cities by number of earthquakes (2004-2017)')

    plt.savefig('top15.png')
    plt.show()