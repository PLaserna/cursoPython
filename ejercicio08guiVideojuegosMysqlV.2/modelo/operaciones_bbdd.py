'''
Módulo en el que se incluyen las funciones que modifican la base de datos
@author: Pedro Laserna
'''

import mysql.connector
from modelo import constantes_sql

#función para conectar con la BBDD
def conectar():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_videojuegos"
        )
    return mydb
#end conectar

#función para la inserción de un nuevo videojuego en la BBDD
def registro_videojuego_bd(videojuego):
    sql = constantes_sql.SQL_INSERTAR_VIDEOJUEGO
    mydb = conectar()
    cursor = mydb.cursor()
    #convertimos videojuego (de la clase Videojuego) a la tupla que vamos a utilizar para la sql
    val = (videojuego.titulo, videojuego.plataforma, videojuego.genero, videojuego.nota, videojuego.prestado, videojuego.apuntes)
    cursor.execute(sql,val)
    #nos quedamos con el id generado en la inserción para devolverlo en la función
    id_generado = cursor.lastrowid
    mydb.commit()
    mydb.disconnect()
    return id_generado
#end registro_videojuego_bd

#función para buscar videojuegos según los parámetros de busqueda. Posteriormente se podran visualizar, editar o borrar los registros obtenidos
def buscar_videojuegos_bd(valores): #"valores" es un diccionario con clave (Ejemplo: plataforma) y valor (Ejemplo: PlayStation) correspondientes a los valores de cada videojuego
    #utilizamos la misma sql para obtener los listados de todos los videojuegos pero modificándola para incluir los valores aportados para la búsqueda
    sql = constantes_sql.SQL_LISTAR_VIDEOJUEGOS[:-1]
    #creamos dos tuplas para identificar si los valores son de texto (LIKE %valor%) o numéricos (= valor)
    campos_igual = ("id","prestado")
    campos_like = ("titulo","genero","apuntes")
    #recorremos el diccionario para ir modificando la sql. el campo "prestado" y "plataforma" siempre se aportan porque tienen valores por defecto en el formulario  
    for campo, valor in valores.items():
        #verificamos si se ha aportado algún valor en el formulario de busqueda y si es el primero valor para modificar la sql con "WHERE" o "AND" según corresponda
        if campo in campos_igual and valor != "" and sql.count("WHERE") <= 0:
            sql += " WHERE " + campo + " = " + str(valor)
        elif campo in campos_like and valor != "" and sql.count("WHERE") <= 0:
            sql += " WHERE " + campo + " LIKE '%" + valor + "%'"
        elif campo in campos_igual and valor != "" and sql.count("WHERE") > 0:
            sql += " AND " + campo + " = " + str(valor)
        elif campo in campos_like and valor != "" and sql.count("WHERE") > 0:
            sql += " AND " + campo + " LIKE '%" + valor + "%'"
        #el campo "plataforma" es especial, se elige entre valores ya definidos y no debe llevar comodines porque produciria errores en la busqueda (%PlayStation% devuelve resultados de "PlayStation 2", por ejemplo) 
        elif campo == "plataforma" and valor != "" and sql.count("WHERE") <= 0:
            sql += " WHERE " + campo + " = '" + valor + "'"
        elif campo == "plataforma" and valor != "" and sql.count("WHERE") > 0:
            sql += " AND " + campo + " = '" + valor + "'"
    sql += ";" 
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute(sql)
    videojuegos_encontrados = cursor.fetchall()
    mydb.disconnect()
    #devolvemos los videojuegos encontrados
    return videojuegos_encontrados
#end buscar_videojuegos_bd

#función para obtener todos los videojuegos registrados en la BBDD
def obtener_videojuegos_bd():
    sql = constantes_sql.SQL_LISTAR_VIDEOJUEGOS
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute(sql)
    resultado_lista = cursor.fetchall()
    mydb.disconnect()
    return resultado_lista
#end obtener_videojuegos_bd

#función para borrar un videojuego de la BBDD aportando la clave primaria del videojuego a borrar
def borrar_videojuego_bd(id_a_borrar):
    sql = constantes_sql.SQL_BORRAR_VIDEOJUEGO
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute(sql, id_a_borrar)
    mydb.commit()
    mydb.disconnect()
#end borrar_videojuego_bd

#función para modificar los datos de un registro de la BBDD facilitando la tupla con los valores a modificar y la clave primaria para el WHERE
def modificar_videojuego_bd(videojuego_a_modificar):
    sql = constantes_sql.SQL_MODIFICAR_VIDEOJUEGO
    v = videojuego_a_modificar
    valores = (v.titulo, v.plataforma, v.genero, v.nota, v.prestado, v.apuntes, v.id)
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute(sql,valores)
    mydb.commit()
    mydb.disconnect()
#end modificar_videojuego_bd
