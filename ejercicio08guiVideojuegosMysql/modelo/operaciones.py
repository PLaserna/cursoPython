import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from ventanas import introducir_videojuego, editar_videojuego, modificar_videojuego, listado_videojuegos, listado_videojuegos_list, listado_videojuegos_table
from modelo import clases, operaciones_bd

app = QtWidgets.QApplication(sys.argv)

# Definimos las ventanas que vamos a utilizar en el módulo
Dialog1 = QtWidgets.QDialog()
ui_registro_videojuego = introducir_videojuego.Ui_Dialog()
ui_registro_videojuego.setupUi(Dialog1)

Dialog2 = QtWidgets.QDialog()
ui_editar_videojuego = editar_videojuego.Ui_Dialog()
ui_editar_videojuego.setupUi(Dialog2)

Dialog3 = QtWidgets.QDialog()
ui_listado_videojuegos = listado_videojuegos.Ui_Dialog()
ui_listado_videojuegos.setupUi(Dialog3)

Dialog4 = QtWidgets.QDialog()
ui_listado_videojuegos_list = listado_videojuegos_list.Ui_Dialog()
ui_listado_videojuegos_list.setupUi(Dialog4)

Dialog5 = QtWidgets.QDialog()
ui_listado_videojuegos_table = listado_videojuegos_table.Ui_Dialog()
ui_listado_videojuegos_table.setupUi(Dialog5)

Dialog6 = QtWidgets.QDialog()
ui_modificar_videojuego = modificar_videojuego.Ui_Dialog()
ui_modificar_videojuego.setupUi(Dialog6)

# Función que crea un objeto de la clase Videojuego con los datos introducidos para posteriormente insertarlo como un nuevo registro en la BBDD
def registrar_videojuego():
    videojuego = clases.Videojuego()
    # Tomamos los valores de los distintos widgets de la ventana de registro
    videojuego.titulo = ui_registro_videojuego.lin_titulo.text()
    videojuego.plataforma = ui_registro_videojuego.lin_plataforma.text()
    videojuego.genero = ui_registro_videojuego.lin_genero.text()
    fecha = ui_registro_videojuego.cal_anyo.selectedDate()
    videojuego.anyo = str(fecha.toPyDate())
    videojuego.precio = float(ui_registro_videojuego.spb_precio.value())
    # Solicitamos la inclusión mediante sentencia INSERT de sql
    operaciones_bd.registro_videojuego_bd(videojuego)
    # Mostramos mensaje de confirmación
    QMessageBox.about(Dialog1, "Información", "Registro de nuevo videojuego completado")
    # Reinicializamos los campos de la ventana
    ui_registro_videojuego.lin_titulo.clear()
    ui_registro_videojuego.lin_plataforma.clear()
    ui_registro_videojuego.lin_genero.clear()
    ui_registro_videojuego.cal_anyo.setSelectedDate(QtCore.QDate.currentDate())
    ui_registro_videojuego.spb_precio.setValue(0)
# end registrar_videojuego

#Función que toma los valores introducidos por el usuario para realizar una busqueda en la BBDD
def buscar_videojuego():
    # Reinicializamos el widget donde se muestran los resultados, aunque el widget no puede verse hasta que no se muestran resultados
    ui_editar_videojuego.lst_videojuegos_encontrados.clear()
    # Creamos un diccionaro con el nombre de la columna y el valor facilitado por el cliente para realizar la busqueda
    valores = dict()
    valores["id"] = ui_editar_videojuego.lin_id.text()
    valores["titulo"] = ui_editar_videojuego.lin_titulo.text()
    valores["plataforma"] = ui_editar_videojuego.lin_plataforma.text()
    valores["genero"] = ui_editar_videojuego.lin_genero.text()
    valores["precio"] = ui_editar_videojuego.lin_precio.text()
    # lanzamos la busqueda con los valores obtenidos de la ventana
    videojuegos = operaciones_bd.buscar_videojuegos_bd(valores)
    # Comprobamos si hay resultado de la busqueda, si no los hay se deshabilitan los botones de editar y borrar registro y se muestra mensaje
    if len(videojuegos) == 0:
        ui_editar_videojuego.btn_borrar_videojuego.setEnabled(False)
        ui_editar_videojuego.btn_editar_videojuego.setEnabled(False)
        QMessageBox.about(Dialog2, "Información", "No se ha encontrado ningún videojuego")
    else:
        # Si hay resultados se recorren para mostrarlos en un ListWidget
        for v in videojuegos:
            texto = ""
            texto += "Id: " + str(v[0]) + " - Titulo: " + v[1] + "\n"
            texto += "Plataforma: " + v[2] + " - Género: " + v[3]
            texto += " - Año: " + str(v[4]) + " - Precio: " + str(v[5]) + "\n"
            texto += " ********** "
            ui_editar_videojuego.lst_videojuegos_encontrados.addItem(texto)
        # Ampliamos la ventana para que se muestren los resultados
        Dialog2.setMinimumSize(QtCore.QSize(562, 843))
        Dialog2.setMaximumSize(QtCore.QSize(562, 843))
    # Indicamoss en una etiqueta los registros encontrados tras la busqueda
    ui_editar_videojuego.lbl_numero_juegos.setText("Juegos encontrados: " + str(ui_editar_videojuego.lst_videojuegos_encontrados.count()))
# end buscar_videojuego

# Función para el borrado de un registro
def borrar_videojuego():
    # Con esta línea tomamos el texto del registro seleccionado y se elimina de la lista de resultados
    texto_del_item_seleccionado = ui_editar_videojuego.lst_videojuegos_encontrados.takeItem(ui_editar_videojuego.lst_videojuegos_encontrados.currentRow()).text()
    # Cogemos solo la clave primaria (id) del registro que queremos borrar
    id_a_borrar = (texto_del_item_seleccionado.split()[1],)
    # Solicitamos el borrado mediante la función con la instrucción sql
    operaciones_bd.borrar_videojuego_bd(id_a_borrar)
    # Mostramos mensaje de confirmación
    QMessageBox.about(Dialog2, "Información", "El videojuego ha sido borrado")
    # Actualizamos el número de registros encontrados tras el borrado de uno de ellos
    ui_editar_videojuego.lbl_numero_juegos.setText("Juegos encontrados: " + str(ui_editar_videojuego.lst_videojuegos_encontrados.count()))
# end borrar_videojuego

# Función para modificar los datos de un videojuego
def editar_videojuego():
    # Creamos una lista en la que vamos a almacenar todos los datos modificados por el usuario
    videojuego_modificado = []
    videojuego_modificado.append(ui_modificar_videojuego.lin_titulo.text())
    videojuego_modificado.append(ui_modificar_videojuego.lin_plataforma.text())
    videojuego_modificado.append(ui_modificar_videojuego.lin_genero.text())
    fecha = ui_modificar_videojuego.cal_anyo.selectedDate()
    videojuego_modificado.append(str(fecha.toPyDate()))
    videojuego_modificado.append(float(ui_modificar_videojuego.spb_precio.value()))
    videojuego_modificado.append(ui_modificar_videojuego.lin_id.text())
    # Transformamos la lista en tupla para que podamos facilitarla en la instrucción sql
    valores = tuple(videojuego_modificado)
    # Solicitamos el UPDATE a la BBDD
    operaciones_bd.modificar_videojuego_bd(valores)
    # Mostramos mensaje informativo y cerramos la ventana de modificación de los datos del videojuego
    QMessageBox.about(Dialog6, "Información", "El videojuego ha sido modificado")
    Dialog6.close()
# end editar_videojuego

# Función para activar los botones de "editar" y "borrar" una vez que se ha seleccionado el registro a borrar
def activar_botones():
    ui_editar_videojuego.btn_borrar_videojuego.setEnabled(True)
    ui_editar_videojuego.btn_editar_videojuego.setEnabled(True)
# end activar_botones

# Función para borrar los datos del formulario de busqueda. Se invoca mediante un botón específico
def borrar_formulario():
    ui_editar_videojuego.lin_id.clear()
    ui_editar_videojuego.lin_titulo.clear()
    ui_editar_videojuego.lin_plataforma.clear()
    ui_editar_videojuego.lin_genero.clear()
    ui_editar_videojuego.lin_precio.clear()
    ui_editar_videojuego.lst_videojuegos_encontrados.clear()
    # También redimensiona de nuevo la ventana
    Dialog2.setMinimumSize(QtCore.QSize(562, 350))
    Dialog2.setMaximumSize(QtCore.QSize(562, 350))
# end borrar_formulario

# Función para mostrar la ventana de registro de un nuevo videojuego
def mostrar_ventana_registro():
    ui_registro_videojuego.btn_registrar_videojuego.clicked.connect(registrar_videojuego)
    Dialog1.show()
# end mostrar_ventana_registro

# Función para mostrar la ventana de busqueda de videojuego que posteriormente permite la edición o borrado de los registros encontrados
def mostrar_ventana_editar():
    ui_editar_videojuego.btn_buscar_videojuego.clicked.connect(buscar_videojuego)
    ui_editar_videojuego.btn_borrar_videojuego.clicked.connect(borrar_videojuego)
    ui_editar_videojuego.btn_editar_videojuego.clicked.connect(mostrar_ventana_modificar_datos)
    ui_editar_videojuego.btn_limpiar_formulario.clicked.connect(borrar_formulario)
    # Cuando se selecciona algún registro de los encontrados tras la busqueda se habilitan los botones de editar y borrar
    ui_editar_videojuego.lst_videojuegos_encontrados.itemSelectionChanged.connect(activar_botones)
    Dialog2.show()
    # Borramos el formulario para que si se vuelve a invocar esta ventana aparezca vacio
    borrar_formulario()
# end mostrar_ventana_editar

# Función para mostrar la ventana con los datos del videojuego seleccionado para que el usuario los modifique
def mostrar_ventana_modificar_datos():
    # Utilizamos varios métodos para extraer la clave primaria del registro seleccionado 
    texto_del_item_seleccionado = ui_editar_videojuego.lst_videojuegos_encontrados.item(ui_editar_videojuego.lst_videojuegos_encontrados.currentRow()).text()
    valores = dict()
    valores["id"] = texto_del_item_seleccionado.split()[1]
    # Una vez extraida la clave primaria invocamos la función buscar_videojuegos_bd para que muestre al usuario el resto de valores y los modifique
    videojuego_a_editar = operaciones_bd.buscar_videojuegos_bd(valores)
    # La id no debe modificarla, por lo que se muestra al usuario pero se deshabilita el campo
    ui_modificar_videojuego.lin_id.setEnabled(True)
    ui_modificar_videojuego.lin_id.setText(str(videojuego_a_editar[0][0]))
    ui_modificar_videojuego.lin_id.setEnabled(False)
    ui_modificar_videojuego.lin_titulo.setText(videojuego_a_editar[0][1])
    ui_modificar_videojuego.lin_plataforma.setText(videojuego_a_editar[0][2])
    ui_modificar_videojuego.lin_genero.setText(videojuego_a_editar[0][3])
    ui_modificar_videojuego.spb_precio.setValue(videojuego_a_editar[0][5])
    ui_modificar_videojuego.cal_anyo.setSelectedDate(videojuego_a_editar[0][4])
    # Una vez que el usuario ha hecho los cambios, si pulsa el botón las modificaciones se realizarán mediante la función editar_videojuego
    ui_modificar_videojuego.btn_modificar_videojuego.clicked.connect(editar_videojuego)
    Dialog6.show()
# end mostrar_ventana_modificar_datos

# Función que muestra el listado de videojuegos registrados en la BBDD mediante un widget TextEdit 
def mostrar_listado_videojuegos():
    videojuegos = operaciones_bd.obtener_videojuegos_bd()
    texto = ""
    # Recorremos los resultados para mostrarlos mas visualmente al usuario
    for v in videojuegos:
        texto += "Id: " + str(v[0]) + " - Titulo: " + v[1] + "\n"
        texto += "Plataforma: " + v[2] + " - Género: " + v[3]
        texto += " - Año: " + str(v[4]) + " - Precio: " + str(v[5]) + "\n"
        texto += " ********** \n"
    ui_listado_videojuegos.txt_listado.setText(texto)
    # Mostramos en una etiqueta el número de registros recuperados
    ui_listado_videojuegos.lbl_numero_juegos.setText("Juegos listados: " + str(len(videojuegos)))
    Dialog3.show()
# end mostrar_listado_videojuegos

# Función que muestra el listado de videojuegos registrados en la BBDD mediante un widget List
def mostrar_listado_videojuegos_list():
    videojuegos = operaciones_bd.obtener_videojuegos_bd()
    # Recorremos los resultados para mostrarlos mas visualmente al usuario
    for v in videojuegos:
        texto = ""
        texto += "Id: " + str(v[0]) + " - Titulo: " + v[1] + "\n"
        texto += "Plataforma: " + v[2] + " - Género: " + v[3]
        texto += " - Año: " + str(v[4]) + " - Precio: " + str(v[5]) + "\n"
        texto += " ********** "
        # Vamos añadiendo un item al ListWidget por cada registro recuperado
        ui_listado_videojuegos_list.lst_listado.addItem(texto)
    # Mostramos en una etiqueta el número de registros recuperados
    ui_listado_videojuegos_list.lbl_numero_juegos.setText("Juegos listados: " + str(len(videojuegos)))
    Dialog4.show()
# end mostrar_listado_videojuegos_list()

# Función que muestra el listado de videojuegos registrados en la BBDD mediante un widget Table
def mostrar_listado_videojuegos_table():
    videojuegos = operaciones_bd.obtener_videojuegos_bd()
    fila = 0
    # Mediante dos For anidados vamos creando la tabla añadiendo una fila por cada registro y una columna por cada campo del registro
    for videojuego in videojuegos:
        columna = 0
        ui_listado_videojuegos_table.tbl_listado.insertRow(fila)
        for campo in videojuego:
            celda = QTableWidgetItem(str(campo))
            ui_listado_videojuegos_table.tbl_listado.setItem(fila, columna, celda)
            columna += 1
        fila += 1
    # Mostramos en una etiqueta el número de registros recuperados
    ui_listado_videojuegos_table.lbl_numero_juegos.setText("Juegos listados: " + str(len(videojuegos)))
    Dialog5.show()
# end mostrar_listado_videojuegos_table
