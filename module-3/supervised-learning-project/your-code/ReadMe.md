# Entrenamiento modelos machine Learning.

En este proyecto hemos realizado todos los pasos, de principio a fin, necesarios para alimentar un modelo de **machine learning supervised**, elegir el clasificador con mayor porcentaje de acierto y optimizar sus predicciones modificando sus hiper parámetros mediante grid searching.

### El data set.
Los datos que he elegido para tratar han sido los del dataset de cáncer de mama de la universidad de Winsconsin. Lo he elegido, además de por ser interesante,por ser un data set relativamente pequeño para no cargar con muchos cálculos al procesador en la etapa de entrenamiento.

Los datos están bastante limpios y solo he tenido que tratar una columna que presentaba valores con "?". Cada linea en el data set representa una persona a la que se le han realizado diversos estudios. Aunque eran solo 16 los valores faltantes no he querido descartar la linea ya que se le han realizado todas las demás pruebas. Han sido sustituidos por la moda en dicha columna.

El valor que debemos predecir es el de la columna clase. Dicho valor es un 2 si el tumor es benigno o un 4 en caso de ser maligno.

El estudio de la correlación de las "features" nos da valores correctos, no existiendo una fuerte colinealidad entre las diferentes variables.

![Matriz de correlación](https://i.ibb.co/QQsjV7X/Captura-de-pantalla-de-2019-05-27-07-14-01.png)

Si bien vemos un 0.91 he decidido de dejarlo porque es solo un caso y muy cerca del limite establecido por convenio de 0.90.

### Modelos a entrenar

Los modelos clasificadores que he elegido han sido los siguientes:
```python
classifiers = [
    KNeighborsClassifier(),
    SVC(kernel="rbf", C=0.025, probability=True, gamma='scale'),
    NuSVC(probability=True, gamma='scale'),
    DecisionTreeClassifier(),
    RandomForestClassifier(n_estimators=100),
    AdaBoostClassifier(),
    GradientBoostingClassifier(),
    GaussianNB(),
    LinearDiscriminantAnalysis(),
    QuadraticDiscriminantAnalysis()]

```

Se ha realizado un bucle, en el cual, para cada uno de los clasificadores se entrena el modelo y se predice el "ground truth".
Genera dos gráficos con la matriz de confusión y la curva ROC. Además guardamos el valor de "accuracy" en otro Data Frame para tener los datos de cada modelo relacionados y de facil acceso.

![Matriz de confusión](http://i65.tinypic.com/10xylxz.png)

La matriz se ha generado con Seaborn como un mapa de calor.
Podemos apreciar la relación entre los valores reales y predecidos.
Los falsos y verdaderos positivos y negativos.

![ROC curve](http://i66.tinypic.com/zj786e.png)
La AUC ROC curve es una importante métrica de evaluación para medir el acierto de los modelos de clasificación multiclase.
Este no es el caso ya que tenemos una clase, en el fondo, binaria. Vale 2 o vale 4, positivo o negativo...

Aun así he decidido incluirlo por motivos didácticos.

Estos gráficos se guardan en nuestro disco en una carpeta output situada en el directorio donde se ejecute el jupyter notebook.

### Búsqueda de los mejores hiper parámetros mediante grid search.

He decidido realizarlo con el el método GridSearchCV de sklearn .

````python
param_grid={
    'n_neighbors':[3, 5, 10, 20, 40], 
    'algorithm':['auto', 'ball_tree', 'kd_tree', 'brute'], 
    'weights':['uniform', 'distance'],
    'p': [1,2],
    'leaf_size': [5,10,20,40]
    }
grid=GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, iid=True, return_train_score=True)
grid.fit(X_train, y_train)
print ('Test acierto: {:.2f}'.format(grid.score(X_test, y_test)))
print ('Mejores parametros: {}'.format(grid.best_params_))
print ('Mejor acierto cross-val: {:.2f}'.format(grid.best_score_))
print ('Mejor estimador: \n{}\n'.format(grid.best_estimator_))
````
Pasamos un diccionario con los hiper parámetros a testear y todo el trabajo "sucio" se realiza automáticamente. 
Además mientras se procesa podemos deleitarnos con el "bonito sonido" de los ventiladores poniendose al 100% para disipar el calor generado de tanto cálculo.