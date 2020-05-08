'''
Módulo en el que se incluyen las funciones que operan con la bbdd
@author: Pedro Laserna
'''

import mysql.connector
from operaciones_bd import constantes_sql
from clases import modelo

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_anuncios_ropa"
        )
    return conexion

def registrar_anuncio(prenda, codigo):
    sql = constantes_sql.SQL_INSERCION_ANUNCIO
    conexion = conectar()
    id_generado = -1
    try:
        cursor = conexion.cursor()
        val = (prenda.id_categoria, prenda.genero, prenda.marca, prenda.talla, prenda.precio, prenda.email, prenda.descripcion, codigo)
        cursor.execute(sql, val)
        conexion.commit()
        id_generado = cursor.lastrowid
    except Exception as e:
        print(e)
    finally:
        if conexion is not None:
            conexion.disconnect()
    return id_generado

def comprobar_codigo_anuncio(id, codigo):
    sql = constantes_sql.SQL_COMPROBAR_CODIGO_ANUNCIO
    conexion = conectar()
    lista = None
    try:
        cursor = conexion.cursor()
        val = (id, codigo)
        cursor.execute(sql, val)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if conexion is not None:
            conexion.disconnect()
    return len(lista) #si da 0 es que el id y el codigo no es válido y si da un 1 es que si lo son

def validar_email_anuncio(id):
    sql = constantes_sql.SQL_VALIDAR_ANUNCIO
    conexion = conectar()
    val = (id,)
    cursor = conexion.cursor()
    cursor.execute(sql, val)
    conexion.commit()
    conexion.disconnect()

def obtener_anuncios():
    sql = constantes_sql.SQL_LISTADO_ANUNCIOS
    conexion = conectar()
    lista = None
    try:
        cursor = conexion.cursor()
        cursor.execute(sql)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if conexion is not None:
            conexion.disconnect()
    return lista

def borrar_anuncio(id):
    sql = constantes_sql.SQL_BORRAR_ANUNCIO
    conexion = conectar()
    val = (id,)
    cursor = conexion.cursor()
    cursor.execute(sql, val)
    conexion.commit()
    conexion.disconnect()

def obtener_anuncio_por_id(id):
    sql = constantes_sql.SQL_OBTENER_ANUNCIO_POR_ID
    conexion = conectar()
    val = (id,)
    cursor = conexion.cursor()
    cursor.execute(sql, val)
    res = cursor.fetchone()
    conexion.disconnect()

    prenda = modelo.Prenda()
    prenda.id = res[0]
    prenda.id_categoria = res[1]
    prenda.genero = res[2]
    prenda.marca = res[3]
    prenda.talla = res[4]
    prenda.precio = res[5]
    prenda.email = res[6]
    prenda.descripcion = res[7]
    prenda.email_valido = res[8]

    return prenda

def guardar_cambios_anuncio(prenda):
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_ANUNCIO
    conexion = conectar()
    cursor = conexion.cursor()
    val = (prenda.id_categoria,prenda.genero,prenda.marca,prenda.talla,prenda.precio,prenda.email,prenda.descripcion,prenda.email_valido,prenda.id)
    cursor.execute(sql, val)
    conexion.commit()
    conexion.disconnect()

def obtener_categorias():
    sql = constantes_sql.SQL_OBTENER_CATEGORIAS
    conexion = conectar()
    lista = None
    try:
        cursor = conexion.cursor()
        cursor.execute(sql)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if conexion is not None:
            conexion.disconnect()
    return lista
