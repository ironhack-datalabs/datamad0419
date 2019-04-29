# pipeline.py


# se importan librerias
import pandas as pd       # dataframe 
import datetime           # para manejo temporal
import quandl             # api quandl
import numpy as np        # numerical python
from draw import *        # importacion para plots



def full(df):             # funcion para mostrar el dataframe completo
    pd.set_option('display.max_rows', len(df))
    print(df)
    pd.reset_option('display.max_rows')
    return '\nDone'




def read(csv):           # funcion de lectura del dataframe
	df=pd.read_csv(csv)
	return df






def token(token):          # lectura del token desde .txt
	with open(token, 'r') as f:
		t=f.readlines()[0].split('\n')[0]
	return t






def clean_flares(df):     # seleccion del dataframe de llamaradas
	df=df[['Sol', 'JJJ Start', 'JJJ Peak', 'JJJ End', 'JJJ Class']]  # seleccion de columnas
	
	df=df.rename(columns={'Sol': 'Date', 'JJJ Start': 'Start', 'JJJ Peak': 'Peak',\
	                      'JJJ End': 'End', 'JJJ Class': 'Class'})    # renombra columnas
	return df                    

	
	



def time_process(df):  # procesa datos, agrupa por fecha, limpia y renombra el dataframe de las llamaradas
	df=clean_flares(df)
	date=[df['Date'][i].split('_') for i in range(len(df))]    # formato de fecha
	date=[date[i][0] for i in range(len(df))]
	date=[pd.to_datetime(date[i],  format='%Y%m%d', errors='ignore').date() for i in range(len(df))]
	df['Date']=date
	
	start=[df['Start'][i] for i in range(len(df))]      # tiempo llamaradas (formato de fecha)
	start=[datetime.datetime.strptime(start[i], '%Y-%m-%dT%H:%M:%S') for i in range(len(df))]
	end=[df['End'][i] for i in range(len(df))]
	end=[datetime.datetime.strptime(end[i], '%Y-%m-%dT%H:%M:%S') for i in range(len(df))]
	df['Start']=start
	df['End']=end
	df['Flare Duration']=df['End']-df['Start']  # duracion de cada llamarada
	

	f_class=pd.DataFrame(df.groupby(['Date'])['Class'].apply(list), columns=['Class'])                       # agrupacion por fecha de las llamaradas
	f_duration=pd.DataFrame(df.groupby(['Date'])['Flare Duration'].apply(list), columns=['Flare Duration'])  # agrupacion por fecha de la duracion
	
	df=pd.concat([f_class, f_duration], axis=1)         # concatena clase y duracion
	
	
	#df.insert(9, 'F Month Max', pd.Series(list(range(len(df))))) 
	max_f=[max(df['Flare Duration'][i]) for i in range(len(df))]  # duracion maxima
	df['F Max Duration']=max_f
	
	mean_f=[np.mean(df['Flare Duration'][i]) for i in range(len(df))]  # media de duracion
	df['F Mean Duration']=mean_f
	
	n_flares=[len(df['Class'][i]) for i in range(len(df['Class']))]  # numero de llamaradas
	df['Flares Number']=n_flares
	
	df['Flare Duration']=[[str(df['Flare Duration'][j][i])[-8:] for i in range(len(df['Flare Duration'][j]))] for j in range(len(df))]  # formato temporal
	df['Flare Duration']=[[pd.to_datetime(df['Flare Duration'][j][i],  format='%H%M%S', errors='ignore')\
	                       for i in range(len(df['Flare Duration'][j]))] for j in range(len(df))]
	
	df['F Mean Duration']=[str(df['F Mean Duration'][i])[6:15] for i in range(len(df))]  # formato temporal
	df['F Mean Duration']=[pd.to_datetime(df['F Mean Duration'][i],  format='%H%M%S', errors='ignore') for i in range(len(df))] 
	
	return df
	





def spots():
	spots=quandl.get("SIDC/SUNSPOTS_D", authtoken=token('Token.txt'))        # llamada al csv desde la api
	spots=spots[(spots.index>='2010-05-01') & (spots.index<='2017-10-09')]   # seleccion por fecha
	df=pd.DataFrame()
	df['Spots Number']=spots['Daily Sunspot Number']        # me quedo con el numero de manchas..
	df['Std Spots Number']=spots['Standard Deviation']      # y su desviacion estandar
	return df





def f_n_class(df):                 # clasificacion numerica de las llamaradas
	cnf=[]
	for j in range(len(df)):
		temp_cnf=[]
		for i in range(len(df['Class'][j])):
			c=df['Class'][j][i]
			if c[0]=='A'  : n_class=float('{:.2f}'.format(float(c[1:])))
			elif c[0]=='B': n_class=float('{:.2f}'.format(10*float(c[1:])))
			elif c[0]=='C': n_class=float('{:.2f}'.format(100*float(c[1:])))
			elif c[0]=='M': n_class=float('{:.2f}'.format(1000*float(c[1:])))
			elif c[0]=='X': n_class=float('{:.2f}'.format(10000*float(c[1:])))
			temp_cnf.append(n_class)
		cnf.append(temp_cnf)	
		
	df.insert(1, 'n_Class', pd.Series(cnf))  # no funciona como yo pensaba, reintroduce los datos
	df['n_Class']=cnf		                 # inserta clase numerica
	
	
	df.insert(1, 'Maximum', pd.Series(cnf))   # inserta maxima diaria        
	maximum=[(df['Class'][j]).index(max(df['Class'][j])) for j in range(len(df))]
	df['Maximum']=[df['Class'][j][(maximum[j])] for j in range(len(df))]
	
	
	mean=[float('{:.2f}'.format(np.mean(cnf[i]))) for i in range(len(cnf))]  # inserta media diaria
	mean_class=[]
	for e in mean:
		if e>=1 and e<10: mean_class.append('A'+'{:.2f}'.format(e))
		elif e/10>=1 and e/10<10: mean_class.append('B'+'{:.2f}'.format(e/10))
		elif e/100>=1 and e/100<10: mean_class.append('C'+'{:.2f}'.format(e/100))
		elif e/1000>=1 and e/1000<10: mean_class.append('M'+'{:.2f}'.format(e/1000))
		else: mean_class.append('X'+'{:.2f}'.format(e/10000)) 
	df.insert(2, 'Mean', pd.Series(mean))
	df['Mean']=mean_class	
	
	df.insert(4, 'n_Maximum', pd.Series(mean))
	df['n_Maximum']=[df['n_Class'][j][(maximum[j])] for j in range(len(df))]
	
	df.insert(5, 'n_Mean', pd.Series(mean))
	df['n_Mean']=mean
	
	return df
		





def month_means(df):         # medias mensuales de llamaradas y manchas (media de medias, media de maximos, etc..)
	
	df.insert(6, 'F Month Mean', pd.Series(list(range(len(df)))))   # media mensual de medias
	for i in range(5, 13):
		df.loc[(df.index.year==2010) & (df.index.month==i), 'F Month Mean']=df[(df.index.year==2010) & (df.index.month==i)]['n_Mean'].mean()
	for i in range(1, 13):
		df.loc[(df.index.year==2011) & (df.index.month==i), 'F Month Mean']=df[(df.index.year==2011) & (df.index.month==i)]['n_Mean'].mean()
	for i in range(1, 11):
		df.loc[(df.index.year==2012) & (df.index.month==i), 'F Month Mean']=df[(df.index.year==2012) & (df.index.month==i)]['n_Mean'].mean()
	df.loc[(df.index.year==2012) & (df.index.month==12), 'F Month Mean']=df[(df.index.year==2012) & (df.index.month==12)]['n_Mean'].mean()
	for i in range(1, 8):
		df.loc[(df.index.year==2013) & (df.index.month==i), 'F Month Mean']=df[(df.index.year==2013) & (df.index.month==i)]['n_Mean'].mean()
	for i in range(11, 13):
		df.loc[(df.index.year==2013) & (df.index.month==i), 'F Month Mean']=df[(df.index.year==2013) & (df.index.month==i)]['n_Mean'].mean()
	for i in range(2014, 2017):
		for j in range(1, 13):
			df.loc[(df.index.year==i) & (df.index.month==j), 'F Month Mean']=df[(df.index.year==i) & (df.index.month==j)]['n_Mean'].mean()
	for i in range(1, 11):
		df.loc[(df.index.year==2017) & (df.index.month==i), 'F Month Mean']=df[(df.index.year==2017) & (df.index.month==i)]['n_Mean'].mean()
	
	
	df.insert(6, 'F Month Maximum', pd.Series(list(range(len(df))))) # media mensual de maximos
	for i in range(5, 13):
		df.loc[(df.index.year==2010) & (df.index.month==i), 'F Month Maximum']=df[(df.index.year==2010) & (df.index.month==i)]['n_Maximum'].mean()
	for i in range(1, 13):
		df.loc[(df.index.year==2011) & (df.index.month==i), 'F Month Maximum']=df[(df.index.year==2011) & (df.index.month==i)]['n_Maximum'].mean()
	for i in range(1, 11):
		df.loc[(df.index.year==2012) & (df.index.month==i), 'F Month Maximum']=df[(df.index.year==2012) & (df.index.month==i)]['n_Maximum'].mean()
	df.loc[(df.index.year==2012) & (df.index.month==12), 'F Month Maximum']=df[(df.index.year==2012) & (df.index.month==12)]['n_Maximum'].mean()
	for i in range(1, 8):
		df.loc[(df.index.year==2013) & (df.index.month==i), 'F Month Maximum']=df[(df.index.year==2013) & (df.index.month==i)]['n_Maximum'].mean()
	for i in range(11, 13):
		df.loc[(df.index.year==2013) & (df.index.month==i), 'F Month Maximum']=df[(df.index.year==2013) & (df.index.month==i)]['n_Maximum'].mean()
	for i in range(2014, 2017):
		for j in range(1, 13):
			df.loc[(df.index.year==i) & (df.index.month==j), 'F Month Maximum']=df[(df.index.year==i) & (df.index.month==j)]['n_Maximum'].mean()
	for i in range(1, 11):
		df.loc[(df.index.year==2017) & (df.index.month==i), 'F Month Maximum']=df[(df.index.year==2017) & (df.index.month==i)]['n_Maximum'].mean()
	
	return df	






def data():                      # datos
	df=read('flares.csv')        # leer csv
	df=time_process(df)          # dataframe (kaggle)
	df=pd.merge(df, spots(), how='inner', left_index=True, right_index=True) # merge con los datos de la api
	df=f_n_class(df)                 # clasificacion numerica
	df=month_means(df)               # medias mensuales
	df.to_csv('flares(clean).csv')   # guarda dataset limpio 
	return df









