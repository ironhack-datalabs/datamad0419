# repo.py

from fpdf import FPDF    # para crear pdf
from pipeline import *
from draw import *
from stats import *


def repo(df):
	print ('Escribiendo repo...')
	pdf=FPDF(format='letter') # formato dinA4
	pdf.add_page()        # añade pagina
	pdf.set_xy(0, 0)
	pdf.set_font('arial', 'B', 12)                            # arial 12 en negrita
	pdf.cell(60)                                              # posicion texto
	pdf.cell(90, 10, "Solar Flares vs Sunspots", 0, 2, 'C')   # titulo
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.image('sol.jpg', x=8, y=20, w=200, h=200, type = '', link = '') # imagen
	pdf.cell(90, 10, "Yonatan Rodriguez", 0, 2, 'C') 
	
	
	pdf.add_page()                     # pagina 1
	pdf.set_font('arial', '', 10)      # cuerpo
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'El próposito de éste trabajo es encontrar una relación entre las manchas solares y las llamaradas solares.')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'Mi hipótesis alternativa es que el número de manchas solares está de alguna manera relacionado con las')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 0, 'llamaradas solares. Empezaré uniendo dos datasets, uno de de las manchas, sacado de una API, y otro de las llamaradas.')
	pdf.ln(0.25)
	pdf.cell(0, 10, 'Crearé un pipeline, con varios archivos añadidos, para que sea un código lo más limpio y lo más eficiente posible.')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'El dataset de llamaradas solares lo he obtenido de la siguiente página:')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'https://www.kaggle.com/heliodata/instruments-solarflares  ')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'gracias a https://arxiv.org/abs/1703.04412')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'Desde la API Quandl he obtenido el dataset de manchas solares:')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'https://www.quandl.com/data/SIDC/SUNSPOTS_D-Total-Sunspot-Numbers-Daily ')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'En la siguiente gráfica pueden verse los datos de las llamaradas:')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.image('barplot_flares.png', x=42, y=None, w=120, h=100, type = '', link = '') # imagen
	
	
	
	pdf.add_page()                     # pagina 2
	pdf.set_font('arial', '', 10)      
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'Otra gráfica con los datos de las manchas solares:')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.image('barplot_spots.png', x=42, y=None, w=100, h=80, type = '', link = '')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'Puede verse que faltan datos. Es un problema del dataset, y también existen valores que son nulos,')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 0, 'donde no ha habido ni llamaradas ni manchas solares.')
	pdf.ln(0.25)
	pdf.cell(0, 10, 'La distribución, tanto de manchas como de llamaradas, parece seguir la normal con el tiempo,')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'aunque en proporción parecen seguir la distribución de Poisson.')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 0, 'Esto se ve en las siguientes gráficas:')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.image('distplot_flares.png', x=42, y=None, w=100, h=80, type = '', link = '')
	
	
	pdf.add_page()                     # pagina 3
	pdf.set_font('arial', '', 10)    
	pdf.image('distplot_spots.png', x=42, y=None, w=120, h=100, type = '', link = '')  
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'La siguiente gráfica muestra la clasificación de las llamaradas solares:')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.image('binning.png', x=42, y=None, w=120, h=100, type = '', link = '')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'En el último ciclo solar, del cúal se analizan los datos, no ha habido llamaradas clase A.')
	
	
	
	
	pdf.add_page()                     # pagina 4
	pdf.set_font('arial', '', 10) 
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'Con estos datos he intentado hacer un análisis basándome en la correlación.')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 0, 'Usaré la correlación de Pearson, Spearman y Kendall con el fin de sacar alguna conclusión.')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'A continuación se muestran los resultados.')
	pdf.ln(0.25)     
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 0, correlation(df)[0])
	pdf.ln(0.25)
	pdf.cell(0, 10, correlation(df)[1])
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, correlation(df)[2])
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.image('correlation Pearson.png', x=42, y=None, w=100, h=80, type = '', link = '')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'No parece existir una relación lineal entre el número de manchas solares y el número de llamaradas solares,')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 0, 'en éste caso habría que quedarse con la hipótesis nula, salvo en la correlación de las medias mensuales.')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'referencia : http://adsabs.harvard.edu/abs/2004AAS...205.1002S')
	
	
	
	pdf.add_page()                     # pagina 5
	pdf.set_font('arial', '', 10) 
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')   
	pdf.cell(0, 0, correlation(df)[3])
	pdf.ln(0.25)
	pdf.cell(0, 10, correlation(df)[4])
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, correlation(df)[5])
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.image('correlation Spearman.png', x=42, y=None, w=100, h=80, type = '', link = '')
	pdf.ln(0.25)     
	pdf.cell(0, 10, 'Como se puede observar, en éste caso sí existe correlación de tipo no lineal entre las medias mensuales')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 0, 'y también con los máximos de las llamaradas. Veamos ahora la correlación de Kendall:')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')   
	pdf.cell(0, 0, correlation(df)[6])
	pdf.ln(0.25)
	pdf.cell(0, 10, correlation(df)[7])
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, correlation(df)[8])
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.image('correlation Kendall.png', x=42, y=None, w=100, h=80, type = '', link = '')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	
	
	pdf.add_page()                     # pagina 6
	pdf.set_font('arial', '', 10) 
	pdf.ln(0.25)
	pdf.cell(0, 10, 'En éste caso no queda del todo clara la correlación, pero viendo el conjunto de resultados resulta')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 0, 'evidente que ,efectivamente, existe una correlación entre el número de manchas solares y las llamaradas')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'solares, y por consiguiente con las eyecciones de masa coronal (CME), las cuales pueden ser causa de graves')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'daños, sobretodo en el ámbito tecnológico.')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 0, 'Para ver si de verdad existe una de causalidad entre ambos fenómenos serían necesarios más estudios')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'que incluyeran datos como el tamaño de las manchas solares y abarcarán un mayor rango temporal.')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 0, 'He obtenido datos en crudo, también desde una API, los he limpiado y creado un pipeline.')
	pdf.ln(0.25)
	pdf.cell(90, 10, " ", 0, 2, 'C')
	pdf.cell(0, 10, 'He hecho un pequeño análisis y dibujado varios plots para ello. PIPELINE PROJECT.')
	
	pdf.output('repo.pdf', 'F')
	print ('repo guardado.')
	
	
	return ''


	


