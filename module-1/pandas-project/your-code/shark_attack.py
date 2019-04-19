# -*- coding: utf-8 -*-
# shark_attack.py



'''
Mi objetivo es relacionar la mortalidad y el tipo de daños causados con la 
especie de tiburon para descubrir, no solo que especie es la que genera mayor tasa de mortalidad, 
sino tambien que especie provoca mayores daños no mortales.

En una segunda parte intentare construir una serie temporal con esa informacion 
para tratar de responder una pregunta:
¿los tiburones se estan volviendo mas agresivos con el tiempo?.   
De ser cierto, ¿esta relacionado con la actividad humana?.
'''


#1º
import pandas as pd                    # dataframe
from matplotlib import pyplot as plt   # para plots




#2º
datos=pd.read_csv('attacks.csv', encoding='ISO-8859-1')           # se crea el dataframe
#print (datos)
#print (datos.columns)




#3º
datos=datos[['Year',  'Type', 'Activity', 'Species ', 'Injury', 'Fatal (Y/N)']]  # se escogen los datos a tratar
# elimino el resto de columnas porque no me hacen falta para el proposito del estudio
datos=datos.rename(columns={'Year': 'Año', 'Type': 'Tipo', 'Activity': 'Actividad',\
                            'Species ': 'Especie', 'Injury': 'Daños', 'Fatal (Y/N)': 'Mortal'}) 
# renombro las columnas por comodidad




#4º
datos['Año']=datos[datos['Año']>=1940]['Año']        # una primera seleccion de datos, desde 1940
datos=datos.dropna(how='all')                        # elimina Nan, desde el registro 6304 no hay datos
datos=datos.iloc[0:4782, :]                          # ahora solo me quedo con los registros desde 1940, 4783 registros
# print (datos['Año'])




#5º
datos=datos.fillna('UNKNOWN')                                   # renombro los valores nulos...
datos=datos[datos['Especie'].map(lambda x: str(x)!='UNKNOWN')]  # ... y los elimino segun ese nombre.
datos.index=range(len(datos))                                   # reindexo el frame por si lo necesito en el futuro 
#print (datos.shape)                                             # 2993 registros
null=datos.isna().sum()                                         # se miran los valores nulos
#print (null[null>0])                                            # el frame esta limpio




#6º














