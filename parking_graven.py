import re
import random
import string
import time

EMPLACEMENTS = 27
ETAGES = 3
VOITURE_GARE = "V"
EMPLACEMENT_LIBRE = "D"

PARKING_1 = [[EMPLACEMENT_LIBRE for etage_1 in range(EMPLACEMENTS)],  # étage 1 du parking 1
             [EMPLACEMENT_LIBRE for etage_2 in range(EMPLACEMENTS)],  # étage 2 du parking 1
             [EMPLACEMENT_LIBRE for etage_3 in range(EMPLACEMENTS)],  # étage 3 du parking 1
             ]
# placer une voitre sur l'emplacement 1
PARKING_1[0][0] = VOITURE_GARE

"""
lorsque qu'une place est reserver, generer un Passcode avec comme clé le numero de l'emplacement et l'étage
Ajouter la clé et le passcode a une liste de dictionnaire
lorsque lutilisateur souhaite reprendre sa voiture : demander l'emplacement de sa voiture
trouver le passcode avec la clé correspondant a l'emplacement
demander le passcode a l'user
si c'est bon, rendre la voiture, sinon redemander

"""
memoire_passcodes = {}

def generate_passcode():
    numbers = random.sample(string.digits, 4)
    four_letters = random.sample(string.ascii_uppercase, 4)
    two_letters = random.sample(string.ascii_uppercase, 2)
    passcode = "".join(four_letters) + "-" + "".join(numbers) + "-" + "".join(two_letters)
    return passcode


def affiche_emplacement(emplacements, etage):
    for numb, emplacement in enumerate(emplacements):
        if emplacement == "D":
            print(f"Etage n°{etage}: emplacement n°{numb + 1}: Disponible")
        else:
            print(f"Etage n°{etage}: emplacement n°{numb + 1}: Indisponible")


def gestion_des_places(emplacements, etage):
    choix_du_client = int(input("1 = garer votre voiture / 2: récupérer votre voiture: "))
    while choix_du_client > 2 or choix_du_client < 1:
        choix_du_client = int(input("choix incorrect, 1 ou 2 "))
    if choix_du_client == 1:
        emplacement_pour_garer = int(input("Emplacement souhaité :  ")) - 1
        #gestion des erreurs
        while emplacement_pour_garer > len(emplacements):
            emplacement_pour_garer = int(input("Nous avons 27 places maximum ! :  ")) - 1
        while emplacements[emplacement_pour_garer] == VOITURE_GARE:
            emplacement_pour_garer = int(
                input("Desole, l'emplacement est deja prit !!!!! Selectionnez un autre : ")) - 1

        generate_key_dict = str(emplacement_pour_garer + 1) + "-" + str(etage)
        #on ajoute au dictionnaire le passcode generer avec comme clé l'emplacement selectionner
        memoire_passcodes.update({generate_key_dict: generate_passcode()})
        emplacements[emplacement_pour_garer] = VOITURE_GARE
        print(f"Voiture Garé. VOTRE PASSCODE : {memoire_passcodes[generate_key_dict]} // RETENEZ LE BIEN !")

    elif choix_du_client == 2:
        emplacement_pour_reprendre = int(input("Emplacement de votre voiture : ")) - 1
        passcode_client = input("ENTREZ VOTRE PASSCODE : ")
        while emplacement_pour_reprendre > len(emplacements):
            emplacement_pour_reprendre = int(input("Nous avons 27 places maximum ! :  ")) - 1
        if passcode_client == memoire_passcodes[emplacement_pour_reprendre+1]:
            emplacements[emplacement_pour_reprendre] = EMPLACEMENT_LIBRE
            #on supprimer du dictionnaire le passcode
            memoire_passcodes.pop(emplacement_pour_reprendre+1)
            print("vous pouvez reprendre votre voiture")
        else:
            print("mauvais passcode, revenez plus tard")
    time.sleep(2)
    affiche_emplacement(emplacements, etage)
    print(memoire_passcodes)


def main():
    while True:
        print("Bienvenue au parking STORUSIEN")
        ask_etage = int(input("Bonjour, a quelle étage souhaitez vous Garer/Récuperer votre voiture ?? : "))
        try:
            print("Vous êtes a l'etage", ask_etage, "que souhaitez vous faire ?")
            gestion_des_places(PARKING_1[ask_etage - 1], ask_etage)
            print("A la prochaine !")
        except IndexError:
            print("Nous avons 3 étage !")


if __name__ == "__main__":
    main()
