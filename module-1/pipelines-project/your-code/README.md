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
**main.py** : Pipeline  
**config.py**: Configuración y contantes  
**limpia.py**: Funciones para limpiar los datos  
**analisis.py**: Funciones para el análisis de los datos  
**guardar.py**: Funciones para guardar csv y gráficas  
**report.py**: Funciones para crear los gráficos  
**callapi.py**: Funciones para llamar a la api  
**FAO.csv** : CSV de producción de alimentos  
**README.md** : Descripción del proyecto  


## Parámetros para el main.py

**--p1** Primer pais a comparar  
**--p2** Segundo pais a comparar  

## Datos complementarios para el dataset

Para completar el conjunto de datos del que disponemos, realizaremos llamadas a la siguiente api:  

[https://restcountries.eu/](https://restcountries.eu/)  

De la cual obetendremos el continente del area.  

## Anotaciones

Para las gráficas de comparación de países se toman los años desde el 2000 al 2010  
Para la gráfica de el top5 se utiliza todos los años disponibles en los datos

## Mejoras


