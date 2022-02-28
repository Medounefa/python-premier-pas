nom = input("Votre nom....")
age = int(input("Votre age..."))

def recuperer_nom(mon_nom,mon_age):
    return mon_nom, mon_age
print("Bonjour ", recuperer_nom(nom, age), "ans")