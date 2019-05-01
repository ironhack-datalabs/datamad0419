{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "El dataset empleado es: www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009\n",
    "Durante el trabajo se ha procurado utilizar algunas de las herramientas aprendidas recientemente.\n",
    "Los pasos seguidos en la realización de la 'pipeline' han sido:\n",
    "    - Importación de los módulos necesarios;\n",
    "    - Descarga del archivo csv de la página de Kaggel, que contiene el dataset elegido;\n",
    "    - Lectura del mismo para, a partir de este momento, utilizar los datos en el formato dataframe de pandas;\n",
    "    - Limpieza de datos:\n",
    "        * modificación de  los nombres de las columnas y\n",
    "        * comprobación, mediante la importación de una función propia, de que el porcentaje de \n",
    "          'missing values' es cero y no requiere ninguna actuación;\n",
    "    - Análisis de datos:\n",
    "        * cálculo del porcentaje de vinos por calidades, con empleo función lambda;\n",
    "        * cálculo del número de vinos en base a su clasificación en calidad alta (ranking 7 a 10), media (4 a 7) o baja \n",
    "          (0 a 4), mediante bins;\n",
    "        * creación de un dataframe que permita una correcta comprensión de los datos, pivotando la tabla con posterior \n",
    "          transposición.\n",
    "            \n",
    "    - Resultado:\n",
    "        La conclusión del estudio se fundamenta en la gráfica con indicación de todos los componentes químicos según \n",
    "        calidades.\n",
    "        En la misma se aprecia que sólo hay tres características químicas que varían con la calidad: el alcohol,el \n",
    "        dióxido de sulfuro libre y el dióxido de sulfuro total. \n",
    "        La calidad vendrá expresada por la mayor cantidad de alcohol y la menor de dióxido de sulfuro libre y de\n",
    "        dióxido de sulfuro total.\n",
    "    \n",
    "        \n",
    "          "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
