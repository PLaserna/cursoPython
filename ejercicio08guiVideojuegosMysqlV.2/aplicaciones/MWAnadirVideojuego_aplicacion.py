'''
Módulo de la ventana para añadir nuevos videojuegos
@author: Pedro Laserna
'''

import os
import shutil
import pathlib
from PyQt5 import QtWidgets
from PyQt5.Qt import QPixmap
from ventanas import MWAnadirVideojuego
from modelo import clases, operaciones_bbdd, constantes
from validaciones import validacion_videojuego

class MainWindow_anadir_videojuego(QtWidgets.QMainWindow, MWAnadirVideojuego.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.ui = MainWindow
        
        #cada vez que se modifique un radio button se llama al método que modifica el combobox asociado
        self.rb_pc.toggled.connect(self.mostrar_combobox_plataforma)
        self.rb_sega.toggled.connect(self.mostrar_combobox_plataforma)
        self.rb_nintendo.toggled.connect(self.mostrar_combobox_plataforma)
        self.rb_sony.toggled.connect(self.mostrar_combobox_plataforma)
        self.rb_microsoft.toggled.connect(self.mostrar_combobox_plataforma)
        
        #habilitamos link a metacritic si el usuario ha modificado el campo título
        self.le_titulo.textEdited.connect(self.enlazar_metacritic)
        
        #definimos las acciones a realizar para los botones
        self.btn_guardar.clicked.connect(self.registrar_videojuego)
        self.btn_imagen.clicked.connect(self.seleccionar_imagen)
    
    #método para rellenar el combobox dependiendo del radio button seleccionado     
    def mostrar_combobox_plataforma(self):
        #inicializamos el combobox
        self.cmb_plataforma.setEnabled(True)
        self.cmb_plataforma.clear()
        #consultamos que radio buton está marcado para mostrar los elementos que correspondan en el combo 
        if self.rb_pc.isChecked():
            self.cmb_plataforma.addItems(constantes.pc)
        elif self.rb_sega.isChecked():
            self.cmb_plataforma.addItems(constantes.sega)
        elif self.rb_nintendo.isChecked():
            self.cmb_plataforma.addItems(constantes.nintendo)
        elif self.rb_sony.isChecked():
            self.cmb_plataforma.addItems(constantes.sony)
        elif self.rb_microsoft.isChecked():
            self.cmb_plataforma.addItems(constantes.microsoft)
        #si hay mas de un elemento en el combo se mantendrá activo para afinar la selección, si solo hay un elemento se deshabilita
        if self.cmb_plataforma.count() < 2:
            self.cmb_plataforma.setEnabled(False)
    
    #método para habilitar hipervínculo en la etiqueta de nota cuando el usuario modifique el campo título
    def enlazar_metacritic(self):
        titulo = self.le_titulo.text().replace(" ","%20")
        url_metacritic = "https://www.metacritic.com/search/game/"+titulo+"/results"
        self.lbl_nota.setText("Nota ("+"<a href='"+url_metacritic+"'>Metacritic</a>): ")
        self.lbl_nota.setOpenExternalLinks(True)
    
    #método para seleccionar una imagen asociada al videojuego a registrar    
    def seleccionar_imagen(self):
        #abrimos ventana para selección de archivo
        archivo = QtWidgets.QFileDialog.getOpenFileName(self.ui, "Seleccione imagen", "D:\Descargas", "*.jpg")
        #validamos si el usuario ha cerrado la ventana sin seleccionar ningún archivo para que no de error y cierre de aplicación
        if archivo[0] != "":
            #copiamos el archivo a la carpeta "temporal" como "imagen.jpg" y la redimensionamoss para mostrarla en una etiqueta de la ventana 
            ruta_archivo = archivo[0]
            try:
                shutil.copy(ruta_archivo,constantes.ruta_temporal+"/imagen.jpg")
            except:
                os.makedirs(constantes.ruta_temporal)
                shutil.copy(ruta_archivo,constantes.ruta_temporal+"/imagen.jpg")
            pixmap = QPixmap(constantes.ruta_temporal+"/imagen.jpg")
            alto_label = self.lbl_imagen.height()
            pixmap_redim = pixmap.scaledToHeight(alto_label)
            self.lbl_imagen.setPixmap(pixmap_redim)
    
    #método para reinicializar la ventana
    def limpiar_ventana(self):
        self.le_titulo.clear()
        self.le_genero.clear()
        self.rb_pc.setChecked(True)
        self.dspb_nota.setValue(0)
        self.chb_prestado.setChecked(False)
        self.le_apuntes.clear()
        self.lbl_imagen.setText("Sin imagen")
        self.lbl_nota.setText("Nota (Metacritic): ")
        self.lbl_nota.setOpenExternalLinks(False)
        self.lbl_ayuda.clear()
    
    #controlamos que al cerrar la ventana se reinicien los componentes
    def closeEvent(self, event):
        self.limpiar_ventana()
    
    #método para registrar el nuevo videojuego
    def registrar_videojuego(self):
        #recogemos todos los datos en variables
        titulo = self.le_titulo.text()
        titulo_ok = validacion_videojuego.validar_titulo(titulo)
        if not titulo_ok:
            self.lbl_ayuda.setText("Formato de título incorrecto")
            return
        else:
            self.lbl_ayuda.clear()
        genero = self.le_genero.text()
        genero_ok = validacion_videojuego.validar_genero(genero)
        if not genero_ok:
            self.lbl_ayuda.setText("Formato de género incorrecto")
            return
        else:
            self.lbl_ayuda.clear()
        plataforma = self.cmb_plataforma.currentText()
        nota = self.dspb_nota.value()
        #al tratarse de un checkbox validamos si está marcado para indicar si el juego está prestado o no
        if self.chb_prestado.isChecked():
            prestado = 1
        else:
            prestado = 0
        apuntes = self.le_apuntes.text()
        #creamos el videojuego con los datos aportados
        videojuego_a_anadir = clases.Videojuego(titulo,plataforma,genero,nota,prestado,apuntes,0)
        #llamamos a la función registro_videojuego_bd para registrarlo en la bbdd y nos quedamos con la id del nuevo videojuego
        id_generado = operaciones_bbdd.registro_videojuego_bd(videojuego_a_anadir)
        ruta_imagen = constantes.ruta_temporal+"/imagen.jpg"
        objeto_path = pathlib.Path(ruta_imagen)
        existe = objeto_path.is_file()
        #si se ha seleccionado una imagen para el videojuego se mueve a la carpeta imagenes identificándola con la id generada
        if existe:
            shutil.move(constantes.ruta_temporal+"/imagen.jpg","aplicaciones\\../imagenes/"+str(id_generado)+".jpg")
        QtWidgets.QMessageBox.about(self.ui,"Información","El videojuego se ha registrado correctamente.")
        #reinicializamos los campos
        self.limpiar_ventana()
