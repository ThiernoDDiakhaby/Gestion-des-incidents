-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 09 nov. 2020 à 16:00
-- Version du serveur :  10.4.11-MariaDB
-- Version de PHP : 7.3.15
use gestion_incident;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `gestion_incident`
--

-- --------------------------------------------------------

--
-- Structure de la table `probleme`
--

--
-- Structure de la table `utilisateur`
--

CREATE TABLE `utilisateur` (
  `id_u` int(11) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `Login` text NOT NULL,
  `psw` text NOT NULL,
  `role` text NOT NULL 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`id_u`, `prenom`, `nom`, `Login`, `psw`, `role`) VALUES
(56, 'moussa', 'Deme', 'logtest@gmail.com', 'passtest', 'user'),
(57, 'thierno', 'diakhaby', 'logtest', 'passtest', 'user'),
(58, '', '', 'logtest', 'passtest', 'user'),
(60, 'moussa', 'deme', 'admin@gmail.com', 'admin', 'admin'),
(61, 'sdcsdc', 'Moussa ', 'moussademe97@gmail.com', 'yryrèyuyu', 'user'),
(62, 'dzeryz', 'Moussa ', 'moussademe97@gmail.com', 'zedrzyed', 'user'),
(63, 'arzeya', 'zteay', 'moussademe97@gmail.com', 'azeyaz', 'user'),
(64, 'thierno', 'diakhaby', 'thiernodd@gmail.com', 'khadija', 'user'),
(65, 'aly', 'ba', 'aly@gmail.com', 'alyalyaly', 'user');


CREATE TABLE `probleme` (
  `id_p` int(11) NOT NULL,
  `severite` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `date_p` timestamp NOT NULL DEFAULT current_timestamp(),
  `id_user` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `probleme`
--

INSERT INTO `probleme` (`id_p`, `severite`, `description`, `date_p`, `id_user`) VALUES
(47, 'urgent', 'test de probleme de ROS à regler', '0000-00-00 00:00:00', 60),
(48, 'bas', 'probleme de gestion', '2020-10-31 22:33:36', 57),
(49, 'urgent', 'probleme sur le front', '2018-07-21 22:00:00', 56),
(50, 'urgent', 'probleme sur le front', '2018-07-21 22:00:00', 56),
(51, 'bas', 'design à refaire', '2020-10-31 23:00:00', 56),
(52, 'bas', 'design à refaire', '2020-10-31 23:00:00', 56),
(53, 'bas', 'test de langage corporelle', '2020-11-06 23:00:00', 60);

-- --------------------------------------------------------

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `probleme`
--
ALTER TABLE `utilisateur`
  ADD PRIMARY KEY (`id_u`);

ALTER TABLE `probleme`
  ADD PRIMARY KEY (`id_p`),
  ADD KEY `id_user` (`id_user`) USING BTREE;

--
-- Index pour la table `utilisateur`
--


--
-- AUTO_INCREMENT pour les tables déchargées
--
ALTER TABLE `utilisateur`
  MODIFY `id_u` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT pour la table `probleme`
--
ALTER TABLE `probleme`
  MODIFY `id_p` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT pour la table `utilisateur`
--

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `probleme`
--
ALTER TABLE `probleme`
  ADD CONSTRAINT `probleme_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `utilisateur` (`id_u`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
