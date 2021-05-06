# exo France IOI : Niveau 01 Calcul des denivelees


nb_montees_descentes = int(input())
total_montee = 0
total_descente = 0

for monteeDescente in range(nb_montees_descentes):
	altitude = int(input())
	if altitude >= 0:
		total_montee += altitude
	else:
		total_descente += altitude

print(total_montee)
print(total_descente-(total_descente*2))
