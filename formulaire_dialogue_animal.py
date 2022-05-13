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

# Importer les classes
from Serpent import *
from Oiseau import *
from Poisson import *

# Importer la liste des animaux
from liste_animaux import *

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def verifier_animal_liste(p_numero_nmal):
    """
    Vérifie si l'animal existe dans la liste des animaux
    :param p_numero_nmal: le numéro de l'animal
    :return: True si l'animal est trouvé dans la liste des animaux et False sinon
    """
    for elt in ls_Animaux:
        if elt.NumAnimal == p_numero_nmal.capitalize():
            return True
    return False

def cacher_labels_erreur(object):
    """
    Cacher les différents labels d'erreur
    """
    object.label_erreur_nmal_existe.setVisible(False)
    object.label_erreur_nmal_inexistant.setVisible(False)
    object.label_erreur_numero_nmal.setVisible(False)
    object.label_erreur_aucun_enclos.setVisible(False)
    object.label_erreur_poid_nmal.setVisible(False)
    object.label_erreur_longueur_bec.setVisible(False)
    object.label_erreur_longueur_poisson.setVisible(False)

##############################################################
###### DÉFINITIONS DE LA CLASSE Fenetre_dialogue_animal ######
##############################################################

# Créer une classe qui hérite de Qt et de notre ui.
# Nom de ma classe (fenetrePrincipal)            # Nom de mon fichier ui
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

    # Utiliser le décorateur ici pour empêcher que le code du gestionnaire d'événement du bouton ne s'éxecute deux fois
    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()

    # Bouton Ajouter
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un object Animal
        nmal = Animal()
        # Entrée de donnée pour les attributs de l'object Animal
        nmal.NumAnimal = self.lineEdit_numero_nmal.text().capitalize()
        nmal.PoidAnimal = float(self.lineEdit_poid_nmal.text())
        nmal.Espece_animal = self.comboBox_choix_nmal.currentText()
        nmal.Enclos = self.comboBox_enclos.currentText()
        # Booleen qui nous informe si le numéro de l'animal existe ou pas dans la liste des animaux
        verifier_animal = verifier_animal_liste(nmal.NumAnimal)
        # Instancier un objet Serpent
        serp = Serpent()
        # Entrée de donnée pour les attributs de l'object Serpent
        serp.NumAnimal = self.lineEdit_numero_nmal.text().capitalize()
        serp.PoidAnimal = float(self.lineEdit_poid_nmal.text())
        serp.Espece_animal = self.comboBox_espece_serpent.currentText()
        serp.Enclos = self.comboBox_enclos.currentText()
        serp.Couleur_ecailles = self.comboBox_couleur_serpent.currentText()
        serp.Venmieux = self.comboBox_venimeux.currentText()
        # Vérifier si le serpent existe ou pas dans la liste des animaux
        verifier_animal = verifier_animal_liste(serp.NumAnimal)
        # Instancier un object Oiseau
        ois = Oiseau()
        # Entrée de donnée pour les attributs de l'object Oiseau
        ois.NumAnimal = self.lineEdit_numero_nmal.text().capitalize()
        ois.PoidAnimal = float(self.lineEdit_poid_nmal.text())
        ois.Espece_animal = self.comboBox_espece_oiseau.currentText()
        ois.Enclos = self.comboBox_enclos.currentText()
        ois.Couleur_plumes = self.comboBox_couleur_oiseau.currentText()
        ois.LongueurBec = int(self.lineEdit_longueur_bec.text())
        # Vérifier si l'oiseau existe ou pas dans la liste des animaux
        verifier_animal = verifier_animal_liste(ois.NumAnimal)
        # Instancier un object Poisson
        poiss = Poisson()
        # Entrée de donnée pour les attributs de l'object Poisson
        poiss.NumAnimal = self.label_numero_nmal.text().capitalize()
        poiss.PoidAnimal = float(self.lineEdit_poid_nmal.text())
        poiss.Espece_animal = self.comboBox_espece_poisson.currentText()
        poiss.Enclos = self.comboBox_enclos.currentText()
        poiss.Couleur_ecailles = self.comboBox_couleur_poisson.currentText()
        poiss.LongueurPoisson = int(self.lineEdit_longueur_poisson.text())
        # Vérifier si le poisson existe ou pas dans la liste des animaux
        verifier_animal = verifier_animal_liste(poiss.NumAnimal)

        # Si le numéro de l'animal est valide mais existe déjà dans la liste des animaux (on ne peut donc pas l'ajouter)
        if verifier_animal is True:
            # Effacer le lineEdit du numéro animal et afficher le message d'erreur
            self.lineEdit_numero_nmal.clear()
            self.label_erreur_nmal_existe.setVisible(True)
        # Si le numéro de l'animal est invalide, effacer le lineEdit du numéro animal et affciher un message d'erreur
        if nmal.NumAnimal == "":
            self.lineEdit_numero_nmal.clear()
            self.label_erreur_numero_nmal.setVisible(True)
        # Si le poid de l'animal est invalide, afficher un message d'erreur
        if nmal.PoidAnimal == "":
            self.lineEdit_poid_nmal.clear()
            self.label_erreur_poid_nmal.setVisible(True)
        # Si les informations entrées sont valides et l'animal n'esxiste pas dans la liste des animaux
        if nmal.NumAnimal != "" and nmal.PoidAnimal != "" and nmal.Enclos != "" and ois.LongueurBec != "" and \
                poiss.LongueurPoisson != "" is False:
            # Ajouter l'object instancié à la liste des animaux
            nmal.serp.ois.poiss = nmal
            ls_Animaux.append(nmal)
            # Ajouter les informations de l'animal au TextBrowser
            self.textBrowser_afficher_animaux.append(nmal.__str__())
            # Réinitialiser les lineEdits
            self.lineEdit_numero_nmal.clear()
            self.lineEdit_poid_nmal.clear()
            self.lineEdit_longueur_bec.clear()
            self.lineEdit_longueur_poisson.clear()