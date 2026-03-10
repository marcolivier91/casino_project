import time

mise = 10

def insert_mise():
    global mise
    try:
        mise = int(input('Insérez votre mise : '))
        if mise <= 0:
            print('Le nombre de crédits ne peut pas être négatif, essayez à nouveau !')
            insert_mise()
        print(f'Vous avez {mise} euros.')
        time.sleep(2)
        return mise
    except ValueError:
        print("Ce n'est pas un nombre valide, essayez à nouveau !")
        insert_mise()
        
def get_mise():
    print(f'Vous avez {mise} euros.')
    time.sleep(2)
    return mise