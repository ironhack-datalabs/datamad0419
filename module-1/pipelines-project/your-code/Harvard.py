from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re 

data = 'apiharvardartmuseums.csv'

from prueba import *

if __name__=="__main__":

    harvard = abrirdoc("harvard",data)
    print("-------------------------------------------------")
    print("Porcentaje de artistas según el genero")
    tabla = genero_autores(harvard,"gender","unknown","male","female","unidentified")
    print("-------------------------------------------------")
    print("Porcentaje de artistas quitando desconocido el genero")
    tabla2 = genero_autoressindesc(harvard,"gender","unknown","male","female","unidentified")