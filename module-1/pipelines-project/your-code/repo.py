# repo.py

from fpdf import FPDF    # para crear pdf
from pipeline import *
from draw import *
from stats import *



pdf=FPDF(format='letter') # formato dinA4
pdf.add_page()        # añade pagina
pdf.set_xy(0, 0)
pdf.set_font('arial', 'B', 12)                            # arial 12 en negrita
pdf.cell(60)                                              # posicion texto
pdf.cell(90, 10, "Solar Flares vs Sunspots", 0, 2, 'C')   # titulo
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.image('sol.jpg', x=8, y=20, w=200, h=200, type = '', link = '') # imagen
pdf.cell(90, 10, "Yonatan Rodriguez", 0, 2, 'C') 


pdf.add_page()
pdf.set_font('arial', '', 10)      # cuerpo
pdf.ln(0.25)
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(0, 10, 'Mi hipotesis alternativa es que el numero de manchas solares esta de alguna manera relacionado con las')
pdf.ln(0.25)
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(0, 0, 'llamaradas solares. Empezare uniendo dos datasets, uno de de las manchas y otro de las llamaradas.')
pdf.ln(0.25)
pdf.cell(0, 10, 'Creare un pipeline, con varios archivos añadidos, para que sea un codigo lo mas limpio y lo mas eficiente posible.')
pdf.ln(0.25)
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(0, 10, 'https://www.kaggle.com/heliodata/instruments-solarflares  # dataset llamaradas')
pdf.ln(0.25)
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(0, 10, 'gracias a https://arxiv.org/abs/1703.04412')
pdf.ln(0.25)
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(0, 10, 'desde la API Quandl dataset manchas:')
pdf.ln(0.25)
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(0, 10, 'https://www.quandl.com/data/SIDC/SUNSPOTS_D-Total-Sunspot-Numbers-Daily ')
pdf.ln(0.25)
pdf.cell(90, 10, " ", 0, 2, 'C')

#pdf.image('binning.png', x=None, y=None, w=120, h=100, type = '', link = '') # imagen
pdf.output('repo.pdf', 'F')


	

'''
No parece existir una relación entre el número de manchas solares y el número de llamaradas solares,
en éste caso habría que quedarse con la hipótesis nula. De hecho el coeficiente de correlación es 0,32.
referencia : http://adsabs.harvard.edu/abs/2004AAS...205.1002S
''' 




