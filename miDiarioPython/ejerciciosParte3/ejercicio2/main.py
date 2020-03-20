'''
Escribe un programa que te permita jugar a una versión simplificada del juego Master Mind. El juego consistirá en adivinar una cadena de números 
distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras). Después el programa debe ir pidiendo que intentes 
adivinar la cadena de números. En cada intento, el programa informará de cuántos números han sido acertados (el programa considerará que se ha 
acertado un número si coincide el valor y la posición).
'''

import random

def comprobar_long():
    print("Dime la longitud de la cadena: ")
    while True:
            introducido = input()
            if introducido.isnumeric():
                introducido_int = int(introducido)
                if introducido_int < 2 or introducido_int > 9:
                    print("Debes introducir un número del 2 al 9: ")
                else:
                    return introducido_int
            else:
                print("Debes introducir un número del 2 al 9: ")
# end comprobar_long

def generar_cadena(long_cadena):
    cadena = []
    for valor in range(long_cadena):
        cadena.insert(valor, random.randint(1,9))
    return cadena
# end generar_cadena

def comprobar_intento():
    global intento_introducido
    intento_lista_int = []
    intento_introducido = input()
    while len(intento_lista_int) != long_cadena:
        for valor in intento_introducido:
            if valor.isnumeric():
                if int(valor) < 1 or int(valor) > 9 or len(intento_introducido) != len(cadena):
                    print("Debes introducir " + str(long_cadena) + " números del 1 al 9: ")
                    intento_introducido = input()
                    break
                else:
                    intento_lista_int.append(int(valor))
            else:
                print("Debes introducir " + str(long_cadena) + " números del 1 al 9: ")
                intento_introducido = input()
                break   
    return intento_lista_int
# end comprobar_intento

intento = ""
intento_introducido = ""
num_intentos = 0

long_cadena = comprobar_long()
cadena = generar_cadena(long_cadena)
print("Intenta adivinar la cadena: ")

while intento != cadena:
    intento = comprobar_intento()
    aciertos = 0
    num_intentos += 1
    for i in range(len(cadena)):
        if intento[i] == cadena[i]:
            aciertos += 1
    if aciertos < len(cadena):
        print("Con " + intento_introducido + " has adivinado " + str(aciertos) + " valores. Intenta adivinar la cadena: ")
# end while

print("Con " + intento_introducido + " has adivinado los " + str(long_cadena) + " valores. Felicidades")
print("Número de intentos: " + str(num_intentos))
