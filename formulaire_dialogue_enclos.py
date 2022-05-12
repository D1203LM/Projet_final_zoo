####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Dimitri Lacroix-Moreau
###  No étudiant: 2041532
###  No Groupe: 01
###  Description du fichier: Description de la classe Fenetre_dialogue_enclos
####################################################################################

# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue
import dialogue_enclos

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def cacher_labels_erreur(object):
    """
    Cacher les différents labels d'erreur
    """
    object.label_erreur_numero_enclos.setVisible(False)

##############################################################
###### DÉFINITIONS DE LA CLASSE Fenetre_dialogue_enclos ######
##############################################################

class Fenetre_dialogue_enclos(QtWidgets.QDialog, dialogue_enclos.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param: QtWidgets.QDialog et dialogue_enclos.Ui_Dialog
        """
        # Appeler le constructeur parent avec ma classe en paramètre
        super(Fenetre_dialogue_enclos, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre animaux
        self.setWindowTitle("Animaux")
        # Cacher tous les labels d'erreur
        cacher_labels_erreur(self)

    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()