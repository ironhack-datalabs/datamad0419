La presente base de datos incluye información sobre las proteínas que se presentan en el cortex cerebral de ratones en la combinación de todas las posibles condiciones según:

-Condición del ratón. Trisómicos -t-(equivalencia a Síndrome de Down humano) frente a monosómicos/Control -c-(normales/sin mutación). 
-Contexto. Tarea de condicionamiento al miedo estimulante del aprendizaje -CS- frente a Control -SC- (ausencia de condicionamiento al miedo)
-Farmacología. Inyectados con memantina -m- frente a Control -s- (inyectados con solución salina). 

La combinación de estas condiciones se registra en la columna "class"

Mi pregunta de investigación es qué proteínas están asociadas a la función de aprendizaje.


En primer lugar elimino todos los valores extremos (outliers), puesto que en este caso un valor extremo suele indicar un error de medida. A continuación elimino todas las columnas en las cuales haya más de tres valores inexistentes en los registros. Estos valores inexistentes pueden deberse a un fallo en la recogida de datos o a la ausencia de la expresión de la proteína en dicho registro. Puesto que quiero centrarme en aquellas proteínas cuya expresión sea común, sólo me interesan las que aparzcan en un numero muy alto de registros. 

Tras la limpieza de los datos, analizo la diferencia de medias para los diferentes grupos mediante un ANOVA. Como la muestra es grande (1080), no compruebo si los datos se distribuyen de manera nomal o si existe homocedasticidad. Tras el ANOVA hago un análisis post-hoc (Tuckey) para todas las proteínas para comprobar en mayor profundidad las diferencias y conocer entre qué grupos se producen las diferencias. 

En cuanto a la representación de los datos, primero realizo un gráfico de barras para observar, de cada proteína, su presencia media en el cortex. Posteriormente realizo un diagrama de caja y bigotes para comparar la distribución de las proteínas en el cortex según grupos. 

Parece ser que S6_N se presenta en mayor medida por lo general en las condiciones de aprendizaje que las de no aprendizaje, y tras la presentación de la memantina que tras la de la solución salina, por lo que podría ser una proteína relacionada con el aprendizaje. El hecho de que se presente en mayor medida en ratones trísomicos podría ser indicativo de un mayor esfuerzo cognitivo en el momento del aprendizaje para este grupo. 
P3525_N se comporta de la misma manera en ratones monosómicos pero no en trisómicos; podría ser una proteína asociada al aprendizaje en población normal pero que no esta asociada a está función para la población con Síndrome de Down. 
Aunque los datos de GluR3_N y GluR3_N también van en esta misma dirección, las diferencias no parecen ser significativas. 



