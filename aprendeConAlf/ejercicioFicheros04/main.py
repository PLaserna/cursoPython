'''
Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.
'''
from urllib import request

def leer_fichero_internet():
    f = request.urlopen('https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md')
    datos = f.read()
    palabras = datos.decode('utf-8').split()
    print(palabras)
    print("Hay " + str(len(palabras)) + " palabras")
    f.close()
#end leer_fichero_internet

leer_fichero_internet()
print("\n¡Hecho!")
