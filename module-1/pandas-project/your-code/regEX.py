# -*- coding: utf-8 -*-
# para regEX


import re



def regEX(datos):
	R=[]
	for e in datos:
		n_dato=re.findall('no[t]? i[a-z]+', e)
		R.append(n_dato)
	return R
