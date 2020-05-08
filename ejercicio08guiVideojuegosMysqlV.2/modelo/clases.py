'''
Módulo para definición de las clases utilizadas en la aplicación
@author: Pedro Laserna
'''

#definimos la clase Videojuego a utilizar en la aplicación
class Videojuego():
    def __init__(self,titulo="",plataforma="",genero="",nota=0.0,prestado=0,apuntes="",id=0):
        self.titulo = titulo
        self.plataforma = plataforma
        self.genero = genero
        self.nota = nota
        self.prestado = prestado
        self.apuntes = apuntes
        self.id = id
