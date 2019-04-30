import pandas as pd
import numpy as np
import argparse

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
    datos_paises = analisis.columna_total_alimento(datos)
    datos_paises = analisis.produccion_bin(datos)
    total_pais = analisis.total_produccion_pais(datos)

    return datos_paises, total_pais

def report(data, total):
    pais1 = reports.comprobar_pais(data, args.pais1)
    pais2 = reports.comprobar_pais(data, args.pais2)

    chart_compara = reports.report_compare(data, pais1, pais2, args.ver)
    guardar.save_viz(chart_compara, 'Compara_paises')

    chart_total = reports.paises_mayores_productores(total, args.ver)
    guardar.save_viz(chart_total, 'Los 5 países que más producen - Valores por 1000 toneladas')

#Para pasar los valores de los paises
parser = argparse.ArgumentParser(description='Genera un gráfico comparando los datos de los paises eligidos')
parser.add_argument('--p1', dest = 'pais1',
                    default = 'Italy',
                    help = 'País 1 para la comparación')
parser.add_argument('--p2', dest = 'pais2',
                    default = 'France',
                    help = 'País 2 para la comparación') 
parser.add_argument('-v', dest = 'ver',
                    default = 0,
                    type = int,
                    help = 'Ver gráfica')                                        

args = parser.parse_args()



def main():
    df = acquire()
    df_new = wrangle(df)
    datos, total_pais = analyze(df_new)
    #guardamos el csv
    guardar.guardar_csv(datos, 'Datos_totales')
    report(datos, total_pais)
    
    

if __name__ == "__main__":
    main()