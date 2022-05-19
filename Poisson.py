########################################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Dimitri Lacroix-Moreau
###  No étudiant: 2041532
###  No Groupe: 01
###  Description du fichier: Description de la classe Poisson, dérivée de la classe parent Animal
########################################################################################################

from Animal import *

class Poisson (Animal):
    """
    Classe Poisson, dérivée de la classe parent Animal
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################
    def __init__(self, p_num_animal="", p_poid_animal=0.00, p_espece_animal="", p_couleur_ecailles="",
                 p_longueur_poisson=0):
        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un poisson
        """
        Animal.__init__(self, p_num_animal, p_poid_animal, p_espece_animal)
        self.Couleur_ecailles = p_couleur_ecailles
        self.__longueur_poisson = p_longueur_poisson

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    # Propriété LongueurPoisson
    def _get_longueur_poisson(self):
        """
        Accesseur de l'attribut privée __longueur_poisson
        """
        return self.__longueur_poisson

    def _set_longueur_poisson(self, p_longueur_poisson):
        """
        Mutateur de l'attribut privée __longueur_poisson
        """
        if p_longueur_poisson > 0:
            self.__longueur_poisson = p_longueur_poisson

    LongueurPoisson = property(_get_longueur_poisson, _set_longueur_poisson)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################
    def __str__(self):
        """
        Méthode spéciale d'affichage. À utiliser avec print(objet)
        :return: Chaine à afficher
        """
        chaine = "\nNuméro du poisson : " + str(self.NumAnimal)
        chaine += "\nPoid du poisson : " + str(self.PoidAnimal)
        chaine += "\nEspèce du poisson : " + str(self.Espece_animal)
        chaine += "\nCouleur des écailles du poisson : " + str(self.Couleur_ecailles)
        chaine += "\nLongueur du poisson : " + str(self.LongueurPoisson)
        chaine += "\n" + self.Enclos.__str__()

        return chaine