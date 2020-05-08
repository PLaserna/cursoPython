'''
Módulo en el que se incluyen las sentencias SQL a utilizar
@author: Pedro Laserna
SQL de creación de tabla: CREATE TABLE `bd_anuncios_ropa`.`tabla_anuncios_ropa` ( `id` INT NOT NULL AUTO_INCREMENT ,  `id_categoria` INT(4) NOT NULL ,  
`genero` VARCHAR(6) NULL ,  `marca` VARCHAR(255) NULL ,  `talla` VARCHAR(8) NOT NULL ,  `precio` DECIMAL(8,2) NOT NULL ,  
`email` VARCHAR(255) NOT NULL , `descripcion` VARCHAR(255) NULL,     PRIMARY KEY  (`id`)) ENGINE = InnoDB;
'''
#columnas: `id`, `id_categoria`, `genero`, `marca`, `talla`, `precio`, `email`
SQL_INSERCION_ANUNCIO = "INSERT INTO `tabla_anuncios_ropa` (`id`, `id_categoria`, `genero`, `marca`, `talla`, `precio`, `email`, `descripcion`, `email-valido`, `codigo`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, 'NO', %s);"

SQL_LISTADO_ANUNCIOS = "SELECT a.`id`, c.`nombre`, a.`genero`, a.`marca`, a.`talla`, a.`descripcion`, a.`precio`, a.`email`, a.`email-valido` FROM tabla_anuncios_ropa AS a, tabla_categorias_ropa AS c WHERE a.`id_categoria` = c.`id` ORDER BY a.`id` DESC;"

SQL_COMPROBAR_CODIGO_ANUNCIO = "SELECT `id_categoria` FROM `tabla_anuncios_informatica` WHERE `id` = %s AND `codigo` = %s;"

SQL_VALIDAR_ANUNCIO = "UPDATE `tabla_anuncios_ropa` SET `email-valido` = 'SI' WHERE `id` = %s;"

SQL_BORRAR_ANUNCIO = "DELETE FROM `tabla_anuncios_ropa` WHERE `id` = %s;"

SQL_OBTENER_ANUNCIO_POR_ID = "SELECT * FROM `tabla_anuncios_ropa` WHERE `id` = %s;"

SQL_GUARDAR_CAMBIOS_ANUNCIO = "UPDATE `tabla_anuncios_ropa` SET `id_categoria` = %s, `genero` = %s, `marca` = %s, `talla` = %s, `precio` = %s, `email` = %s, `descripcion` = %s, `email-valido` = %s WHERE `id` = %s;"

SQL_OBTENER_CATEGORIAS = "SELECT * FROM `tabla_categorias_ropa` ORDER BY `id` ASC;"