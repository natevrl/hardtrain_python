saisir_un_mois = int(input())
nombre_de_jours = 0

if ( (saisir_un_mois >= 1) and (saisir_un_mois <= 3) ) or ( (saisir_un_mois >= 7) and (saisir_un_mois <= 9) ):
	nombre_de_jours = 30
elif ( (saisir_un_mois >= 4) and (saisir_un_mois <= 6) ) or (saisir_un_mois == 10):
	nombre_de_jours = 31
else:
	nombre_de_jours = 29

print(nombre_de_jours)