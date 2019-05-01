import pandas as pd
import numpy as np
from functools import reduce
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
import requests

# Función para agrupar los csv.
def agrupar():
    files = ['Data/content.csv', 'Data/genres.csv', 'Data/labels.csv', 'Data/reviews.csv', 'Data/years.csv']
    return files 


# Función para importar los archivos csv.
def df_frames(files):
    dframes = []
    for file in files:
        dframes.append(pd.read_csv(file))
    return dframes


# Función para crear dataframe y limpiarlo.
def cleaning(df):
    df = reduce(lambda x,y: pd.merge(x,y, on='reviewid', how='outer'), [df_frames(files)[0], df_frames(files)[1], df_frames(files)[2], df_frames(files)[3], df_frames(files)[4]])
    null_cols = df.isnull().sum()
    drop_cols = list(null_cols[null_cols > 5000].index)
    data = df.drop(drop_cols, axis=1)
    select_columns = ['content', 'label', 'url', 'best_new_music', 'author', 'pub_date', 'pub_weekday', 'pub_day', 'pub_month', 'pub_year']
    dframe = data.drop(select_columns, axis=1)
    select_columns = ['reviewid', 'genre', 'title', 'artist', 'score', 'year']
    dframe = dframe[select_columns].drop_duplicates()
    dframe = dframe.rename(columns={'title':'album'})
    column_order = ['reviewid', 'artist', 'album', 'year', 'genre', 'score']
    dframe = dframe[column_order]
    dframe['year'] = dframe['year'].fillna(0)
    dframe['year'] = dframe['year'].astype('int64')
    dframe = dframe[dframe.year != 0]
    dframe['genre'] = dframe['genre'].fillna(0)
    dframe = dframe[dframe.genre != 0]
    dframe['album'] = dframe['album'].fillna(0)
    dframe = dframe[dframe.album != 0]
    return dframe


# Función para eliminar duplicados de álbumes.
def sort_dupl(dframe):
    sel_col = ['reviewid', 'artist', 'album']
    df_dupl = dframe.drop_duplicates(sel_col, keep='first')
    df_final = df_dupl.sort_values('score', ascending=False)
    return df_final


# Función para los bins de score.
def create_bins(df_final):
    score = df_final['score']
    bins = (0, 3, 5, 6, 8, 9, 10)
    labels = ('Pésimo', 'Flojo', 'Para fans', 'Recomendado', 'Muy bueno', 'Obra maestra')
    groups = pd.cut(score, bins=bins, labels=labels)
    scores = groups.value_counts(sort=False)
    print(scores)
    return df_final


# Función para dejar los elementos con nota 10 en el dataset.
def filter_score(df_final): 
    dfx = df_final
    dfx = dfx[dfx['score'] == 10.0]
    return dfx


# Funciones para la API.
def apireq(artist, album):
    key = open(".env").read()
    url = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo'
    response = requests.get(url+"&api_key={}&artist={}&album={}&format=json".format(key, artist, album))
    res = response.json()
    return res

def apiloop():
    artist = list(pitch['artist'])
    album = list(pitch['album'])
    listeners = []
    for i in range(len(album)):
        answer = apireq(artist[i], album[i])
        try:
            listeners.append(answer['album']['listeners'])
            #print(answer['album']['listeners'])
        except:
            listeners.append('no data')
            #print(answer, 'Este artista no tiene el álbum en last.fm')
    dictionary = {'album': album, 'listeners_lastfm': listeners}
    answer = pd.DataFrame(dictionary)
    return answer

def apimerge(pitch, answer):
    final = pd.merge(pitch, answer, on='album')
    final = final[final.listeners_lastfm != 'no data']
    final['listeners_lastfm'] = final['listeners_lastfm'].astype('int64')
    final['listeners_lastfm'].dtype
    final = final.sort_values(by='listeners_lastfm', ascending=False)
    return final


# Función para guardar csv.
def savecsv (final):
    final.to_csv('pipelines_pitchfork.csv')


# Funciones para los gráficos.
def plt_score(df_final):
    score = df_final['score']
    bins = (0, 3, 5, 6, 8, 9, 10)
    labels = ('Pésimo', 'Flojo', 'Para fans', 'Recomendado', 'Muy bueno', 'Obra maestra')
    groups = pd.cut(score, bins=bins, labels=labels)
    scores = groups.value_counts(sort=False)
    colors = ('#28C3A6', '#2893C3', '#2845C3', '#5828C3', '#A628C3', '#C32893')
    ax = scores.plot.bar(rot=0, color=colors, figsize=(16,10))
    plt.title("Ranking score by reviewers", fontsize=16)
    plt.ylabel('No. Albums', fontsize=14)
    plt.xlabel('Scores', fontsize=14)
    plt.savefig('rankingscore.png')
    return plt.show()

def plt_genre(pitch):
    loved_genres = pitch.genre.value_counts()
    colors = ('#DAF7A6', '#FFE99F', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845')
    ax = loved_genres.plot.bar(rot=0, color=colors, figsize=(16,10))
    plt.title("Genres preferred by Pitchfork Reviewers", fontsize=16)
    plt.ylabel('No. Votes Scored: #10', fontsize=14)
    plt.xlabel('Genres', fontsize=14)
    plt.savefig('genrespreferred')
    return plt.show()
