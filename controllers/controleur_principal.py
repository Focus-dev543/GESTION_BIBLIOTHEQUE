from models.livre import Livre
from models.membre import Membre

class Controleur:
    def __init__(self, biblio, vue):
        self.biblio = biblio
        self.vue = vue

    def demarrer(self):
        while True:
            self.vue.afficher_menu()
            choix = self.vue.demander_choix()

            if choix == "1":
                infos = self.vue.demander_infos_livre()
                nouveau_livre = Livre(infos["isbn"], infos["titre"], infos["auteur"], infos["maison_edition"])
                # On ajoute le livre (la sauvegarde SQL est automatique)
                self.biblio.ajouter_livre(nouveau_livre)
                self.vue.afficher_message("Livre ajouté avec succès !")

            elif choix == "2":
                livres = self.biblio.afficher_livres()
                if not livres:
                    self.vue.afficher_message("Aucun livre dans la bibliothèque.")
                else:
                    self.vue.afficher_message("--- Liste des livres ---")
                    for l in livres:
                        statut = "Disponible" if l.disponible else "Emprunté"
                        self.vue.afficher_message(f"[{l.isbn}] {l.titre} par {l.auteur} - Statut : {statut}")

            elif choix == "3":
                mot_cle = self.vue.demander_chaine("Entrez un titre ou un auteur : ")
                resultats = self.biblio.rechercher_livre(mot_cle)
                if not resultats:
                    self.vue.afficher_message("Aucun livre ne correspond à votre recherche.")
                else:
                    self.vue.afficher_message("--- Résultats de la recherche ---")
                    for l in resultats:
                        statut = "Disponible" if l.disponible else "Emprunté"
                        self.vue.afficher_message(f"[{l.isbn}] {l.titre} par {l.auteur} - Statut : {statut}")

            elif choix == "4":
                infos = self.vue.demander_infos_membre()
                nouveau_membre = Membre(infos["id_membre"], infos["nom"], infos["prenoms"])
                # On ajoute le membre (la sauvegarde SQL est automatique)
                self.biblio.ajouter_membre(nouveau_membre)
                self.vue.afficher_message("Membre inscrit avec succès !")

            elif choix == "5":
                membres = self.biblio.afficher_membres()
                if not membres:
                    self.vue.afficher_message("Aucun membre inscrit.")
                else:
                    self.vue.afficher_message("--- Liste des membres ---")
                    for m in membres:
                        self.vue.afficher_message(f"[{m.id_membre}] {m.nom} {m.prenoms} - Livres empruntés : {len(m.livres_empruntes)}")

            elif choix == "6":
                isbn = self.vue.demander_chaine("Entrez l'ISBN du livre : ")
                id_membre = self.vue.demander_chaine("Entrez l'ID du membre : ")
                resultat = self.biblio.emprunter_livre(isbn, id_membre)
                # Plus besoin de tester "startswith('Erreur')", on affiche juste le résultat
                self.vue.afficher_message(resultat)

            elif choix == "7":
                isbn = self.vue.demander_chaine("Entrez l'ISBN du livre à rendre : ")
                id_membre = self.vue.demander_chaine("Entrez l'ID du membre : ")
                resultat = self.biblio.rendre_livre(isbn, id_membre)
                # Plus besoin de tester "startswith('Erreur')"
                self.vue.afficher_message(resultat)

            elif choix == "8":
                emprunts = self.biblio.afficher_emprunts_en_cours()
                if not emprunts:
                    self.vue.afficher_message("Aucun emprunt en cours.")
                else:
                    self.vue.afficher_message("--- Emprunts en cours ---")
                    for e in emprunts:
                        self.vue.afficher_message(f"Livre ISBN: {e.isbn} | Membre ID: {e.id_membre} | Date: {e.date_emprunt}")

            elif choix == "0":
                # On ne sauvegarde plus manuellement
                self.vue.afficher_message("Fermeture du programme...")
                break

            else:
                self.vue.afficher_message("Choix invalide, veuillez réessayer.")