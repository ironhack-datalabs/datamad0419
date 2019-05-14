import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
      super().__init__()
      self.title = 'Puntuaciones GEOSPHERE'
      self.left = 20
      self.top = 20
      self.width = 480
      self.height = 360
      self.initUI()
      self.values= {}
      self.videojuegos
      self.software
      self.bigcompany
      self.startup
      self.usa
      self.values= {
        'games_video' : 0,
        'software' : 0,
        'bigcompany' : 0,
        'startup' : 0,
        'usa': 0
      }
    
    def initUI(self):
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self.width, self.height)
      
      lblIntro = QLabel("Introduzca las puntuaciones:", self)
      lblIntro.move(20, 20)

      lblVJ = QLabel("Valores para videojuegos:", self)
      lblVJ.move(20, 60)

      lblSW = QLabel("Valores para software:", self)
      lblSW.move(20, 100)

      lblBC = QLabel("Valores para gran compañía:", self)
      lblBC.move(20, 140)

      lblST = QLabel("Valores para Startup:", self)
      lblST.move(20, 180)

      lblUSA = QLabel("Penalización USA:", self)
      lblUSA.move(20, 220)

      # Inputs
      self.videojuegos= QLineEdit(self)
      self.videojuegos.setPlaceholderText("Numeros enteros")
      self.videojuegos.move(250, 60)

      self.software = QLineEdit(self)
      self.software.setPlaceholderText("Numeros enteros")
      self.software.move(250, 100)

      self.bigcompany = QLineEdit(self)
      self.bigcompany.setPlaceholderText("Numeros enteros")
      self.bigcompany.move(250, 140)

      self.startup = QLineEdit(self)
      self.startup.setPlaceholderText("Numeros enteros")
      self.startup.move(250, 180)

      self.usa = QLineEdit(self)
      self.usa.setPlaceholderText("Valor negativo")
      self.usa.move(250, 220)

      button = QPushButton('Enviar', self)
      button.move(250,280)
      button.clicked.connect(self.on_click)
      
      self.show()

    @pyqtSlot()
    def on_click(self):
      self.values= {
      'games_video' : self.videojuegos.text(),
      'software' : self.software.text(),
      'bigcompany' : self.bigcompany.text(),
      'startup' : self.startup.text(),
      'usa': self.usa.text()
      }


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


