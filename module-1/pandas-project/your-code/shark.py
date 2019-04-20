# -*- coding: utf-8 -*-
# para tiburones


import re



def shark(datos):
	
	R=[]

	for e in datos:
		
		#1er filtro
		n_dato=re.sub('[0-9]', '', e)
		n_dato=re.sub('\W', '', n_dato)
		n_dato=re.sub('[a-z ]*?white[a-z ]* ?\W?','white', n_dato)                        # blanco
		n_dato=re.sub('[a-z ]*?mako[a-z ]* ?\W?','mako', n_dato)                          # mako
		n_dato=re.sub('[a-z ]*?blue[a-z ]* ?\W?','blue', n_dato)                          # azul
		n_dato=re.sub('[a-z ]*?bull[a-z ]* ?\W?', 'bull', n_dato)                         # toro
		n_dato=re.sub('[a-z ]*?[san]?[d]?tiger[a-z ]* ?\W?', 'tiger', n_dato)             # tigre
		n_dato=re.sub('[a-z ]*?lemon[a-z ]* ?\W?', 'lemon', n_dato)                       # limon
		n_dato=re.sub('[a-z ]*?blacktip[a-z ]* ?\W?', 'blacktip', n_dato)                 # blacktip
		n_dato=re.sub('[a-z ]*?nurse[a-z ]* ?\W?', 'nurse', n_dato)                       # nurse
		n_dato=re.sub('[a-z ]*?goblin[a-z ]* ?\W?', 'goblin', n_dato)                     # goblin
		n_dato=re.sub('[a-z ]*?spinner[a-z ]* ?\W?', 'spinner', n_dato)                   # spinner
		n_dato=re.sub('[a-z ]*?wobbegong[a-z ]* ?\W?', 'wobbegong', n_dato)               # wobbegong
		n_dato=re.sub('[a-z ]*?grey[a-z ]* ?\W?', 'grey', n_dato)                         # gris
		n_dato=re.sub('[a-z ]*?reef[a-z ]* ?\W?', 'reef', n_dato)                         # de arrecife
		n_dato=re.sub('[a-z ]*?galapagos[a-z ]* ?\W?', 'galapagos', n_dato)               # galapagos
		n_dato=re.sub('[a-z ]*?dogfish[a-z ]* ?\W?', 'dogfish', n_dato)                   # dogfish
		n_dato=re.sub('[a-z ]*?[a-z ]?hammerhead[a-z ]* ?\W?', 'hammerhead', n_dato)      # martillo
		n_dato=re.sub('[a-z ]*?bronze[a-z ]* ?\W?', 'bronze', n_dato)                     # bronce
		n_dato=re.sub('[a-z ]*?zambesi[a-z ]* ?\W?', 'zambesi', n_dato)                   # zambesi
		n_dato=re.sub('[a-z ]*?zambezi[a-z ]* ?\W?', 'zambesi', n_dato)                   # zambesi
		n_dato=re.sub('[a-z ]*?dusky[a-z ]* ?\W?', 'dusky', n_dato)                       # dusky
		n_dato=re.sub('[a-z ]*?leopard[a-z ]* ?\W?', 'leopard', n_dato)                   # leopardo
		n_dato=re.sub('[a-z ]*?raggedtooth[a-z ]* ?\W?', 'raggedtooth', n_dato)           # raggedtooth
		n_dato=re.sub('[a-z ]*?carpet[a-z ]* ?\W?', 'carpet', n_dato)                     # carpet
		n_dato=re.sub('[a-z ]*?angel[a-z ]* ?\W?', 'angel', n_dato)                       # angel
		n_dato=re.sub('[a-z ]*?banjo[a-z ]* ?\W?', 'banjo', n_dato)                       # banjo
		n_dato=re.sub('[a-z ]*?copper[a-z ]* ?\W?', 'copper', n_dato)                     # copper
		n_dato=re.sub('[a-z ]*?cleucas[a-z ]* ?\W?', 'cleucas', n_dato)                   # cleucas
		n_dato=re.sub('[a-z ]*?spurdog[a-z ]* ?\W?', 'spurdog', n_dato)                   # spurdog
		
		n_dato=re.sub('[a-z ]*?m?shark[a-z ]* ?\W?', 'other', n_dato)                     # otros
		n_dato=re.sub('[a-z ]*?invalid[a-z ]* ?\W?', 'other', n_dato)                     # otros
		n_dato=re.sub('[a-z ]*?questionable[a-z ]* ?\W?', 'other', n_dato)                # otros
		n_dato=re.sub('[a-z ]*?doubt[a-z ]* ?\W?', 'other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?unidentif[a-z ]* ?\W?', 'other', n_dato)                   # otros
		n_dato=re.sub('[a-z ]*?tooth[a-z ]* ?\W?', 'other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?believe[a-z ]* ?\W?', 'other', n_dato)                     # otros
		n_dato=re.sub('[a-z ]*?diameter[a-z ]* ?\W?', 'other', n_dato)                    # otros
		n_dato=re.sub('[a-z ]*?drown[a-z ]* ?\W?', 'other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?climb[a-z ]* ?\W?', 'other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?authen[a-z ]* ?\W?', 'other', n_dato)                      # otros
		n_dato=re.sub('[a-z ]*?margi[a-z ]* ?\W?', 'other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?to[a-z ]* ?\W?', 'other', n_dato)                          # otros
		n_dato=re.sub('[a-z ]*?less[a-z ]* ?\W?', 'other', n_dato)                        # otros
		n_dato=re.sub('[a-z ]*?whale[a-z ]* ?\W?', 'other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?beag[a-z ]* ?\W?', 'other', n_dato)                        # otros
		n_dato=re.sub('[a-z ]*?unkno[a-z ]* ?\W?', 'other', n_dato)                       # otros




		R.append(n_dato)


	return R
	
	
