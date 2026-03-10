import random

def maingame():
    global chances
    chances = 3
    global maxlimit
    maxlimit = 10
    global number
    number = random.randint(1, maxlimit)
    while True:
        try:
            print(f'Vous avez {chances} chances pour trouver le nombre')
            guess = int(input('Votre proposition : '))
        except ValueError:
            print("Ce n'est pas un nombre valide, essayez à nouveau !")
            continue
        match guess:
            case 'exit':
                print('Merci d\'avoir joué, à bientôt !')
                break
            case guess if guess < 0:
                print('La proposition est trop petite !')
                continue
            case guess if guess> maxlimit:
                print('La proposition est trop grande !')
                continue
            case guess if (guess != number and guess < maxlimit):
                chances -= 1
                print('Mauvaise réponse !')
            case guess if guess == number:
                print('Bravo, vous avez trouvé le nombre !')
                break
        if chances <= 0:
                print('Dommage, vous avez épuisé toutes vos chances !')
                break