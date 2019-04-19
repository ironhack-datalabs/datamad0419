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



import pandas as pd                    # dataframe
from matplotlib import pyplot as plt   # para plots






datos=pd.read_csv('attacks.csv', encoding='ISO-8859-1')           # se crea el dataframe
#print (datos)
#print (datos.columns)


datos=datos[['Year',  'Type', 'Activity', 'Species ', 'Injury', 'Fatal (Y/N)']]  # se escogen los datos a tratar
# elimino el resto de columnas porque no me hacen falta para el proposito del estudio

datos['Year']=datos[datos['Year']>=1940]['Year']              # una primera seleccion de datos, desde 1940
datos=datos.dropna(how='all')                                 # elimina Nan, desde el registro 6304 no hay datos
datos=datos.iloc[0:4782, :]                                   # ahora solo me quedo con los registros desde 1940, 4783 registros
#print (datos['Year'])

#print (datos.shape)
datos=datos.dropna(how='all')                                 # elimina Nan, desde el registro 6304 no hay datos
#print (datos.shape)
null=datos.isna().sum()                                       # se miran los valores nulos
#print (null[null>0])


datos=datos.fillna('UNKNOWN')
#print (datos.shape)
print (null[null>0])
#print (datos['Species '])
#print (datos)
#print (datos.dtypes)




