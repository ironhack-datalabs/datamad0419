# Pipelines Project

Para este proyecto, escogí un dataset de los terremotos ocurridos en Turquía entre los años 1910 y 2017. En él se puede encontrar información sobre la geolocalización del terremoto (latitud y longitud, ciudad, área...), información temoporal (la fecha y la hora) y otros campos de datos técnicos (Escala de Richter y otros). La URL del dataset es la siguiente: https://www.kaggle.com/caganseval/earthquake.

Mi idea inicial era enriquecer este dataset con información acerca de la población de las ciudades turcas, para estudiar la relación entre la frecuencia de los terremotos y la densidad de población en las diferentes regiones. Sin embargo, ante la dificultad para encontrar una API que diera esta información, descarté esta opción.

Explorando los datos, vi que faltaban muchos datos en el campo 'city'. Entonces se me ocurrió buscar una API que, a partir de las coordenadas de latitud y longitud, me proporcionara la ciudad. Por suerte la encontré. Esta técnica se llama 'reverse geolocation'. La URL de la API es la siguiente: https://rapidapi.com/Noggle/api/reverse-geocoding-and-geolocation-service.

Tras conseguir hacer las peticiones y obtener los resultados que buscaba, decidí que los outputs del proyecto iban a ser dos:

* La evolución de los terremotos en los últimos años según la Escala de Richter (https://es.wikipedia.org/wiki/Escala_sismol%C3%B3gica_de_Richter)
* Las ciudades que más teremotos han sufrido en los últimos años

## Adquisición:

Para obtener la información en mi programa, simplemente tuve que leer el csv a través de la librería Pandas.

## Limpieza de datos:

Lo primero que hice fue buscar registros duplicados. No los había, así que aqui no hubo que hacer nada.

Quería tener el dato de los años para cada registro, pero no existía. Entonces, tuve que sacarlo del campo 'date', que tiene el formato 'AAAA.MM.DD'. Creé una nueva columna con este campo.

Explorando los datos, vi que los registros de terremotos antes de 2004 eran muy reducidos, así que me enfoqué en los años 2004 - 2017. Eliminé todos los registros anteriores.

Además, en el campo de la magnitud en la Escala de Richter, había registros con 0. Eliminé también estos registros.

En este momento llega la hora de utilizar la API. Definí una función cuyo input es una tupla de latitud y longitud y cuyo output es, a través de una petición a dicha API, el nombre de la ciudad más cercana a esas coordenadas. Nuestro dataset tenía unas 6000 líneas, por lo que había que hacer ese mismo número de peticiones. Comprobé si se repetían las ciudades y las coordenadas, para intentar hacer menos llamadas a la API, pero la coordenada que más se repetía lo hacía 7 veces, por lo que no vi otra solución que hacer las 6000 peticiones.

Hice un bucle para crear una lista que contuviera todas las ciudades de esos 6000 registros, el cual tardó una hora. Debido a esto, decidí guardarme el dataset en este punto y usarlo, ya que no me podía permitir esperar una hora cada vez que corriera el programa.

En este momento creé una columna nueva con unos bins de la magnitud en la Escala de Richter (de 0 a 4, de 4 a 5 y de 5 a 7)

## Análisis:

Para llegar a mis dos objetivos, creé dos dataframes. Como he adelantado antes, el primero contenía información acerca de la evolución de los terremotos en los últimos años (2004 - 2017) según su magnitud en la Escala de Richter (usando los bins). Por otro lado, el segundo dataframe contiene las 15 ciudades que más terremotos han sufrido en los años del estudio.

## Informe:

El informe son dos gráficos hechos usando la librería Matplotlib.

/home/dani/aaironhack/datamad0419/datamad0419/module-1/pipelines-project/your-code/earthquake_year.png

* En el primer gráfico podemos ver dos tendencias. Una que va desde 2004 hasta 2010, con una media de 250 terremotos anuales y otra desde 2011 a 2017, con una media de 600 anuales. Respecto a la magnitud de los mismos, la proporción de su magnitud es más o menos constante, siendo la mayor parte de terremotos de magnitud entre 0 y 4.

/home/dani/aaironhack/datamad0419/datamad0419/module-1/pipelines-project/your-code/top15.png

* En el segundo gráfico podemos ver las 15 ciudades con más terremotos sufridos durante los años del estudio. La primera es Sitia, con más de 300, seguida por Ercis, Van y Changelos, con unos 250.

### Enlace al proyecto:

https://github.com/ironhack-datalabs/datamad0419/pull/238