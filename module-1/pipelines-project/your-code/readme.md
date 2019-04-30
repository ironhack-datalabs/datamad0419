
El dataset elegido ha sido: [**18,393 Pitchfork Reviews**](https://www.kaggle.com/nolanbconaway/pitchfork-data), un conjunto de reviews de álbums de música de la revista Pitchfork *de Enero del año 1999 a Enero del 2017*.
Link de selección de colores: https://htmlcolorcodes.com/color-picker/

Dado que el dataset estaba en formato **.sqlite**, he tenido que descargarlo y convertir en *.csv* las diferentes columnas (a excepción de artistas, cuyas columnas ya estaban en las demás y no era necesaria).

**Mi objetivo a analizar es encontrar si hay un estilo preferido por los reviewers de la revista y la valoración media de los álbumes según las notas asignadas.**


# ¡Manos a la obra!


## Importamos los datos.

Primero importamos las librerias con las que vamos a trabajar, en este caso *pandas*, *numpy*, *functools* (import reduce), *matplotlib*, *requests* y mi archivo de funciones: *functionspipe*.

Visualizamos los .csv que hemos importado y hacemos un merge de los mismos a través de la función reduce de *functools*.
http://oi63.tinypic.com/29vmdmh.jpg


## Trabajo con el Dataframe.
Analizamos si hay columnas nulas y si es así eliminamos las de mayor valor de números nulos. En este caso se elimina a **author_type**.

Posteriormente eliminamos las columnas que no nos interesan para nuestro análisis: **content**, **label**, **url**, **best_new_music**, **author**, **pub_date**, **pub_weekday**, **pub_day**, **pub_month**, **pub_year**.
Nos quedamos con *6 columnas*.

Seguidamente, eliminamos valores duplicados, renombramos la columna **title** como **album** y ordenamos el dataset.

Con la variable **year**, asignamos los valores nulos a 0 y transformamos la variable a una variable tipo: int64 para eliminar los float y eliminamos los valores nulos.

Hacemos lo mismo con la variable **genre**, asignamos los valores nulos a 0 y los eliminamos del dataframe.

Por último, lo mismo con la variable **album** y, al comprobar que ahora hay valores duplicados tanto en *reviewid, artist y album*, los eliminamos y nos quedamos con el primero.
Seguidamente ordenamos el dataset de manera ascendente en función de la columna score.
http://oi63.tinypic.com/2m5ma2f.jpg


## Análisis del Dataframe.

Hacemos los bins de score para representarlos gráficamente donde: 
- Pésimo: Notas de 0 a 3.
- Flojo: Notas de 3 a 5.
- Para fans: Notas de 5 a 6.
- Recomendado: Notas de 6 a 8.
- Muy bueno: Notas de 8 a 9.
- Obra maestra: Notas 9/10.

Filtramos el dataset a sólo los elementos con nota de #10. Imprimimos los diferentes estilos de música que abarcan los álbumes con mayor nota y mostramos el número de elementos.


## Añadimos la API.

Usamos la API de *last.fm* con la apiKey personal para obtener el resultado que nos da en relación al artista y álbum en concreto y así obtener el número de oyentes del mismo.

Una vez obtenidos los datos los pasamos a un Dataframe e incorporamos al que teníamos con anterioridad. Dado que algunos elementos no pudieron ser obtenidos con la API y eran valores nulos los eliminamos y ordenamos en Dataframe en función del número de oyentes por álbum.
http://oi65.tinypic.com/28v5850.jpg

Guardamos el Dataset final.


## Hacemos Gráficos.

Graficamos el ranking de álbumes según la revista a partir de los bins.
rankingscore.png

También hacemos un gráfico de barras para analizar los géneros preferidos por la revista Pitchfork en función las reviews con nota 10.
genrespreferred.png