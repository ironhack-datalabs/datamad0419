# -*- coding: utf-8 -*-
# shark_attack.py

# borrador


'''
Mi objetivo es relacionar la mortalidad y el tipo de daños causados con la 
especie de tiburon para descubrir, no solo que especie es la que genera mayor tasa de mortalidad, 
sino tambien que especie provoca mayores daños no mortales.

En una segunda parte intentare construir una serie temporal con esa informacion 
para tratar de responder una pregunta:
¿los tiburones se estan volviendo mas agresivos con el tiempo?.   
De ser cierto, ¿esta relacionado con la actividad humana?. (esta pregunta para otra ocasion)
'''


#1º
#importa librerias
import pandas as pd                    # dataframe
from dibuja import *                   # para plots
from dibuja2 import *                  # para plots
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
#print (null[null>0])                                            # el frame esta limpio, casi




#6º
# clasifico el tipo de ataque: clase '0'=sin daños, '1'=daño bajo, '2'=daño medio, '3'=daño alto, '4'=mortal
datos.loc[datos['Mortal']=='Y', 'Daños']='4'                     # cambio los mortales a clase '4'
#print (datos['Daños'])		
str_daños=[datos['Daños'][i].lower() for i in range(len(datos))]   # pasa a minusculas
datos['Clase_Daños']=regEX(str_daños)                              # clasificacion categorica de los ataques

datos.loc[datos['Clase_Daños']=='4', 'Mortal']='Y'       # limpio de 'UNKNOWN' la columna Mortal por la Clase_Daños
datos.loc[datos['Clase_Daños']=='3', 'Mortal']='N'
datos.loc[datos['Clase_Daños']=='2', 'Mortal']='N'
datos.loc[datos['Clase_Daños']=='1', 'Mortal']='N'
datos.loc[datos['Clase_Daños']=='0', 'Mortal']='N'
#print (datos)



#7º 
# Ahora las especies
str_shark=[datos['Especie'][i].lower() for i in range(len(datos))]   # pasa a minusculas
datos['Especie(clean)']=shark(str_shark)                             # limpieza especies
#print (shark(str_shark))
#print (datos)



'''
#8º 
# plot por especie, numero de ataques
tiburones=datos['Especie(clean)'].value_counts()
#print (tiburones)
tiburones[(tiburones<800) & (tiburones>10)].plot.barh(color='red')   # ataque entre 10 y 800
plt.title('Ataques por especie',size=14,fontweight='bold')
plt.xlabel('Numero de ataques',size=13)
plt.show()



#9º
# plot mortal si o no
datos[datos['Mortal'].isin(['N','Y'])]["Mortal"].value_counts().plot(kind='bar', color= ['green','red'])
plt.title('Ataques mortales',size=14,fontweight='bold')
plt.ylabel('Numero de ataques',size=13)
plt.show()   
'''


#10º
# plots tipo de ataque y especie (blanco, tigre, toro, punta negra, nodriza, bronce)
'''
#ataque0=datos[(datos['Clase_Daños'].isin(['0']))&(datos['Especie(clean)']!='Other')\
               #&(datos['Especie(clean)']!='')]["Especie(clean)"].value_counts().sort_index()    # ataque sin daño
#ataque0.plot(kind='bar', color= 'g')
#ataque1=datos[(datos['Clase_Daños'].isin(['1']))&(datos['Especie(clean)']!='Other')\
               #&(datos['Especie(clean)']!='')]["Especie(clean)"].value_counts().sort_index()    # ataque daño bajo
#ataque1.plot(kind='bar', color= 'b')
#ataque0.plot(kind='bar', color= 'g')
#plt.xticks(rotation=60)
#plt.show()                         # para multihistograma (todavia no sale)
'''
#print(dibuja(datos))


#11º
# creo un dataframe del porcentaje de cada tipo de ataque segun especie
pd.options.display.float_format = '{:.2f}'.format         # formato con dos decimales en pandas

ataque_w=datos[datos['Especie(clean)'].isin(['White'])]["Clase_Daños"].value_counts().sort_index()
total_w=ataque_w.sum()

ataque_t=datos[datos['Especie(clean)'].isin(['Tiger'])]["Clase_Daños"].value_counts().sort_index()
total_t=ataque_t.sum()

ataque_bu=datos[datos['Especie(clean)'].isin(['Bull'])]["Clase_Daños"].value_counts().sort_index()
total_bu=ataque_bu.sum()

ataque_bl=datos[datos['Especie(clean)'].isin(['Blacktip'])]["Clase_Daños"].value_counts().sort_index()
total_bl=ataque_bl.sum()

ataque_n=datos[datos['Especie(clean)'].isin(['Nurse'])]["Clase_Daños"].value_counts().sort_index()
total_n=ataque_n.sum()

ataque_br=datos[datos['Especie(clean)'].isin(['Bronze'])]["Clase_Daños"].value_counts().sort_index()
total_br=ataque_br.sum()


tipo_ataque=pd.DataFrame(columns=['White', 'Tiger', 'Bull', 'Blacktip', 'Nurse', 'Bronze'])

tipo_ataque['White']=[ataque_w[i]*100/total_w for i in range(len(ataque_w))]
tipo_ataque['Tiger']=[ataque_t[i]*100/total_t for i in range(len(ataque_t))]
tipo_ataque['Bull']=[ataque_bu[i]*100/total_bu for i in range(len(ataque_bu))] 
tipo_ataque['Blacktip']=pd.Series([ataque_bl[i]*100/total_bl for i in range(len(ataque_bl))])
tipo_ataque=tipo_ataque.fillna('0')        # he de hacer esto porque las longitudes no coinciden
tipo_ataque['Nurse']=[ataque_n[i]*100/total_n for i in range(len(ataque_n))]
tipo_ataque['Bronze']=[ataque_br[i]*100/total_br for i in range(len(ataque_br))]

tipo_ataque=tipo_ataque.transpose()
tipo_ataque=tipo_ataque.rename(columns={0:'%-Sin daños', 1:'%-Daño bajo', 2:'%-Daño medio', 3:'%-Daño alto', 4:'%-Mortal'}) 

#print (tipo_ataque)
tipo_ataque.to_csv('tipo_ataque(6-especies).csv')  # guardo este dataframe



'''
Una primera conclusión es que, en contra de lo que pudiera parecer, no es el tiburón blanco el que tiene 
una mayor tasa de mortalidad, sino el tiburón tigre. Por supuesto, el tiburon blanco ataca unas tres veces
más que el tiburón tigre, y en términos absolutos mata a más personas, pero el tiburón tigre tiene un 3,5% más 
de ataques mortales en términos relativos.
Es interesante observar que el tiburón blanco tiene la mayor tasa de ataques sin daños, lo cual puede ser debido 
a su comportamiento de morder para probar antes de decidir si la presa es buena.
Por otro lado, tampoco es el tiburón blanco el que más daños provoca en sus ataques. En el caso de las lesiones
graves y leves, el tiburón que más daños causa es el tiburón nodriza, y en el caso de lesiones de tipo medio es
el tiburón de punta negra. De éste último no existen registros de ataques mortales, aunque también tiene un alto
porcentaje de lesiones graves en sus víctimas.
Ahora intentaré observar como cambian estos datos con el tiempo. 
'''


#12º
# plots nº ataques vs tiempo segun tipo de daños

#plt.rcParams["figure.figsize"]=(15,15)          # ajuste de tamaño completo
#print (dibuja2(datos))                          # subplots temporales segun tipo de daños



'''
He intentado hacer una regresión lineal en cada plot para ver la pendiente, pero aún no se hacerlo con 
pandas.plot, no es como con numpy. Dicha pendiente sería un buen indicador.
Sin embargo, puede observarse un repunte en las dos últimas décadas de los ataques sin daño, con daño bajo y 
daño medio. Las series de daño alto y mortal parecen ser estacionarias, que oscilan alrededor de un valor.
Con esto es complicado llegar a una buena conclusión. Pudiera ser que actualmente se recogen más y mejores
datos, que el registro es más amplio. También pudiera ser que efectivamente los tiburones han atacado más en 
las dos últimas décadas, aunque de ser así lo han de hecho de una manera menos agresiva. También es posible
que el cambio climático y el aumento de la población humana conlleve un mayor número de ataques. Asi pues, 
¿los tiburones se estan volviendo mas agresivos con el tiempo?, sería necesario un nuevo estudio para llegar 
a una conclusión en firme.

Por último, y no menos importante, pues es el objetivo primero de éste proyecto, se extrae el dataframe limpio.
'''


#13º
# se exporta el dataframe limpio
# ahora elimino tambien el Tipo y la Actividad, pues no lo he utilizado en el estudio
attacks_clean=pd.DataFrame()
attacks_clean['Year']=datos['Año']
attacks_clean['Species']=datos['Especie(clean)']
attacks_clean['Injury']=datos['Daños']
attacks_clean['Injury_Class']=datos['Clase_Daños']
attacks_clean['Fatal (Y/N)']=datos['Mortal']
print (attacks_clean)
attacks_clean.to_csv('attacks(clean).csv')













