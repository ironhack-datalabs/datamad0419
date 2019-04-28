import pandas as pd
import numpy as np
import re
import requests
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns
import time
from raven import Client

#Estos datos iran en el archivo de configuración
DATOS_PATH = 'data/FAO.csv'
SALIDA_PATH = 'reports/'
URL_API = 'https://restcountries.eu/rest/v2/alpha/'

def acquire():
    df = pd.read_csv(DATOS_PATH, encoding='latin1')
    return df

def wrangle(data):
    pass

def analyze():
    pass

def report():
    pass

def save_viz(chart, title):
    fig = chart.get_figure()
    fig.savefig(title + '.png')

def main():
    df = acquire()
    df.head()

if __name__ == "__main__":
    main()