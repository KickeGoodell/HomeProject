-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 12, 2022 at 08:23 AM
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
-- Database: `Highscores`
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
(69, 'Adrian(test)', 22, '2022-12-07');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Attempts`
--
ALTER TABLE `Attempts`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Attempts`
--
ALTER TABLE `Attempts`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
