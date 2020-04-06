
# Definimos las distintas instrucciones SQL que vamos a utilizar
SQL_INSERTAR_VIDEOJUEGO = "INSERT INTO `tabla_videojuegos` (`titulo`, `plataforma`, `genero`, `anyo`, `precio`) VALUES (%s, %s, %s, %s, %s);"
SQL_LISTADO_VIDEOJUEGOS = "SELECT * FROM `tabla_videojuegos`"
SQL_BORRAR_VIDEOJUEGO = "DELETE FROM `tabla_videojuegos` WHERE id = %s"
SQL_MODIFICAR_VIDEOJUEGO = "UPDATE `tabla_videojuegos` SET `titulo` = %s, `plataforma` = %s, `genero` = %s, `anyo` = %s, `precio` = %s WHERE id = %s"
