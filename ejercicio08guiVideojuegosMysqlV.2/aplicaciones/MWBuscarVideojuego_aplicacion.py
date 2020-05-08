'''
Módulo de la ventana para buscar videojuegos, que posteriormente permitirá borrar y editar los datos de los videojuegos incluidos en la bbdd
@author: Pedro Laserna
'''

import os
import shutil
import pathlib
from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QPixmap
from ventanas import MWBuscarVideojuego, DialogModificarVideojuego
from modelo import operaciones_bbdd, clases, constantes
from validaciones import validacion_videojuego

class MainWindow_buscar_videojuego(QtWidgets.QMainWindow, MWBuscarVideojuego.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.ui = MainWindow
        
        #comprobamos los checkbox para ver si es necesario activar/desactivar los radio button asociados
        self.gb_plataformas.toggled.connect(self.activar_rb_plataformas)
        self.gb_prestado.toggled.connect(self.activar_rb_prestado)
        
        #cada vez que se modifique un radio button se llama al método que modifica el combobox asociado
        self.rb_pc.toggled.connect(self.mostrar_combobox_plataforma)
        self.rb_sega.toggled.connect(self.mostrar_combobox_plataforma)
        self.rb_nintendo.toggled.connect(self.mostrar_combobox_plataforma)
        self.rb_sony.toggled.connect(self.mostrar_combobox_plataforma)
        self.rb_microsoft.toggled.connect(self.mostrar_combobox_plataforma)
        
        #definimos las acciones de los botones para limpiar el formulario e iniciar la búsqueda
        self.btn_limpiar.clicked.connect(self.limpiar_formulario)
        self.btn_buscar.clicked.connect(self.buscar_videojuego)
        
        #indicamos que cuando se seleccione alguno de los videojuegos encontrados tras la búsqueda se activen los botones para editar y borrar 
        self.tbl_juegos_encontrados.itemSelectionChanged.connect(self.activar_botones)
        
        #definimos las acciones de los botones para editar y borrar el registro de la bbdd
        self.btn_borrar.clicked.connect(self.borrar_videojuego)
        self.btn_editar.clicked.connect(self.editar_videojuego)
    
    #método para activar los radio button de las plataformas
    def activar_rb_plataformas(self):
        if self.gb_plataformas.isChecked():
            self.rb_pc.setEnabled(False)
            self.rb_sega.setEnabled(False)
            self.rb_nintendo.setEnabled(False)
            self.rb_sony.setEnabled(False)
            self.rb_microsoft.setEnabled(False)
            self.cmb_plataforma.setEnabled(False)
        else:
            self.rb_pc.setEnabled(True)
            self.rb_sega.setEnabled(True)
            self.rb_nintendo.setEnabled(True)
            self.rb_sony.setEnabled(True)
            self.rb_microsoft.setEnabled(True)
            
    #método para activar los radio button de los prestados    
    def activar_rb_prestado(self):
        if self.gb_prestado.isChecked():
            self.rb_prestado_si.setEnabled(False)
            self.rb_prestado_no.setEnabled(False)
        else:
            self.rb_prestado_si.setEnabled(True)
            self.rb_prestado_no.setEnabled(True)
    
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
            
    #método para borrar/reinicializar los campos del formulario de búsqueda    
    def limpiar_formulario(self):
        self.le_id.clear()
        self.le_titulo.clear()
        self.le_genero.clear()
        self.rb_pc.setChecked(True)
        self.gb_plataformas.setChecked(True)
        self.gb_prestado.setChecked(True)
        self.le_apuntes.clear()       
        self.lbl_juegos_encontrados.clear()
        self.limpiar_tabla_resultados()
        self.desactivar_botones()
        self.reducir_ventana()
    
    #método para borrar la tabla con los resultado de la búsqueda
    def limpiar_tabla_resultados(self):
        while self.tbl_juegos_encontrados.rowCount() > 0:
            self.tbl_juegos_encontrados.removeRow(0)
    
    #método para ampliar la ventana si la búsqueda ha devuelto resultados y así poder visualizarlos
    def ampliar_ventana(self):
        self.ui.resize(1222, 651)
        self.ui.setMinimumSize(QtCore.QSize(1222, 651))
        self.ui.setMaximumSize(QtCore.QSize(1222, 651))
    
    #método para reducir la ventana a su tamaño original y ver solo el formulario de búsqueda
    def reducir_ventana(self):
        self.ui.resize(432, 651)
        self.ui.setMinimumSize(QtCore.QSize(432, 651))
        self.ui.setMaximumSize(QtCore.QSize(432, 651))
    
    #método para activar botones de editar/borrar
    def activar_botones(self):
        self.btn_borrar.setEnabled(True)
        self.btn_editar.setEnabled(True)
    
    #método para desactivar botones de editar/borrar
    def desactivar_botones(self):
        self.btn_borrar.setEnabled(False)
        self.btn_editar.setEnabled(False)
    
    #al cerrar la ventana se reinician todos los componentes
    def closeEvent(self, event):
        self.limpiar_formulario()
        self.limpiar_tabla_resultados()
        self.desactivar_botones()
        self.reducir_ventana()
    
    #método para buscar el videojuego en bbdd con los valores aportados
    def buscar_videojuego(self):
        id = self.le_id.text()
        id_ok = validacion_videojuego.validar_id(id)
        if not id_ok:
            self.lbl_ayuda.setText("Formato de id incorrecto")
            return
        else:
            self.lbl_ayuda.clear()
        #reiniciamos tabla de resultados y deshabilitamos los botones de editar/borrar
        self.limpiar_tabla_resultados()
        self.desactivar_botones()
        #creamos diccionario con el campo y el valor para posteriormente realizar las búsquedas
        valores = dict()
        valores["id"] = self.le_id.text()
        valores["titulo"] = self.le_titulo.text()
        valores["genero"] = self.le_genero.text()
        if self.gb_plataformas.isChecked():
            valores["plataforma"] = ""
        else:
            valores["plataforma"] = self.cmb_plataforma.currentText()
        if self.gb_prestado.isChecked():
            valores["prestado"] = ""
        else:
            if self.rb_prestado_no.isChecked():
                valores["prestado"] = 0
            else:
                valores["prestado"] = 1
        valores["apuntes"] = self.le_apuntes.text()
        #solicitamos la búsqueda en bbdd
        videojuegos_encontrados = operaciones_bbdd.buscar_videojuegos_bd(valores)
        #se no se han encontrado resultados se informa mediante mensaje
        if len(videojuegos_encontrados) == 0:
            self.desactivar_botones()
            self.reducir_ventana()
            QtWidgets.QMessageBox.about(self.ui, "Información", "No se ha encontrado ningún videojuego.")
        else:
            #si hay resultados se recorren para ir rellenando la tabla a mostrar al usuario
            fila = 0
            for videojuego in videojuegos_encontrados:
                columna = 0
                self.tbl_juegos_encontrados.insertRow(fila)
                for campo in videojuego:
                    #mostramos "Si" o "No" en vez de 0 y 1 para el campo "prestado"
                    if columna == 5 and campo == 0:
                        campo = "No"
                    elif columna == 5 and campo == 1:
                        campo = "Si"
                    celda = QtWidgets.QTableWidgetItem(str(campo))
                    celda.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tbl_juegos_encontrados.setItem(fila, columna, celda)
                    columna += 1
                #mostramos también la imagen del videjuego si existiera
                icono = QtWidgets.QLabel()
                ruta_imagen = "aplicaciones\\../imagenes/"+str(videojuego[0])+".jpg"
                objeto_path = pathlib.Path(ruta_imagen)
                existe = objeto_path.is_file()
                if existe:
                    pixmap = QPixmap("aplicaciones\\../imagenes/"+str(videojuego[0])+".jpg")
                    pixmap_redim = pixmap.scaledToHeight(100)
                    icono.setPixmap(pixmap_redim)
                    self.tbl_juegos_encontrados.setCellWidget(fila, columna, icono)
                else:
                    sin_imagen = QtWidgets.QTableWidgetItem("Sin Imagen")
                    sin_imagen.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tbl_juegos_encontrados.setItem(fila, columna, sin_imagen)
                fila += 1
            #redimensionamos la tabla de resultados para su visualización
            self.tbl_juegos_encontrados.resizeColumnsToContents()
            self.tbl_juegos_encontrados.verticalHeader().setDefaultSectionSize(100)
            #ampliamos la ventana para que se muestren los resultados
            self.ampliar_ventana()
        #mostramos en etiqueta la cantidad de juegos encontrados
        self.lbl_juegos_encontrados.setText("Juegos encontrados: {}".format(self.tbl_juegos_encontrados.rowCount()))
    
    #método para borrar videojuego de la bbdd
    def borrar_videojuego(self):
        #cogemos la fila seleccionada y de ahí extraemos la id del videojuego a borrar
        fila_seleccionada = self.tbl_juegos_encontrados.currentRow()
        texto_de_columna_id = self.tbl_juegos_encontrados.item(fila_seleccionada, 0).text()
        #la pasamos a tupla para la sql
        id_a_borrar = (texto_de_columna_id,)
        #preguntamos al usuario si está conforme con el borrado
        respuesta = QtWidgets.QMessageBox.question(self.ui, "Alerta", "¿Estás seguro de borrar el videojuego con Id: {}?".format(texto_de_columna_id))
        if respuesta == QtWidgets.QMessageBox.Yes:
            #solicitamos el borrado en bbdd
            operaciones_bbdd.borrar_videojuego_bd(id_a_borrar)
            #comprobamos si el videojuego tenia imagen asociada
            ruta_imagen = "aplicaciones\\../imagenes/"+str(texto_de_columna_id)+".jpg"
            objeto_path = pathlib.Path(ruta_imagen)
            existe = objeto_path.is_file()
            if existe:
                #si la tiene la borramos igualmente
                objeto_path.unlink()
            #informamos al usuario del borrado
            QtWidgets.QMessageBox.about(self.ui, "Información", "El videojuego ha sido borrado")
            #eliminamos la fila de la tabla y si no hay mas filas reducimos la ventana
            linea_seleccionada = self.tbl_juegos_encontrados.currentRow()
            self.tbl_juegos_encontrados.removeRow(linea_seleccionada)
            if self.tbl_juegos_encontrados.rowCount() > 0:
                self.desactivar_botones()
            else:
                self.reducir_ventana()
                self.desactivar_botones()
            #actualizamos la información de la etiqueta con los juegos encontrados tras la eliminación
            self.lbl_juegos_encontrados.setText("Juegos encontrados: {}".format(self.tbl_juegos_encontrados.rowCount()))
    
    #método para editar videojuego en la bbdd
    def editar_videojuego(self):
        #instanciamos una nueva ventana para modificar en ella los datos del videojuego
        self.ventana_modificar = DialogModificarVideojuego_aplicacion()
        
        #extraemos la id de la fila seleccionada para que nos devuelva nuevamente los datos del videojuego mediante la función buscar_videojuegos_bd
        fila_seleccionada = self.tbl_juegos_encontrados.currentRow()
        texto_de_columna_id = self.tbl_juegos_encontrados.item(fila_seleccionada, 0).text()
        valores = dict()
        valores["id"] = texto_de_columna_id
        videojuego_a_editar = operaciones_bbdd.buscar_videojuegos_bd(valores)
        
        #rellenamos los campos de la nueva ventana con la información devuelta por la función buscar_videojuegos_bd
        self.ventana_modificar.ui.le_id.setText(str(videojuego_a_editar[0][0]))
        self.ventana_modificar.ui.le_titulo.setText(videojuego_a_editar[0][1])
        
        self.ventana_modificar.enlazar_metacritic()
        #indicamos que radio button debe aparecer marcado y que item del combobox señalada
        if videojuego_a_editar[0][2] in constantes.pc:
            self.ventana_modificar.ui.rb_pc.setChecked(True)
        elif videojuego_a_editar[0][2] in constantes.sega:
            self.ventana_modificar.ui.rb_sega.setChecked(True)
        elif videojuego_a_editar[0][2] in constantes.nintendo:
            self.ventana_modificar.ui.rb_nintendo.setChecked(True)
        elif videojuego_a_editar[0][2] in constantes.sony:
            self.ventana_modificar.ui.rb_sony.setChecked(True)
        elif videojuego_a_editar[0][2] in constantes.microsoft:
            self.ventana_modificar.ui.rb_microsoft.setChecked(True)
        self.ventana_modificar.ui.cmb_plataforma.setCurrentText(videojuego_a_editar[0][2])
        #seguimos rellenando los campos
        self.ventana_modificar.ui.le_genero.setText(videojuego_a_editar[0][3])
        self.ventana_modificar.ui.dspb_nota.setValue(float(videojuego_a_editar[0][4]))
        self.ventana_modificar.ui.chb_prestado.setChecked(videojuego_a_editar[0][5])
        self.ventana_modificar.ui.le_apuntes.setText(videojuego_a_editar[0][6])
        #comprobamos si el videojuego tiene imagen asociada para mostrarla en la etiqueta correspondiente
        ruta_imagen = "aplicaciones\\../imagenes/"+str(videojuego_a_editar[0][0])+".jpg"
        objeto_path = pathlib.Path(ruta_imagen)
        existe = objeto_path.is_file()
        if existe:
            pixmap = QPixmap(ruta_imagen)
            alto_label = self.ventana_modificar.ui.lbl_imagen.height()
            pixmap_redim = pixmap.scaledToHeight(alto_label)
            self.ventana_modificar.ui.lbl_imagen.setPixmap(pixmap_redim)
        
        self.ventana_modificar.show()

#la definición de la ventana en la que se cargan los datos para modificar el videojuego
class DialogModificarVideojuego_aplicacion(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = DialogModificarVideojuego.Ui_Dialog()
        self.ui.setupUi(self)
                
        #cada vez que se modifique un radio button se llama al método que modifica el combobox asociado
        self.ui.rb_pc.toggled.connect(self.mostrar_combobox_plataforma)
        self.ui.rb_sega.toggled.connect(self.mostrar_combobox_plataforma)
        self.ui.rb_nintendo.toggled.connect(self.mostrar_combobox_plataforma)
        self.ui.rb_sony.toggled.connect(self.mostrar_combobox_plataforma)
        self.ui.rb_microsoft.toggled.connect(self.mostrar_combobox_plataforma)
        
        #modificamos el link a metacritic cuando el usuario cambie el campo título
        self.ui.le_titulo.textEdited.connect(self.enlazar_metacritic)
        
        #definimos las acciones a realizar para los botones
        self.ui.btn_imagen.clicked.connect(self.seleccionar_imagen)        
        self.ui.btn_guardar.clicked.connect(self.guardar_cambios)
    
    #método para rellenar el combobox dependiendo del radio button seleccionado   
    def mostrar_combobox_plataforma(self):
        #inicializamos el combobox
        self.ui.cmb_plataforma.setEnabled(True)
        self.ui.cmb_plataforma.clear()
        #consultamos que radio buton está marcado para mostrar los elementos que correspondan en el combo
        if self.ui.rb_pc.isChecked():
            self.ui.cmb_plataforma.addItems(constantes.pc)
        elif self.ui.rb_sega.isChecked():
            self.ui.cmb_plataforma.addItems(constantes.sega)
        elif self.ui.rb_nintendo.isChecked():
            self.ui.cmb_plataforma.addItems(constantes.nintendo)
        elif self.ui.rb_sony.isChecked():
            self.ui.cmb_plataforma.addItems(constantes.sony)
        elif self.ui.rb_microsoft.isChecked():
            self.ui.cmb_plataforma.addItems(constantes.microsoft)
        #si hay mas de un elemento en el combo se mantendrá activo para afinar la selección, si solo hay un elemento se deshabilita
        if self.ui.cmb_plataforma.count() < 2:
            self.ui.cmb_plataforma.setEnabled(False)
    
    #método para habilitar hipervínculo en la etiqueta de nota cuando el usuario modifique el campo título
    def enlazar_metacritic(self):
        titulo = self.ui.le_titulo.text().replace(" ","%20")
        url_metacritic = "https://www.metacritic.com/search/game/"+titulo+"/results"
        self.ui.lbl_nota.setText("Nota ("+"<a href='"+url_metacritic+"'>Metacritic</a>): ")
        self.ui.lbl_nota.setOpenExternalLinks(True)
    
    #método para seleccionar una imagen asociada al videojuego o cambiar la que tuviera 
    def seleccionar_imagen(self):
        #abrimos ventana para selección de archivo
        archivo = QtWidgets.QFileDialog.getOpenFileName(self, "Seleccione imagen", "D:\Descargas", "*.jpg")
        #validamos si el cliente ha cerrado la ventana sin seleccionar ningún archivo para que no de error y cierre de aplicación
        if archivo[0] != "":
            #copiamos el archivo a la carpeta "temporal" como "imagen.jpg" y la redimensionamoss para mostrarla en una etiqueta de la ventana
            ruta_archivo = archivo[0]
            try:
                shutil.copy(ruta_archivo,constantes.ruta_temporal+"/imagen.jpg")
            except:
                os.makedirs(constantes.ruta_temporal)
                shutil.copy(ruta_archivo,constantes.ruta_temporal+"/imagen.jpg")
            pixmap = QPixmap(constantes.ruta_temporal+"/imagen.jpg")
            alto_label = self.ui.lbl_imagen.height()
            pixmap_redim = pixmap.scaledToHeight(alto_label)
            self.ui.lbl_imagen.setPixmap(pixmap_redim)
    
    #método para guardar los cambios realizados
    def guardar_cambios(self):
        #validamos nuevamente el campo título y género del videojuego, si no es válido lo mostramos en una etiqueta informativa
        titulo = self.ui.le_titulo.text()
        titulo_ok = validacion_videojuego.validar_titulo(titulo)
        if not titulo_ok:
            self.ui.lbl_ayuda.setText("Formato de título incorrecto")
            return
        else:
            self.ui.lbl_ayuda.clear()
        genero = self.ui.le_genero.text()
        genero_ok = validacion_videojuego.validar_genero(genero)
        if not genero_ok:
            self.ui.lbl_ayuda.setText("Formato de género incorrecto")
            return
        else:
            self.ui.lbl_ayuda.clear()
        #consultamos al usuario sobre si quiere guardar los cambios
        respuesta = QtWidgets.QMessageBox.question(self, "Alerta", "¿Estás seguro de guardar los cambios?")
        if respuesta == QtWidgets.QMessageBox.Yes:
            #creamos nuevo objeto de la clase Videojuego con todos los datos de la ventana
            videojuego_a_modificar = clases.Videojuego()
            videojuego_a_modificar.id = self.ui.le_id.text()
            videojuego_a_modificar.titulo = titulo
            videojuego_a_modificar.plataforma = self.ui.cmb_plataforma.currentText()
            videojuego_a_modificar.genero = genero
            videojuego_a_modificar.nota = self.ui.dspb_nota.value()
            if self.ui.chb_prestado.isChecked():
                videojuego_a_modificar.prestado = 1
            else:
                videojuego_a_modificar.prestado = 0
            videojuego_a_modificar.apuntes = self.ui.le_apuntes.text()
            #solicitamos la modificación en bbdd
            operaciones_bbdd.modificar_videojuego_bd(videojuego_a_modificar)
            #y la modificación de la imagen si procede
            ruta_imagen = constantes.ruta_temporal+"/imagen.jpg"
            objeto_path = pathlib.Path(ruta_imagen)
            existe = objeto_path.is_file()
            if existe:
                shutil.move(constantes.ruta_temporal+"/imagen.jpg","aplicaciones\\../imagenes/"+str(videojuego_a_modificar.id)+".jpg")
            #informamos al usuario de la modificación y cerramos la ventana 
            QtWidgets.QMessageBox.about(self, "Información", "El videojuego ha sido modificado")
            self.close()
        