import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from igdbApi import igdbApi

filePath= 'data/metacritic_games.csv'
outPath= 'output/'

def acquire():
  df = pd.read_csv(filePath)
  return df

def wrangle(df):
  df_selected = df[['game','platform','developer', 'metascore','user_score']]
  
  df_dev_null=df_selected[df_selected['developer'].isnull()==True]
  df_selected = df_selected.drop(df_dev_null.index)

  df_selected['total_score']=(df_selected['metascore']+df_selected['user_score'])/2
  df_selected['dif_score']= df_selected['metascore']-df_selected['user_score']
  return df_selected

def create_bins(df):
  score_labels=['Avoid','For fans','Meh','Recommendable', 'Essential']
  cutoffs = [0,60,72,80,89.5,100]
  bins = pd.cut(df['total_score'],cutoffs, labels=score_labels)
  df['category']=bins
  return df

def analyze_serie(df, name):
  serie = df[name].value_counts().sort_index()
  return serie

def visualize(name, df= None, ser= None):
  print('\n-------------{}-------------'.format(name))
  if df is not None: print(df.to_string())
  elif ser is not None: print(ser.to_string())

def save_plots(name, df= None, ser= None):
  if df is not None: plot= df.plot.bar()
  elif ser is not None: plot= ser.plot.bar()
  
  fig= plot.get_figure()
  fig.savefig(outPath+name)

if __name__ == '__main__':
  try:
    df = acquire()
  except:
    print('Error en la lectura del fichero .csv')
  else:
    print('Capturando datos de Metacritic.')
    
  df_selected= wrangle(df)
  df_selected= create_bins(df_selected)

  # Titulos imprescindibles y por por plataforma.
  df_essentials= df_selected[df_selected['category']=='Essential']
  visualize('Titulos imprescindibles', df_essentials)

  essential_serie= analyze_serie(df_essentials, 'platform')
  visualize('Esenciales plataforma', ser=essential_serie)
  save_plots('Esenciales_plataforma.png', ser=essential_serie)
  
  # Estudio de categorías de puntuación.
  categories_serie= analyze_serie(df_selected, 'category')
  visualize('Categorias de puntuación', ser=categories_serie)
  save_plots('Categorias_de_puntuación.png', ser=categories_serie)

  #analizar puntuaciones.
  df_media= df_selected[df_selected['dif_score']<-28.5]
  visualize('Mayores diferencias prensa', df_media)

  df_users= df_selected[df_selected['dif_score']>52.5].sort_values('dif_score', ascending=False)
  visualize('Mayores diferencias usuarios', df_users)

  #Top ten populares
  top10hyped_df= igdbApi()
  visualize('Juegos más populares hoy', top10hyped_df)



    