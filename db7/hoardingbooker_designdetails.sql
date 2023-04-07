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
-- Table structure for table `designdetails`
--

DROP TABLE IF EXISTS `designdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `designdetails` (
  `ddid` int(11) NOT NULL AUTO_INCREMENT,
  `pcpic` varchar(45) NOT NULL,
  `dname` varchar(45) NOT NULL,
  `dsize` varchar(45) NOT NULL,
  `dtype` varchar(45) NOT NULL,
  `dmaterial` varchar(45) NOT NULL,
  `logid` int(11) NOT NULL,
  `dprice` varchar(45) NOT NULL,
  `ddiscript` varchar(45) NOT NULL,
  `dcatid` int(11) NOT NULL,
  PRIMARY KEY (`ddid`),
  KEY `logid_idx` (`logid`),
  KEY `cid_idx` (`dcatid`),
  CONSTRAINT `logid` FOREIGN KEY (`logid`) REFERENCES `login` (`lid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `designdetails`
--

LOCK TABLES `designdetails` WRITE;
/*!40000 ALTER TABLE `designdetails` DISABLE KEYS */;
INSERT INTO `designdetails` VALUES (62,'/media/design2_Al13EWo.jpg','design2','500*200','Food Court','PVC',24,'20000','good',1),(64,'/media/design4_czF9KPs.jpg','design4','800*300','Food Court','pvc',24,'15000','unique design',2),(65,'/media/design5_0BfhCXj.jpg','design5','200*800','Other','Aluminium',24,'30000','advertisement',2),(66,'/media/design6_GjtybZ9.jpg','design6','100*50','Insurance Company','acrylic',24,'20000','good',4),(67,'/media/design7_9vodYAf.jpg','design7','500*1000','Other','fabric',24,'11000','latest design',4),(68,'/media/design10_mKWl04M.jpg','design10','1000*500','Food Court','Aluminium',24,'11000','advertisement',4),(69,'/media/design11.jpg','design11','100*50','P.G.','acrylic',24,'11000','advertisement',4),(70,'/media/design12_8kiXLaN.jpg','design12','1500*200','P.G.','pvc',24,'15000','advertisement',2),(73,'/media/design20.jpg','design20','1000*500','P.G.','plastic',24,'11000','advertisement',1),(74,'/media/design21.jpg','design21','100*50','Insurance Company','fabric1',24,'15000','advertisement',1),(75,'/media/design22.jpg','design22','1000*500','Cosmetic','fabric',24,'11000','advertisement',2),(76,'/media/design24.jpg','design24','200*800','Study Institute','plastic',24,'15000','advertisement',2);
/*!40000 ALTER TABLE `designdetails` ENABLE KEYS */;
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
