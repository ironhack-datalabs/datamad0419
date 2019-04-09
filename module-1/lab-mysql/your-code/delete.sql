-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: lab_mysql
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cars` (
  `idCar` int(11) NOT NULL,
  `vin` varchar(45) DEFAULT NULL,
  `manufacturer` varchar(45) DEFAULT NULL,
  `model` varchar(45) DEFAULT NULL,
  `year` varchar(45) DEFAULT NULL,
  `colour` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCar`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cars`
--

LOCK TABLES `Cars` WRITE;
/*!40000 ALTER TABLE `Cars` DISABLE KEYS */;
INSERT INTO `Cars` VALUES (0,'3K096I98581DHSNUP','Volkswagen','Tiguan','2019','Blue'),(1,'ZM8G7BEUQZ97IH46V','Peugeot','Rifter','2019','Red'),(2,'RKXVNNIHLVVZOUB4M','Ford','Fusion','2018','White'),(3,'HKNDGS7CU31E9Z7JW','Toyota','RAV4','2018','Silver'),(5,'DAM41UDN3CHU2WVF6','Volvo','V60 Cross CCountry','2019','Gray');
/*!40000 ALTER TABLE `Cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customers` (
  `idCustomers` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `phone number` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `state/prov` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `postal` varchar(45) DEFAULT NULL,
  `Cars_idCar` int(11) NOT NULL,
  PRIMARY KEY (`idCustomers`),
  KEY `fk_Customers_Cars1_idx` (`Cars_idCar`),
  CONSTRAINT `fk_Customers_Cars1` FOREIGN KEY (`Cars_idCar`) REFERENCES `Cars` (`idCar`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES (10001,'Pablo Picasso','+34 636 17 63 82','ppicasso@gmail.com','Paseo de la Chopera, 14 - Madrid','Madrid','Spain','28045',3),(20001,'Abraham Lincoln','+1 305 907 7086','lincoln@us.gov','120 SW 8th St - Miami','Florida','USA','33130',0),(30001,'Napoléon Bonaparte','+33 1 79 75 40 00','hello@napoleon.me','40 Rue du Colisée - Paris','Île-de-France','France','75008',2);
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Invoices`
--

DROP TABLE IF EXISTS `Invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Invoices` (
  `idInvoice` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `Cars_idCar` int(11) NOT NULL,
  `Customers_idCustomers` int(11) DEFAULT NULL,
  `Salespersons_idStaff` int(11) NOT NULL,
  PRIMARY KEY (`idInvoice`),
  KEY `fk_Invoices_Cars_idx` (`Cars_idCar`),
  KEY `fk_Invoices_Customers1_idx` (`Customers_idCustomers`),
  KEY `fk_Invoices_Salespersons1_idx` (`Salespersons_idStaff`),
  CONSTRAINT `fk_Invoices_Cars` FOREIGN KEY (`Cars_idCar`) REFERENCES `Cars` (`idCar`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Customers1` FOREIGN KEY (`Customers_idCustomers`) REFERENCES `Customers` (`idCustomers`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Salespersons1` FOREIGN KEY (`Salespersons_idStaff`) REFERENCES `Salespersons` (`idStaff`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Invoices`
--

LOCK TABLES `Invoices` WRITE;
/*!40000 ALTER TABLE `Invoices` DISABLE KEYS */;
INSERT INTO `Invoices` VALUES (271135104,'2019-01-22',2,NULL,7),(731166526,'2018-12-31',3,NULL,5),(852399038,'2018-08-22',0,NULL,3);
/*!40000 ALTER TABLE `Invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Salespersons`
--

DROP TABLE IF EXISTS `Salespersons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Salespersons` (
  `idStaff` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `store` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idStaff`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Salespersons`
--

LOCK TABLES `Salespersons` WRITE;
/*!40000 ALTER TABLE `Salespersons` DISABLE KEYS */;
INSERT INTO `Salespersons` VALUES (1,'Petey Cruiser','Madrid'),(2,'Anna Sthesia','BCN'),(3,'Paul Molive','Berlin'),(4,'Gail Forcewind','Paris'),(5,'Paige Turner','Miami'),(6,'Bob Frapples','Mexico City'),(7,'Walter Melon','Amsterdam'),(8,'Shonda Leer','São Paulo');
/*!40000 ALTER TABLE `Salespersons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Salespersons_has_Cars`
--

DROP TABLE IF EXISTS `Salespersons_has_Cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Salespersons_has_Cars` (
  `Salespersons_idStaff` int(11) NOT NULL,
  `Cars_idCar` int(11) NOT NULL,
  PRIMARY KEY (`Salespersons_idStaff`,`Cars_idCar`),
  KEY `fk_Salespersons_has_Cars_Cars1_idx` (`Cars_idCar`),
  KEY `fk_Salespersons_has_Cars_Salespersons1_idx` (`Salespersons_idStaff`),
  CONSTRAINT `fk_Salespersons_has_Cars_Cars1` FOREIGN KEY (`Cars_idCar`) REFERENCES `Cars` (`idCar`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Salespersons_has_Cars_Salespersons1` FOREIGN KEY (`Salespersons_idStaff`) REFERENCES `Salespersons` (`idStaff`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Salespersons_has_Cars`
--

LOCK TABLES `Salespersons_has_Cars` WRITE;
/*!40000 ALTER TABLE `Salespersons_has_Cars` DISABLE KEYS */;
INSERT INTO `Salespersons_has_Cars` VALUES (3,0),(7,2),(5,3);
/*!40000 ALTER TABLE `Salespersons_has_Cars` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-09 21:23:55
