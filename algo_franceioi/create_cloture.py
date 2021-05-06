nombre_maisons = int(input())
plus_grand_x = 0
plus_petit_x = 1000000
plus_grand_y = 0
plus_petit_y = 1000000


for maison in range(nombre_maisons):
	x = int(input())
	y = int(input())
	if x < plus_petit_x:
		plus_petit_x = x
	elif x > plus_grand_x:
		plus_grand_x = x
	if y < plus_petit_y:
		plus_petit_y = y
	elif y > plus_grand_y:
		plus_grand_y = y



ligne_des_abscisse = plus_grand_x - plus_petit_x
ligne_des_ordonnee = plus_grand_y - plus_petit_y

perimetre = (ligne_des_abscisse+ligne_des_ordonnee)*2
if perimetre < 0:
	perimetre = 0

print(perimetre)