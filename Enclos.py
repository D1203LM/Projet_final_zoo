####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Dimitri Lacroix-Moreau
###  No étudiant: 2041532
###  No Groupe: 01
###  Description du fichier: Description de la classe Enclos
####################################################################################

import json

class Enclos:
    """
    Classe Enclos
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################
    def __init__(self, p_num_enclos="", p_taille_enclos="", p_lieu_enclos=""):
        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un enclos
        """
        self.__num_enclos = p_num_enclos
        self.Taille_enclos = p_taille_enclos
        self.Lieu_enclos = p_lieu_enclos

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    # Propriété NumEnclos
    def _get_num_enclos(self):
        """
        Accesseur de l'attribut privée __num_enclos
        """
        return self.__num_enclos

    def _set_num_enclos(self, p_num_enclos):
        """
        Mutateur de l'attribut privée __num_enclos
        """
        if len(p_num_enclos) == 2 and p_num_enclos[0].isalpha() and p_num_enclos[1].isnumeric():
            self.__num_enclos = p_num_enclos

    NumEnclos = property(_get_num_enclos, _set_num_enclos)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        """
        Méthode spéciale d'affichage. À utiliser avec print(objet)
        :return: Chaine à afficher
        """
        chaine = "\nNuméro de l'enclos : " + self.__num_enclos
        chaine += "\nTaille de l'enclos : " + self.Taille_enclos
        chaine += "\nLieu de l'enclos : " + self.Lieu_enclos

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
        self.__dict__["Enclos"]=str(Enclos())

        try:
            with open(p_fichier, "w") as fichier:
                try:
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2