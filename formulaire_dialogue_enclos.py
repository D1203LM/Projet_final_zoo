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

# Importer les classes
from Serpent import *
from Oiseau import *
from Poisson import *
from Enclos import *

# Importer les listes
from liste_animaux import *
from liste_enclos import *

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def verifier_enclos_liste_(p_num_enclos):
    """
    Vérifie si l'enclos existe dans la liste des enclos
    :param p_num_enclos: le numéro de l'enclos
    :return: True si l'enclos est trouvé dans la liste des enclos et False sinon
    """
    for elt in ls_Enclos:
        if elt.NumEnclos == p_num_enclos.capitalize():
            return True
    return False

def cacher_labels_erreur(object):
    """
    Cacher les différents labels d'erreur
    """
    object.label_erreur_enclos_existe.setVisible(False)
    object.label_erreur_enclos_inexistant.setVisible(False)
    object.label_erreur_numero_enclos.setVisible(False)

##############################################################
###### DÉFINITIONS DE LA CLASSE Fenetre_dialogue_enclos ######
##############################################################

# Créer une classe qui hérite de Qt et de notre ui.
# Nom de ma classe (fenetrePrincipal)            # Nom de mon fichier ui
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

    # Utiliser le décorateur ici pour empêcher que le code du gestionnaire d'événement du bouton ne s'éxecute deux fois
    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()

    @pyqtSlot()
    # Bouton Ajouter
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un object Enclos
        enc = Enclos()
        # Entrée de donnée pour les attributs de l'object Enclos
        enc.NumEnclos = self.lineEdit_numero_enclos.text().capitalize()
        enc.Taille_enclos = self.comboBox_taille_enclos.currentText()
        enc.Lieu_enclos = self.comboBox_lieu_enclos.currentText()
        # Booleen qui nous informe si le numéro d'étudiant existe ou pas dans la liste des enclos
        verifier_enclos = verifier_enclos_liste_(enc.NumEnclos)
        # Si le numéro d'enclos est valide mais existe déjà dans la liste des enclos (on ne peut donc pas l'ajouter)
        if verifier_enclos is True:
            # Effacer le lineEdit du numéro d'enclos et afficher le mesage d'erreur
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_enclos_existe.setVisible(True)
        # Si le numéro de l'enclos est invalide, afficher le message d'ereur
        if enc.NumEnclos == "":
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos.setVisible(True)
        # Si les informations entrés sont valides et l'enclos n'existe pas dans la liste des enclos
        if enc.NumEnclos != "" and verifier_enclos is False:
            # Ajouter l'object instancié à la liste des enclos
            ls_Enclos.append(enc)
            # Ajouter les informations de l'enclos entré au textBrowser
            self.textBrowser_afficher_enclos.append(enc.__str__())
            # Réinitialiser le lineEdit du numéro d'enclos
            self.lineEdit_numero_enclos.clear()

    @pyqtSlot()
    # Bouton Modifier
    def on_pushButton_modifier_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Modifier
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un object Enclos
        enc = Enclos()
        # Entrée de donnée pour les attributs de l'object Enclos
        enc.NumEnclos = self.lineEdit_numero_enclos.text().capitalize()
        enc.Taille_enclos = self.comboBox_taille_enclos.currentText()
        enc.Lieu_enclos = self.comboBox_lieu_enclos.currentText()
        # Booleen qui nous informe si le numéro d'étudiant existe ou pas dans la liste des enclos
        verifier_enclos = verifier_enclos_liste_(enc.NumEnclos)
        # Vérifier si le numéro de l'enclos existe dans la liste des enclos
        if verifier_enclos is False and enc.NumEnclos != "":
            # Effacer le lineEdit du numéro de l'enclos et afficher le message d'erreur
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_enclos_inexistant.setVisible(True)
        # Si le numéro de l'enclos est invalide, afficher un message d'erreur
        if enc.NumEnclos == "":
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos.setVisible(True)
        # Si les informations entrées sont valides et l'enclos existe dans la liste des enclos
        if enc.NumEnclos != "" and verifier_enclos is True:
            for elt in ls_Enclos:
                # Chercher dans la liste des enclos un enclos ayant le numéro de l'enclos entré
                if elt.NumEnclos == self.lineEdit_numero_enclos.text().capitalize():
                    # Apporter les modifications aux attributs
                    elt.NumEnclos = self.lineEdit_numero_enclos.text().capitalize()
                    elt.Taille_enclos = self.comboBox_taille_enclos.currentText()
                    elt.Lieu_enclos = self.comboBox_lieu_enclos.currentText()
            # Effacer le textBrowser
            self.textBrowser_afficher_enclos.clear()
            # Après modifications, réafficher tous les enclos de la liste dans le textBrowser
            for elt in ls_Enclos:
                self.textBrowser_afficher_enclos.append(elt.__str__())
            # Réinitialiser lee lineEdit du numéro de l'enclos
            self.lineEdit_numero_enclos.clear()

    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_supprimer_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un object Enclos
        enc = Enclos()
        # Entrée de donnée pour les attributs de l'object Enclos
        enc.NumEnclos = self.lineEdit_numero_enclos.text().capitalize()
        enc.Taille_enclos = self.comboBox_taille_enclos.currentText()
        enc.Lieu_enclos = self.comboBox_lieu_enclos.currentText()
        # Booleen qui nous informe si le numéro d'étudiant existe ou pas dans la liste des enclos
        verifier_enclos = verifier_enclos_liste_(enc.NumEnclos)
        # Si le numéro de l'enclos est valide et l'enclos existe dans la liste des enclos
        if enc.NumEnclos != "" and verifier_enclos is True:
            trouve = False
            for elt in ls_Enclos:
                # Chercher dans la liste des enclos un enclos ayant l'information entrée
                if elt.NumEnclos == self.lineEdit_numero_enclos.text():
                    # Supprimer l'enclos de la liste des enclos
                    trouve = True
                    ls_Enclos.remove(elt)
                    break
            # Si l'enclos n'existe pas dans la liste, afficher un message d'erreur
            if not trouve:
                self.label_erreur_enclos_inexistant.setVisible(True)
            else:
                # Réafficher dans le textBrowser la nouvelle liste qui ne contient pas l'enclos supprimé
                self.textBrowser_afficher_enclos.clear()
                for elt in ls_Enclos:
                    self.textBrowser_afficher_enclos.append(elt.__str__())
                # Réinitialiser  le lineEdit du numéro de l'enclos
                self.lineEdit_numero_enclos.clear()
        # Si le numéro de l'enclos n'existe pas dans la liste, afficher un message d'erreur
        if verifier_enclos is False and enc.NumEnclos != "":
            # Effacer le lineEdit du numéro de l'enclos et afficher le message d'erreur
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_enclos_inexistant.setVisible(True)
        # Si le numéro est invalide, afficher un message d'erreur
        if enc.NumEnclos == "":
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos.setVisible(True)