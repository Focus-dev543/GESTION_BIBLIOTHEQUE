class Membre:
    def __init__(self, id_membre, nom, prenoms):
        self.id_membre = id_membre
        self.nom = nom
        self.prenoms = prenoms
        self.livres_empruntes = [] # On garde l'attribut pour l'affichage, mais on le remplira via SQL