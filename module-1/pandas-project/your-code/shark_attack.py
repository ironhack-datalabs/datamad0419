# -*- coding: utf-8 -*-
# shark_attack.py



'''
Mi objetivo es relacionar la mortalidad y el tipo de daños causados con la 
especie de tiburon para descubrir, no solo que especie es la que genera mayor tasa de mortalidad, 
sino tambien que especie provoca mayores daños no mortales.

En una segunda parte intentare construir una serie temporal con esa informacion 
para tratar de responder una pregunta:
¿los tiburones se estan volviendo mas agresivos con el tiempo?   
De ser cierto, ¿esta relacionado con la actividad humana?
'''



import pandas as pd                    # dataframe
from matplotlib import pyplot as plt   # para plots






datos=pd.read_csv('attacks.csv', encoding='ISO-8859-1')           # se crea el dataframe
#print (datos)
#print (datos.columns)


datos=datos[['Date', 'Type', 'Activity', 'Species ', 'Injury', 'Fatal (Y/N)']]  # se escogen los datos a tratar
print (datos.head())























