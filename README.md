# 📚 Gestion de Bibliothèque

Application console développée en Python pour gérer les emprunts de livres au sein d'une bibliothèque.

## 🎯 Fonctionnalités

- **Gestion des livres** : Ajout, modification, suppression et affichage des livres.
- **Gestion des membres** : Enregistrement des membres de la bibliothèque.
- **Gestion des emprunts** : Emprunt et retour de livres avec suivi des dates.
- **Disponibilité** : Mise à jour automatique du statut des livres (disponible ou emprunté).

## 🏗️ Architecture

Le projet est structuré selon le patron de conception **MVC (Modèle-Vue-Contrôleur)** :
- **Modèle (`models/`)** : Contient les classes `Livre`, `Membre` et `Emprunt`.
- **Vue (`views/`)** : Gère l'affichage dans la console (menus, messages).
- **Contrôleur (`controllers/`)** : Fait le lien entre la vue et le modèle, contient la logique métier.
- **Base de données (`database.py`)** : Gère la connexion et les requêtes SQL.

## 🛠️ Technologies utilisées

- **Langage** : Python 3
- **Base de données** : SQLite (relationnelle)
- **Architecture** : MVC (Modèle-Vue-Contrôleur)
