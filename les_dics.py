# dictionnaire ->notion de valeurs et de cles
# Creer un dictionnaire
mon_dic = {}
# Ajouter des valeurs
mon_dic["nom"] = "Fall"
mon_dic["prenom"] = "Medoune"
mon_dic["profession"] = "Developpeur"
# Recuperer une valeur
nom = mon_dic.get("nom")
# Supprimer une entre
# del mon_dic["nom"]
# print(mon_dic)
# Recuperer les valeurs
for valeurs in mon_dic.values() :
    pass
for cles in mon_dic.keys() :
    pass
# Recuperer les cles et valeurs
for cles, valeurs in mon_dic.items() :
    print(cles, ":", valeurs)