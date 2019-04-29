import pandas as pd
import numpy as np
import json
import requests

def acquire():
    cars = pd.read_csv('./data.csv', sep=';')
    return cars.head()

def wrangle(df):
    before = len(cars)
    cars1 = cars.drop_duplicates()
    after = len(cars1)
    return('Number of duplicate records dropped: ', str(before - after))

def wrangle1(df):
    cars1 = cars[['make', 'model', 'months_old', 'power','gear_type','fuel_type','kms','price']]
    return cars1.head()

def wrangle2(df):
    cars1['old_years'] = cars1['months_old'].divide(12).round()
    return cars1.head()

def wrangle3(df):
    cars1 = cars1[['make', 'model', 'power','gear_type','fuel_type','kms','old_years','price']]
    return cars1.head()

def wrangle4(df):
    cars1['model'] = cars1['model'].str.replace('C-Elys�e', 'C-Elys')
    return (set(cars1['model']))

def acquire2():
    response = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas')
    results = response.json()
    return results

def wrangle5(df):
    datacars = pd.DataFrame(results)
    return datacars.head()

 def wrangle6(df):
     datacars.rename(columns={'nome': 'make'}, inplace=True)
     datacars['make'] = datacars['make'].str.replace('Alfa Romeo', 'Alfa')
     return datacars.head()
 
def analyze(df):
    s1 = pd.merge(cars1,datacars,how='left', on=['make'])
    return s1.head()

def analyze1(df):
    table = pd.pivot_table(s1, index=['make','codigo','model'], aggfunc={'model':[len],'power': np.mean, 'kms':np.mean, 'old_years':np.mean, 'price':np.mean}).round()
    return table.head()

def report(df):
    table1 = table[['model','kms','power','old_years','price']]
    return table1.head()

if __name__ == '__main__':
    
    