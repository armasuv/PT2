# TP2
# Crée par Victor-Ionut Armasu

#importation de la fonction random
import random
#On définit les variables
nombre_essaie = 0
question = True

#On choisis un nombre aléatoire
nombre_aleatoire = random.randint(1, 100)

#Dit le contexte
print("J’ai choisi un nombre au hasard entre 0 et 1000. \n À vous de le deviner...")

#On utilise la fonction while pour poser la question
while question:
    essaie = int(input("Entrez votre essai :_"))
    #Si c'est bon ça fini la question
    if essaie == nombre_aleatoire:
        print("Bravo, vous avez deviné en %d essais" % nombre_essaie)
        question = False
    #sinon ça dit que c'est plus grand que l'Essaie
    elif essaie < nombre_aleatoire:
        print("Mauvais choix, le nombre est plus grand que %d" %essaie)
        nombre_essaie += 1
    #sinon ça dit que c'est plus petit que l'essaie
    elif essaie > nombre_aleatoire:
        print("Mauvaise réponse, le nombre est plus petit que %d" %essaie)
        nombre_essaie += 1

