# -*- coding: utf-8 -*-
# para regEX


import re



def regEX(datos):
	R=[]
	cero=0   # contador
	uno=0
	dos=0
	tres=0
	cuatro=0
	for e in datos:
		
		n_dato=re.sub('^[a-z ]?,?no[t]? ?inj[a-z]+,?\W?\w?[a-z ]+,?\W?[a-z ]+\W?\w?','0', e)          # clase sin daño
		
		n_dato=re.sub('\w? ?\w? ?minor\W? ?[a-z ]+ ?\W? ?[a-z]+ ?[a-z]+', '1', n_dato)         # clase bajo
		
		n_dato=re.sub('[0-9]?lacer[a-z ]+\W? ?[a-z ]+ ?[a-z ]+ ?[a-z]+ ?\W+? ?\w+', '2', n_dato)                # clase medio
		
		n_dato=re.sub('[a-z]? ?[a-z]?[severe][a-z]+ ?[a-z ]+ ?[a-z ]+[0-9]?\W? ?\w?\W? ?\w?', '3', n_dato)                  # clase alto
		
		#n_dato=re.sub('[a-z]\w? ?\W?\w?[fatal][a-z ]+ ?[a-z ]+ ?[a-z]+\W?', '4', n_dato)              # clase mortal

		R.append(n_dato)
		
	for f in R:
		if   f=='0': cero+=1	
		elif f=='1': uno+=1
		elif f=='2': dos+=1
		elif f=='3': tres+=1
		elif f=='4': cuatro+=1
	return R, '0={}, 1={}, 2={}, 3={}, 4={}, total={}, faltan={}'.format(cero, uno, dos, tres, cuatro, len(R), len(R)-cero-uno-dos-tres-cuatro)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
