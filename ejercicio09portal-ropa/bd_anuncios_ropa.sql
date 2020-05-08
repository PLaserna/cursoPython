-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-05-2020 a las 10:06:31
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_anuncios_ropa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_anuncios_ropa`
--

CREATE TABLE `tabla_anuncios_ropa` (
  `id` int(11) NOT NULL,
  `id_categoria` int(4) NOT NULL,
  `genero` varchar(6) DEFAULT NULL,
  `marca` varchar(255) DEFAULT NULL,
  `talla` varchar(8) NOT NULL,
  `precio` decimal(8,2) NOT NULL,
  `email` varchar(255) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `email-valido` varchar(2) NOT NULL DEFAULT 'NO',
  `codigo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_anuncios_ropa`
--

INSERT INTO `tabla_anuncios_ropa` (`id`, `id_categoria`, `genero`, `marca`, `talla`, `precio`, `email`, `descripcion`, `email-valido`, `codigo`) VALUES
(1, 2, 'Hombre', 'NIKE', 'M', '12.95', 'camiseto@gmail.com', 'Es una camiseta buenísima y tirada de precio', 'SI', NULL),
(3, 7, 'Unisex', 'VANS', 'M', '10.00', 'gorri@hotmail.com', 'Fantástica gorra que hará que seas la envidia del lugar', 'SI', NULL),
(4, 4, 'Mujer', 'LEVIS', 'S', '25.00', 'pantaloncia@yahoo.es', 'No aprietan', 'SI', NULL),
(5, 11, 'Mujer', 'RIPCURL', 'L', '73.52', 'sudaderio@gmail.com', 'Es una sudadera pero no se suda con ella. A no ser que te pongas a correr, entonces si que se suda', 'SI', NULL),
(6, 3, 'Hombre', 'RALPH LAUREN', 'XL', '50.30', 'camisario@hotmail.com', 'Camisa elegante para ocasiones especiales (guiño guiño)', 'SI', NULL),
(8, 2, 'Hombre', 'ADIDAS', 'M', '12.50', 'eze_sin@yahoo.es', 'Camiseta Adidas, muy normalita', 'SI', '3ueLWYcwcuHvUJg2Vjs2qlaeRVmBgPTDH7REnmWakFEPnrYPqiFBqBo7X3sXadOFOSiCQN9ec7c1gfOgH282iGa1LQyNL6um9t6h'),
(9, 6, 'Hombre', 'CORTEFIEL', 'M', '21.00', 'eze_sin@yahoo.es', 'Corbata sosa de rombos', 'NO', '3OeCt9Lt2lMxllxOCY3KthEkzUd5RhWobpCnd09bAi6aPYN6ODbh2Lg9uTx9VqzmQLV7Xl5dyUgPfYdaqrdWnIh2XESlZfIZH0OL'),
(29, 5, 'Mujer', 'ZARA', 'S', '42.00', 'eze_sin@yahoo.es', 'Falda de flores blancas. Sin apenas uso', 'SI', 'iZClD4zrEqBNt3u6WDJHkx8SaIiugX8bY32mmAVsSsNFmmMb69HBHr405z7ihroJlflJ9a7HV5Ofjym2Dy769mnlBvpxyytsSaDW');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_categorias_ropa`
--

CREATE TABLE `tabla_categorias_ropa` (
  `id` int(4) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_categorias_ropa`
--

INSERT INTO `tabla_categorias_ropa` (`id`, `nombre`, `descripcion`) VALUES
(1, 'SIN CATEGORIA', 'Pendiente de asignar categoría'),
(2, 'CAMISETAS', 'Camisetas de manga corta o larga'),
(3, 'CAMISAS', 'Camisas de manga corta o larga'),
(4, 'PANTALONES', 'Pantalones de todo tipo de tejidos y estilos'),
(5, 'FALDAS', 'Faldas/minifaldas de todos los estilos'),
(6, 'COMPLEMENTOS', 'Bolsos y complementos textiles de todo tipo'),
(7, 'SOMBREROS', 'Sombreros y gorros'),
(8, 'ROPA INTERIOR', 'Todo tipo de ropa interior de hombre y mujer'),
(9, 'ABRIGOS', 'Prendas de abrigo, como chaquetas, parcas, chubasqueros, etc'),
(10, 'VESTIDOS', 'Vestidos de una o varias piezas'),
(11, 'SUDADERAS', 'Sudaderas y jerseys'),
(12, 'ROPA DE CASA', 'Pijamas, mantas y cualquier otras ropa del hogar');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tabla_anuncios_ropa`
--
ALTER TABLE `tabla_anuncios_ropa`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Indices de la tabla `tabla_categorias_ropa`
--
ALTER TABLE `tabla_categorias_ropa`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tabla_anuncios_ropa`
--
ALTER TABLE `tabla_anuncios_ropa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `tabla_categorias_ropa`
--
ALTER TABLE `tabla_categorias_ropa`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tabla_anuncios_ropa`
--
ALTER TABLE `tabla_anuncios_ropa`
  ADD CONSTRAINT `tabla_anuncios_ropa_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `tabla_categorias_ropa` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
