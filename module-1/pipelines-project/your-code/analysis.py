import pandas as pd
import os
import requests
import quandl
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
from collections import Counter


def read(DataFrame):
    imdb = pd.read_csv(DataFrame)
    return imdb

def set_up(imdb):
    colnames = ['movie_title', 'country', 'title_year', 'duration', 'genres',
                'budget', 'gross', 'director_name' ,'imdb_score' , 'num_voted_users']
    imdb = pd.DataFrame(imdb, columns=colnames)
    return imdb

def data_cleaning(imdb):
    imdb = imdb.sort_values(by='imdb_score', ascending=False)
    imdb = imdb.drop_duplicates(subset=['movie_title', 'title_year']).dropna()
    imdb['duration'] = imdb['duration'].astype(int)
    imdb['title_year'] = imdb['title_year'].astype(int)
    imdb['budget'] = imdb['budget'].round(1)
    imdb['gross'] = imdb['gross'].round(1)
    imdb['num_voted_users'] = imdb['num_voted_users'].round(1)
    imdb = imdb.drop(imdb[imdb['num_voted_users']<5000].index)
    imdb = imdb.drop(imdb[imdb['budget']<100000].index)
    imdb = imdb.drop(imdb[imdb['gross']<100000].index)
    imdb = imdb.drop(imdb[imdb['country']!='USA'].index)
    return imdb

def data_wrangling(imdb):
    imdb['Budget (US$ Mn)'] = (imdb['budget']/(10**6))
    imdb['Gross Revenue (US$ Mn)'] = (imdb['gross']/(10**6))
    imdb['Total votes (k)'] = (imdb['num_voted_users']/(10**3))
    imdb.drop(['gross', 'budget', 'num_voted_users'], axis='columns', inplace=True)
    imdb['Gross Profit (x)'] = (imdb['Gross Revenue (US$ Mn)']/imdb['Budget (US$ Mn)'])
    imdb['Gross Profit (x)'] = imdb['Gross Profit (x)'].round(2)
    return imdb

def data_binning(imdb):
    bins=[0, 90, 120, 150, 500]
    group_names=['Less than 90 min', 'Between 90 and 120 min', 
             'Between 120 and 150 min', 'More than 150 min']
    imdb['Duration range']=pd.cut(imdb['duration'], bins, labels=group_names)
    imdb = imdb.drop(columns=['duration'])
    return imdb

def data_embellish(imdb):
    column_order = ['movie_title', 'title_year', 'country', 'genres', 'Duration range',
                    'director_name', 'imdb_score', 'Total votes (k)', 'Budget (US$ Mn)',
                   'Gross Revenue (US$ Mn)', 'Gross Profit (x)']
    imdb = imdb[column_order]
    imdb.rename(columns={'movie_title':'Title'}, inplace=True)
    imdb.rename(columns={'title_year':'Year'}, inplace=True)
    imdb.rename(columns={'country':'Country'}, inplace=True)
    imdb.rename(columns={'genres':'Genre'}, inplace=True)
    imdb.rename(columns={'director_name':'Director'}, inplace=True)
    imdb.rename(columns={'imdb_score':'Score'}, inplace=True)
    return imdb

def API_input(token):
    CPI_index = quandl.get("RATEINF/CPI_USA", authtoken=token)
    CPI_index.head()
    CPI_index = CPI_index.resample('Y').mean()
    CPI_index['Date YYYY'] = CPI_index.index
    CPI_index = CPI_index.reset_index()
    CPI_index['Year Date'] = CPI_index['Date YYYY'].map(lambda x: x.year)
    colnames=['Year Date', 'Value']
    CPI_index = pd.DataFrame(CPI_index, columns=colnames)
    CPI_index['Value'] = CPI_index['Value']/CPI_index['Value'][106]
    return CPI_index

def merge(imdb, CPI_index):
    imdb = imdb.merge(CPI_index, left_on='Year', right_on='Year Date')
    imdb['Budget (US$ Mn)'] = imdb['Budget (US$ Mn)']/imdb['Value']
    imdb['Gross Profit (x)'] = imdb['Gross Profit (x)']/imdb['Value']
    imdb['Budget (US$ Mn)'] = imdb['Budget (US$ Mn)'].round(2)
    imdb['Gross Profit (x)'] = imdb['Gross Profit (x)'].round(2)
    imdb['Gross Revenue (US$ Mn)'] = imdb['Gross Revenue (US$ Mn)'].round(2)
    imdb['Total votes (k)'] = imdb['Total votes (k)'].round(1)
    imdb['Gross Profit (x)'] = (imdb['Gross Revenue (US$ Mn)']/imdb['Budget (US$ Mn)'])
    imdb['Gross Profit (x)'] = imdb['Gross Profit (x)'].round(2)
    imdb = imdb.drop(columns=['Value'])
    imdb = imdb.drop(columns=['Year Date'])
    imdb = imdb.sort_values(by='Score', ascending=False)
    return imdb

def toCSV(imdb):
    imdb.to_csv('Dataset procesado.csv')

def plot_genre(imdb):
    category_data= imdb.Genre.str.split('|', expand=True).stack().value_counts(0)/len(imdb)*100
    category_data = category_data.round(1)
    category_data.head(5).plot('bar') 
    plt.title("Total movies by genre in %")
    plt.savefig('Plot by genres')
    plt.show()

def plot_bins(imdb):
    v = imdb['Duration range'].value_counts()
    v.plot('bar')
    plt.title("Movie duration bins")
    plt.savefig('Plot by movies duration')
    plt.show()

def plot_yearVSmovies(imdb):
    imdb2=imdb.drop(imdb[imdb['Year']<1970].index)
    imdb2=imdb2.drop(imdb[imdb['Year']>2015].index)
    imdb2.groupby('Year').count()['Title'].plot(xticks = np.arange(1970,2016,5))

    sns.set(rc={'figure.figsize':(10,5)})
    plt.title("Year Vs Number of Movies",fontsize = 14)
    plt.xlabel('Release year',fontsize = 13)
    plt.ylabel('Number of Movies',fontsize = 13)
    plt.ylim(0,140)

    sns.set_style("whitegrid")
    plt.savefig('Relation movies by year')
    plt.show()

def plot_yearVSvotes(imdb):
    imdb.groupby('Year').mean()['Total votes (k)'].plot(xticks = np.arange(1940,2016,5))

    sns.set(rc={'figure.figsize':(10,5)})
    plt.title("Year Vs Average # of votes",fontsize = 14)
    plt.xlabel('Release year',fontsize = 13)
    plt.ylabel('# of votes',fontsize = 13)

    sns.set_style("whitegrid")
    plt.savefig('Relation years and mean votes')
    plt.show()

def plot_top10budget(imdb):
    info = pd.DataFrame(imdb['Budget (US$ Mn)'].sort_values(ascending = False))
    info['Title'] = imdb['Title']
    data = list(map(str,(info['Title'])))

    x = list(data[:10])
    y = list(info['Budget (US$ Mn)'][:10])

    ax = sns.pointplot(x=y,y=x)
    sns.set(rc={'figure.figsize':(10,5)})
    ax.set_title("Top 10 High Budget Movies",fontsize = 15)
    ax.set_xlabel("Budget (US$ Mn)",fontsize = 13)
    sns.set_style("whitegrid")
    plt.savefig('Top 10 movies by budget')
    plt.show()

def plot_worsttop10(imdb):
    info = pd.DataFrame(imdb['Score'].sort_values(ascending = True))
    info['Title'] = imdb['Title']
    data = list(map(str,(info['Title'])))

    x = list(data[:10])
    y = list(info['Score'][:10])

    ax = sns.pointplot(x=y,y=x)
    sns.set(rc={'figure.figsize':(10,5)})
    ax.set_title("Top 10 less voted movies",fontsize = 15)
    ax.set_xlabel("Score",fontsize = 13)
    sns.set_style("whitegrid")
    plt.savefig('Top 10 less voted movies.png')
    plt.show()

def plot_corr_coreVSbudget(imdb):
    ax = sns.regplot(x=imdb['Score'], y=imdb['Budget (US$ Mn)'],color='c')

    ax.set_title("Score Vs Budget correlation",fontsize=13)
    ax.set_xlabel("Score",fontsize=12)
    ax.set_ylabel("Budget",fontsize=12)

    sns.set(rc={'figure.figsize':(6,4)})
    sns.set_style("whitegrid")

    imdb['Budget (US$ Mn)'] =imdb['Budget (US$ Mn)'].replace(0,np.NAN)
    imdb['Score'] =imdb['Score'].replace(0,np.NAN)

    data_corr = imdb.corr()
    print("Correlation Between Score And Budget : ",data_corr.loc['Score','Budget (US$ Mn)'])
    plt.savefig('Correlation between budget and score.png')
    plt.show()

def categorizer(imdb):
    print("Selecciona una categoría para ordenar los directores. \n Categorías: Score, Title, Budget (US$ Mn), Gross Profit (x)")
    categoria = input()

    imdb_directors = imdb.groupby('Director', as_index=False).agg({"Score": "mean", 'Title':'count', 'Budget (US$ Mn)':'mean', 'Gross Profit (x)':'mean'})
    imdb_directors = imdb_directors.drop(imdb_directors[imdb_directors['Title']<5].index)
    imdb_directors = imdb_directors.sort_values(by='{}'.format(categoria), ascending=False)
    imdb_directors = imdb_directors.round(1)
    output1 = imdb_directors.head(10)
    return print(output1)

def director(imdb):
    print("Selecciona una director para conocer su filmografía.")
    director = input()
    output2 = imdb.loc[imdb['Director']=='{}'.format(director),['Score', 'Title', 'Budget (US$ Mn)', 'Gross Profit (x)']]
    return print(output2)
    