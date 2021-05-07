from datetime import datetime, timedelta
import time
import math

MACHINE_CAPACITE = 8  # kg d'habits pour 1 machine
TOUR_PAR_MINUTE = 1400  # tour par minutes
TEMPS_LAVAGE_COMPLET = 35  # un lavage complet en minute
multiples = [x for x in range(1, 1000) if x % MACHINE_CAPACITE == 0]


# Gestion du temps ---->
def affiche_temps_actuel(temps):
    return temps.strftime("%H:%M")


def ajoute_35_minutes(temps_actuel):
    temps_apres_machine = temps_actuel + timedelta(minutes=TEMPS_LAVAGE_COMPLET)
    return temps_apres_machine.strftime("%H:%M")


# def nombre_machine(quantite_dhabits):
#     nb_machine = 1
#     for machine in multiples:
#         if quantite_dhabits <= machine:
#             break
#         nb_machine += 1
#     return nb_machine

def demarrer_machine(kg_habits, nb_machine):
    temps_actuel = datetime.now()
    for machine in range(nb_machine):
        print(f"Machine n°{machine+1} : Demarrage...")
        time.sleep(2)
        print(f"Il est: {affiche_temps_actuel(temps_actuel)}, votre machine sera terminée à : {ajoute_35_minutes(temps_actuel)} ")
        nb_machine -= 1
        if nb_machine == 0:
            reste_dernier_tour = int(kg_habits % MACHINE_CAPACITE)
            print(f"Dernière machine ! Plus que {reste_dernier_tour} KG à laver, courage !")
            time.sleep(2)
        temps_actuel += timedelta(minutes=TEMPS_LAVAGE_COMPLET)






quantite_dhabits_kg = 38
reste_dernier_tour = int(quantite_dhabits_kg % MACHINE_CAPACITE)
nb_machines = math.ceil(quantite_dhabits_kg / MACHINE_CAPACITE)



# nb_machines = nombre_machine(quantite_dhabits_kg)
# int(input("Quelle quantité souhaitez-vous laver (kg) ?"))
comsommation_eau = nb_machines * 60

def main():
    print(f"Pour {quantite_dhabits_kg} KG d'habits, il vous faudra faire: {nb_machines} machine")
    time.sleep(1)
    demarrer_machine(quantite_dhabits_kg, nb_machines)
    print(f"\nVotre consommation deau total est de : {comsommation_eau}L")
    print(f"Pour ces {nb_machines} lavages, votre machine à effectuer {(TOUR_PAR_MINUTE*TEMPS_LAVAGE_COMPLET)*nb_machines} ")

    pass

if __name__ == "__main__":
    main()

