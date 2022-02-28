# retoune moi une liste

def addition(*param) :
    return param[0] + param[1] + param[2]
resultat = addition(2,3,4)
# print(resultat)
# Retour moi in dictionnaire

def afficheNom(**params) :
    return params["nom"]
resultat = afficheNom(nom="Fall")
print(resultat)
