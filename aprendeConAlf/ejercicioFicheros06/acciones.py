'''
módulo acciones
'''
from menus import menu_insertar, menu_borrar

def registrar_cliente():
    nuevo_cliente = menu_insertar()
    f = open("listin.txt","a")
    f.write(nuevo_cliente.nombre + "," + nuevo_cliente.telefono + "\n")
    f.close()
# end registrar_cliente

def borrar_cliente():
    listado = listar_clientes()
    if listado != False:
        cliente_a_borrar = menu_borrar(listado)
        borrado = False
        for cliente in listado:
            if cliente_a_borrar.lower() == cliente.split(",")[0].lower():
                listado.remove(cliente)
                print("El cliente ha sido borrado")
                borrado = True
                break
        if not borrado:
            print("Opción no válida")
        f = open("listin.txt","w")
        for linea in listado: 
            f.write(linea)
        f.close()
# end borrar_cliente

def listar_clientes():
    try:
        f = open("listin.txt")
    except:
        print("No hay ningún cliente registrado")
        return False
    else:
        listado = f.readlines()
        listado.sort()
        for linea in listado:
            print("Nombre: " + linea.split(",")[0])
            print("Teléfono: " + linea.split(",")[1])
        f.close()
        return listado
# end listar_clientes