# Pipelines Project - Producción de alimentos proporcionado por la FAO

## Descripción

Para la realización de este proyecto se ha optado por el siguiente dataset:

[Who eats the food we grow?](https://www.kaggle.com/dorbicycle/world-foodfeed-production)

Muestra los datos de producción de alimentos por los distintos paises desde el año 1961 hasta el 2013

Food - Se refiere a la cantidad total de alimento disponible como alimento humano.
Feed - Se refiere a la cantidad de alimento disponible para alimentar al ganado y las aves de corral.
En la columna de los años, las cantidades están expresadas en 1000 toneladas. 

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/FAO_logo.svg/245px-FAO_logo.svg.png "FAO")

## Archivos del repo

**main.ipynb** : Para el trabajo de data cleaning y manipulation.
**pipeline.ipynb** : Pipeline en Jupyter Notebook
**main.py** : Pipeline
**FAO.csv** : CSV de producción de alimentos
**README.me** : Descripción del proyecto

## Datos complementarios para el dataset

Para completar el conjunto de datos del que disponemos, realizaremos llamadas a la siguiente api:

[https://restcountries.eu/](https://restcountries.eu/)

De la cual obetendremos el continente del area y su codificación para el csv de población.



## Anotaciones


