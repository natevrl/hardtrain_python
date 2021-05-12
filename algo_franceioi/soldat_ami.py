entree_soldat_1 = int(input())
sortie_soldat_1 = int(input())
entree_soldat_2 = int(input())
sortie_soldat_2 = int(input())

list_soldat_1 = []
list_soldat_2 = []

for heure in range(sortie_soldat_1+1):
    if heure >= entree_soldat_1:
        list_soldat_1.append(heure)
for heure in range(sortie_soldat_2+1):
    if heure >= entree_soldat_2:
        list_soldat_2.append(heure)


for numb in list_soldat_1:
    if numb in list_soldat_2:
        print("Amis")
        break 
else:
    print("Pas amis")
