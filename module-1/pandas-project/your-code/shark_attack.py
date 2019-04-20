# -*- coding: utf-8 -*-
# shark_attack.py



'''
Mi objetivo es relacionar la mortalidad y el tipo de daños causados con la 
especie de tiburon para descubrir, no solo que especie es la que genera mayor tasa de mortalidad, 
sino tambien que especie provoca mayores daños no mortales.

En una segunda parte intentare construir una serie temporal con esa informacion 
para tratar de responder una pregunta:
¿los tiburones se estan volviendo mas agresivos con el tiempo?.   
De ser cierto, ¿esta relacionado con la actividad humana?. (esto para otra)
'''


#1º
import pandas as pd                    # dataframe
from matplotlib import pyplot as plt   # para plots
from regEX import *                    # expresiones regulares, clasificacion ataque
from shark import *                    # expresiones regulares, limpieza especie



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
#datos['Año']=datos[datos['Año']>=1940]['Año']        # una primera seleccion de datos, desde 1940, solo para visualizacion[i]
datos=datos.dropna(how='all')                        # elimina Nan, desde el registro 6302 no hay datos
#print (datos.shape)
datos=datos[datos.Año>=1940]                        # una primera seleccion de datos, desde 1940
#datos=datos.iloc[0:4782, :]                          # ahora solo me quedo con los registros desde 1940, 4780 registros
#print (datos['Año'])
#print (datos.shape)



#5º
datos=datos.fillna('UNKNOWN')                                   # renombro los valores nulos...
datos=datos[datos['Especie'].map(lambda x: str(x)!='UNKNOWN')]  # ... y los elimino segun ese nombre.
datos=datos.drop_duplicates()                                   # se eliminan duplicados
#print (datos.shape)                                             # 2980 registros
datos.index=range(len(datos))                                   # reindexo el frame por si lo necesito en el futuro 
null=datos.isna().sum()                                         # se miran los valores nulos
#print (null[null>0])                                            # el frame esta limpio




#6º
# clasifico el tipo de ataque: clase '0'=sin daños, '1'=daño bajo, '2'=daño medio, '3'=daño alto, '4'=mortal
datos.loc[datos['Mortal']=='Y', 'Daños']='4'                     # cambio los mortales a clase '4'
#print (datos['Daños'])		
str_daños=[datos['Daños'][i].lower() for i in range(len(datos))]   # pasa a minusculas
datos['Clase_Daños']=regEX(str_daños)                              # clasificacion categorica de los ataques
#print (datos)



#7º 
# Ahora las especies
str_shark=[datos['Especie'][i].lower() for i in range(len(datos))]   # pasa a minusculas
datos['Especie(clean)']=shark(str_shark)                             # limpieza especies
#print (shark(str_shark))
#print (datos)




#8º 
# plot por especie, numero de ataques
tiburones=datos['Especie(clean)'].value_counts()
#print (tiburones)
tiburones[(tiburones<800) & (tiburones>10)].plot.barh(color='red')   # ataque entre 10 y 800
plt.title('Ataques por especie',size=14,fontweight='bold')
plt.xlabel('Numero de ataques',size=13)
plt.show()


'''
#9º
# plot mortal si o no
datos[datos['Mortal'].isin(['N','Y'])]["Mortal"].value_counts().plot(kind='bar', color= ['green','red'])
plt.title('Ataques mortales',size=14,fontweight='bold')
plt.ylabel('Numero de ataques',size=13)
plt.show()   
'''


#10º
# plots tipo de ataque y especie (blanco, tigre, toro, punta negra, nodriza, bronce)
fig=plt.figure()                                # subplots de 6 especies
fig.subplots_adjust(hspace=0.4, wspace=0.4)     # ajuste de espacio

plt.subplot(3,2,1)           # posicion subplot
ataque=datos[datos['Especie(clean)'].isin(['White'])]["Clase_Daños"].value_counts().sort_index()
#datos
#plt.ylim(0, 260)                                           # ajusta eje y
ataque.plot(kind='bar', color= ['g','b','y','orange','r'])  # dibuja
plt.title('White shark',size=12,fontweight='bold')          # titulo
plt.ylabel('Numero de ataques',size=10)                     # etiqueta eje y

plt.subplot(3,2,2)
ataque=datos[datos['Especie(clean)'].isin(['Tiger'])]["Clase_Daños"].value_counts().sort_index()
ataque.plot(kind='bar', color= ['g','b','y','orange','r'])
plt.title('Tiger shark',size=12,fontweight='bold')

plt.subplot(3,2,3)
ataque=datos[datos['Especie(clean)'].isin(['Bull'])]["Clase_Daños"].value_counts().sort_index()
ataque.plot(kind='bar', color= ['g','b','y','orange','r'])
plt.title('Bull shark',size=12,fontweight='bold')
plt.ylabel('Numero de ataques',size=10)

plt.subplot(3,2,4)
ataque=datos[datos['Especie(clean)'].isin(['Blacktip'])]["Clase_Daños"].value_counts().sort_index()
ataque.plot(kind='bar', color= ['g','b','y','orange','r'])
plt.title('Blacktip shark',size=12,fontweight='bold')

plt.subplot(3,2,5)
ataque=datos[datos['Especie(clean)'].isin(['Nurse'])]["Clase_Daños"].value_counts().sort_index()
ataque.plot(kind='bar', color= ['g','b','y','orange','r'])
plt.title('Nurse shark',size=12,fontweight='bold')
plt.xlabel('Tipo de ataque',size=10)                   # etiqueta eje x
plt.ylabel('Numero de ataques',size=10)

plt.subplot(3,2,6)
ataque=datos[datos['Especie(clean)'].isin(['Bronze'])]["Clase_Daños"].value_counts().sort_index()
ataque.plot(kind='bar', color= ['g','b','y','orange','r'])
plt.title('Bronze shark',size=12,fontweight='bold')
plt.xlabel('Tipo de ataque',size=10)
plt.show() 


#ataque0=datos[(datos['Clase_Daños'].isin(['0']))&(datos['Especie(clean)']!='Other')\
               #&(datos['Especie(clean)']!='')]["Especie(clean)"].value_counts().sort_index()    # ataque sin daño
#ataque0.plot(kind='bar', color= 'g')
#ataque1=datos[(datos['Clase_Daños'].isin(['1']))&(datos['Especie(clean)']!='Other')\
               #&(datos['Especie(clean)']!='')]["Especie(clean)"].value_counts().sort_index()    # ataque daño bajo
#ataque1.plot(kind='bar', color= 'b')
#ataque0.plot(kind='bar', color= 'g')
#plt.xticks(rotation=60)
#plt.show()                         # para multihistograma (todavia no sale)




#11º






