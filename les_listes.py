# les liste en python

# liste_des_etudiants.append("Fall")
# del liste_des_etudiants[0]
# print(liste_des_etudiants[0])

# liste_des_etudiants = ["Medoune","Ousseynou", "Xarala","Samba","Awa","Khady"]
# liste_des_etudiants.remove("Samba")
# print(liste_des_etudiants)

from itertools import count


# numero = [23, 6, 4, 3, 3, 9, "a", "a", "b", "c","d"]
# # numero_del = len(numero)
# # compter = numero.count("a")
# # position_a = numero.index("a")
# dernier = numero[-4:]
# print(dernier)



list_des_candidats = ["Macky", "Sonko", "Madikce", "Issa", "Macky"]
if list_des_candidats.count("Macky") > 1 :
  print("Vous avez inscrit deux fois")
  for candidat in list_des_candidats :
        print("Candidat ", candidat)