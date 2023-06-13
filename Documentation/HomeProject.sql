-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 13, 2023 at 10:04 AM
-- Server version: 8.0.31-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `HomeProject`
--

-- --------------------------------------------------------

--
-- Table structure for table `Attempts`
--

CREATE TABLE `Attempts` (
  `ID` int NOT NULL,
  `Navn` varchar(30) NOT NULL,
  `Score` int NOT NULL,
  `Dato` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Attempts`
--

INSERT INTO `Attempts` (`ID`, `Navn`, `Score`, `Dato`) VALUES
(64, 'Kicke', 10, '2022-12-07'),
(68, 'Viusan', 24, '2022-12-07'),
(69, 'Adrian(test)', 22, '2022-12-07'),
(79, 'KickeNewAndImproved', 43, '2022-12-12'),
(80, 'MarieTest', 16, '2023-01-04'),
(83, 'MEWOWOWW', 8, '2023-06-04'),
(84, 'TOT', 21, '2023-06-04'),
(85, 'KICKEEE', 9, '2023-06-05');

-- --------------------------------------------------------

--
-- Table structure for table `FAQ`
--

CREATE TABLE `FAQ` (
  `ID` int NOT NULL,
  `Name` varchar(30) NOT NULL,
  `QuestionTitle` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Question` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Answer` varchar(160) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Visibility` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'no'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `FAQ`
--

INSERT INTO `FAQ` (`ID`, `Name`, `QuestionTitle`, `Question`, `Answer`, `Visibility`) VALUES
(23, 'Enrique', 'Game broks', 'Why can', 'Sorry! Servers are currently down. I hope this helps', 'yes'),
(24, 'Alf Morten', 'Ip-addresse', 'Hva er en ip-addresse', 'En ip-addresse er en selvstendig identifikasjon på en enhet innenfor et nettverk', 'yes');

-- --------------------------------------------------------

--
-- Table structure for table `WebUsers`
--

CREATE TABLE `WebUsers` (
  `ID` int NOT NULL,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Privileges` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `WebUsers`
--

INSERT INTO `WebUsers` (`ID`, `Username`, `Password`, `Privileges`) VALUES
(6, 'admin', '1234', 'all'),
(7, 'Enrique', '123', 'faq'),
(12, 'Kicke', 'yolo', 'all'),
(13, 'test', '12345', 'faq');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Attempts`
--
ALTER TABLE `Attempts`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `FAQ`
--
ALTER TABLE `FAQ`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `WebUsers`
--
ALTER TABLE `WebUsers`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Attempts`
--
ALTER TABLE `Attempts`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;

--
-- AUTO_INCREMENT for table `FAQ`
--
ALTER TABLE `FAQ`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `WebUsers`
--
ALTER TABLE `WebUsers`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
