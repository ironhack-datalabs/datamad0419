# stats.py

from pipeline import *
from draw import *
from stats import *
from scipy.stats import spearmanr as spr      # coeficiente correlacion spearman
from scipy.stats import kendalltau as kdl     # coeficiente correlacion kendall



def correlation(df):
	corrp1=np.corrcoef(df['Spots Number'],df['Flares Number'])      
	cp1='La correlación de Pearson entre el número de manchas y el número de llamaradas es {:.2f}'.format(corrp1[0][1])
	#print (cp1)
	corrp2=np.corrcoef(df['Spots Month Mean'],df['F Month Mean'])      
	cp2='La correlación de Pearson entre la media mensual de manchas y de llamaradas es {:.2f}'.format(corrp2[0][1])
	#print (cp2)
	corrp3=np.corrcoef(df['Spots Month Mean'],df['F Month Maximum'])      
	cp3='La correlación de Pearson entre la media mensual de manchas y el máximo mensual de llamaradas es {:.2f}'.format(corrp3[0][1])
	#print (cp3)
	
	
	corrs1=spr(df['Spots Number'],df['Flares Number'])  
	cs1='La correlación de Spearman entre el número de manchas y el número de llamaradas es {:.2f}'.format(corrs1[0])
	#print (cs1)
	corrs2=spr(df['Spots Month Mean'],df['F Month Mean'])      
	cs2='La correlación de Spearman entre la media mensual de manchas y de llamaradas es {:.2f}'.format(corrs2[0])
	#print (cs2)
	corrs3=spr(df['Spots Month Mean'],df['F Month Maximum'])      
	cs3='La correlación de Spearman entre la media mensual de manchas y el máximo mensual de llamaradas es {:.2f}'.format(corrs3[0])
	#print (cs3)
	
	
	corrk1=kdl(df['Spots Number'],df['Flares Number'])   
	ck1='La correlación de Kendall entre el numero de manchas y el número de llamaradas es {:.2f}'.format(corrk1[0])
	#print (ck1)
	corrk2=kdl(df['Spots Month Mean'],df['F Month Mean'])      
	ck2='La correlación de Kendall entre la media mensual de manchas y de llamaradas es {:.2f}'.format(corrk2[0])
	#print (ck2)
	corrk3=kdl(df['Spots Month Mean'],df['F Month Maximum'])      
	ck3='La correlación de Kendall entre la media mensual de manchas y el máximo mensual de llamaradas es {:.2f}'.format(corrk3[0])
	#print (ck3)

	return [cp1, cp2, cp3, cs1, cs2, cs3, ck1, ck2, ck3]





def stats(df):
	correlation(df)
	return ''







