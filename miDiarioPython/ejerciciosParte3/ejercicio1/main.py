#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Reino del Dragon....

import random
import time

def introduccion():
    print ("Estamos en una tierra llena de dragones. Delante nuestro,")
    print ("se ven dos cuevas. En una cueva, el dragón es amigable")
    print ("y compartirá el tesoro contigo. El otro dragón")
    print ("es codicioso y hambriento, y te va a comer en cuanto te vea.")
    print ("")

def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print ("¿A que cueva quieres entrar? 1 o 2?")
        cueva = input()
    return cueva

def cheqcueva(CambiarCueva):
    print ("Te acercas a la Cueva...")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragón salta delante tuyo, abre su boca y...")
    print ("")
    time.sleep(3)
   
    FriendlyCueva = random.randint (1, 2)
   
    if CambiarCueva == str(FriendlyCueva):
        print ("Te entrega el tesoro...")
        return True
    else:
        print ("El dragón te come de un bocado....")
        return False
   
EmpezarNuevo = ("si")
monedas = 0

while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):
    introduccion()
    NumCaverna = CambiarCueva()
    ganaste = cheqcueva(NumCaverna)
    if ganaste:
        monedas += 100
    else:
        monedas = 0
    print("Total monedas: " + str(monedas))
    print ("Quieres jugar de nuevo? (si o no)")
    EmpezarNuevo = input()

print("--- FIN DEL JUEGO ---")
