'''
De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar. El programa determinará el total
 a pagar, como una factura.
Una variante a este ejercicio que lo haría un poco más complejo sería dar la posibilidad de seguir ingresando diferentes códigos de productos 
con sus respectivas cantidades, y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras. Te animas??
'''

class Producto():
    nombre = ""
    codigo = 0
    precio = 0

    def __init__(self, nombre, codigo, precio):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
# end Producto

def cargar_almacen():
    almacen = []
    almacen.append(Producto("Código inválido",0,0))
    almacen.append(Producto("Camisa    ",1,30.00))
    almacen.append(Producto("Cinturón  ",2,14.59))
    almacen.append(Producto("Zapatos   ",3,60.00))
    almacen.append(Producto("Pantalón  ",4,35.00))
    almacen.append(Producto("Calcetines",5,8.00))
    almacen.append(Producto("Falda     ",6,25.00))
    almacen.append(Producto("Gorra     ",7,12.50))
    almacen.append(Producto("Jersey    ",8,25.95))
    almacen.append(Producto("Corbata   ",9,22.99))
    almacen.append(Producto("Chaqueta  ",10,80.25))
    return almacen
# end cargar_almacen

def listado(almacen):
    print("Elija el producto deseado:")
    print("PRODUCTO       CÓDIGO")
    print("--------       ------")
    for p in almacen:
        if p.codigo == 0:
            continue
        else:
            print(p.nombre + "  -->  " + str(p.codigo))
# end listado

def compra(almacen):
    global total_compra
    unidades = ""
    print("\nIntroduce código: ")
    codigo = input()
    if codigo.isnumeric() and int(codigo) > 0 and int(codigo) <= 10:
        codigo_int = int(codigo)
        print("El precio unitario es $" + str(almacen[codigo_int].precio))
        while not unidades.isnumeric():
            unidades = input("Introduzca el número de unidades: ")
            if unidades.isnumeric():
                unidades_int = int(unidades)
                print("El importe a pagar por estos " + unidades + " productos es: $" + str(unidades_int * almacen[codigo_int].precio))
                total_compra += unidades_int * almacen[codigo_int].precio
                
            else:
                print("Por favor introduzca un valor válido")    
    else:
        print("Por favor introduzca un valor válido")

salir = "1"
total_compra = 0

almacen = cargar_almacen()

while salir != "0":
    listado(almacen)
    compra(almacen)
    salir = input("Si desea salir y ver el total pulse '0', si va a añadir mas productos a la cesta pulse cualquier otra tecla: ")

print("\nEl importe total de la compra es: $" + str(total_compra))
print("--- FIN DEL PROGRAMA ---")
