plus_petit_x = int(input())
plus_grand_x = int(input())
plus_petit_y = int(input())
plus_grand_y = int(input())
nombre_maisons = int(input())

maison_dans_la_zone = 0


for maison in range(nombre_maisons):
	x = int(input())
	y = int(input())
	if x >= plus_petit_x and x <= plus_grand_x:
		if y >= plus_petit_y and y <= plus_grand_y:
			maison_dans_la_zone += 1


print(maison_dans_la_zone)