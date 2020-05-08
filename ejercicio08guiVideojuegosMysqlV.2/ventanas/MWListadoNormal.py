# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanas/MWListadoNormal.ui'
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
        self.lbl_listado_videojuegos = QtWidgets.QLabel(self.centralwidget)
        self.lbl_listado_videojuegos.setGeometry(QtCore.QRect(10, 10, 780, 90))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_listado_videojuegos.setFont(font)
        self.lbl_listado_videojuegos.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_listado_videojuegos.setObjectName("lbl_listado_videojuegos")
        self.lbl_juegos_listados = QtWidgets.QLabel(self.centralwidget)
        self.lbl_juegos_listados.setGeometry(QtCore.QRect(10, 590, 781, 16))
        self.lbl_juegos_listados.setText("")
        self.lbl_juegos_listados.setObjectName("lbl_juegos_listados")
        self.txe_listado_videojuegos = QtWidgets.QTextEdit(self.centralwidget)
        self.txe_listado_videojuegos.setGeometry(QtCore.QRect(10, 110, 780, 471))
        self.txe_listado_videojuegos.setReadOnly(True)
        self.txe_listado_videojuegos.setObjectName("txe_listado_videojuegos")
        MainWindow.setCentralWidget(self.centralwidget)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Listado normal"))
        self.lbl_listado_videojuegos.setText(_translate("MainWindow", "Listado de Videojuegos"))
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
