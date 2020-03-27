'''
Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior a $100.00, el programa dirá que el cliente 
no aplica a la promoción. Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa genera de forma aleatoria 
un número entero del cero al cinco. Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar el descuento 
que el cliente recibirá como premio. Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, 
sí se aplicará un descuento determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo 
inicialmente el usuario, de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.
'''
from random import *

def sorteo_descuento(total_compras_float):
    bola_sorteo = randint(0,4)
    print('''Su gasto iguala o supera los $100.00 y por tanto participa en la promoción:
    
    COLOR            DESCUENTO
    -----            ---------
    Bola blanca       No tiene
    Bola roja           10%
    Bola azul           20%
    Bola verde          25%
    Bola amarilla       50%
    ''')
    if bola_sorteo == 0:
        print("Aleatoriamente usted obtuvo una bola blanca. Mala suerte :-C")
    elif bola_sorteo == 1:
        print("Aleatoriamente usted obtuvo una bola roja.")
        print("Felicidades, ha ganado un 10% de descuento")
        print("Su nuevo total a pagar es: $" + str(round(total_compras_float * 0.9, 2)))
    elif bola_sorteo == 2:
        print("Aleatoriamente usted obtuvo una bola azul.")
        print("Felicidades, ha ganado un 20% de descuento")
        print("Su nuevo total a pagar es: $" + str(round(total_compras_float * 0.8, 2)))
    elif bola_sorteo == 3:
        print("Aleatoriamente usted obtuvo una bola verde.")
        print("Felicidades, ha ganado un 25% de descuento")
        print("Su nuevo total a pagar es: $" + str(round(total_compras_float * 0.75, 2)))
    elif bola_sorteo == 4:
        print("Aleatoriamente usted obtuvo una bola roja.")
        print("Felicidades, ha ganado un 50% de descuento")
        print("Su nuevo total a pagar es: $" + str(round(total_compras_float * 0.5, 2)))
# end sorteo_descuento

salir = "1"

while salir != "0":
    total_compras = input("\nPor favor, introduzca el importe total de las compras efectuadas: ")
    total_compras_float = float(total_compras)
    if total_compras_float >= 100:
        descuento = sorteo_descuento(total_compras_float)
    else:
        print("Lo siento, no tiene posibilidad de descuentos.")
    salir = input("Si desea salir pulse '0' o de lo contrario pulse cualquier otra tecla: ")

print("--- FIN DEL PROGRAMA ---")
