'''
Módulo con las instrucciones SQL utilizadas
@author: Pedro Laserna
'''

#definimos las distintas instrucciones SQL que vamos a utilizar
SQL_INSERTAR_VIDEOJUEGO = "INSERT INTO `tabla_videojuegos_v2`(`titulo`, `plataforma`, `genero`, `nota`, `prestado`, `apuntes`) VALUES (%s, %s, %s, %s, %s, %s);"
SQL_LISTAR_VIDEOJUEGOS = "SELECT * FROM `tabla_videojuegos_v2`;"
SQL_BORRAR_VIDEOJUEGO = "DELETE FROM `tabla_videojuegos_v2` WHERE `id` = %s;"
SQL_MODIFICAR_VIDEOJUEGO = "UPDATE `tabla_videojuegos_v2` SET `titulo` = %s, `plataforma` = %s, `genero` = %s, `nota` = %s, `prestado` = %s, `apuntes` = %s WHERE `id` = %s;"