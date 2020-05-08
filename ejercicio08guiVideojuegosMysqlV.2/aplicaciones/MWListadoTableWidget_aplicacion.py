'''
Módulo para mostrar listado de todos los videojuegos mediante Table widget
@author: Pedro Laserna
'''

import pathlib
from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QPixmap
from ventanas import MWListadoTableWidget
from modelo import operaciones_bbdd

class MainWindow_listado_table_widget(MWListadoTableWidget.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        #llamamos al método sacar_listado para rellenar la tabla con los registros de la bbdd
        self.sacar_listado()
    
    #único método de la ventana que se encarga de rellenar el listado
    def sacar_listado(self):
        #reinicializamos el widget para mostrar la información
        self.tbl_listado_videojuegos.clearContents()
        #obtenemos todos los videojuegos
        videojuegos = operaciones_bbdd.obtener_videojuegos_bd()
        
        fila = 0
        #recorremos el listado de videojuegos y vamos añadiendo a la tabla la información a visualizar
        for videojuego in videojuegos:
            columna = 0
            self.tbl_listado_videojuegos.insertRow(fila)
            for campo in videojuego:
                if columna == 5 and campo == 0:
                    campo = "No"
                elif columna == 5 and campo == 1:
                    campo = "Si"
                celda = QtWidgets.QTableWidgetItem(str(campo))
                #solicitamos alinear el texto de las celdas al centro
                celda.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tbl_listado_videojuegos.setItem(fila, columna, celda)
                columna += 1
            #incluimos la imagen asociada al videojuego (si la tuviera) en la última columna
            icono = QtWidgets.QLabel()
            ruta_imagen = "aplicaciones\\../imagenes/"+str(videojuego[0])+".jpg"
            objeto_path = pathlib.Path(ruta_imagen)
            existe = objeto_path.is_file()
            if existe:
                pixmap = QPixmap("aplicaciones\\../imagenes/"+str(videojuego[0])+".jpg")
                pixmap_redim = pixmap.scaledToHeight(100)
                icono.setPixmap(pixmap_redim)
                self.tbl_listado_videojuegos.setCellWidget(fila, columna, icono)
            else:
                #si no existe imagen se indica mediante el texto "Sin Imagen" centrado 
                sin_imagen = QtWidgets.QTableWidgetItem("Sin Imagen")
                sin_imagen.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tbl_listado_videojuegos.setItem(fila, columna, sin_imagen)
            fila += 1
        #ajustamos las columnas al contenido de las celdas
        self.tbl_listado_videojuegos.resizeColumnsToContents()
        #indicamos el alto de las filas para que se puedan visualizar mínimamente las imágenes
        self.tbl_listado_videojuegos.verticalHeader().setDefaultSectionSize(100)
        #finalmente indicamos en etiqueta la cantidad de videojuegos encontrados
        self.lbl_juegos_listados.setText("Juegos listados: {}".format(len(videojuegos)))
        