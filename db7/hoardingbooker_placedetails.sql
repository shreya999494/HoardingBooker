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
-- Table structure for table `placedetails`
--

DROP TABLE IF EXISTS `placedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `placedetails` (
  `pdid` int(11) NOT NULL AUTO_INCREMENT,
  `phpic` varchar(45) NOT NULL,
  `pname` varchar(45) NOT NULL,
  `psize` varchar(45) NOT NULL,
  `parea` varchar(45) NOT NULL,
  `logid2` int(11) NOT NULL,
  `pprice` varchar(45) NOT NULL,
  `pdiscript` varchar(45) NOT NULL,
  `cid` int(11) DEFAULT NULL,
  PRIMARY KEY (`pdid`),
  KEY `logid2_idx` (`logid2`),
  KEY `catid_idx` (`cid`),
  CONSTRAINT `catid` FOREIGN KEY (`cid`) REFERENCES `category` (`catid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `logid2` FOREIGN KEY (`logid2`) REFERENCES `login` (`lid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `placedetails`
--

LOCK TABLES `placedetails` WRITE;
/*!40000 ALTER TABLE `placedetails` DISABLE KEYS */;
INSERT INTO `placedetails` VALUES (12,'/media/place%202_FcNkgNX.jpg','place 2','1200*1500','vastrapur',22,'50000','digital design',3),(13,'/media/place%203.jpg','place 3','8000*2000','s.g. highway',22,'30000','awesome',4),(14,'/media/place%204.jpg','place 4','5000*2000','baroda express highway',22,'30000','good',4),(15,'/media/place%205.jpg','place 5','500*2000','kalasagar mall',22,'33000','Awesome...',5),(16,'/media/place%206.jpg','place 6','800*800','himalaya mall',22,'36000','crowdy place',5);
/*!40000 ALTER TABLE `placedetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-27 23:08:25
