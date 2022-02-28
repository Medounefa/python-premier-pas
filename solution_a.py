print('--Inscription--')
print('Entrez votre nom utilisateur...')
nom = input()
print('Entrez un mot de passe')
mot_de_passe = input()
print('Confirmez le mot de passe')
mot_de_passe_2 = input()

if mot_de_passe == mot_de_passe_2 :
    print('--Connexion--')
    print('Nom utilisateur...')
    name = input()
    print('Mot de passe...')
    password = input()
else :
    print("Mot de passe incorrect")
if name == nom and password == mot_de_passe :
    print("Bienvenue ", name)
if( name  != nom and password !=mot_de_passe) :
        print('Information incorrect')
