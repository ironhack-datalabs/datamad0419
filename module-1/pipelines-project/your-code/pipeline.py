# pipeline.py



import pandas as pd       # se importan librerias



'''
def full(df):                            # funcion para mostrar el dataframe completo
    pd.set_option('display.max_rows', len(df))
    print(df)
    pd.reset_option('display.max_rows')
'''



def read(csv):           # funcion de lectura del dataframe
	df=pd.read_csv(csv)
	return df





def clean_flares(df):     # limpieza de llamaradas
	df=df[['Sol', 'JJJ Start', 'JJJ Peak', 'JJJ End', 'JJJ Class']]  # seleccion de columnas
	
	df=df.rename(columns={'Sol': 'Date', 'JJJ Start': 'Start', 'JJJ Peak': 'Peak',\
	                     'JJJ End': 'End', 'JJJ Class': 'Class'})    # renombra columnas
	
	return df                    





























