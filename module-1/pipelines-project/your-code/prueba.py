from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re 

def abrirdoc(nombre,csv):
    nombre = pd.read_csv(csv)
    return nombre

def genero_autores(moma,columna,valor1,valor2,valor3,valor4="none"):
    Unknown=(moma[(moma[columna]==valor1)][columna].value_counts()/len(moma[columna])*100)
    Unknown="% .2f" %Unknown[0]
    Male=(moma[(moma[columna]==valor2)][columna].value_counts()/len(moma[columna])*100)
    Male="% .2f"%Male[0]
    Female=(moma[(moma[columna]==valor3)][columna].value_counts()/len(moma[columna])*100)
    Female="% .2f"%Female[0]
    if valor4 is not "none":
        Unidentified =(moma[(moma[columna]==valor4)][columna].value_counts()/len(moma[columna])*100)
        Unidentified="% .2f" %Unidentified[0]
        porcentaje= {valor1:[Unknown],valor2:[Male],valor3:[Female],valor4:[Unidentified]}
        Total=pd.DataFrame(data=porcentaje).T
        Total2=Total.rename(columns={0:'%Gender_authors'})
        return print(Total2)
def genero_autoressindesc(moma,columna,valor1,valor2,valor3,valor4):
    GenderList = [x for x in moma[columna] if str(x) != valor1]
    z = pd.DataFrame(GenderList)
    Malez=(z[(z[0]==valor2)][0].value_counts()/len(z[0])*100)
    Malez="% .2f"%Malez[0]
    Femalez=(z[(z[0]==valor3)][0].value_counts()/len(z[0])*100)
    Femalez="% .2f"%Femalez[0]
    porcentajez= {valor2:[Malez],valor3:[Femalez]}
    Totalz=pd.DataFrame(data=porcentajez).T
    Total2z=Totalz.rename(columns={0:'%Gender_authors'})
    return print(Total2z)
'''def plot_val_counts(df,column='Name_x',figsize=(10,8),title=None):
    counts = df[column].value_counts()[:20]
    plt.figure(figsize=figsize)
    sns.barplot(counts.values,counts.index)
    plt.xlabel(column)
    plt.xlabel('Number of artworks')
    plt.xticks(rotation=0)
    plt.title(title)
    plt.show()
def obrasartista(Genero):
    obrasgenero= moma[moma['Gender'] == Genero]
    t = obrasgenero.Name_x.value_counts()
    return print (t)
def nacionalidadartista(nacionalidad):
    obrasgenero= moma[moma['Nationality'] == nacionalidad]
    d = (obrasgenero.Name_x.value_counts())
    return print(d)
def gennacartista(Genero,nacionalidad):
    obrasgenero= moma[(moma['Gender'] == Genero) & (moma['Nationality'] == nacionalidad)] 
    gennarcar = obrasgenero.Name_x.value_counts()
    return print(gennarcar)
def limpiezadate(moma):
    moma['Acquisition Date']= moma['Acquisition Date'].fillna("0")
    return moma
def nuevaadquisicion(Acquisition_Date):
    new_acquisition= re.sub("\-+\d*","",Acquisition_Date)
    return new_acquisition
def categorizacion():
    etiquetas= ['desconocido','preguerrilla','postguerrilla']
    cortes = [-1,1925,1985,2019]
    moma['Acquisition_Datenew'] = pd.cut(moma['Acquisition Date'],cortes, labels=etiquetas)
    return moma['Acquisition_Datenew']
def impactoguerrilla(periodo):
    generoperiodo= moma[moma['Acquisition_Datenew'] == periodo]
    tab=genero_autoressindesc(generoperiodo)
    return tab
artista = abrirdoc("artista",'artists.csv')
obras = abrirdoc("obras",'artworks.csv')

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

#plot_val_counts(moma,title='Top 20 artists with greatest number of artworks on display at MoMa')

obrasartista("Male")

print("\n")
print("-------------------------------------------------")

nacionalidadartista("Spanish")
print("\n")
print("-------------------------------------------------")

gennacartista("Male","Spanish")
print("\n")
print("-------------------------------------------------")

moma= limpiezadate(moma)

moma['Acquisition Date']= moma["Acquisition Date"].apply(nuevaadquisicion)
moma["Acquisition Date"] = moma["Acquisition Date"].astype(int)
moma['Acquisition_Datenew']= categorizacion()

print("Proporción del género de los/as artistas antes de 1985")
impactoguerrilla("preguerrilla")
print("\n")
print("-------------------------------------------------")
print("Proporción del género de los/as artistas después de 1985")
impactoguerrilla("postguerrilla")
print("-------------------------------------------------")
'''