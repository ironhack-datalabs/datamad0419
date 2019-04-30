# stats.py

from pipeline import *
from draw import *
from stats import *


def correlation(df):
	corr1=np.corrcoef(df['Spots Number'],df['Flares Number'])      
	c1='La correlacion entre el numero de manchas y el numero de llamaradas es {:.2f}'.format(corr1[0][1])
	#print (c1)
	
	corr2=np.corrcoef(df['Spots Month Mean'],df['F Month Mean'])      
	c2='La correlacion entre la media mensual de manchas y de llamaradas es {:.2f}'.format(corr2[0][1])
	#print (c2)
	
	corr3=np.corrcoef(df['Spots Month Mean'],df['F Month Maximum'])      
	c3='La correlacion entre la media mensual de manchas y el maximo mensual de llamaradas es {:.2f}'.format(corr3[0][1])
	#print (c3)
	
	return c1, c2, c3





def stats(df):
	correlation(df)
	return ''







