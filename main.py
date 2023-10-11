# TP2
# Crée par Victor-Ionut Armasu

#importation de la fonction random

# Fonction jeu qui contient le code
def jeu():
    repete = True
    # boucle while qui repète le jeu
    while repete:
        # fonction qui import random
        import random

        #On définit les variables
        nombre_essaie = 0
        question = True

        #On choisis un nombre aléatoire

        nbr1 = int(input("Entrez un premier nombre:"))
        nbr2 = int(input("Entrez un deuxième nombre:"))

        nombre_aleatoire = random.randint(nbr1, nbr2)

        #Dit le contexte
        print("J’ai choisi un nombre au hasard entre %d et %d. \n À vous de le deviner..." % (nbr1, nbr2))

        #On utilise la fonction while pour poser la question

        while question:
            essaie = int(input("Entrez votre essai :_"))

            #Si c'est bon ça fini la question

            if essaie == nombre_aleatoire:
                nombre_essaie += 1
                print("Bravo, vous avez deviné en %d essais" % nombre_essaie)
                question = False
                # Question qui demande si l'utilisateur veut refaire le programme
                refaire = str(input('Voulez vous recommencer?'))
                if refaire == 'oui':
                    repete = True
                else:
                    print('Bye')
                    repete = False
            #sinon ça dit que c'est plus grand que l'Essaie

            elif essaie < nombre_aleatoire:
                print("Mauvais choix, le nombre est plus grand que %d" %essaie)
                nombre_essaie += 1

            #sinon ça dit que c'est plus petit que l'essaie

            elif essaie > nombre_aleatoire:
                print("Mauvaise réponse, le nombre est plus petit que %d" %essaie)
                nombre_essaie += 1
# Ligne qui active la fonction jeu
jeu()