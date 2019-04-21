# -*- coding: utf-8 -*-
# para regEX


import re



def regEX(datos):
	R=[]
	res=[]
	cero=0   # contador
	uno=0
	dos=0
	tres=0
	cuatro=0
	for e in datos:
		#1er filtro
		n_dato=re.sub('fatal', '4', e)
		n_dato=re.sub('^[a-z ]?,?no[t]? ?inj[a-z]+,?\W?\w?[a-z ]+,?\W?[a-z ]+\W?\w?','0', n_dato)                 # clase sin daño
		n_dato=re.sub('\w? ?\w? ?minor\W? ?[a-z ]+ ?\W? ?[a-z]+ ?[a-z]+', '1', n_dato)                            # clase bajo
		n_dato=re.sub('[0-9]?lacer[a-z ]+\W? ?[a-z ]+ ?[a-z ]+ ?[a-z]+ ?\W+? ?\w+\W?', '2', n_dato)               # clase medio
		n_dato=re.sub('[a-z]+? ?[a-z]?[severe][a-z]+ ?[a-z ]+ ?[a-z ]+[0-9]?\W? ?\w?\W? ?\w?[a-z]?', '3', n_dato) # clase alto
		
		#2ºfiltro , barriendo el resto
		n_dato=re.sub('[a-z]+? ?[bit][a-z ]+', '2', n_dato)          # clase medio
		n_dato=re.sub('[a-z ]+\W+', '', n_dato) 
		n_dato=re.sub('unknown', '2', n_dato)                        # clase medio, por asignacion
		n_dato=re.sub('[a-z ]', '', n_dato) 
		n_dato=re.sub('\W|ã', '', n_dato) 
		n_dato=re.sub('[5-9]', '', n_dato) 
		
		R.append(n_dato)
	
	for e in R:                        # intento de clasificacion con numeros
		if len(e)==1:res.append(e) 
		else:
			for i in range(len(e)):
				n=e[i]
				if e[i-1]>e[i]:n=e[i-1]
			res.append(n)	
				
		
	for f in res:                # bucle para cuantas me faltan por asignar 
		if   f=='0': cero+=1	
		elif f=='1': uno+=1
		elif f=='2': dos+=1
		elif f=='3': tres+=1
		elif f=='4': cuatro+=1
	return res#, '0={}, 1={}, 2={}, 3={}, 4={}, total={}, faltan={}'.format(cero, uno, dos, tres, cuatro, len(res), len(res)-cero-uno-dos-tres-cuatro)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
