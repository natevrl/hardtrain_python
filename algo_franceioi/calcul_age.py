age = int(input())
poids_bagage = int(input())
prix_a_payer = 0

if age == 60:
	prix_a_payer = 0
elif age < 10:
	prix_a_payer = 5
elif age > 10 and age != 60:
	if poids_bagage >= 20:
		prix_a_payer = 40
	else:
		prix_a_payer = 30
print(prix_a_payer)