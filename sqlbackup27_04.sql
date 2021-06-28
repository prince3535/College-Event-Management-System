-- MariaDB dump 10.17  Distrib 10.4.10-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	10.4.10-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES ('prathamesh patil','Very great institute.Also the Events are good, but','Mumbai','9634201563');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_college_level`
--

DROP TABLE IF EXISTS `feedback_college_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_college_level` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_college_level`
--

LOCK TABLES `feedback_college_level` WRITE;
/*!40000 ALTER TABLE `feedback_college_level` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedback_college_level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_college_level_garba`
--

DROP TABLE IF EXISTS `feedback_college_level_garba`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_college_level_garba` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_college_level_garba`
--

LOCK TABLES `feedback_college_level_garba` WRITE;
/*!40000 ALTER TABLE `feedback_college_level_garba` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedback_college_level_garba` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_college_level_ig_nith`
--

DROP TABLE IF EXISTS `feedback_college_level_ig_nith`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_college_level_ig_nith` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_college_level_ig_nith`
--

LOCK TABLES `feedback_college_level_ig_nith` WRITE;
/*!40000 ALTER TABLE `feedback_college_level_ig_nith` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedback_college_level_ig_nith` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_comp`
--

DROP TABLE IF EXISTS `feedback_comp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_comp` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_comp`
--

LOCK TABLES `feedback_comp` WRITE;
/*!40000 ALTER TABLE `feedback_comp` DISABLE KEYS */;
INSERT INTO `feedback_comp` VALUES ('mayur','Average Event.','Panvel','876091648'),('avinash','nice,good oranised.','kalyan','7865094876'),('Tanvir','VERY NICE COMPUTER DEPARTMENT','MUMBAI','8970654786');
/*!40000 ALTER TABLE `feedback_comp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_comp_seminar`
--

DROP TABLE IF EXISTS `feedback_comp_seminar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_comp_seminar` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_comp_seminar`
--

LOCK TABLES `feedback_comp_seminar` WRITE;
/*!40000 ALTER TABLE `feedback_comp_seminar` DISABLE KEYS */;
INSERT INTO `feedback_comp_seminar` VALUES ('shivam','many games.... Well organised.','chembur','8902345268');
/*!40000 ALTER TABLE `feedback_comp_seminar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_comp_sports`
--

DROP TABLE IF EXISTS `feedback_comp_sports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_comp_sports` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_comp_sports`
--

LOCK TABLES `feedback_comp_sports` WRITE;
/*!40000 ALTER TABLE `feedback_comp_sports` DISABLE KEYS */;
INSERT INTO `feedback_comp_sports` VALUES ('alpesh','great....','thane','8956473201');
/*!40000 ALTER TABLE `feedback_comp_sports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_comp_tech-fest`
--

DROP TABLE IF EXISTS `feedback_comp_tech-fest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_comp_tech-fest` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_comp_tech-fest`
--

LOCK TABLES `feedback_comp_tech-fest` WRITE;
/*!40000 ALTER TABLE `feedback_comp_tech-fest` DISABLE KEYS */;
INSERT INTO `feedback_comp_tech-fest` VALUES ('Atharva','Something great can be done in events.','Kalyan','7894320187');
/*!40000 ALTER TABLE `feedback_comp_tech-fest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_electrical`
--

DROP TABLE IF EXISTS `feedback_electrical`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_electrical` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_electrical`
--

LOCK TABLES `feedback_electrical` WRITE;
/*!40000 ALTER TABLE `feedback_electrical` DISABLE KEYS */;
INSERT INTO `feedback_electrical` VALUES ('vedant','GREAT .','jalgaon','958749327');
/*!40000 ALTER TABLE `feedback_electrical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_electrical_seminar`
--

DROP TABLE IF EXISTS `feedback_electrical_seminar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_electrical_seminar` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_electrical_seminar`
--

LOCK TABLES `feedback_electrical_seminar` WRITE;
/*!40000 ALTER TABLE `feedback_electrical_seminar` DISABLE KEYS */;
INSERT INTO `feedback_electrical_seminar` VALUES ('tanmay nwg','Better','mumbai','7869436521');
/*!40000 ALTER TABLE `feedback_electrical_seminar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_electrical_sports`
--

DROP TABLE IF EXISTS `feedback_electrical_sports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_electrical_sports` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_electrical_sports`
--

LOCK TABLES `feedback_electrical_sports` WRITE;
/*!40000 ALTER TABLE `feedback_electrical_sports` DISABLE KEYS */;
INSERT INTO `feedback_electrical_sports` VALUES ('Manas ','Ok.','pune','9443618852'),('junid','nice','Panvel','9876584098');
/*!40000 ALTER TABLE `feedback_electrical_sports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_electrical_tech-fest`
--

DROP TABLE IF EXISTS `feedback_electrical_tech-fest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_electrical_tech-fest` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_electrical_tech-fest`
--

LOCK TABLES `feedback_electrical_tech-fest` WRITE;
/*!40000 ALTER TABLE `feedback_electrical_tech-fest` DISABLE KEYS */;
INSERT INTO `feedback_electrical_tech-fest` VALUES ('vinay','very good','maharashtra','8902345268');
/*!40000 ALTER TABLE `feedback_electrical_tech-fest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_electronic`
--

DROP TABLE IF EXISTS `feedback_electronic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_electronic` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_electronic`
--

LOCK TABLES `feedback_electronic` WRITE;
/*!40000 ALTER TABLE `feedback_electronic` DISABLE KEYS */;
INSERT INTO `feedback_electronic` VALUES ('jon','Hi i am jon its great seeing this.','Germany','+49 47826'),('fsvf','','','');
/*!40000 ALTER TABLE `feedback_electronic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_electronic_seminar`
--

DROP TABLE IF EXISTS `feedback_electronic_seminar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_electronic_seminar` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_electronic_seminar`
--

LOCK TABLES `feedback_electronic_seminar` WRITE;
/*!40000 ALTER TABLE `feedback_electronic_seminar` DISABLE KEYS */;
INSERT INTO `feedback_electronic_seminar` VALUES ('aniket raverkar','GREAT .','mumbai','7894320187');
/*!40000 ALTER TABLE `feedback_electronic_seminar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_electronic_tech-fest`
--

DROP TABLE IF EXISTS `feedback_electronic_tech-fest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_electronic_tech-fest` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_electronic_tech-fest`
--

LOCK TABLES `feedback_electronic_tech-fest` WRITE;
/*!40000 ALTER TABLE `feedback_electronic_tech-fest` DISABLE KEYS */;
INSERT INTO `feedback_electronic_tech-fest` VALUES ('manisha','had a great experience','latur','7894320187');
/*!40000 ALTER TABLE `feedback_electronic_tech-fest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_mechanical`
--

DROP TABLE IF EXISTS `feedback_mechanical`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_mechanical` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_mechanical`
--

LOCK TABLES `feedback_mechanical` WRITE;
/*!40000 ALTER TABLE `feedback_mechanical` DISABLE KEYS */;
INSERT INTO `feedback_mechanical` VALUES ('Atharva','Nice to see.','Vashi','8574635241');
/*!40000 ALTER TABLE `feedback_mechanical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_mechanical_seminar`
--

DROP TABLE IF EXISTS `feedback_mechanical_seminar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_mechanical_seminar` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_mechanical_seminar`
--

LOCK TABLES `feedback_mechanical_seminar` WRITE;
/*!40000 ALTER TABLE `feedback_mechanical_seminar` DISABLE KEYS */;
INSERT INTO `feedback_mechanical_seminar` VALUES ('priya','execellent','raver','9648352097');
/*!40000 ALTER TABLE `feedback_mechanical_seminar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_mechanical_sports`
--

DROP TABLE IF EXISTS `feedback_mechanical_sports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_mechanical_sports` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_mechanical_sports`
--

LOCK TABLES `feedback_mechanical_sports` WRITE;
/*!40000 ALTER TABLE `feedback_mechanical_sports` DISABLE KEYS */;
INSERT INTO `feedback_mechanical_sports` VALUES ('nilesh','Better','ghansoli','9443618852');
/*!40000 ALTER TABLE `feedback_mechanical_sports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_mechanical_tech-fest`
--

DROP TABLE IF EXISTS `feedback_mechanical_tech-fest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_mechanical_tech-fest` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_mechanical_tech-fest`
--

LOCK TABLES `feedback_mechanical_tech-fest` WRITE;
/*!40000 ALTER TABLE `feedback_mechanical_tech-fest` DISABLE KEYS */;
INSERT INTO `feedback_mechanical_tech-fest` VALUES ('pankaj','Nice','kalwa','9644332876');
/*!40000 ALTER TABLE `feedback_mechanical_tech-fest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_nss`
--

DROP TABLE IF EXISTS `feedback_nss`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_nss` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_nss`
--

LOCK TABLES `feedback_nss` WRITE;
/*!40000 ALTER TABLE `feedback_nss` DISABLE KEYS */;
INSERT INTO `feedback_nss` VALUES ('hitesh','Looking to event more events can be organised','pune','7865903452'),('sachin','Good work you are doing','udaipur','7986504932');
/*!40000 ALTER TABLE `feedback_nss` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_nss_residential_special_camp`
--

DROP TABLE IF EXISTS `feedback_nss_residential_special_camp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_nss_residential_special_camp` (
  `Name` varchar(20) NOT NULL,
  `Feedback` varchar(50) NOT NULL,
  `Location` varchar(20) NOT NULL,
  `Phone_no.` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_nss_residential_special_camp`
--

LOCK TABLES `feedback_nss_residential_special_camp` WRITE;
/*!40000 ALTER TABLE `feedback_nss_residential_special_camp` DISABLE KEYS */;
INSERT INTO `feedback_nss_residential_special_camp` VALUES ('rahul','nss camp was just awesome','jaipur','8965473821'),('ganesh','nice well planed.','maharashtra','9875643907');
/*!40000 ALTER TABLE `feedback_nss_residential_special_camp` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-27 23:47:00
