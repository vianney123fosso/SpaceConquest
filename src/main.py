def afficher_ressources(mois, population, argent, outil, mine, usine, labo, recherche):
    print("\n=== Etat de la planete ===")
    print("Mois :", mois)
    print("Population :", population,"humains")
    print("Argent :", argent)
    print("Outils :", outil)
    print("Usines :", usine)
    print("Mines :", mine)
    print("Labos :", labo)
    print("Recherche :", recherche)


def afficher_menu():
    print("\n=== Actions disponibles ===")
    print("1. Construire une mine")
    print("2. Construire une usine")
    print("3. Construire un labo")
    print("4. Finir le mois")
    print("0. Quitter") 
    
    
def demander_choix():
        while True:
            try:
                choix = int(input("Choisis une action : "))

                if choix >= 0 and choix <= 4:
                    return choix

                print("Choix inexistant.")

            except ValueError:
                print("Tu dois entrer un nombre.")
                
                
def construire_mine(argent, outil, mine):
    cout_argent = 300
    cout_outil = 100

    if argent >= cout_argent and outil >= cout_outil:
        argent -=  cout_argent
        outil -=  cout_outil
        mine +=  1
        print("Mine construite avec succes.")
    else:
        print("Ressources insuffisantes pour construire une mine.")

    return argent, outil, mine


def construire_usine(argent, outil, usine):
    cout_argent = 400
    cout_outil = 150

    if argent >= cout_argent and outil >= cout_outil:
        argent -=  cout_argent
        outil -=  cout_outil
        usine +=  1
        print("Usine construite avec succes.")
    else:
        print("Ressources insuffisantes pour construire une usine.")

    return argent, outil, usine


def construire_labo(argent, outil, labo):
    cout_argent = 200
    cout_outil = 50

    if argent >= cout_argent and outil >= cout_outil:
        argent -=  cout_argent
        outil -=  cout_outil
        labo +=  1
        print("labo construit avec succes.")
    else:
        print("Ressources insuffisantes pour construire un labo.")

    return argent, outil, labo


def main():
    print("Bienvenue dans SpaceConquest 🚀")
    argent = 1000
    population=100
    outil = 500
    usine=0
    mine=0
    labo=0
    recherche = 0
    mois = 1
    
    
    afficher_ressources(argent, recherche, mois, population, usine, labo, outil, mine)
    afficher_menu()
    choix=demander_choix()
    if choix == 1:
        argent, outil, mine = construire_mine(argent, outil, mine)
        afficher_ressources(mois, population, argent, outil, mine, usine, labo, recherche)
    elif choix == 2:
        argent, outil, usine = construire_usine(argent, outil, usine)
        afficher_ressources(mois, population, argent, outil, mine, usine, labo, recherche)
    elif choix == 3:
        argent, outil, labo = construire_labo(argent, outil, labo)
        afficher_ressources(mois, population, argent, outil, mine, usine, labo, recherche)
    elif choix == 4:
        mois+=1
        afficher_ressources(mois, population, argent, outil, mine, usine, labo, recherche)
    elif choix== 0:
        print ("Fin du jeu")
    else:
        pass
    
         
   
    
        



if __name__ == "__main__":
    main()
    
