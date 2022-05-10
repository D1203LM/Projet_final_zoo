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
# Importer Pour le model de la boite de dialogue animal
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# importer les interfaces graphiques
import interface_graphique_zoo
from formulaire_dialogue_animal import *

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

def cacher_labels_erreur(object):
    """
    Cacher les différents labels d'erreur
    """
    object.label_erreur_nmal_existe.setVisible(False)
    object.label_erreur_nmal_inexistant.setVisible(False)
    object.label_erreur_numero_nmal.setVisible(False)
    object.label_erreur_poid_serpent.setVisible(False)
    object.label_erreur_poid_oiseau.setVisible(False)
    object.label_erreur_poid_poisson.setVisible(False)
