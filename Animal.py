####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Dimitri Lacroix-Moreau
###  No étudiant: 2041532
###  No Groupe: 01
###  Description du fichier: Description de la classe parent Animal
####################################################################################
from Enclos import *

class Animal:
    """
    Classe parent Animal
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################
    def __init__(self, p_num_animal="", p_poid_animal=0.00, p_espece_animal="", p_enclos=Enclos()):
        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un animal
        """
        self.__num_animal = p_num_animal
        self.__poid_animal = p_poid_animal
        self.Espece_animal = p_espece_animal
        self.Enclos = p_enclos

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    # Propriété NumAnimal
    def _get_num_animal(self):
        """
        Accesseur de l'attribut privée __num_animal
        """
        return self.__num_animal

    def _set_num_animal(self, p_num_animal):
        """
        Mutateur de l'attribut privée __num_animal
        """
        if len(p_num_animal) == 5 and p_num_animal[0].isalpha() and p_num_animal[1:4].isnumeric():
            self.__num_animal = p_num_animal

    NumAnimal = property(_get_num_animal, _set_num_animal)

    # Propriété PoidAnimal
    def _get_poid_animal(self):
        """
        Accesseur de l'attribut privée __poid_animal
        """
        return self.__poid_animal

    def _set_poid_animal(self, p_poid_animal):
        """
        Mutateur de l'attribut privée __poid_animal
        """
        if p_poid_animal > 0.00:
            self.__poid_animal = p_poid_animal

    PoidAnimal = property(_get_poid_animal, _set_poid_animal)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        """
        Méthode spéciale d'affichage. À utiliser avec print(objet)
        :return: Chaine à afficher
        """
        chaine = " " * 60 + "\n" + "\n\n"
        chaine += "\nNuméro de l'animal : " + self.__num_animal
        chaine += "\nPoid de l'animal : " + str(self.__poid_animal)
        chaine += "\nEspèce de l'animal : " + self.Espece_animal
        chaine += "\n" + self.Enclos.__str__() + "\n\n" + "*" * 60

        return chaine