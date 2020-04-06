# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanas/listado_videojuegos_table.ui'
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
        self.tbl_listado = QtWidgets.QTableWidget(Dialog)
        self.tbl_listado.setGeometry(QtCore.QRect(30, 130, 841, 461))
        self.tbl_listado.setObjectName("tbl_listado")
        self.tbl_listado.setColumnCount(6)
        self.tbl_listado.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_listado.setHorizontalHeaderItem(5, item)
        self.lbl_numero_juegos = QtWidgets.QLabel(Dialog)
        self.lbl_numero_juegos.setGeometry(QtCore.QRect(30, 590, 200, 31))
        self.lbl_numero_juegos.setText("")
        self.lbl_numero_juegos.setObjectName("lbl_numero_juegos")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Listado videojuegos"))
        self.lbl_listado.setText(_translate("Dialog", "Listado de videojuegos (Table Widget)"))
        item = self.tbl_listado.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Id."))
        item = self.tbl_listado.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Título"))
        item = self.tbl_listado.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Plataforma"))
        item = self.tbl_listado.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Género"))
        item = self.tbl_listado.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Año"))
        item = self.tbl_listado.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Precio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
