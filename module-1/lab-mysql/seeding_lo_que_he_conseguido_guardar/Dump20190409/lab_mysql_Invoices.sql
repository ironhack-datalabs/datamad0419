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
-- Table structure for table `Invoices`
--

DROP TABLE IF EXISTS `Invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Invoices` (
  `idInvoices` int(11) NOT NULL,
  `Date` datetime DEFAULT NULL,
  `Car` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Customer` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Salesperson` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Cars_idCars` int(11) NOT NULL,
  PRIMARY KEY (`idInvoices`),
  KEY `fk_Invoices_Cars1_idx` (`Cars_idCars`),
  CONSTRAINT `fk_Invoices_Cars1` FOREIGN KEY (`Cars_idCars`) REFERENCES `cars` (`idCars`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Invoices`
--

LOCK TABLES `Invoices` WRITE;
/*!40000 ALTER TABLE `Invoices` DISABLE KEYS */;
INSERT INTO `Invoices` VALUES (1,'1998-07-01 00:00:00','ipaugv','4','yy',1),(2,'2010-06-03 00:00:00','aoihv','5','rrr',2),(3,'2016-08-01 00:00:00','oiñhg','6','ggg',3),(4,'1999-02-03 00:00:00','ipg','7','jjj',4),(5,'2012-04-01 00:00:00','oihv','1','aaaa',5);
/*!40000 ALTER TABLE `Invoices` ENABLE KEYS */;
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
