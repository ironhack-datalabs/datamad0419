# -*- coding: utf-8 -*-
# para tiburones


import re



def shark(datos):
	
	R=[]

	for e in datos:
		
		#1er filtro
		n_dato=re.sub('[0-9]', '', e)
		n_dato=re.sub('\W', '', n_dato)
		n_dato=re.sub('[a-z ]*?white[a-z ]* ?\W?','White', n_dato)                        # blanco
		n_dato=re.sub('[a-z ]*?mako[a-z ]* ?\W?','Mako', n_dato)                          # mako
		n_dato=re.sub('[a-z ]*?blue[a-z ]* ?\W?','Blue', n_dato)                          # azul
		n_dato=re.sub('[a-z ]*?bull[a-z ]* ?\W?', 'Bull', n_dato)                         # toro
		n_dato=re.sub('[a-z ]*?[san]?[d]?tiger[a-z ]* ?\W?', 'Tiger', n_dato)             # tigre
		n_dato=re.sub('[a-z ]*?lemon[a-z ]* ?\W?', 'Lemon', n_dato)                       # limon
		n_dato=re.sub('[a-z ]*?blacktip[a-z ]* ?\W?', 'Blacktip', n_dato)                 # blacktip
		n_dato=re.sub('[a-z ]*?nurse[a-z ]* ?\W?', 'Nurse', n_dato)                       # nurse
		n_dato=re.sub('[a-z ]*?goblin[a-z ]* ?\W?', 'Goblin', n_dato)                     # goblin
		n_dato=re.sub('[a-z ]*?spinner[a-z ]* ?\W?', 'Spinner', n_dato)                   # spinner
		n_dato=re.sub('[a-z ]*?wobbegong[a-z ]* ?\W?', 'Wobbegong', n_dato)               # wobbegong
		n_dato=re.sub('[a-z ]*?grey[a-z ]* ?\W?', 'Grey', n_dato)                         # gris
		n_dato=re.sub('[a-z ]*?reef[a-z ]* ?\W?', 'Reef', n_dato)                         # de arrecife
		n_dato=re.sub('[a-z ]*?galapagos[a-z ]* ?\W?', 'Galapagos', n_dato)               # galapagos
		n_dato=re.sub('[a-z ]*?dogfish[a-z ]* ?\W?', 'Dogfish', n_dato)                   # dogfish
		n_dato=re.sub('[a-z ]*?[a-z ]?hammerhead[a-z ]* ?\W?', 'Hammerhead', n_dato)      # martillo
		n_dato=re.sub('[a-z ]*?bronze[a-z ]* ?\W?', 'Bronze', n_dato)                     # bronce
		n_dato=re.sub('[a-z ]*?zambesi[a-z ]* ?\W?', 'Zambesi', n_dato)                   # zambesi
		n_dato=re.sub('[a-z ]*?zambezi[a-z ]* ?\W?', 'Zambesi', n_dato)                   # zambesi
		n_dato=re.sub('[a-z ]*?dusky[a-z ]* ?\W?', 'Dusky', n_dato)                       # dusky
		n_dato=re.sub('[a-z ]*?leopard[a-z ]* ?\W?', 'Leopard', n_dato)                   # leopardo
		n_dato=re.sub('[a-z ]*?raggedtooth[a-z ]* ?\W?', 'Raggedtooth', n_dato)           # raggedtooth
		n_dato=re.sub('[a-z ]*?carpet[a-z ]* ?\W?', 'Carpet', n_dato)                     # carpet
		n_dato=re.sub('[a-z ]*?angel[a-z ]* ?\W?', 'Angel', n_dato)                       # angel
		n_dato=re.sub('[a-z ]*?banjo[a-z ]* ?\W?', 'Banjo', n_dato)                       # banjo
		n_dato=re.sub('[a-z ]*?copper[a-z ]* ?\W?', 'Copper', n_dato)                     # copper
		n_dato=re.sub('[a-z ]*?cleucas[a-z ]* ?\W?', 'Cleucas', n_dato)                   # cleucas
		n_dato=re.sub('[a-z ]*?spurdog[a-z ]* ?\W?', 'Spurdog', n_dato)                   # spurdog
		
		#2º filtro, otros
		n_dato=re.sub('[a-z ]*?m?shark[a-z ]* ?\W?', 'Other', n_dato)                     # otros
		n_dato=re.sub('[a-z ]*?invalid[a-z ]* ?\W?', 'Other', n_dato)                     # otros
		n_dato=re.sub('[a-z ]*?questionable[a-z ]* ?\W?', 'Other', n_dato)                # otros
		n_dato=re.sub('[a-z ]*?doubt[a-z ]* ?\W?', 'Other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?unidentif[a-z ]* ?\W?', 'Other', n_dato)                   # otros
		n_dato=re.sub('[a-z ]*?tooth[a-z ]* ?\W?', 'Other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?believe[a-z ]* ?\W?', 'Other', n_dato)                     # otros
		n_dato=re.sub('[a-z ]*?diameter[a-z ]* ?\W?', 'Other', n_dato)                    # otros
		n_dato=re.sub('[a-z ]*?drown[a-z ]* ?\W?', 'Other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?climb[a-z ]* ?\W?', 'Other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?authen[a-z ]* ?\W?', 'Other', n_dato)                      # otros
		n_dato=re.sub('[a-z ]*?margi[a-z ]* ?\W?', 'Other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?to[a-z ]* ?\W?', 'Other', n_dato)                          # otros
		n_dato=re.sub('[a-z ]*?less[a-z ]* ?\W?', 'Other', n_dato)                        # otros
		n_dato=re.sub('[a-z ]*?whale[a-z ]* ?\W?', 'Other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?beag[a-z ]* ?\W?', 'Other', n_dato)                        # otros
		n_dato=re.sub('[a-z ]*?unkno[a-z ]* ?\W?', 'Other', n_dato)                       # otros
		n_dato=re.sub('[a-z ]*?ROther[a-z ]* ?\W?', 'Other', n_dato)                      # otros




		R.append(n_dato)


	return R
	
	
