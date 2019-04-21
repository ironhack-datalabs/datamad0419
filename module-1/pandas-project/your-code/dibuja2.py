# -*- coding: utf-8 -*-
# para dibujar2

from matplotlib import pyplot as plt        # para plots
import numpy as np                          # numerical python, algebra lineal


def dibuja2(datos):
	fig=plt.figure()                                # subplots de 6 especies
	fig.subplots_adjust(hspace=0.7, wspace=0.7)     # ajuste de espacio  entre plots
	
	plt.subplot(5,1,1)                                    # posicion subplot
	años0=datos[datos['Clase_Daños'].isin(['0'])]["Año"].value_counts().sort_index()
	años0.plot(color='g', label='Sin daño')			
	#plt.title('Sin daño',size=10,fontweight='bold')     # titulo
	plt.legend(loc='best')
	

	
	plt.subplot(5,1,2)                                    # posicion subplot
	años1=datos[datos['Clase_Daños'].isin(['1'])]["Año"].value_counts().sort_index()
	años1.plot(color='b', label='Daño bajo')			
	#plt.title('Daño Bajo',size=10,fontweight='bold')    # titulo
	plt.legend(loc='best')
	
	

	plt.subplot(5,1,3)                                    # posicion subplot
	años0=datos[datos['Clase_Daños'].isin(['2'])]["Año"].value_counts().sort_index()
	años0.plot(color='y', label='Daño medio')			
	#plt.title('Daño medio',size=10,fontweight='bold')   # titulo
	plt.ylabel('Numero de ataques',size=12)             # etiqueta eje y
	plt.legend(loc='best')	


	
	plt.subplot(5,1,4)                                    # posicion subplot
	años0=datos[datos['Clase_Daños'].isin(['3'])]["Año"].value_counts().sort_index()
	años0.plot(color='orange', label='Daño alto')			
	#plt.title('Daño alto',size=10,fontweight='bold')     # titulo
	plt.legend(loc='best')



	plt.subplot(5,1,5)                                    # posicion subplot
	años0=datos[datos['Clase_Daños'].isin(['4'])]["Año"].value_counts().sort_index()
	años0.plot(color='r', label='Mortal')			
	#plt.title('Mortal',size=10,fontweight='bold')     # titulo
	plt.xlabel('Año',size=12)                           # etiqueta eje x
	plt.legend(loc='best')
	
	
	plt.show()
	return ''
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	








