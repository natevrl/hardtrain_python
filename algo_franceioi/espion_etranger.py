nombre_personne = int(input())
jour_min = int(input())
jour_max = int(input())
potentiel_espion = 0

for personne in range(nombre_personne):
	jour_entree = int(input())
	if (jour_entree >= jour_min) and (jour_entree <= jour_max):
		potentiel_espion += 1
	else:
		continue


print(potentiel_espion)