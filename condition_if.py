print("Entrez votre age")
age = input()
age = int(age)
print('Votre nom...')
nom = input()

if(age == 18 or age == 20) : 
    print('Bienvenue vous avez ', age, "ans")
elif(age == 24 and nom == 'xarala') : 
    print('Bienvenue ',nom,' vous avez ',age, "ans")
else :
    print("Acces nos autorise , vous avez ",age ,"ans")