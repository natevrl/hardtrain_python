max_pierres = int(input())
etage = 0
construction = 0
somme_pierre = 0

while somme_pierre < max_pierres:
    construction += etage + (etage + 1)
    somme_pierre += construction
    etage += 1
    if somme_pierre > max_pierres:
        somme_pierre -= construction
        etage -= 1
        break

print(etage)
print(somme_pierre)



