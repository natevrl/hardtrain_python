#! /usr/bin/env python3
# coding: utf-8

distance_deja_parcourue = int(input())
nb_villages = int(input())
village_atteignable = 0


for village in range(nb_villages):
	distance_du_village = int(input())
	print(distance_du_village - distance_deja_parcourue)
	if distance_du_village - distance_deja_parcourue < 50 and distance_du_village - distance_deja_parcourue > -50:
		print("True")
		village_atteignable += 1
	else :
		print("False")

print(village_atteignable)