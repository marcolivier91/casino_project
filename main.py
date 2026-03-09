from termcolor import colored

def casino():
    number = 5
    chances = 3
    maxlimit = 10
    
    print(colored('Bienvenue au Casino du Paradis !', 'cyan', attrs=['bold']))
    print(f'Je possède un nombre entre 1 et {maxlimit}, essayez de le deviner !')
    print(f'Vous avez {chances} chances pour trouver le nombre.')
    while True:            
        try:
            guess = int(input('Votre proposition : '))
        except ValueError:
            print("Invalid input!")
            continue

        if guess < maxlimit:
            print('La proposition est trop petite !')
        if guess > maxlimit:
            print('La proposition est trop grande !')
        if (guess != number and guess < maxlimit):
            chances -= 1
            print('Mauvaise réponse, essayez à nouveau !')
            print(f'Il vous reste {chances} chances.')
        else:
            print('Bravo, vous avez trouvé le nombre !')
            break
        if chances <= 0:
            print('Dommage, vous avez épuisé toutes vos chances !')
            break

        
casino()