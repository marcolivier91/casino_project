from termcolor import colored
import regles
import checkMise
import maingame

chances = 3
maxlimit = 10

def showmainmenu():
    print(colored('Bienvenue au Casino du Paradis !', 'cyan', attrs=['bold']))
    print(f'Je possède un nombre entre 1 et {maxlimit}, essayez de le deviner !')
    print(colored('Pour quitter le jeu, tapez "exit".', 'red', attrs=['bold']))
    if input(colored('Êtes-vous prêt à jouer ? (oui/non) : ', 'yellow')).lower() != 'oui':
        print('Dommage, peut-être une prochaine fois !')
    else:
        regles.afficher_regles()            
        checkMise.show_mise()
        maingame.maingame()
        
    # options = ['Jouer', 'Lire les règles', 'Afficher mes statistiques', 'Quitter']
    # user_input = ''
    # input_message = "Choisissez une option:\n"
    # for index, item in enumerate(options):
    #     input_message += f'{index+1}) {item}\n'
    # input_message += 'Votre choix: '
    # while user_input not in map(str, range(1, len(options) + 1)):
    #     user_input = input(input_message)
