from termcolor import colored
import os
import time

def gameover_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored('GAME OVER', 'red', attrs=["reverse", "blink", "bold"]))
    time.sleep(2)
    print(colored('Merci d\'avoir joué ! A très bientôt.', 'yellow', attrs=['bold']))
    exit()