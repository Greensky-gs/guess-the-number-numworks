from random import randint
from math import isnan

launched = False

def returnRandom(tuple: tuple):
    return tuple[randint(0, len(tuple) - 1)]

def lowerMessage():
    reps = ("Mon nombre est plus petit", "Essayez un nombre plus petit", "Mon nombre est plus petit que ça", "Votre réponse est trop grande pour mon nombre")
    return returnRandom(reps)

def higherMessage():
    reps = ("Mon nombre est plus grand", "Essayez un nombre plus grand", "Mon nombre est plus grand que ça", "Votre réponse est trop basse pour mon nombre")
    return returnRandom(reps)

def winMessage():
    reps = ("Vous avez trouvé mon nombre !", "Bien vu !", "Bien joué ! Vous avez gagné", "Vous m'avez battu")
    return returnRandom(reps)

def looseMessage(number):
    reps = ("Perdu, mon nombre était " + number, "Mon nombre était " + number + ", désolé", "Je suppose que vous avez perdu, mon nombre était " + number)
    return returnRandom(reps)

def tryMessage():
    reps = ("Votre tentative :", "Nouvelle tentative :", "Votre réponse :", "Essayez encore :")
    return returnRandom(reps)

def main():
    number = randint(0, 100)

    print("J'ai choisit mon nombre aléatoire entre 0 et 100")
    ended = False
    remaining = 10
    
    while ended == False:
        guess = input(tryMessage() + ' ')
        if guess is None or guess == '' or not guess:
            print("Valeur invalide. Utilisez un nombre")
        else:
            guess = float(guess)
            if isnan(guess) or guess > 100 or guess < 0:
                print("Valeur invalide. Utilisez un nombre entre 0 et 100")
            else:
                remaining -= 1

                if guess == number:
                    ended = True
                    print(winMessage())
                elif guess > number:
                    print(lowerMessage())
                else:
                    print(higherMessage())
        
                if remaining == 0:
                    ended = True
                    print(looseMessage(number))

def choose():
    choice = input("Voulez vous quitter (q) ou lancer une partie (l): ")
    if choice.lower() == 'q':
        return exit()
    
    launched = True
    main()
    launched = False

while True:
    if launched == False:
        choose()