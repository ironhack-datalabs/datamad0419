import pandas as pd
import numpy as np
from raven import Client

from config import DATOS_PATH, URL_API, SALIDA_PATH
import limpia ,analisis, guardar, reports 

def acquire():
    df = pd.read_csv(DATOS_PATH, encoding='latin1')
    return df

def wrangle(data):
    nueva_data = limpia.renombra_columnas(data)
    nueva_data = limpia.eliminar_columnas(nueva_data)
    return nueva_data

def analyze(data):
    datos = analisis.datos_analisis(data)
    areas = set(datos['Area_ISO'])
    datos = analisis.columna_continente(datos, areas)
    datos = analisis.columna_total_alimento(datos)
    datos = analisis.produccion_bin(datos)
    total_pais = analisis.total_produccion_pais(datos)

    return datos, total_pais

def report(data, total):
    chart_compara = reports.report_compare(data, 'Italy', 'France')
    guardar.save_viz(chart_compara, 'Compara_paises')

    chart_total = reports.paises_mayores_productores(total)
    guardar.save_viz(chart_total, 'Países que más producen')



def main():
    df = acquire()
    df_new = wrangle(df)
    datos, total_pais = analyze(df_new)

    #guardamos el csv
    guardar.guardar_csv(datos, 'Datos_totales')
    report(datos, total_pais)
    print(datos.head(5))
    

if __name__ == "__main__":
    main()