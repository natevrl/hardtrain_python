nb_jetons = int(input())


def zone_de_couleurs(abs, ord):
    if (0 <= abs <= 90) and (0 <= ord <= 70):
        zone_rouge = (60 <= ord <= 70) and ((abs >= 15 and (abs <= 45)) or ((abs >= 60) and (abs <= 85)))
        zone_bleue = (10 <= ord <= 55) and (10 <= abs <= 85) and not \
                     ((25 <= abs <= 50 ) and (20 <= ord <= 45))
        if zone_bleue:
            print("Dans une zone bleue")
        elif zone_rouge:
            print("Dans une zone rouge ")
        elif not zone_rouge and not zone_bleue:
            print("Dans une zone jaune")
        else:
            print("sa marche pas")
    else:
        print("En dehors de la feuille")


for jeton in range(nb_jetons):
    zone_de_couleurs(int(input()), int(input()))
