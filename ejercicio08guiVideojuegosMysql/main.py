'''
Programa de gestión de los videojuegos que tengo en soporte físico (cartuchos, cds, dvds...)
@author: Pedro Laserna
'''
import sys
from PyQt5 import QtWidgets
from ventanas import ventana_principal
from modelo import operaciones, operaciones_bd
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

# Iniciamos ventana principal
ui_principal = ventana_principal.Ui_MainWindow()
ui_principal.setupUi(MainWindow)

# Definimos las acciones de los submenus y que en la barra de estado aparezcan la cantidad de registrso de la BBDD
ui_principal.subm_registrar_videojuego.triggered.connect(operaciones.mostrar_ventana_registro)
ui_principal.subm_editar_videojuego.triggered.connect(operaciones.mostrar_ventana_editar)
ui_principal.subm_listado_normal.triggered.connect(operaciones.mostrar_listado_videojuegos)
ui_principal.subm_listado_List_Widget.triggered.connect(operaciones.mostrar_listado_videojuegos_list)
ui_principal.subm_listado_Table_Widget.triggered.connect(operaciones.mostrar_listado_videojuegos_table)
ui_principal.sts_barra.showMessage("Juegos registrados: " + str(len(operaciones_bd.obtener_videojuegos_bd())))

MainWindow.show()
sys.exit(app.exec_())
