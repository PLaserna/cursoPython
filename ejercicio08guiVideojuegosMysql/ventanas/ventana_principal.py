# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanas/ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 666)
        MainWindow.setMinimumSize(QtCore.QSize(802, 666))
        MainWindow.setMaximumSize(QtCore.QSize(802, 666))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_titulo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(14)
        font.setUnderline(True)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.verticalLayout.addWidget(self.lbl_titulo)
        self.lbl_imagen_portada = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagen_portada.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_imagen_portada.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_imagen_portada.setText("")
        self.lbl_imagen_portada.setPixmap(QtGui.QPixmap("ventanas\\../imagenes/videojuegos_780x470.jpg"))
        self.lbl_imagen_portada.setObjectName("lbl_imagen_portada")
        self.verticalLayout.addWidget(self.lbl_imagen_portada)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 26))
        self.menubar.setObjectName("menubar")
        self.menu_videojuegos = QtWidgets.QMenu(self.menubar)
        self.menu_videojuegos.setObjectName("menu_videojuegos")
        self.subm_listar_videojuegos = QtWidgets.QMenu(self.menu_videojuegos)
        self.subm_listar_videojuegos.setObjectName("subm_listar_videojuegos")
        MainWindow.setMenuBar(self.menubar)
        self.sts_barra = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sts_barra.setFont(font)
        self.sts_barra.setSizeGripEnabled(False)
        self.sts_barra.setObjectName("sts_barra")
        MainWindow.setStatusBar(self.sts_barra)
        self.subm_registrar_videojuego = QtWidgets.QAction(MainWindow)
        self.subm_registrar_videojuego.setObjectName("subm_registrar_videojuego")
        self.subm_listado_normal = QtWidgets.QAction(MainWindow)
        self.subm_listado_normal.setObjectName("subm_listado_normal")
        self.subm_listado_List_Widget = QtWidgets.QAction(MainWindow)
        self.subm_listado_List_Widget.setObjectName("subm_listado_List_Widget")
        self.subm_listado_Table_Widget = QtWidgets.QAction(MainWindow)
        self.subm_listado_Table_Widget.setObjectName("subm_listado_Table_Widget")
        self.subm_editar_videojuego = QtWidgets.QAction(MainWindow)
        self.subm_editar_videojuego.setObjectName("subm_editar_videojuego")
        self.subm_modificar_videojuego = QtWidgets.QAction(MainWindow)
        self.subm_modificar_videojuego.setObjectName("subm_modificar_videojuego")
        self.subm_listar_videojuegos.addAction(self.subm_listado_normal)
        self.subm_listar_videojuegos.addAction(self.subm_listado_List_Widget)
        self.subm_listar_videojuegos.addAction(self.subm_listado_Table_Widget)
        self.menu_videojuegos.addAction(self.subm_registrar_videojuego)
        self.menu_videojuegos.addAction(self.subm_editar_videojuego)
        self.menu_videojuegos.addSeparator()
        self.menu_videojuegos.addAction(self.subm_listar_videojuegos.menuAction())
        self.menubar.addAction(self.menu_videojuegos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inicio"))
        self.lbl_titulo.setText(_translate("MainWindow", "Aplicación de gestión de videojuegos en formato físico\n"
"(Usando PyQt5)"))
        self.menu_videojuegos.setTitle(_translate("MainWindow", "Videojuegos"))
        self.subm_listar_videojuegos.setTitle(_translate("MainWindow", "Listar videojuegos"))
        self.subm_registrar_videojuego.setText(_translate("MainWindow", "Registrar videojuego"))
        self.subm_listado_normal.setText(_translate("MainWindow", "Listado normal"))
        self.subm_listado_List_Widget.setText(_translate("MainWindow", "Listado (List Widget)"))
        self.subm_listado_Table_Widget.setText(_translate("MainWindow", "Listado (Table Widget)"))
        self.subm_editar_videojuego.setText(_translate("MainWindow", "Borrar / Editar videojuego"))
        self.subm_modificar_videojuego.setText(_translate("MainWindow", "Modificar videojuego"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
