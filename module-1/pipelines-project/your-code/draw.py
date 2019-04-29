# draw.py.


import matplotlib.pyplot as plt   # para plots
from pandas.plotting import register_matplotlib_converters  # plots pandas
register_matplotlib_converters()
import numpy as np                      # numerical python
import seaborn as sns                   # para plots
from scipy.interpolate import interp1d


def bar_plot(df):
	plt.bar(df.index, df['F Month Mean'], color='b')
	#plt.bar(df.index, df['Spots Number'], color='r')
	plt.plot(df.index, df['Spots Number'], color='r')
	plt.show()
	return ''



def curve_plot(df):
	f=interp1d([i for i in range(len(df))], df['F Month Mean'].to_list(), 'quadratic')
	plt.plot([i for i in range(len(df))],f([i for i in range(len(df))]), color='r')
	plt.show()
	return ''



def correlation_heatmap(df):
	mask=np.zeros_like(df.corr(), dtype=np.bool)
	mask[np.triu_indices_from(mask)]=True
	cmap=sns.diverging_palette(220, 10, as_cmap=True)
	sns.heatmap(df.corr(), mask=mask, cmap=cmap, vmax=1.0, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
	plt.title("Correlation")                                     
	plt.show()   
	return ''



def draw(df):
	bar_plot(df)
	curve_plot(df)
	correlation_heatmap(df)













