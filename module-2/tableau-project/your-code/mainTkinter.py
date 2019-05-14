#Si guardamos el fichero como .pyw se abre sin la terminal de fondo.

import tkinter
from tkinter import *

root = Tk()
root.title('Puntuaciones GEOSPHERE')
# ancho y alto, bool
# root.resizable(0,0)
# root.iconbitmap('icon.ico')

frame= Frame(root, width= 640, height= 400)
# Por defecto pack pone arriba y centrado. Se pueden especificar diferentes posiciones
# side='rigth', anchor='e'   (e,w,s,n)
frame.pack(fill='both', expand=1)

# Las mismas propiedades de frame se pueden usar a root para toda la ventana.
frame.config(bg='lightgray')

titulo= Label(frame, text= 'Introduzca puntuaciones.')
titulo.config(font= ('Chandas', 24))
titulo.pack(anchor='nw')
#Abajo del todo para que sea lo último. Es el ejecutador.
root.mainloop()