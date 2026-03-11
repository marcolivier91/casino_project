global tentatives
tentatives = 0

def add_tentative():
    global tentatives
    tentatives = tentatives + 1
    
def delete_tentative():
    global tentatives
    tentatives = tentatives - 1

def get_tentatives():
    return tentatives