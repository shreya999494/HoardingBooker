-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: hoardingbooker
-- ------------------------------------------------------
-- Server version	5.7.18-log

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
-- Table structure for table `customizeform`
--

DROP TABLE IF EXISTS `customizeform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customizeform` (
  `cfid` int(11) NOT NULL AUTO_INCREMENT,
  `custname` varchar(45) NOT NULL,
  `custmaterial` varchar(45) NOT NULL,
  `custbudget` varchar(45) NOT NULL,
  `custdname` varchar(45) NOT NULL,
  `custdsize` varchar(45) NOT NULL,
  `custdtype` varchar(45) NOT NULL,
  `custreq` varchar(45) NOT NULL,
  `paid` int(11) NOT NULL,
  `custmid` int(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`cfid`),
  KEY `paid_idx` (`paid`),
  KEY `custmid_idx` (`custmid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customizeform`
--

LOCK TABLES `customizeform` WRITE;
/*!40000 ALTER TABLE `customizeform` DISABLE KEYS */;
INSERT INTO `customizeform` VALUES (1,'sjkjkld','fabric','5000','de1','123','suhjiox','jskdal;,a.\"?Xz',0,0,'Accepted'),(2,'sjkjkld','fabric','5000','de1','123','suhjiox','Requirement...',0,0,'Accepted'),(3,'sjkjkld','fabric','5000','de1','123','suhjiox','Requirement...',8,0,'Rejected'),(4,'sjkjkld','fabric','5000','de2','123','suhjiox','Requirement...',7,23,'Rejected'),(5,'sjkjkld','fabric','5000','de1','123','suhjiox','Requirement...',5,23,'Accepted'),(6,'trusti','fabric','5000','de1','123','suhjiox','Requirement...hkdjl',10,23,'pending');
/*!40000 ALTER TABLE `customizeform` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-27 23:08:26
