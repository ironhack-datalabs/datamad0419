import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

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
    return df_selected

def create_bins(df):
  score_labels=['Avoid','For fans','Meh','Recommendable', 'Essential']
  cutoffs = [0,60,72,80,89.5,100]
  bins = pd.cut(df_selected['total_score'],cutoffs, labels=score_labels)
  df_selected['category']=bins
  return df_selected




if __name__ == '__main__':
  df = acquire()
  df_selected= wrangle(df)
  df_selected= create_bins(df_selected)
  
  print(categories = df_selected['category'].value_counts().sort_index())
  #cat_plot= categories.plot.bar()


    