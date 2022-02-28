
class Humain :
    """
     Classe des etres humains
    """
    humains_crees = 0
    def __init__(self,c_prenom, c_age) -> None:
        print("Creation d'humain....")

        self.prenom = c_prenom
        self.age = c_age
        Humain.humains_crees +=1
        # self.prenom = "Medoune"
        # self.age = 23

print("Lancement du programme....")

h1 = Humain("Medoune", 23)
print("Humains existants {}".format(Humain.humains_crees))


h2 = Humain("Mina", 32)
print("Humains existants {}".format(Humain.humains_crees))


# print("Prenom de h1 : {}".format(h1.prenom))
# print("Age de h1 : {}".format(h1.age))

# h1.prenom = "Ousmane"
# print("Prenom de h1 : {}".format(h1.prenom))

# h2 = Humain("Ndeye", 20)
# print("Prenom de h2 : {}".format(h2.prenom))
# print("Age de h2 : {}".format(h2.age))