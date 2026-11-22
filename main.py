from models.bibliotheque import Bibliotheque
from views.vue_console import VueConsole
from controllers.controleur_principal import Controleur

if __name__ == "__main__":
    biblio = Bibliotheque()
    biblio.charger_donnees()
    vue = VueConsole()
    controleur = Controleur(biblio, vue)
    controleur.demarrer()

















