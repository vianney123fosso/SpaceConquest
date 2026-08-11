import random


COUT_RECHERCHE = 50
CHANCE_ECHEC_RECHERCHE = 0.05
CHANCE_EXPLORATION = 0.90

TECHNOLOGIES = [
    "Steroides",
    "Metal rare",
    "Medecine",
    "Antivirus",
    "Domes",
    "Armes",
    "Bombe atomique",
    "Robotique",
    "Textile",
    "Exploration"
]

def afficher_menu():
    print("\n=== Actions disponibles ===")
    print("1. Construire une mine")
    print("2. Construire une usine")
    print("3. Construire un labo")
    print("4. Miser la recherche")
    print("5. Finir le mois")
    print("0. Quitter") 
    
def creer_etat_initial():
    return {
        "mois": 1,
        "population": 100,
        "argent": 1000,
        "outil": 500,
        "mine": 0,
        "usine": 0,
        "labo": 0,
        "recherche": 0,
        "defense": 0,
        "sante": 0,
        "cyber": 0,
        "exploration_debloquee": False,
        "technologies": []
    }
    
def afficher_ressources(etat):
    print("Mois :", etat["mois"])
    print("Population :", etat["population"], "humains")
    print("Argent :", etat["argent"])
    print("Outils :", etat["outil"])
    print("Mines :", etat["mine"])
    print("Usines :", etat["usine"])
    print("Labos :", etat["labo"])
    print("Recherche :", etat["recherche"])
    print("Defense :", etat["defense"])
    print("Sante :", etat["sante"])
    print("Cyberdefense :", etat["cyber"])
    if etat["technologies"]!=[]:
        print("Technologies :", ", ".join(etat["technologies"]))
    else:
        print("Technologies : aucune")
    
def demander_choix():
        while True:
            try:
                choix = int(input("Choisis une action : "))

                if choix >= 0 and choix <= 5:
                    return choix

                print("Choix inexistant.")

            except ValueError:
                print("Tu dois entrer un nombre.")

def appliquer_technologie(etat, technologie):
    if technologie in etat["technologies"]:
        print("Technologie deja connue :", technologie)
        return

    etat["technologies"].append(technologie)
    print("Nouvelle decouverte :", technologie)
    
    
    if technologie == "Exploration":
        etat["exploration_debloquee"] = True
        print("Exploration debloquee : la planete entiere devient accessible.")
    elif technologie == "Steroides":
        etat["population"] += 20
    elif technologie == "Metal rare":
        etat["argent"] += 300
    elif technologie == "Medecine":
        etat["sante"] += 25
    elif technologie == "Antivirus":
        etat["cyber"] += 25
    elif technologie == "Domes":
        etat["defense"] += 25
    elif technologie == "Armes":
        etat["defense"] += 30
    elif technologie == "Bombe atomique":
        etat["defense"] += 50
    elif technologie == "Robotique":
        etat["outil"] += 100
    elif technologie == "Textile":
        print("Les humains sont mieux habilles, mais cela n'aide pas la survie.")
def miser_recherche(etat):
    if etat["recherche"] < COUT_RECHERCHE:
        print("Recherche insuffisante pour miser.")
        return

    etat["recherche"] -= COUT_RECHERCHE

    if random.random() < CHANCE_ECHEC_RECHERCHE:
        print("La recherche echoue. Aucune technologie decouverte.")
        return
    
    if not etat["exploration_debloquee"] and random.random() < CHANCE_EXPLORATION:
        appliquer_technologie(etat, "Exploration")
        return

    technologies_disponibles = [
        technologie
        for technologie in TECHNOLOGIES
        if technologie not in etat["technologies"]
    ]

    if not technologies_disponibles:
        print("Aucune nouvelle technologie disponible.")
        return

    technologie = random.choice(technologies_disponibles)
    appliquer_technologie(etat, technologie)


                
def construire_mine(etat):
    cout_argent = 300
    cout_outil = 100

    if etat["argent"] >= cout_argent and etat["outil"] >= cout_outil:
        etat["argent"] -= cout_argent
        etat["outil"] -= cout_outil
        etat["mine"] += 1
        print("Mine construite avec succes.")
    else:
        print("Ressources insuffisantes pour construire une mine.")


def construire_usine(etat):
    cout_argent = 400
    cout_outil = 100

    if etat["argent"] >= cout_argent and etat["outil"] >= cout_outil:
        etat["argent"] -= cout_argent
        etat["outil"] -= cout_outil
        etat["usine"] += 1
        print("Usine construite avec succes.")
    else:
        print("Ressources insuffisantes pour construire une Usine.")

def construire_labo(etat):
    cout_argent = 300
    cout_outil = 100

    if etat["argent"] >= cout_argent and etat["outil"] >= cout_outil:
        etat["argent"] -= cout_argent
        etat["outil"] -= cout_outil
        etat["labo"] += 1
        print("Labo construit avec succes.")
    else:
        print("Ressources insuffisantes pour construire un labo.")



def passer_mois(etat):
    production_argent = etat["mine"] * 100
    production_outil = etat["usine"] * 50
    production_recherche = etat["labo"] * 10

    etat["argent"] += production_argent
    etat["outil"] += production_outil
    etat["recherche"] += production_recherche
    etat["mois"] += 1

    print("Un mois passe.")
    print("Production argent :", production_argent)
    print("Production outils :", production_outil)
    print("Production recherche :", production_recherche)
    
    
def main():
    print("Bienvenue dans SpaceConquest 🚀")
 
    etat = creer_etat_initial()
    
    jeu=True
    while jeu:
        afficher_ressources(etat)
        afficher_menu()
        choix=demander_choix()
        if choix == 1:
            construire_mine(etat)
        elif choix == 2:
            construire_usine(etat)
        elif choix == 3:
            construire_labo(etat)
        elif choix == 4:
            miser_recherche(etat)
        elif choix == 5:
            passer_mois(etat)

        else:
            print ("Fin du jeu")
            jeu=False
   
    
        


if __name__ == "__main__":
    main()
    
