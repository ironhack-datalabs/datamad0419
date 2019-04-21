# -*- coding: utf-8 -*-
# para dibujar

from matplotlib import pyplot as plt        # para plots

def dibuja(datos):
	fig=plt.figure()                                # subplots de 6 especies
	fig.subplots_adjust(hspace=0.4, wspace=0.4)     # ajuste de espacio  entre plots
	#plt.rcParams["figure.figsize"]=(15,15)         # ajuste de tamaño completo
	
	plt.subplot(3,2,1)           # posicion subplot
	ataque=datos[datos['Especie(clean)'].isin(['White'])]["Clase_Daños"].value_counts().sort_index()
	#datos
	#plt.ylim(0, 260)                                           # ajusta eje y
	ataque.plot(kind='bar', color=['g','b','y','orange','r'])   # dibuja
	plt.title('White shark',size=12,fontweight='bold')          # titulo
	plt.ylabel('Numero de ataques',size=10)                     # etiqueta eje y
	
	plt.subplot(3,2,2)
	ataque=datos[datos['Especie(clean)'].isin(['Tiger'])]["Clase_Daños"].value_counts().sort_index()
	ataque.plot(kind='bar', color= ['g','b','y','orange','r'])
	plt.title('Tiger shark',size=12,fontweight='bold')
	
	plt.subplot(3,2,3)
	ataque=datos[datos['Especie(clean)'].isin(['Bull'])]["Clase_Daños"].value_counts().sort_index()
	ataque.plot(kind='bar', color=['g','b','y','orange','r'])
	plt.title('Bull shark',size=12,fontweight='bold')
	plt.ylabel('Numero de ataques',size=10)
	
	plt.subplot(3,2,4)
	ataque=datos[datos['Especie(clean)'].isin(['Blacktip'])]["Clase_Daños"].value_counts().sort_index()
	ataque.plot(kind='bar', color=['g','b','y','orange','r'])
	plt.title('Blacktip shark',size=12,fontweight='bold')
	
	plt.subplot(3,2,5)
	ataque=datos[datos['Especie(clean)'].isin(['Nurse'])]["Clase_Daños"].value_counts().sort_index()
	ataque.plot(kind='bar', color=['g','b','y','orange','r'])
	plt.title('Nurse shark',size=12,fontweight='bold')
	plt.xlabel('Tipo de ataque',size=10)                   # etiqueta eje x
	plt.ylabel('Numero de ataques',size=10)
	
	plt.subplot(3,2,6)
	ataque=datos[datos['Especie(clean)'].isin(['Bronze'])]["Clase_Daños"].value_counts().sort_index()
	ataque.plot(kind='bar', color=['g','b','y','orange','r'])
	plt.title('Bronze shark',size=12,fontweight='bold')
	plt.xlabel('Tipo de ataque',size=10)
	
	plt.show()
	return "Tipo de ataque: '0'=sin daños, '1'=daño bajo, '2'=daño medio, '3'=daño alto, '4'=mortal\
	        \
	                Plots de las 6 especies de tiburón que más atacan." 




