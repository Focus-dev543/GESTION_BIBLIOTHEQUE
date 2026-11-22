class Membre:
    def __init__(self,id_membre,nom,prenoms,livres_empruntes=None):
        self.id_membre=id_membre
        self.nom=nom
        self.prenoms=prenoms
        if livres_empruntes is None:
            livres_empruntes=[]
        self.livres_empruntes=livres_empruntes

    def to_dict(self):
        return {"id_membre":self.id_membre,"nom":self.nom,"prenoms":self.prenoms,"livres_empruntes":self.livres_empruntes}

    @staticmethod
    def from_dict(donnees):
        return Membre(donnees["id_membre"],donnees["nom"],donnees["prenoms"],
                      donnees["livres_empruntes"])

