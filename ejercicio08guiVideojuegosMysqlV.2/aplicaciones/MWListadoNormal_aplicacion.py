'''
Módulo para mostrar listado de todos los videojuegos mediante Text Edit widget
@author: Pedro Laserna
'''

from PyQt5 import QtWidgets
from ventanas import MWListadoNormal
from modelo import operaciones_bbdd

class MainWindow_listado_normal(MWListadoNormal.Ui_MainWindow):
    def __init__(self):
        super().__init__()
         
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        
        #llamamos al método sacar_listado para rellenar el text edit widget con los registros de la bbdd
        self.sacar_listado()
    
    #único método de la ventana que se encarga de rellenar el listado
    def sacar_listado(self):
        #reinicializamos el widget para mostrar la información
        self.txe_listado_videojuegos.clear()
        #obtenemos todos los videojuegos
        videojuegos = operaciones_bbdd.obtener_videojuegos_bd()
        #definimos la variable en la que se va a incluir la información de los videojuegos
        texto = ""
        #recorremos el listado de videojuegos y vamos añadiendo la información a visualizar
        for v in videojuegos:
            if v[5] == 0:
                prestado = "No"
            else:
                prestado = "Si"
            texto += "Id: " + str(v[0]) + " - Título: "+ v[1] + "\n"
            texto += "Plataforma: " + v[2] + " | Género: " + v[3] + " | Nota: " + str(v[4]) + " | Prestado: " + prestado
            texto += "\n - - - - - - - - - - \n"
        #mostramos toda la información en el text edit widget
        self.txe_listado_videojuegos.setText(texto)
        #finalmente indicamos en etiqueta la cantidad de videojuegos encontrados
        self.lbl_juegos_listados.setText("Juegos listados: {}".format(len(videojuegos)))
        