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
-- Table structure for table `pcreg`
--

DROP TABLE IF EXISTS `pcreg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pcreg` (
  `pcid` int(11) NOT NULL AUTO_INCREMENT,
  `pcname` varchar(45) NOT NULL,
  `pccname` varchar(45) NOT NULL,
  `pcadd` varchar(45) NOT NULL,
  `pcmob` varchar(45) NOT NULL,
  `pcemail` varchar(45) NOT NULL,
  `pcdoc` varchar(45) NOT NULL,
  `loginid` int(11) NOT NULL,
  `status` varchar(45) DEFAULT NULL,
  `pcclogo` varchar(45) NOT NULL,
  PRIMARY KEY (`pcid`),
  KEY `loginid_idx` (`loginid`),
  CONSTRAINT `loginid` FOREIGN KEY (`loginid`) REFERENCES `login` (`lid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pcreg`
--

LOCK TABLES `pcreg` WRITE;
/*!40000 ALTER TABLE `pcreg` DISABLE KEYS */;
INSERT INTO `pcreg` VALUES (5,'pa1','satnam enterprice','None','9825535916','bipinlic585@yahoo.co.in','',24,'Accepted','abc.jpg'),(6,'pa2','xyz','None','9825535916','raj12@gmail.com','',30,'Accepted','abc.jpg'),(7,'pa3','abc','None','9825535916','raj12@gmail.com','',31,'Accepted','abc.jpg'),(9,'pa5','xyz','None','9825535916','raj12@gmail.com','',33,'Accepted','xyz.jpg'),(10,'pa5','abc','None','9825535916','bipinlic585@yahoo.co.in','',34,'Accepted','abc.png'),(11,'bipin patel','satnam enterprice','c1c b2hm','9825535916','admin@gmail.com','satnam enterprice.pdf',36,'Accepted','satnam enterprice.png'),(12,'pa5','satnam enterprice','F/2-3','9825535916','pa5@gmail.com','satnam enterprice.pdf',40,'Rejected','satnam enterprice.png'),(14,'pa6','satnam enterprice','F/2-3,Palika Bazar','9825535916','pa6@gmail.com','satnam enterprice.pdf',42,'pending','satnam enterprice.png');
/*!40000 ALTER TABLE `pcreg` ENABLE KEYS */;
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
