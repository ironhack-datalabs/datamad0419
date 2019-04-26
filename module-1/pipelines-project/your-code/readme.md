
El dataset elegido ha sido: **18,393 Pitchfork Reviews**, un conjunto de reviews de álbums de música de la revista Pitchfork *de Enero del año 1999 a Enero del 2017*.
Link: (https://www.kaggle.com/nolanbconaway/pitchfork-data)

Dado que el dataset estaba en formato **.sqlite**, he tenido que descargarlo y convertir en *.csv* las diferentes columnas (a excepción de artistas, cuyas columnas ya estaban en las demás y no era necesaria).


# ¡Manos a la obra!

## Importamos los datos.

Primero importamos las librerias con las que vamos a trabajar, en este caso *pandas*, *numpy*, *functools* (import reduce) y mi archivo de funciones: *functionspipe*.