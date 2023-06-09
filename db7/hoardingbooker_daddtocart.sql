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
-- Table structure for table `daddtocart`
--

DROP TABLE IF EXISTS `daddtocart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `daddtocart` (
  `ddcartid` int(11) NOT NULL AUTO_INCREMENT,
  `ddcustid` int(11) NOT NULL,
  `ddcatid` int(11) NOT NULL,
  `dddetailsid` int(11) NOT NULL,
  `ddqty` int(11) NOT NULL,
  `ddtotalprice` int(11) NOT NULL,
  PRIMARY KEY (`ddcartid`),
  KEY `dcustid_idx` (`ddcustid`),
  KEY `dcatid_idx` (`ddcatid`),
  KEY `ddetailsid_idx` (`dddetailsid`),
  CONSTRAINT `ddcatid` FOREIGN KEY (`ddcatid`) REFERENCES `category1` (`catid1`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ddcustid` FOREIGN KEY (`ddcustid`) REFERENCES `login` (`lid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `dddetailsid` FOREIGN KEY (`dddetailsid`) REFERENCES `designdetails` (`ddid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daddtocart`
--

LOCK TABLES `daddtocart` WRITE;
/*!40000 ALTER TABLE `daddtocart` DISABLE KEYS */;
INSERT INTO `daddtocart` VALUES (24,38,2,64,2,30000),(25,23,2,64,2,30000);
/*!40000 ALTER TABLE `daddtocart` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-27 23:08:24
