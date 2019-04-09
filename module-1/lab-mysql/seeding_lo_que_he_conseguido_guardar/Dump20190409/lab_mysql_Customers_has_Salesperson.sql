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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-09 20:08:13
