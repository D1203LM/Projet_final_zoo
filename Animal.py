####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Dimitri Lacroix-Moreau
###  No étudiant: 2041532
###  No Groupe: 01
###  Description du fichier: Description de la classe parent Animal
####################################################################################

class Animal:
    """
    Classe parent Animal

    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################
    def __init__(self, p_num_animal="", p_poid=0.00, p_espece=""):
        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un animal
        """
        self.__num_animal = p_num_animal
        self.__poid = p_poid
        self.Espece = p_espece

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

    # Propriété Poid
    def _get_poid(self):
        """
        Accesseur de l'attribut privée __poid
        """
        return self.__poid

    def _set_poid(self, p_poid):
        """
        Mutateur de l'attribut privée __poid
        """
        if p_poid > 0.00:
            self.__poid = p_poid

    Poid = property(_get_poid, _set_poid)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        """
        Méthode spéciale d'affichage. À utiliser avec print(objet)
        :return: Chaine à afficher
        """
        chaine = "\nNuméro de l'animal : " + self.__num_animal
        chaine += "\nPoid de l'animal : " + self.__poid
        chaine += "\nEspèce de l'animal : " + self.Espece

        return chaine