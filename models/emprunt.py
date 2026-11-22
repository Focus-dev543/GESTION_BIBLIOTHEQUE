class Emprunt:
    def __init__(self,isbn,id_membre,date_emprunt,date_rendu=None):
        self.isbn = isbn
        self.id_membre = id_membre
        self.date_emprunt = date_emprunt
        self.date_rendu = date_rendu

    def est_en_cours(self):
        if self.date_rendu is None:
            return True
        else:return False

    def cloturer(self,date_rendu):
        self.date_rendu = date_rendu

    def to_dict(self):
        return {"isbn":self.isbn,"id_membre":self.id_membre,"date_emprunt":self.date_emprunt,
                "date_rendu":self.date_rendu}

    @staticmethod
    def from_dict(donnees):
        return Emprunt(donnees["isbn"],donnees["id_membre"],donnees["date_emprunt"],
                       donnees["date_rendu"])