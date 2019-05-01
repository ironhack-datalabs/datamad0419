# O. importing all needed packages/libraries to work with on Spotify pipeline

# to work with data: dataframes, statistics & regular expressions
import pandas as pd
import numpy as np
import re

# to import and connect external data via API
import json
import requests
import argparse

# for data viz
%matplotlib inline
import matplotlib 
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Raw data

def importing_csv(csv_path):
    df = pd.read_csv(csv_path)
    return df

def raw(df):
    print('shape:',df.shape)
    print('\n columns:',df.shape)
    print('\n variables info:')    
    return df.info(),df.describe()

# 2. Preparing data: internal (Database) & external (APIs) - Data integration
'''API
API.ApiConfig.api_key = "hr5FPZc3e_DneGG_wsUf"
get/requests/blablabla
'''

# 3. Data cleaning & manipulation

def conversion_ms_to_min(x):
    return x/60000

def bins(var):
    bins_labels = ['Low','Mid','High']
    if cutoffs_table[var]['min'] != cutoffs_table[var]['25%']:
        cutoffs = [cutoffs_table[var]['min'],cutoffs_table[var]['25%'],cutoffs_table[var]['75%'],cutoffs_table[var]['max']]
    else:
        cutoffs = [cutoffs_table[var]['min'],cutoffs_table[var]['50%'],cutoffs_table[var]['75%'],cutoffs_table[var]['max']] 
    df[str(var)+'_labels']= pd.cut(df[var],cutoffs, labels=bins_labels)
    return df.head(5)

def tempo_classification(var):
    bins_labels = ['Larghissimo','Grave','Lento','Larghetto','Adagio','Andante','Moderato','Allegro','Vivace','Presto','Prestissimo']
    cutoffs = [0,20,40,60,66,76,108,120,140,168,200,400] 
    df['tempo_clas'] = pd.cut(df[var],cutoffs, labels=bins_labels)
    return df[['tempo','tempo_clas']].head()

def removing_duplicates(df, columns = []):
    before_removing = len(df)
    df = df.drop_duplicates(columns, keep='last')
    after_removing = len(df)
    removed = before_removing - after_removing
    print('# duplicated removed from df: {}'.format(removed))
    return df

# 3. DATA ANALYSIS

def valcount(data, var):
    return df[var].value_counts()

def topN(data,var,n):
    return df[var].value_counts().head(n)

def concat_pivot(data, rows, columns, values):
    df = pd.concat(data, sort=True)
    pivot = df.pivot_table(values=values, columns=columns, index=rows)
    return pivot

def histo(df, var):
    return df[var].hist()

def plotting(df,var):
    return df[var].boxplot()

def bars(df, var):
    sns.set_style(style='darkgrid')
    table=df[var].value_counts()
    table_plot=pd.DataFrame(table)
    plt.title(var+' ranking & distribution')
    return sns.barplot(table_plot[var], table_plot.index, palette="viridis")

def corr_matrix(df, days=30):
    corr_matrix = df.tail(days).corr()
    return corr_matrix

def barchart(df, x, y, length=8, width=14, title=""):
    df = df.sort_values(x, ascending=False)
    plt.figure(figsize=(width,length))
    chart = sns.barplot(data=df, x=x, y=y)
    plt.title(title + "\n", fontsize=16)
    return chart

def correlation_plot(corr, title=""):
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    plt.subplots(figsize=(15, 10))
    cmap = sns.diverging_palette(6, 255, as_cmap=True)
    
    chart = sns.heatmap(corr, mask=mask, cmap=cmap, center=0, linewidths=.5, annot=True, fmt='.2f')
    plt.title(title, fontsize=16)
    return chart

def save_viz(chart, title):
    fig = chart.get_figure()
    fig.savefig(title + '.png')



def wrangle(data):
    pivot = concat_pivot(data, 'Date', 'Ticker', 'Adj. Close')
    returns = compute_returns(pivot)
    return returns

def analyze(returns, days=30):
    ratios = return_risk_ratio(returns, days=days)
    top10 = ratios.sort_values('Ratio', ascending=False).head(10)
    
    target_list = returns[list(top10['Company'])]
    correlation = corr_matrix(target_list)
    return top10, correlation

def report(top10, correlation):
    bar_plot = barchart(top10, 'Ratio', 'Company', title='Stock Return vs. Risk Ratios - ' + str(day) + ' Days')
    save_viz(bar_plot, 'Return vs. Risk Top 10 - ' + str(day) + ' Days')
    
    corr_plot = correlation_plot(correlation, title='Stock Return Correlation - ' + str(day) + ' Days')
    save_viz(corr_plot, 'Correlation Plot - ' + str(day) + ' Days')

if __name__ == "__main__":
    data = acquire()
    returns = wrangle(data)

    num_days = [90,180,360]

    for day in num_days:
        top10, correlation = analyze(returns, days=day)
        report(top10, correlation)
