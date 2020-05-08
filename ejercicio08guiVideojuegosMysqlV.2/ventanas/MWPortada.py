# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanas/MWPortada.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 640)
        MainWindow.setMinimumSize(QtCore.QSize(800, 640))
        MainWindow.setMaximumSize(QtCore.QSize(800, 640))
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ventanas\\imagenes_ventanas/mando.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_imagen_portada = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagen_portada.setGeometry(QtCore.QRect(10, 110, 780, 470))
        self.lbl_imagen_portada.setText("")
        self.lbl_imagen_portada.setPixmap(QtGui.QPixmap("ventanas\\imagenes_ventanas/portada_780x470.jpg"))
        self.lbl_imagen_portada.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_imagen_portada.setObjectName("lbl_imagen_portada")
        self.lbl_texto_portada = QtWidgets.QLabel(self.centralwidget)
        self.lbl_texto_portada.setGeometry(QtCore.QRect(10, 10, 780, 90))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_texto_portada.setFont(font)
        self.lbl_texto_portada.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_texto_portada.setObjectName("lbl_texto_portada")
        self.lbl_juegos_registrados = QtWidgets.QLabel(self.centralwidget)
        self.lbl_juegos_registrados.setGeometry(QtCore.QRect(10, 590, 781, 16))
        self.lbl_juegos_registrados.setText("")
        self.lbl_juegos_registrados.setObjectName("lbl_juegos_registrados")
        MainWindow.setCentralWidget(self.centralwidget)
        self.mbar_videojuegos = QtWidgets.QMenuBar(MainWindow)
        self.mbar_videojuegos.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.mbar_videojuegos.setObjectName("mbar_videojuegos")
        self.menu_videojuegos = QtWidgets.QMenu(self.mbar_videojuegos)
        self.menu_videojuegos.setObjectName("menu_videojuegos")
        self.menu_listar_videojuegos = QtWidgets.QMenu(self.menu_videojuegos)
        self.menu_listar_videojuegos.setObjectName("menu_listar_videojuegos")
        MainWindow.setMenuBar(self.mbar_videojuegos)
        self.subm_anadir_videjuego = QtWidgets.QAction(MainWindow)
        self.subm_anadir_videjuego.setObjectName("subm_anadir_videjuego")
        self.subm_editar_videojuego = QtWidgets.QAction(MainWindow)
        self.subm_editar_videojuego.setObjectName("subm_editar_videojuego")
        self.subm_borrar_videojuego = QtWidgets.QAction(MainWindow)
        self.subm_borrar_videojuego.setObjectName("subm_borrar_videojuego")
        self.subm_listado_normal = QtWidgets.QAction(MainWindow)
        self.subm_listado_normal.setObjectName("subm_listado_normal")
        self.subm_listado_list_widget = QtWidgets.QAction(MainWindow)
        self.subm_listado_list_widget.setObjectName("subm_listado_list_widget")
        self.subm_listado_table_widget = QtWidgets.QAction(MainWindow)
        self.subm_listado_table_widget.setObjectName("subm_listado_table_widget")
        self.menu_listar_videojuegos.addAction(self.subm_listado_normal)
        self.menu_listar_videojuegos.addAction(self.subm_listado_list_widget)
        self.menu_listar_videojuegos.addAction(self.subm_listado_table_widget)
        self.menu_videojuegos.addAction(self.subm_anadir_videjuego)
        self.menu_videojuegos.addAction(self.subm_editar_videojuego)
        self.menu_videojuegos.addAction(self.subm_borrar_videojuego)
        self.menu_videojuegos.addSeparator()
        self.menu_videojuegos.addAction(self.menu_listar_videojuegos.menuAction())
        self.mbar_videojuegos.addAction(self.menu_videojuegos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Portada"))
        self.lbl_texto_portada.setText(_translate("MainWindow", "Gestión de Videojuegos en formato físico\n"
"(Utilizando PyQt5)"))
        self.menu_videojuegos.setTitle(_translate("MainWindow", "Videojuegos"))
        self.menu_listar_videojuegos.setTitle(_translate("MainWindow", "Listar Videojuegos"))
        self.subm_anadir_videjuego.setText(_translate("MainWindow", "Añadir Videojuego"))
        self.subm_editar_videojuego.setText(_translate("MainWindow", "Editar Videojuego"))
        self.subm_borrar_videojuego.setText(_translate("MainWindow", "Borrar Videojuego"))
        self.subm_listado_normal.setText(_translate("MainWindow", "Listado Normal"))
        self.subm_listado_list_widget.setText(_translate("MainWindow", "Listado (List Widget)"))
        self.subm_listado_table_widget.setText(_translate("MainWindow", "Listado (Table Widget)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
