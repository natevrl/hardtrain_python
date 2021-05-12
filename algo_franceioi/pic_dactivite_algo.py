nb_personnes = int(input("nombre de personnes : "))
nb_simultane = []
nb_max = 0

for personne in range(nb_personnes*2):
    arrivee_depart = int(input())
    if arrivee_depart > 0:
        nb_simultane.append(arrivee_depart)
    else:
        nb_simultane.remove(arrivee_depart - (arrivee_depart*2))
    if len(nb_simultane) > nb_max:
        nb_max = len(nb_simultane)

print(nb_max)

