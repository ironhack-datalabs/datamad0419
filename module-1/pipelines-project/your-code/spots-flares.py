# funciones spots, flares(main).py


from pipeline import *

'''
Mi hipotesis alternativa es que las manchas solares estan de alguna manera relacionadas
con las llamaradas solares. Empezare uniendo dos datasets, uno de de las manchas y otro
de las llamaradas. Creare un pipeline, con varios archivos añadidos, para que sea un codigo
lo mas limpio y lo mas eficiente posible.

https://www.kaggle.com/heliodata/instruments-solarflares  # dataset llamaradas
'''



F=clean_flares(read('flares.csv'))



print (F)





'''
import quandl                                                            # quandl api
spots=quandl.get("SIDC/SUNSPOTS_D", authtoken="T9Wrh_cyK_Bvuz5TqJao")    # llamada al csv desde la api
spots=spots[(spots.index>='2010-05-01') & (spots.index<='2017-10-09')]   # seleccion por fecha
print (spots)
?client_id=TuNombreDeUsuario&client_secret={}
'''








