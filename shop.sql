-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: shop
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `teleg_store`
--

DROP TABLE IF EXISTS `teleg_store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teleg_store` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name_devices` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `photo_name` varchar(255) NOT NULL,
  `description_devices` text NOT NULL,
  `type_devices` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teleg_store`
--

LOCK TABLES `teleg_store` WRITE;
/*!40000 ALTER TABLE `teleg_store` DISABLE KEYS */;
INSERT INTO `teleg_store` VALUES (1,'Xiomi',4.00,'one.jpg','rqwetr','Телефон'),(2,'Sumsung',5.00,'two.jpg','укупуцп','Планшет'),(3,'Сборка',6.00,'three.jpg','i3 344234','ПК'),(4,'ggqergg',8.00,'hhh.jpg','erggg','ПК'),(5,'wgtg',9.00,'jjj.jpg','куйукп','Планшет'),(6,'рцрреры',5.00,'phone-retro.jpg','пыпф','Телефон'),(7,'5нй54н',7.00,'uuu.png','gegg','Планшет'),(8,'йун',6.00,'lll.jpg','jstyjst','Телефон'),(9,'ппр',8.00,'ttt.jpg','kfgj','ПК');
/*!40000 ALTER TABLE `teleg_store` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-20 18:42:41
