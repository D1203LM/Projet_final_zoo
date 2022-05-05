########################################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Dimitri Lacroix-Moreau
###  No étudiant: 2041532
###  No Groupe: 01
###  Description du fichier: Description de la classe Serpent, dérivée de la classe parent Animal
########################################################################################################

from Animal import *

class Serpent (Animal):
    """
    Classe Serpent, dérivée de la classe parent Animal
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################
    def __init__(self, p_num_animal="", p_poid_animal=0.00, p_espece_animal="", p_couleur_ecailles="", p_venimeux=False):
        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un Serpent
        """
        Animal.__init__(self, p_num_animal, p_poid_animal, p_espece_animal)
        self.Couleur_ecailles = p_couleur_ecailles
        self.Venmieux = p_venimeux

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################
    def __str__(self):
        """
        Méthode spéciale d'affichage. À utiliser avec print(objet)
        :return: Chaine à afficher
        """
        chaine = "\nNuméro du serpent : " + str(self.NumAnimal)
        chaine += "\nPoid du serpent : " + str(self.PoidAnimal)
        chaine += "\nEspèce du serpent : " + str(self.Espece_animal)
        chaine += "\nCouleur des écailles du serpent : " + str(self.Couleur_ecailles)
        chaine += "\nVenimeux : " + str(self.Venmieux)

        return chaine