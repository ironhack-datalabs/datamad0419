-- MySQL dump 10.13  Distrib 8.0.15, for macos10.14 (x86_64)
--
-- Host: localhost    Database: mysql_lab
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
  `VIN` varchar(45) NOT NULL,
  `Manufacturer` varchar(45) NOT NULL,
  `Model` varchar(45) NOT NULL,
  `Year` varchar(45) NOT NULL,
  `Color` varchar(45) NOT NULL,
  PRIMARY KEY (`VIN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cars`
--

LOCK TABLES `Cars` WRITE;
/*!40000 ALTER TABLE `Cars` DISABLE KEYS */;
INSERT INTO `Cars` VALUES ('3K096I98581DHSNUP','Volkswagen','Tiguan','2019','Blue'),('DAM41UDN3CHU2WVF6','Volvo','V60 Cross Country','2019','Gray'),('HKNDGS7CU31E9Z7JW','Toyota','RAV4','2018','Silver'),('RKXVNNIHLVVZOUB4M','Ford','Fusion','2018','White'),('ZM8G7BEUQZ97IH46V	','Peugeot','Rifter','2019','Red');
/*!40000 ALTER TABLE `Cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Customers` (
  `CustomerID` int(11) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Phone number` varchar(45) NOT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Adress` varchar(45) DEFAULT NULL,
  `City` varchar(45) DEFAULT NULL,
  `State/province` varchar(45) DEFAULT NULL,
  `Country` varchar(45) DEFAULT NULL,
  `Zip Postal Code` varchar(45) DEFAULT NULL,
  `Cars_VIN` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`CustomerID`),
  KEY `fk_Customers_Cars2_idx` (`Cars_VIN`),
  CONSTRAINT `fk_Customers_Cars2` FOREIGN KEY (`Cars_VIN`) REFERENCES `cars` (`VIN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES (10001,'Pablo Picasso	','+34 636 17 63 82	','-','Paseo de la Chopera, 14	','Madrid','Madrid','Spain','28045','3K096I98581DHSNUP'),(20001,'Abraham Lincoln','+1 305 907 7086','-','120 SW 8th St','Miami','Florida','United States','33130','RKXVNNIHLVVZOUB4M'),(30001,'Napoléon Bonaparte	','+33 1 79 75 40 00	','-','40 Rue du Colisée	','Paris','Île-de-France	','France','75008','DAM41UDN3CHU2WVF6');
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Invoices`
--

DROP TABLE IF EXISTS `Invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Invoices` (
  `Invoice number` int(11) NOT NULL,
  `Data` date DEFAULT NULL,
  `Customers_CustomerID` int(11) NOT NULL,
  `Salespersons_Staff ID` int(11) NOT NULL,
  `Cars_VIN` varchar(45) NOT NULL,
  PRIMARY KEY (`Invoice number`),
  KEY `fk_Invoices_Customers2_idx` (`Customers_CustomerID`),
  KEY `fk_Invoices_Salespersons2_idx` (`Salespersons_Staff ID`),
  KEY `fk_Invoices_Cars1_idx` (`Cars_VIN`),
  CONSTRAINT `fk_Invoices_Cars1` FOREIGN KEY (`Cars_VIN`) REFERENCES `cars` (`VIN`),
  CONSTRAINT `fk_Invoices_Customers2` FOREIGN KEY (`Customers_CustomerID`) REFERENCES `customers` (`CustomerID`),
  CONSTRAINT `fk_Invoices_Salespersons2` FOREIGN KEY (`Salespersons_Staff ID`) REFERENCES `salespersons` (`Staff ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Invoices`
--

LOCK TABLES `Invoices` WRITE;
/*!40000 ALTER TABLE `Invoices` DISABLE KEYS */;
INSERT INTO `Invoices` VALUES (271135104,'2018-01-22',30001,2,'DAM41UDN3CHU2WVF6'),(731166526,'2018-12-31',20001,2,'RKXVNNIHLVVZOUB4M'),(852399038,'2018-08-22',10001,1,'3K096I98581DHSNUP');
/*!40000 ALTER TABLE `Invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Salespersons`
--

DROP TABLE IF EXISTS `Salespersons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Salespersons` (
  `Staff ID` int(11) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Store` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Staff ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Salespersons`
--

LOCK TABLES `Salespersons` WRITE;
/*!40000 ALTER TABLE `Salespersons` DISABLE KEYS */;
INSERT INTO `Salespersons` VALUES (1,'Petey Cruiser','Madrid'),(2,'Anna Sthesia	','Barcelona'),(3,'Paul Molive	','Berlin'),(4,'Gail Forcewind	','Paris'),(6,'Bob Frapples	','Mexico City'),(7,'Walter Melon','Amsterdam'),(8,'Shonda Leer','São Paulo');
/*!40000 ALTER TABLE `Salespersons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Salespersons_has_Customers`
--

DROP TABLE IF EXISTS `Salespersons_has_Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Salespersons_has_Customers` (
  `Salespersons_Staff ID` int(11) NOT NULL,
  `Customers_CustomerID` int(11) NOT NULL,
  PRIMARY KEY (`Salespersons_Staff ID`,`Customers_CustomerID`),
  KEY `fk_Salespersons_has_Customers_Customers1_idx` (`Customers_CustomerID`),
  KEY `fk_Salespersons_has_Customers_Salespersons1_idx` (`Salespersons_Staff ID`),
  CONSTRAINT `fk_Salespersons_has_Customers_Customers1` FOREIGN KEY (`Customers_CustomerID`) REFERENCES `customers` (`CustomerID`),
  CONSTRAINT `fk_Salespersons_has_Customers_Salespersons1` FOREIGN KEY (`Salespersons_Staff ID`) REFERENCES `salespersons` (`Staff ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Salespersons_has_Customers`
--

LOCK TABLES `Salespersons_has_Customers` WRITE;
/*!40000 ALTER TABLE `Salespersons_has_Customers` DISABLE KEYS */;
/*!40000 ALTER TABLE `Salespersons_has_Customers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-09 22:17:41
