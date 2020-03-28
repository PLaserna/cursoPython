
# vamos a usar el archivo generado de la ventana directamente
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_python
import sys

# función que ejecuta la conversión de moneda dependiendo de la moneda escogida en el combo. Por defecto el dólar estadounidense 
def conversion():
    introducido = ui.entradaEuros.text().replace(",",".")
    if introducido.replace(".","").isnumeric():
        introducido_float = float(introducido.replace(",","."))
        if ui.comboBox.currentIndex() == 0:
            moneda_conv = introducido_float * 1.11
        elif ui.comboBox.currentIndex() == 1:
            moneda_conv = introducido_float * 120.50
        elif ui.comboBox.currentIndex() == 2:
            moneda_conv = introducido_float * 0.89
        elif ui.comboBox.currentIndex() == 3:
            moneda_conv = introducido_float * 1.06
        elif ui.comboBox.currentIndex() == 4:
            moneda_conv = introducido_float * 1.81
        elif ui.comboBox.currentIndex() == 5:
            moneda_conv = introducido_float * 1.56
        else:
            print("ERROR")
        ui.labelResultado.setText("Resultado en " + ui.comboBox.currentText() + ": " + "{:.2f}".format(moneda_conv).replace(".",","))
    else:
        ui.labelResultado.setText("Debe introducir un valor numérico")
# end conversion

# función que se encarga de cambiar el icono del botonConvertir al seleccionar otra moneda en el combo
def cambiar_icono():
    icon = QtGui.QIcon()
    if ui.comboBox.currentIndex() == 0:
        icon.addPixmap(QtGui.QPixmap("ventanas/banderas/EEUU.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.botonConvertir.setIcon(icon)
        ui.botonConvertir.setIconSize(QtCore.QSize(35, 35))
    elif ui.comboBox.currentIndex() == 1:
        icon.addPixmap(QtGui.QPixmap("ventanas/banderas/japon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.botonConvertir.setIcon(icon)
        ui.botonConvertir.setIconSize(QtCore.QSize(35, 35))
    elif ui.comboBox.currentIndex() == 2:
        icon.addPixmap(QtGui.QPixmap("ventanas/banderas/RU.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.botonConvertir.setIcon(icon)
        ui.botonConvertir.setIconSize(QtCore.QSize(35, 35))
    elif ui.comboBox.currentIndex() == 3:
        icon.addPixmap(QtGui.QPixmap("ventanas/banderas/suiza.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.botonConvertir.setIcon(icon)
        ui.botonConvertir.setIconSize(QtCore.QSize(35, 35))
    elif ui.comboBox.currentIndex() == 4:
        icon.addPixmap(QtGui.QPixmap("ventanas/banderas/australia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.botonConvertir.setIcon(icon)
        ui.botonConvertir.setIconSize(QtCore.QSize(35, 35))
    elif ui.comboBox.currentIndex() == 5:
        icon.addPixmap(QtGui.QPixmap("ventanas/banderas/canada.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.botonConvertir.setIcon(icon)
        ui.botonConvertir.setIconSize(QtCore.QSize(35, 35))
    else:
        print("ERROR")  
# end cambiar_icono
    
# linea obligatoria para usar pyqt5
app = QtWidgets.QApplication(sys.argv)

# se prepara un MainWindow de pyqt5, esto sería parte del código recomendado de pyqt5
MainWindow = QtWidgets.QMainWindow()

# así crea un objeto de la clase en el archivo generado y lo usa para preparar la ventana principal llamada MainWindow
#para que tenga todo lo que pusimos en el designer
ui = ventana_python.Ui_MainWindow()
ui.setupUi(MainWindow)

# todos los componentes puestos en la ventana por el designer están ui
ui.botonConvertir.clicked.connect(conversion)
ui.comboBox.currentIndexChanged.connect(cambiar_icono)

# se muestra la ventana principal de pyqt5
MainWindow.show()
sys.exit(app.exec_())
