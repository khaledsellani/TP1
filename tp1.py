# Probleme liste de courses
# TP universitaire python

mystr = """Choisissez parmi les 5 options suivantes :
1: Ajouter un element a la liste
2: Retirer un element de la liste 
3: Afficher la liste
4: Vider la liste
5: Quitter
"""

print(mystr)
user_choice = int(input(" Votre choix : "))

liste = []

while user_choice in [1,2,3,4,5]:
    match user_choice:
        case 1:
            name = int(input("Entrez le nom de l'element a rajouter : "))
            liste.append(name)
            print(f"L'element {name} a ete bien rajouter")
            print("_"*30)
            print("\n")
        case 2:
            name = int(input("Entrez le nom de l'element a retirer : "))
            if name in liste:
                liste.remove(name)
                print(f"L'element {name} a ete bien supprime")
                print("______________________________________\n")

            else:
                print(f"l'element {name} n'existe pas dans a liste")
                print("______________________________________\n")
        case 3:
            print(liste)
            print("______________________________________\n")
        case 4:
            if len(liste) == 0:
                print("la liste est deja vide")
            else:
                liste.clear()
            print("______________________________________\n")
        case 5:
            break
    print(mystr)
    user_choice = int(input(" Votre choix : "))