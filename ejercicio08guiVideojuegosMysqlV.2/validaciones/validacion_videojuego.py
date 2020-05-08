'''
Módulo para la validación de los campos título y género en la introducción de estos datos
@author: pedro
'''

import re

#definimos las expresiones regulares que vamos a utilizar
expresion_id = "^[0-9]{0,4}$"
expresion_titulo = "^[0-9a-zA-Z áéíóúÁÉÍÓÚñÑ]{2,30}$"
expresion_genero = "^[a-zA-Z áéíóúÁÉÍÓÚñÑ]{2,20}$"

#definimos las funciones para validar la id, el título y el género del videojuego
def validar_id(id):
    validador_id = re.compile(expresion_id)
    return validador_id.match(id)
#end validar_id

def validar_titulo(titulo):
    validador_titulo = re.compile(expresion_titulo)
    return validador_titulo.match(titulo)
#end validar_titulo

def validar_genero(genero):
    validador_genero = re.compile(expresion_genero)
    return validador_genero.match(genero)
#end validar_genero
