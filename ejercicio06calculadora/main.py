'''
Ejercicio 05 Calculadora con TKinter
'''

from tkinter import *
from tkinter.font import Font

def escribir(tecla): # función para escribir en la pantalla y en las variables utilizadas por el programa según la tecla pulsada por el usuario
    global operacion, texto
    if operacion == "ERROR": # si la última operación ha dado error se pide que se inicialice la pantalla de la calculadora
        borrar_todo()
    elif operacion == "0" and tecla != ".": # si la primera tecla que se pulsa no es la "," para poner un decimal, se inicializa la pantalla
        borrar_todo()
    elif operacion == "" and tecla == ".": # si la primera tecla que se pulsa es la "," se concatena con un cero para poner decimales
        operacion = "0"
    operacion += tecla # se concatena la variable "operacion" con el valor correspondiente a la tecla pulsada
    texto.set(operacion) # se asigna al StringVar (lo mostrado en pantalla) la varible "operación"
# end escribir

def borrar(): # función para borrar el último caracter de la pantalla de la calculadora
    global operacion, texto
    operacion = operacion[:-1]
    if len(operacion) == 0: # si la variable operación no tiene nada entonces le asignamos "0"
        operacion = "0"
    texto.set(operacion)
# end borrar

def borrar_todo(): # función para borrar todo el texto en pantalla
    global operacion, texto
    operacion = ""
    texto.set("0") # dejamos que se muestre un "0" cuando se borra la pantalla como es habitual en las calculadoras
# end borrar_todo

def ver_resultado(): # función que a través de "eval" nos va a permitir realizar las operaciones incluidas en las variable de tipo str "operacion"
    global operacion, texto
    try: # comprobamos con "try/except" si eval nos devuelve error (p.e. /0) 
        r = str(eval(operacion))
        if "." in r and r.split(".")[1] == "0": # si el resultado de la operación es un entero no queremos que nos muestre decimales (p.e. en divisiones)
            r = r.split(".")[0]
    except:
        r = "ERROR"
    operacion = str(r) # asignamos el valor de r a la variable operacion
    texto.set(operacion) # y lo mostramos
# end ver_resultado

ventana_calc = Tk()

# definimos algunos valores comunes para los botones
ancho_boton_drcha = 8
ancho_boton_normal = 6
alto_boton_normal = 2
mi_fuente_boton = Font(family = "Arial", size = 12)

# creamos las variables para realizar las operaciones y mostrar en pantalla (StringVar) y reiniciamos con la función borrar_todo
texto = StringVar()
operacion = ""
borrar_todo()

# características de la pantalla de la calculadora
pantalla = Label(ventana_calc, textvariable = texto, bg = "light blue", bd = 3, anchor = W, font = ("System", 25), height = 1, width = 11, relief = GROOVE)
pantalla.grid(row = 0, column = 0, columnspan = 3, rowspan = 2, padx = 5, pady = 5)

# características y valores de los botones 
boton1 = Button(ventana_calc, text = "< borrar", height = 1, width = ancho_boton_drcha, justify = RIGHT, font = mi_fuente_boton, anchor = E, command = borrar)
boton1.grid(padx = 5, pady = 5, row = 0, column = 3)
boton2 = Button(ventana_calc, text = "<<< borrar", height = 1, width = ancho_boton_drcha, justify = RIGHT, font = mi_fuente_boton, anchor = E, command = borrar_todo)
boton2.grid(padx = 5, pady = 5, row = 1, column = 3)
boton3 = Button(ventana_calc, text = "7", bg = "gray99", height = alto_boton_normal, width = ancho_boton_normal, font = mi_fuente_boton, command = lambda:escribir("7"))
boton3.grid(padx = 5, pady = 5, row = 2, column = 0)
boton4 = Button(ventana_calc, text = "8", bg = "gray99", height = alto_boton_normal, width = ancho_boton_normal, font = mi_fuente_boton, command = lambda:escribir("8"))
boton4.grid(padx = 5, pady = 5, row = 2, column = 1)
boton5 = Button(ventana_calc, text = "9", bg = "gray99", height = alto_boton_normal, width = ancho_boton_normal, font = mi_fuente_boton, command = lambda:escribir("9"))
boton5.grid(padx = 5, pady = 5, row = 2, column = 2)
boton6 = Button(ventana_calc, text = "/", bg = "gray79", height = alto_boton_normal, width = ancho_boton_drcha, font = mi_fuente_boton, command = lambda:escribir("/"))
boton6.grid(padx = 5, pady = 5, row = 2, column = 3)
boton7 = Button(ventana_calc, text = "4", bg = "gray99", height = alto_boton_normal, width = ancho_boton_normal, font = mi_fuente_boton, command = lambda:escribir("4"))
boton7.grid(padx = 5, pady = 5, row = 3, column = 0)
boton8 = Button(ventana_calc, text = "5", bg = "gray99", height = alto_boton_normal, width = ancho_boton_normal, font = mi_fuente_boton, command = lambda:escribir("5"))
boton8.grid(padx = 5, pady = 5, row = 3, column = 1)
boton9 = Button(ventana_calc, text = "6", bg = "gray99", height = alto_boton_normal, width = ancho_boton_normal, font = mi_fuente_boton, command = lambda:escribir("6"))
boton9.grid(padx = 5, pady = 5, row = 3, column = 2)
boton10 = Button(ventana_calc, text = "*", bg = "gray79", height = alto_boton_normal, width = ancho_boton_drcha, font = mi_fuente_boton, command = lambda:escribir("*"))
boton10.grid(padx = 5, pady = 5, row = 3, column = 3)
boton11 = Button(ventana_calc, text = "1", bg = "gray99", height = alto_boton_normal, width = ancho_boton_normal, font = mi_fuente_boton, command = lambda:escribir("1"))
boton11.grid(padx = 5, pady = 5, row = 4, column = 0)
boton12 = Button(ventana_calc, text = "2", bg = "gray99", height = alto_boton_normal, width = ancho_boton_normal, font = mi_fuente_boton, command = lambda:escribir("2"))
boton12.grid(padx = 5, pady = 5, row = 4, column = 1)
boton13 = Button(ventana_calc, text = "3", bg = "gray99", height = alto_boton_normal, width = ancho_boton_normal, font = mi_fuente_boton, command = lambda:escribir("3"))
boton13.grid(padx = 5, pady = 5, row = 4, column = 2)
boton14 = Button(ventana_calc, text = "-", bg = "gray79", height = alto_boton_normal, width = ancho_boton_drcha, font = mi_fuente_boton, command = lambda:escribir("-"))
boton14.grid(padx = 5, pady = 5, row = 4, column = 3)
boton15 = Button(ventana_calc, text = "0", bg = "gray99", height = alto_boton_normal, width = 15, font = mi_fuente_boton, command = lambda:escribir("0"))
boton15.grid(padx = 5, pady = 5, row = 5, column = 0, columnspan = 2)
boton16 = Button(ventana_calc, text = ",", bg = "gray79", height = alto_boton_normal, width = ancho_boton_normal, font = mi_fuente_boton, command = lambda:escribir("."))
boton16.grid(padx = 5, pady = 5, row = 5, column = 2)
boton17 = Button(ventana_calc, text = "+", bg = "gray79", height = alto_boton_normal, width = ancho_boton_drcha, font = mi_fuente_boton, command = lambda:escribir("+"))
boton17.grid(padx = 5, pady = 5, row = 5, column = 3)
boton18 = Button(ventana_calc, text = "=", bg = "gray79", height = alto_boton_normal, width = 35, font = mi_fuente_boton, command = ver_resultado)
boton18.grid(padx = 5, pady = 5, row = 6, column = 0, columnspan = 4, sticky = SE)

# características de la ventana principal
ventana_calc.title("Calculadora")
ventana_calc.resizable(False, False)
ventana_calc.mainloop()
