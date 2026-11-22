import sqlite3
from datetime import date
from models.livre import Livre
from models.membre import Membre
from models.emprunt import Emprunt

class Bibliotheque:
    def __init__(self, chemin_db="data/bibliotheque.db"):
        # 1. Connexion à la base (créera le fichier si absent)
        self.conn = sqlite3.connect(chemin_db)
        self.curseur = self.conn.cursor()
        self.creer_tables()

    def creer_tables(self):
        # Création des 3 tables si elles n'existent pas
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS livres (
                isbn TEXT PRIMARY KEY,
                titre TEXT,
                auteur TEXT,
                maison_edition TEXT,
                disponible INTEGER
            )
        """)
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS membres (
                id_membre TEXT PRIMARY KEY,
                nom TEXT,
                prenoms TEXT
            )
        """)
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS emprunts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isbn TEXT,
                id_membre TEXT,
                date_emprunt TEXT,
                date_rendu TEXT
            )
        """)
        self.conn.commit()

    # --- AJOUTS ---
    def ajouter_livre(self, livre):
        try:
            self.curseur.execute("INSERT INTO livres VALUES (?, ?, ?, ?, ?)",
                                 (livre.isbn, livre.titre, livre.auteur, livre.maison_edition, int(livre.disponible)))
            self.conn.commit()
        except sqlite3.IntegrityError:
            return "Erreur : Ce livre existe déjà."

    def ajouter_membre(self, membre):
        try:
            self.curseur.execute("INSERT INTO membres VALUES (?, ?, ?)",
                                 (membre.id_membre, membre.nom, membre.prenoms))
            self.conn.commit()
        except sqlite3.IntegrityError:
            return "Erreur : Ce membre existe déjà."

    # --- RECHERCHES ---
    def trouver_livre_par_isbn(self, isbn):
        self.curseur.execute("SELECT * FROM livres WHERE isbn = ?", (isbn,))
        res = self.curseur.fetchone()
        if res:
            return Livre(res[0], res[1], res[2], res[3], bool(res[4]))
        return None

    def trouver_membre_par_id(self, id_membre):
        self.curseur.execute("SELECT * FROM membres WHERE id_membre = ?", (id_membre,))
        res = self.curseur.fetchone()
        if res:
            membre = Membre(res[0], res[1], res[2])
            # On récupère ses livres en cours d'emprunt
            self.curseur.execute("SELECT isbn FROM emprunts WHERE id_membre = ? AND date_rendu IS NULL", (id_membre,))
            membre.livres_empruntes = [ligne[0] for ligne in self.curseur.fetchall()]
            return membre
        return None

    # --- EMPRUNT & RETOUR ---
    def emprunter_livre(self, isbn, id_membre):
        livre = self.trouver_livre_par_isbn(isbn)
        membre = self.trouver_membre_par_id(id_membre)

        if livre is None: return "Erreur : Livre introuvable"
        if membre is None: return "Erreur : Membre introuvable"
        if not livre.disponible: return "Erreur : Livre déjà emprunté"

        # Mise à jour du livre
        self.curseur.execute("UPDATE livres SET disponible = 0 WHERE isbn = ?", (isbn,))
        # Création de l'emprunt
        self.curseur.execute("INSERT INTO emprunts (isbn, id_membre, date_emprunt) VALUES (?, ?, ?)",
                             (isbn, id_membre, str(date.today())))
        self.conn.commit()
        return "Le livre a bien été emprunté !"

    def rendre_livre(self, isbn, id_membre):
        livre = self.trouver_livre_par_isbn(isbn)
        membre = self.trouver_membre_par_id(id_membre)

        if livre is None: return "Erreur : Livre introuvable"
        if membre is None: return "Erreur : Membre introuvable"
        if livre.disponible: return "Erreur : Ce livre est déjà disponible"
        if isbn not in membre.livres_empruntes: return "Erreur : Ce membre n'a pas ce livre"

        # Mise à jour du livre
        self.curseur.execute("UPDATE livres SET disponible = 1 WHERE isbn = ?", (isbn,))
        # Clôture de l'emprunt
        self.curseur.execute("""
            UPDATE emprunts SET date_rendu = ? 
            WHERE isbn = ? AND id_membre = ? AND date_rendu IS NULL
        """, (str(date.today()), isbn, id_membre))
        self.conn.commit()
        return "Succès : Le livre a bien été rendu !"

    # --- AFFICHAGES ---
    def afficher_livres(self):
        self.curseur.execute("SELECT * FROM livres")
        return [Livre(res[0], res[1], res[2], res[3], bool(res[4])) for res in self.curseur.fetchall()]

    def afficher_membres(self):
        self.curseur.execute("SELECT * FROM membres")
        membres = []
        for res in self.curseur.fetchall():
            m = Membre(res[0], res[1], res[2])
            self.curseur.execute("SELECT isbn FROM emprunts WHERE id_membre = ? AND date_rendu IS NULL", (m.id_membre,))
            m.livres_empruntes = [ligne[0] for ligne in self.curseur.fetchall()]
            membres.append(m)
        return membres

    def rechercher_livre(self, mot_cle):
        # %mot_cle% permet de chercher le mot n'importe où dans le titre ou l'auteur
        self.curseur.execute("SELECT * FROM livres WHERE titre LIKE ? OR auteur LIKE ?",
                             (f"%{mot_cle}%", f"%{mot_cle}%"))
        return [Livre(res[0], res[1], res[2], res[3], bool(res[4])) for res in self.curseur.fetchall()]

    def afficher_emprunts_en_cours(self):
        self.curseur.execute("SELECT isbn, id_membre, date_emprunt FROM emprunts WHERE date_rendu IS NULL")
        return [Emprunt(res[0], res[1], res[2], None) for res in self.curseur.fetchall()]
        







