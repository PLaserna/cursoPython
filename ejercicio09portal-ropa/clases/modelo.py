'''
Módulo en el que se incluyen las clases a utilizar en la aplicación
@author: Pedro Laserna
'''

class Prenda():
    def __init__(self,id_categoria=1,genero="",marca="",talla="",precio=0.0,email="",descripcion="",email_valido="NO",id=-1):
        self.id_categoria = id_categoria
        self.genero = genero
        self.marca = marca
        self.talla = talla
        self.precio = precio
        self.email = email
        self.descripcion = descripcion
        self.email_valido = email_valido
        self.id = id
        