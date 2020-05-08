-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-04-2020 a las 23:19:10
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
(8, 'Borderlands 2', 'PC', 'FPS', '2012-09-21', '29.99'),
(48, 'TituloModificado', 'PlataformaModificada', 'GeneroModificadoOK', '2020-04-07', '5.00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_videojuegos_v2`
--

CREATE TABLE `tabla_videojuegos_v2` (
  `id` int(11) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `plataforma` varchar(50) NOT NULL,
  `genero` varchar(50) NOT NULL,
  `nota` decimal(2,1) NOT NULL,
  `prestado` tinyint(1) NOT NULL DEFAULT 0,
  `apuntes` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_videojuegos_v2`
--

INSERT INTO `tabla_videojuegos_v2` (`id`, `titulo`, `plataforma`, `genero`, `nota`, `prestado`, `apuntes`) VALUES
(1, 'Super Metroid', 'Super Nintendo', 'Plataformas', '9.2', 0, 'Mi juego favorito'),
(28, 'Diablo 3', 'PC', 'Action RPG', '8.8', 0, '+DLCs en Battle.net'),
(31, 'Borderlands 2', 'PC', 'FPS Looter', '8.9', 0, '+DLCs en Steam');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tabla_videojuegos`
--
ALTER TABLE `tabla_videojuegos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tabla_videojuegos_v2`
--
ALTER TABLE `tabla_videojuegos_v2`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tabla_videojuegos`
--
ALTER TABLE `tabla_videojuegos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT de la tabla `tabla_videojuegos_v2`
--
ALTER TABLE `tabla_videojuegos_v2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
