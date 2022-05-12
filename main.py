####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Dimitri Lacroix-Moreau
###  No étudiant: 2041532
###  No Groupe: 01
###  Description du fichier: Programme principal
####################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
########+##############################

# Importer le module sys nécessaire à l'exécution.
import sys

# importer les interfaces graphiques
import interface_graphique_zoo
from formulaire_dialogue_animal import *
from formulaire_dialogue_enclos import *

# importer les classes
from Animal import *
from Serpent import *
from Oiseau import *
from Poisson import *

##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################

# Déclarer une liste d'animaux
ls_Animaux = []

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def verifier_animal_liste(p_num_animal):
    """
    Vérifie si l'animal existe dans la liste des animaux
    :param p_num:  le numéro de l'animal
    :return: True si l'animal est trouvé dans la liste des étudiants et False sinon
    """
    for elt in ls_Animaux:
        if elt.NumAnimal == p_num_animal.capitalize():
            return True
    return False



########################################################
###### DÉFINITIONS DE LA CLASSE FenetrePrincipale ######
########################################################

# Créer une classe qui hérite de Qt et de notre ui.
class FenetrePrincipale(QtWidgets.QMainWindow, interface_graphique_zoo.Ui_MainWindow):
    """
    Nom de la classe : FenetrePrincipale
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - interface_graphique_zoo.Ui_MainWindow : Ma classe généré avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et interfcae_graphique_zoo.Ui_MainWindow
        """
        # Appeler le constructeur parent avec ma classe en paramètre
        super(FenetrePrincipale, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre principale
        self.setWindowTitle("Gestion du zoo")

    # Utiliser le décorateur ici pour empêcher que le code du gestionnaire d'événement du bouton ne s'éxecute deux fois
    @pyqtSlot()
    def on_pushButton_animal_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Animal
        """
        # Instancier une boite de dialogue Fenetre_dialogue_animal
        dialog = Fenetre_dialogue_animal()
        # Afficher la boite de dialogue
        dialog.show()
        reply = dialog.exec_()

    @pyqtSlot()
    def on_pushButton_enclos_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Enclos
        """
        # Instancier une boite de dialogue Fenetre_dialogue_enclos
        dialog = Fenetre_dialogue_enclos()
        # Afficher la boite de dialogue
        dialog.show()
        reply = dialog.exec_()

    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()


#################################
###### PROGRAMME PRINCIPAL ######
#################################

# Créer le main qui lance la fenêtre de Qt

def main():
    """
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    reply = Dialog.exec_()
    """
    # Instancier une application et une fenetre principale
    app = QtWidgets.QApplication(sys.argv)
    form = FenetrePrincipale()
    # Afficher la fenêtre principale
    form.show()
    # Lancer l'application
    app.exec()

if __name__ == "__main__":
    main()