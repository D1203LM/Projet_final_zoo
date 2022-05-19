########################################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Dimitri Lacroix-Moreau
###  No étudiant: 2041532
###  No Groupe: 01
###  Description du fichier: Description de la classe Oiseau, dérivée de la classe parent Animal
########################################################################################################

from Animal import *

class Oiseau (Animal):
    """
    Classe Oiseau, dérivée de la classe parent Animal
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################
    def __init__(self, p_num_animal="", p_poid_animal=0.00, p_espece_animal="", p_couleur_plumes="", p_longueur_bec=0):
        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un oiseau
        """
        Animal.__init__(self, p_num_animal, p_poid_animal, p_espece_animal)
        self.Couleur_plumes = p_couleur_plumes
        self.__longueur_bec = p_longueur_bec

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    # Propriété LongueurBec
    def _get_longueur_bec(self):
        """
        Accesseur de l'attribut privée __longueur_bec
        """
        return self.__longueur_bec

    def _set_longueur_bec(self, p_longueur_bec):
        """
        Mutateur de l'attribut privée __longueur_bec
        """
        if p_longueur_bec > 0:
            self.__longueur_bec = p_longueur_bec

    LongueurBec = property(_get_longueur_bec, _set_longueur_bec)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################
    def __str__(self):
        """
        Méthode spéciale d'affichage. À utiliser avec print(objet)
        :return: Chaine à afficher
        """
        chaine = "\nNuméro de l'oiseau : " + str(self.NumAnimal)
        chaine += "\nPoid de l'oiseau : " + str(self.PoidAnimal)
        chaine += "\nEspèce de l'oiseau : " + str(self.Espece_animal)
        chaine += "\nCouleur des plumes de l'oiseau : " + str(self.Couleur_plumes)
        chaine += "\nLongueur du bec : " + str(self.LongueurBec)
        chaine += "\n" + self.Enclos.__str__()

        return chaine