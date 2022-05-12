####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Dimitri Lacroix-Moreau
###  No étudiant: 2041532
###  No Groupe: 01
###  Description du fichier: Description de la classe Fenetre_dialogue_animal
####################################################################################

# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue
import dialogue_animal

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def cacher_labels_erreur(object):
    """
    Cacher les différents labels d'erreur
    """
    object.label_erreur_nmal_existe.setVisible(False)
    object.label_erreur_nmal_inexistant.setVisible(False)
    object.label_erreur_numero_nmal.setVisible(False)
    object.label_erreur_aucun_enclos.setVisible(False)
    object.label_erreur_poid_serpent.setVisible(False)
    object.label_erreur_poid_oiseau.setVisible(False)
    object.label_erreur_poid_poisson.setVisible(False)

##############################################################
###### DÉFINITIONS DE LA CLASSE Fenetre_dialogue_animal ######
##############################################################

class Fenetre_dialogue_animal(QtWidgets.QDialog, dialogue_animal.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param: QtWidgets.QDialog et dialogue_animal.Ui_Dialog
        """
        # Appeler le constructeur parent avec ma classe en paramètre
        super(Fenetre_dialogue_animal, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre animaux
        self.setWindowTitle("Animaux")
        # Cacher tous les labels d'erreur
        cacher_labels_erreur(self)

    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()