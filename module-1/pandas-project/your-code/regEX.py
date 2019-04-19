# -*- coding: utf-8 -*-
# para regEX


import re



def regEX(datos):
	R=[]
	for e in datos:
		n_dato=re.sub('no[t]? ?i[a-z]+,?\W?\w?[a-z ]+,?\W?[a-z ]+','0', e)
		R.append(n_dato)
	return R
