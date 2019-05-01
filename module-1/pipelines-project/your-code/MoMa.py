from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re 

artist = 'artists.csv'
artworks = 'artworks.csv'

from main import *

if __name__=="__main__":

    artista = abrirdoc("artista",artist)
    obras = abrirdoc("obras",artworks)
    obras =rename(obras,"Artist ID",'Artist_ID')
    artista=rename(artista,"Artist ID",'Artist_ID')
    obras = limpiaArtisobras(obras)
    moma = merge("moma",artista,obras,'Artist_ID')
    print("-------------------------------------------------")
    print("Porcentaje de artistas según el genero")
    genero_autores(moma)
    print("-------------------------------------------------")
    print("Porcentaje de artistas quitando desconocido el genero")
    genero_autoressindesc(moma)
    print("\n")
    print("-------------------------------------------------")
    obrasartista(moma,"Male")
    print("\n")
    print("-------------------------------------------------")
    nacionalidadartista(moma,"Spanish")
    print("\n")
    print("-------------------------------------------------")
    gennacartista(moma,"Female","Spanish")
    print("\n")
    print("-------------------------------------------------")
    moma= limpiezadate(moma)
    moma['Acquisition Date']= moma["Acquisition Date"].apply(nuevaadquisicion)
    moma["Acquisition Date"] = moma["Acquisition Date"].astype(int)
    moma['Acquisition_Datenew']= categorizacion(moma)
    print("Proporción del género de los/as artistas antes de 1985")
    impactoguerrilla(moma,"preguerrilla")
    print("\n")
    print("-------------------------------------------------")
    print("Proporción del género de los/as artistas después de 1985")
    impactoguerrilla(moma,"postguerrilla")
    print("-------------------------------------------------")
