'''
módulo menus
'''
from clases import Cliente

def menu_principal():
    salir = True
    while salir:
        print("\nInserta una opción:")
        print("-------------------")
        print("1- Registrar cliente")
        print("2- Borrar cliente")
        print("3- Listar clientes")
        print("\n4- SALIR")
        introducido = input()
        if introducido.isnumeric():
            introducido_int = int(introducido)
            if introducido_int < 1 or introducido_int > 4:
                print("Opción no válida")
            else:
                return introducido_int
        else:
            print("Debes introducir un número del 1 al 4")
#end menu_principal

def menu_insertar():
    nuevo_cliente = Cliente()    
    print("\nInserta el nombre del cliente:")
    nuevo_cliente.nombre = input()
    print("\nInserta el teléfono del cliente:")
    nuevo_cliente.telefono = input()
    return nuevo_cliente
#end menu_insertar

def menu_borrar(listado):
    print("\nInserta el nombre del cliente a borrar:")
    cliente_a_borrar = input()
    return cliente_a_borrar
# end menu_borrar