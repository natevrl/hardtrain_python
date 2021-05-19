juste_prix = int(input())
run = True
essai = 0

while run:
    proposition = int(input())
    if proposition > juste_prix:
        print("c'est moins")
    elif proposition < juste_prix:
        print("c'est plus")
    else:
        run = False
    essai += 1

print(f"Nombre d'essais nécessaires \n{essai}")
