class Livre:
    def __init__(self, isbn, titre, auteur, maison_edition, disponible=True):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.maison_edition = maison_edition
        self.disponible = disponible