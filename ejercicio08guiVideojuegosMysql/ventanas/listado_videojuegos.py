# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanas/listado_videojuegos.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 640)
        Dialog.setMinimumSize(QtCore.QSize(900, 640))
        Dialog.setMaximumSize(QtCore.QSize(900, 640))
        Dialog.setSizeGripEnabled(False)
        self.lbl_listado = QtWidgets.QLabel(Dialog)
        self.lbl_listado.setGeometry(QtCore.QRect(30, 30, 841, 71))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(12)
        font.setUnderline(True)
        self.lbl_listado.setFont(font)
        self.lbl_listado.setAutoFillBackground(False)
        self.lbl_listado.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_listado.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_listado.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_listado.setObjectName("lbl_listado")
        self.txt_listado = QtWidgets.QTextEdit(Dialog)
        self.txt_listado.setGeometry(QtCore.QRect(30, 130, 841, 461))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txt_listado.setFont(font)
        self.txt_listado.setObjectName("txt_listado")
        self.lbl_numero_juegos = QtWidgets.QLabel(Dialog)
        self.lbl_numero_juegos.setGeometry(QtCore.QRect(30, 590, 200, 31))
        self.lbl_numero_juegos.setText("")
        self.lbl_numero_juegos.setObjectName("lbl_numero_juegos")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Listado videojuegos"))
        self.lbl_listado.setText(_translate("Dialog", "Listado de videojuegos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
