import pandas as pd
import numpy as np
import my_functions as mf
from matplotlib import pyplot as plt
import seaborn as sns
import json
import requests

def acquire(path):
    with open(path) as csvfile:
        df = pd.read_csv(path)
        return df

def request_api(url):
    response = requests.get(url)
    result_api = response.json()
    data_temp = pd.DataFrame(result_api)
    return data_temp

def wrangle(data):
    cols_names = data.columns.str.strip()\
                             .str.replace(' ', '_')    
    return df 

def analyze(data):
    quality_rank = data.groupby(['quality'])['quality']\
                       .count()\
                       .sort_index(ascending=False)\
                       .reset_index(name = 'num_by_qual')
    total = quality_rank['num_by_qual'].sum()
    quality_rank['pct_by_qual'] = quality_rank.apply(lambda row: row['num_by_qual'] * 100 / total , axis=1)
    quality_rank.to_csv('quality_rank.csv')
    
    bins = pd.cut(quality_rank['quality'], [0, 4, 7, 10])
    bins_qual_rank = quality_rank.groupby(bins, as_index=False)['num_by_qual']\
                                 .agg(['sum'])\
                                 .sort_index(ascending=False)
    bins_qual_rank.to_csv('bins_qual_rank.csv')
    
    pivot = data.pivot_table(data,index=['quality']).T
    pivot.to_csv('chemicals by quality.csv')

def graph(data):
    sns.set_style("white")
    xticks_range = range(0, len(df.columns))
    df.plot(title='Physicochemical variables by quality', xticks=xticks_range)
    plt.xticks(rotation=-45)
    plt.savefig('graph.png', transparent=True)    
    
def graph_api(data):
    years_list = []
    for r in range(len(data)):
        year = pd.Series(data['monthVals'].iloc[1])
    years_list.append(year)
    years = pd.concat(years_list, ignore_index=True)
    sns.set_style("white")  
    years.plot(title='Temperature evolution from 1980 to 1995 in Portugal')     
    plt.savefig('graph_temp.png', transparent=True)    

if __name__ == "__main__":

    filename = 'data/winequality-red.csv'
    df = acquire(filename)     

    wrangle(df)
    missing = mf.missing_pct(df)
    print('Table "missing.csv" to be shown')

    quality_rank = analyze(df)
    print('Table "quality_rank.csv" to be shown')
    print('Table "bins_qual_rank.csv" to be shown')      

    chart = graph(df)    
    print('Chart "chart.csv" to be shown')

    url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/PRT'
    data = request_api(url)
    graph_api(data)    
    print('Graph "graph_temp.png" to be shown') 

    