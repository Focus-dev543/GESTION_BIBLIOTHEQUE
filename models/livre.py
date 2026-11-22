class Livre:
    def __init__(self,isbn,titre,auteur,maison_edition,
                 disponible=True):
        self.isbn= isbn
        self.titre= titre
        self.auteur= auteur
        self.maison_edition= maison_edition
        self.disponible=disponible

    def to_dict(self):
        return{"isbn":self.isbn,"titre":self.titre,"auteur":self.auteur,"maison_edition":self.maison_edition,
               "disponible":self.disponible}
    @staticmethod
    def from_dict(donnees):
        return Livre(donnees["isbn"],donnees["titre"],donnees["auteur"],donnees["maison_edition"]
                     ,donnees["disponible"])