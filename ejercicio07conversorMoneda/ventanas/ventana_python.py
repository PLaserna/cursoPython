# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 422)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.botonConvertir = QtWidgets.QPushButton(self.centralwidget)
        self.botonConvertir.setGeometry(QtCore.QRect(240, 160, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.botonConvertir.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ventanas/banderas/EEUU.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonConvertir.setIcon(icon)
        self.botonConvertir.setIconSize(QtCore.QSize(35, 35))
        self.botonConvertir.setObjectName("botonConvertir")
        self.labelResultado = QtWidgets.QLabel(self.centralwidget)
        self.labelResultado.setGeometry(QtCore.QRect(50, 280, 681, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelResultado.setFont(font)
        self.labelResultado.setText("")
        self.labelResultado.setObjectName("labelResultado")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 30, 771, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labelTexto1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelTexto1.setFont(font)
        self.labelTexto1.setObjectName("labelTexto1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelTexto1)
        self.entradaEuros = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.entradaEuros.setFont(font)
        self.entradaEuros.setObjectName("entradaEuros")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.entradaEuros)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.labelTexto2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelTexto2.setFont(font)
        self.labelTexto2.setObjectName("labelTexto2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelTexto2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botonConvertir.setText(_translate("MainWindow", " Convertir"))
        self.labelTexto1.setText(_translate("MainWindow", "Introduce la cantidad de €:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Dólar Estadounidense"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Yen"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Libra Esterlina"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Franco suizo"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Dólar Australiano"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Dólar Canadiense"))
        self.labelTexto2.setText(_translate("MainWindow", "Elige la moneda a convertir:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
