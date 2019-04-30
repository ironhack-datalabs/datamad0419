# draw.py.


import matplotlib.pyplot as plt   # para plots
from pandas.plotting import register_matplotlib_converters  # plots pandas
register_matplotlib_converters()
import numpy as np                      # numerical python
import seaborn as sns                   # para plots
from pipeline import *                  # desde el pipeline
from stats import *


def bar_plot(df):   # plot del numero de  manchas
	plt.bar(df.index, df['Spots Number'], color='r')
	plt.title('Sunspots',size=12,fontweight='bold')
	plt.xlabel('Date',size=10)                   
	plt.ylabel('Number',size=10)
	plt.savefig('barplot_spots.png')
	#plt.show()
	plt.close()
	
	plt.bar(df.index, df['Flares Number'], color='y')
	plt.title('Solar Flares',size=12,fontweight='bold')
	plt.xlabel('Date',size=10)                   
	plt.ylabel('Number',size=10)
	plt.savefig('barplot_flares.png')
	#plt.show()
	plt.close()
	return ''



def binning_plot(df):   # plot por clase de llamarada
	A=0
	B=0
	C=0
	M=0
	X=0
	for i in range(len(df)):
		for j in range(len(df['n_Class'][i])):
			if df['n_Class'][i][j]<10: A+=1
			elif df['n_Class'][i][j]>=10 and df['n_Class'][i][j]<100: B+=1
			elif df['n_Class'][i][j]>=100 and df['n_Class'][i][j]<1000: C+=1
			elif df['n_Class'][i][j]>=1000 and df['n_Class'][i][j]<10000: M+=1
			else : X+=1
	values=[A,B,C,M,X]
	binn=pd.DataFrame(values)
	binn=binn.T
	binn=binn.rename(columns={0: 'A', 1: 'B', 2: 'C', 3: 'M', 4: 'X'})
	binn.plot(kind='bar', color=['g','b','y','orange','r'])
	plt.title('Flares Classes',size=12,fontweight='bold')
	plt.xlabel('Class',size=10)                   
	plt.ylabel('Number',size=10)
	plt.savefig('binning.png')
	#plt.show()
	plt.close()
	return ''



def correlation_heatmap(df):     # plot de correlacion
	mask=np.zeros_like(df.corr(), dtype=np.bool)
	mask[np.triu_indices_from(mask)]=True
	cmap=sns.diverging_palette(220, 10, as_cmap=True)
	sns.heatmap(df.corr(method='spearman'), mask=mask, cmap=cmap, vmax=1.0, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
	plt.title("Correlation")  
	plt.savefig('correlation.png', dpi=100)                                   
	plt.show()  
	plt.close() 
	return ''



def draw(df):
	bar_plot(df)
	binning_plot(df)
	correlation_heatmap(df)













