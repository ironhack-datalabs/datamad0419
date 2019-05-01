from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re 

def abrirdoc(nombre,csv):
    nombre = pd.read_csv(csv)
    return nombre

def rename(df,col1,coln):
    df=df.rename(columns={col1:coln})
    return df
def limpiaArtisobras(obras):
    obras['Artist_ID'] = obras['Artist_ID'].fillna(0)
    lista=[]
    for a in obras['Artist_ID']:
        if len(list(str(a).split(','))) >= 2:
            lista.append(0)
        else:
            lista.append(a)
    obras=obras.assign(Artist_ID=lista)
    obras['Artist_ID'] = obras["Artist_ID"].astype(int)
    return obras
def merge(nombre,primerdf,segundodf,columna):
    nombre = pd.merge(primerdf, segundodf, on=columna,how='inner')
    return nombre
def genero_autores(moma):
    moma['Gender'] = moma['Gender'].str.replace('male', 'Male')
    moma['Gender'] = moma['Gender'].str.replace('FeMale', 'Female')
    moma['Gender'] = moma['Gender'].fillna('Unknown')
    Unknown=(moma[(moma["Gender"]=="Unknown")]["Gender"].value_counts()/len(moma["Gender"])*100)
    Unknown="% .2f" %Unknown[0]
    Male=(moma[(moma["Gender"]=="Male")]["Gender"].value_counts()/len(moma["Gender"])*100)
    Male="% .2f"%Male[0]
    Female=(moma[(moma["Gender"]=="Female")]["Gender"].value_counts()/len(moma["Gender"])*100)
    Female="% .2f"%Female[0]
    porcentaje= {"Unknown":[Unknown],"Male":[Male],"Female":[Female]}
    Total=pd.DataFrame(data=porcentaje).T
    Total2=Total.rename(columns={0:'%Gender_authors'})
    return print(Total2)
def genero_autoressindesc(moma):
    GenderList = [x for x in moma["Gender"] if str(x) != 'Unknown']
    z = pd.DataFrame(GenderList)
    Malez=(z[(z[0]=="Male")][0].value_counts()/len(z[0])*100)
    Malez="% .2f"%Malez[0]
    Femalez=(z[(z[0]=="Female")][0].value_counts()/len(z[0])*100)
    Femalez="% .2f"%Femalez[0]
    porcentajez= {"Male":[Malez],"Female":[Femalez]}
    Totalz=pd.DataFrame(data=porcentajez).T
    Total2z=Totalz.rename(columns={0:'%Gender_authors'})
    return print(Total2z)
"""def plot_val_counts(df,column='Name_x',figsize=(10,8),title=None):
    counts = df[column].value_counts()[:20]
    plt.figure(figsize=figsize)
    sns.barplot(counts.values,counts.index)
    plt.xlabel(column)
    plt.xlabel('Number of artworks')
    plt.xticks(rotation=0)
    plt.title(title)
    plt.show()"""
def obrasartista(moma,Genero):
    obrasgenero= moma[moma['Gender'] == Genero]
    t = obrasgenero.Name_x.value_counts()
    return print (t)
def nacionalidadartista(moma,nacionalidad):
    obrasgenero= moma[moma['Nationality'] == nacionalidad]
    d = (obrasgenero.Name_x.value_counts())
    return print(d)
def gennacartista(moma,Genero,nacionalidad):
    obrasgenero= moma[(moma['Gender'] == Genero) & (moma['Nationality'] == nacionalidad)] 
    gennarcar = obrasgenero.Name_x.value_counts()
    return print(gennarcar)
def limpiezadate(moma):
    moma['Acquisition Date']= moma['Acquisition Date'].fillna("0")
    return moma
def nuevaadquisicion(Acquisition_Date):
    new_acquisition= re.sub("\-+\d*","",Acquisition_Date)
    return new_acquisition
def categorizacion(moma):
    etiquetas= ['desconocido','preguerrilla','postguerrilla']
    cortes = [-1,1925,1985,2019]
    moma['Acquisition_Datenew'] = pd.cut(moma['Acquisition Date'],cortes, labels=etiquetas)
    return moma['Acquisition_Datenew']
def impactoguerrilla(moma,periodo):
    generoperiodo= moma[moma['Acquisition_Datenew'] == periodo]
    tab=genero_autoressindesc(generoperiodo)
    return tab
