#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd
import numpy as np
import json
import requests
import scipy.stats as stats
import matplotlib
import researchpy as rp
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:

def get_wiki_info(theme):
    response = requests.get('https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles='+str(theme))
    results = response.json()
    return results

def rm_outliers(data,column): 
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3-q1
    low  = q1-1.5*iqr
    high = q3+1.5*iqr
    res = []
    for e in data[column]:
        if type(e)==float and (e < low or e > high):
            res.append(np.nan)
        else: 
            res.append(e)
    return res

def separate_measure_subject(data):
    data['Measurement']=list(i.split('_')[1] for i in data['MouseID'])
    data['Subject']=list(i.split('_')[0] for i in data['MouseID'])

def drop_null_cols(data):
    null_cols = data.isnull().sum()
    drop_cols = list(null_cols[null_cols > 3].index)
    data2=data.drop(drop_cols, axis=1)
    return data2

def Anova(data2):  
    proteins=list(data2._get_numeric_data().columns)
    result = []
    for protein in proteins:
        o= protein
        x = (rp.summary_cont(data2.groupby('class'))[protein])
        y = (stats.f_oneway(data2[protein][data2['class'] == 'c-CS-m'], 
               data2[protein][data2['class'] == 'c-CS-s'],
               data2[protein][data2['class'] == 'c-SC-m'], 
               data2[protein][data2['class'] == 'c-SC-s'],
               data2[protein][data2['class'] == 't-CS-m'],
               data2[protein][data2['class'] == 't-CS-s'],
               data2[protein][data2['class'] == 't-SC-m'],
               data2[protein][data2['class'] == 't-SC-s'])) 
        result.append((o,x, y))
    return result
    

def Tuckey(data2):
    proteins=list(data2._get_numeric_data().columns) 
    result = []
    for protein in proteins:
        mc = MultiComparison(data2[protein], data2['class'])
        mc_results = mc.tukeyhsd()
        result.append(mc_results)
    return result

def binn(data2):
    proteins=list(data2._get_numeric_data().columns)
    data3=data2.copy()
    for protein in proteins:
        mpg_labels = ['Very Low', 'Low', 'Moderate', 'High', 'Very High']
        data3[protein] = pd.cut(data3[protein],5, labels=mpg_labels)
    return data3
    
def distribution_plot(data2,data3):
    data3=binn(data2)
    proteins=list(data2._get_numeric_data().columns)
    for protein in proteins:
        v=data3[protein].value_counts(sort=False)
        v.plot('bar')
        plt.title(protein + ' distribution')
        plt.savefig(protein + ' distribution.png')
        plt.show()
        
def box_plot (data2):
    proteins=list(data2._get_numeric_data().columns)
    proteins.append('class')
    data2[proteins].groupby(['class']).mean()
    for protein in proteins[0:9]:
        p=data2[[protein, 'class']]
        bpx_plot=sns.boxplot(x='class', y=protein,  data=p)
        plt.title(protein + ': box plot by group') 
        plt.savefig(protein + ': box plot by group')
        plt.show()

def acquire ():
    data=pd.read_csv('./Data_Cortex_Nuclear.csv')
    results_m=get_wiki_info('Memantine')['query']['pages']['1289426']['extract']
    results_s=get_wiki_info('Saline water')['query']['pages']['2101553']['extract']
    data['Treatment information']=np.where(data['Treatment']=='Saline',results_s,results_m)
    return data

def wrangle (data):
    for column in data._get_numeric_data():
        data[column]=rm_outliers(data,column)
    separate_measure_subject(data)
    data2=drop_null_cols(data)
    return data2

def analyze(data):
    data2=wrangle(data)
    a=Anova(data2)
    x=Tuckey(data2)
    print(a)
    for z in x: 
        print(z.summary())

def visualize(data2):
    proteins=(list(data2._get_numeric_data().columns)).append('class')
    data3=binn(data2)
    distribution_plot(data2,data3)
    box_plot (data2)

def save(data2):
    data3=binn(data2)
    data2.to_csv('Cortex_cuantitative.csv')
    data3.to_csv('Cortex_cualitative.csv')




