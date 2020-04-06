-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-04-2020 a las 01:17:08
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
-- Base de datos: `bd_videojuegos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_videojuegos`
--

CREATE TABLE `tabla_videojuegos` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `plataforma` varchar(255) NOT NULL,
  `genero` varchar(255) NOT NULL,
  `anyo` date NOT NULL,
  `precio` decimal(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_videojuegos`
--

INSERT INTO `tabla_videojuegos` (`id`, `titulo`, `plataforma`, `genero`, `anyo`, `precio`) VALUES
(1, 'Portal 2', 'PC', 'Puzles', '2011-04-19', '8.19'),
(6, 'Diablo 3', 'PC', 'Action RPG', '2012-05-15', '19.99'),
(7, 'The Orange Box', 'PC', 'Acción', '2007-10-10', '16.79'),
(8, 'Borderlands 2', 'PC', 'FPS', '2012-09-21', '29.99');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tabla_videojuegos`
--
ALTER TABLE `tabla_videojuegos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tabla_videojuegos`
--
ALTER TABLE `tabla_videojuegos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
