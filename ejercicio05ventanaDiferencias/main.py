'''
ejemplo de un juego basado en ventanas con tkinter.
Para mostrar un ejemplo sobre eventos y diferentes componentes visuales
'''
import time
from tkinter import *
from tkinter import messagebox

# tkinter está disponible por defecto en python. Otro recurso muy usado es pyQt5

x = 0
y = 0
aciertos = [False, False, False, False, False] # creo una lista para contabilizar si el usuario acierta las 5 diferencias
pendientes = 5 # variable para mostrar el número de diferencias pendientes de acertar
top_10 = [] # para guardar y ordenar los mejores tiempos
nombre = ""
puntuaciones = ""
nuevo_record = None
tiempo_tardado = None

class Record(): # para guardar en la lista top_10 y poder ordenar por el campo 'tiempo'
    tiempo = 0.0
    nombre = ""

    def __init__(self, tiempo, nombre):
        self.tiempo = tiempo
        self.nombre = nombre
# end Record

def guardar_nombre(): # función para cuando se pulsa el botón para guardar el nombre del jugador. Valida si no ha metido ningún carácter
    global nombre
    nombre = e.get()
    if nombre == "":
        messagebox.showwarning("Error", "Por favor, introduce tu nombre")
    else:
        ventana_nombre.destroy()
# end guardar_nombre

def click_raton(evento): # función para verificar si se ha pinchado en alguna diferencia. Llama a su vez a la función 'comprobar_acierto'
    global x, y, pendientes
    # se pone global para poder usar las variables 'x', 'y' y 'pendiente' definidas fuera de la función
    x = evento.x
    y = evento.y
    print("x: " + str(x))
    print("y: " + str(y))
    if x >= 1048 and x <= 1122 and y >= 117 and y <= 171:
        comprobar_acierto(0)
    elif x >= 1359 and x <= 1445 and y >= 0 and y <= 47:
        comprobar_acierto(1)
    elif x >= 1519 and x <= 1594 and y >= 277 and y <= 345:
        comprobar_acierto(2)
    elif x >= 1732 and x <= 1799 and y >= 130 and y <= 193:
        comprobar_acierto(3)
    elif x >= 1614 and x <= 1693 and y >= 387 and y <= 432:
        comprobar_acierto(4)
    else:
        print("Ahí no hay ninguna diferencia")
#end click_raton

def comprobar_acierto(i): # verifica si se han acertado todas las diferencias y avisa de las que queden pendientes. Se pasa el parámetro 'i' para
    #identificar cual de las cinco áreas se debe comprobar (sirviendo de índice para la lista 'aciertos')
    global pendientes, tiempo_tardado, nuevo_record, nombre, puntuaciones
    if aciertos[i] != True:
        aciertos[i] = True
        pendientes -= 1
        if pendientes > 0:
            print("Felicidades, adivinaste una diferencia. Te quedan " + str(pendientes) + " diferencias por adivinar")
        else:
            tfin = time.time()
            tiempo_tardado = tfin - tini # si ha adivinado todas las diferencias obtenemos el tiempo empleado ('tiempo_tardado') y lo mostramos
            messagebox.showinfo("¡Enhorabuena!", "Has encontrado todas las diferencias. \nTu tiempo ha sido: " + str(tiempo_tardado))
            fichero = open("puntuaciones.txt")
            for linea in fichero.readlines(): # leemos el fichero de las mejores puntuaciones para volcarlo en la lista 'top_10'
                top_10.append(Record(float(linea.split(";")[0]),str(linea.split(";")[1]))) # creamos un objeto Record guardando por separado 
                # (con split) los campos 'nombre' y 'tiempo' 
            fichero.close()
            top_10.sort(key=lambda nuevo_record : nuevo_record.tiempo) # ordenamos 'top_10' por el campo 'tiempo'
            if len(top_10) < 10 or tiempo_tardado < top_10[-1].tiempo: # una vez ordenado 'top_10' comprobamos si hay menos de 10 registros (solo
                # queremos guardar los 10 mejores) o si el nuevo tiempo es mejor que el peor incluido en 'top_10'
                nuevo_record = Record(tiempo_tardado,nombre+"\n") # si se cumplen las condiciones creamos un nuevo Record para guardarlo en 'top_10'
                top_10.append(nuevo_record)
                top_10.sort(key=lambda nuevo_record : nuevo_record.tiempo) # volvemos a ordenar la lista por 'tiempo'
                print("¡Has entrado en el top 10!\n") # avisamos por consola si se ha conseguido alguno de los 10 mejores tiempos
                fichero = open("puntuaciones.txt", "w") # sobreescribimos el fichero 'puntuaciones' ya que vamos a insertar las puntuaciones ordenadas
                # tras los cambios
                c = 0
                for puntuacion in top_10:
                    c += 1
                    if c <= 10: # grabamos nuevamente en el fichero únicamente los 10 mejores tiempos de 'top_10' 
                        fichero.write(str(puntuacion.tiempo) + ";" + puntuacion.nombre)
                fichero.close()
                fichero = open("puntuaciones.txt")
                c = 0
                puntuaciones = ""
                for linea in fichero.readlines(): # si se ha conseguido record mostramos también por consola los mejores tiempos incluido el último
                    c += 1
                    puntuaciones += str(c) + " - Tiempo: " + linea.split(";")[0] + " | Nombre: " + linea.split(";")[1] + "\n"
                fichero.close()
                print(puntuaciones)
            else:
                print("No has batido record") # avisamos por consola si no se ha conseguido record
    else:
        print("Esa diferencia ya la habías adivinado")
#end comprobar_acierto

try:
    fichero = open("puntuaciones.txt") # comprobamos si existe fichero de puntuaciones creado
    i = 0
    for linea in fichero.readlines(): # si existe lo listamos
        i += 1
        puntuaciones += str(i) + " - Tiempo: " + linea.split(";")[0] + " | Nombre: " + linea.split(";")[1] + "\n"
except:
    fichero = open("puntuaciones.txt", "x") # si no existe lo creamos
    puntuaciones = "SIN PUNTUACIONES REGISTRADAS..."
finally:
    fichero.close()

ventana_nombre = Tk() # ventana para que el usuario introduzca su nombre y vea el listado de mejores tiempos (si los hay)
canvas1 = Canvas(ventana_nombre)
canvas1.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady = 3, sticky = E+W)
l1 = Label(canvas1, text = puntuaciones, bg = "white", bd = 3, width = 60, height = 19, justify = LEFT, anchor = NW, font = "Arial 13 italic")
l1.grid(padx = 3, pady = 3, sticky = N+W)
l2 = Label(ventana_nombre, text = "Introduce nombre para registrar tu tiempo:")
l2.grid(padx = 5, pady = 5, row = 1, column = 0)
e = Entry(ventana_nombre, bd=5)
e.grid(padx = 5, pady = 5, row = 1, column = 1)
e.focus()
b = Button(ventana_nombre, text = "Aceptar", command = guardar_nombre)
b.grid(padx = 5, pady = 5, row = 2, column = 0, columnspan = 2, sticky = S+N+E+W)
ventana_nombre.title("Mejores puntuaciones")
ventana_nombre.mainloop()

ventana = Tk() # ventana del juego en el que se cargará la imagen
canvas2 = Canvas(ventana, width = 800, height = 600)
canvas2.pack(expand = YES, fill = BOTH)
imagen = PhotoImage(file = "imagen.png")
canvas2.create_image(0,0,image = imagen, anchor = NW)
ventana.geometry("1815x605")
ventana.title("Haz click en las diferencias de la imagen de la derecha")
messagebox.showinfo("Instrucciones", """Busca y haz click en las cinco diferencias de la imagen de la derecha. 
El tiempo comenzará a contar en cuanto pulses el botón de 'Aceptar'.""")
tini = time.time()
ventana.bind("<Button 1>",click_raton)
ventana.mainloop()
