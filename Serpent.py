########################################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Dimitri Lacroix-Moreau
###  No étudiant: 2041532
###  No Groupe: 01
###  Description du fichier: Description de la classe Serpent, dérivée de la classe parent Animal
########################################################################################################
import json
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
        Définition des attributs d'un serpent
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

    ############################################
    #####          Autres MÉTHODES         #####
    ############################################

    # inspiré de la méthode sérialiser étudiant
    def serialiser(self, p_fichier):
        """
           Méthode permttant de sérialiser un objet de la classe Animal
           ::param p_fichier : Le nom du fichier qui contiendra l'objet sérialisé
           :: return : retourne 0 si le fichier est ouvert et les informations y sont écrites,
                       1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture

        """
        self.__dict__["Animaux"]=str(self.Serpent())+"\n"+str(self.Oiseau())+"\n"+str(self.Poisson())

        try:
            with open(p_fichier , "w") as fichier:
                try:
                    #json.dump(self.__dict__, fichier)
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2