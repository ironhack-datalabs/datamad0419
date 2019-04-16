#!/usr/bin/env python
# coding: utf-8

# ## Global Historical Climatology Network Dataset
# Variables are stored in both rows and columns
# This dataset represents the daily weather records for a weather station (MX17004) in Mexico for five months in 2010.

# In[1]:



import os                   # se importan librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


datos=pd.read_csv(os.path.join('../weather-raw.csv'))   # se cargan los datos
print (datos.head())


# In[3]:


#print (datos.info())          # informacion de no nulos
print (datos.describe())       # descripcion estadistica


# In[4]:


null=datos.isna().sum()       # se miran los valores nulos
null[null>0]


# In[5]:


# me quedo solo con los datos de los sensores y pongo a cero los NaN para bucle
 
datos=datos.fillna(0)
datos=datos.iloc[:,4::]   # todas las columnas desde la 5ª
datos=datos.transpose()
print (datos)            # ahora cada columna es t_max o t_min de cada mes, falta septiembre


# In[12]:


# extraigo los datos de temperatura

lista=[datos[c] for c in datos]                # lista de cada columna de los datos              

Ene_M=np.mean([e for e in lista[0] if e!=0])   # busco las temperaturas max y min de cada mes, un poco a lo bruto
Ene_m=np.mean([e for e in lista[1] if e!=0])
Feb_M=np.mean([e for e in lista[2] if e!=0])   
Feb_m=np.mean([e for e in lista[3] if e!=0])
Mar_M=np.mean([e for e in lista[4] if e!=0])   
Mar_m=np.mean([e for e in lista[5] if e!=0])
Abr_M=np.mean([e for e in lista[6] if e!=0])   
Abr_m=np.mean([e for e in lista[7] if e!=0])
May_M=np.mean([e for e in lista[8] if e!=0])   
May_m=np.mean([e for e in lista[9] if e!=0])
Jun_M=np.mean([e for e in lista[10] if e!=0])   
Jun_m=np.mean([e for e in lista[11] if e!=0])
Jul_M=np.mean([e for e in lista[12] if e!=0])   
Jul_m=np.mean([e for e in lista[13] if e!=0])
Ago_M=np.mean([e for e in lista[14] if e!=0])   
Ago_m=np.mean([e for e in lista[15] if e!=0])
Oct_M=np.mean([e for e in lista[16] if e!=0])   
Oct_m=np.mean([e for e in lista[17] if e!=0])
Sep_M=(Ago_M+Oct_M)/2         # septiembre falta, hago la media de los meses adyacentes
Sep_m=(Ago_m+Oct_m)/2
Nov_M=np.mean([e for e in lista[18] if e!=0])   
Nov_m=np.mean([e for e in lista[19] if e!=0])
Dic_M=np.mean([e for e in lista[20] if e!=0])   
Dic_m=np.mean([e for e in lista[21] if e!=0])


# In[13]:


t_Max=[Ene_M, Feb_M, Mar_M, Abr_M, May_M, Jun_M, Jul_M, Ago_M, Sep_M, Oct_M, Nov_M, Dic_M]  # listas de temperaturas max y min anuales
t_min=[Ene_m, Feb_m, Mar_m, Abr_m, May_m, Jun_m, Jul_m, Ago_m, Sep_m, Oct_m, Nov_m, Dic_m]
print (t_Max)
print (t_min)


# In[16]:


plt.plot([i for i in range(12)], t_Max, linestyle='-', marker='.',color = 'r')  # plot rojo temp Max
plt.plot([i for i in range(12)], t_min, linestyle='-', marker='.',color = 'b')  # plot azul temp min
plt.xlabel('Meses',size=13)
plt.ylabel('Temperatura',size=13)
plt.title('MX17004',size=14,fontweight='bold')
plt.savefig('temperaturas_MX17004.png', format='png')   # guarda imagen
plt.show()


# In[20]:


# construyo el dataframe completamente limpiado
Meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

weather=pd.DataFrame(columns=Meses)
weather=weather.transpose()
weather['T_Max']=t_Max
weather['T_min']=t_min
weather.to_csv('weather.csv')  # se guarda el nuevo dataframe
print (weather)


# In[ ]:





# ## 
