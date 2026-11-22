from datetime import date
from models.emprunt import Emprunt
from models.livre import Livre
import json

from models.membre import Membre


class Bibliotheque:

    def __init__(self):
        self.livres = []
        self.membres = []
        self.emprunts = []
        self.disponible=[]
    def ajouter_livre(self,livre):
          self.livres.append(livre)

    def ajouter_membre(self,membre):
        self.membres.append(membre)

    def ajouter_emprunt(self,emprunt):
        self.emprunts.append(emprunt)

    def trouver_livre_par_isbn(self,isbn):
        for livre in self.livres:
            if livre.isbn==isbn:
                return livre
        return None


    def trouver_membre_par_id(self,id_membre):
        for membre in self.membres:
            if membre.id_membre == id_membre:
                return membre
        return None

    def emprunter_livre(self,isbn,id_membre):
        livre=self.trouver_livre_par_isbn(isbn)
        membre=self.trouver_membre_par_id(id_membre)

        if livre is None:
            return "Erreur:Livre introuvable"

        if membre is None:
            return "Erreur:Membre introuvable"

        if not livre.disponible:
            return "Erreur:Livre disponible"

        livre.disponible = False
        membre.livres_empruntes.append(isbn)

        nouvel_emprunt = Emprunt(isbn, id_membre, str(date.today()))
        self.ajouter_emprunt(nouvel_emprunt)
        return "Le livre a bien été emprunté !"

    def rendre_livre(self,isbn,id_membre):
        livre=self.trouver_livre_par_isbn(isbn)
        membre=self.trouver_membre_par_id(id_membre)
        if livre is None:
            return "Erreur : Livre introuvable"
        if membre is None:
            return "Erreur : Membre introuvable"
        if livre.disponible:
            return "Erreur : Ce livre est déjà dans la bibliothèque (non emprunté)."

        if isbn not in membre.livres_empruntes:
            return "Erreur : Ce membre n'a pas emprunté ce livre."
        livre.disponible = True
        membre.livres_empruntes.remove(isbn)
        for emprunt in self.emprunts:
            if emprunt.isbn == isbn and emprunt.id_membre == id_membre and emprunt.date_rendu is None:
             emprunt.cloturer(str(date.today()))  # On utilise ta méthode !
        return "Succès : Le livre a bien été rendu !"

    def sauvegarder_donnees(self):
        donnees = {
            "livres": [livre.to_dict() for livre in self.livres],
            "membres": [membre.to_dict() for membre in self.membres],
            "emprunts": [emprunt.to_dict() for emprunt in self.emprunts],
        }

        with open("data/donnees.json", "w", encoding="utf-8") as fichier:
            json.dump(donnees, fichier, indent=2, ensure_ascii=False)

    def charger_donnees(self):
        try:
            with open("data/donnees.json", "r", encoding="utf-8") as fichier:
                donnees = json.load(fichier)
            self.livres = [Livre.from_dict(l) for l in donnees.get("livres", [])]
            self.membres = [Membre.from_dict(m) for m in donnees.get("membres", [])]
            self.emprunts = [Emprunt.from_dict(e) for e in donnees.get("emprunts", [])]

        except FileNotFoundError:
            pass


    # 1. Afficher tous les livres
    def afficher_livres(self):
        return self.livres

    # 2. Rechercher un livre par titre ou auteur
    def rechercher_livre(self, mot_cle):
        resultats = []
        # On met tout en minuscules pour que la recherche ignore les majuscules
        mot_cle = mot_cle.lower()
        for livre in self.livres:
            if mot_cle in livre.titre.lower() or mot_cle in livre.auteur.lower():
                resultats.append(livre)
        return resultats

    # 3. Afficher tous les membres
    def afficher_membres(self):
        return self.membres

    # 4. Afficher les emprunts en cours
    def afficher_emprunts_en_cours(self):
        # On utilise la méthode est_en_cours() que tu avais écrite dans emprunt.py !
        return [emprunt for emprunt in self.emprunts if emprunt.est_en_cours()]

        







