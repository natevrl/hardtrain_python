nombre_de_marchand = int(input())
prix_moins_cher = 1000*1000


for marchand in range(1,nombre_de_marchand + 1):
	prix_galette = int(input())
	if prix_galette <= prix_moins_cher:
		prix_moins_cher = prix_galette
		index = marchand



print(index)

