# pipeline steps: acquisition, wrangling, analysis, reporting

'''
comentarios e ideas:

idea principal: ver si en las zonas donde hay más terremotos hay más o menos densidad de población

el propio dataset nos da la información de la cantidad de terremotos

la densidad de población nos la dará una API

me gustaría llegar a representar el mapa de Turquía por colores según la cantidad de terremotos en las regiones

además, haré histogramas, el primero que se me ocurre es según la escala de richter, con bins

estaría bien poner un input de los años que se quieran ver y que el resultado sea de esos años

usar filter, map, reduce
'''

import pandas as pd
import pandas_profiling
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns

# acquisition

def acquisition():
    data = pd.read_csv('earthquake.csv')
    return data

# wrangling

def wrangling(df):
    print('Vamos a explorar el dataset')
    print('Primero veremos la cantidad de filas y columnas que tiene:')
    print(df.shape)
    filtered = df
    return filtered


if __name__ == '__main__':
    data = acquisition()
    filtered = wrangling(data)