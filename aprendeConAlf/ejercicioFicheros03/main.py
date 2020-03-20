'''
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
'''
def leer_fichero():
    n = int(input("Introduce un número del 1 al 10: "))
    m = int(input("Introduce otro número del 1 al 10: "))
    try:
        f = open("tabla-" + str(n) + ".txt","r")
    except:
        print("El fichero tabla-" + str(n) + ".txt no existe")
    else:
        lineas = f.readlines()
        print(lineas[m-1])
        f.close()
#end leer_fichero

leer_fichero()
print("\n¡Hecho!")
