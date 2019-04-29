import re

def renombra_columnas_year_aux(c):
    if len(c) > 4:
        if re.match('^(?=.*[0-9])', c):
            return c[1:]
        else:
            return c
    else:
        return c

def renombra_columnas(data):  
    data_columns = [renombra_columnas_year_aux(c) for c in data.columns]
    data.columns = data_columns
    #otras columnas a renombrar
    data = data.rename(columns = {'Area Abbreviation' : 'Area_ISO'})
    return data

def eliminar_columnas(data):
    nueva_data = data.drop(['Area Code', 'Item Code', 'Element Code', 'Unit', 'latitude', 'longitude'], axis=1)
    return nueva_data