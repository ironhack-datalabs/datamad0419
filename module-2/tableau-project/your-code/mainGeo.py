import pandas as pd
from pymongo import MongoClient, GEOSPHERE
from pandas.io.json import json_normalize
import os
import webbrowser
import folium

puntuaciones= {
  'games_video' : 100,
  'software' : 50,
  'BigCompany' : 25,
  'Startup' : 40,
  'USA': -80
  }

client = MongoClient ('localhost', 27017)
db = client.companies
collection = db.companies

def query_to_db():
  cursor = collection.find({'$and': 
                      [ {'deadpooled_year':None}, 
                        {'founded_year': {'$gt':2003}},
                        {'offices': { '$ne': [] } },
                        {'$or': [{'category_code':'games_video'},
                                  {'category_code':'software'}] 
                      }]}
                      , {'name':1 , 'category_code':1, 'number_of_employees':1, 'founded_year':1, 
                          "offices.city":1, "offices.country_code":1, "offices.latitude":1, "offices.longitude":1}
                      ).sort('number_of_employees', -1)
  return cursor

def clean_nans(data):
  data= data.dropna(subset=['latitude', 'longitude', 'number_of_employees'])
  return data

def calculate_type(reg):
  if reg['founded_year'] > 2007 and reg['number_of_employees'] < 50:
      return 'Startup'
  else: return 'BigCompany'
    
def get_class(data):
  data['type']= data.apply(calculate_type, axis=1)
  return data


def order_data(data):
  data = data[['name', 'category_code', 'founded_year', 
                'country_code', 'city', 'latitude', 'longitude', 
                'number_of_employees']]
  data= data.reset_index(drop=True)
  return data

def get_2d_geo(data):
  data['2Dgeo']= data.apply(lambda reg: [reg['longitude'], reg['latitude']], axis=1)
  return data

def create_db_index(json_file):
  existe = os.path.isfile(json_file)
  if existe:
      os.system('mongoimport --db ofi_final --collection ofi_final --drop --file '+ json_file)
      db_ofi = client['ofi_final']
      db_ofi.ofi_final.create_index([('2dGeo', GEOSPHERE )])
      print('Base de datos y collección creadas')
  else:
      raise ValueError('Error archivo no encontrado')
    

# Obtener datos de mongo con el indice 2d geo.
def get_geo_data(datos):
  cursor_geo= datos.find()
  df = pd.DataFrame(cursor_geo)
  df = df.drop('_id', axis=1)
  return df

def sum_points(reg):
  points = 0
  points+= puntuaciones[reg.category_code]
  points+= puntuaciones[reg.type]
  if reg.country_code== 'USA': points+= puntuaciones['USA']
  return points

def get_offices_near(reg):
  points= list()
  lat = float(reg.latitude)
  long = float(reg.longitude)
  df_location = pd.DataFrame(datos_mongo.find({
                              "2Dgeo": {
                                "$near": {
                                  "$geometry": {
                                    "type": "Point" ,
                                    "coordinates": [ long, lat ]
                                  },
                                  "$maxDistance": 3000, # In meters
                                }
                              }
                          }))
  points.extend(df_location.apply(sum_points, axis=1))
  return sum(points)

def calculate_points(df):
  df['points'] = df.apply(get_offices_near, axis=1)
  return df  

def generate_map(row):
  latitud= float(row.latitude)
  longitud= float(row.longitude)
  nombre= str(row['name'])
  m = folium.Map(
  location=[latitud, longitud],
  tiles='Stamen Toner',
  zoom_start=16)

  tooltip = 'Este es tu sitio!'
  folium.Marker([latitud, longitud], 
                popup=nombre, 
                tooltip=tooltip, 
                icon=folium.Icon(color='green')
                ).add_to(m)
  m.save('main_map.html')
  return m

#Main
datos_crudo= query_to_db()
df = json_normalize(data= datos_crudo, record_path='offices', 
                    meta=['name', 'category_code', 'number_of_employees', 'founded_year'])
df_clean= clean_nans(df)
df_ordered= order_data(df_clean)
df_final= get_class(df_ordered)
df_geo = get_2d_geo(df_final)

df_geo.to_json('data_normalize_to_plot.json', orient='records', lines= True)

create_db_index('data_normalize_to_plot.json')

db = client.ofi_final
datos_mongo = db.ofi_final

df_geo_mongo = get_geo_data(datos_mongo)
df_points = calculate_points(df_geo_mongo)
df_points= df_points.sort_values('points', ascending=False)
mapa= generate_map(df_points[0:1])

webbrowser.open('file://' + os.path.realpath('main_map.html'))
