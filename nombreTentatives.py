global tentatives
tentatives = 0

def add_tentative():
    global tentatives
    tentatives += 1

def get_tentatives():
    print(f'Vous avez effectué {tentatives} tentative(s)')
    return tentatives