-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.31 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para sistema_pacientes
CREATE DATABASE IF NOT EXISTS `sistema_pacientes` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `sistema_pacientes`;

-- Volcando estructura para tabla sistema_pacientes.consulta
CREATE TABLE IF NOT EXISTS `consulta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_hospital` int(11) NOT NULL DEFAULT '0',
  `nombre` varchar(50) NOT NULL DEFAULT '0',
  `estado` int(11) NOT NULL DEFAULT '0',
  `cantidad_pacientes_atender` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla sistema_pacientes.consulta: 3 rows
/*!40000 ALTER TABLE `consulta` DISABLE KEYS */;
INSERT INTO `consulta` (`id`, `id_hospital`, `nombre`, `estado`, `cantidad_pacientes_atender`) VALUES
	(1, 1, 'Pediatría', 3, 2),
	(2, 1, 'CGI', 3, 5),
	(3, 1, 'Urgencia', 3, 1);
/*!40000 ALTER TABLE `consulta` ENABLE KEYS */;

-- Volcando estructura para tabla sistema_pacientes.especialistas
CREATE TABLE IF NOT EXISTS `especialistas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_consulta` int(11) NOT NULL DEFAULT '0',
  `nombre` varchar(100) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla sistema_pacientes.especialistas: 3 rows
/*!40000 ALTER TABLE `especialistas` DISABLE KEYS */;
INSERT INTO `especialistas` (`id`, `id_consulta`, `nombre`) VALUES
	(1, 1, 'Sebastian Castro'),
	(2, 2, 'Cristo Garcia'),
	(3, 3, 'Jose Pino');
/*!40000 ALTER TABLE `especialistas` ENABLE KEYS */;

-- Volcando estructura para tabla sistema_pacientes.estados
CREATE TABLE IF NOT EXISTS `estados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla sistema_pacientes.estados: 6 rows
/*!40000 ALTER TABLE `estados` DISABLE KEYS */;
INSERT INTO `estados` (`id`, `descripcion`) VALUES
	(1, 'En sala de espera'),
	(2, 'En atencion'),
	(3, 'Consulta desocupada'),
	(4, 'Consulta ocupada'),
	(5, 'Atendido'),
	(6, 'Consulta con cupo');
/*!40000 ALTER TABLE `estados` ENABLE KEYS */;

-- Volcando estructura para tabla sistema_pacientes.hospital
CREATE TABLE IF NOT EXISTS `hospital` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla sistema_pacientes.hospital: 1 rows
/*!40000 ALTER TABLE `hospital` DISABLE KEYS */;
INSERT INTO `hospital` (`id`, `nombre`) VALUES
	(1, 'Hospital Fonasa');
/*!40000 ALTER TABLE `hospital` ENABLE KEYS */;

-- Volcando estructura para tabla sistema_pacientes.pacientes
CREATE TABLE IF NOT EXISTS `pacientes` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(100) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `tipo_paciente` int(11) DEFAULT NULL,
  `id_consulta` int(11) DEFAULT NULL,
  `id_estado_atencion` int(11) DEFAULT '1',
  `id_historia_clinica` int(11) DEFAULT NULL,
  `id_hospital` int(11) DEFAULT NULL,
  `fecha_ingreso` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla sistema_pacientes.pacientes: 10 rows
/*!40000 ALTER TABLE `pacientes` DISABLE KEYS */;
INSERT INTO `pacientes` (`ID`, `nombres`, `apellidos`, `edad`, `email`, `telefono`, `tipo_paciente`, `id_consulta`, `id_estado_atencion`, `id_historia_clinica`, `id_hospital`, `fecha_ingreso`) VALUES
	(1, 'Andrea Olga', 'Carrasco Prado', 40, 'andrea@gmail.com', '21546215', 2, 2, 1, 21546, 1, NULL),
	(2, 'Carla Paulina', 'Vasquez Jarry', 6, 'carla@gmail.com', '3654451254', 1, 1, 1, 2154, 1, NULL),
	(3, 'Pia ', 'Pino', 12, 'pia@gmail.com', '65978784', 3, 1, 1, 2154, 1, NULL),
	(4, 'Ivan ', 'Vivar', 65, 'ivan@gmail.com', '98874511', 2, 2, 1, 36549, 1, NULL),
	(5, 'Gianfranco ', 'Altamirano', 85, 'gian@gmail.com', '87451952', 2, 2, 1, 458754, 1, NULL),
	(6, 'Hilda', 'Andrades', 80, 'hilda@gmail.com', '654879542', 2, 2, 1, 7458451, 1, NULL),
	(7, 'Alejandra ', 'Araya', 54, 'alejandra@gmail.com', '65459874', 2, 2, 1, 12365, 1, NULL),
	(8, 'Cristian ', 'Cifuentes', 26, 'cristian@gmail.com', '45621547', 2, 2, 1, 548754, 1, NULL),
	(9, 'Susana ', 'Pinto', 18, 'susana@gmail.com', '85465924', 2, 2, 1, 5456251, 1, NULL),
	(10, 'Francisco', 'Ormeño', 30, 'francisco@gmail.com', '94568745', 2, 2, 1, 1654987, 1, NULL),
	(11, 'Jurek ', 'Hernandez', 5, 'jurek@gmail.com', '974784099', 1, 1, 1, 66565, 1, NULL);
/*!40000 ALTER TABLE `pacientes` ENABLE KEYS */;

-- Volcando estructura para tabla sistema_pacientes.pacientes_detalles
CREATE TABLE IF NOT EXISTS `pacientes_detalles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `es_fumador` int(11) NOT NULL DEFAULT '0',
  `tiempo_fumador` int(11) DEFAULT NULL,
  `tiene_dieta` int(11) DEFAULT NULL,
  `peso` int(11) DEFAULT NULL,
  `estatura` int(11) DEFAULT NULL,
  `id_paciente` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla sistema_pacientes.pacientes_detalles: 10 rows
/*!40000 ALTER TABLE `pacientes_detalles` DISABLE KEYS */;
INSERT INTO `pacientes_detalles` (`id`, `es_fumador`, `tiempo_fumador`, `tiene_dieta`, `peso`, `estatura`, `id_paciente`) VALUES
	(1, 0, 0, 0, 0, 0, 1),
	(2, 0, 0, 0, 40, 120, 2),
	(3, 0, 0, 0, 50, 168, 3),
	(4, 0, 0, 1, 0, 0, 4),
	(5, 0, 0, 1, 0, 0, 5),
	(6, 0, 0, 0, 0, 0, 6),
	(7, 0, 0, 0, 0, 0, 7),
	(8, 1, 5, 0, 0, 0, 8),
	(9, 0, 0, 0, 0, 0, 9),
	(10, 1, 15, 0, 0, 0, 10),
	(11, 0, 0, 0, 20, 110, 11);
/*!40000 ALTER TABLE `pacientes_detalles` ENABLE KEYS */;

-- Volcando estructura para tabla sistema_pacientes.tipo_paciente
CREATE TABLE IF NOT EXISTS `tipo_paciente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla sistema_pacientes.tipo_paciente: 3 rows
/*!40000 ALTER TABLE `tipo_paciente` DISABLE KEYS */;
INSERT INTO `tipo_paciente` (`id`, `descripcion`) VALUES
	(1, 'Niño'),
	(2, 'Joven/Adulto'),
	(3, '3° Edad');
/*!40000 ALTER TABLE `tipo_paciente` ENABLE KEYS */;

-- Volcando estructura para tabla sistema_pacientes.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` char(102) DEFAULT NULL,
  `fullName` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla sistema_pacientes.user: 1 rows
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `username`, `password`, `fullName`) VALUES
	(1, 'admin', 'pbkdf2:sha256:260000$c4Eko37qVYz1GPei$efc8ac94f57d9605704907677a02fcb48ac1403ac333c6217ae4d01bfdff13ea', 'Administrador');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
