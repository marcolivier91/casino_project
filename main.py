import mainmenu
def casino():
    try:
        mainmenu.showmainmenu()
    except KeyboardInterrupt:
        print("\nInterrompu par l'utilisateur.")
casino()