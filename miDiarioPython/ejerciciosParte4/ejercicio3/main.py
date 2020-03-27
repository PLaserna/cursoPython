'''
Este programa muestra primero el listado de categorías de películas y pide al usuario que introduzca el código de la categoría de la película y 
posterior a ello pide que el usuario introduzca el número de días de atraso, y así se muestra al final el total a pagar.
'''

class Categoria():
    nombre = ""
    precio = 0.0
    codigo = 0
    recargo_dia = 0.0

    def __init__(self, nombre, precio, codigo, recargo_dia):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
        self.recargo_dia = recargo_dia
# end Categoria

def cargar_categorias():
    categorias = []
    categorias.append(Categoria("Favoritos     ",2.50,1,0.50))
    categorias.append(Categoria("Nuevos        ",3.00,2,0.75))
    categorias.append(Categoria("Estrenos      ",3.50,3,1.00))
    categorias.append(Categoria("Super Estrenos",4.00,4,1.50))
    return categorias
# end cargar_categorias

def listado(categorias):
    print("\nCATEGORIA\t\tPRECIO\t\tCÓDIGO\t\tRECARGO/DÍA DE RETRASO")
    print("---------\t\t------\t\t------\t\t----------------------")
    for c in categorias:
        print(c.nombre + "\t\t$" + "{:.2f}".format(c.precio) + "\t\t" + str(c.codigo) + "\t\t$" + "{:.2f}".format(c.recargo_dia))
# end listado

salir = "1" 
categorias = cargar_categorias()

while salir != "0":
    listado(categorias)
    codigo = input("\nIntroduzca el código de la categoría de la película: ")
    if codigo.isnumeric() and int(codigo) > 0 and int(codigo) < len(categorias):
        dias_atraso = input("Introduzca el número de días de atraso en la devolución: ")
        if dias_atraso.isnumeric():
            dias_atraso_int = int(dias_atraso)
            total_a_pagar = categorias[int(codigo)-1].precio + dias_atraso_int * categorias[int(codigo)-1].recargo_dia
            print("El total a pagar es: $" + "{:.2f}".format(total_a_pagar))
        else:
            print("El valor introducido no es válido")
            continue
    else:
            print("El valor introducido no es válido")
            continue
    salir = input("\nSi desea salir pulse '0' o de lo contrario pulse cualquier otra tecla: ")
# end while

print("--- FIN DEL PROGRAMA ---")
