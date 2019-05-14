# MongoDB y geolocation

## Descripción

### Se busca la ubicación más adecuada para una empresa con las siguientes características:

La empresa se dedica a crear videojuegos, tiene 50 empleados de los cuales:

* 20 Desarrolladores
* 20 Diseñadores gráficos
* 10 Ejecutivos  

Se deben cumplir las siguientes condiciones:

* Ratio entre startus y grandes empresas.
* Evitar empresas muy antiguas.
* Que las empresas del entorno compartan intereses.

Para obtener la localización obtaremos por encontrar un buen ratio entre empresas grandes y startup, que haya al menos 10 empresas alrededor, que el precio de alquiler no sea muy elevado y que las empresas del entorno compartan intereses.

Se ha obtenido el costo del alquiler de un estudio, para tomarlo como referencia de que tan caro sería vivir en cada ciudad.  
Para ello se ha realizado un scraping de la siguiente web:  

[expatistan.com](https://www.expatistan.com/price/studio-rent-normal-area/london) 

## Archivos del repositorio referentes a mongDB

**main_companies.ipynb** : Donde se realiza toda la programación.  
**oficinas.json**: Datos después de realizar los filtros  
**oficinas_tableau.json** : Datos de la localización final  
**map-oficinas.html**: Mapa html con la localizaciones de las oficinas [abrir](http://gmd.ovh/temp/map-oficinas.html)  
**map-final.html**: Mapa html con la localización final [abrir](http://gmd.ovh/temp/map-final.html)  
**README.md** : Descripción del proyecto  

## Anotaciones
Se podría limpiar los datos en lo referente a las ciudades, ya que aparecen barrios y otras localizaciones
y así poder utilizar [numbeo.com/london](https://www.numbeo.com/cost-of-living/in/London) para obtener el costo de la vida
en esas ciudades.

## Mejoras
Se puede implementar el código en archivos .py y así poder utilizarlos desde consola
para generar los mapas con ciertos parámetros

## Otras cuestiones
Al realizar el scraping de expatistan, hay que adaptar algunos nombres de ciudades, para ello se ha creado la columna **city_search**
Numbeo tiene api, pero esta es de pago, por lo que también se ha otado por realizar escraping, aunque no se ha llegado a utilizar en el
proyecto, por el tema del nombre de las ciudades.
