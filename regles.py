import time
import os

def effacer_ecran():
    effacer = input('Voulez-vous continuer ? (oui/non) : ')
    if effacer.lower() == 'oui':
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('Dommage, peut-être une prochaine fois !')
        
def afficher_regles():
    with open('./regles.txt', 'r', encoding='utf-8') as file:
        regles = file.readlines()
        for ligne in regles:
            print(ligne.strip())
            time.sleep(1)
        time.sleep(5)
        effacer_ecran()