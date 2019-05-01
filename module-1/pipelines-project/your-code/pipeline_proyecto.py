from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def acquire(path):
    data = pd.read_csv(path)
    df=pd.DataFrame(data)
    return df

def wrangle(df):
    df.rename(columns = {' gdp_for_year ($) ':'gdp_for_year'},inplace=True)
    print(df.dtypes)
    df['gdp_for_year']=df['gdp_for_year'].str.replace(',','',regex=False)
    df['gdp_for_year']=df.gdp_for_year.astype(int)
    df.columns = df.columns.str.strip()
    df.drop(['population','suicides/100k pop','country-year', 'HDI for year','gdp_per_capita ($)', 'generation'], axis=1, inplace=True)
    df=df.query("country=='Spain' | country=='Germany' | country=='France' | country=='Italy' | country=='Belgium'| country=='Denmark'| country=='Croatia'| country=='Finland'| country=='Slovakia'| country=='Greece'| country=='Austria' | country=='Bulgary'| country=='Slovenia'| country=='Estonia' | country=='Hungary'| country=='Ireland' | country=='Poland'| country=='Portugal' | country=='Netherlands'| country=='Romania'| country=='Sweden'| country=='Czech Republic'")
    return df

def analyze(df, selected):
    df=df.groupby(['country','year', 'gdp_for_year'])['suicides_no'].sum().reset_index()
    df=df[['country','year','suicides_no','gdp_for_year']]
    df=df.loc[df.country==str(selected)]
    return df

def visualize(entrada):
    df=entrada.sort_values(by=['year', 'suicides_no'], inplace=False)
    grafica_1=df.plot(x='year', y=['suicides_no'])
    df=entrada.sort_values(by=['year', 'gdp_for_year'], inplace=False)
    grafica_2=df.plot(x='year', y=['gdp_for_year'])
    return grafica_1, grafica_2

def save_viz(grafica_1, grafica_2): # TENGO DOS GRAFICAS
    fig = grafica_1.get_figure()
    fig.savefig('n_suicidios' + '.png')
    fig = grafica_2.get_figure()
    fig.savefig('ev_pib' + '.png')

if __name__ == '__main__':
    selected= input('Hi, we are an app that deals with suicide data within the EU. Please, enter a Country of the UE and we will give you the correlation between number of suicides and the evolution of the gdp: ')
    filename = 'Suicidios.csv'

    data = acquire(filename)
    filtered = wrangle(data)
    results = analyze(filtered, selected)
    grafica_1, grafica_2 = visualize(results)
    save_viz(grafica_1, grafica_2)