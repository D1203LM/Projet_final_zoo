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
from liste_enclos import *

#variable
choix_animal = ""
#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def verifier_animal_liste(p_num_animal):
    """
    Vérifie si l'animal existe dans la liste des animaux
    :param p_num_animal: le numéro de l'animal
    :return: True si l'animal est trouvé dans la liste des animaux et False sinon
    """
    for elt in ls_Animaux:
        if elt.NumAnimal == p_num_animal.capitalize():
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

def desactiver_widgets_animaux(object):
    object.label_serpent.setEnabled(False)
    object.label_espece_serpent.setEnabled(False)
    object.label_couleur_serpent.setEnabled(False)
    object.label_venimeux.setEnabled(False)
    object.comboBox_espece_serpent.setEnabled(False)
    object.comboBox_couleur_serpent.setEnabled(False)
    object.comboBox_venimeux.setEnabled(False)
    object.pushButton_serialiser.setEnabled(False)
    object.pushButton_deserialiser.setEnabled(False)
    object.label_oiseau.setEnabled(False)
    object.label_espece_oiseau.setEnabled(False)
    object.label_couleur_oiseau.setEnabled(False)
    object.label_longueur_bec.setEnabled(False)
    object.comboBox_espece_oiseau.setEnabled(False)
    object.comboBox_couleur_oiseau.setEnabled(False)
    object.lineEdit_longueur_bec.setEnabled(False)
    object.label_poisson.setEnabled(False)
    object.label_espece_poisson.setEnabled(False)
    object.label_couleur_poisson.setEnabled(False)
    object.label_longueur_poisson.setEnabled(False)
    object.comboBox_espece_poisson.setEnabled(False)
    object.comboBox_couleur_poisson.setEnabled(False)
    object.lineEdit_longueur_poisson.setEnabled(False)


def activer_widgets_serpent(object):
    object.label_serpent.setEnabled(True)
    object.label_espece_serpent.setEnabled(True)
    object.label_couleur_serpent.setEnabled(True)
    object.label_venimeux.setEnabled(True)
    object.comboBox_espece_serpent.setEnabled(True)
    object.comboBox_couleur_serpent.setEnabled(True)
    object.comboBox_venimeux.setEnabled(True)
    object.pushButton_serialiser.setEnabled(True)
    object.pushButton_deserialiser.setEnabled(True)

def desactiver_widgets_serpent(object):
    object.label_serpent.setEnabled(False)
    object.label_espece_serpent.setEnabled(False)
    object.label_couleur_serpent.setEnabled(False)
    object.label_venimeux.setEnabled(False)
    object.comboBox_espece_serpent.setEnabled(False)
    object.comboBox_couleur_serpent.setEnabled(False)
    object.comboBox_venimeux.setEnabled(False)
    object.pushButton_serialiser.setEnabled(False)
    object.pushButton_deserialiser.setEnabled(False)

def activer_widgets_oiseau(object):
    object.label_oiseau.setEnabled(True)
    object.label_espece_oiseau.setEnabled(True)
    object.label_couleur_oiseau.setEnabled(True)
    object.label_longueur_bec.setEnabled(True)
    object.comboBox_espece_oiseau.setEnabled(True)
    object.comboBox_couleur_oiseau.setEnabled(True)
    object.lineEdit_longueur_bec.setEnabled(True)

def desactiver_widgets_oiseau(object):
    object.label_oiseau.setEnabled(False)
    object.label_espece_oiseau.setEnabled(False)
    object.label_couleur_oiseau.setEnabled(False)
    object.label_longueur_bec.setEnabled(False)
    object.comboBox_espece_oiseau.setEnabled(False)
    object.comboBox_couleur_oiseau.setEnabled(False)
    object.lineEdit_longueur_bec.setEnabled(False)

def activer_widgets_poisson(object):
    object.label_poisson.setEnabled(True)
    object.label_espece_poisson.setEnabled(True)
    object.label_couleur_poisson.setEnabled(True)
    object.label_longueur_poisson.setEnabled(True)
    object.comboBox_espece_poisson.setEnabled(True)
    object.comboBox_couleur_poisson.setEnabled(True)
    object.lineEdit_longueur_poisson.setEnabled(True)

def desactiver_widgets_poisson(object):
    object.label_poisson.setEnabled(False)
    object.label_espece_poisson.setEnabled(False)
    object.label_couleur_poisson.setEnabled(False)
    object.label_longueur_poisson.setEnabled(False)
    object.comboBox_espece_poisson.setEnabled(False)
    object.comboBox_couleur_poisson.setEnabled(False)
    object.lineEdit_longueur_poisson.setEnabled(False)

def charger_enclos(object):
    for elt in ls_Enclos:
        object.comboBox_enclos.addItem(elt.NumEnclos)

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
        # Désactiver les widgets des animaux
        desactiver_widgets_animaux(self)
        # charger la comboBox_enclos à partir de la liste enclos
        charger_enclos(self)


    # Utiliser le décorateur ici pour empêcher que le code du gestionnaire d'événement du bouton ne s'éxecute deux fois
    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()

    # Bouton Ajouter
    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        global choix_animal
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet Serpent
        if choix_animal == "Serpent":
            serp = Serpent()
            # Entrée de donnée pour les attributs de l'object Serpent
            serp.NumAnimal = self.lineEdit_numero_nmal.text().capitalize()
            serp.PoidAnimal = float(self.lineEdit_poid_nmal.text())
            serp.Espece_animal = self.comboBox_espece_serpent.currentText()
            mon_enclos = Enclos()
            for elt in ls_Enclos:
                if self.comboBox_enclos.currentText()== elt.NumEnclos :
                    mon_enclos = elt
            serp.Enclos = mon_enclos
            serp.Couleur_ecailles = self.comboBox_couleur_serpent.currentText()
            serp.Venimeux = self.comboBox_venimeux.currentText()
            # Vérifier si le serpent existe ou pas dans la liste des animaux
            verifier_animal = verifier_animal_liste(serp.NumAnimal)
        # Si le numéro du serpent est valide mais existe déjà dans la liste des animaux (on ne peut donc pas l'ajouter)
            if verifier_animal is True:
                # Effacer le lineEdit du numéro animal et afficher le message d'erreur
                self.lineEdit_numero_nmal.clear()
                self.label_erreur_nmal_existe.setVisible(True)
            # Si le numéro du serpent est invalide, effacer le lineEdit du numéro animal et affciher un message d'erreur
            if serp.NumAnimal == "":
                self.lineEdit_numero_nmal.clear()
                self.label_erreur_numero_nmal.setVisible(True)
            # Si le poid du serpent est invalide, afficher un message d'erreur
            if serp.PoidAnimal == "":
                self.lineEdit_poid_nmal.clear()
                self.label_erreur_poid_nmal.setVisible(True)
            # Si les informations entrées sont valides et l'animal n'esxiste pas dans la liste des animaux
            if serp.NumAnimal != "" and serp.PoidAnimal != "" :
                # Ajouter l'object instancié à la liste des animaux
                ls_Animaux.append(serp)
                # Ajouter les informations de l'animal au TextBrowser
                self.textBrowser_afficher_animaux.append(serp.__str__())
                # Réinitialiser les lineEdits
                self.lineEdit_numero_nmal.clear()
                self.lineEdit_poid_nmal.clear()
        # Instancier un object Oiseau
        if choix_animal == "Oiseau":
            ois = Oiseau()
            # Entrée de donnée pour les attributs de l'object Oiseau
            ois.NumAnimal = self.lineEdit_numero_nmal.text().capitalize()
            ois.PoidAnimal = float(self.lineEdit_poid_nmal.text())
            ois.Espece_animal = self.comboBox_espece_oiseau.currentText()
            mon_enclos = Enclos()
            for elt in ls_Enclos:
                if self.comboBox_enclos.currentText() == elt.NumEnclos:
                    mon_enclos = elt
            ois.Enclos = mon_enclos
            ois.Couleur_plumes = self.comboBox_couleur_oiseau.currentText()
            ois.LongueurBec = int(self.lineEdit_longueur_bec.text())
            # Vérifier si l'oiseau existe ou pas dans la liste des animaux
            verifier_animal = verifier_animal_liste(ois.NumAnimal)
        # Si le numéro du serpent est valide mais existe déjà dans la liste des animaux (on ne peut donc pas l'ajouter)
            if verifier_animal is True:
                # Effacer le lineEdit du numéro animal et afficher le message d'erreur
                self.lineEdit_numero_nmal.clear()
                self.label_erreur_nmal_existe.setVisible(True)
            # Si le numéro de l'oiseau est invalide, effacer le lineEdit du numéro animal et affciher un message d'erreur
            if ois.NumAnimal == "":
                self.lineEdit_numero_nmal.clear()
                self.label_erreur_numero_nmal.setVisible(True)
            # Si le poid de l'oiseau est invalide, afficher un message d'erreur
            if ois.PoidAnimal == "":
                self.lineEdit_poid_nmal.clear()
                self.label_erreur_poid_nmal.setVisible(True)
            # Si les informations entrées sont valides et l'animal n'esxiste pas dans la liste des animaux
            if ois.NumAnimal != "" and ois.PoidAnimal != "" and ois.LongueurBec != "":
                # Ajouter l'object instancié à la liste des animaux
                ls_Animaux.append(ois)
                # Ajouter les informations de l'animal au TextBrowser
                self.textBrowser_afficher_animaux.append(ois.__str__())
                # Réinitialiser les lineEdits
                self.lineEdit_numero_nmal.clear()
                self.lineEdit_poid_nmal.clear()
                self.lineEdit_longueur_bec.clear()
        # Instancier un object Poisson
        if choix_animal == "Poisson":
            poiss = Poisson()
            # Entrée de donnée pour les attributs de l'object Poisson
            poiss.NumAnimal = self.lineEdit_numero_nmal.text().capitalize()
            poiss.PoidAnimal = float(self.lineEdit_poid_nmal.text())
            poiss.Espece_animal = self.comboBox_espece_poisson.currentText()
            mon_enclos = Enclos()
            for elt in ls_Enclos:
                if self.comboBox_enclos.currentText() == elt.NumEnclos:
                    mon_enclos = elt
            poiss.Enclos = mon_enclos
            poiss.Couleur_ecailles = self.comboBox_couleur_poisson.currentText()
            poiss.LongueurPoisson = int(self.lineEdit_longueur_poisson.text())
            # Vérifier si le poisson existe ou pas dans la liste des animaux
            verifier_animal = verifier_animal_liste(poiss.NumAnimal)
        # Si le numéro du poisson est valide mais existe déjà dans la liste des animaux (on ne peut donc pas l'ajouter)
            if verifier_animal is True:
                # Effacer le lineEdit du numéro animal et afficher le message d'erreur
                self.lineEdit_numero_nmal.clear()
                self.label_erreur_nmal_existe.setVisible(True)
            # Si le numéro du poisson est invalide, effacer le lineEdit du numéro animal et affciher un message d'erreur
            if poiss.NumAnimal == "":
                self.lineEdit_numero_nmal.clear()
                self.label_erreur_numero_nmal.setVisible(True)
            # Si le poid du poisson est invalide, afficher un message d'erreur
            if poiss.PoidAnimal == "":
                self.lineEdit_poid_nmal.clear()
                self.label_erreur_poid_nmal.setVisible(True)
            # Si les informations entrées sont valides et l'animal n'esxiste pas dans la liste des animaux
            if poiss.NumAnimal != "" and poiss.PoidAnimal != "" and poiss.LongueurPoisson != "":
                # Ajouter l'object instancié à la liste des animaux
                ls_Animaux.append(poiss)
                # Ajouter les informations de l'animal au TextBrowser
                self.textBrowser_afficher_animaux.append(poiss.__str__())
                # Réinitialiser les lineEdits
                self.lineEdit_numero_nmal.clear()
                self.lineEdit_poid_nmal.clear()
                self.lineEdit_longueur_poisson.clear()

    @pyqtSlot()
    # Bouton Modifier
    def on_pushButton_modifier_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Modifier
        """
        global choix_animal
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet Serpent
        if choix_animal == "Serpent":
            serp = Serpent()
            # Entrée de donnée pour les attributs de l'object Serpent
            serp.NumAnimal = self.lineEdit_numero_nmal.text().capitalize()
            serp.PoidAnimal = float(self.lineEdit_poid_nmal.text())
            serp.Espece_animal = self.comboBox_espece_serpent.currentText()
            mon_enclos = Enclos()
            for elt in ls_Enclos:
                if self.comboBox_enclos.currentText() == elt.NumEnclos:
                    mon_enclos = elt
            serp.Enclos = mon_enclos
            serp.Couleur_ecailles = self.comboBox_couleur_serpent.currentText()
            serp.Venimeux = self.comboBox_venimeux.currentText()
            # Vérifier si le serpent existe ou pas dans la liste des animaux
            verifier_animal = verifier_animal_liste(serp.NumAnimal)
            # Vérifier si le numéro de l'animal existe dans la liste des animaux
            if verifier_animal is False and serp.NumAnimal != "":
                # Effacer le lineEdit du numéro de l'animal et afficher le message d'erreur
                self.lineEdit_numero_nmal.clear()
                self.label_erreur_nmal_inexistant.setVisible(True)
            # Si le poid du serpent est invalide, afficher un message d'erreur
            if serp.PoidAnimal == "":
                self.lineEdit_poid_nmal.clear()
                self.label_erreur_poid_nmal.setVisible(True)
            # Si les informations sont valides et l'animal existe dans la liste des animaux
            if serp.NumAnimal != "" and serp.PoidAnimal != "" and verifier_animal is True:
                for elt in ls_Animaux:
                    # Chercher dans la liste des animaux un animal ayant le numéro d'animal entré
                    if elt.NumAnimal == self.lineEdit_numero_nmal.text():
                        # Apporter les modifications aux attributs
                        elt.PoidAnimal = self.lineEdit_poid_nmal.text()
                        elt.Enclos = self.comboBox_enclos.currentText()
                        elt.Espece_animal = self.comboBox_espece_serpent.currentText()
                        elt.Couleur_ecailles = self.comboBox_couleur_serpent.currentText()
                        elt.Venimeux = self.comboBox_venimeux.currentText()
                # Effacer le textBrowser
                self.textBrowser_afficher_animaux.clear()
                # Après modifications, réafficher tous les animaux de la liste dans le textBrowser
                for elt in ls_Animaux:
                    self.textBrowser_afficher_animaux.append(elt.__str__())
                # Réinitialiser les lineEdits du numéro de l'animal et du poid
                self.lineEdit_numero_nmal.clear()
                self.lineEdit_poid_nmal.clear()
        # Instancier un object Oiseau
        if choix_animal == "Oiseau":
            ois = Oiseau()
            # Entrée de donnée pour les attributs de l'object Oiseau
            ois.NumAnimal = self.lineEdit_numero_nmal.text().capitalize()
            ois.PoidAnimal = float(self.lineEdit_poid_nmal.text())
            ois.Espece_animal = self.comboBox_espece_oiseau.currentText()
            mon_enclos = Enclos()
            for elt in ls_Enclos:
                if self.comboBox_enclos.currentText() == elt.NumEnclos:
                    mon_enclos = elt
            ois.Enclos = mon_enclos
            ois.Couleur_plumes = self.comboBox_couleur_oiseau.currentText()
            ois.LongueurBec = int(self.lineEdit_longueur_bec.text())
            # Vérifier si l'oiseau existe ou pas dans la liste des animaux
            verifier_animal = verifier_animal_liste(ois.NumAnimal)
            # Vérifier si le numéro de l'animal existe dans la liste des animaux
            if verifier_animal is False and ois.NumAnimal != "":
                # Effacer le lineEdit du numéro de l'animal et afficher le message d'erreur
                self.lineEdit_numero_nmal.clear()
                self.label_erreur_nmal_inexistant.setVisible(True)
            # Si le poid de l'oiseau est invalide, afficher un message d'erreur
            if ois.PoidAnimal == "":
                self.lineEdit_poid_nmal.clear()
                self.label_erreur_poid_nmal.setVisible(True)
            # Si la longueur du bec d'un oiseau est invalide, afficher un message d'erreur
            if ois.LongueurBec == "":
                self.lineEdit_longueur_bec.clear()
                self.label_erreur_longueur_bec.setVisible(True)
            # Si les informations sont valides et l'animal existe dans la liste des animaux
            if ois.NumAnimal != "" and ois.PoidAnimal != "" and ois.LongueurBec != "" and verifier_animal is True:
                for elt in ls_Animaux:
                    # Chercher dans la liste des animaux un animal ayant le numéro d'animal entré
                    if elt.NumAnimal == self.lineEdit_numero_nmal.text():
                        # Apporter les modifications aux attributs
                        elt.PoidAnimal = self.lineEdit_poid_nmal.text()
                        elt.Enclos = self.comboBox_enclos.currentText()
                        elt.Couleur_plumes = self.comboBox_couleur_oiseau.currentText()
                        elt.Espece_animal = self.comboBox_espece_oiseau.currentText()
                        elt.LongueurBec = self.lineEdit_longueur_bec.text()
                # Effacer le textBrowser
                self.textBrowser_afficher_animaux.clear()
                # Après modifications, réafficher tous les animaux de la liste dans le textBrowser
                for elt in ls_Animaux:
                    self.textBrowser_afficher_animaux.append(elt.__str__())
                # Réinitialiser les lineEdits du numéro de l'animal, du poid et du bec
                self.lineEdit_numero_nmal.clear()
                self.lineEdit_poid_nmal.clear()
                self.lineEdit_longueur_bec.clear()
        # Instancier un object Poisson
        if choix_animal == "Poisson":
            poiss = Poisson()
            # Entrée de donnée pour les attributs de l'object Poisson
            poiss.NumAnimal = self.label_numero_nmal.text().capitalize()
            poiss.PoidAnimal = float(self.lineEdit_poid_nmal.text())
            poiss.Espece_animal = self.comboBox_espece_poisson.currentText()
            mon_enclos = Enclos()
            for elt in ls_Enclos:
                if self.comboBox_enclos.currentText() == elt.NumEnclos:
                    mon_enclos = elt
            poiss.Enclos = mon_enclos
            poiss.Couleur_ecailles = self.comboBox_couleur_poisson.currentText()
            poiss.LongueurPoisson = int(self.lineEdit_longueur_poisson.text())
            # Vérifier si le poisson existe ou pas dans la liste des animaux
            verifier_animal = verifier_animal_liste(poiss.NumAnimal)
        # Vérifier si le numéro de l'animal existe dans la liste des animaux
        if verifier_animal is False and poiss.NumAnimal != "":
            # Effacer le lineEdit du numéro de l'animal et afficher le message d'erreur
            self.lineEdit_numero_nmal.clear()
            self.label_erreur_nmal_inexistant.setVisible(True)
        # Si le poid du poisson est invalide, afficher un message d'erreur
        if poiss.PoidAnimal == "":
            self.lineEdit_poid_nmal.clear()
            self.label_erreur_poid_nmal.setVisible(True)
        # Si la longueur du poisson est invalide, afficher un message d'erreur
        if poiss.LongueurPoisson == "":
            self.lineEdit_longueur_poisson.clear()
            self.label_erreur_longueur_poisson.setVisible(True)
        # Si les informations sont valides et l'animal existe dans la liste des animaux
        if poiss.NumAnimal != "" and poiss.PoidAnimal != "" and poiss.LongueurPoisson != "" and verifier_animal is True:
            for elt in ls_Animaux:
                # Chercher dans la liste des animaux un animal ayant le numéro d'animal entré
                if elt.NumAnimal == self.lineEdit_numero_nmal.text():
                    # Apporter les modifications aux attributs
                    elt.PoidAnimal = self.lineEdit_poid_nmal.text()
                    elt.Enclos = self.comboBox_enclos.currentText()
                    elt.Espece_animal = self.comboBox_couleur_poisson.currentText()
                    elt.Couleur_ecailles = self.comboBox_couleur_poisson.currentText()
                    elt.LongueurPoisson = self.lineEdit_longueur_poisson.text()
            # Effacer le textBrowser
            self.textBrowser_afficher_animaux.clear()
            # Après modifications, réafficher tous les animaux de la liste dans le textBrowser
            for elt in ls_Animaux:
                self.textBrowser_afficher_animaux.append(elt.__str__())
            # Réinitialiser les lineEdits du numéro de l'animal, du poid, du bec de l'oiseau et longueur du poisson
            self.lineEdit_numero_nmal.clear()
            self.lineEdit_poid_nmal.clear()
            self.lineEdit_longueur_poisson.clear()

    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_supprimer_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        global choix_animal
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet Serpent
        if choix_animal == "Serpent":
            serp = Serpent()
            # Entrée de donnée pour les attributs de l'object Serpent
            serp.NumAnimal = self.lineEdit_numero_nmal.text().capitalize()
            serp.PoidAnimal = float(self.lineEdit_poid_nmal.text())
            serp.Espece_animal = self.comboBox_espece_serpent.currentText()
            mon_enclos = Enclos()
            for elt in ls_Enclos:
                if self.comboBox_enclos.currentText() == elt.NumEnclos:
                    mon_enclos = elt
            serp.Enclos = mon_enclos
            serp.Couleur_ecailles = self.comboBox_couleur_serpent.currentText()
            serp.Venimeux = self.comboBox_venimeux.currentText()
            # Vérifier si le serpent existe ou pas dans la liste des animaux
            verifier_animal = verifier_animal_liste(serp.NumAnimal)
            # Si le numéro et le poid sont valides et l'animal existe dans la liste des animaux
            if serp.NumAnimal != "" and serp.PoidAnimal != "" and verifier_animal is True:
                trouve = False
                for elt in ls_Animaux:
                    # Chercher dans la liste des animaux un animal ayant les informations entrées
                    if elt.NumAnimal == self.lineEdit_numero_nmal.text() and elt.PoidAnimal == \
                            self.lineEdit_poid_nmal.text():
                        # Supprimer l'animal de la liste des animaux
                        trouve = True
                        ls_Animaux.remove(elt)
                        break
                # Si l'animal n'existe pas dans la liste, afficher un message d'erreur
                if not trouve:
                    self.label_erreur_nmal_inexistant.setVisible(True)
                else:
                    # Réafficher dans le textBrowser la nouvelle liste qui ne contient pas l'animal supprimé
                    self.textBrowser_afficher_animaux.clear()
                    for elt in ls_Animaux:
                        self.textBrowser_afficher_animaux.append(elt.__str__())
                    # Réinitialiser les lineEdits
                    self.lineEdit_numero_nmal.clear()
                    self.lineEdit_poid_nmal.clear()
                    # Si le numéro de l'animal n'existe pas dans la liste des animaux, afficher un message d'erreur
            if verifier_animal is False and serp.NumAnimal != "":
                # Effacer le lineEdit numero animal et afficher le message d'erreur
                self.lineEdit_numero_nmal.clear()
                self.label_erreur_nmal_inexistant.setVisible(True)
            # Si le numéro de l'animal est invalide, afficher un message d'erreur
            if serp.NumAnimal == "":
                self.lineEdit_numero_nmal.clear()
                self.label_numero_nmal.setVisible(True)
            # Si le poid du serpent est invalide, afficher un message d'erreur
            if serp.PoidAnimal == "":
                self.lineEdit_poid_nmal.clear()
                self.label_erreur_poid_nmal.setVisible(True)
        # Instancier un object Oiseau
        if choix_animal == "Oiseau":
            ois = Oiseau()
            # Entrée de donnée pour les attributs de l'object Oiseau
            ois.NumAnimal = self.lineEdit_numero_nmal.text().capitalize()
            ois.PoidAnimal = float(self.lineEdit_poid_nmal.text())
            ois.Espece_animal = self.comboBox_espece_oiseau.currentText()
            mon_enclos = Enclos()
            for elt in ls_Enclos:
                if self.comboBox_enclos.currentText() == elt.NumEnclos:
                    mon_enclos = elt
            ois.Enclos = mon_enclos
            ois.Couleur_plumes = self.comboBox_couleur_oiseau.currentText()
            ois.LongueurBec = int(self.lineEdit_longueur_bec.text())
            # Vérifier si l'oiseau existe ou pas dans la liste des animaux
            verifier_animal = verifier_animal_liste(ois.NumAnimal)
            # Si le numéro et le poid sont valides et l'animal existe dans la liste des animaux
            if ois.NumAnimal != "" and ois.PoidAnimal != "" and verifier_animal is True:
                trouve = False
                for elt in ls_Animaux:
                    # Chercher dans la liste des animaux un animal ayant les informations entrées
                    if elt.NumAnimal == self.lineEdit_numero_nmal.text() and elt.PoidAnimal == \
                            self.lineEdit_poid_nmal.text():
                        # Supprimer l'animal de la liste des animaux
                        trouve = True
                        ls_Animaux.remove(elt)
                        break
                # Si l'animal n'existe pas dans la liste, afficher un message d'erreur
                if not trouve:
                    self.label_erreur_nmal_inexistant.setVisible(True)
                else:
                    # Réafficher dans le textBrowser la nouvelle liste qui ne contient pas l'animal supprimé
                    self.textBrowser_afficher_animaux.clear()
                    for elt in ls_Animaux:
                        self.textBrowser_afficher_animaux.append(elt.__str__())
                    # Réinitialiser les lineEdits
                    self.lineEdit_numero_nmal.clear()
                    self.lineEdit_poid_nmal.clear()
                    # Si le numéro de l'animal n'existe pas dans la liste des animaux, afficher un message d'erreur
            if verifier_animal is False and ois.NumAnimal != "":
                # Effacer le lineEdit numero animal et afficher le message d'erreur
                self.lineEdit_numero_nmal.clear()
                self.label_erreur_nmal_inexistant.setVisible(True)
            # Si le numéro de l'animal est invalide, afficher un message d'erreur
            if ois.NumAnimal == "":
                self.lineEdit_numero_nmal.clear()
                self.label_numero_nmal.setVisible(True)
            # Si le poid de l'oiseau est invalide, afficher un message d'erreur
            if ois.PoidAnimal == "":
                self.lineEdit_poid_nmal.clear()
                self.label_erreur_poid_nmal.setVisible(True)
        # Instancier un object Poisson
        if choix_animal == "Poisson":
            poiss = Poisson()
            # Entrée de donnée pour les attributs de l'object Poisson
            poiss.NumAnimal = self.label_numero_nmal.text().capitalize()
            poiss.PoidAnimal = float(self.lineEdit_poid_nmal.text())
            poiss.Espece_animal = self.comboBox_espece_poisson.currentText()
            mon_enclos = Enclos()
            for elt in ls_Enclos:
                if self.comboBox_enclos.currentText() == elt.NumEnclos:
                    mon_enclos = elt
            poiss.Enclos = mon_enclos
            poiss.Couleur_ecailles = self.comboBox_couleur_poisson.currentText()
            poiss.LongueurPoisson = int(self.lineEdit_longueur_poisson.text())
            # Vérifier si le poisson existe ou pas dans la liste des animaux
            verifier_animal = verifier_animal_liste(poiss.NumAnimal)
            # Si le numéro et le poid sont valides et l'animal existe dans la liste des animaux
            if poiss.NumAnimal != "" and poiss.PoidAnimal != "" and verifier_animal is True:
                trouve = False
                for elt in ls_Animaux:
                    # Chercher dans la liste des animaux un animal ayant les informations entrées
                    if elt.NumAnimal == self.lineEdit_numero_nmal.text() and elt.PoidAnimal==self.lineEdit_poid_nmal.text():
                        # Supprimer l'animal de la liste des animaux
                        trouve = True
                        ls_Animaux.remove(elt)
                        break
                # Si l'animal n'existe pas dans la liste, afficher un message d'erreur
                if not trouve:
                    self.label_erreur_nmal_inexistant.setVisible(True)
                else:
                    # Réafficher dans le textBrowser la nouvelle liste qui ne contient pas l'animal supprimé
                    self.textBrowser_afficher_animaux.clear()
                    for elt in ls_Animaux:
                        self.textBrowser_afficher_animaux.append(elt.__str__())
                    # Réinitialiser les lineEdits
                    self.lineEdit_numero_nmal.clear()
                    self.lineEdit_poid_nmal.clear()
                    # Si le numéro de l'animal n'existe pas dans la liste des animaux, afficher un message d'erreur
            if verifier_animal is False and poiss.NumAnimal != "":
                # Effacer le lineEdit numero animal et afficher le message d'erreur
                self.lineEdit_numero_nmal.clear()
                self.label_erreur_nmal_inexistant.setVisible(True)
            # Si le numéro de l'animal est invalide, afficher un message d'erreur
            if poiss.NumAnimal == "":
                self.lineEdit_numero_nmal.clear()
                self.label_numero_nmal.setVisible(True)
            # Si le poid du poisson est invalide, afficher un message d'erreur
            if poiss.PoidAnimal == "":
                self.lineEdit_poid_nmal.clear()
                self.label_erreur_poid_nmal.setVisible(True)

    @pyqtSlot()
    def on_pushButton_choix_nmal_clicked(self):
        global choix_animal
        if self.comboBox_choix_nmal.currentText() == "Serpent":
            activer_widgets_serpent(self)
            desactiver_widgets_oiseau(self)
            desactiver_widgets_poisson(self)
            choix_animal = "Serpent"
        elif self.comboBox_choix_nmal.currentText() == "Oiseau":
            activer_widgets_oiseau(self)
            desactiver_widgets_serpent(self)
            desactiver_widgets_poisson(self)
            choix_animal = "Oiseau"
        else:
            activer_widgets_poisson(self)
            desactiver_widgets_serpent(self)
            desactiver_widgets_oiseau(self)
            choix_animal = "Poisson"