'''
Módulo correspondiente a la ventana de Portada de la aplicación
@author: Pedro Laserna
'''

from ventanas import MWPortada
from aplicaciones import MWAnadirVideojuego_aplicacion, MWBuscarVideojuego_aplicacion
from aplicaciones import MWListadoNormal_aplicacion, MWListadoListWidget_aplicacion, MWListadoTableWidget_aplicacion
from modelo import operaciones_bbdd

class MainWindow_portada(MWPortada.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        
        #definimos las acciones de los menus y submenus
        self.subm_anadir_videjuego.triggered.connect(self.mostrar_anadir_videojuego)
        self.subm_editar_videojuego.triggered.connect(self.mostrar_buscar_videojuego)
        self.subm_borrar_videojuego.triggered.connect(self.mostrar_buscar_videojuego)
        self.subm_listado_normal.triggered.connect(self.mostrar_listado_normal)
        self.subm_listado_list_widget.triggered.connect(self.mostrar_listado_list_widget)
        self.subm_listado_table_widget.triggered.connect(self.mostrar_listado_table_widget)
        #indicamos en etiqueta la cantidad de juegos registrados en la bbdd mediante la función obtener_videojuegos_bd
        self.lbl_juegos_registrados.setText("Juegos registrados: {}".format(len(operaciones_bbdd.obtener_videojuegos_bd())))
        self.MainWindow = MainWindow
    
    #mostramos las distintas ventanas de la aplicación mediante los menús
    def mostrar_anadir_videojuego(self):
        self.VentanaAnadirVideojuego = MWAnadirVideojuego_aplicacion.MainWindow_anadir_videojuego()
        self.VentanaAnadirVideojuego.setupUi(self.MainWindow)
    
    def mostrar_buscar_videojuego(self):
        self.VentanaBuscarVideojuego = MWBuscarVideojuego_aplicacion.MainWindow_buscar_videojuego()
        self.VentanaBuscarVideojuego.setupUi(self.MainWindow)
    
    def mostrar_listado_normal(self):
        self.VentanaListadoNormal = MWListadoNormal_aplicacion.MainWindow_listado_normal()
        self.VentanaListadoNormal.setupUi(self.MainWindow)
        
    def mostrar_listado_list_widget(self):
        self.VentanaListadoListWidget = MWListadoListWidget_aplicacion.MainWindow_listado_list_widget()
        self.VentanaListadoListWidget.setupUi(self.MainWindow)
        
    def mostrar_listado_table_widget(self):
        self.VentanaListadoTableWidget = MWListadoTableWidget_aplicacion.MainWindow_listado_table_widget()
        self.VentanaListadoTableWidget.setupUi(self.MainWindow)
               