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
-- Table structure for table `custreg`
--

DROP TABLE IF EXISTS `custreg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custreg` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(45) NOT NULL,
  `cmob` varchar(45) NOT NULL,
  `cemail` varchar(45) NOT NULL,
  `loginid1` int(11) NOT NULL,
  `caddress` varchar(45) NOT NULL,
  `cintrest` varchar(45) NOT NULL,
  PRIMARY KEY (`cid`),
  KEY `loginid1_idx` (`loginid1`),
  CONSTRAINT `loginid1` FOREIGN KEY (`loginid1`) REFERENCES `login` (`lid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custreg`
--

LOCK TABLES `custreg` WRITE;
/*!40000 ALTER TABLE `custreg` DISABLE KEYS */;
INSERT INTO `custreg` VALUES (3,'cust1','15486513','cust1@gmail.com',23,'6,vaikunthdham soc.,unjha','Food Court'),(4,'cust2','8128115215','cust@gmail.com',38,'10,shreeji apt,ahmedabad','Insurance Company'),(5,'ABC','8128115215','gsjh@sgj.cip',39,'A-112 shukun bunglows,ahmedabad','Food Court'),(7,'cust4','8128115215','cust4@gmail.com',46,'dgfhghjkl','P.G.');
/*!40000 ALTER TABLE `custreg` ENABLE KEYS */;
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
