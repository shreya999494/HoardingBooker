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
-- Table structure for table `paddtocart`
--

DROP TABLE IF EXISTS `paddtocart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paddtocart` (
  `pcartid` int(11) NOT NULL AUTO_INCREMENT,
  `pcustid` int(11) NOT NULL,
  `pcatid` int(11) NOT NULL,
  `pdetailsid` int(11) NOT NULL,
  `pqty` int(11) NOT NULL,
  `pprice` int(11) NOT NULL,
  PRIMARY KEY (`pcartid`),
  KEY `pcustid_idx` (`pcustid`),
  KEY `pcatid_idx` (`pcatid`),
  KEY `pdetailsid_idx` (`pdetailsid`),
  CONSTRAINT `pcatid` FOREIGN KEY (`pcatid`) REFERENCES `category` (`catid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `pcustid` FOREIGN KEY (`pcustid`) REFERENCES `login` (`lid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `pdetailsid` FOREIGN KEY (`pdetailsid`) REFERENCES `placedetails` (`pdid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paddtocart`
--

LOCK TABLES `paddtocart` WRITE;
/*!40000 ALTER TABLE `paddtocart` DISABLE KEYS */;
INSERT INTO `paddtocart` VALUES (27,23,4,14,1,30000),(30,38,3,12,5,250000);
/*!40000 ALTER TABLE `paddtocart` ENABLE KEYS */;
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
