#! /usr/bin/env python3
# coding: utf-8

nb_membres = int(input())
poid_total_equipe2 = 0
poid_total_equipe1 = 0

for poid_par_joueur in range(1, nb_membres*2 + 1):
	if (poid_par_joueur % 2) == 0:
		print("ce chiffre est pair")
		get_poid_equipe2 = int(input())
		poid_total_equipe2 += get_poid_equipe2
	else:
		print("ce chiffre in IMPAIR")
		get_poid_equipe1 = int(input())
		poid_total_equipe1 += get_poid_equipe1

if poid_total_equipe2 > poid_total_equipe1:
	print("L'équipe 2 a un avantage")

else: 
	print("L'équipe 1 a un avantage")

print("Poids total pour l'équipe 2 :", poid_total_equipe2)
print("Poids total pour l'équipe 1 :", poid_total_equipe1)

