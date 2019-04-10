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
-- Table structure for table `Cars`
--

DROP TABLE IF EXISTS `Cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Cars` (
  `idCars` int(11) NOT NULL,
  `Manufacturer` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Model` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Year` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Color` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`idCars`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cars`
--

LOCK TABLES `Cars` WRITE;
/*!40000 ALTER TABLE `Cars` DISABLE KEYS */;
INSERT INTO `Cars` VALUES (1,'Aston Martin','A2','2090','rojo'),(2,'Audi','67','1945','naranja'),(3,'Renault','C5','2031','verde'),(4,'Audi','78','2010','azul'),(5,'Merceder','N6','1978','gris');
/*!40000 ALTER TABLE `Cars` ENABLE KEYS */;
UNLOCK TABLES;

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

--
-- Table structure for table `Customers_has_Salesperson`
--

DROP TABLE IF EXISTS `Customers_has_Salesperson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Customers_has_Salesperson` (
  `Customers_idCustomers` int(11) NOT NULL,
  `Salesperson_idSalesperson` int(11) NOT NULL,
  PRIMARY KEY (`Customers_idCustomers`,`Salesperson_idSalesperson`),
  KEY `fk_Customers_has_Salesperson_Salesperson1_idx` (`Salesperson_idSalesperson`),
  KEY `fk_Customers_has_Salesperson_Customers1_idx` (`Customers_idCustomers`),
  CONSTRAINT `fk_Customers_has_Salesperson_Customers1` FOREIGN KEY (`Customers_idCustomers`) REFERENCES `customers` (`idCustomers`),
  CONSTRAINT `fk_Customers_has_Salesperson_Salesperson1` FOREIGN KEY (`Salesperson_idSalesperson`) REFERENCES `salesperson` (`idSalesperson`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers_has_Salesperson`
--

LOCK TABLES `Customers_has_Salesperson` WRITE;
/*!40000 ALTER TABLE `Customers_has_Salesperson` DISABLE KEYS */;
INSERT INTO `Customers_has_Salesperson` VALUES (3,1),(2,2),(1,3),(4,4),(5,5);
/*!40000 ALTER TABLE `Customers_has_Salesperson` ENABLE KEYS */;
UNLOCK TABLES;

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

--
-- Table structure for table `Salesperson`
--

DROP TABLE IF EXISTS `Salesperson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Salesperson` (
  `idSalesperson` int(11) NOT NULL,
  `Name` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Store` varchar(45) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Cars_idCars` int(11) NOT NULL,
  `Invoices_idInvoices` int(11) NOT NULL,
  PRIMARY KEY (`idSalesperson`),
  KEY `fk_Salesperson_Cars1_idx` (`Cars_idCars`),
  KEY `fk_Salesperson_Invoices1_idx` (`Invoices_idInvoices`),
  CONSTRAINT `fk_Salesperson_Cars1` FOREIGN KEY (`Cars_idCars`) REFERENCES `cars` (`idCars`),
  CONSTRAINT `fk_Salesperson_Invoices1` FOREIGN KEY (`Invoices_idInvoices`) REFERENCES `invoices` (`idInvoices`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Salesperson`
--

LOCK TABLES `Salesperson` WRITE;
/*!40000 ALTER TABLE `Salesperson` DISABLE KEYS */;
INSERT INTO `Salesperson` VALUES (1,'HY','traefg',1,1),(2,'YY','raet',2,2),(3,'TR','taert',3,3),(4,'OP','afreag',4,4),(5,'RE','ersgfd',5,5);
/*!40000 ALTER TABLE `Salesperson` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-10  9:22:19
