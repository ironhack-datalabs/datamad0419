# main.py


from pipeline import *

'''
Mi hipotesis alternativa es que el numero de manchas solares esta de alguna manera relacionado
con las llamaradas solares. Empezare uniendo dos datasets, uno de de las manchas y otro
de las llamaradas. Creare un pipeline, con varios archivos añadidos, para que sea un codigo
lo mas limpio y lo mas eficiente posible.

https://www.kaggle.com/heliodata/instruments-solarflares  # dataset llamaradas
gracias a https://arxiv.org/abs/1703.04412

desde la API Quandl dataset manchas:
https://www.quandl.com/data/SIDC/SUNSPOTS_D-Total-Sunspot-Numbers-Daily 
'''


if __name__=="__main__":
	df=data()
	#corr=np.corrcoef(df['Spots Number'],df['Month Mean'])      
	#print (corr) 
	draw(df)    
	#print (df)                              
	             
	
	

'''
No parece existir una relación entre el número de manchas solares y el número de llamaradas solares,
en éste caso habría que quedarse con la hipótesis nula. De hecho el coeficiente de correlación es 0,32.
referencia : http://adsabs.harvard.edu/abs/2004AAS...205.1002S
''' 











	
