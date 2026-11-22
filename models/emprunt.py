
class Emprunt:
    def __init__(self, isbn, id_membre, date_emprunt, date_rendu=None):
        self.isbn = isbn
        self.id_membre = id_membre
        self.date_emprunt = date_emprunt
        self.date_rendu = date_rendu

    def est_en_cours(self):
        return self.date_rendu is None