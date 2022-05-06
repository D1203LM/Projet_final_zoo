####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Dimitri Lacroix-Moreau
###  No étudiant: 2041532
###  No Groupe: 01
###  Description du fichier: Test des classes
####################################################################################

from Serpent import *
from Oiseau import *
from Poisson import *

################################
#####  TEST CLASSE Animal  #####
################################

a1 = Animal()
try:
    a1.NumAnimal = "a1234"
    a1.PoidAnimal = 1.23
except:
    print("Erreur")
else:
    print(a1)

#################################
#####  TEST CLASSE Serpent  #####
#################################

s1 = Serpent()
try:
    s1.NumAnimal = "S1234"
    s1.PoidAnimal = 5.10
except:
    print("Erreur")
else:
    print(s1)

################################
#####  TEST CLASSE Oiseau  #####
################################

o1 = Oiseau()
try:
    o1.NumAnimal = "o1234"
    o1.PoidAnimal = 0.05
    o1.LongueurBec = 15
except:
    print("Erreur")
else:
    print(o1)

#################################
#####  TEST CLASSE Poisson  #####
#################################

p1 = Poisson()
try:
    p1.NumAnimal = "P1234"
    p1.PoidAnimal = 1.50
    p1.LongueurPoisson = 12
except:
    print("Erreur")
else:
    print(p1)