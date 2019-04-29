import pandas as pd
import callapi

def datos_analisis(data):
    datos_analisis = data[data['Element'] == 'Food'].copy()
    return datos_analisis

def columna_continente(data, areas):
    area_continente = callapi.continentes(areas)   
    data['Continente'] = data['Area_ISO'].apply(lambda x : area_continente[x])

    return data

def total_produccion_pais_anyo(data):
    total = data.groupby(['Area']).sum()
    return total

def columna_total_alimento(data):
    data['Total'] = data[data.columns[4:57]].sum(axis=1)
    return data

def total_produccion_pais(data):
    total = data.groupby(['Area']).Total.sum()
    return total    

def produccion_bin(data):
    por_produccion = ['Muy baja', 'Baja', 'Media', 'Alta', 'Muy Alta']
    cutoffs = [0, 100000, 200000, 300000, 500000, 10000000]

    produccion_bins = pd.cut(data['Total'], cutoffs, labels = por_produccion)
    data['Nivel Producción'] = produccion_bins
    
    return data   
