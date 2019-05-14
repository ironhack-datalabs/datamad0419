# Geolocalización con MongoDB

Mi criterio en la query realizada a MongoDB ha sido el siguiente:
* Que deadpooled year sea nulo. Lo que considerado año de quiebra.
* Año de fundación superior a 2003. Queremos estar rodeados de empresas que a priori tengan ideas novedosas.
* Que el array de oficinas no esté vacío.
* Que se dediquen al mundo del videojuego o software exclusivamente.
* Consideramos Startup a las empresas creadas a partir de 2007 (el dataset va hasta 2013) y con menos de 50 empleados.

La limpieza de datos y construcción se ha realizado en **dos diferentes jupyter notebook.**
Primero se hizo "mongo-geo-lambdas" en el cual conseguí los datos deseados mediante apply y lambdas.
Posteriormente se hizo con la función normalize ya que simplificaba el proceso y me permitía obtener todas las oficinas de las empresas se una  mejor manera.

Es estudio final se lanza desde **mainGeo.py**. Pide los parámetros de puntuación.
El ficheros mainQT.py ha sido para practicar interfaces graficas pero he teneido problemas de scope y he decidido no incluirlo al final por falta de tiempo.

Se han eliminado todas las oficinas que presentaban NaN en latitud o longitud y las empresas que no especificaban número de empleados.

Tras este punto obtenemos el Data set de las empresas seleccionadas.

Con la nueva base de datos, que incluye el punto geo espacial en MongoDB se realiza una **consulta oficina por oficina** de las empresas en un radio de 3 km.

Considero que el sector del desarrollo de videojuegos es muy precario y la gente se mueve mucho de proyecto en proyecto cambiando de empresa. Queremos un radio pequeñito para poder fichar o recolocar gente.

El sistema de puntuaje de empresa valora con diferentes puntuaciones si la empresa se dedica al desarrollo de videojuegos o de software en general.
Si es una "Big company" o una Startup. Además nos gustaría evitar USA por lo que se establece una penalización para este país.

Con los calculos realizados para cada oficina obtenemos la oficina mejor valorada y su ubicación en el mapa. Construiremos lo más cerca posible.