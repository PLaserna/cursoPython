'''
Versión 2 del programa de gestión de videojuegos en soporte físico (cartuchos, cds, dvds...)
@author: Pedro Laserna
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import MWPortada
from modelo import operaciones_bbdd
from aplicaciones import MWPortada_aplicacion

    #arranque de la aplicación principal
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
    
Portada = MWPortada_aplicacion.MainWindow_portada()
Portada.setupUi(MainWindow)   
     
MainWindow.show()
sys.exit(app.exec_())
