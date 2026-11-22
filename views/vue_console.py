class VueConsole:

    def afficher_menu(self):
        print("\n" + "=" * 30)
        print("   GESTION DE BIBLIOTHÈQUE")
        print("=" * 30)
        print("1. Ajouter un livre")
        print("2. Afficher les livres")
        print("3. Rechercher un livre")
        print("4. Inscrire un membre")
        print("5. Afficher les membres")
        print("6. Emprunter un livre")
        print("7. Rendre un livre")
        print("8. Afficher les emprunts en cours")
        print("0. Quitter")
        print("=" * 30)

    def demander_choix(self):
        return input("Votre choix : ")

    def afficher_message(self, message):
        print(f"\n>>> {message}")

    def demander_infos_livre(self):
        print("\n--- Nouveau Livre ---")
        isbn = input("ISBN : ")
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        maison_edition = input("Maison d'édition : ")
        return {"isbn": isbn, "titre": titre, "auteur": auteur, "maison_edition": maison_edition}

    def demander_infos_membre(self):
        print("\n--- Nouveau Membre ---")
        id_membre = input("ID du membre : ")
        nom = input("Nom : ")
        prenoms = input("Prénoms : ")
        return {"id_membre": id_membre, "nom": nom, "prenoms": prenoms}

    def demander_chaine(self, message):
        return input(message)