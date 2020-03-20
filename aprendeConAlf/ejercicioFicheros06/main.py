'''
Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. 
El programa debe incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, 
añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.txt 
donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.
'''
from menus import menu_principal
from acciones import registrar_cliente, borrar_cliente, listar_clientes

salir = False

while not salir:
    opcion = menu_principal()
    if opcion == 1:
        registrar_cliente()
    elif opcion == 2:
        borrar_cliente()
    elif opcion == 3:
        listar_clientes()
    else:
        salir = True

print("--- FIN DEL PROGRAMA ---")
