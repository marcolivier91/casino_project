import random
import time
import gameover
import nombreTentatives
import checkMise
import levelManagement

def maingame():
    global chances
    chances = 3
    global maxlimit
    maxlimit = 10
    global number
    number = random.randint(1, maxlimit)
    while True:
        try:
            print(number)
            print(f'Niveau 1, vous avez {chances} chances pour trouver le nombre')
            guess = int(input('Votre proposition : '))
            nombreTentatives.add_tentative()
        except ValueError:
            print("Ce n'est pas un nombre valide, essayez à nouveau !")
            continue
        match guess:
            case guess if guess < 0:
                print('La proposition est trop petite !')
                nombreTentatives.delete_tentative()
                continue
            case guess if guess> maxlimit:
                print('La proposition est trop grande !')
                nombreTentatives.delete_tentative()
                continue
            case guess if (guess != number and guess < maxlimit):
                chances -= 1
                print('Mauvaise réponse !')
            case guess if guess == number:
                print(f'Bravo, vous avez trouvé le nombre en {nombreTentatives.get_tentatives()} tentatives !')
                checkMise.update_mise(tentatives=nombreTentatives.get_tentatives())
                levelManagement.update_level()
        if chances <= 0:
                print('Dommage, vous avez épuisé toutes vos chances !')
                time.sleep(2)
                gameover.gameover_screen()