-- MySQL dump 10.13  Distrib 8.0.15, for macos10.14 (x86_64)
--
-- Host: localhost    Database: lab_mysql
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Customers` (
  `idCustomers` int(11) NOT NULL,
  `Name` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Phone number` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Email` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Address` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `City` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `State/province` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Country` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Zip/Postal code` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Cars_idCars` int(11) NOT NULL,
  `Invoices_idInvoices` int(11) NOT NULL,
  PRIMARY KEY (`idCustomers`),
  KEY `fk_Customers_Cars_idx` (`Cars_idCars`),
  KEY `fk_Customers_Invoices1_idx` (`Invoices_idInvoices`),
  CONSTRAINT `fk_Customers_Cars` FOREIGN KEY (`Cars_idCars`) REFERENCES `cars` (`idCars`),
  CONSTRAINT `fk_Customers_Invoices1` FOREIGN KEY (`Invoices_idInvoices`) REFERENCES `invoices` (`idInvoices`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES (1,'Leviatan','3476950','oghapvi','Avenida de Europa','Madrid','Comunidad de Madrid','Spain','352',1,1),(2,'Horacio','83742650','kkkkk@eeeee','Estrella Polar','Madrid','Comunidad de Madrid','Spain','54676',2,2),(3,'Patricia','9873405978','ggggg@jjjj','Fray Diego de Cádiz','Sevilla','Andalucía','Spain','34573',3,3),(4,'Soufle','7238046','gdgdg@ddd','Calle Berruguete','Madrid','Comunidad de Madrid','Spain','3546',4,4),(5,'Macarena','2738405','ffff@tt','Relator','Sevilla','Andalucía','Spain','3457',5,5);
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-09 20:08:12
