
from modelo import constantes_sql
import mysql.connector

# Función para conectar con la BBDD
def conectar():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_videojuegos"
        )
    return mydb
# end conectar

# Función para la inserción de un nuevo videojuego en la BBDD
def registro_videojuego_bd(videojuego):
    sql = constantes_sql.SQL_INSERTAR_VIDEOJUEGO
    mydb = conectar()
    cursor = mydb.cursor()
    val = (videojuego.titulo, videojuego.plataforma, videojuego.genero, videojuego.anyo, videojuego.precio)
    cursor.execute(sql,val)
    mydb.commit()
    mydb.disconnect()
# end registro_videojuego_bd

# Función para obtener todos los videojuegos registrados en la BBDD
def obtener_videojuegos_bd():
    sql = constantes_sql.SQL_LISTADO_VIDEOJUEGOS
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute(sql)
    resultado_lista = cursor.fetchall()
    mydb.disconnect()
    return resultado_lista
# end obtener_videojuegos_bd

# Función para buscar videojuegos según los parámetros de busqueda. Posteriormente se podran visualizar, editar o borrar los registros obtenidos
def buscar_videojuegos_bd(valores): # "valores" es un diccionario con clave (P.E. Id) y valor (P.E. 1) correspondientes a los valores de cada videojuego
    sql = constantes_sql.SQL_LISTADO_VIDEOJUEGOS
    valores_completados = False # creamos variable booleana para identificar si el usuario ha cumplimentado algún campo
    for campo, valor in valores.items():
        if valor != "" and campo == "id": # Si se aporta el campo id, al ser la clave primaria ya se ignoran el resto de posibles valores aportados
            sql += " WHERE " + campo + " = " + valor # Añadimos a la sentencia sql el WHERE para que filtre resultados por la clave primaria (id)
            valores_completados = True
            break
        elif valor != "" and sql.count("WHERE") <= 0: # Si no se aporta id y es el primer valor que se encuentra se añade el WHERE a la sentencia sql
            sql += " WHERE " + campo + " LIKE '%" + valor + "%'"
            valores_completados = True
        elif valor != "" and sql.count("WHERE") > 0: # Si hay mas valores aportados en la busqueda se añade un AND para seguir filtrando los resultados
            sql += " AND " + campo + " LIKE '%" + valor + "%'"
    if valores_completados: # Si se han aportado datos para la busqueda entonces se hace la conexión y se devuelven los resultados
        mydb = conectar()
        cursor = mydb.cursor()
        cursor.execute(sql)
        resultado_lista = cursor.fetchall()
        mydb.disconnect()
        return resultado_lista
    else:
        return [] # Si no se ha facilitado ningún dato para la busqueda entonces se devuelve una lista vacia, del mismo modo que si no hubiera encontrado resultados en la BBDD
# end buscar_videojuegos_bd

#Función para borrar un videojuego de la BBDD aportando la clave primaria del videojuego a borrar
def borrar_videojuego_bd(id_a_borrar):
    sql = constantes_sql.SQL_BORRAR_VIDEOJUEGO
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute(sql,id_a_borrar)
    mydb.commit()
    mydb.disconnect()
# end borrar_videojuego_bd

# Función para modificar los datos de un registro de la BBDD facilitando la tupla con los valores a modificar y la clave primaria para el WHERE
def modificar_videojuego_bd(valores):
    sql = constantes_sql.SQL_MODIFICAR_VIDEOJUEGO
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute(sql,valores)
    mydb.commit()
    mydb.disconnect()
# end modificar_videojuego_bd
